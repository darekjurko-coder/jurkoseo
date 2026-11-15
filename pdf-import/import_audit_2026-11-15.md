# JURKO AI — audit importu katalogów PDF, 2026-11-15

**WYNIK: NIEUKOŃCZONE — bez powiadomienia o zakończeniu.** Kontrola w trybie tylko do odczytu dla Google Drive i Make; brak nowych pobrań, nadpisań i usunięć.

## Inwentaryzacja Drive, 15.11.2026

Zebrano bieżące wyniki wyszukiwania Drive z filtrem MIME `application/pdf` i **dodatkowo lokalnie odfiltrowano ścisły prefiks nazwy** (wyszukiwanie słowne Drive zwraca również fałszywe dopasowania, np. `CIR_` z innych nazw). Wszystkie 11 zapytań zwróciły wynik bez tokenu kolejnej strony; każdy dokument wykazuje rozmiar >0. Liczby oznaczają rekordy PDF, a nie unikatowe publikacje ani kompletność oficjalnego katalogu.

| Producent | Liczba rekordów PDF |
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
| **SUMA** | **236** |

**0 nowych dokumentów** utworzonych w tym zestawie od 14 listopada 2026 r. (UTC). **0 PDF o zerowym rozmiarze**. Na podstawie odczytanego bieżącego `pdf-import/catalogues.csv` ponownie porównano wszystkie **122 rekordy** względem dokładnej nazwy dokumentu i dokładnego ID folderu rodzica w bieżącym spisie 236 plików. Wynik: **122/122 jednoznacznych dopasowań, 0 brakujących, 0 wieloznacznych**. Nie oznacza to sprawdzenia integralności plików, ich oficjalnego pochodzenia ani pokrycia niezarejestrowanych materiałów.

Powtarzają się nazwy `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf` (2) i `CERCOM_BOOK_ADOBE.pdf` (2); nie przeprowadzono dzisiaj ponownej kontroli SHA-256. Z audytu 12.11 pozostaje wcześniejsze ustalenie o trzech grupach identycznych SHA-256 i pięciu nadmiarowych kopiach, bez nowych pomiarów.

## Nowe ustalenia względem dnia poprzedniego

1. **Century: brak nie tylko Outdoor, ale również Organizer.** Oficjalna strona https://www.century-ceramica.it/download/ wymienia 20 pozycji: Organizer, Large Sizes, Outdoor i 17 serii (Cristalia, Moodboard, Rocknest, Aurum, Blend, Contact, Cottage, Ecostone, Geology, Glam, Jasper, Medley, Reaction, Stonerock, Titan, TWO 20mm, Uptown). W Drive odnotowano 17 odpowiadających serii i Large Sizes, plus katalog ogólny 2025. W rekordach o kanonicznym prefiksie `CENTURY_` brak osobnych `Organizer` i `Outdoor`. Nie znaleziono zweryfikowanych bezpośrednich URL PDF dla tych dwóch pozycji. Nie wolno podstawiać obcego `Outdoor.pdf`: poprzedni audyt wykazał, że jest to katalog TAU Ceramica.
2. **Cercom: zgodność nominalnego wykazu katalogów.** Oficjalna strona https://www.cercomceramiche.it/download/ wymienia **19** książek kolekcji oraz **3** katalogi ogólne. W spisie Drive jest dokument odpowiadający każdemu z 22 tytułów według nazwy, plus druga kopia Book Adobe (23 rekordy). Nie dowodzi to identyczności danych PDF lub oficjalnej proweniencji; **0** pozycji Cercom jest obecnie w głównym `catalogues.csv`. Oficjalne przykładowe bezpośrednie URL to https://www.cercomceramiche.it/wp-content/uploads/WORKBOOK-CERCOM-2026.pdf, https://www.cercomceramiche.it/wp-content/uploads/CERCOM-ADOBE.pdf, https://www.cercomceramiche.it/wp-content/uploads/Cercom_catalogo_2CM_PagDoppie.pdf. Te linki pozwalają na przyszły audyt proweniencji; nie importowano ponownie istniejących dokumentów.
3. **Cotto Petrus: trzy foldery serii nadal puste**, każdy sprawdzony bezpośrednio: Spaccone `1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`, Rangers OUT `1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`, Galaxy OUT `12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`. Oficjalna biblioteka https://www.cottopetrus.it/download/s5cb0a778 oferuje Spaccone i Rangers OUT jako pliki ZIP w sekcji *minimali* (`.../userfiles/Download/spaccone.zip`, `.../userfiles/Download/rangers-out.zip`). Dwa sprawdzone linki są rzeczywiście zasobami `application/zip`, których narzędzie przeglądarkowe nie mogło odczytać; nie potwierdzono, czy zawierają jakikolwiek PDF, więc brak udokumentowanego, bezpośredniego katalogu PDF dla tych serii. Galaxy OUT jest wymieniona w oficjalnej liście kolekcji, a treść jest w ogólnym katalogu edycja 12, jednak osobne źródło PDF nadal niepotwierdzone.
4. **Cotto Petrus Columbia — kontrola niespójności w nazwach:** rejestr wskazuje na oryginalny plik `08e_CottoPetrus_Generale_23_Soho.pdf` i zapis `COTTO_PETRUS_COLUMBIA_2023.pdf`. Odczytano z Drive ten PDF (ID `1MW1gh6Y9ZtRBwRsBU_RCRlAokNkxvqK9`, 628890 bajtów): dokument zawiera nagłówek `COLUMBIA` i wyroby `Soho` (12 wystąpień). Zatem różnica nazw nie dowodzi błędnej klasyfikacji, lecz wymaga zachowania obu oznaczeń w metadanych. Nie zmieniano pliku.

## Stan Make
Scenariusz `9983437` (*JURKO Armonie — import PDF na żądanie*) ma status **inactive**, połączenie Google Drive **ok**, zaległe nieudane wykonania **0**. Lista wykonań od 12.11 wykazała jedno udane uruchomienie 13.11.2026 o 08:59:58 UTC (2 operacje), bez nowych wykonań 14–15.11.2026. Nie uruchamiano importu bez zweryfikowanego nowego oficjalnego PDF oraz bez wstępnej kontroli duplikatów. Scenariusz Make nie ma samodzielnego mechanizmu eliminacji duplikatów.

## Nadal do wykonania
Pełne oficjalne wykazy 11 producentów i ich mapowanie na Drive (nie tylko prefiksy), udokumentowanie źródeł dla CEDIR / Ceramica Vogue / Cercom / CIPA Gres i pozostałych niezarejestrowanych plików, znalezienie i ocena Century Organizer i Outdoor, rozpatrzenie archiwów ZIP Cotto Petrus, weryfikacja faktycznych stron i obrazów PDF, pełne porównanie binarnych SHA-256, a następnie kontrolowany import jedynie rzeczywiście brakujących pozycji.

**Podsumowanie:** 236 rekordów PDF, 122/122 zgodności rejestru z Drive w nazwie i folderze, 3 wciąż puste foldery Cotto Petrus, 2 nowe potwierdzone luki w wykazie Century (Organizer i Outdoor), 22/22 tytułów Cercom dopasowanych nominalnie, 0 zmian w Drive / Make / rejestrze CSV. Import całości nadal nieukończony.
