# SPECYFIKACJA WDROŻENIA — JURKO SEO kolejka materiałów

## Cel
Zbudować pełny proces:
1. Użytkownik dodaje producenta i kolekcję do kolejki w jurkoseo.pl.
2. Automat pobiera oficjalne materiały producenta.
3. Zapisuje katalog PDF, zdjęcia źródłowe i tekstury na Google Drive.
4. Generuje od 0 do 5 obrazów AI, zgodnie z wyborem użytkownika.
5. Generuje tytuł, opis posta, słowa kluczowe i CTA.
6. Pokazuje wszystko w karcie kolejki w jurkoseo.pl.
7. Użytkownik zatwierdza materiał.
8. Po zatwierdzeniu może wybrać publikację za 3 dni.
9. Publikacja do Google Business Profile następuje dopiero po zatwierdzeniu.
10. Po publikacji zapisujemy datę i ID wpisu Google.

## Ograniczanie kosztów
- Domyślnie 2 obrazy AI na kolekcję.
- Użytkownik może wybrać 0, 1, 2, 3, 4 lub 5 obrazów.
- Maksymalnie 5 obrazów AI na kolekcję.
- Nie pobierać ponownie plików, które już istnieją.
- Opis i słowa kluczowe generować jednym wywołaniem AI.
- Brak nieskończonych retry.
- Maksymalnie 20–30 operacji Make na jedną kolekcję.
- Publikować tylko rekordy zatwierdzone.
- Jeśli koszt/limit zostanie osiągnięty, zatrzymać kolejne generowanie i ustawić status BŁĄD/LIMIT.

## Google Sheets
Plik: JURKO SEO – kolejka publikacji

### Zakładka 01_KOLEJKA
A ID
B DATA_DODANIA
C PRODUCENT
D KOLEKCJA
E KATEGORIA
F STATUS
G ETAP_AUTOMATU
H SOURCE_URL
I DRIVE_FOLDER_URL
J PDF_URL
K RAW_IMAGE_URL
L AI_IMAGE_URL
M FINAL_IMAGE_URL
N POST_TEXT
O KEYWORDS
P HASHTAGS
Q CTA
R TARGET_URL
S APPROVED
T APPROVED_AT
U PUBLISH_AT
V PUBLISHED_AT
W GOOGLE_POST_ID
X ERROR
Y UPDATED_AT
Z NOTES
AA AI_IMAGES_COUNT
AB GENERATED_IMAGES_COUNT
AC ESTIMATED_COST_LEVEL

### Zakładka 02_MATERIALY
A MATERIAL_ID
B QUEUE_ID
C PRODUCENT
D KOLEKCJA
E TYPE
F SOURCE_URL
G DRIVE_URL
H FILE_NAME
I MIME_TYPE
J SOURCE
K SELECTED
L CREATED_AT
M NOTES

TYPE:
- catalog_pdf
- technical_pdf
- raw_image
- texture
- ai_image
- final_image

### Zakładka 03_PUBLIKACJE
A PUBLICATION_ID
B QUEUE_ID
C PRODUCENT
D KOLEKCJA
E CHANNEL
F POST_TEXT
G IMAGE_URL
H TARGET_URL
I PUBLISHED_AT
J EXTERNAL_POST_ID
K STATUS
L VIEWS
M CLICKS
N CALLS
O WEBSITE_ACTIONS
P CHECKED_AT

### Zakładka 04_KONFIGURACJA
A PRODUCENT
B SOURCE_URL
C DOWNLOAD_URL
D DRIVE_ROOT_FOLDER_ID
E ACTIVE
F AI_PROMPT
G POST_INTERVAL_DAYS
H DEFAULT_PUBLISH_TIME
I LOCATION
J NOTES

## Statusy
- Nowe
- Do przygotowania
- Pobieranie materiałów
- Materiały zapisane na Drive
- Generowanie obrazów AI
- Tworzenie opisu
- Do zatwierdzenia
- Zaplanowane
- Publikowanie
- Opublikowane
- Błąd
- Odrzucone
- Archiwum

## Struktura Google Drive
JURKO SEO/
  Producent/
    Kolekcja/
      01_PDF/
      02_ZDJECIA_ZRODLOWE/
      03_TEKSTURY/
      04_AI/
      05_FINAL/
      06_ARCHIWUM/

## UI jurkoseo.pl
Przy dodawaniu do kolejki dodać pole:
"Liczba obrazów AI" = select [0,1,2,3,4,5], default 2.

Karta kolejki ma pokazywać:
- producent
- kolekcja
- status
- etap automatu
- liczba wybranych obrazów AI
- liczba wygenerowanych obrazów
- link do folderu Drive
- link do PDF
- miniatury zdjęć źródłowych
- miniatury obrazów AI
- finalne zdjęcie
- gotowy opis
- słowa kluczowe
- CTA
- planowaną datę publikacji

Przyciski:
- Przygotuj materiały
- Otwórz folder Drive
- Pokaż materiały
- Popraw opis
- Zmień zdjęcie
- Odrzuć
- Zatwierdź i opublikuj za 3 dni
- Opublikuj teraz
- Archiwizuj

## Logika zatwierdzania
Publikacja możliwa tylko gdy:
APPROVED = TAK
STATUS = Zaplanowane
PUBLISH_AT <= aktualny czas

Po kliknięciu "Zatwierdź i opublikuj za 3 dni":
- APPROVED = TAK
- APPROVED_AT = teraz
- PUBLISH_AT = teraz + 3 dni
- STATUS = Zaplanowane

Po publikacji:
- STATUS = Opublikowane
- PUBLISHED_AT = teraz
- GOOGLE_POST_ID = zwrócone ID posta

## Make — scenariusz 1: PREPARE MATERIALS
Trigger: webhook z jurkoseo.pl

Kroki:
1. Odbierz: producer, collection, profile, source, drive, ai_images_count.
2. Utwórz rekord w 01_KOLEJKA.
3. Utwórz folder producent/kolekcja na Drive.
4. Pobierz oficjalną stronę producenta.
5. Znajdź katalog PDF i zdjęcia źródłowe.
6. Pobierz maksymalnie 1 katalog PDF i maksymalnie 5 zdjęć źródłowych.
7. Zapisz je na Drive.
8. Zapisz rekordy do 02_MATERIALY.
9. Wygeneruj 0–5 obrazów AI zgodnie z AI_IMAGES_COUNT.
10. Zapisuj postęp 1/5, 2/5 itd.
11. Wygeneruj jednym wywołaniem:
    - tytuł
    - opis posta po polsku
    - 2–4 naturalne frazy SEO
    - CTA
12. Zapisz wynik do 01_KOLEJKA.
13. Ustaw STATUS = Do zatwierdzenia.
14. Nie publikuj automatycznie.

## Make — scenariusz 2: PUBLISH APPROVED
Trigger: co 1 godzinę

1. Pobierz rekordy:
   APPROVED=TAK
   STATUS=Zaplanowane
   PUBLISH_AT<=teraz
2. Opublikuj do Google Business Profile.
3. Zapisz GOOGLE_POST_ID.
4. Zapisz PUBLISHED_AT.
5. STATUS=Opublikowane.
6. Jeśli publikacja się nie uda: STATUS=Błąd i zapis błędu do ERROR.

## Reguły jakości
- Zawsze korzystać z oficjalnej strony producenta jako źródła kolekcji.
- Nie używać przypadkowych zdjęć z internetu.
- Nie wymyślać parametrów technicznych.
- Jeśli PDF lub zdjęcia są niedostępne, ustawić błąd zamiast podstawiać inny produkt.
- Nie publikować bez akceptacji użytkownika.
- Nie generować więcej obrazów niż wybrano.
- Jeśli AI_IMAGES_COUNT = 0, przygotować tylko materiały źródłowe + tekst.

## Pierwszy test
Producent: Italgraniti
Kolekcja: I Cementi
Źródło: oficjalna strona Italgraniti
Domyślnie: 2 obrazy AI
Test kończy się statusem: Do zatwierdzenia
