# JURKO AI — PDF catalogue import audit (2026-11-13)

**Status: INCOMPLETE. No completion notification.** One new **official manufacturer PDF** was successfully imported to Google Drive without replacing existing files; the CSV registry was extended by one row. This is not a full vendor-by-vendor completeness or binary-hash audit.

## New import: Cotto Petrus General Catalogue 12 (2026)

- **Official manufacturer source:** https://www.cottopetrus.it/userfiles/News/files/CottoPetrus_Cat-Generale_2026_LOW.pdf (linked from manufacturer news page "Catalogo Generale 12", dated **16 September 2026**: https://www.cottopetrus.it/catalogo-generale-12/s2fd5efb3).
- **Drive file:** `COTTO_PETRUS_GENERAL_ED12_OFFICIAL_2026.pdf`, ID `1ima4IS3sFXrdIntAdTh1mAOzbmG0FlmR`, https://drive.google.com/file/d/1ima4IS3sFXrdIntAdTh1mAOzbmG0FlmR/view
- **Parent:** Cotto Petrus root folder `12SNtTUT5EypRlWgwE2ysXX27QFsZS8XP` (same location as existing general catalogues).
- **Verified size:** 11,709,158 bytes, matching the manufacturer URL's returned content length, Make upload output, and Google Drive metadata. Google Drive reports `application/pdf`; text extraction was successful (351,671 characters), with exact initial title **"CATALOGO GENERALE .12"**, collection index including **Galaxy Out on page 104**, **Muraglia**, and a printing/editorial date **August 2026**. These are content checks, **not** a cryptographic comparison of source and stored bytes.
- **Make:** on-demand scenario `9983437` was temporarily activated and run, execution `b905f4185edf451aa93d342ddf3f6b28`, successful on 13 Nov 2026 at ~08:59 UTC (2 module operations, no incomplete executions). The scenario was then **deactivated again**; Drive connection remains `ok`.
- **Duplicate avoidance:** exact target filename was absent before uploading. An earlier `COTTO_PETRUS_GENERAL_2026.pdf` (11,328,033 bytes, ID `1j5JlDrVR9hMjDoJ7aPadQC5XIfpnhdke`) remains untouched. Its extracted document begins **"CATALOGO GENERALE .11"**, as does `COTTO_PETRUS_GENERAL_2025.pdf`. The new catalogue clearly identifies edition 12; there was no overwrite or deletion. Existing "2026" filename **does not mean it is edition 12**; provenance/renaming should be reviewed separately.
- **GitHub registry:** appended a unique new row with manufacturer URL, correct folder ID and final filename to `pdf-import/catalogues.csv`; it now has **122 source rows** (121 prior + 1 new). No prior rows were overwritten. Update commit: `d2c0ce5ff93ef4f8473a084d35cf50b4ce44eb67`.

## Current Google Drive metadata census

Fresh queries on **13 November 2026** used `mimeType = application/pdf`, one canonical filename prefix per manufacturer, and excluded unrelated files/price lists. No query had a next-page token. All returned files reported nonzero size. Counts are **Drive PDF records**, not deduplicated publications or proof of library completeness.

| Manufacturer | PDF records |
| --- | ---: |
| Atlas Concorde | 33 |
| Casalgrande Padana | 9 |
| CEDIR | 1 |
| Century | 19 |
| Ceramica Cielo | 13 |
| Ceramica Vogue | 13 |
| Cercom | 23 |
| Cerdomus | 36 |
| CIPA Gres | 3 |
| CIR | 25 |
| Cotto Petrus | **61** (previously 60) |
| **TOTAL** | **236** (previously 235) |

**Historical 239 vs 235 discrepancy explained at search-filter level:** broader search for `CERCOM_`, `CERDOMUS_`, `CIR_` returns four PDF records whose names do **not** start with canonical catalogue prefixes: `CERCOM-CENNIK-2019.pdf` (price list), `PDF Listino Price List 2026_Cerdomus.pdf` (price list), `DURSTONE - Ciro - Uzupelnienie 2026.pdf`, and `DURSTONE - City Ciro - Nowosc 2026.pdf` (Durstone). Hence 235 canonical records + four other results = 239 matches in that broader approach. This does not prove any catalogue was lost.

## New content-level assessment and remaining gaps

- The **official edition 12** includes `Galaxy Out` on its contents page (p. 104) and multiple product references to `GALAXY OUT`; thus the variant is **documented inside an official general catalogue now on Drive**, although there is still **no independently verified stand-alone Galaxy OUT catalogue**. Its dedicated Drive folder (`12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`) remains empty.
- `Spaccone` appears as product/texture references in the new edition 12, and the previously imported general edition 11 contains the series too. The official site exposes a ZIP link (https://www.cottopetrus.it/userfiles/Download/spaccone.zip), not a verified stand-alone PDF. ZIP contents could not be inspected through the available download methods. Dedicated Drive folder `1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP` is empty.
- `Rangers OUT` is covered by the older manufacturer general 2025 catalogue (p. 126), while the new edition 12 does not contain that literal label. Manufacturer ZIP (https://www.cottopetrus.it/userfiles/Download/rangers-out.zip) remains uninspected. Dedicated folder `1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB` is empty.
- Century manufacturer download page (https://www.century-ceramica.it/download/) still lists `Outdoor`, but no verified separate official PDF URL has been established. `Rocknest`, `Reaction`, and `Jasper` **are already present** as distinct `CENTURY_..._CATALOGUE.pdf` records in the existing 19, so these are **not** new missing files.
- An existing `COTTO_PETRUS_MURAGLIA_CATALOGUE.pdf` was found and its extracted text confirms a manufacturer Muraglia catalogue; no duplicate was uploaded.

## Outstanding verification before completion

1. Reconcile all official downloads for each of the 11 vendors against Drive folder trees, including published variants, updated editions and vendor official origin for third-party-hosted documents.
2. Resolve 4 vendors with **no CSV provenance rows**: CEDIR, Ceramica Vogue, Cercom, CIPA Gres. The other 121 rows had correct filename+folder matches on 12 November; today the new 122nd was explicitly verified. **Not all 122 entries were independently rechecked today.**
3. Inspect manufacturer ZIP archives and confirm whether separate PDFs exist for Spaccone and Rangers OUT; clarify Galaxy OUT stand-alone PDF status and Century Outdoor direct URL.
4. Run comprehensive binary SHA-256 and PDF content checks across the Drive catalogue inventory. Previous day's selected hash tests found **3 binary duplicate groups comprising 8 records (5 excess copies)**; those results were *not* rehashed today. Avoid deleting them before editorial disposition.
5. Examine the misleading older `COTTO_PETRUS_GENERAL_2026.pdf` edition-11 naming and decide how to preserve/display provenance alongside the official edition-12 version.

**No existing PDF was overwritten, moved or deleted. The import remains incomplete.**
