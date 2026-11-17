# JURKO AI — audyt importu katalogów PDF, 2026-11-17

**Stan: NIEUKOŃCZONE.** Brak podstaw do powiadomienia o pełnym ukończeniu importu. Nie uruchamiano Make i nie dodawano, nie nadpisywano ani nie usuwano plików PDF na Drive.

## Weryfikacja Google Drive (17.11.2026)

Ponownie wykonano 11 zapytań Drive filtrowanych na `mimeType='application/pdf'` i prefiksy nazw; po stronie klienta zastosowano ścisłe `startsWith` (zapytanie Google Drive z `contains` może objąć niepowiązane nazwy, szczególnie przy `CIR_`). Żadne zapytanie nie miało następnej strony wyników.

| Producent | PDF na Drive |
| --- | ---: |
| Atlas Concorde | 33 |
| Casalgrande Padana | 9 |
| CEDIR | 1 |
| Century | 19 |
| Ceramica Cielo | 13 |
| Ceramica Vogue | 13 |
| Cercom | 23 |
| Cerdomus | 36 |
| CIPA Gres | 3 |
| CIR | 25 |
| Cotto Petrus | 61 |
| **Razem** | **236** |

**0 nowych plików** w tych 11 zestawach w dniach 16–17 listopada, **0 rekordów o rozmiarze zerowym**. Nie jest to dowód pełnej integralności ani kompletności bibliotek.

## Nowe ustalenie: Century Organizer 2025 jest prawdopodobnie już na Drive

Oficjalny katalog [Century Organizer 2025](https://www.century-ceramica.it/wp-content/uploads/2025/04/Catalogo_generale_interattivo_Century_0525.pdf) ma pierwszą stronę oznaczoną `organizer25CENTURY`; na Drive istnieje `CENTURY_CATALOGO_GENERALE_2025.pdf` (ID `1a_3yvwPDKbCAlAxU_JqGRdFOskJ0F-GN`) o tej samej identyfikacji w wyodrębnionej treści oraz rozmiarze **14 079 040 bajtów**. Zewnętrzny podgląd źródła również raportował **14 079 040 bajtów**. Ustalenie silnie wskazuje na tę samą publikację, więc **nie wolno tworzyć drugiej kopii**. Nie wykonano bezpośredniego porównania SHA-256 obu strumieni binarnych, zatem formalna identyczność binarna nadal nie została udowodniona.

Dodano do GitHub `pdf-import/catalogues.csv` pojedynczy wpis proweniencji dla **istniejącego** pliku Century (kategoria `Organizer 2025`, typ `general`, oficjalny URL, istniejący ID folderu i nazwa). Commit: `3faee0eeb0d7ed15f5f0997f27ddacdcf0606609`. Rejestr wzrósł z **122 do 123 rekordów**, a następnie do **126** po dopisaniu trzech istniejących PDF Cercom. Nowy wpis weryfikowano ponownie względem pliku i folderu na Drive.

**Stan ewidencji:** z 236 PDF **126 rekordów jest wpisanych do rejestru** i mają zgodność nazwy i folderu Drive; **110 pozostałych PDF** nie ma jeszcze odpowiednika w CSV. Łącznie 126/126 wpisów wskazuje jednoznaczne pliki zgodnie z nazwą i rodzicem (122 wcześniej zweryfikowane 15.11, 4 dopisane i sprawdzone 17.11). Sama zgodność metadanych nie stanowi kontroli wszystkich hashy.

**Century Outdoor** wciąż jest wymieniony na [oficjalnej stronie Download](https://www.century-ceramica.it/download/), ale nie udało się ustalić odrębnego, zweryfikowanego URL bezpośredniego PDF. `Outdoor.pdf` odnaleziony uprzednio dotyczy TAU Ceramica (patrz audyt 14.11) i nie wolno go przypisywać Century.

## Dopisane trzy oficjalne źródła Cercom (17.11)

Na [oficjalnej stronie pobierania Cercom](https://www.cercomceramiche.it/download/) bezpośrednio potwierdzono linki do trzech katalogów i zestawiono je z nazwami oraz rozpoznawalną treścią istniejących na Drive plików:
- **Workbook Cercom 26**: [źródło](https://www.cercomceramiche.it/wp-content/uploads/WORKBOOK-CERCOM-2026.pdf) → `CERCOM_WORKBOOK_CERCOM_26.pdf`, Drive ID `1S-KudhjdTtmZeKxajpOUvTgXVdniNN0e`, 14 093 772 bajty.
- **Adobe**: [źródło](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-ADOBE.pdf) → `CERCOM_BOOK_ADOBE.pdf` w folderze kolekcji, Drive ID `1cWELyFNTIMHgUB57EuUBI7C1VLT9iwKc`, 14 646 949 bajtów. Druga kopia Adobe pozostaje niezmieniona i niezarejestrowana.
- **Katalog 2 CM 2024**: [źródło](https://www.cercomceramiche.it/wp-content/uploads/Cercom_catalogo_2CM_PagDoppie.pdf) → `CERCOM_CERCOM_CATALOGO_GENERALE_2_CM_2024.pdf`, Drive ID `1qoResfolUa09vvP0lqc_iUkD1Cinr2bX`, 8 309 334 bajty. Oficjalny PDF zweryfikowano wizualnie na pierwszej stronie, a tekst istniejącej kopii Drive odpowiada jej początkowi.

Wpisy dopisano do rejestru `pdf-import/catalogues.csv` bez nowych uploadów: commit `be58c600e17965bc2e56c835efcac1f858a8c724`. Wszystkie 3 nowe pozycje ponownie sprawdzono w Drive — właściwa nazwa, folder i niezerowy rozmiar. **Nie prowadzono porównania binarnych SHA-256** między serwerem producenta i Drive.

## Czytelność przykładowych PDF (17.11)

Przez połączenie Drive odczytano i rozpoznano tekst z siedmiu istniejących plików (nie oznacza to pełnego sprawdzenia wszystkich stron):
- Century `CENTURY_CATALOGO_GENERALE_2025.pdf`: `organizer25`, spis treści, 14 079 040 bajtów.
- CEDIR `CEDIR_GENERAL_ARCHIVAL_CATALOGUE.pdf`: tekst katalogowy i liczne wzmianki CEDIR; zawiera również dane słoweńskiego dystrybutora Merilly d.o.o., wobec czego pochodzenie bezpośrednio od producenta wymaga osobnej oceny.
- Ceramica Vogue `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf`: identyfikuje System i Ceramica Vogue.
- Cercom `CERCOM_BOOK_ADOBE.pdf`: opis kolekcji Adobe, wzmianka Cercom.
- Cercom `CERCOM_WORKBOOK_CERCOM_26.pdf`: katalog `archivio materiali 2026`, wzmianki Cercom.
- CIPA Gres `CIPA_GRES_COLOURSTYLE_2025.pdf`: identyfikuje Colourstyle / Hi-Tech / CIPA Gres.
- Cotto Petrus `COTTO_PETRUS_GENERAL_ED12_OFFICIAL_2026.pdf`: `CATALOGO GENERALE .12`, spis kolekcji, w tym Galaxy.

**Trzy foldery Cotto Petrus nadal puste** (bezpośredni odczyt folderów): Spaccone `1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`, Rangers OUT `1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`, Galaxy OUT `12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`. Na [oficjalnej stronie Cotto Petrus](https://www.cottopetrus.it/download/s5cb0a778) linki Spaccone i Rangers OUT prowadzą do **ZIP**, których narzędzie przeglądarkowe nie potrafi odczytać (`application/zip`), więc nie wiadomo, czy archiwa zawierają PDF. Brak potwierdzonego odrębnego PDF Galaxy OUT. Część treści jest w już zapisanym katalogu generalnym, edycja 12.

W spisie Drive są dwa razy nazwy `CERCOM_BOOK_ADOBE.pdf` i `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf`. Poprzedni audyt 12.11 wykrył trzy grupy równych SHA-256 i pięć nadmiarowych kopii, ale **17.11 nie wykonywano pełnego SHA-256**; nie usuwano żadnych pozycji.

## Stan Make (17.11)

Scenariusz `9983437` (*JURKO Armonie — import PDF na żądanie*): **inactive**, Google Drive connection **ok**, incomplete executions **0**. W historii od 12.11 pozostaje tylko sukces z **13.11.2026 08:59:58 UTC**; nie ma późniejszych wykonań. Moduły: pobierz plik HTTP, przepuść gdy nagłówek Content-Type zawiera PDF, zapisz na Drive. **Brak wbudowanej kontroli duplikatów**, dlatego scenariusza nie aktywowano bez pewnego nowego źródła i kontrolowanego miejsca docelowego.

## Braki blokujące zakończenie

1. Pełne, aktualne porównanie bibliotek **wszystkich 11** producentów do oficjalnych wykazów oraz udokumentowanie niedostępności poszczególnych osobnych plików.
2. Wyjaśnienie Century Outdoor i zawartości ZIP dla Spaccone / Rangers OUT.
3. Uzupełnienie proweniencji **110 niezarejestrowanych rekordów**, zwłaszcza CEDIR, Ceramica Vogue i CIPA Gres (wciąż 0 wpisów w CSV). Cercom ma już 3 udokumentowane rekordy, ale 20 pozostałych nie ma wpisów.
4. Sprawdzenie zawartości wszystkich PDF, ich przypisania do odpowiednich kolekcji, pełnych hashy i ewentualnych duplikatów.

**Wynik: import wciąż nieukończony.** Dzisiaj uporządkowano ewidencję istniejącego Century Organizer oraz trzech katalogów Cercom bez duplikowania PDF; na Google Drive liczba pozostaje 236.
