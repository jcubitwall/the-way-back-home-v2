"""Classroom posters for Sunday school (ages 6–9): one full-colour US Letter sheet per week for the wall.
Picture (print-quality, art/print) on top, the week's big idea and memory verse on the chapter colour below."""
import sys, html
sys.path.insert(0, '/tmp/claude-0/gen')
from content69 import WEEKS
from content import CSB

esc = html.escape
B = '/tmp/claude-0/build'
ART = '/root/twbh/art/print'
# picture, which part to keep in view (vertical %)
PIC = {1: ('garden-end', 40), 2: ('fruit-end', 30), 3: ('test-2-end', 38), 4: ('scrub-clip', 28),
       5: ('cross-kneel', 62), 6: ('tomb-end', 45), 7: ('gates-run', 40)}

BAND = {6: '#b07a00'}   # week 6 gold darkened so white text reads well

CSS = '''
@page { size: letter; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: 'Andika', sans-serif; }
.p { width: 8.5in; height: 11in; position: relative; overflow: hidden; page-break-after: always; }
.p:last-child { page-break-after: auto; }
.pic { position: absolute; top: 0; left: 0; width: 8.5in; height: 6.75in; overflow: hidden; }
.pic img { width: 100%; height: 100%; object-fit: cover; display: block; }
.wk { position: absolute; top: .35in; left: .35in; background: #fff; border-radius: 99px; padding: 5pt 16pt; font: 900 15pt 'Grandstander'; letter-spacing: .03em; }
.band { position: absolute; top: 6.75in; left: 0; width: 8.5in; height: 4.25in; color: #fff; padding: .3in .5in .3in; }
.title { font: 900 13pt 'Grandstander'; letter-spacing: .14em; text-transform: uppercase; opacity: .85; margin: 0 0 .06in; }
.big { font: 900 34pt/1.05 'Grandstander'; margin: 0 0 .2in; }
.verse { font: 700 18pt/1.4 'Andika'; margin: 0; padding-top: .16in; border-top: 2px solid rgba(255,255,255,.45); }
.ref { display: block; font: 900 15pt 'Grandstander'; margin-top: .06in; color: #FFD166; }
.foot { position: absolute; left: .5in; right: .5in; bottom: .22in; font-size: 6.5pt; opacity: .7; margin: 0; }
'''

def poster(w):
    img, y = PIC[w['n']]
    return (f'<div class="p"><div class="pic"><img src="file://{ART}/{img}.jpg" style="object-position:50% {y}%"><span class="wk" style="color:{w["col"]}">WEEK {w["n"]}</span></div>'
            f'<div class="band" style="background:{BAND.get(w["n"], w["col"])}"><p class="title">{esc(w["title"])}</p><p class="big">{esc(w["big"])}</p>'
            f'<p class="verse">“{esc(w["verse"][0])}”<span class="ref" style="{'color:#fff' if w['n'] in BAND else ''}">{esc(w["verse"][1])}</span></p>'
            f'<p class="foot">The Way Back Home · thewaybackhome.net · {CSB}</p></div></div>')

if __name__ == '__main__':
    import weasyprint
    h = f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="fonts.css"><style>{CSS}</style></head><body>{"".join(poster(w) for w in WEEKS)}</body></html>'
    open(f'{B}/posters69.html', 'w').write(h)
    weasyprint.HTML(f'{B}/posters69.html', base_url=B).write_pdf(f'{B}/posters69.pdf')
    print('ok')
