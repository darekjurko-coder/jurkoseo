# JURKO AI — import original PDF catalogues: audit 2026-11-14

**Status: INCOMPLETE — do not notify completion.** No new catalogues imported, no existing files overwritten, moved, or deleted.

## Fresh Drive inventory, 14 November 2026
Queried Drive directly for `mimeType = application/pdf` and canonical filename prefixes; each query returned without a continuation token. The counts are **file records**, not verified distinct publications and not proof of completeness.

| Manufacturer | PDF records | CSV source registry rows |
| --- | ---: | ---: |
| Atlas Concorde | 33 | 28 |
| Casalgrande Padana | 9 | 3 |
| CEDIR | 1 | 0 |
| Century | 19 | 15 |
| Ceramica Cielo | 13 | 11 |
| Ceramica Vogue | 13 | 0 |
| Cercom | 23 | 0 |
| Cerdomus | 36 | 10 |
| CIPA Gres | 3 | 0 |
| CIR | 25 | 1 |
| Cotto Petrus | 61 | 54 |
| **TOTAL** | **236** | **122** |

Scope clarification: broader `CERCOM_`, `CERDOMUS_`, `CIR_` substring queries include one Cercom price list, one Cerdomus price list, and two unrelated Durstone files. These **four files do not count** toward the 236 catalog PDFs, explaining the historical larger raw search total.

## Full registry-to-Drive metadata reconciliation
Read current `pdf-import/catalogues.csv` (122 data rows) from GitHub and cross-referenced **all 122 rows** against a fresh Google Drive inventory by exact filename **and** exact parent-folder ID. **122/122 matched exactly one file; 0 absent and 0 ambiguous.** This verifies registry entries' placement and naming metadata, *not* manufacturer origin, PDF bytes, completeness, hashes or all unregistered documents.

**Four producers with zero registered provenance rows:** CEDIR, Ceramica Vogue, Cercom, CIPA Gres; despite Drive records. Many other Drive records likewise have no source row. Do not label these official-source-verified without finding and verifying primary-source URLs.

## PDF content spot checks (Drive text extraction successful)
Eight different PDF records were opened and their extracted contents inspected. These are content spot checks and are **not** SHA-256 tests of source versus Drive:

- **CEDIR:** `CEDIR_GENERAL_ARCHIVAL_CATALOGUE.pdf`, 148,072 extracted characters; includes CEDIR business/address/website but begins with a distributor's contact and "catalogue - price list"; archival provenance still unresolved.
- **Ceramica Vogue:** `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf`, 73,331 characters; identifies Ceramica Vogue System and March 2023.
- **CIPA Gres:** `CIPA_GRES_HI_TECH_2025.pdf`, 318,752 characters; identifies CIPA Gres and its official company website.
- **Century:** `CENTURY_CATALOGO_GENERALE_2025.pdf`, 479,529 characters; identifies Century/Fincibec, published May 2025.
- **Cerdomus:** `CERDOMUS_GENERAL_2026.pdf`, 522,269 characters; identifies Cerdomus collection showcase 2026.
- **CIR:** `CIR_GENERAL_2026.pdf`, 280,424 characters; identifies CIR Workbook 2026.
- **Ceramica Cielo:** `CERAMICA_CIELO_GENERAL_BOOK.pdf`, 280,927 characters; identifies Ceramica Cielo.
- **Cercom:** `CERCOM_WORKBOOK_CERCOM_26.pdf`, 269,071 characters; identifies Cercom 2026 workbook.
- **Previously imported Cotto Petrus edition 12:** `COTTO_PETRUS_GENERAL_ED12_OFFICIAL_2026.pdf`, 351,671 characters extracted on 14 Nov; starts "CATALOGO GENERALE .12", contents include Galaxy OUT on p.104; manufacturer source and file metadata verified in 13 Nov audit.

The 8 newly spot-checked PDFs had successful nonempty text extraction; this alone does **not** prove intact embedded images, complete pages, or cryptographic equivalence.

## Named duplicate / cross-placement risks
- `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf` appears in **two different parent folders**, matching the earlier concern about multiple System copies.
- `CERCOM_BOOK_ADOBE.pdf` appears in **two different parent folders**.
- No deletion or renaming was performed; same name/size alone does not establish a binary duplicate.
- Audit of 12 Nov reported **3 SHA-256-identical groups (8 records, 5 excess)** based on selective binary testing; these particular tests were **not repeated** in this run.

## Confirmed open gaps
- **Century Outdoor:** manufacturer download library https://www.century-ceramica.it/download/ lists Outdoor, but the 19 canonical Drive records include no `CENTURY_OUTDOOR` file. The Drive file `Outdoor.pdf` (ID `1OwCQ52GSU0lstvAwMzAqzrpfZsjAja5P`, 9,884,741 bytes) is **not** Century. Its 48,551 characters of extracted text include product names Borga/Campaspero and `www.tauceramica.com` and contain **zero** occurrences of "Century" or "Fincibec": it is a **TAU Ceramica** catalogue and must not be reclassified or copied as Century. A separate official Century Outdoor PDF URL was not verified.
- **Cotto Petrus** dedicated folders **Spaccone**, **Rangers OUT**, and **Galaxy OUT** were checked and each has **0 files** (folder IDs `1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`, `1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`, `12HsAH9H5zCndaSxAIMqdEY6afuzE76eT` respectively). The official collection pages https://www.cottopetrus.it/collezioni/sdfe11632 and https://www.cottopetrus.it/download/s5cb0a778 list these collections. Existing official general edition 12 includes Galaxy OUT and Spaccone references, older general edition 11 covers Rangers OUT; whether separate official catalogue PDFs exist is not confirmed.
- Manufacturer ZIP download links `https://www.cottopetrus.it/userfiles/Download/spaccone.zip` and `https://www.cottopetrus.it/userfiles/Download/rangers-out.zip` could not be opened as inspectable archives using available tools, so their contents remain **unverified**.
- The older `COTTO_PETRUS_GENERAL_2026.pdf` actually contains general edition 11. Its filename may be misleading; original file remains untouched.
- Comprehensive official-library comparison for each of 11 manufacturers, PDF binary SHA-256 coverage, and primary source attribution for the unregistered records still remain unfinished.

## Make import workflow
Scenario `9983437`, `JURKO Armonie — import PDF na żądanie`: **inactive**, Google Drive credential `ok`, incomplete executions **0**. Latest run `b905f4185edf451aa93d342ddf3f6b28`, successful on **13 November 2026 at 08:59:58 UTC** (2 operations); no newer runs in the queried period. The scenario is not a duplicate-detection mechanism; no run was started without a newly verified missing PDF source and exact destination.

## Outcome
**236 canonically named PDF records; 122/122 registry rows match a single Drive file in their intended folder; 8 additional selected PDFs content-inspected, the edition-12 Cotto Petrus PDF re-inspected; 0 new imports today.** Important evidence shows the apparent "Outdoor.pdf" is TAU, not Century. Three Cotto Petrus series folders are empty. Not all official catalogues have been authenticated or imported; do not issue a completion notification.
