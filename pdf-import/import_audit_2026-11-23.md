# JURKO AI — audyt katalogów PDF, 23 listopada 2026

**STATUS: NIEUKOŃCZONE. Warunek ogłoszenia ukończenia NIE jest spełniony.**

## 1. Bieżący stan Google Drive

Ponownie wyszukano pliki katalogowe z prefiksami poszczególnych producentów (bez cenników i plików innych marek). **237 PDF**:

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

Nie stwierdzono nowych plików katalogowych po poprzedniej kontroli. Obowiązuje zastrzeżenie: liczba PDF nie odpowiada liczbie **unikalnych oficjalnych katalogów** — znane są duplikaty i błędne przypisania marek.

## 2. Nowa pełna kontrola struktury Cotto Petrus

Bezpośrednio przejrzano folder producenta [Cotto Petrus](https://drive.google.com/drive/folders/12SNtTUT5EypRlWgwE2ysXX27QFsZS8XP) oraz **wszystkie 59 podfolderów kolekcji** przez Google Drive. Wynik:

- **56 podfolderów z plikami, 3 puste**: [Spaccone](https://drive.google.com/drive/folders/1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP), [Rangers OUT](https://drive.google.com/drive/folders/1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB), [Galaxy OUT](https://drive.google.com/drive/folders/12HsAH9H5zCndaSxAIMqdEY6afuzE76eT).
- **55 podfolderów zawiera po jednym PDF**, folder [Galaxy](https://drive.google.com/drive/folders/1ab0RXfNSpGo5RRZ-4tVPUNubaTXZs6ss) zawiera **dwa**: katalog 2026 i kartę techniczną 2026. Razem **57 plików PDF w podfolderach**.
- W folderze głównym znajdują się **4 PDF** (General ED12 2026, General 2026, General 2025 i Merchandising 2025). Łącznie **57 + 4 = 61 PDF**, zgodne z kontrolą wyszukiwania.
- Zweryfikowano odczyt tekstu pliku [General ED12 Official 2026](https://drive.google.com/file/d/1ima4IS3sFXrdIntAdTh1mAOzbmG0FlmR/view): katalog zawiera w spisie treści **Galaxy Out** (strona wskazana w spisie: 104), a także osobne pozycje Spaccone i Rangers Out. Występowanie kolekcji w katalogu ogólnym **nie dowodzi**, że istnieje osobny PDF lub że jest on poprawnie zapisany w dedykowanym folderze.
- Oficjalna [strona pobierania Cotto Petrus](https://www.cottopetrus.it/download/s5cb0a778) zawiera odnośniki do **Spaccone** oraz **Rangers OUT**, prowadzące do plików `/userfiles/Download/spaccone.zip` i `/userfiles/Download/rangers-out.zip`. Próba odczytu za pośrednictwem narzędzia przeglądania wskazała typ `application/zip`, lecz nie udostępniła bajtów archiwum, ponieważ format ZIP nie jest przez nie obsługiwany. Próba bezpośredniego pobrania w środowisku roboczym zakończyła się błędem połączenia; nadal **nie znamy zawartości ZIP**. Nie jest to potwierdzenie trwałej niedostępności u producenta. Brak podstaw do importu niezweryfikowanej zawartości.

## 3. Kontrola dwóch katalogów Century bez wpisów źródłowych

- [CENTURY_JASPER_CATALOGUE.pdf](https://drive.google.com/file/d/1HDS1IFQw5urswLLLwlXmE8sZ3Zu3Fgzo/view): **5 738 086 bajtów**; tekst możliwy do odczytu, zawiera logo/nazwę **CENTURY** i treść serii **Jasper** (27 634 znaków tekstu pozyskanego przez konektor). Seria jest także wymieniona na [oficjalnej stronie Century](https://www.century-ceramica.it/en/products/jasper/).
- [CENTURY_REACTION_CATALOGUE.pdf](https://drive.google.com/file/d/1efW_Gaj-F49-OQublyoQo8YO9VD2Ajoo/view): **5 391 005 bajtów**; tekst możliwy do odczytu, zawiera **CENTURY** i **Reaction** (38 052 znaki tekstu). [Oficjalna strona kolekcji](https://www.century-ceramica.it/prodotti/reaction/) potwierdza istnienie serii.

Oba pliki **już są na Drive** w odpowiednich folderach. Nie trzeba ich pobierać ponownie. Nie uzyskano wiarygodnych bezpośrednich URL oryginalnych PDF do porównania binarnego, więc **nie dopisywano** tych wpisów do `catalogues.csv` na podstawie samego tytułu lub domyślnego adresu URL. Wciąż niezweryfikowany osobny **Century Outdoor** z [oficjalnej strony pobierania](https://www.century-ceramica.it/download/); nie używać pliku TAU Ceramica `Outdoor.pdf`.

## 4. GitHub / Make

- [Rejestr catalogues.csv](https://github.com/darekjurko-coder/jurkoseo/blob/main/pdf-import/catalogues.csv) nadal zawiera **156 wierszy danych** (bez nagłówka). Z 237 zapisanych PDF **81 egzemplarzy nie ma indywidualnego wpisu źródłowego**. Nie oznacza to 81 katalogów do ponownego pobrania.
- Scenariusz Make **9983437** `JURKO Armonie — import PDF na żądanie`: **inactive**, połączenie Google Drive **ok**, `incompleteExecutions = 0`. Dwa najnowsze uruchomienia: **18 listopada 2026 08:17:51 UTC** (success, 2 operacje) i **13 listopada 2026 08:59:58 UTC** (success, 2 operacje). Brak nowego uruchomienia. Scenariusz nie ma automatycznej ochrony przed duplikatami przed uploadem.
- Z wcześniejszych audytów pozostają: **co najmniej 7 nadmiarowych kopii PDF**, w tym trzy dokumenty zapisane pod Ceramica Vogue, mimo że należą do Appiani lub Ceramica Bardelli. Pełna kontrola sum SHA-256 wszystkich 237 plików jest nieukończona.

## 5. Decyzja i ograniczenia

**Nie uruchamiano Make, nie dodawano, nie nadpisywano, nie przenoszono ani nie usuwano plików na Drive.** Nie zmieniano `catalogues.csv`. Powód: nie potwierdzono nowego, unikalnego pliku PDF, którego źródło, docelowy folder i brak duplikatu byłyby jednocześnie zweryfikowane.

Do ukończenia: ustalić zawartość ZIP Spaccone/Rangers OUT; rozstrzygnąć osobny katalog Galaxy OUT i Century Outdoor; skorygować przypisania marek bez zerwania odwołań; udokumentować pozostałe źródła; porównać dostępne oficjalne katalogi każdego z 11 producentów; sprawdzić integralność oraz SHA-256 całej biblioteki. **Zadanie pozostaje otwarte; nie ogłaszać ukończenia.**
