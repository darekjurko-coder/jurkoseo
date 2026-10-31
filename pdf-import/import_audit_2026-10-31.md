# JURKO PDF import — audit 2026-10-31

## Successful uploads (6)
Six original Atlas Concorde PDF catalogues were uploaded using Make scenario 9983437 from official manufacturer CDN sources. Each Make run returned success and file ID. A separate Google Drive folder listing confirmed the exact filename, application/pdf MIME and identical nonzero size. Independent Drive PDF text extraction confirmed the named collection appears in each document. No existing PDFs were overwritten.

| Collection | Drive PDF | Bytes | Destination folder | Official source |
|---|---|---:|---|---|
| Boost Vision | [PDF](https://drive.google.com/file/d/1rEMwqshzl8XXa8Xx959ggFeEFjyGDhsG/view) | 21867017 | [Folder](https://drive.google.com/drive/folders/1b5TMBI-4Q7rsc6OX-51yzhHsfW4AFYO6) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/20d40494-b074-476c-85f5-678a1321dacc/hemlh3/WEB/atlasconcorde_boostvision_catalog_09_2025) |
| Marvel Epic | [PDF](https://drive.google.com/file/d/1-pNyhkJyMhpP4pjvypWWz354CCGTBZjU/view) | 38406952 | [Folder](https://drive.google.com/drive/folders/1Uo8koiU2vh-XxhodBbbp4Wgz087ULeM6) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/ccfb9f35-1061-493e-a49b-7ffa9462c7df/u31amm/WEB/atlasconcorde_marvelepic_catalogue_2025-09) |
| Log Select | [PDF](https://drive.google.com/file/d/11x1tk1JiSgedAdRwGqVKS8oB4Ccujp0f/view) | 18828025 | [Folder](https://drive.google.com/drive/folders/13uThJOae9LZA2UmgjAOF44G39PjY4PJU) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/cc7f7c09-deb6-4a8b-b6f4-e60fe5dbabb6/n6l1w3/WEB/ac_logselect_catalogo_dgt_250916_lr) |
| Boost Mineral | [PDF](https://drive.google.com/file/d/1AmAWyu3ZNbaACEjHpa9piueHxYTXMcxn/view) | 25467910 | [Folder](https://drive.google.com/drive/folders/1D7VPZXs0rtBhZFT3NX36YVvoZKchqM8F) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/c3283fe9-3146-405a-9940-682f2952342a/lsvqpj/WEB/atlasconcorde_boostmineral_catalogue_2023_06) |
| Log Cansei | [PDF](https://drive.google.com/file/d/1LLkNTWLXukqjEgv_4ZfR_vcJViLkM9Zj/view) | 27055074 | [Folder](https://drive.google.com/drive/folders/1Vic8EMYV7MgT4Gp2LU2Z7qqnZARv7iup) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/static/N8SQJH_AtlasConcorde_LogCansei_Catalogue_2024-09_HK87MA.pdf) |
| Marvel Shine | [PDF](https://drive.google.com/file/d/19Ts6fyazlkSdI0xjnEhkZIem3eBcZlFo/view) | 4209647 | [Folder](https://drive.google.com/drive/folders/16l5SuRVgPNtSSMaJ3tQgyMZF1JwYWfv3) | [Manufacturer CDN](https://gruppoconcorde-cdn.thron.com/static/LV8A1D_AtlasConcorde_MarvelShine_Catalogue_2022-02_KRJETR.pdf) |

**New bytes:** 135,834,625. Six new collection folders have valid PDFs.

## Failed attempt / empty folder
- **Atlas Concorde — Boost Balance:** official project page https://www.atlasconcorde.com/en/ac-collection/boost-balance/project links to https://gruppoconcorde-cdn.thron.com/static/RYFKR0_AtlasConcorde_BoostBalance_QRHECE.pdf . Make HTTP download returned `InvalidConfigurationError: Forbidden` (HTTP 403). No PDF was uploaded. The dedicated [Boost Balance folder](https://drive.google.com/drive/folders/1scm06ruTdHG8h5Cvk0kD8gPDKzuDd0EA) remains empty. The source is not recorded as an importable PDF until a working official URL is found.

## Recount from Google Drive (31 October)
All 11 manufacturer roots and their **immediate** subfolders were listed and PDF MIME types counted. This is a count of Drive entries, **not** a count of unique PDF contents and **not** a SHA-256 audit.

| Manufacturer | PDFs |
|---|---:|
| Atlas Concorde | 21 |
| Casalgrande Padana | 9 |
| CEDIR | 1 |
| Century | 19 |
| Ceramica Cielo | 13 |
| Ceramica Vogue | 13 |
| Cercom | 23 |
| Cerdomus | 38 |
| CIPA Gres | 3 |
| CIR | 25 |
| Cotto Petrus | 60 |
| **Total** | **225** |

The six new Atlas Concorde files explain the increase from the previous 219 estimated entries to 225 now directly recounted. **No errors** occurred while listing the manufacturer roots or their immediate subfolders.

## Missing / unresolved
- Atlas Concorde download area lists 58 catalogue entries across its families and brands; Drive contains 21 PDF entries including general books, so category-by-category reconciliation remains incomplete. https://www.atlasconcorde.com/en/download-area
- Boost Balance official CDN returned HTTP 403 as above. Its folder is empty.
- Cotto Petrus **Spaccone**, **Rangers OUT**, and **Galaxy OUT** collection folders remain empty. The manufacturer shows these products, but no independently verified standalone PDF source was found for these three today. https://www.cottopetrus.it/download/s5cb0a778 and https://www.cottopetrus.it/collections/
- Century download area includes **Outdoor**. The exact current official Outdoor PDF download URL has not been verified; the existing **TWO 20mm** catalogue is not automatically assumed to be the same document. https://www.century-ceramica.it/download/
- The previously reported **Cotto Petrus Columbia / Soho** URL discrepancy was checked by reading text of the stored `COTTO_PETRUS_COLUMBIA_2023.pdf`. The PDF explicitly contains a **COLUMBIA** section and lists **Soho** product variants; this is not evidence of misfiling, so no change was made.
- Full comparison against every manufacturer's current official catalogue inventory remains incomplete. Full-byte checksums, duplicate-content detection across folders, and verification of editions for all 225 entries remain outstanding.

## Repository
- Added six successful official PDF URLs to `pdf-import/catalogues.csv`.
- Added seven collection folders (including the empty Boost Balance folder) to `pdf-import/collection_folders.csv`.
- Make import scenario was originally inactive; it was temporarily activated for the uploads and should be returned to inactive after this audit.
- **Not complete:** do not announce overall completion or disable the recurring audit.
