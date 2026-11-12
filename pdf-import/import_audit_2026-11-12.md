# JURKO AI — PDF catalogue audit (2026-11-12)

**Status: INCOMPLETE. No completion notification. No new uploads, overwrites, moves, or deletions in this run.**

## Direct Google Drive inventory (strict filename prefix + PDF MIME)

Queried Google Drive individually for each manufacturer, filtered to `mimeType=application/pdf` and strictly accepted names starting with the vendor-specific canonical prefix; each query returned no further page token. Counts refer to Drive file records, **not unique catalogues** and **not a recursively verified completeness census**.

| Manufacturer | PDF records | Latest modification (UTC) | Registered CSV source rows matched in correct folder |
| --- | ---: | --- | ---: |
| Atlas Concorde | 33 | 2026-11-02 08:58 | 28/28 |
| Casalgrande Padana | 9 | 2026-10-20 07:21 | 3/3 |
| CEDIR | 1 | 2026-10-16 07:56 | 0/0 |
| Century | 19 | 2026-10-30 08:11 | 15/15 |
| Ceramica Cielo | 13 | 2026-10-28 08:38 | 11/11 |
| Ceramica Vogue | 13 | 2026-10-16 07:58 | 0/0 |
| Cercom | 23 | 2026-10-18 08:01 | 0/0 |
| Cerdomus | 36 | 2026-10-25 08:20 | 10/10 |
| CIPA Gres | 3 | 2026-10-16 07:55 | 0/0 |
| CIR | 25 | 2026-10-16 05:20 | 1/1 |
| Cotto Petrus | 60 | 2026-10-26 08:34 | 53/53 |
| **TOTAL** | **235** | | **121/121** |

All 235 prefix-filtered items report MIME `application/pdf`, nonzero sizes, and none have a modified timestamp on or after 2026-11-11 UTC. Read `pdf-import/catalogues.csv`: **121 CSV source rows**, all 121 had at least one matching exact filename on Drive in the stated `folder_id`. This is a metadata audit of the register, not verification of original bytes against manufacturer URLs. `CEDIR`, `Ceramica Vogue`, `Cercom`, and `CIPA Gres` currently have **no register rows** despite holding PDF files; expand source traceability. Previous 2026-11-02 inventory listed 239 under a different/looser search methodology; **235 vs 239 is not evidence that four files were deleted**. Some broad search matches include unrelated files and price lists.

## Binary SHA-256 checks of selected suspected duplicates (downloaded from Drive)

Actual binary PDF files were fetched from Drive and SHA-256 checked locally; PDFs were successfully parsed and page-count checked without modification.

1. **Ceramica Vogue: four byte-identical PDFs**, SHA-256 `66e4ba8e84551cfcebac5a2ef6d8f9ff1862a55c8e6b05407e49e1c3545aea5c`, each 14,247,829 bytes / 108 pages:
   - System in general manufacturer folder: `1hRNPYqcbFiDNRoT3FoKbq8Joq8foU5yr`
   - System collection: `1pCpqEKmEGuxR0xJyvT0ii7CHqLp4bS5j`
   - System Mix: `171OK-ikrOFbgYj8e6NFyySxN57TdgNN_`
   - System Triangoli: `1Lprnn7U8fV613SNj121Qhkn_TKPn3vva`
   These are **three extra copies of the same bytes**; the distinct collection filenames do not demonstrate distinct content. Preserve until editorial decision on canonical placement.
2. **Cercom Adobe: two byte-identical PDFs**, SHA-256 `ca1f168455e248c49e57fa469caa763d596e3e3df6862dabf5da561f018ecc79`, each 14,646,949 bytes / 32 pages:
   - Manufacturer general folder: `1Njr0mOfj067n7jTq16yASPnzKyG0ME6L`
   - Adobe collection folder: `1cWELyFNTIMHgUB57EuUBI7C1VLT9iwKc`.
3. **CIR Boston Brick: two byte-identical PDFs**, SHA-256 `e8a1a2eb87d11701359bc04011570b7514e0f5da31a4458f672c5b021e189b65`, each 644,273 bytes / 5 pages:
   - Manufacturer general folder: `1Zfx47P2AvjnRPLClC_jphz1e9suJoMjE`
   - Boston Brick collection: `1j3DoFu9DVVtku-6bsD1g7puh5bDRw2-u`.

**Confirmed across these three hash groups: 8 file records and 3 unique byte streams (5 redundant records).** No duplicates removed; they may be intentional cross-listings, but System Mix/Triangoli need content attribution review.

**Important negative control:** Ceramica Vogue Materia `1LJ1I4OUPdEwS2EYrJqrhiQFnOMwBoFSs` and System Bisello `1trBrJB2scH0LWS8NOFRtvkCmVin49r8m` both report 1,227,762 bytes / 52 pages and have identical extracted text, **but different SHA-256** (`b3494e92fbffa9e12992105b22a811e041e92ce98d48fc1bfa6694204861661f` versus `e29a464d034a9f7de74f8bd4b03f15eeaef2250536597e9be6734545fa9dc82d`). Therefore do **not** designate these files as binary duplicates based on text/size alone; visual comparison is pending.

## Official-site follow-ups

- Cotto Petrus official [English download page](https://www.cottopetrus.it/download/s5cb0a6f6) provides `rangers out` as [rangers-out.zip](https://www.cottopetrus.it/userfiles/Download/rangers-out.zip) and `Spaccone` as [spaccone.zip](https://www.cottopetrus.it/userfiles/Download/spaccone.zip), **not as direct downloadable PDFs at those links**. Both ZIP contents remain uninspected (download attempt failed). Official [2025 general PDF](https://www.cottopetrus.it/download/CottoPetrus_Catalogo_Generale_2025.pdf) is already on Drive as `COTTO_PETRUS_GENERAL_2025.pdf` (44,490,148 bytes). Therefore lack of stand-alone PDF in `Spaccone` or `Rangers OUT` is unresolved until ZIP inspection and catalogue inclusion determination.
- Cotto Petrus official [collection index](https://www.cottopetrus.it/collections/) lists `Galaxy OUT`; separate direct manufacturer PDF for that variant **not verified**. The existing `COTTO_PETRUS_GALAXY_2026.pdf` extracted text identifies the **indoor** catalogue and has no `Galaxy OUT`/outdoor text matches. The designated Drive folder `Galaxy OUT` remains empty.
- Direct Drive folder listings: `Spaccone` (`1AWBBTLj1txIaBXpoGEc9Ng_99xCfPyKP`), `Rangers OUT` (`1UzPgrU6R6AKAP_UmrlTessFmAWdTVtJB`), and `Galaxy OUT` (`12HsAH9H5zCndaSxAIMqdEY6afuzE76eT`) each contain **0 direct items**.
- Century official [Download page](https://www.century-ceramica.it/download/) lists `Outdoor`, but an independently verified direct PDF URL remains unavailable. Do not attach unrelated `Outdoor.pdf` to Century without file provenance.
- Atlas Concorde official [2026 general catalogue statement](https://www.atlasconcorde.com/en/news/general-catalogues-2026) identifies three catalogues (General, Large Sizes and Outdoor); their 2026 PDFs already have corresponding Atlas-prefixed Drive files. Nonetheless the complete collection-by-collection catalogue inventory has not been reconciled against the official download library.

## Make scenario / remaining requirements

Scenario **9983437** `JURKO Armonie — import PDF na żądanie` was read: status `inactive`, 0 incomplete executions, Drive connection `ok`; execution list from 2026-11-07 returned 0 runs. Scenario accepts `pdf_url`, `folder_id`, `filename` but **contains no pre-upload duplicate guard**. We did not activate it or import anything without a confirmed new PDF that is genuinely absent.

Before declaring completion: reconcile every official vendor catalogue title to Drive, determine absent/archival/included-in-general/ZIP-only cases, verify each file's true manufacturer authorship and provenance, detect unexpected misfoldering among all 235 (registered 121 are matched), compare SHA-256 more broadly, and agree on whether cross-listing duplicates should be consolidated. No completion claim.
