# JURKO AI — audyt 28 listopada 2026

**STATUS: NIEUKOŃCZONE.**

Na oficjalnych kartach [Texture](https://www.casalgrandepadana.com/product/elements-texture), [Pebbles](https://www.casalgrandepadana.com/product/elements-pebbles) oraz [Essence](https://www.casalgrandepadana.com/product/elements-essence) znaleziono wspólny katalog Elements oraz trzy odrębne katalogi wykończeń. Wspólny katalog zapisano tylko raz. Przed importem sprawdzono folder producenta, wyszukiwanie PDF (22 pliki) i rejestr (175 unikatowych URL); nowe cztery foldery sprawdzono jako puste. Bezpośredni odczyt źródłowych PDF przez przeglądarkę zwrócił cache miss, ale pobranie przez Make 9983437 zakończyło się sukcesem.

| Katalog | Bajty | Plik Drive | Wykonanie Make | Znaki odczytu |
|---|---:|---|---|---:|
| Elements | 10005116 | [PDF](https://drive.google.com/file/d/15v6sKBbfW4k__mbDiWNRPbtILvolKToj/view) | c6ac4d51835e4c21a65fa55004f03e9b | 82214 |
| Elements Texture | 2841155 | [PDF](https://drive.google.com/file/d/1owtz67ROONA47zQN8ROfZXoSyzWPFLMV/view) | cbe22fdb88934978901f1e8faa42256c | 72611 |
| Elements Pebbles | 2428372 | [PDF](https://drive.google.com/file/d/1f2tLqjliE1sLqbdBEj8dmbyhodc_2zg4/view) | 1b59aa245b1e4f3bbfe628d70a9330a3 | 71584 |
| Elements Essence | 2369799 | [PDF](https://drive.google.com/file/d/1JkzW37O5AqQkCIFUhMCc1RSPb_CP6lzc/view) | 9d841ae36a804a6eaaf86d4600d1b020 | 75990 |

Odczyt każdego folderu po imporcie potwierdził po jednym pliku, zgodny ID, nazwę, MIME PDF oraz rozmiar z Make. Odczyt treści potwierdził spisy treści i odpowiednie nazwy kolekcji. Nie ustalono pełnej liczby stron ani SHA-256 źródło/Drive; nie sprawdzono każdej strony wizualnie. Nie nadpisano, nie usunięto ani nie przeniesiono istniejących PDF. Make przywrócono do inactive, incompleteExecutions=0, połączenie OK.

Rejestr [catalogues.csv](catalogues.csv): 179 unikatowych URL, w tym 24 Casalgrande Padana, commit 46c532445c800605ba78772a56ff1d1f911c008d. [Foldery](collection_folders.csv): commit d0989b9bbb120f021becc3d2f1aaa802b413a5fa.

Casalgrande Padana: 22 przed importem + 4 potwierdzone nowe = 26 egzemplarzy. Stan wszystkich marek szacowany na 254 (250 z audytu 27 XI + 4), pozostałych dziesięciu marek nie przeliczono w tej sesji. Różnica 75 pomiędzy szacowaną liczbą egzemplarzy i liczbą unikatowych URL nie stanowi liczby brakujących katalogów.

Otwarte: pełna inwentaryzacja oficjalnych bibliotek wszystkich marek (strona Casalgrande pokazuje 70 kolekcji, nie oznacza to 70 osobnych PDF), pozostałe źródła, Cotto Petrus Spaccone/Rangers OUT/Galaxy OUT, Century Outdoor, wcześniejsze błędne przypisania Ceramica Vogue i duplikaty, pełna weryfikacja SHA-256. Nie ogłaszać zakończenia.
