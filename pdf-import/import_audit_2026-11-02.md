# JURKO PDF import — audit 2026-11-02

## Seven Atlas Concorde original manufacturer-authored PDF catalogues imported

All seven PDF downloads were from publicly accessible **third-party mirrors**, not the official Atlas Concorde CDN. These are manufacturer-branded, manufacturer-authored catalogues; source hosting provenance must be retained. Five new collection folders were created. Existing files were not overwritten. Make scenario 9983437 reported success for all seven uploads. Separate Drive folder listings confirmed exact names, `application/pdf`, nonzero sizes, and target folder placement. Total new bytes: **107,329,792 (107.33 MB decimal)**. No full-byte checksum comparison was performed. Some mirrors label editions as 2026 even when the document interior has an earlier date (Marvel Onyx PDF identifies September 2023); file naming uses the document's internal edition when known.

| Collection | Edition | Drive PDF | Bytes | Folder | Mirror source |
|---|---|---|---:|---|---|
| Boost Balance | 2023 | [PDF](https://drive.google.com/file/d/1enurUd11G4i264EBY3cb67gxNUJjhaXw/view) | 59111557 | [folder](https://drive.google.com/drive/folders/1scm06ruTdHG8h5Cvk0kD8gPDKzuDd0EA) | [PDF source](https://www.caemdordini.it/storage/151798/ceramiche-atlasconcorde-boostbalance-2023.pdf) |
| Marvel Onyx | 2023 | [PDF](https://drive.google.com/file/d/1l3ZWi2JJ8ePcR1W26qQwKJuI795Nvhhe/view) | 4814653 | [folder](https://drive.google.com/drive/folders/1xbfax6vQnsTvSRogNI6G3fMgd9MBkUD8) | [PDF source](https://www.caemdordini.it/storage/216102/Atlas-Concorde-Marvel-Onyx-catalogo-2026.pdf) |
| 3D Wall Carve | 2021 | [PDF](https://drive.google.com/file/d/13KA8oBVTWVYQTjJS7845z3bpOYoXE4cx/view) | 9437182 | [folder](https://drive.google.com/drive/folders/1NiJ-5bin6O8-DSlSGSTv5hLdjjIP7QdW) | [PDF source](https://mosaichomeinteriors.com/Catalogs/15/3DWallCarve.pdf) |
| Prism | 2025 | [PDF](https://drive.google.com/file/d/1Bi6-k8tZvop83NcAgxVatblIZKOPZekz/view) | 6721113 | [folder](https://drive.google.com/drive/folders/1Fs6QUfl_WAN7AK-ALM11ltjczLrXH9a1) | [PDF source](https://www.caemdordini.it/storage/194126/atlas-concorde-prism-catalogo-2025.pdf) |
| Boost | 2026 | [PDF](https://drive.google.com/file/d/1O926XYqe1v9D2ZXiZQ_opV1qzklzzGWR/view) | 11411312 | [folder](https://drive.google.com/drive/folders/1eDb9qojdid_F3wE3abl2HBvReP1ou8Np) | [PDF source](https://www.caemdordini.it/storage/216074/Atlas-Concorde-Boost-catalogo-2026.pdf) |
| Vivia | 2026 | [PDF](https://drive.google.com/file/d/1g8wX1Yg1xCI1-H2Eo2srQ7Vw_WoUJfIm/view) | 4366974 | [folder](https://drive.google.com/drive/folders/1qy2ZE4-82fz5GUtQYVZl2LSXbFVXJ3RM) | [PDF source](https://www.caemdordini.it/storage/239323/Atlas-Concorde-Vivia-catalogo-2026.pdf) |
| Boost Balance | 2026 | [PDF](https://drive.google.com/file/d/1ViwBdvTlypMdYxBeUYvx6whOtrmqBnSM/view) | 11467001 | [folder](https://drive.google.com/drive/folders/1scm06ruTdHG8h5Cvk0kD8gPDKzuDd0EA) | [PDF source](https://www.caemdordini.it/storage/216066/AtlasConcorde-Boost-Balance-catalogo-2026.pdf) |

Boost Balance 2023 and 2026 are intentionally retained as separate editions, not treated as duplicates. The earlier Boost Balance folder was empty before this run.

## Fresh Google Drive inventory — 2026-11-02

A Google Drive search for `mimeType=application/pdf` and the manufacturer-specific filename prefixes (not a full recursive ancestor-folder audit) returned **239 PDF file records**: Atlas Concorde 33; Casalgrande Padana 9; CEDIR 1; Century 19; Ceramica Cielo 13; Ceramica Vogue 13; Cercom 24; Cerdomus 37; CIPA Gres 3; CIR 27; Cotto Petrus 60. No pagination remained in any search. This is a count of file records, not unique contents or a guarantee that every file is in its intended manufacturer folder.

Potential duplicate copies requiring content-hash comparison: `CERAMICA_VOGUE_SYSTEM_CATALOGO.pdf` appears twice, both 14,247,829 bytes, in manufacturer root and System collection folder; `CERCOM_BOOK_ADOBE.pdf` appears twice, both 14,646,949 bytes, in manufacturer root and Adobe collection folder. Neither pair was deleted or overwritten; identical filename and size do not establish identical bytes.

## Remaining gaps and verification limits

- Atlas Concorde official download page advertises **58 catalogues**; 33 Atlas-prefixed PDFs now exist, including 3 general catalogues and two Boost Balance editions. A direct subtraction is not a valid missing-catalogue count until a title-by-title reconciliation is completed.
- Century `Outdoor` catalogue direct PDF source remains unverified. Rocknest, Reaction and Jasper catalogues were independently found already present in their own folders, so no duplicate uploads were made.
- Cotto Petrus `Spaccone`, `Rangers OUT`, and `Galaxy OUT` collection folders were listed again and remain empty. Manufacturer site lists these collections or minimali, but no verified standalone PDFs for those folders were found.
- Need full official source-title reconciliation for all 11 manufacturers, recursive folder-parent audit, PDF content and SHA-256/MD5 comparison across folders, and correction of any misplaced or duplicate copies.

## Repository / Make

- Appended 7 source rows to `pdf-import/catalogues.csv` and 5 new folder mappings to `pdf-import/collection_folders.csv`.
- Make scenario 9983437 was activated temporarily to upload PDFs and should be restored to its prior inactive state after the batch.
- **Overall import NOT complete.** Continue the scheduled monitoring; do not notify the user of completion.
