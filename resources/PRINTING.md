# The Way Back Home: printed book, ready-to-print files

All files are made by `python3 tools/booklet_pdf.py` (add `--isbn 978-…` to print the ISBN on the Amazon imprint page).
Rebuild after any change to `booklet.html` or a picture in `art/hd/`.

## 1. Amazon KDP (paperback, sold on Amazon.ca / .com, printed on demand)

| Upload slot | File |
|---|---|
| Manuscript | `resources/kdp/TWBH-KDP-interior.pdf`: 48 pages, 6.125 × 9.25 in |
| Cover | `resources/kdp/TWBH-KDP-cover.pdf`: one page, 12.363 × 9.25 in |

Settings to choose in KDP:
- **Ink and paper:** Premium colour, white paper
- **Trim size:** 6 × 9 in
- **Bleed:** Yes (bleed)
- **Cover finish:** Matte
- **Page count:** 48 (the cover file is made for exactly this: spine 0.1127 in, plain navy, no spine text, as KDP requires under 79 pages)
- **Barcode:** let KDP add it. The lower right of the back cover is kept clear for it.
- **AI-generated content:** answer Yes (pictures).
- **ISBN:** free KDP ISBN, or your own from ISBN Canada. If you use your own, rebuild with `--isbn` so it appears on the imprint page.

Interior order: title page, book pages 2–47, imprint (copyright) page. Book page 2 lands on a left-hand page, so the
road map (pages 4–5) and the long road (pages 20–21) open as two-page spreads, the same as in the stapled book.
Pages 1 and 48 of the stapled book are the KDP cover.

**Order one printed proof before publishing** and check the colours and the spreads.

## 2. Stapled booklet from an offset or digital printer (church giveaways, bulk)

Spec to quote: 6 × 9 in, 48 pages plus cover, full colour both sides, saddle stitched,
~100 lb gloss or silk text, ~100 lb cover, matte, PDF with 0.125 in bleed.

| Option | Files |
|---|---|
| One file, self-cover (48 pages, all the same paper) | `resources/TWBH-Book-6x9-bleed.pdf` (6.25 × 9.25 in per page) |
| Thicker cover ("44 pages + 4-page cover") | `resources/TWBH-Book-6x9-cover-bleed.pdf` (p1, p2, p47, p48) and `resources/TWBH-Book-6x9-interior-bleed.pdf` (p3–p46) |

Reading copy (no bleed, for screens and email): `resources/TWBH-Book-6x9.pdf`.

## Checks done (20 Oct 2026)
- Every font embedded. Every picture at least ~180 dpi at printed size, most 290–300 dpi.
- All text at least 0.3 in inside the trim.
- QR codes open https://thewaybackhome.net/.
- Bible quotes checked word for word against the CSB; paraphrases have no quote marks.
- Files are RGB (KDP and most printers convert). Ask an offset printer for a hard-copy proof, because colours shift a little in CMYK.
