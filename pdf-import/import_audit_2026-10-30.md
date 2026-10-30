# JURKO PDF — audit 2026-10-30

## Import outcome
Six new official PDFs uploaded using Make on-demand scenario 9983437: **5 Atlas Concorde** and **1 Century**. Each run returned success, a Google Drive file ID, MIME application/pdf, and a nonzero size. Independent Google Drive folder listings confirmed all six exact names, sizes, and MIME types. Five Atlas Concorde collection folders were created; Century Large Sizes was placed in the Century manufacturer root. No pre-existing files were overwritten.

| Manufacturer | Collection / document | Verified Drive PDF | Bytes | Official PDF URL |
|---|---|---|---:|---|
| Atlas Concorde | Boost Mix | https://drive.google.com/file/d/1zaO_wC2hOuu-Xt6lG0TQiKU-1WbcwRRC/view | 24112991 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/e9215e18-93f1-4ac9-9877-feb5a2dc0fc6/u38j94/WEB/AtlasConcorde_BoostMix_Catalogue_2022-04.pdf |
| Atlas Concorde | Marvel Travertine | https://drive.google.com/file/d/1fcaVTo-w2oAZ-OSsw8yuzfiH7l72krUh/view | 32869838 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/06270ec0-00c8-46b5-bb37-0d3722c0840f/u38j94/WEB/AtlasConcorde_MarvelTravertine_Catalogue_2023-05.pdf |
| Atlas Concorde | Heartwood | https://drive.google.com/file/d/1IzX8H97epoxHQWIH5tbOlG8bGlGR1a_D/view | 11219180 | https://gruppoconcorde-cdn.thron.com/static/N1EXWQ_AtlasConcorde_Heartwood_Catalogue_2019-04_B5S8MM.pdf |
| Atlas Concorde | Boost Expression | https://drive.google.com/file/d/1i7s1ilXQiRHfKfAa65XB0T2kUq5yLPs6/view | 13722627 | https://gruppoconcorde-cdn.thron.com/delivery/public/document/gruppoconcorde/368361f3-ea19-45cf-bce8-4cf9fcc2b2f3/u38j94/WEB/AtlasConcorde_Boost_Expression_Catalog_2024-09.pdf |
| Atlas Concorde | Marvel Diva | https://drive.google.com/file/d/1K_w9nGLSnMUXl8mnbpjxJPcCmZ9Ci1dw/view | 21756806 | https://gruppoconcorde-cdn.thron.com/static/AT1OWP_AtlasConcorde_MarvelDiva_Catalog_2025-11_LG4TXT.pdf |
| Century | Large Sizes | https://drive.google.com/file/d/1Yet773e02jp6ba5Oeo2hAMGILA2CjN-C/view | 11663818 | https://www.century-ceramica.it/wp-content/uploads/2025/04/LARGE-SIZES.pdf |

Total new bytes: 115345260. Verification is metadata/readback only; **no SHA256 full-byte verification** and no content-level duplicate comparison were performed.

## Current scope and incomplete work
- Previous 2026-10-29 audit counted 213 PDF entries across the 11 manufacturer roots and immediate subfolders. Adding these six verified files gives **219 entries estimated**, assuming no unrelated deletions/changes. This is not a new exhaustive recount and is not a unique-content count.
- Atlas Concorde now has **15 entries estimated** (10 previously + 5 new); the official Download Area displays 58 catalogues across Atlas Concorde, Habitat, Plan, and related categories. Full category-by-category reconciliation is incomplete. https://www.atlasconcorde.com/en/download-area
- Century now has **19 entries estimated** (18 previously + Large Sizes). The official download page additionally lists Outdoor. Organizer appears to be a general catalogue, but equivalence to the existing general PDF has not been proven. https://www.century-ceramica.it/download/
- Cotto Petrus folders Spaccone, Rangers OUT, Galaxy OUT were independently listed today and **remain empty**. Its official download page lists Spaccone and Rangers OUT, but a direct verified standalone PDF source was not identified today. https://www.cottopetrus.it/download/s5cb0a778
- Cotto Petrus/Columbia contains COTTO_PETRUS_COLUMBIA_2023.pdf (628890 bytes), while its GitHub CSV source URL contains Soho. This is a **content mapping discrepancy requiring verification**, not proof that the file is Columbia. No replacement or renaming was attempted.
- Coverage checks for the other manufacturers still require official inventory comparison. Some items are older editions (e.g. Heartwood 2019); current-edition availability remains to be checked.
- All six sources and five Atlas collection folder IDs were added to catalogues.csv and collection_folders.csv.
- Import is **not complete**; do not announce final completion or disable the recurring audit.
