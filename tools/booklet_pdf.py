#!/usr/bin/env python3
"""Print booklet.html to PDF with Chromium.

  python3 tools/booklet_pdf.py            -> resources/TWBH-Book-6x9-bleed.pdf (6.25 x 9.25 in, for the printer)
                                             resources/TWBH-Book-6x9.pdf       (trimmed 6 x 9 in, for reading)
  python3 tools/booklet_pdf.py --png DIR  -> also one PNG per page in DIR (for checking)
"""
import sys, threading, http.server, functools, pathlib
from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
png = sys.argv[sys.argv.index('--png') + 1] if '--png' in sys.argv else None
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Q, directory=str(root))
srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), H)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f'http://127.0.0.1:{srv.server_port}/booklet.html'

with sync_playwright() as p:
    b = p.chromium.launch()
    for q, w, h, out in [('', '6.25in', '9.25in', 'TWBH-Book-6x9-bleed.pdf'), ('?trim', '6in', '9in', 'TWBH-Book-6x9.pdf')]:
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
