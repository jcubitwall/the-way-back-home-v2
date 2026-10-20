#!/usr/bin/env python3
"""Print booklet.html to PDF with Chromium.

  python3 tools/booklet_pdf.py            -> resources/TWBH-Book-6x9-bleed.pdf (6.25 x 9.25 in, for the printer)
                                             resources/TWBH-Book-6x9.pdf       (trimmed 6 x 9 in, for reading)
  python3 tools/booklet_pdf.py --png DIR  -> also one PNG per page in DIR (for checking)
  --isbn 978-...                           -> print the ISBN on the Amazon imprint page

Also writes the Amazon KDP paperback files (premium colour, 6 x 9, bleed) into resources/kdp/:
  TWBH-KDP-interior.pdf  48 pages, 6.125 x 9.25 in: KDP title page, book pages 2-47, imprint page.
                         Page 2 lands on a left page again, so the map (4-5) and long road (20-21) stay spreads.
  TWBH-KDP-cover.pdf     one wrap-around page: back (p48) + plain spine + front (p1).
"""
import sys, threading, http.server, functools, pathlib
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
png = sys.argv[sys.argv.index('--png') + 1] if '--png' in sys.argv else None
isbn = sys.argv[sys.argv.index('--isbn') + 1] if '--isbn' in sys.argv else ''
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Q, directory=str(root))
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{srv.server_port}/booklet.html'

with sync_playwright() as p:
    b = p.chromium.launch()
    (root / 'resources' / 'kdp').mkdir(exist_ok=True)
    for q, w, h, out in [('', '6.25in', '9.25in', 'TWBH-Book-6x9-bleed.pdf'), ('?trim', '6in', '9in', 'TWBH-Book-6x9.pdf'),
                         ('?kdp' + ('&isbn=' + isbn if isbn else ''), '6.25in', '9.25in', 'kdp/all-pages.pdf')]:
        pg = b.new_page()
        pg.goto(base + q); pg.wait_for_selector('body[data-ready]', timeout=60000)
        pg.add_style_tag(content=f'@page{{size:{w} {h};margin:0}}')
        pg.pdf(path=str(root / 'resources' / out), width=w, height=h, print_background=True, prefer_css_page_size=False)
        print('wrote resources/' + out)
        if png and q == '?trim':
            pathlib.Path(png).mkdir(parents=True, exist_ok=True)
            pg.set_viewport_size({'width': 700, 'height': 1000})
            for i, el in enumerate(pg.query_selector_all('.page')):
                el.screenshot(path=f'{png}/p{i + 1:02d}.png')
            print('pngs in', png)
    b.close()
srv.shutdown()

# Print-shop files for "48 pages plus cover": the cover sheet (heavier stock) is 4 pages
# (outside front = p1, inside front = p2 welcome, inside back = p47 QR page, outside back = p48),
# and the inside is p3-p46 (44 pages, a multiple of 4). Page numbers printed on the pages stay as they are.
from pypdf import PdfReader, PdfWriter
src = PdfReader(str(root / 'resources' / 'TWBH-Book-6x9-bleed.pdf'))
n = len(src.pages)
cov, ins = PdfWriter(), PdfWriter()
for i in (0, 1, n - 2, n - 1): cov.add_page(src.pages[i])
for i in range(2, n - 2): ins.add_page(src.pages[i])
cov.write(str(root / 'resources' / 'TWBH-Book-6x9-cover-bleed.pdf'))
ins.write(str(root / 'resources' / 'TWBH-Book-6x9-interior-bleed.pdf'))
print('wrote cover (4 pages) and interior (%d pages) print files' % (n - 4))

# ---------- Amazon KDP (paperback, premium colour, 6 x 9 with bleed) ----------
from pypdf import PageObject, Transformation
from pypdf.generic import RectangleObject
import io
from reportlab.pdfgen import canvas
B = 9                                    # 0.125 in bleed in points
k = PdfReader(str(root / 'resources' / 'kdp' / 'all-pages.pdf'))
n = len(k.pages)                         # 48 book pages + title (n-2) + imprint (n-1)
W, Hh = float(k.pages[0].mediabox.width), float(k.pages[0].mediabox.height)   # 450 x 666
order = [n - 2] + list(range(1, 47)) + [n - 1]
out = PdfWriter()
for i, src_i in enumerate(order):
    pg = PageObject.create_blank_page(width=W - B, height=Hh)
    # odd KDP page = right-hand page: drop the bleed on its left (spine) edge; even = left-hand page: drop it on the right
    pg.merge_transformed_page(k.pages[src_i], Transformation().translate(-B if i % 2 == 0 else 0, 0))
    out.add_page(pg)
out.write(str(root / 'resources' / 'kdp' / 'TWBH-KDP-interior.pdf'))
pages_kdp = len(order)
spine = pages_kdp * 0.002347 * 72        # KDP premium colour paper
CW = 2 * (W - B) + spine
cov = PageObject.create_blank_page(width=CW, height=Hh)
cov.merge_transformed_page(k.pages[n - 3], Transformation())                       # back cover (book p48), left
cov.merge_transformed_page(k.pages[0], Transformation().translate(W - B + spine - B, 0))  # front cover (p1), right
buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(CW, Hh))
c.setFillColorRGB(0x14 / 255, 0x11 / 255, 0x2b / 255); c.rect(W - B, 0, spine, Hh, stroke=0, fill=1); c.save()
cov.merge_page(PdfReader(buf).pages[0])
cw = PdfWriter(); cw.add_page(cov); cw.write(str(root / 'resources' / 'kdp' / 'TWBH-KDP-cover.pdf'))
(root / 'resources' / 'kdp' / 'all-pages.pdf').unlink()
print('wrote KDP interior (%d pages, %.3f x %.2f in) and cover (%.4f x %.2f in, spine %.4f in)'
      % (pages_kdp, (W - B) / 72, Hh / 72, CW / 72, Hh / 72, spine / 72))

# ---------- lighter reading copy (screens, email): pictures at ~150 dpi ----------
from PIL import Image as _I
rd = PdfReader(str(root / 'resources' / 'TWBH-Book-6x9.pdf')); wr = PdfWriter(clone_from=rd)
for pg in wr.pages:
    for im in pg.images:
        if im.image.width > 1000:
            p = im.image.convert('RGB'); p.thumbnail((p.width // 2, p.height // 2), _I.LANCZOS)
            im.replace(p, quality=80)
wr.compress_identical_objects()
wr.write(str(root / 'resources' / 'TWBH-Book-6x9.pdf'))
print('reading copy made lighter')
