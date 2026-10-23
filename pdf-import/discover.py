import csv, pathlib, re
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).parent
TIMEOUT=(5,8)
MAX_PAGES=75
HEADERS={'User-Agent':'JURKO-PDF-Catalogue-Discovery/1.0 (catalogues for internal reference)'}
LINK_TERMS=re.compile(r'catalog|download|scarica|pdf|collection|collezion|prodott|product|book|brochure',re.I)
DOCUMENT_TERMS=re.compile(r'catalog|book|brochure|download|scarica|pdf',re.I)
TECHNICAL=re.compile(r'technic|technical|scheda|certificat|installation|posa',re.I)

def safe(url,base):
    u=urlparse(url)
    b=urlparse(base)
    return u.scheme=='https' and u.hostname and (u.hostname==b.hostname or u.hostname.endswith('.'+b.hostname.lstrip('www.'))) and not u.username and not u.password

def get_page(s,url):
    response=s.get(url,timeout=TIMEOUT,allow_redirects=True)
    response.raise_for_status()
    if not safe(response.url,url):
        raise ValueError('External page redirect')
    if len(response.content)>3_000_000:
        raise ValueError('Page too large')
    if 'html' not in response.headers.get('Content-Type','').lower(): return None
    return BeautifulSoup(response.text,'html.parser')

def main():
    results=[];issues=[]
    collection_folders={}
    with (ROOT/'collection_folders.csv').open(encoding='utf-8-sig',newline='') as f:
      for row in csv.DictReader(f):
        collection_folders.setdefault(row['manufacturer'],[]).append((row['collection'],row['folder_id']))
    for collections in collection_folders.values():
      collections.sort(key=lambda x:len(x[0]),reverse=True)
    with (ROOT/'sources.csv').open(encoding='utf-8-sig',newline='') as f: sources=list(csv.DictReader(f))
    with requests.Session() as s:
      s.headers.update(HEADERS)
      for source in sources:
        base=source['landing_url'];queue=[(base,0)];seen=set();seen_pdf=set();page_count=0
        while queue and page_count<MAX_PAGES:
          page,depth=queue.pop(0)
          page=urldefrag(page).url
          if page in seen or not safe(page,base):continue
          seen.add(page);page_count+=1
          try: html=get_page(s,page)
          except Exception as exc:
            issues.append((source['manufacturer'],page,type(exc).__name__+': '+str(exc)[:180]))
            continue
          if html is None:continue
          heading=html.find('h1')
          page_title=heading.get_text(' ',strip=True) if heading else ''
          match=next(((name,fid) for name,fid in collection_folders.get(source['manufacturer'],[])
            if page_title.casefold()==name.casefold() or page_title.casefold().startswith(name.casefold()+' -')),None)
          for a in html.select('a[href]'):
            link=urljoin(page,a.get('href','').strip())
            link=urldefrag(link).url
            if not safe(link,base): continue
            title=' '.join(a.stripped_strings).strip()[:130]
            if re.search(r'\.pdf(?:$|\?)',link,re.I):
              if link in seen_pdf:continue
              seen_pdf.add(link)
              generic=bool(re.search(r'general|generale|workbook|design.book|outdoor.book',title+' '+link,re.I))
              technical=bool(TECHNICAL.search(title+' '+link))
              if generic:
                kind='general';collection='';folder=source['folder_id']
              elif match and (DOCUMENT_TERMS.search(title+' '+link) or technical):
                kind='technical' if technical else 'collection'
                collection,folder=match
              else:
                kind='unclassified';collection='';folder=source['folder_id']
              base_name=collection+' '+(title or link.rsplit('/',1)[-1])
              slug=re.sub(r'[^A-Z0-9]+','_',base_name.upper()).strip('_')[:75] or 'DOCUMENT'
              maker=re.sub(r'[^A-Z0-9]+','_',source['manufacturer'].upper()).strip('_')
              results.append({'manufacturer':source['manufacturer'],'collection':collection,'kind':kind,
                'url':link,'folder_id':folder,'filename':maker+'_'+slug+'.pdf'})
            elif depth<2 and (LINK_TERMS.search(title+' '+link) or any(title.casefold()==name.casefold() for name,_ in collection_folders.get(source['manufacturer'],[]))) and link not in seen and len(queue)<400:
              queue.append((link,depth+1))
        print(source['manufacturer']+': visited '+str(page_count)+' pages',flush=True)
    with (ROOT/'discovered.csv').open('w',encoding='utf-8-sig',newline='') as f:
      w=csv.DictWriter(f,fieldnames=['manufacturer','collection','kind','url','folder_id','filename'])
      w.writeheader();w.writerows(results)
    with (ROOT/'discovery_errors.csv').open('w',encoding='utf-8-sig',newline='') as f:
      w=csv.writer(f);w.writerow(['manufacturer','page','error']);w.writerows(issues)
    print('Discovered PDF links:',len(results),'Page errors:',len(issues),flush=True)

if __name__=='__main__':main()
