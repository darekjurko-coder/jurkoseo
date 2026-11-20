# JURKO AI — audyt importu katalogów PDF, 2026-11-20

**Status: NIEUKOŃCZONE.** Brak podstaw do powiadomienia o kompletnym imporcie. Nie zmieniano/usuwano/nadpisywano plików Google Drive.

## Stan Google Drive i rejestru

Bezpośrednio sprawdzono wszystkie 11 prefiksów nazw przez wyszukiwanie Google Drive typu PDF (brak niepobranych stron wyników); wszystkie zwrócone PDF-y mają niezerowy rozmiar. Od poprzedniej kontroli nie wykryto nowego pliku PDF.

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
| **Łącznie** | **237** |

GitHub `pdf-import/catalogues.csv` wzrósł **130 → 137 wpisów**; ponownie potwierdzono, że **137/137** wpisów pasuje do dokładnie jednego PDF-u na Drive o zgodnej nazwie i identyfikatorze folderu. Pozostałych **100 instancji plików** nie ma osobnego 1:1 wpisu źródłowego (99 nazw w ogóle nieobecnych w rejestrze oraz jedna dodatkowa kopia o nazwie występującej w rejestrze). Zgodność metadanych nie oznacza kompletnego audytu bajtów i źródeł.

## 7 oficjalnych źródeł Ceramica Vogue — dodane po porównaniu całych plików

Oficjalne strony produktów [Gruppo Bardelli](https://www.gruppobardelli.com/pages/download) udostępniają katalogi producentów, wskazując konkretne pliki PDF przechowywane na Drive. Dla każdej poniższej pozycji sprawdzono: plik źródłowy, identyczność binarną **pełnych plików**, rozmiar, istniejącą nazwę PDF i folder na JURKO Drive. Zapisano 7 wpisów bez pobierania duplikatów.

| Katalog | Źródło wskazane przez stronę produktu | Rozmiar |
|---|---|---:|
| Twins | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-twins) / [PDF](https://drive.google.com/file/d/1UWTazJWY2Lt9DViGg-4tivgrCAasy8ts/view) | 1 734 446 B |
| Materia | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-materia) / [PDF](https://drive.google.com/file/d/1hZvJ1fTIwgdLQeHL3Xf4m6g3fEVi9nkO/view) | 1 227 762 B |
| System Triangoli | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-system-triangoli) / [PDF](https://drive.google.com/file/d/1nbWtp2AAaIl3c_imBnuy6i6LSY-qCujM/view) | 14 247 829 B |
| System Bisello | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-system-bisello) / [PDF](https://drive.google.com/file/d/1RzU8tRj8M5DQQbNb5V4hrsuD3HKrQBqa/view) | 1 227 762 B |
| Flauti & Flautini | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-flauti-flautini) / [PDF](https://drive.google.com/file/d/1TAK_XWj7PTS1swZEvGov7WmuYjldzh3h/view) | 13 692 943 B |
| System Mix | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-system-mix) / [PDF](https://drive.google.com/file/d/1in6HTsdIMArriq72AeHxHnCo3m3iQfF2/view) | 14 247 829 B |
| System Decor | [strona producenta](https://www.gruppobardelli.com/pages/collections/collection-system-decor) / [PDF](https://drive.google.com/file/d/1qVanZtzyhGKqhjuJmVCMcTrPMDb_pgIB/view) | 5 727 764 B |

GitHub commity zmian:
- `e466e8348eb1bc0c90c889c84e6c0d57b218c69a` — Twins i Materia;
- `e0ef4ce27ed780e03b7c3172e2b7fcbf75049f0b` — System Triangoli i Bisello;
- `b64a01b8fcd64f0cb4785df922898cbe26e6a0d4` — Flauti & Flautini, System Mix i Decor.

**Uwaga o zawartości:** oficjalne linki `System Triangoli`, `System Mix` i ogólnego `System` wskazują bajtowo identyczny plik (systemowy katalog ogólny), nie trzy oddzielne broszury. Rejestr opisuje je jako źródła do nazw na Drive, lecz nie wykazuje trzech niezależnych katalogów.

## Błędy przypisania producenta (nowe ustalenie)

Odczyt zawartości PDF na JURKO Drive ujawnił co najmniej **3 pliki z błędnym prefiksem producenta**:
- `CERAMICA_VOGUE_PASTELLI_CATALOGO.pdf` — tekst wewnątrz wskazuje **Appiani** (oficjalna [strona Pastelli](https://www.gruppobardelli.com/pages/collections/collection-pastelli)).
- `CERAMICA_VOGUE_WELLNESS_POOL_CATALOGO.pdf` — tekst wewnątrz wielokrotnie wskazuje **Appiani**, „Wellness, Pool & Spa”.
- `CERAMICA_VOGUE_HEXA_HEXA_MATT_CATALOGO.pdf` — kolekcja należy do **Ceramica Bardelli** ([strona producenta Hexa](https://www.gruppobardelli.com/pages/collections/collection-hexa-hexa-matt)), nie Ceramica Vogue.

Nie przenoszono ani nie zmieniano nazw automatycznie; przed korektą sprawdzić docelowe foldery właściwych marek. Są to dodatkowe przeszkody w potwierdzeniu prawidłowego przypisania 11 bibliotek.

## Potwierdzone nadmiarowe duplikaty

Pobrano kompletne pliki i porównano pełne dane binarne. **4 identyczne pliki Ceramica Vogue** o rozmiarze **14 247 829 B**:
- `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf` (dwie kopie: `1pCpqEKmEGuxR0xJyvT0ii7CHqLp4bS5j` i `1hRNPYqcbFiDNRoT3FoKbq8Joq8foU5yr`);
- `CERAMICA_VOGUE_SYSTEM_TRIANGOLI_CATALOGO.pdf` (`1Lprnn7U8fV613SNj121Qhkn_TKPn3vva`);
- `CERAMICA_VOGUE_SYSTEM_MIX_CATALOGO.pdf` (`171OK-ikrOFbgYj8e6NFyySxN57TdgNN_`).

Daje to **3 nadmiarowe kopie** identycznego PDF w grupie Vogue System. Dodatkowo poprzednie kontrole binarne potwierdziły **1 kopię nadmiarową** `CERCOM_BOOK_ADOBE.pdf` (dwa ID: `1Njr0mOfj067n7jTq16yASPnzKyG0ME6L`, `1cWELyFNTIMHgUB57EuUBI7C1VLT9iwKc`). **Łącznie co najmniej 4 nadmiarowe kopie**, bez usuwania. Pełny audyt SHA-256 wszystkich 237 plików nadal niezakończony.

Przykład dwóch dokumentów, których nie należy uznawać za duplikaty: `System Bisello` i `Materia` mają identyczną wielkość i wydobyty tekst, lecz **różne SHA-256** i różne dane binarne.

## Braki i niedostępności

- Foldery Cotto Petrus **Spaccone**, **Rangers OUT** i **Galaxy OUT** ponownie sprawdzone bezpośrednio: każdy zawiera **0 plików**. Producent na [stronie pobierania](https://www.cottopetrus.it/download/s5cb0a778) udostępnia archiwa ZIP `spaccone.zip` i `rangers-out.zip`, ale nie udało się odczytać ich zawartości, nie wiadomo czy zawierają samodzielne PDF-y. Część kolekcji (w tym Galaxy OUT) figuruje w katalogu ogólnym Cotto Petrus ED12.
- Na [stronie Century Download](https://www.century-ceramica.it/download/) jest pozycja **Outdoor**, ale wciąż bez zweryfikowanego niezależnego adresu oficjalnego PDF; nie wolno korzystać z `Outdoor.pdf` marki TAU.
- Nie wykonano pełnego porównania wszystkich oficjalnych tytułów 11 producentów i wszystkich hashy dokumentów.

## Make

Scenariusz `9983437` jest nadal **inactive**, połączenie Drive **ok**, `incompleteExecutions=0`. W historii od 18.11 jest jeden udany import CIPA Gres z 18.11; **brak nowego uruchomienia 19–20.11**. Scenariusz to prosty HTTP-download → upload na Drive bez wbudowanej deduplikacji; **nie uruchamiano go bez pewnego nowego źródła**, aby nie wprowadzać kopii.

**Wniosek: brak warunku ukończenia.** Dalsze zadania: poprawne rozdzielenie marek Appiani/Bardelli od Vogue; rozstrzygnięcie ZIP-ów i Century Outdoor; pochodzenie pozostałych 100 kopii, pełne porównanie katalogów producentów oraz audyt integralności i deduplikacji. Nie ogłaszać zakończenia importu.
