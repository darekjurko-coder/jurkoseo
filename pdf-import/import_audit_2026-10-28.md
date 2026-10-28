# JURKO PDF — audit 2026-10-28

## Ceramica Cielo
Source: https://www.ceramicacielo.it/it/download/cataloghi (official catalogue library, 13 downloadable PDF links). Eleven previously absent official PDFs uploaded to eleven newly created dedicated collection/news folders under parent `1J2EunSOSGHILLnl7npUVbpzQDFOQ2Mr0`. Existing `CERAMICA_CIELO_GENERAL_BOOK.pdf` and `CERAMICA_CIELO_CERAMIC_DESIGN_BOOK.pdf` in parent were preserved (no overwrites).

All 11 Make executions returned `success`, `application/pdf`, nonzero bytes and file IDs. All eleven were independently re-listed from their exact Google Drive destination folders, confirming name, MIME and size. Page counts below are from official PDFs inspected via the publisher website, not a second full-byte readback from Drive.

| Collection | Drive PDF | Bytes | Source PDF pages |
|---|---|---:|---:|
| News 2026 | https://drive.google.com/file/d/1uzvT4cQxHIg6uPiqI9Qa_oAXs8Gz1_37/view | 5537966 | 49 |
| News 2024 | https://drive.google.com/file/d/1spZEF1SPjuQMIdODUvix9GUnpS2Pz2rS/view | 5560500 | 60 |
| I Catini | https://drive.google.com/file/d/1LeyHWB91YReuot8RI2v1PAc5Zn-RK6Z5/view | 4412746 | 35 |
| Marcel | https://drive.google.com/file/d/1HVshuL8B7W-krirB-EhBg-BOQo-dkgXI/view | 1854101 | 21 |
| Theo | https://drive.google.com/file/d/1DDRxiRxW3KVFRsqRoqYJ945OXThJdklS/view | 8379787 | 31 |
| Era | https://drive.google.com/file/d/1IlB0I0sQegqjAo5hBJjpywzuPb8djDKp/view | 3646300 | 24 |
| Mare | https://drive.google.com/file/d/1Sex-78M3Ozr6kQBnxudk6jKeUtI5FzVi/view | 4686062 | 22 |
| Les Petites | https://drive.google.com/file/d/1IPyKgQ6H5bxYF3Z7JnCH2-3c3LhEXGwo/view | 4293908 | 37 |
| Infinito New | https://drive.google.com/file/d/1071B2haXycuHWlmg08BtA4kc8fFZ5gDm/view | 4599123 | 37 |
| Plinio Delfo Multiplo | https://drive.google.com/file/d/17fIjSEgaDslFUQ9rFfSMf4rbH_mG20eP/view | 1168610 | 21 |
| Le Acque di Cielo | https://drive.google.com/file/d/1KaS9OsUwKhv1zYFRibz57rkgqWgAGcZV/view | 3290535 | 77 |

Make scenario `9983437` was inactive before the import; it was activated only for on-demand imports and restored to inactive afterward. All 11 source URLs and destination folder IDs added to `pdf-import/catalogues.csv`.

## 11-producer inventory (root folder only; nested files not included)

| Manufacturer | PDF at root | Child folders |
|---|---:|---:|
| Atlas Concorde | 3 | 2 |
| Casalgrande Padana | 1 | 7 |
| CEDIR | 1 | 0 |
| Century | 1 | 15 |
| Ceramica Cielo | 2 | 11 |
| Ceramica Vogue | 1 | 12 |
| Cercom | 4 | 19 |
| Cerdomus | 3 | 34 |
| CIPA Gres | 3 | 0 |
| CIR | 2 | 23 |
| Cotto Petrus | 3 | 59 |

## Remaining coverage issues
- Atlas Concorde's official Download Area reports 58 catalogues; 3 general PDF files and 2 collection folders were found at its root. Many official collection catalogues are still not mapped.
- Century official Download Area includes Cristalia, Moodboard, Rocknest, Reaction and Jasper, which require a source/Drive comparison in addition to the previously imported 12 collections.
- Other producers require a full official-vs-Drive reconciliation including nested folders; root folder counts are not totals.
- No final completion notification should be sent for all eleven manufacturers yet.
