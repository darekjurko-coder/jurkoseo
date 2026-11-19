# JURKO AI — audyt importu PDF, 2026-11-19

**Status: NIEUKOŃCZONE.** Nie potwierdzać kompletności 11 bibliotek, nie wysyłać powiadomienia o zakończeniu.

## Kontrola Google Drive

Ponownie odczytano 11 zestawów plików, filtrując MIME `application/pdf` i ściśle prefiksy nazw; wszystkie zapytania zwróciły komplet wyników bez stronicowania. Wszystkie pliki mają dodatni rozmiar.

| Producent | PDF |
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

**Brak nowego importu PDF po 18.11.2026.** Zbiorcze wyszukiwanie `modifiedTime > 2026-11-18T00:00:00` zwróciło tylko `CIPA_GRES_COLOURSTYLE_10X10_OFFICIAL.pdf` (z 18.11), bez nowego zapisu z 19.11.

## Uzupełnienie źródła w GitHubie

Dodano do `pdf-import/catalogues.csv` **1 wpis** dla już istniejącego katalogu Century Rocknest:
- Oficjalne źródło producenta: https://www.century-ceramica.it/wp-content/uploads/2025/02/Rocknest-1.pdf
- Plik na Drive: `CENTURY_ROCKNEST_CATALOGUE.pdf`, ID `1n_29p4ZWaRGfOInFRToNHR5DCwRaCAsS`, **8 959 456 bajtów**.
- Folder: `1f6Y20Nz9m5mPVvq6RdT5SLtXZv2I-sP3`.
- Weryfikacja tekstowa: tytuł ROCKNEST, nazwy kolekcji/wybarwień, wydanie **Febbraio 2025**, kod **142912** — zgodne z oficjalnym źródłem.
- **Nie wykonano porównania SHA-256 obu źródeł**, więc zgodność binarna nie jest stwierdzona.

GitHub CSV: **130 wpisów (było 129)**, przy kontroli struktury **130/130** wskazuje na dokładnie jeden PDF o zgodnej nazwie i odpowiednim ID folderu. **107/237** PDF-ów wciąż nie ma indywidualnej proweniencji w rejestrze.

## Kontrola zawartości i duplikatów

Odczytano tekst trzech niezależnych PDF na Drive: `CIPA_GRES_COLOURSTYLE_10X10_OFFICIAL.pdf` (tekst COLOURSTYLE 10X10), `CENTURY_ROCKNEST_CATALOGUE.pdf` (ROCKNEST), `COTTO_PETRUS_GENERAL_ED12_OFFICIAL_2026.pdf` (edycja 12, lista kolekcji, w tym Galaxy Out).

**Bezpośrednio potwierdzono identyczność binarną pobranych danych Base64** w dwóch parach o identycznych nazwach (pełna zawartość pliku, nie tylko metadane):
1. `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf`, ID `1pCpqEKmEGuxR0xJyvT0ii7CHqLp4bS5j` i `1hRNPYqcbFiDNRoT3FoKbq8Joq8foU5yr` — po 14 247 829 B, identyczne bajty.
2. `CERCOM_BOOK_ADOBE.pdf`, ID `1Njr0mOfj067n7jTq16yASPnzKyG0ME6L` i `1cWELyFNTIMHgUB57EuUBI7C1VLT9iwKc` — po 14 646 949 B, identyczne bajty.

Te pary to **2 potwierdzone kopie nadmiarowe** w analizowanych zestawach. Nie usuwano żadnego pliku. Wcześniejszy audyt zgłaszał dalsze duplikaty SHA-256, których dziś w całości nie przeliczono. Pełna deduplikacja całych 237 plików nadal nieukończona.

## Nieuzupełnione i niezweryfikowane pozycje

Bezpośrednie listowania Google Drive potwierdziły **0 plików** w trzech folderach Cotto Petrus:
- Spaccone: `1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`
- Rangers OUT: `1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`
- Galaxy OUT: `12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`

Oficjalna [strona Cotto Petrus](https://www.cottopetrus.it/download/s5cb0a778) wskazuje ZIP-y `spaccone.zip` i `rangers-out.zip`. Nie udało się pobrać ich zawartości i potwierdzić, czy znajdują się w nich osobne PDF-y. Dla Galaxy OUT jest sekcja w ogólnym katalogu ED12, ale nie znaleziono osobnego potwierdzonego URL PDF.

Oficjalna [strona Century Download](https://www.century-ceramica.it/download/) nadal wymienia `Outdoor`, lecz brak jednoznacznego, bezpośredniego URL oddzielnego PDF. `Outdoor.pdf` z TAU Ceramica nie jest dokumentem Century — nie importować.

CIPA Gres `OUTDOOR.pdf` nadal wymaga rozstrzygnięcia wersji względem posiadanej `CIPA_GRES_OUTDOOR_2025.pdf`. Wymagany jest pełny audyt wszystkich oficjalnych bibliotek producentów i integralności wszystkich PDF.

## Make / bezpieczeństwo zapisu

Make scenariusz `9983437` **inactive**, połączenie Google Drive **ok**, `incompleteExecutions=0`. W historii od 17.11 jedyny zapis to poprawne wykonanie importu CIPA Gres z 18.11 (ID `970bca26ae1a4445aae37cf2057619a7`); dziś nie uruchamiano scenariusza.

**Nie dodawano PDF-ów na Drive bez zweryfikowanego osobnego źródła, nie nadpisywano ani nie usuwano plików.** Kontynuować weryfikację źródeł i hashy; nie ogłaszać zakończenia zadania.
