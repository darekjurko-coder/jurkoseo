# JURKO AI — audyt katalogów PDF, 25 listopada 2026

**STATUS: NIEUKOŃCZONE.**

## Wynik importu — Casalgrande Padana, Petra
Oficjalna karta https://www.casalgrandepadana.com/product/petra wskazuje katalog PDF: https://www.casalgrandepadana.it/media/filer_public/a6/b4/a6b4a57d-dab3-446e-bcaf-5f33da9ec205/cp_cat_petra_lr_12_2022_upd_10_2025.pdf (44 strony, okładka i treść odczytane). Przed importem sprawdzono folder producenta oraz wyszukano PDF po nazwie; brak osobnego katalogu Petra, nie mylić z Pietra Tiburtina. Utworzono podfolder https://drive.google.com/drive/folders/1m8Az9qO2qSK3McEeiCHmxHIi-73M39xF.
Make 9983437: wykonanie a9d149f7f79b4ac696692fa09610b4e3 zakończone sukcesem. Nowy PDF https://drive.google.com/file/d/1PVRN-ml6haBxkdGj_eEzdqUeGar84uMP/view — CASALGRANDE_PADANA_PETRA_2025.pdf, 2 894 053 bajty, application/pdf. Po zapisie ponownie sprawdzono folder (dokładnie jeden plik), rozmiar i odczyt treści (59 309 znaków, prawidłowa kolekcja, oznaczenie wydania UPD 10/25). Brak pełnego porównania SHA-256. Make przywrócono do stanu inactive; połączenie ok, incompleteExecutions=0.

## Uzupełnienie źródeł istniejących PDF
Dopasowano cztery oficjalne odnośniki z kart produktów do plików w odpowiednich podfolderach. Nature (3 362 362 B; UPD 10/25), Era (5 143 864 B; UPD 07/26), Lithos (2 523 707 B; UPD 10/25): odczytane źródłowe PDF (odpowiednio 56, 56, 52 strony), okładki oraz czytelna treść kopii Drive i oznaczenia wydania. Marmoker 2025 (17 458 113 B, UPD 11/25): oficjalny link z karty Marmoker, długość źródła dokładnie taka sama; limit odczytu internetowego nie pozwolił otworzyć pełnego źródła, kopia Drive czytelna (76 342 znaki). Nie uznano tych dopasowań za binarną weryfikację.
Katalog Marmoker 2023 jest starszym materiałem ecomarmo (1 575 874 B); Water Visions (35 966 037 B) jest czytelnym katalogiem basenowym. Ich bezpośrednie źródła pozostają nieustalone. Pozostałe katalogi producenta wymagają inwentaryzacji oficjalnych kolekcji; 10 PDF nie oznacza kompletnej biblioteki.

## Stan Drive i rejestru
Ponowne wyszukanie PDF po prefiksach 11 marek; wykluczono dwa cenniki (Cercom, Cerdomus) i dwa pliki Durstone Ciro, zgodnie z poprzednią metodą. Atlas Concorde 33, Casalgrande Padana 10, CEDIR 1, Century 19, Ceramica Cielo 13, Ceramica Vogue 13, Cercom 23, Cerdomus 36, CIPA Gres 4, CIR 25, Cotto Petrus 61. Razem **238 katalogowych egzemplarzy PDF**, wszystkie z niezerowym rozmiarem; +1 wobec 24.11. Liczba obejmuje wcześniej wykryte kopie i błędne przypisania, nie jest liczbą unikatowych oficjalnych dokumentów.

Rejestr catalogues.csv: dodano 5 wierszy (4 istniejące pliki, 1 nowy). Commit 63a75d60ff37bdd5c64b89e0765012e7dad9e700. Ponowny odczyt: 163 unikatowe wiersze danych; 163/163 dopasowano dokładnie po nazwie i ID folderu do pojedynczego pliku Drive. 75 egzemplarzy bez indywidualnego wpisu źródłowego. Casalgrande Padana 8/10 z wpisem źródłowym.

Nie nadpisano, nie usunięto ani nie przeniesiono istniejących plików. Nadal otwarte: wcześniej stwierdzone braki Cotto Petrus (Spaccone, Rangers OUT, Galaxy OUT), Century Outdoor, trzy błędne przypisania Ceramica Vogue, co najmniej siedem nadmiarowych kopii, pełna inwentaryzacja wszystkich oficjalnych bibliotek i integralność/SHA-256. Nie ogłaszać zakończenia.
