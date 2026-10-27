# JURKO PDF — audit 2026-10-27

## Result
12 original Century collection PDF files uploaded via Make (scenario 9983437) to distinct collection folders in the Century Google Drive parent. All 12 Make runs returned success, MIME application/pdf and nonzero size; a subsequent Drive folder listing confirmed each file's presence, name, MIME and size. The scenario was inactive before this work and restored to inactive after each batch. The official Century product pages linked directly to these PDFs.

| Collection | Drive PDF | Bytes |
|---|---|---:|
| Contact | https://drive.google.com/file/d/126MDI9PXVdyXB8GSpvtIu4a1gz_BTt-b/view | 5266424 |
| Cottage | https://drive.google.com/file/d/11DwtPf6p3leveIGEHy7rAtF2obGa4_IT/view | 4688564 |
| Aurum | https://drive.google.com/file/d/168iE7Poj3YVVM6jYKJx53WuCbCl0X6jk/view | 2990165 |
| Blend | https://drive.google.com/file/d/1pmdOWBQwhbnz3smdtT45qT-Kx3tj3NMf/view | 5644658 |
| Ecostone | https://drive.google.com/file/d/1WEBXZFqYQXSDv7nxuzcCDedXnv9wA7Jb/view | 2401975 |
| Geology | https://drive.google.com/file/d/1Epv5xZrWgHVOyVi2yGF0TaQ0h_eh50CH/view | 4328473 |
| Glam | https://drive.google.com/file/d/1oF8YYwheFo2AUUFbVgtbBouABs97FQzH/view | 6112768 |
| Medley | https://drive.google.com/file/d/1MBP4WUOJgOu5yNbHUREIy23Z3sIWvYzU/view | 4447381 |
| Stonerock | https://drive.google.com/file/d/1M-_nyZpoQzumN2nMu8-42McOyxN9bolK/view | 3045659 |
| Titan | https://drive.google.com/file/d/1tdTCluoWDpJmiksOuVyD8cw1-YQjaDA6/view | 3002038 |
| TWO 20mm | https://drive.google.com/file/d/1ToJyWYpFCu_Jzox0yLdhZ4pWao_81-f9/view | 8453282 |
| Uptown | https://drive.google.com/file/d/1awfCT-pzGyqq8NL0Q_lrx5-L4V2Krioz/view | 6543885 |

These new curated source URLs and destination folders were added to catalogues.csv and collection_folders.csv. Existing files were not overwritten.

## Coverage snapshot (Google Drive name searches, indicative, not a byte-level audit)
Atlas Concorde 5; Casalgrande Padana 9; CEDIR 1; Century 16; Ceramica Cielo 2; Ceramica Vogue 13; Cercom 24; Cerdomus 37; CIPA Gres 3; CIR 25 matching CIR_ plus two unrelated Ciro files surfaced by search; Cotto Petrus 60. These are current search results, including earlier uploads, not counts of PDFs imported in this run. Names, MIME and sizes for 12 newly uploaded Century files were checked in their actual folders.

## Incomplete / next steps
- Atlas Concorde's official 2026 Download Area lists 58 catalogues; only five Atlas PDFs are currently visible by matching Drive filename. Do not declare completion.
- Century product listing includes Cristalia; its product page exposed a technical sheet but no separate catalogue link in the inspected page. Check whether a catalogue is available elsewhere before marking Century complete.
- Other manufacturers still require comparison against official complete product/download listings, not only curated CSV entries.
- GitHub workflow dispatch/scheduled execution was not directly verified in this run; GitHub Actions secrets and run reports remain to be checked. The workflow treats automatically discovered PDFs as review-only and does not upload them without curated mapping.
- Do not send completion notification until official source coverage, correct folder placement and PDF integrity are audited for all 11 manufacturers.
