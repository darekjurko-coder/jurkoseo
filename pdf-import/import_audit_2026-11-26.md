# JURKO AI — audyt katalogów PDF, 26 listopada 2026

**STATUS: NIEUKOŃCZONE.**

## Import Casalgrande Padana
Z oficjalnych kart produktów producenta (https://www.casalgrandepadana.com/products, 69 wyników kolekcji w chwili kontroli) odnaleziono sześć bezpośrednich odnośników PDF w sekcjach Download Area / Catalogue. Odczytano dokumenty źródłowe, liczbę stron i okładki. Przed importem sprawdzono folder producenta i wszystkie jego dotychczasowe osiem podfolderów: 10 plików, bez tych sześciu tytułów. Sprawdzono rejestr, utworzono właściwe podfoldery i sprawdzono, że są puste. Make 9983437 zakończył wszystkie sześć importów sukcesem. Po zapisie potwierdzono nazwę, MIME, rozmiar, ID folderu oraz odczyt treści każdego pliku; tytuły kolekcji zgodne. Nie przeprowadzono pełnego porównania SHA-256 ze źródłami ani renderowania wszystkich stron.

| Kolekcja | Strony źródła | Bajty na Drive | Plik Drive | Wykonanie Make | Znaki odczytu |
|---|---:|---:|---|---|---:|
| Supreme | 52 | 7253587 | [PDF](https://drive.google.com/file/d/1KtLM5e8dy1tiD57meUPVp0evTLU9W1XU/view) | 6e44bfcd59794398b2074dcace0f5bb8 | 67276 |
| Terre Toscane | 32 | 1864842 | [PDF](https://drive.google.com/file/d/197CXzg5brKCqs3M7d_3PyZ48OHPjv1ZI/view) | e39183ad1ca24bfeb428383995bb3f40 | 35589 |
| Timeless | 40 | 2098102 | [PDF](https://drive.google.com/file/d/1Va9Re8L6viewgpaScacrBkWGuWwp_kdr/view) | ef346f07a3864396b419cac2dc00690e | 63146 |
| Marmora | 52 | 3434552 | [PDF](https://drive.google.com/file/d/1WvjEsu0loIfdAmSWSIiIZZWoeVx4TJNe/view) | 3f6b77a1d9e848018b77b7c3e54b492e | 81199 |
| Terrae | 56 | 3681761 | [PDF](https://drive.google.com/file/d/1LfXTbqQ6UOf9IRg3i0RX45ySw3lbcI4D/view) | 3f2e13a34cf14e52a3ad564c5db615fc | 61849 |
| Concept | 64 | 6961623 | [PDF](https://drive.google.com/file/d/15xHzuOvbsOHrIg1nLqTcX1Y1pIOktMLL/view) | 5d4cdd791ae54549b6f61d69fafed71c | 69815 |

Źródła bezpośrednie i ID folderów zapisano w [catalogues.csv](catalogues.csv), commit 756c26adb2cbd8deac406326f1b978b3d36fbdb2. Ponowny odczyt: 169 unikatowych wierszy, +6, wszystkie sześć nowych wpisów obecne. Casalgrande Padana 16 PDF (14 wpisów źródłowych). Po imporcie Make przywrócony do inactive, incompleteExecutions=0.

## Stan 11 marek
Wyszukanie PDF po prefiksach przed importem dało 238 katalogowych egzemplarzy po zastosowaniu poprzednich wykluczeń (dwa cenniki i dwa pliki Durstone Ciro). Wszystkie wyniki mają niezerowy rozmiar. Po imporcie ponowne wyszukanie Casalgrande Padana potwierdziło 16 zamiast 10, w tym dokładnie po jednym z sześciu nowych tytułów. Łącznie 244 egzemplarze: Atlas Concorde 33, Casalgrande Padana 16, CEDIR 1, Century 19, Ceramica Cielo 13, Ceramica Vogue 13, Cercom 23, Cerdomus 36, CIPA Gres 4, CIR 25, Cotto Petrus 61. Różnica między liczbą egzemplarzy a rejestrem: 75. Nie jest to liczba unikatowych oficjalnych dokumentów.

Nie nadpisano, nie usunięto ani nie przeniesiono istniejących PDF. Nadal otwarte: pełna inwentaryzacja bibliotek (sam wykaz kolekcji Casalgrande Padana obejmuje 69 pozycji, nie wszystkie muszą mieć odrębny PDF), źródła pozostałych dokumentów, Cotto Petrus Spaccone/Rangers OUT/Galaxy OUT, Century Outdoor, wcześniejsze błędne przypisania Ceramica Vogue i co najmniej siedem nadmiarowych kopii, pełna weryfikacja SHA-256. Nie ogłaszać zakończenia.
