# JURKO AI — audyt importu katalogów PDF, 2026-11-21

**Status: NIEUKOŃCZONE — nie ogłaszać finalnego zakończenia.** Zweryfikowano postęp w Google Drive, GitHub i Make. Żadnego PDF-a nie dodawano, nie usuwano, nie przenoszono ani nie nadpisywano.

## Zestawienie Google Drive

Przeszukano dostępne pliki według prefiksów nazw wszystkich 11 producentów; odfiltrowano pliki innych marek pojawiające się w wyszukiwaniu pełnotekstowym. Porównanie z kontrolą 2026-11-20 nie wykazało nowych zapisów katalogowych. Wszystkie 237 odnalezionych PDF-ów mają dodatnią wielkość.

| Producent | Liczba PDF |
|---|---:|
| Atlas Concorde | 33 |
| Casalgrande Padana | 9 |
| CEDIR | 1 |
| Century | 19 |
| Ceramica Cielo | 13 |
| Ceramica Vogue | 13 |
| Cercom | 23 |
| Cerdomus | 36 |
| CIPA Gres | 4 |
| CIR | 25 |
| Cotto Petrus | 61 |
| **Razem** | **237** |

## Postęp — 19 nowych oficjalnych źródeł Cercom powiązanych z istniejącymi PDF-ami

Na oficjalnej [stronie pobrań Cercom](https://www.cercomceramiche.it/download/) odnaleziono i powiązano 19 nowych pozycji źródłowych z plikami już istniejącymi na Drive. Dla każdej z 19 pozycji sprawdzono **jeden istniejący plik PDF (nazwa i rozmiar), tekst katalogu potwierdzający kolekcję, identyfikator folderu oraz czy folder jest odpowiednią kolekcją Cercom bądź katalogiem głównym producenta.** Linki oficjalnego producenta otwierają PDF; dla plików >10 MB przeglądarka internetowa nie zwraca pełnych bajtów (limit odczytu), co nie oznacza niedostępności u producenta. **Nie obliczano nowych porównań binarnych SHA-256 ze źródłami na tym etapie.**

| Kolekcja | Plik na Drive | Oficjalny PDF producenta | Folder docelowy (ID) | Rozmiar, bajty |
|---|---|---|---|---:|
| Stone Lab | `CERCOM_STONE_LAB.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_Cat_STONE_LAB.pdf) | `1xW1jzdXtqdZ1CzFe-MJkpCDhrqGG4boo` | 7685566 |
| Absolute Stone | `CERCOM_BOOK_ABSOLUTE_STONE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-ABSOLUTE-STONE.pdf) | `1_DXYl7ttZ7Ao8MISbIuBa_ARjE1TszCF` | 14344895 |
| Amaranto | `CERCOM_BOOK_AMARANTO.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/AMARANTO.pdf) | `1umOI2h7EfgXyQEvcXmKrbx2R0zga1gok` | 7317626 |
| Archistone | `CERCOM_BOOK_ARCHISTONE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_cat_Archistone_new.pdf) | `1WmCL-AkXF_4W4wqXWqBot4XgipmNeHcD` | 4808791 |
| Bark | `CERCOM_BOOK_BARK.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_BARK.pdf) | `1EYj_enWer0ZVQLjTW9r4AfMBQ3AJ_VIW` | 6615711 |
| Briccole | `CERCOM_BOOK_BRICCOLE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_Cat_Briccole_WEB.pdf) | `1OzItjVLzhySd0tk5LjpYDoTjUODM7rxW` | 4068600 |
| Ceppo di Grès | `CERCOM_BOOK_CEPPO_DI_GRES.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-CEPPO-DI-GRES.pdf) | `1meWN_K9rkd_5A2JWPjnSHcpPs-xWh98Q` | 1059298 |
| Cosmo | `CERCOM_BOOK_COSMO.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/COSMO_CATALOGO.pdf) | `1vF80gokNe0dIdOEqgPeCWN_8lMPgnWsH` | 10938160 |
| Everstone | `CERCOM_BOOK_EVERSTONE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_Cat_EVERSTONE.pdf) | `1PPB5gzmogkKiI4rxULpWnR-qsMcPokZv` | 3227909 |
| Gravity | `CERCOM_BOOK_GRAVITY.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-GRAVITY-1.pdf) | `13L6igNAIXkOvp1T-OJf1pXOAkOcoh2LA` | 1265164 |
| In.Contro | `CERCOM_BOOK_IN_CONTRO.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_cat_IN.CONTRO_nov24.pdf) | `1kCLt1KcRuufwFvjB9qHxeC2wlpITeUDe` | 27306740 |
| Infinity | `CERCOM_BOOK_INFINITY.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-INTFINITY.pdf) | `1-LWxcDyWgkfRzP8w_OLwLu1VL__cC5rQ` | 459078 |
| Residence | `CERCOM_BOOK_RESIDENCE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/Cercom_cat_RESIDENCE.pdf) | `1YOIU0FZAYxHta5VRbvm-Nm73z-xwVxYR` | 13752427 |
| Silent Stone | `CERCOM_BOOK_SILENT_STONE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-SILENT-STONE.pdf) | `1JGgKCnkjkajFjRG23MBkH5lzfr4R204i` | 9849171 |
| Soap Stone | `CERCOM_BOOK_SOAP_STONE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/SOAP-STONE-2023.pdf) | `1y2CSearHJeDL-LlBbb4LAZq93yGMQLDw` | 9443026 |
| Square | `CERCOM_BOOK_SQUARE.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-SQUARE.pdf) | `1Sm56ZOnyIQBnl3vkXg_2f5xAYGFqgoxm` | 1060424 |
| Stone Box | `CERCOM_BOOK_STONE_BOX.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-STONE-BOX-1.pdf) | `1iVmrGCLqaxbvVk7RDNJeFOpYTE0owz3l` | 943894 |
| Stone Vision | `CERCOM_BOOK_STONE_VISION.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/cercom_catalogo_stone_vision.pdf) | `1bwwHSOo8ztwbv6IHv4moB2BR3ksmZ_ei` | 9460058 |
| Temper | `CERCOM_BOOK_TEMPER.pdf` | [PDF](https://www.cercomceramiche.it/wp-content/uploads/CERCOM-TEMPER.pdf) | `14wFLnSWkSxoNb7n9y7_CdUWDSp2GSDdL` | 8831732 |

Zmiana rejestru [`pdf-import/catalogues.csv`](https://github.com/darekjurko-coder/jurkoseo/blob/main/pdf-import/catalogues.csv): **137 → 156 wpisów** (+19, bez powtarzania nazw); w tym wpisy Cercom **3 → 22**, co dokumentuje 22 różne tytuły/pozycje tej marki w bibliotece (23 pliki, bo istnieje dodatkowa kopia `CERCOM_BOOK_ADOBE.pdf`). Zmiana CSV: commit `c64e54898ac32193a5e73ffdd8c571a1b37bed36`. Liczba kopii bez indywidualnego wiersza źródłowego w rejestrze: **81** (237−156; różnica dotyczy egzemplarzy, a nie koniecznie 81 nowych katalogów).

## Pozostające braki, ryzyka i błędy przypisań

1. Foldery kolekcji Cotto Petrus **Spaccone** (`1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`), **Rangers OUT** (`1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`) i **Galaxy OUT** (`12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`) sprawdzono przez paginowany odczyt folderów; **0 obiektów i brak dalszej strony** w każdym. Istnieje ogólny PDF Cotto Petrus ED12 z częścią tych kolekcji oraz osobny plik Galaxy. Spaccone i Rangers OUT w [oficjalnych pobraniach](https://www.cottopetrus.it/download/s5cb0a778) występują jako ZIP; zawartości ZIP nadal nie udało się otworzyć, więc nie można twierdzić, że brakuje samodzielnego PDF-a, ani że taka pozycja jest niedostępna.
2. [Century Download](https://www.century-ceramica.it/download/) wymienia Outdoor, bez potwierdzonego odrębnego oficjalnego PDF. Nie przypisywać błędnie pliku TAU `Outdoor.pdf` do Century.
3. Trzy istniejące pliki `CERAMICA_VOGUE_PASTELLI_CATALOGO.pdf`, `CERAMICA_VOGUE_WELLNESS_POOL_CATALOGO.pdf` i `CERAMICA_VOGUE_HEXA_HEXA_MATT_CATALOGO.pdf` są błędnie przypisane: właściwe marki to odpowiednio Appiani, Appiani i Ceramica Bardelli. Na Drive znaleziono już odrębne pliki pod prawidłowymi markami (`APPIANI_PASTELLI_CATALOGO.pdf`, `APPIANI_WELLNESS_POOL_CATALOGO.pdf`, `BARDELLI_HEXA_HEXA_MATT_CATALOGO.pdf`) o tych samych rozmiarach; **identyczność bajtowa nie została potwierdzona dziś**. Nie przenoszono i nie kasowano kopii bez weryfikacji integralności.
4. Poprzednie kontrole binarne wykazały **co najmniej 4 nadmiarowe kopie**: 3 w grupie Ceramica Vogue System (w tym Mix/Triangoli) i 1 Cercom Adobe; pliki pozostawiono bez zmian.
5. Brak jeszcze pełnego audytu SHA-256 i zgodności z oryginałami wszystkich **237** plików; nie zakończono też kompleksowego porównania list producentów z tym, co dostępne na Drive. Zgodność nazw, folderów i czytelności tekstu nie dowodzi identyczności binarnej ze źródłem.

## Stan Make

Scenariusz `9983437` „JURKO Armonie — import PDF na żądanie”: **inactive**, połączenie Google Drive **ok**, `incompleteExecutions=0`. Historia od 18 listopada zawiera tylko zakończony sukcesem import z 18 listopada; brak nowych uruchomień 19–21 listopada. Scenariusz jest prostym HTTP download → Drive upload, bez kontroli duplikatów. Nie uruchomiono go bez pewnego brakującego PDF-a i weryfikacji braku takiego samego dokumentu.

## Wniosek

**Nie ogłaszać ukończenia**. Udokumentowano 19 kolejnych oficjalnych źródeł bez produkowania duplikatów. Konieczne nadal rozstrzygnięcie archiwów ZIP i Century Outdoor, poprawa przypisań marek, uzupełnienie pochodzenia pozostałych plików, porównanie pełnych oficjalnych bibliotek oraz sum SHA-256. Nie wyłączać zadania okresowej kontroli.
