import csv, hashlib, io, os, pathlib, time, sys, re
from urllib.parse import urlparse, urljoin
import requests
from pypdf import PdfReader
from google.oauth2.credentials import Credentials
from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

HERE=pathlib.Path(__file__).parent
FIELDS=['producent','kolekcja','rodzaj_katalogu','adres_zrodlowy','link_PDF_Drive_lub_sciezka_lokalna','liczba_stron','rozmiar_bajty','sha256','wynik_weryfikacji','status','przyczyna_bledu']
MAX_SIZE=100*1024*1024

def record(rows):
    with (HERE/'report.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS)
        w.writeheader();w.writerows(rows)

def download(url):
    for retry in range(3):
        try:
            for _ in range(6):
                p=urlparse(url)
                if p.scheme!='https' or not p.hostname or p.username or p.password:
                    raise ValueError('Wymagany publiczny HTTPS')
                with requests.get(url,timeout=(8,20),stream=True,allow_redirects=False) as response:
                    if response.status_code in (301,302,303,307,308):
                        url=urljoin(url,response.headers['Location'])
                        continue
                    if response.status_code in (401,403,404):
                        raise ValueError('HTTP '+str(response.status_code)+' — bez ponowienia')
                    response.raise_for_status()
                    stream=io.BytesIO()
                    for chunk in response.iter_content(65536):
                        stream.write(chunk)
                        if stream.tell()>MAX_SIZE:
                            raise ValueError('Przekroczono 100 MB')
                    raw=stream.getvalue()
                    if not raw.startswith(b'%PDF-'):
                        raise ValueError('Brak sygnatury PDF; odrzucono HTML lub inny plik')
                    return raw
            raise ValueError('Za dużo przekierowań')
        except (requests.ConnectionError, requests.Timeout, requests.HTTPError):
            if retry==2: raise
            time.sleep(2**retry)

def client():
    keys=['GOOGLE_CLIENT_ID','GOOGLE_CLIENT_SECRET','GOOGLE_REFRESH_TOKEN']
    if not all(os.getenv(x) for x in keys):
        return None
    cred=Credentials(token=None,refresh_token=os.environ['GOOGLE_REFRESH_TOKEN'],
      token_uri='https://oauth2.googleapis.com/token',client_id=os.environ['GOOGLE_CLIENT_ID'],
      client_secret=os.environ['GOOGLE_CLIENT_SECRET'],scopes=['https://www.googleapis.com/auth/drive'])
    cred.refresh(Request())
    return build('drive','v3',credentials=cred,cache_discovery=False)

def items(api,folder):
    out=[];token=None
    while True:
        response=api.files().list(q="'"+folder+"' in parents and trashed=false",
         fields='nextPageToken,files(id,name,md5Checksum,size)',pageToken=token,pageSize=1000).execute()
        out.extend(response.get('files',[]))
        token=response.get('nextPageToken')
        if not token: return out

def main():
    with (HERE/'catalogues.csv').open(encoding='utf-8-sig',newline='') as f:
        entries=list(csv.DictReader(f))
    additional=HERE/'discovered.csv'
    if additional.exists():
        with additional.open(encoding='utf-8-sig',newline='') as f:
            discovered=list(csv.DictReader(f))
            for entry in discovered:
                entry['review_only']='1'
            entries.extend(discovered)
    unique={}
    for e in entries:
        key=e['url'].strip()
        if key not in unique or (unique[key]['kind']=='unclassified' and e['kind']!='unclassified'):
            unique[key]=e
    entries=list(unique.values())
    rows=[]
    try: api=client()
    except RefreshError as exc:
        message=str(exc).lower()
        code=next((k for k in ('invalid_grant','invalid_client','unauthorized_client','access_denied') if k in message),'unknown_refresh_failure')
        print('Google Drive authentication failed: '+code,flush=True)
        print('Verify OAuth client ID/secret pairing, refresh token, OAuth app testing expiry and consent screen.',flush=True)
        sys.exit(2)
    except Exception as exc:
        print('Google Drive authentication failed: '+exc.__class__.__name__,flush=True)
        sys.exit(2)
    failures=0
    for item in entries:
        r=dict.fromkeys(FIELDS,'')
        r.update(producent=item['manufacturer'],kolekcja=item['collection'],
          rodzaj_katalogu=item['kind'],adres_zrodlowy=item['url'],status='BLAD')
        try:
            if item.get('review_only') == '1':
                r['status']='DO_PRZYPISANIA'
                r['przyczyna_bledu']='Automatyczne odkrycie wymaga potwierdzenia nazwy kolekcji, rodzaju i folderu; bez przesylania na Drive'
                continue
            if item['kind'] not in ('general','collection','technical') or (item['kind'] in ('collection','technical') and not item['collection'].strip()):
                r['status']='DO_PRZYPISANIA'
                r['przyczyna_bledu']='Link wykryty, brak potwierdzonego rodzaju katalogu i kolekcji; pominięto zapis'
                continue
            folder=item['folder_id'].strip();filename=item['filename'].strip()
            if not folder or not filename.lower().endswith('.pdf'):
                raise ValueError('Nieprawidłowy folder lub nazwa PDF')
            current=items(api,folder) if api else []
            if any(f['name']==filename for f in current):
                r.update(status='DUPLIKAT_NAZWY',przyczyna_bledu='Plik już istnieje; bez nadpisywania')
            else:
                raw=download(item['url'])
                sha=hashlib.sha256(raw).hexdigest()
                n=len(PdfReader(io.BytesIO(raw),strict=True).pages)
                if n<1: raise ValueError('Brak stron')
                r.update(liczba_stron=n,rozmiar_bajty=len(raw),sha256=sha,wynik_weryfikacji='Sygnatura, parser i SHA-256 OK')
                md5=hashlib.md5(raw).hexdigest()
                same=next((f for f in current if f.get('md5Checksum')==md5),None)
                if same:
                    r.update(status='DUPLIKAT_TRESCI',link_PDF_Drive_lub_sciezka_lokalna='https://drive.google.com/file/d/'+same['id']+'/view')
                elif api is None:
                    dest=HERE/'verified';dest.mkdir(exist_ok=True)
                    path=dest/(sha+'.pdf');path.write_bytes(raw)
                    r.update(status='LOKALNY',link_PDF_Drive_lub_sciezka_lokalna=str(path))
                else:
                    metadata={'name':filename,'parents':[folder],'mimeType':'application/pdf',
                      'description':'SHA256='+sha+'; pages='+str(n)+'; source='+item['url']}
                    media=MediaIoBaseUpload(io.BytesIO(raw),mimetype='application/pdf')
                    up=api.files().create(body=metadata,media_body=media,
                      fields='id',supportsAllDrives=True).execute()
                    check=api.files().get(fileId=up['id'],supportsAllDrives=True,
                      fields='id,mimeType,md5Checksum,size,parents').execute()
                    if check.get('md5Checksum')!=md5 or int(check.get('size',0))!=len(raw) or folder not in check.get('parents',[]) or check.get('mimeType')!='application/pdf':
                        raise ValueError('Błąd kontroli pliku po zapisie ID='+up['id'])
                    r.update(status='DRIVE_OK',link_PDF_Drive_lub_sciezka_lokalna='https://drive.google.com/file/d/'+up['id']+'/view',wynik_weryfikacji='PDF+SHA256; Drive MD5/size/folder OK')
        except Exception as exc:
            reason=str(exc)
            reason=re.sub(r'(?i)(access_token|refresh_token|client_secret|authorization|api_key)=([^\\s&]+)',r'\\1=[REDACTED]',reason)
            r['przyczyna_bledu']=(exc.__class__.__name__+': '+reason)[:350]
            failures+=1
        finally:
            rows.append(r);record(rows)
            print(r['producent'],r['kolekcja'],r['status'],r['przyczyna_bledu'],flush=True)
    print('RESULT:',len(rows),'checked;',failures,'failed',flush=True)
    # Unavailable supplier catalogues are recorded but do not fail the entire batch.
    # Keep the CSV as the authoritative per-file outcome.
    if failures:
        print('PARTIAL_IMPORT: unavailable catalogues listed in report.csv',flush=True)

if __name__=='__main__': main()
