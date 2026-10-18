"""Makes the tract's print templates and records where the QR code, link and "Given to you by" box are.

  resources/tract-tabloid.pdf   exactly 17 × 11 in (home or office printer, tabloid / 11×17 paper)
  resources/tract-bleed.pdf     17.25 × 11.25 in (print shop: 1/8 in bleed all round, trimmed to 17 × 11)
  resources/tract-boxes.json    for each size: the boxes in inches from the top-left of the sheet, and the card colour

The templates leave the QR code and link blank; tract.html draws the reader's QR code, link and details into them
with pdf-lib when Print is pressed. Re-run after any change to the tract's text, pictures or layout:
    python3 -m http.server 8765 &   then   python3 tools/tract_pdf.py
Needs Playwright's Chromium (Chromium writes PDFs at the exact @page size).
"""
import asyncio, glob, json
from playwright.async_api import async_playwright

SIZES = {'tabloid': ('17in', '11in', ''), 'bleed': ('17.25in', '11.25in', '&bleed=1')}

async def main():
    exe = (glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome') or [None])[0]
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=exe) if exe else await p.chromium.launch()
        for size, (w, h, extra) in SIZES.items():
            pg = await b.new_page(viewport={'width': 1800, 'height': 1200})
            await pg.goto(f'http://localhost:8765/tract.html?lang=en&base=1{extra}')
            await pg.evaluate("localStorage.clear()")
            await pg.goto(f'http://localhost:8765/tract.html?lang=en&base=1{extra}')
            await pg.wait_for_load_state('networkidle'); await pg.wait_for_timeout(800)
            await pg.emulate_media(media='print')
            boxes = await pg.evaluate("""() => {
                const sheet = document.querySelector('.sheet').getBoundingClientRect(), PX = 96;
                const box = el => { const r = el.getBoundingClientRect(); return { x: (r.left - sheet.left) / PX, y: (r.top - sheet.top) / PX, w: r.width / PX, h: r.height / PX }; };
                const g = document.getElementById('giver'), lab = g.querySelector('.lab'), gb = box(g), lb = box(lab);
                const pad = 0.12, top = lb.y + lb.h + 0.01;
                return { qr: box(document.querySelector('.back .qr')), u: box(document.querySelector('.back .u')),
                         lines: { x: gb.x + pad, y: top, w: gb.w - 2 * pad, h: gb.y + gb.h - 0.07 - top },
                         card: getComputedStyle(document.querySelector('.back')).backgroundColor };
            }""")
            r, g_, b_ = [int(v) for v in boxes['card'].replace('rgba(', '').replace('rgb(', '').replace(')', '').split(',')[:3]]
            boxes['card'] = '#%02x%02x%02x' % (r, g_, b_)
            out[size] = boxes
            await pg.pdf(path=f'resources/tract-{size}.pdf', width=w, height=h, print_background=True, prefer_css_page_size=True)
            print(size, boxes)
            await pg.close()
        await b.close()
    json.dump(out, open('resources/tract-boxes.json', 'w'), indent=1)

asyncio.run(main())
