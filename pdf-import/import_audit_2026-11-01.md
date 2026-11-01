# JURKO PDF import — audit 2026-11-01

## Five additional official Atlas Concorde catalogues — successfully uploaded

Source URLs were found on the manufacturer's official CDN, and the collections were absent from the Atlas Concorde manufacturer root. Five new dedicated collection folders were created. Make on-demand scenario `9983437` returned `success` and a Drive file ID for each upload. Separate Google Drive folder listings independently confirmed each exact filename, MIME type `application/pdf`, and matching nonzero size. No existing files were overwritten.

| Collection | Drive PDF | Size (bytes) | Folder | Official manufacturer source |
|---|---|---:|---|---|
| Boost Stone | [PDF](https://drive.google.com/file/d/1JNBJCT-6ESmppzh3SFEs_9oe1D5fwquv/view) | 23,607,672 | [Folder](https://drive.google.com/drive/folders/1gjp9JipzedyrNTl1rPgZMN3hgJ_mq-By) | [CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/23c3c1ea-6a02-40d0-92f5-51eeccc73003/u38j94/WEB/AtlasConcorde_BoostStone_Catalogue_2022-09.pdf) |
| Boost Natural | [PDF](https://drive.google.com/file/d/1ewu0CUSDPlufS81e1hcB0ZPE1YbldqU8/view) | 18,480,890 | [Folder](https://drive.google.com/drive/folders/1EceBKVq_Gd28exkziA3QuoJ0YHEDpFnR) | [CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/7f4b984a-69ef-4149-8c62-65a4332f4389/u38j94/WEB/AtlasConcorde_BoostNatural_Catalogue_2022-09.pdf) |
| Boost Natural Pro | [PDF](https://drive.google.com/file/d/12LYTOPCQ-o8VStAbMPVYhhfb9UaZWB4w/view) | 29,279,028 | [Folder](https://drive.google.com/drive/folders/1qNv-IRmNYeHyS0oVgs_MkLDmXrqvtQ2T) | [CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/ed226960-1045-4e8e-9ac7-ce0b15795546/u38j94/WEB/AtlasConcorde_BoostNaturalPro_2024-04.pdf) |
| Boost Pro | [PDF](https://drive.google.com/file/d/1iHHO6maDC0jBi-AVdKQK8xa3QKf2QxZY/view) | 19,411,008 | [Folder](https://drive.google.com/drive/folders/1hyUuuEJae7tQHVyrzjulE5mQZPVuw3O6) | [CDN](https://gruppoconcorde-cdn.thron.com/static/D4XHMU_AtlasConcorde_BoostPro_Catalogue_2022-09_EKQXWV.pdf) |
| Boost Color | [PDF](https://drive.google.com/file/d/1JppAhXSkb8Lgta0C98sqdNrHvJeaeVZJ/view) | 54,730,465 | [Folder](https://drive.google.com/drive/folders/1vNQnnZDXII9PxKyktOD53-T8TrFF7Nll) | [CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/1c41a0fa-ce1d-46ef-9afb-23d6afbc3584/u38j94/WEB/AtlasConcorde_BoostColor_Catalogue_2024-03.pdf) |

**Total added:** 5 PDF files, 145,509,063 bytes (145.51 MB decimal). Source editions range from 2022 to 2024; these are manufacturer-published editions, not necessarily the latest revisions.

## Progress

All 11 manufacturer root folders were checked, and new Atlas Concorde folder listings were verified. Previous complete root + immediate-subfolder audit (2026-10-31) counted **225** Drive PDF entries (21 Atlas Concorde). Adding the five newly verified files implies **at least 230** entries (26 Atlas Concorde), **assuming no previous files were deleted**. This is an incremental figure, not a full recount. A planned deep recount hit a connector tool-call limit; do not treat the estimate as a full fresh count.

## Confirmed unresolved gaps

- Atlas Concorde **Boost Balance**: dedicated folder still empty. Official project links to a CDN PDF, but previous Make download returned HTTP 403; this run's web fetch of that link timed out. No PDF uploaded.
- Cotto Petrus **Spaccone**, **Rangers OUT**, **Galaxy OUT**: dedicated folders were checked directly and remain empty. Official Cotto Petrus download page has **Spaccone** and **Rangers OUT** as ZIP downloads of minimali rather than verified standalone catalogue PDFs; do not mislabel ZIPs as catalogues. A standalone Galaxy OUT PDF was not verified.
- Century **Outdoor**: appears on the official download page but its direct catalogue PDF URL is still unverified. The existing **TWO 20mm** catalogue is present in its own folder and must not be silently substituted.
- The official catalogues inventory for each of the 11 manufacturers has **not** yet been fully reconciled with all Drive subfolders. Cross-folder SHA-256/content duplicate checks and full PDF content checks for all entries remain pending. This run verified MIME, names, sizes, and folder placement of the five new files, **not** their full-byte SHA-256 checksums.

## Repository and Make

- Added the five official sources to `pdf-import/catalogues.csv`.
- Added five folders to `pdf-import/collection_folders.csv`.
- Temporarily activated Make scenario 9983437 to perform the five uploads, then returned it to its prior **inactive** state.
- **Overall task not complete**. Keep recurring check active; do not announce completion.
