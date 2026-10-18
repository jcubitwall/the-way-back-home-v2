import sys, random, re
sys.path.insert(0, '/tmp/claude-0/gen')
from art import *
import build as LB
from build import img, esc, qr_svg, FONTS, KCSS, ICON_CRAYON, ICON_PENCIL, ICON_SCISSORS, ICON_EYE, brick_wall, cloud
from content69 import WEEKS
from content import CSB, SITE

B = '/tmp/claude-0/build'
SER = 'The Way Back Home · Ages 6–9'
for w in WEEKS: w['say'] = w['big']

CSS = KCSS + '''
.khead h1 { font-size: 25pt; }
.khead .sayit { font-size: 11.5pt; }
.task { font-size: 14.5pt; }
.task .ic { width: .46in; height: .46in; }
.lines div { border-bottom: 1.6px solid #9a93a6; height: .42in; }
.wb { display: flex; flex-wrap: wrap; gap: 6pt; justify-content: center; margin: .06in 0 .1in; }
.wb span { border: 2px solid #1d1a24; border-radius: 99px; padding: 2pt 12pt; font: 800 13pt 'Grandstander'; }
.verse-fill { font: 700 17pt 'Andika'; line-height: 2.05; text-align: center; padding: .1in .2in; border-radius: .16in; }
.blank { display: inline-block; border-bottom: 2.5px solid #1d1a24; min-width: 1.2in; height: 1em; vertical-align: baseline; }
.ref { font: 900 14pt 'Grandstander'; text-align: center; }
.tt { display: flex; align-items: center; gap: .12in; padding: .1in .14in; border-radius: .12in; font-size: 13.5pt; }
.tt:nth-child(odd) { background: #f6f4f9; }
.tt .q { flex: 1; }
.chip { border: 2.5px solid #1d1a24; border-radius: 99px; padding: 2pt 10pt; font: 900 11pt 'Grandstander'; }
.panel { width: 2.45in; }
.panel .ph { position: relative; width: 2.45in; height: 4.0in; border: 3px solid #1d1a24; border-radius: .12in; overflow: hidden; }
.panel .ph img { width: 100%; height: 100%; object-fit: cover; }
.panel .bub { position: absolute; left: .12in; right: .12in; top: .12in; height: 1.0in; background: #fff; border: 2.5px solid #1d1a24; border-radius: 50%; }
.panel .n { position: absolute; bottom: .08in; left: .08in; width: .42in; height: .42in; border-radius: 50%; color: #fff; text-align: center; font: 900 15pt Grandstander; line-height: .42in; border: 2px solid #fff; }
.drawbox { border: 2.5px dashed #9a93a6; border-radius: .16in; position: relative; }
.drawbox span { position: absolute; top: .08in; left: .14in; font: 800 12pt 'Grandstander'; color: #9a93a6; }
.ws { display: grid; gap: 0; border: 3px solid #1d1a24; border-radius: .1in; overflow: hidden; }
.ws div { font: 800 17pt 'Andika'; text-align: center; height: .44in; line-height: .44in; border-right: 1px solid #e3dfe9; border-bottom: 1px solid #e3dfe9; }
.cw td { width: .4in; height: .4in; padding: 0; position: relative; }
.cw td.on { border: 2px solid #1d1a24; background: #fff; }
.cw td small { position: absolute; top: 1px; left: 3px; font: 800 7.5pt 'Andika'; }
.key { display: flex; flex-wrap: wrap; gap: 4pt; justify-content: center; }
.key div { border: 1.5px solid #c9c2d4; border-radius: 6pt; width: .5in; text-align: center; font: 800 11pt 'Grandstander'; padding: 2pt 0; }
.code { display: flex; flex-wrap: wrap; justify-content: center; gap: 4pt 3pt; margin: .1in 0; }
.code .c { width: .44in; text-align: center; }
.code .c .b { border-bottom: 2px solid #1d1a24; height: .36in; }
.code .c .s { font: 800 11pt 'Grandstander'; color: #5b5468; height: .34in; }
.code .gap { width: .3in; }
'''

def kfoot(w, label='page'):
    return (f'<div class="name"><span>My name:<span class="l"></span></span></div>'
            f'<div class="foot"><span>{SER} · {SITE}</span><span>Week {w["n"]}</span></div>')

def khead(w, n): return LB.khead(w, n)

def grownups(w):
    return (f'<div class="grownups"><div class="q">{qr_svg()}</div><div><b>For grown-ups:</b> listen to <i>The Way Back Home</i> together at <b>{SITE}</b> (this week: {esc(w["book"])}). '
            f'<b>Memory verse:</b> {esc(w["verse"][1])}. <b>Ask:</b> {esc(w["ask"])}<br><b>Live it this week:</b> {esc(w["live"])}</div></div>')

def page(w, n, task_ic, task, body, home=False):
    return (f'<div class="page">{khead(w, n)}<div class="task">{task_ic}{esc(task)}</div>{body}'
            f'{grownups(w) if home else ""}{kfoot(w)}</div>')

def wordbank(words): return '<div class="wb">' + ''.join(f'<span>{esc(x)}</span>' for x in words) + '</div>'

def fill_verse(w, text, blanks, bg):
    out = esc(text)
    for b in blanks:
        out = re.sub(r'\b' + re.escape(b) + r'\b', '<span class="blank"></span>', out, count=1)
    return f'<div class="verse-fill" style="background:{bg}">“{out}”</div>'

def lines(k, h=.42): return '<div class="lines">' + ''.join(f'<div style="height:{h}in"></div>' for _ in range(k)) + '</div>'

# ---------------- week 1 ----------------
def day_icon(d):
    if d == 1: return f'<g><circle r="40" {K}/><path d="M0-40a40 40 0 0 1 0 80z" fill="{INK}"/></g>'
    if d == 2: return f'<g>{cloud(-50, -14)}<path d="M-50 30q12-12 25 0t25 0 25 0 25 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/><path d="M-50 48q12-12 25 0t25 0 25 0 25 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></g>'
    if d == 3: return f'<g transform="translate(-16 -6) scale(.16) translate(-300 -222)">{tree()}</g>{flower(34, -4, .7)}<path d="M-56 36h112" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    if d == 4: return f'{sun(-22, -6, 18)}<path d="M40 -40a24 24 0 1 0 14 40a20 20 0 1 1-14-40z" {K4}/><path d="M30 34l5 11 12 1-9 8 3 12-11-6-11 6 3-12-9-8 12-1z" {K4}/>'
    if d == 5: return fish(-20, 24, .9) + f'<g transform="translate(30 -24) scale(.8)">{i_bird()}</g>'
    return kid(-26, 28, .6) + f'<g transform="translate(32 18) scale(.6)">{i_dog()}</g>'

def w1_p1(w):
    words = {1: 'Light: day and night', 2: 'Sky and water', 3: 'Land and plants', 4: 'Sun, moon, stars', 5: 'Fish and birds', 6: 'Animals and people'}
    order = [4, 1, 6, 2, 5, 3]
    s = '<svg viewBox="0 0 760 640" style="width:7.66in;height:6.45in">'
    for i in range(6):
        y = 55 + i * 105
        s += (f'<rect x="10" y="{y-40}" width="250" height="80" rx="18" fill="{w["soft"]}"/><text x="30" y="{y-6}" font-family="Grandstander" font-weight="900" font-size="28" fill="{w["col"]}">Day {i+1}</text>'
              f'<text x="30" y="{y+24}" font-family="Andika" font-weight="700" font-size="18">{words[i+1]}</text><circle cx="285" cy="{y}" r="9" fill="{INK}"/>')
        s += f'<circle cx="470" cy="{y}" r="9" fill="{INK}"/><rect x="500" y="{y-48}" width="240" height="96" rx="18" fill="#f6f4f9"/><g transform="translate(620 {y}) scale(.8)">{day_icon(order[i])}</g>'
    s += '</svg>'
    s += f'<p style="font:800 13pt Grandstander;text-align:center;margin:.06in 0 0">And on day 7? God rested. Read it in Genesis 2:2!</p>'
    return page(w, 1, ICON_PENCIL, 'What did God make each day? Draw a line from each day to its picture.', s)

def w1_p2(w):
    body = (fill_verse(w, w['verse'][0], ['saw', 'made', 'very', 'good'], w['soft']) + wordbank(['good', 'saw', 'very', 'made'])
            + f'<div class="ref">Genesis <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>'
            + f'<div class="drawbox" style="height:3.15in;margin-top:.14in"><span>Draw your favourite thing God made!</span></div>')
    return page(w, 2, ICON_PENCIL, 'Fill in the missing words. Then draw!', body, home=True)

def comic(w, frames, prompt, bubbles=(False, False, False), lines_n=3):
    pan = ''
    for i, f in enumerate(frames):
        bub = (f'<svg viewBox="0 0 240 100" style="width:2.45in;height:1.0in;display:block"><ellipse cx="120" cy="44" rx="114" ry="40" fill="#fff" stroke="{INK}" stroke-width="3"/>'
               f'<circle cx="70" cy="90" r="6" fill="#fff" stroke="{INK}" stroke-width="2.5"/><circle cx="58" cy="98" r="3.5" fill="#fff" stroke="{INK}" stroke-width="2"/></svg>') if bubbles[i] else ''
        ph_h = '3.1in' if any(bubbles) else '4.0in'
        pan += (f'<div class="panel">{bub}<div class="ph" style="height:{ph_h};margin-top:{".02in" if bub else "0"}">{img(f, style="object-position:50% 0%")}<div class="n" style="background:{w["col"]}">{i+1}</div></div>'
                f'{lines(lines_n, .4)}</div>')
    return f'<div style="display:flex;justify-content:space-between;margin-top:.04in">{pan}</div><p class="small" style="font:800 11pt Grandstander;color:#6b6478;margin:.08in 0 0">{esc(prompt)}</p>'

def w1_p3(w):
    panels = [('garden-end', 'What is God saying to Adam and Eve?'), ('rule-point', 'What is Adam saying to Eve?')]
    pan = ''
    for i, (f, q) in enumerate(panels):
        bub = (f'<svg viewBox="0 0 360 120" style="width:3.72in;height:1.24in;display:block"><path d="M30 8h300a22 22 0 0 1 22 22v52a22 22 0 0 1-22 22H{300 if i == 0 else 200}l-22 16 4-16H30a22 22 0 0 1-22-22V30A22 22 0 0 1 30 8z" fill="#fff" stroke="{INK}" stroke-width="3"/></svg>')
        pan += (f'<div style="width:3.72in">{bub}<div class="ph" style="position:relative;width:3.72in;height:4.1in;margin-top:.03in;border:3px solid {INK};border-radius:.12in;overflow:hidden">'
                f'{img(f, style="width:100%;height:100%;object-fit:cover;object-position:50% 55%")}<div class="n" style="position:absolute;bottom:.08in;left:.08in;width:.42in;height:.42in;border-radius:50%;color:#fff;text-align:center;font:900 15pt Grandstander;line-height:.42in;border:2px solid #fff;background:{w["col"]}">{i+1}</div></div>'
                f'<p style="font:800 11pt Grandstander;color:#6b6478;margin:.06in 0 0">{esc(q)}</p>{lines(3, .42)}</div>')
    body = f'<div style="display:flex;justify-content:space-between;margin-top:.04in">{pan}</div>'
    return page(w, 3, ICON_PENCIL, 'Comic strip! Write what they are saying in the speech bubbles. Then write what happens.', body)

# ---------------- week 2 ----------------
TT = [('God made everything good.', 'TRUE'), ('You may eat from every tree in the garden but one.', 'TRUE'), ('“Did God really say that?”', 'TRICK'),
      ('“You won’t die!”', 'TRICK'), ('“That fruit will make you like God!”', 'TRICK'), ('Sin means not trusting and obeying God.', 'TRUE'),
      ('God made Adam and Eve clothes.', 'TRUE'), ('God promised Someone would come to open the way back home.', 'TRUE')]
def w2_p1(w):
    rows = ''.join(f'<div class="tt"><span class="q">{i+1}. {esc(q)}</span><span class="chip" style="color:#1e9e5a">TRUE</span><span class="chip" style="color:#e0453a">TRICK</span></div>' for i, (q, a) in enumerate(TT))
    body = (f'<p style="font-size:12pt;margin:0 0 .08in">Did God say it, or is it true about God (<b>TRUE</b>)? Or did the sneaky serpent say it (<b>TRICK</b>)? Circle one.</p>{rows}'
            f'<div class="drawbox" style="height:1.5in;margin-top:.14in"><span>The serpent tried to trick Eve. Draw the serpent below!</span></div>')
    return page(w, 1, ICON_EYE, 'True or trick?', body)

SHAPES = ['circle', 'square', 'tri', 'star', 'heart', 'diamond', 'plus', 'moon', 'hex', 'drop', 'arrow', 'flower', 'bolt']
def shape(nm, x=0, y=0, s=1.0):
    k = f'fill="#fff" stroke="{INK}" stroke-width="3"'
    d = {'circle': f'<circle r="11" {k}/>', 'square': f'<rect x="-10" y="-10" width="20" height="20" {k}/>', 'tri': f'<path d="M0-12L12 10H-12z" {k}/>',
         'star': f'<path d="M0-13l4 8 9 1-7 6 2 9-8-5-8 5 2-9-7-6 9-1z" {k}/>', 'heart': f'<path d="M0 12C-14 2-14-10-6-10c4 0 6 3 6 5 0-2 2-5 6-5 8 0 8 12-6 22z" {k}/>',
         'diamond': f'<path d="M0-13L11 0 0 13-11 0z" {k}/>', 'plus': f'<path d="M-4-12h8v8h8v8h-8v8h-8v-8h-8v-8h8z" {k}/>', 'moon': f'<path d="M4-12a12 12 0 1 0 0 24a9 9 0 1 1 0-24z" {k}/>',
         'hex': f'<path d="M-6-11h12l6 11-6 11h-12l-6-11z" {k}/>', 'drop': f'<path d="M0-13C6-4 10 2 10 6a10 10 0 0 1-20 0c0-4 4-10 10-19z" {k}/>',
         'arrow': f'<path d="M-12-4h12v-7l12 11-12 11v-7h-12z" {k}/>', 'flower': ''.join(f'<circle cx="{7*math.cos(math.radians(a)):.1f}" cy="{7*math.sin(math.radians(a)):.1f}" r="5" {k}/>' for a in range(0, 360, 72)) + f'<circle r="4" {k}/>',
         'bolt': f'<path d="M3-13L-8 2h7l-3 11L9-2H2z" {k}/>'}[nm]
    return f'<g transform="translate({x} {y}) scale({s})">{d}</g>'

def symbol_code(msg):
    letters = []
    for ch in msg:
        if ch.isalpha() and ch not in letters: letters.append(ch)
    rnd = random.Random(5); keyord = sorted(letters, key=lambda c: rnd.random())
    sym = {c: SHAPES[i] for i, c in enumerate(keyord)}
    key = ''.join(f'<div><svg viewBox="-16 -16 32 32" style="width:.34in;height:.34in;margin:0 auto">{shape(sym[c])}</svg>{c}</div>' for c in sorted(letters))
    cells = ''
    for word in msg.split():
        cells += ''.join(f'<div class="c"><div class="b"></div><svg viewBox="-16 -16 32 32" style="width:.36in;height:.36in;margin:3pt auto 0">{shape(sym[c])}</svg></div>' for c in word) + '<div class="gap"></div>'
    return key, cells

def w2_p2(w):
    key, cells = symbol_code('EVERY WORD OF GOD IS PURE')
    body = (f'<div class="key">{key}</div><div class="code">{cells}</div>'
            f'<p style="font-size:13pt;text-align:center;margin:.04in 0">Now finish the verse:</p>'
            f'<div class="verse-fill" style="background:{w["soft"]};font-size:15pt">“…he is a <span class="blank"></span> to those who take refuge in him.”</div>'
            f'<div class="ref" style="margin-top:.06in">Proverbs <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>')
    return page(w, 2, ICON_EYE, 'Crack the code! Use the key to find the secret words.', body, home=True)

def spiral_svg(col):
    pts, pts2 = [], []
    a, b = 6, 9.2
    for i in range(0, 1380):
        t = i / 60
        r = a + b * t
        pts.append((380 + r * math.cos(t), 330 + r * math.sin(t)))
    d = 'M' + ' L'.join(f'{x:.1f} {y:.1f}' for x, y in pts[200:])
    R = a + b * 23
    dots = ''
    rnd = random.Random(3)
    for i in range(260, 1360, 38):
        t = i / 60; r = a + b * t + b * math.pi
        dots += f'<circle cx="{380 + r*math.cos(t):.1f}" cy="{330 + r*math.sin(t):.1f}" r="{rnd.choice([6,8,10])}" fill="none" stroke="{INK}" stroke-width="3"/>'
    head = (f'<ellipse cx="380" cy="330" rx="52" ry="40" {K}/><circle cx="364" cy="318" r="7" fill="{INK}"/><circle cx="396" cy="318" r="7" fill="{INK}"/>'
            f'<path d="M380 370v22m0 0l-9 10m9-10l9 10" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            f'<text x="380" y="350" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="15">TRUST GOD!</text>')
    return (f'<svg viewBox="0 0 760 660" style="width:7.0in;height:6.08in;margin:0 auto"><circle cx="380" cy="330" r="{R+18:.0f}" fill="#fff" stroke="{INK}" stroke-width="3" stroke-dasharray="12 9"/>'
            f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="12 9"/>{dots}{head}</svg>')

def w2_p3(w):
    body = spiral_svg(w['col']) + '<p style="font:800 12pt Grandstander;text-align:center;margin:.04in 0 0">1 Colour the snake · 2 Cut around the big circle · 3 Cut along the dashed spiral to the head · 4 Hang it from a string</p>'
    return page(w, 3, ICON_SCISSORS, 'Make a twisty snake! The serpent lied, so who do we trust?', body)

# ---------------- week 3 ----------------
WS_WORDS = ['ADAM', 'EVE', 'ROAD', 'PEOPLE', 'SIN', 'LAW', 'MIRROR', 'TEN', 'RULES', 'LIE', 'ALL', 'HEART']
def wordsearch(words, n=11, seed=9):
    rnd = random.Random(seed)
    for attempt in range(500):
        g = [[''] * n for _ in range(n)]; ok_all = True
        for wd in sorted(words, key=len, reverse=True):
            placed = False
            for _ in range(400):
                dy, dx = rnd.choice([(0, 1), (1, 0)])
                y = rnd.randrange(n - dy * (len(wd) - 1)); x = rnd.randrange(n - dx * (len(wd) - 1))
                if all(g[y+dy*k][x+dx*k] in ('', wd[k]) for k in range(len(wd))):
                    for k in range(len(wd)): g[y+dy*k][x+dx*k] = wd[k]
                    placed = True; break
            if not placed: ok_all = False; break
        if not ok_all: continue
        AB = 'BCDFGHJKMNPQSTUVWXYZ'
        for y in range(n):
            for x in range(n):
                if not g[y][x]: g[y][x] = rnd.choice(AB)
        rows = [''.join(r) for r in g]; cols = [''.join(g[y][x] for y in range(n)) for x in range(n)]
        lines_ = rows + cols
        if all(sum(l.count(wd) for l in lines_) + (sum(l.count(wd[::-1]) for l in lines_) if wd != wd[::-1] else 0) == 1 for wd in words):
            return g
    raise SystemExit('wordsearch failed')

def w3_p1(w):
    g = wordsearch(WS_WORDS)
    n = len(g)
    cells = ''.join(f'<div>{c}</div>' for r in g for c in r)
    words = ''.join(f'<li style="font:800 14pt Grandstander;margin-bottom:5pt;list-style:none">☐ {x}</li>' for x in WS_WORDS)
    body = (f'<div style="display:flex;gap:.25in;align-items:flex-start"><div class="ws" style="grid-template-columns:repeat({n},.47in);width:{n*.47+.04:.2f}in">{cells}</div>'
            f'<ul style="padding:0;margin:0">{words}</ul></div>'
            f'<p style="font-size:12.5pt;margin:.14in 0 0">Words go <b>across →</b> and <b>down ↓</b>. Tick each one when you find it.</p>')
    return page(w, 1, ICON_EYE, 'Word search: find all 12 words from the story.', body)

def w3_p2(w):
    words = w['verse'][0].rstrip('.').split()
    rnd = random.Random(4); sc = words[:]; rnd.shuffle(sc)
    body = (f'<div class="wb" style="margin:.1in 0 .16in">{"".join(f"<span>{esc(x)}</span>" for x in sc)}</div>'
            f'<p style="font-size:13pt;margin:0">Write the verse in the right order:</p>{lines(3, .5)}'
            f'<div class="ref" style="margin-top:.1in">Romans <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>'
            f'<div style="display:flex;gap:.2in;align-items:center;margin-top:.18in;background:{w["soft"]};border-radius:.16in;padding:.12in .18in">'
            f'<div style="font-size:13pt">God’s law is like a <b>R O R I R M</b> (unscramble it!). It shows us our sin.<br><span class="blank" style="min-width:2.4in;margin-top:.1in"></span></div></div>')
    return page(w, 2, ICON_PENCIL, 'Verse scramble! The words got mixed up.', body, home=True)

def w3_p3(w):
    fr = ['road-clip', 'road-mid', 'road-end', 'test-end']; order = [2, 0, 3, 1]
    slots = ''.join(f'<div style="width:1.78in"><div class="slot" style="width:1.78in;height:2.75in"><b style="background:{w["col"]};width:.5in;height:.5in;font-size:22pt;line-height:.5in">{i+1}</b><i>glue here</i></div>{lines(2, .36)}</div>' for i in range(4))
    cards = ''.join(f'<div class="card" style="width:1.78in;height:2.75in">{img(fr[k])}</div>' for k in order)
    body = (f'<div class="slots">{slots}</div><div class="scissor-line"><span>✂</span></div><div class="cutrow">Cut on the dashed lines</div><div class="cards">{cards}</div>')
    return page(w, 3, ICON_SCISSORS, 'Cut out the 4 pictures. Glue them in order and write a sentence under each.', body)

# ---------------- week 4 ----------------
CW = [('MIRROR', 'God’s law is like a ___. It shows our sin.'), ('SOAP', 'The children tried to wash with water and ___.'), ('GIFT', 'Being saved is God’s ___.'),
      ('LOCKED', 'Sin ___ us out of God’s home.'), ('GATES', 'The golden ___ slammed shut.'), ('SORRY', 'Saying ___ is good, but it can’t wash sin away.'), ('GRACE', 'We are saved by ___ through faith.')]
def crossword(entries, seed=2):
    rnd = random.Random(seed)
    best = None
    for attempt in range(400):
        ws = entries[:]; rnd.shuffle(ws)
        grid = {}; placed = []
        def fits(word, x, y, d):
            dx, dy = (1, 0) if d == 'A' else (0, 1)
            if (x - dx, y - dy) in grid or (x + dx * len(word), y + dy * len(word)) in grid: return False
            cross = 0
            for k, ch in enumerate(word):
                p = (x + dx * k, y + dy * k)
                if p in grid:
                    if grid[p][0] != ch or d in grid[p][1]: return False
                    cross += 1
                else:
                    for s in (-1, 1):
                        if (p[0] + dy * s, p[1] + dx * s) in grid: return False
            return cross > 0 or not grid
        def put(word, x, y, d):
            dx, dy = (1, 0) if d == 'A' else (0, 1)
            for k, ch in enumerate(word):
                p = (x + dx * k, y + dy * k)
                grid[p] = (ch, grid.get(p, ('', ''))[1] + d)
        w0 = ws[0][0]; put(w0, 0, 0, 'A'); placed.append((ws[0], 0, 0, 'A'))
        for e in ws[1:]:
            word = e[0]; opts = []
            for (px, py), (ch, ds) in list(grid.items()):
                for k, c in enumerate(word):
                    if c != ch: continue
                    for d in 'AD':
                        x, y = (px - k, py) if d == 'A' else (px, py - k)
                        if fits(word, x, y, d): opts.append((x, y, d))
            if opts:
                x, y, d = rnd.choice(opts); put(word, x, y, d); placed.append((e, x, y, d))
        if len(placed) == len(entries):
            xs = [p[0] for p in grid]; ys = [p[1] for p in grid]
            area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
            if max(xs) - min(xs) < 14 and max(ys) - min(ys) < 13 and (best is None or area < best[0]):
                best = (area, dict(grid), list(placed))
    return best

def w4_p1(w):
    _, grid, placed = crossword(CW)
    xs = [p[0] for p in grid]; ys = [p[1] for p in grid]; x0, y0 = min(xs), min(ys)
    W_, H_ = max(xs) - x0 + 1, max(ys) - y0 + 1
    starts = sorted({(y - y0, x - x0) for (e, x, y, d) in placed})
    num = {s: i + 1 for i, s in enumerate(starts)}
    rows = ''
    for yy in range(H_):
        rows += '<tr>' + ''.join((f'<td class="on">{f"<small>{num[(yy, xx)]}</small>" if (yy, xx) in num else ""}</td>' if (xx + x0, yy + y0) in grid else '<td></td>') for xx in range(W_)) + '</tr>'
    acr = sorted((num[(y - y0, x - x0)], e[1]) for e, x, y, d in placed if d == 'A')
    dwn = sorted((num[(y - y0, x - x0)], e[1]) for e, x, y, d in placed if d == 'D')
    clue = lambda L: ''.join(f'<p style="margin:0 0 4pt;font-size:11.5pt"><b>{n}.</b> {esc(c)}</p>' for n, c in L)
    sz = min(.46, 4.3 / max(W_, 1), 4.9 / max(H_, 1))
    body = (f'<div style="display:flex;gap:.2in"><table class="cw" style="border-collapse:collapse">{rows.replace("<td", f"<td style=width:{sz:.2f}in;height:{sz:.2f}in")}</table>'
            f'<div style="flex:1"><h3 style="font-size:14pt;color:{w["col"]}">Across →</h3>{clue(acr)}<h3 style="font-size:14pt;color:{w["col"]};margin-top:.1in">Down ↓</h3>{clue(dwn)}</div></div>'
            + wordbank([e[0] for e in CW]))
    w4_p1.answer = '; '.join(f'{n} across {next(e[0] for e, x, y, d in placed if num[(y-y0, x-x0)] == n and d == "A")}' for n, _ in acr) + '; ' + '; '.join(f'{n} down {next(e[0] for e, x, y, d in placed if num[(y-y0, x-x0)] == n and d == "D")}' for n, _ in dwn)
    return page(w, 1, ICON_PENCIL, 'Crossword: use the clues and the word box.', body)

def w4_p2(w):
    tags = ''.join(f'<div style="text-align:center"><svg viewBox="0 0 160 150" style="width:1.6in;height:1.5in"><rect x="20" y="50" width="120" height="90" rx="8" {K4}/><rect x="12" y="34" width="136" height="26" rx="6" {K4}/>'
                   f'<path d="M80 34v26" stroke="{INK}" stroke-width="4"/><path d="M80 34c-20-30-46-20-30-2M80 34c20-30 46-20 30-2" fill="none" stroke="{INK}" stroke-width="4"/>'
                   f'<text x="80" y="104" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="22" fill="{w["col"]}">{s}</text></svg><span class="blank" style="min-width:1.3in"></span></div>'
                   for s in ['E C R A G', 'T H I F A', 'T F I G'])
    body = (f'<div style="display:flex;justify-content:space-around">{tags}</div>'
            f'<p style="font-size:13pt;text-align:center;margin:.14in 0 .04in">Unscramble the gift boxes, then use the words to fill the verse:</p>'
            + fill_verse(w, w['verse'][0], ['grace', 'faith', 'gift'], w['soft']) +
            f'<div class="ref" style="margin-top:.06in">Ephesians <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>')
    return page(w, 2, ICON_PENCIL, 'Gift-box verse! Being saved is a gift, not something we earn.', body, home=True)

def w4_p3(w):
    return page(w, 3, ICON_PENCIL, 'What are they thinking? Write it in the thought bubbles. Then write what happens.',
                comic(w, ['locked-end', 'scrub-clip', 'scrub-end'], 'Tip: they tried to scrub their sin marks off. Did it work?', (True, True, True), 2))

# ---------------- week 5 ----------------
def w5_p1(w):
    return page(w, 1, ICON_PENCIL, 'Find the way through the crowd to the door. Jesus is the door!',
                LB.p2_maze(w, 8, 7, 'door-clip', 'door-end', 515, 'Start', 'The door!').replace('max-height:6.1in', 'max-height:7.3in'))

def w5_p2(w):
    body = (fill_verse(w, w['verse'][0], ['loved', 'world', 'Son', 'believes', 'perish', 'eternal'], w['soft']) + wordbank(['world', 'eternal', 'loved', 'perish', 'Son', 'believes'])
            + f'<div class="ref">John <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>'
            + f'<div style="border:3px solid {w["col"]};border-radius:.16in;padding:.12in .2in;margin-top:.16in;font-size:15pt;line-height:1.9">'
              f'<b style="font-family:Grandstander">Put your name in it!</b><br>For God loved <span class="blank" style="min-width:2.2in"></span> in this way: He gave his one and only Son…</div>')
    return page(w, 2, ICON_PENCIL, 'Fill in the most famous verse in the Bible!', body, home=True)

def two_part(w, top, under_img, pos, task, note):
    x, y, ww, hh, off = pos
    return (f'<div class="page">{khead(w, 3)}<div class="task" style="font-size:13.5pt">{ICON_SCISSORS}{esc(task)}</div>'
            f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto">{top}</svg>'
            f'<div class="scissor-line" style="margin-top:.05in"><span>✂</span></div><div class="cutrow" style="font-size:9.5pt">Cut along this line first</div>'
            f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto"><rect x="2" y="2" width="756" height="396" rx="22" fill="#f6f4f9"/>'
            f'<defs><clipPath id="u{w["n"]}"><rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="10"/></clipPath></defs>'
            f'<image href="img/{under_img}.jpg" x="{x}" y="{y-off}" width="{ww}" height="{ww*1280/720:.0f}" clip-path="url(#u{w["n"]})" preserveAspectRatio="xMidYMin slice"/>'
            f'<text x="380" y="34" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="20" fill="#9a93a6">{note}</text>'
            f'<text x="380" y="388" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="20" fill="#9a93a6">Glue on the grey edges, then press the top picture on.</text></svg>{kfoot(w)}</div>')

def w5_p3(w):
    page_ = LB.k_door(w)
    return page_

# ---------------- week 6 ----------------
def num_code(msg):
    cells = ''
    for word in msg.split():
        cells += ''.join(f'<div class="c"><div class="b"></div><div class="s">{ord(c)-64}</div></div>' for c in word) + '<div class="gap"></div>'
    return f'<div class="code">{cells}</div>'

def w6_p1(w):
    key = ''.join(f'<div>{chr(65+i)}<br>{i+1}</div>' for i in range(26))
    body = (f'<div class="key" style="gap:3pt">{key.replace("<div>", "<div style=width:.5in>")}</div>'
            f'<h3 style="font-size:13pt;margin:.14in 0 0">1. What the angel said:</h3>{num_code("HE IS NOT HERE")}'
            f'<h3 style="font-size:13pt;margin:.06in 0 0">2. The best news ever:</h3>{num_code("JESUS IS ALIVE")}'
            f'<h3 style="font-size:13pt;margin:.06in 0 0">3. How clean Jesus makes us:</h3>{num_code("WHITE AS SNOW")}')
    return page(w, 1, ICON_PENCIL, 'Secret number code! A = 1, B = 2… Write the letter above each number.', body)

def w6_p2(w):
    body = (f'<div style="display:flex;gap:.2in;margin:.06in 0 .1in">'
            f'<div style="flex:1;text-align:center"><svg viewBox="0 0 300 220" style="width:3.4in;height:2.5in"><path d="M30 20h240a20 20 0 0 1 20 20v110a20 20 0 0 1-20 20H120l-50 40 8-40H30a20 20 0 0 1-20-20V40a20 20 0 0 1 20-20z" {K}/>'
            f'<text x="150" y="70" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="22">With my MOUTH I say:</text><text x="150" y="125" text-anchor="middle" font-family="Andika" font-weight="700" font-size="24">“Jesus is ________”</text></svg></div>'
            f'<div style="flex:1;text-align:center"><svg viewBox="0 0 300 240" style="width:3.4in;height:2.6in"><path d="M150 60c-30-60-140-50-140 20 0 70 90 110 140 150 50-40 140-80 140-150 0-70-110-80-140-20z" {K}/>'
            f'<text x="150" y="100" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="19">In my HEART I believe:</text><text x="150" y="140" text-anchor="middle" font-family="Andika" font-weight="700" font-size="17">God raised Him</text><text x="150" y="168" text-anchor="middle" font-family="Andika" font-weight="700" font-size="17">from the ________</text></svg></div></div>'
            + fill_verse(w, w['verse'][0], ['confess', 'Lord', 'believe', 'dead', 'saved'], w['soft']).replace('font-size:17pt', '') + wordbank(['saved', 'Lord', 'dead', 'confess', 'believe'])
            + f'<div class="ref">Romans <span class="blank" style="min-width:.6in"></span> : <span class="blank" style="min-width:.6in"></span></div>')
    return page(w, 2, ICON_PENCIL, 'Mouth and heart: fill in the bubbles, then the verse.', body, home=True)

# ---------------- week 7 ----------------
STORY12 = ['garden-end', 'rule-end', 'serpent-end', 'fruit-end', 'exile-end', 'road-end', 'test-end', 'scrub-end', 'door-end', 'clean', 'tomb-end', 'gates-end']
CIRCLE_BR = {'fruit-end', 'scrub-end', 'serpent-end', 'garden-end', 'gates-end', 'clean'}
ORDER12 = [3, 9, 0, 6, 11, 4, 1, 8, 5, 10, 2, 7]
# where the blank number circle goes (always a bottom corner, away from faces) and how each picture is cropped
STORY_FIT = {'garden-end': ('br', 30), 'rule-end': ('br', 40), 'serpent-end': ('br', 20), 'fruit-end': ('br', 15), 'exile-end': ('br', 40),
             'road-end': ('br', 45), 'test-end': ('br', 30), 'scrub-end': ('br', 10), 'door-end': ('br', 10), 'clean': ('br', 40),
             'tomb-end': ('br', 45), 'gates-end': ('br', 15)}
def w7_p1(w):
    cells = ''
    for k in ORDER12:
        nm = STORY12[k]; corner, y = STORY_FIT[nm]
        pos = 'bottom:.06in;right:.06in' if corner == 'br' else 'bottom:.06in;left:.06in'
        cells += (f'<div style="position:relative;width:1.82in;height:2.18in;border-radius:.1in;overflow:hidden;border:2.5px solid #1d1a24">{img(nm, style=f"width:100%;height:100%;object-fit:cover;object-position:50% {y}%")}'
                  f'<div style="position:absolute;{pos};width:.48in;height:.48in;background:#fff;border:2.5px solid #1d1a24;border-radius:50%"></div></div>')
    body = f'<div style="display:grid;grid-template-columns:repeat(4,1.82in);justify-content:space-between;row-gap:.1in">{cells}</div>'
    return page(w, 1, ICON_PENCIL, 'The whole story! Number the pictures 1 to 12 in the circles.', body)

def w7_p2(w):
    abc = ''.join(f'<div style="display:flex;gap:.14in;align-items:center;margin-bottom:.1in"><div style="width:.7in;height:.7in;border-radius:50%;background:{w["col"]};color:#fff;text-align:center;font:900 30pt Grandstander;line-height:.7in;flex:none">{k}</div>'
                  f'<div style="font-size:13.5pt;line-height:1.5"><span class="blank" style="min-width:1.4in"></span> {esc(r)}</div></div>'
                  for k, r in [('A', 'to God that you have sinned, and say you are sorry.'), ('B', 'that Jesus is God’s Son, that He died for you, and that He rose again.'), ('C', 'to trust Jesus and follow Him every day.')])
    body = (abc + wordbank(['Believe', 'Choose', 'Admit'])
            + f'<div class="verse-fill" style="background:{w["soft"]};font-size:16pt;line-height:1.7;margin-top:.04in">“Look, I am making everything new.” <span style="font-size:12pt">Revelation 21:5</span></div>'
            + f'<div class="drawbox" style="height:2.88in;margin-top:.1in"><span>Draw the new earth: even better than Eden!</span></div>')
    return page(w, 2, ICON_PENCIL, 'A, B, C: fill in the word that starts with each letter.', body, home=True)

def w7_p3(w):
    return LB.k_gates(w)

PAGES = {1: (w1_p1, w1_p2, w1_p3), 2: (w2_p1, w2_p2, w2_p3), 3: (w3_p1, w3_p2, w3_p3), 4: (w4_p1, w4_p2, w4_p3),
         5: (w5_p1, w5_p2, w5_p3), 6: (w6_p1, w6_p2, LB.k_tomb), 7: (w7_p1, w7_p2, w7_p3)}

# ---------------- extras ----------------
def letter():
    rows = ''.join(f'<tr><td style="width:.4in"><b style="color:{w["col"]};font-family:Grandstander;font-size:13pt">{w["n"]}</b></td><td><b>{esc(w["title"])}</b></td>'
                   f'<td>“{esc(w["big"])}”</td><td>{esc(w["verse"][1])}</td></tr>' for w in WEEKS)
    return (f'<div class="page letter"><div style="display:flex;gap:.25in;align-items:center">{img("cover", style="width:1.6in;height:2.2in;object-fit:cover;border-radius:.15in")}'
            f'<div><h1>Dear families,</h1><p style="margin:.06in 0 0">For seven Sundays, our 6- to 9-year-olds are walking through <b><i>The Way Back Home</i></b>: the true story of the Bible from God’s good garden, '
            f'to the sin that locked us out, to Jesus, the door, who made the way back home.</p></div></div>'
            f'<p>Each week your child brings home three pages. Page 2 has a memory verse and a <b>“For grown-ups”</b> box with a question to ask and one small thing to try that week.</p>'
            f'<h2 style="font-size:16pt;margin-top:.1in">Three ways to help at home</h2><ol>'
            f'<li><b>Listen together.</b> The whole book is free at <b>{SITE}</b> (scan the code). Ask your child to pause it and tell you what happens next.</li>'
            f'<li><b>Practise the memory verse</b> in the car or at bedtime. Let your child teach you the hand motions.</li>'
            f'<li><b>Find it in a real Bible.</b> Each week we learn to find one verse. Ask your child to show you how.</li></ol>'
            f'<table><tr><td></td><td><b>Week</b></td><td><b>Big idea</b></td><td><b>Memory verse</b></td></tr>{rows}</table>'
            f'<div style="display:flex;gap:.2in;align-items:center;margin-top:.16in"><div class="qrb" style="width:1.05in;height:1.05in;flex:none">{qr_svg()}</div>'
            f'<p style="margin:0">If your child asks about following Jesus, or tells you they prayed, we would love to talk with you. Thank you for sharing your child with us!</p></div>'
            f'<p style="margin-top:.14in">With love,</p><div style="border-bottom:2px solid #1d1a24;width:3in;height:.22in"></div>'
            f'<div class="foot"><span>{SER} · {SITE}</span><span>{CSB}</span></div></div>')

def map_page():
    html = LB.chart().replace('img/scrub-end.jpg', 'img/locked-end.jpg" data-x="', 1)
    html = html.replace('Every week, put a sticker in the dashed circle!', 'Every week: colour the stop, add a sticker, and write the verse reference!')
    html = html.replace('The Way Back Home · Little ones', SER)
    for w0, w in zip(LB.WEEKS, WEEKS):
        html = html.replace(f'>{esc(w0["title"])}<', f'>{esc(w["title"])}<br><span style="font:600 9pt Andika">________ __ : __</span><')
    return html

def bookmarks_invites():
    bm = ''
    for _ in range(3):
        refs = ''.join(f'<div style="display:flex;gap:6pt;align-items:center;margin-bottom:5pt"><div style="width:.26in;height:.26in;border:2px solid #1d1a24;border-radius:4pt;flex:none"></div><span style="font-size:10.5pt"><b>{esc(w["verse"][1])}</b></span></div>' for w in WEEKS)
        bm += (f'<div style="width:2.2in;height:4.5in;border:2.5px dashed #1d1a24;padding:.1in;position:relative">'
               f'<div style="font:900 13pt Grandstander;line-height:1.1;color:#1e88e5">Find it!</div><p style="font-size:8.5pt;margin:2pt 0 6pt">Tick each verse when you find it in your Bible.</p>{refs}'
               f'<p style="font:800 9pt Grandstander;margin:6pt 0 0">Old Testament: Genesis → Malachi<br>New Testament: Matthew → Revelation</p>'
               f'<p style="font:800 9pt Grandstander;margin:4pt 0 0;color:#e0453a">Go Eat Pop Corn!</p></div>')
    inv = ''
    for _ in range(4):
        inv += (f'<div style="width:3.7in;height:2.2in;border:2.5px dashed #1d1a24;padding:.12in;display:flex;gap:.12in;align-items:center">'
                f'<div class="qrb" style="width:1.25in;height:1.25in;flex:none">{qr_svg()}</div><div><div style="font:900 15pt Grandstander;line-height:1.1">You’re invited!</div>'
                f'<p style="font-size:9.5pt;margin:4pt 0">To: <span class="blank" style="min-width:1.4in"></span></p><p style="font-size:9.5pt;margin:0 0 4pt">Scan to hear a true story: <i>The Way Back Home</i>. Come to church with me!</p>'
                f'<p style="font-size:9.5pt;margin:0">From: <span class="blank" style="min-width:1.3in"></span></p></div></div>')
    return (f'<div class="page"><h1 style="font-size:24pt">Bookmarks and invite cards</h1><p style="font:800 11pt Grandstander;margin:2pt 0 .1in">Cut on the dashed lines. Bookmarks: week 1. Invite cards: week 7.</p>'
            f'<div style="display:flex;gap:.2in;justify-content:center">{bm}</div><div style="display:flex;flex-wrap:wrap;gap:.16in;justify-content:space-between;margin-top:.22in">{inv}</div>'
            f'<div class="foot"><span>{SER} · {SITE}</span><span>Extras</span></div></div>')

def cert():
    c = LB.cert().replace('I heard<br>The Way Back Home!', 'I finished<br>The Way Back Home!').replace('Jesus loves', 'Jesus welcomes home')
    return c.replace('“We love because he first loved us.” 1 John 4:19', '“Look, I am making everything new.” Revelation 21:5')

def build():
    pages = [letter(), map_page(), bookmarks_invites()]
    for w in WEEKS:
        pages += [f(w) for f in PAGES[w['n']]]
    pages.append(cert())
    css = CSS.replace('The Way Back Home · Little ones', SER)
    out = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{css}</style></head><body>{"".join(pages)}</body></html>'
    return out.replace('The Way Back Home · Little ones', SER)

if __name__ == '__main__':
    import weasyprint, json
    open(f'{B}/kids69.html', 'w').write(build())
    weasyprint.HTML(f'{B}/kids69.html', base_url=B).write_pdf(f'{B}/kids69.pdf')
    json.dump({'cw': getattr(w4_p1, 'answer', '')}, open(f'{B}/answers69.json', 'w'))
    print('ok')
