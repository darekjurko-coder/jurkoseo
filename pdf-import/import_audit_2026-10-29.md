# JURKO PDF — audit 2026-10-29

## Outcome
Seven additional original catalogue PDFs uploaded using the on-demand Make scenario `9983437`: **five Atlas Concorde**, **two Century**. All seven Make executions returned `success`, `application/pdf`, a nonzero byte count and a Google Drive file ID. Each of the seven destination folders was independently listed after upload; exact file name, MIME type and size matched. No existing files were overwritten. Make scenario was inactive before the imports and restored to inactive after them; its Google Drive connection was healthy.

This is a Drive metadata/readback audit, **not a full-byte SHA256 comparison of downloaded source and stored file**.

| Manufacturer | Collection | Drive file | Bytes | Official source |
|---|---|---|---:|---|
| Century | Moodboard | https://drive.google.com/file/d/1AoY788Dj3VsV4HeZlliI5fG0uM4yCrkC/view | 8728385 | https://www.century-ceramica.it/wp-content/uploads/2026/09/MOODBOARD-Bassa.pdf |
| Century | Cristalia | https://drive.google.com/file/d/1zJt_TN9WAkBHd7abgTNEGCeyOetAMSCW/view | 41076342 | https://www.century-ceramica.it/wp-content/uploads/2025/09/Cristalia.pdf |
| Atlas Concorde | Log Anthology | https://drive.google.com/file/d/1e_Dx8A_yVaMhQvelD6dBA2sd6V-VqDRL/view | 18302717 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/07de76bb-e21f-4051-8d13-e24c5942dfa3/qof92t/WEB/2608-atlasconcorde_log-web |
| Atlas Concorde | Nyra | https://drive.google.com/file/d/1oEqiUCKVLLdxi9X3YP68OIaQF3_u6mkN/view | 21355574 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/da536d24-f622-4477-b45c-be2dc146c679/bctb6c/WEB/250910-atlasconcorde_nyra_catalog2025-interattivo |
| Atlas Concorde | Marvel Next | https://drive.google.com/file/d/1zmAEqUy5CydHY9StPTSbtXb2Rr9mKd5K/view | 28167212 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/0b32e8de-1588-47b4-8a8a-c595ee212842/0ynxec/WEB/atlasconcorde_marvel-next-catalog-interactive |
| Atlas Concorde | Boost Hux | https://drive.google.com/file/d/14flMg3WdCCALhqmXYzJPLTNITF-gMrQa/view | 6199277 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/750cb19e-4e33-42fe-a6e1-7d2b165d3c23/6mghtj/WEB/ac-boost-hux-catalogo-interattivo |
| Atlas Concorde Habitat | Tratto | https://drive.google.com/file/d/190k7pYa26SGCKV2ODqEXvUU1sjGRK1qH/view | 8750076 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/0a98062c-e714-4242-8d84-8bf9ac7557ea/kcpo4l/WEB/atlasconcordehabitat_tratto_catalogue_2025-09 |

Century Reaction, Rocknest and Jasper were checked in their pre-existing collection folders: all three already had nonzero PDF files; therefore **not** re-uploaded.

## Inventory — eleven producers, root and immediate subfolders
Direct Google Drive listings on 2026-10-29. A nonzero PDF size and MIME `application/pdf` were checked for files in the collection folders. This is not a proof of complete catalogue coverage, not a full document integrity audit, and not a checksum deduplication.

| Manufacturer | PDFs at root | Collection folders | PDFs in immediate subfolders | Total PDF entries |
|---|---:|---:|---:|---:|
| Atlas Concorde | 3 | 7 | 7 | 10 |
| Casalgrande Padana | 1 | 7 | 8 | 9 |
| CEDIR | 1 | 0 | 0 | 1 |
| Century | 1 | 17 | 17 | 18 |
| Ceramica Cielo | 2 | 11 | 11 | 13 |
| Ceramica Vogue | 1 | 12 | 12 | 13 |
| Cercom | 4 | 19 | 19 | 23 |
| Cerdomus | 3 | 34 | 35 | 38 |
| CIPA Gres | 3 | 0 | 0 | 3 |
| CIR | 2 | 23 | 23 | 25 |
| Cotto Petrus | 3 | 59 | 57 | 60 |
| **Total** | **24** | **189** | **189** | **213** |

The 213 figure is **file entries**, not 213 unique documents. Potential duplicated content is not yet reconciled by checksum.

## Known remaining gaps and next actions
- Atlas Concorde's official Download Area lists **58 catalogues**; only **10 PDF entries** are present under the manufacturer folder after this run (including 3 general PDFs and a Habitat furniture catalogue). Official vs Drive matching remains incomplete. Official download page: https://www.atlasconcorde.com/en/download-area
- Century now has 17 collection PDFs plus one general PDF. The official download area also lists Organizer, Large Sizes and Outdoor; check whether these are covered by existing general PDF or require separate files. Official download page: https://www.century-ceramica.it/download/
- Cotto Petrus has three empty collection folders: `Spaccone`, `Rangers OUT`, `Galaxy OUT`. These series may be included in the general/Rangers/Galaxy PDFs, but must be verified before declaring coverage. The official Cotto Petrus catalogue includes Spaccone, and Rangers OUT appears in the Rangers product family.
- Verify mapping of the `Columbia` CSV entry: its source PDF URL contains `Soho`; do not silently treat that as verified Columbia content.
- Remaining manufacturers require an official downloadable catalogue list compared to each Drive file; technical sheets, duplicates and obsolete documents must be distinguished from collection catalogues.
- Final completion notice is **not warranted** yet. Continue scheduled checking.

## Repo updates
- `pdf-import/catalogues.csv`: seven new curated source URLs and exact destination folder IDs.
- `pdf-import/collection_folders.csv`: seven new folder mappings.
- Make `9983437`: activated for seven imports, then returned to inactive.
