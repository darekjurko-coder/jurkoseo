# JURKO AI — audyt katalogów PDF, 24 listopada 2026

**STATUS: NIEUKOŃCZONE.**

## Drive
Ponowne wyszukanie PDF dla 11 marek oraz wyłączenie cenników i innych marek: Atlas Concorde 33, Casalgrande Padana 9, CEDIR 1, Century 19, Ceramica Cielo 13, Ceramica Vogue 13, Cercom 23, Cerdomus 36, CIPA Gres 4, CIR 25, Cotto Petrus 61. Razem **237**, wszystkie o niezerowym rozmiarze. Surowe wyniki Cercom 24 (wyłączono CERCOM-CENNIK-2019.pdf), Cerdomus 37 (wyłączono PDF Listino Price List 2026_Cerdomus.pdf), CIR 27 (wyłączono dwa pliki Durstone Ciro). Liczba obejmuje znane kopie, nie liczbę unikatowych katalogów.

## Nowe ustalenia — Ceramica Cielo
Sprawdzono folder producenta https://drive.google.com/drive/folders/1J2EunSOSGHILLnl7npUVbpzQDFOQ2Mr0 i wszystkie 11 podfolderów: każdy zawiera jeden PDF, a katalog główny dwa. Oficjalny wykaz https://www.ceramicacielo.it/fr/download/cataloghi wymienia te same tytuły (w wersji wyników z News 2026; starszy odczyt strony zawiera 12 tytułów). Nie stwierdzono brakującego tytułu w tym wykazie.

Dodano dwa brakujące wpisy źródłowe do catalogues.csv, bez pobierania ponownie plików:
- General Book: https://img.ceramicacielo.it/download_cataloghi/catalogo_generale.pdf — istniejący plik https://drive.google.com/file/d/1KsMbq3Lxh7mVSWv-usscRs8ITsYKvVSw/view, 35 132 140 bajtów. Oficjalny serwer zgłosił długość dokładnie 35 132 140 bajtów, odczyt źródła przez przeglądarkę ograniczony limitem wielkości. Odczyt tekstu kopii Drive: 280 927 znaków, właściwy tytuł i treść.
- Ceramic Design Book: https://img.ceramicacielo.it/download_cataloghi/ceramic_design_book.pdf — istniejący plik https://drive.google.com/file/d/1ZE4yy9WlhkqpfbQ-7cwXRCMLzxJyKK1t/view, 7 597 860 bajtów. Oficjalny PDF (147 stron, wydanie 2019) otwarty, sprawdzona okładka i tekst, zgodny z początkiem tekstu i spisem treści kopii Drive (135 491 znaków tekstu). 
Oba wpisy dokumentują źródło i dopasowanie, **nie pełną zgodność SHA-256**. Cielo ma teraz 13/13 zapisanych PDF z wpisem źródłowym. Rejestr ogółem 158 unikatowych wierszy danych (wcześniej 156), 79 egzemplarzy bez osobnego wpisu. Commit rejestru 35e5ef9f04bfcb0d3ef7aed68f84cdc8012142a5.

## Pozostałe
Cotto Petrus: ponownie potwierdzono puste foldery Spaccone, Rangers OUT i Galaxy OUT. Nie rozstrzygnięto zawartości ZIP. Century: oficjalna strona https://www.century-ceramica.it/download/ nadal wymienia Outdoor, lecz odczyt strony nie udostępnia bezpośredniego linku do PDF. Nie potwierdzono nowego unikatowego pliku do importu.
Make 9983437: inactive, połączenie ok, incompleteExecutions=0, ostatnie udane wykonanie 18.11.2026 08:17:51 UTC; brak nowszych wykonań. Filtr MIME PDF, brak kontroli duplikatów.
Nie dodawano, nie nadpisywano, nie przenoszono ani nie usuwano plików Drive. Nadal otwarte wcześniejsze kwestie nieprawidłowego przypisania marek, co najmniej 7 nadmiarowych kopii, brakujących źródeł oraz pełnej weryfikacji oficjalnych bibliotek i integralności wszystkich plików. Nie ogłaszać zakończenia.
