# JURKO AI — audyt importu PDF, 2026-11-18

**Status: NIEUKOŃCZONE.** Import nie został uznany za kompletny; nie wysyłać powiadomienia o zakończeniu.

## Nowy, zweryfikowany import (18.11.2026)
- Producent: **CIPA Gres**, publikacja **COLOURSTYLE 10X10** (osobna publikacja produktowa, różna od dużego katalogu Colourstyle).
- Oficjalny bezpośredni URL PDF producenta: https://www.cipagres.it/img/cms/C%20A%20T%20A%20L%20O%20G%20H%20I/CIPA%20GRES_10x10_COLOURSTYLE.pdf
- Przed importem folder producenta zawierał tylko 3 inne katalogi; weryfikacja po nazwie i wyszukiwanie Drive nie wykazały już zapisanego katalogu 10x10.
- Wykonano pojedynczy przebieg scenariusza Make `9983437`, execution ID `970bca26ae1a4445aae37cf2057619a7`, **success**. Scenariusz włączono tylko na czas kontrolowanego importu i **ponownie wyłączono**.
- Plik: `CIPA_GRES_COLOURSTYLE_10X10_OFFICIAL.pdf`, ID `1uscQLPKXDAJjA1HGKJKXiTyJgWiu45fi`, rozmiar **5 203 685 B**, `application/pdf`.
- Lokalizacja Google Drive (folder **CIPA Gres**): `1OW_ZuHrMvSx8aeoQZ7bfXq9-oWJEZqNX`. Potwierdzono metadane pliku, rodzica, rozmiar i odczyt treści (`COLOURSTYLE 10X10`, format 10×10 cm, charakterystyka produktu). [Plik na Drive](https://drive.google.com/file/d/1uscQLPKXDAJjA1HGKJKXiTyJgWiu45fi/view).
- Nie nadpisano żadnego starego pliku. Nie wykonano porównania binarnego SHA-256 źródła i Drive.

## Uzupełnienie rejestru proweniencji w GitHubie
Dopisano **3** wiersze do `pdf-import/catalogues.csv`:
1. CIPA Gres Hi-Tech (już istniejący PDF) — oficjalny [HI-TECH.pdf](https://www.cipagres.it/img/cms/ULTIMI%20FILE%20CARICATI/HI-TECH.pdf), zgodność tekstu i rodzaju publikacji.
2. CIPA Gres Colourstyle (już istniejący PDF) — oficjalny [COLOURSTYLE.pdf](https://www.cipagres.it/img/cms/ULTIMI%20FILE%20CARICATI/COLOURSTYLE.pdf), zgodność treści i rodzaju publikacji.
3. CIPA Gres Colourstyle 10x10 — dopiero co pobrany oficjalny PDF, wskazany wyżej.

**GitHub commit CSV:** `15fe2e5e7f895fb10d68d0bb2475504e0f81fce7`. Dla dwóch już zapisanych katalogów zgodność źródeł ma charakter **tekstowy**, nie porównano pełnych bajtów i hashy. Nie dodano proweniencji Outdoor ze względu na brak rozstrzygnięcia wersji wydawniczej.

## Stan liczbowy Google Drive — pełne ponowne sprawdzenie 11 prefiksów
Wykonano 11 zapytań Google Drive z filtrem `mimeType = application/pdf` i prefiksami nazw (ścisłe `startsWith` w wynikach). Każde zwróciło wszystkie wyniki bez potrzeby stronicowania.

| Producent | PDF 17.11 | PDF 18.11 |
|---|---:|---:|
| Atlas Concorde | 33 | 33 |
| Casalgrande Padana | 9 | 9 |
| CEDIR | 1 | 1 |
| Century | 19 | 19 |
| Ceramica Cielo | 13 | 13 |
| Ceramica Vogue | 13 | 13 |
| Cercom | 23 | 23 |
| Cerdomus | 36 | 36 |
| CIPA Gres | 3 | **4** |
| CIR | 25 | 25 |
| Cotto Petrus | 61 | 61 |
| **Razem** | **236** | **237** |

- Wszystkie **237** znalezionych PDF-ów mają rozmiar > 0.
- `catalogues.csv` zawiera obecnie **129** wpisów (wcześniej 126). **129/129** wskazuje dokładnie jeden plik o zgodnej nazwie i dokładnie tym folderze docelowym; nie znaleziono uszkodzonych wierszy ani powtórzonych rekordów `filename + folder_id`.
- **108/237** plików nie ma jeszcze indywidualnego wpisu z oficjalnym źródłem w CSV.
- Nadal są **2 pary powtarzających się nazw plików** na Drive: `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf` oraz `CERCOM_BOOK_ADOBE.pdf`. Powtórzenie nazwy nie jest nowym wynikiem porównania binarnego; wcześniejsze audyty zgłaszały również duplikaty SHA-256, których dzisiaj nie przeliczono.

## Sprawdzone braki / ograniczenia
- Foldery **Cotto Petrus Spaccone** (`1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`), **Rangers OUT** (`1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`) i **Galaxy OUT** (`12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`) są wciąż **puste** (bezpośrednie odczyty Drive). Strona producenta [download](https://www.cottopetrus.it/download/s5cb0a778) wymienia Spaccone i Rangers OUT, ale udostępniane ZIP-y pozostają niezweryfikowane; osobnego oficjalnego PDF Galaxy OUT nie potwierdzono.
- Oficjalna [strona pobierania Century](https://www.century-ceramica.it/download/) nadal wymienia **Outdoor**; nie ustalono jednoznacznego, osobnego URL PDF. Nie importowano pliku `Outdoor.pdf` z innego producenta.
- CIPA Gres ma także dostępny na stronie producenta plik `OUTDOOR.pdf`, ale nie potwierdzono, że jest binarnie tą samą **edycją 2025** co istniejący na Drive `CIPA_GRES_OUTDOOR_2025.pdf`; dlatego nie powiązano ich w rejestrze jako pewnej identyczności i nie importowano kolejnej kopii.
- Pełna kontrola SHA-256, spójności wszystkich stron i kompletności względem **aktualnych** oficjalnych bibliotek wszystkich 11 producentów nie jest wykonana.

## Make
Scenariusz `9983437`: ostatni przebieg **success**, po imporcie ponownie **inactive**. Połączenie Google Drive `ok`. Liczba incomplete executions **0**. Scenariusz nie ma samodzielnej ochrony przed duplikatami; każdy przyszły import wymaga wcześniejszego sprawdzenia folderu i nazwy.

**Wniosek:** realny postęp: +1 oryginalny PDF, +3 udokumentowane źródła w CSV, +1 producent z uzupełnionym rejestrem. Całość nadal nieukończona; nie potwierdzać kompletności i nie usuwać istniejących plików.
