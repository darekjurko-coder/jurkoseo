# JURKO AI — audyt PDF, 22 listopada 2026

**STATUS: NIEUKOŃCZONE. Nie ogłaszać zakończenia importu.**

## Google Drive, GitHub, Make

Na Drive 237 katalogowych PDF dla 11 marek: Atlas Concorde 33; Casalgrande Padana 9; CEDIR 1; Century 19; Ceramica Cielo 13; Ceramica Vogue 13; Cercom 23; Cerdomus 36; CIPA Gres 4; CIR 25; Cotto Petrus 61. Brak nowych zapisów katalogowych od 21.11. 241 trafień brutto z wyszukiwania po prefiksach, wyłączono 2 cenniki i 2 pliki Durstone (nie katalogi CIR). Wszystkie katalogowe PDF mają dodatnie rozmiary.

Rejestr [catalogues.csv](https://github.com/darekjurko-coder/jurkoseo/blob/main/pdf-import/catalogues.csv) zawiera 156 rekordów. Sprawdzono 156/156 zgodności nazwy PDF oraz przypisanego folderu. 81 spośród 237 egzemplarzy katalogowych nie ma osobnego wiersza w tym rejestrze; nie jest to równoznaczne z brakiem 81 nowych katalogów.

Make, scenario 9983437: inactive; połączenie Google Drive ok; incompleteExecutions 0. Ostatnie udane wykonanie 2026-11-18 08:17:51 UTC. Scenariusz wykonuje HTTP download i zapis na Drive, bez weryfikacji duplikatów przed zapisem. Nie uruchamiano nowego importu bez potwierdzonego brakującego PDF.

## Nowa weryfikacja: 7 oficjalnych dokumentów Ceramica Vogue

Siedem linków źródłowych zapisanych w GitHub CSV sprawdzono niezależnie z siedmioma przyciskami pobierania na oficjalnych stronach Gruppo Bardelli. Wszystkie 7 ID źródłowych zgadzają się z oficjalną stroną producenta. Chociaż linki wskazują drive.google.com, są to oficjalne pliki udostępnione na stronie producenta, a nie odnośniki do kopii JURKO.

Pobrano osobno pełne bajty każdej pary oryginał producenta i katalog JURKO, porównano równość kompletnego base64: **7/7 identycznych binarnie**. Wyliczono SHA-256 zachowanych kopii. Przez PyMuPDF udało się programowo otworzyć każdą z **387 stron** siedmiu PDF, a 350 stron zawiera tekst możliwy do wyodrębnienia. Brak wyodrębnionego tekstu na części stron graficznych nie jest równoznaczny z błędem.

| Kolekcja | Oficjalna strona | Drive źródła | Drive JURKO | Bajtów | Stron | SHA-256 |
|---|---|---|---|---:|---:|---|
| Twins | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-twins) | 1UWTazJWY2Lt9DViGg-4tivgrCAasy8ts | 1N084sB7A339mJRncPYPOiHPeFO07wjjw | 1734446 | 10 | a029c13b37dbfdb31250b5ec72769b62c7483f12ceea121002e0557ca3cc8bcf |
| Materia | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-materia) | 1hZvJ1fTIwgdLQeHL3Xf4m6g3fEVi9nkO | 1LJ1I4OUPdEwS2EYrJqrhiQFnOMwBoFSs | 1227762 | 52 | b3494e92fbffa9e12992105b22a811e041e92ce98d48fc1bfa6694204861661f |
| System Triangoli | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-system-triangoli) | 1nbWtp2AAaIl3c_imBnuy6i6LSY-qCujM | 1Lprnn7U8fV613SNj121Qhkn_TKPn3vva | 14247829 | 108 | 66e4ba8e84551cfcebac5a2ef6d8f9ff1862a55c8e6b05407e49e1c3545aea5c |
| System Bisello | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-system-bisello) | 1RzU8tRj8M5DQQbNb5V4hrsuD3HKrQBqa | 1trBrJB2scH0LWS8NOFRtvkCmVin49r8m | 1227762 | 52 | e29a464d034a9f7de74f8bd4b03f15eeaef2250536597e9be6734545fa9dc82d |
| Flauti & Flautini | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-flauti-flautini) | 1TAK_XWj7PTS1swZEvGov7WmuYjldzh3h | 13C3K78Iy9IxDSk_xagmmPhwnZQkx2MIq | 13692943 | 29 | 8936f515c9b0f7f0bf01bd6564ff3b71ffbb3e239066f1048c75bbb6a9ec0852 |
| System Mix | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-system-mix) | 1in6HTsdIMArriq72AeHxHnCo3m3iQfF2 | 171OK-ikrOFbgYj8e6NFyySxN57TdgNN_ | 14247829 | 108 | 66e4ba8e84551cfcebac5a2ef6d8f9ff1862a55c8e6b05407e49e1c3545aea5c |
| System Decor | [Gruppo Bardelli](https://www.gruppobardelli.com/pages/collections/collection-system-decor) | 1qVanZtzyhGKqhjuJmVCMcTrPMDb_pgIB | 1IgQ8liAQm1nxWCOzDL3Cf2E1QeP_og5G | 5727764 | 28 | 48ddf38f5f199eca38fd8e5ec1cd76a1afeaae1dd1e1cf04a397d91dbba02cdf |

System Triangoli i System Mix są binarnie identyczne względem siebie (producent publikuje je pod odrębnymi ID), Materia i System Bisello mają równe rozmiary, ale różne SHA-256. Żadnego z tych egzemplarzy nie usuwano.

## Blokady zakończenia

- Foldery Cotto Petrus Spaccone (1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP), Rangers OUT (1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB) i Galaxy OUT (12HsAH9H5zCndaSxAIMqdEY6afuzE76eT) ponownie sprawdzono bezpośrednio: po **0 obiektów**, brak dalszej strony. Strona producenta https://www.cottopetrus.it/download/s5cb0a778 linkuje Spaccone do /userfiles/Download/spaccone.zip, a Rangers OUT do /userfiles/Download/rangers-out.zip. Pobranie archiwów ZIP w środowisku testowym nie powiodło się; nie zweryfikowano zawartości i nie należy stwierdzać niedostępności producenta. Galaxy OUT istnieje na stronie kolekcji, osobnego PDF nie potwierdzono.
- Century Outdoor pojawia się w https://www.century-ceramica.it/download/, lecz nie potwierdzono osobnego bezpośredniego PDF; nie przypisywać pliku TAU Outdoor.pdf.
- Trzy kopie podpisane jako Ceramica Vogue faktycznie pochodzą z marek Appiani (Pastelli; Wellness, Pool & Spa) i Ceramica Bardelli (Hexa / Hexa Matt); poprzednio zweryfikowano identyczne poprawnie oznaczone odpowiedniki. Łącznie wykazano co najmniej 7 nadmiarowych kopii PDF w całej bibliotece 11 marek.
- Nie ukończono pełnego porównania oficjalnych bibliotek 11 producentów, audytu integralności 237 plików oraz kontroli wszystkich duplikatów. Nie potwierdzono kompletności.

## Zmiany

Nie dodawano, nie nadpisywano, nie przenoszono i nie usuwano plików na Drive. Nie modyfikowano catalogues.csv ani konfiguracji Make. Uzupełniono wyłącznie audyt GitHub. Kontynuować okresową kontrolę; **nie powiadamiać o ukończeniu**.