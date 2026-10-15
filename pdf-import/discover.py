import csv, pathlib, re
from urllib.parse import urljoin, urlparse, urldefrag
import requests
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).parent
TIMEOUT=(6,12)
MAX_PAGES=65
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
    results=[];issues=[];seen_pdf=set()
    with (ROOT/'sources.csv').open(encoding='utf-8-sig',newline='') as f: sources=list(csv.DictReader(f))
    with requests.Session() as s:
      s.headers.update(HEADERS)
      for source in sources:
        base=source['landing_url'];queue=[(base,0)];seen=set();page_count=0
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
          for a in html.select('a[href]'):
            link=urljoin(page,a.get('href','').strip())
            link=urldefrag(link).url
            if not safe(link,base): continue
            title=' '.join(a.stripped_strings).strip()[:130]
            if re.search(r'\\.pdf(?:$|\\?)',link,re.I):
              if link in seen_pdf:continue
              seen_pdf.add(link)
              parent=a.find_parent(['section','article','div'])
              heading=parent.find(['h1','h2','h3','h4']) if parent else None
              label=(heading.get_text(' ',strip=True) if heading else title).strip()[:100]
              technical=bool(TECHNICAL.search(label+' '+title+' '+link))
              generic=bool(re.search(r'generale|general|workbook|design book|outdoor book',label+' '+title,re.I))
              kind='technical' if technical else 'general' if generic else 'unclassified'
              # Do not guess that a PDF belongs to a collection from its filename alone.
              slug=re.sub(r'[^A-Z0-9]+','_',title.upper()).strip('_')[:45] or 'DOCUMENT'
              results.append({'manufacturer':source['manufacturer'],'collection':'','kind':kind,
                'url':link,'folder_id':source['folder_id'],
                'filename':re.sub(r'[^A-Z0-9]+','_',source['manufacturer'].upper()).strip('_')+'_'+slug+'.pdf'})
            elif depth<1 and LINK_TERMS.search(title+' '+link) and link not in seen and len(queue)<400:
              queue.append((link,depth+1))
        print(source['manufacturer']+': visited '+str(page_count)+' pages',flush=True)
    with (ROOT/'discovered.csv').open('w',encoding='utf-8-sig',newline='') as f:
      w=csv.DictWriter(f,fieldnames=['manufacturer','collection','kind','url','folder_id','filename'])
      w.writeheader();w.writerows(results)
    with (ROOT/'discovery_errors.csv').open('w',encoding='utf-8-sig',newline='') as f:
      w=csv.writer(f);w.writerow(['manufacturer','page','error']);w.writerows(issues)
    print('Discovered PDF links:',len(results),'Page errors:',len(issues),flush=True)

if __name__=='__main__':main()
