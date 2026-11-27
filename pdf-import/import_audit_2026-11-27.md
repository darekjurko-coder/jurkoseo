# JURKO AI — audyt katalogów PDF, 27 listopada 2026

**STATUS: NIEUKOŃCZONE.**

## Import Casalgrande Padana
Na oficjalnej stronie https://www.casalgrandepadana.com/products (69 kolekcji) z kart produktów pobrano odnośniki Catalogue do sześciu odrębnych PDF. Odczytano źródłowe dokumenty, liczbę stron i sprawdzono okładki. Przed importem sprawdzono folder producenta, wszystkie 14 dotychczasowych podfolderów i rejestr: 16 PDF, brak sześciu poniższych katalogów. Utworzono sześć podfolderów, sprawdzono ich pustą zawartość, uruchomiono import Make 9983437. Po imporcie niezależne wyszukiwanie Drive i odczyt treści potwierdziły nazwy, MIME, rozmiary, lokalizacje i rozpoznawalne tytuły. Nie przeprowadzono pełnego porównania SHA-256 ze źródłami ani renderowania wszystkich stron.

| Kolekcja | Strony źródła | Bajty na Drive | Plik Drive | Wykonanie Make | Znaki odczytu |
|---|---:|---:|---|---|---:|
| Saxum | 52 | 3802872 | [PDF](https://drive.google.com/file/d/1kyV_0lb4EeCATI5GTiz68UJNiBSucWIr/view) | 1f43fcca57724f338959ee9ccc3e4566 | 64234 |
| Stonetech | 48 | 2246804 | [PDF](https://drive.google.com/file/d/14_Lah6XDRYl-3MdqYIT8D-dU18HPf0K5/view) | abcb2d0e16e641548328db386a845315 | 68624 |
| Project Wood | 44 | 2104267 | [PDF](https://drive.google.com/file/d/1C3AK6hTCOPQVpSdgx3iiewSPtZHMl4Sg/view) | 53389179d9e24eec820aa2c2ac5c2764 | 58963 |
| Terrazzotech | 48 | 3497146 | [PDF](https://drive.google.com/file/d/1QvINMaNfhvWy-AZGz4beEODzWij1cw32/view) | 0b0d8d644339417d93ff0652602193ae | 66995 |
| English Wood | 60 | 5622894 | [PDF](https://drive.google.com/file/d/1JxaanS76d8tb0yFEk4vBLFwVN1cmXw16/view) | bf541277d45f4b249db9806767964142 | 66770 |
| Fusion | 52 | 4957647 | [PDF](https://drive.google.com/file/d/15zlU3N25TXUCgCQLTAVRpyz79uusq0Nw/view) | cef889fa00444e61b4a8afa20a552089 | 59709 |

Razem 304 strony źródeł. Bezpośrednie URL i ID folderów zapisano w [catalogues.csv](catalogues.csv), commit e402fd3d27d4bd3de645f53129b7e36550bb0a91. Ponowny odczyt: 175 unikatowych wierszy, w tym 20 Casalgrande Padana. Make: sześć udanych wykonań, przywrócony stan inactive, incompleteExecutions=0, połączenie Google Drive OK.

## Stan 11 marek
Wyszukanie PDF po nazwach przed importem wykazało 244 katalogowe egzemplarze po wykluczeniu dwóch cenników (CERCOM-CENNIK-2019.pdf, PDF Listino Price List 2026_Cerdomus.pdf) oraz dwóch plików Durstone Ciro. Wszystkie miały niezerowe rozmiary. Po imporcie ponownie potwierdzono 22 PDF Casalgrande Padana, w tym po jednym nowym tytule. Łącznie 250 egzemplarzy: Atlas Concorde 33, Casalgrande Padana 22, CEDIR 1, Century 19, Ceramica Cielo 13, Ceramica Vogue 13, Cercom 23, Cerdomus 36, CIPA Gres 4, CIR 25, Cotto Petrus 61. Różnica liczby egzemplarzy i wpisów źródłowych: 75; nie jest to liczba brakujących unikatowych katalogów.

Nie nadpisano, nie usunięto ani nie przeniesiono istniejących PDF. Nadal otwarte: pełna inwentaryzacja oficjalnych bibliotek, pozostałe źródła, Cotto Petrus Spaccone/Rangers OUT/Galaxy OUT, Century Outdoor, wcześniejsze błędne przypisania Ceramica Vogue i co najmniej siedem nadmiarowych kopii, pełna kontrola SHA-256. Nie ogłaszać zakończenia.
