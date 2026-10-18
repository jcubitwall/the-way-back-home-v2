import sys, random, html
sys.path.insert(0, '/tmp/claude-0/gen')
import segno
from art import *
from content import WEEKS, CSB, SITE

B = '/tmp/claude-0/build'
esc = html.escape
def img(n, cls='', style=''):
    return f'<img src="img/{n}.jpg" class="{cls}" style="{style}" alt="">'

qr = segno.make(f'https://{SITE}/en/', error='m')
def qr_svg():
    import io; b = io.BytesIO(); qr.save(b, kind='svg', border=1, dark=INK, light='#fff', xmldecl=False, svgns=True, nl=False)
    return b.getvalue().decode()

FONTS = '<link rel="stylesheet" href="fonts.css">'
BASE_CSS = '''
@page { size: letter; margin: 0.42in; }
* { box-sizing: border-box; }
body { margin: 0; color: #1d1a24; font-family: 'Andika', sans-serif; }
.page { page-break-after: always; position: relative; height: 10.1in; overflow: hidden; }
.page:last-child { page-break-after: auto; }
h1, h2, h3, .disp { font-family: 'Grandstander', sans-serif; font-weight: 900; margin: 0; }
svg { display: block; }
'''

# ======================================================================
#                         KIDS ACTIVITY PACK
# ======================================================================
KCSS = BASE_CSS + '''
.khead { display: flex; align-items: center; gap: .16in; border-radius: .22in; padding: .1in .16in .1in .1in; color: #fff; height: 1.32in; }
.khead .ph { width: 1.12in; height: 1.12in; border-radius: 50%; object-fit: cover; border: 4px solid #fff; flex: none; }
.khead .wk { font: 900 10pt 'Grandstander'; background: #fff; border-radius: 99px; padding: 2pt 9pt; display: inline-block; letter-spacing: .04em; }
.khead h1 { font-size: 27pt; line-height: 1.05; margin-top: 3pt; }
.khead .sayit { font: 800 12.5pt 'Grandstander'; opacity: .95; margin-top: 2pt; }
.khead .pn { margin-left: auto; text-align: center; font: 900 9pt 'Grandstander'; }
.khead .pn b { display: block; font-size: 26pt; line-height: 1; background: #fff; border-radius: 50%; width: .62in; height: .62in; padding-top: .1in; margin: 0 auto 2pt; }
.task { display: flex; align-items: center; gap: .12in; margin: .14in 0 .08in; font: 800 17pt 'Grandstander'; line-height: 1.15; }
.task .ic { width: .56in; height: .56in; flex: none; }
.name { position: absolute; bottom: .22in; left: 0; right: 0; display: flex; justify-content: space-between; align-items: flex-end; font: 800 11pt 'Grandstander'; }
.name span.l { border-bottom: 2px solid #1d1a24; width: 3.2in; display: inline-block; margin-left: 6pt; }
.foot { position: absolute; bottom: 0; left: 0; right: 0; font: 7pt 'Andika'; color: #8a8296; display: flex; justify-content: space-between; }
.colour { width: 7.66in; height: 5.6in; margin: 0 auto; }
.trace { width: 7.66in; margin: .06in auto 0; }
.grownups { position: absolute; bottom: .55in; left: 0; right: 0; border: 2px dashed #b9b2c6; border-radius: .16in; padding: .08in .14in; display: flex; gap: .14in; align-items: center; font-size: 9.6pt; line-height: 1.32; }
.grownups .q { width: .92in; height: .92in; flex: none; }
.grownups .q svg, .qrb svg { width: 100%; height: 100%; }
.grownups b { font-family: 'Andika'; }
.cards { display: flex; justify-content: space-between; margin-top: .1in; }
.card { width: 2.42in; height: 3.3in; border: 2.5px dashed #1d1a24; padding: .08in; border-radius: 0; position: relative; }
.card img { width: 100%; height: 100%; object-fit: cover; border-radius: .08in; display: block; }
.slots { display: flex; justify-content: space-between; margin: .04in 0 .1in; }
.slot { width: 2.42in; height: 3.3in; border: 3px solid #1d1a24; border-radius: .14in; background: #f6f4f9; position: relative; }
.slot b { position: absolute; top: .1in; left: .1in; font: 900 30pt 'Grandstander'; width: .62in; height: .62in; border-radius: 50%; color: #fff; text-align: center; line-height: .62in; }
.slot i { position: absolute; bottom: .12in; left: 0; right: 0; text-align: center; font: 800 11pt 'Grandstander'; color: #9a93a6; font-style: normal; }
.cutrow { font: 800 11pt 'Grandstander'; color: #6b6478; text-align: center; margin-top: .02in; }
.scissor-line { border-top: 2.5px dashed #1d1a24; margin: .1in 0 0; position: relative; height: 0; }
.scissor-line span { position: absolute; left: -.04in; top: -.17in; background: #fff; font-size: 14pt; padding-right: 3pt; }
.squares { display: grid; grid-template-columns: repeat(3, 2.42in); justify-content: space-between; row-gap: 0; }
.sq { width: 2.42in; height: 1.75in; border: 2.5px dashed #1d1a24; margin: -1.25px 0 0; }
.half { position: relative; height: 4.35in; border-radius: .14in; overflow: hidden; }
.pic-under { position: absolute; }
.glue { font: 800 10pt 'Grandstander'; color: #9a93a6; }
.cert { text-align: center; padding-top: .3in; border: 6px solid; border-radius: .3in; height: 9.4in; padding: .4in .5in; }
.letter { font-size: 11pt; line-height: 1.42; }
.letter h1 { font-size: 26pt; }
.letter table { border-collapse: collapse; width: 100%; font-size: 10.5pt; margin-top: .1in; }
.letter td { padding: 4pt 6pt; border-bottom: 1px solid #e3dfe9; vertical-align: top; }
'''

ICON_CRAYON = f'<svg viewBox="0 0 60 60" class="ic"><g transform="rotate(-35 30 30)"><rect x="22" y="10" width="16" height="36" rx="3" {K4}/><path d="M22 46l8 12 8-12z" {K4}/><path d="M22 18h16M22 38h16" stroke="{INK}" stroke-width="3"/></g></svg>'
ICON_PENCIL = f'<svg viewBox="0 0 60 60" class="ic"><circle cx="30" cy="30" r="24" {K4}/><path d="M20 30l7 8 14-16" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
ICON_SCISSORS = f'<svg viewBox="0 0 60 60" class="ic"><circle cx="16" cy="44" r="9" {K4}/><circle cx="44" cy="44" r="9" {K4}/><path d="M21 37L44 6M39 37L16 6" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/></svg>'
ICON_EYE = f'<svg viewBox="0 0 60 60" class="ic"><path d="M4 30q26-28 52 0-26 28-52 0z" {K4}/><circle cx="30" cy="30" r="9" fill="{INK}"/></svg>'

def khead(w, n):
    return (f'<div class="khead" style="background:{w["col"]}">{img(w["photo"], "ph")}'
            f'<div><span class="wk" style="color:{w["col"]}">WEEK {w["n"]}</span><h1>{esc(w["title"])}</h1><div class="sayit">“{esc(w["say"])}”</div></div>'
            f'<div class="pn"><b style="color:{w["col"]}">{n}</b>page</div></div>')

def kfoot(w):
    return (f'<div class="name"><span>My name:<span class="l"></span></span></div>'
            f'<div class="foot"><span>The Way Back Home · Little ones · {SITE}</span><span>Week {w["n"]} · page</span></div>')

def trace_svg(text, size=64):
    return (f'<svg viewBox="0 0 740 100" class="trace"><text x="370" y="76" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="{size}" '
            f'fill="#f1eef5" stroke="#8a8296" stroke-width="2.2" stroke-dasharray="5 5" letter-spacing="2">{esc(text)}</text></svg>')

def grownups(w):
    tune, lines = w['song']
    return (f'<div class="grownups"><div class="q">{qr_svg()}</div><div><b>For grown-ups:</b> listen to <i>The Way Back Home</i> together at <b>{SITE}</b> '
            f'(this week: {esc(w["book"])}). <b>Ask:</b> {esc(w["ask"])}<br><b>Sing it</b> (tune: {esc(tune)}): {esc(" ".join(lines))}</div></div>')

COLOUR_FOR = {1: 'garden', 2: 'snake', 3: 'mirror', 4: 'hands', 5: 'door', 6: 'tomb', 7: 'gates'}
TASK1 = {1: 'Colour God’s good garden. Count the fruit!', 2: 'Colour the tree. Can you see the sneaky snake?', 3: 'Draw your face in the mirror. God sees your heart!',
         4: 'Trace your hand. Colour the soap bubbles!', 5: 'Colour the door. Follow the footsteps to the door!', 6: 'Colour the empty tomb. Trace the sun’s rays!',
         7: 'Colour heaven’s gates. Draw yourself running home!'}

def k_page1(w):
    return (f'<div class="page">{khead(w, 1)}<div class="task">{ICON_CRAYON}{esc(TASK1[w["n"]])}</div>'
            f'<svg viewBox="0 0 600 440" class="colour">{COLOUR[COLOUR_FOR[w["n"]]]()}</svg>'
            f'<div class="task" style="font-size:13pt;margin:.08in 0 0">{ICON_PENCIL}Trace the words. Say them with the moves!</div>{trace_svg(w["say"], 62 if len(w["say"]) < 22 else 52)}'
            f'{kfoot(w)}</div>')

# ---------- page 2 puzzles ----------
def p2_count():
    rows = [(i_sun, 1, .9), (i_tree, 2, .78), (i_bird, 3, .9), (i_fish, 4, .82), (i_flower, 5, .8)]
    out = '<svg viewBox="0 0 760 590" style="width:7.66in;height:5.95in">'
    for r, (ic, cnt, s) in enumerate(rows):
        y = 58 + r * 116
        out += f'<rect x="4" y="{y-52}" width="752" height="106" rx="18" fill="{"#f6f4f9" if r % 2 == 0 else "#fff"}"/>'
        for k in range(cnt):
            out += use(ic, 58 + k * 82, y + (8 if ic is i_flower else 0) + (6 if ic is i_tree else 0), s)
        for k in range(1, 6):
            out += f'<circle cx="{470 + (k-1)*64}" cy="{y}" r="26" {K4}/><text x="{470 + (k-1)*64}" y="{y+11}" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="30">{k}</text>'
    return out + '</svg>'

def p2_snakes():
    tally = ''.join(f'<circle cx="{180 + i*100}" cy="690" r="32" {K}/>' for i in range(4))
    return (f'<svg viewBox="0 0 660 730" style="width:5.6in;height:6.2in;margin:0 auto">{hidden_snakes()}'
            f'<text x="20" y="700" font-family="Grandstander" font-weight="900" font-size="26">Found:</text>{tally}</svg>')

def p2_maze(w, cols, rows, start, end, seed, label_start, label_end):
    cell = 92
    W, H, m = maze(cols, rows, cell, seed)
    vbw, vbh = W + 300, H + 40
    ox, oy = 150, 20
    r = 62
    sx, sy = ox - 78, oy + cell / 2
    ex, ey = ox + W + 78, oy + H - cell / 2
    clip = (f'<defs><clipPath id="cs"><circle cx="{sx}" cy="{sy+40}" r="{r}"/></clipPath><clipPath id="ce"><circle cx="{ex}" cy="{ey-40}" r="{r}"/></clipPath></defs>')
    pics = (f'<image href="img/{start}.jpg" x="{sx-r}" y="{sy+40-r*1.78/1.3}" width="{2*r}" height="{2*r*1.78}" clip-path="url(#cs)" preserveAspectRatio="xMidYMid slice"/>'
            f'<circle cx="{sx}" cy="{sy+40}" r="{r}" fill="none" stroke="{w["col"]}" stroke-width="8"/>'
            f'<image href="img/{end}.jpg" x="{ex-r}" y="{ey-40-r*1.78/1.6}" width="{2*r}" height="{2*r*1.78}" clip-path="url(#ce)" preserveAspectRatio="xMidYMid slice"/>'
            f'<circle cx="{ex}" cy="{ey-40}" r="{r}" fill="none" stroke="{w["col"]}" stroke-width="8"/>')
    lab = (f'<text x="{sx}" y="{sy+40+r+30}" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="24" fill="{w["col"]}">{label_start}</text>'
           f'<text x="{ex}" y="{ey-40-r-14}" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="24" fill="{w["col"]}">{label_end}</text>'
           f'<path d="M{ox-14} {oy+cell/2}h10m-14-12l14 12-14 12" fill="none" stroke="{w["col"]}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    return (f'<svg viewBox="0 0 {vbw} {vbh}" style="width:7.66in;height:{7.66*vbh/vbw:.2f}in;max-height:6.1in;margin:0 auto">{clip}'
            f'<g transform="translate({ox} {oy})">{m}</g>{pics}{lab}</svg>')

def p2_wash():
    items = [(i_boot, 'muddy boot'), (i_plate, 'dirty plate'), (i_hand, 'messy hands'), (i_dog, 'spotty dog'), (i_heart, 'my heart')]
    out = '<svg viewBox="0 0 760 600" style="width:7.66in;height:6.05in">'
    pos = [(130, 140), (380, 140), (630, 140), (220, 430), (540, 430)]
    for (ic, lab), (x, y) in zip(items, pos):
        heart = ic is i_heart
        out += f'<rect x="{x-115}" y="{y-115}" width="230" height="230" rx="26" fill="{"#fde7e5" if heart else "#f6f4f9"}" stroke="{INK if heart else "none"}" stroke-width="3" stroke-dasharray="{"10 8" if heart else "0"}"/>'
        out += use(ic, x, y - 12, 1.45 if not heart else 1.35)
        out += f'<text x="{x}" y="{y+100}" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="22">{lab}</text>'
    return out + '</svg>'

def p2_tombs():
    out = '<svg viewBox="0 0 760 360" style="width:7.66in;height:3.63in">'
    for i, op in enumerate([False, True, False]):
        x = 130 + i * 250
        out += f'<g transform="translate({x} 170) scale(1.15)">{tomb_small(op)}</g>'
        out += f'<path d="M{x-110} 260h220" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
    out += '</svg>'
    out += (f'<div class="task" style="font-size:15pt">{ICON_CRAYON}Now colour the sunshine. Jesus is alive!</div>'
            f'<svg viewBox="0 0 760 250" style="width:7.66in;height:2.5in">{sun(380, 130, 58, True)}{flower(120, 190, 1.1)}{flower(640, 190, 1.1)}{bird(180, 60)}{bird(540, 70, .9)}</svg>')
    return out

TASK2 = {1: (ICON_PENCIL, 'Count what God made. Circle the number!'), 2: (ICON_EYE, 'Find the 4 sneaky snakes hiding. Circle them!'),
         3: (ICON_PENCIL, 'Walk the long road. Draw a line from the garden to God’s good rules.'),
         4: (ICON_PENCIL, 'Circle what soap can wash. Put a big X on the heart. Only God can make hearts clean!'),
         5: (ICON_PENCIL, 'Find the way through the crowd to the door. Jesus is the door!'),
         6: (ICON_EYE, 'Which tomb is empty? Circle it!'), 7: (ICON_PENCIL, 'Run home! Find the way through heaven’s gates to Jesus.')}

def k_page2(w):
    n = w['n']
    body = {1: p2_count, 2: p2_snakes, 4: p2_wash, 6: p2_tombs}.get(n)
    if body: body = body()
    elif n == 3: body = p2_maze(w, 5, 4, 'road-clip', 'test-end', 31, 'Start', 'Finish!')
    elif n == 5: body = p2_maze(w, 6, 5, 'door-clip', 'door-end', 52, 'Start', 'The door!')
    else: body = p2_maze(w, 7, 5, 'gates-run', 'gates-end', 74, 'Start', 'Home!')
    ic, t = TASK2[n]
    return f'<div class="page">{khead(w, 2)}<div class="task">{ic}{esc(t)}</div>{body}{grownups(w)}{kfoot(w)}</div>'

# ---------- page 3: cut and glue / crafts ----------
CARDS = {2: ['serpent-end', 'fruit-end', 'exile-end'], 3: ['road-clip', 'road-end', 'test-end'], 4: ['locked-end', 'scrub-clip', 'scrub-end']}
CARD_ORDER = {2: [2, 0, 1], 3: [1, 2, 0], 4: [2, 0, 1]}   # shuffled order on the cut row (indexes into the true order)
CARD_LABEL = {2: ['The sneaky snake', 'Uh-oh!', 'Out of the garden'], 3: ['Adam and Eve leave', 'All the people', 'God’s good rules'],
              4: ['Locked out', 'Scrub, scrub…', 'It won’t come off!']}

def k_story(w):
    n = w['n']
    slots = ''.join(f'<div class="slot"><b style="background:{w["col"]}">{i+1}</b><i>glue here</i></div>' for i in range(3))
    cards = ''.join(f'<div class="card">{img(CARDS[n][k])}</div>' for k in CARD_ORDER[n])
    return (f'<div class="page">{khead(w, 3)}<div class="task">{ICON_SCISSORS}Cut out the 3 pictures. Glue them in order: 1, 2, 3. Then tell the story!</div>'
            f'<div class="slots">{slots}</div><div class="scissor-line"><span>✂</span></div><div class="cutrow">Cut on the dashed lines</div>'
            f'<div class="cards">{cards}</div>{kfoot(w)}</div>')

def k_garden(w):
    sq_icons = [(i_sun, .95), (i_bird, 1.0), (i_fish, .95), (i_flower, .9), (i_butterfly, .95), (i_kid, .9)]
    labels = ['sun', 'bird', 'fish', 'flower', 'butterfly', 'me!']
    scene = (f'<svg viewBox="0 0 760 380" style="width:6.4in;height:3.2in;margin:0 auto"><rect x="4" y="4" width="752" height="372" rx="26" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             f'<path d="M4 250c120-24 260 14 380 0s250-18 372 4V350a26 26 0 0 1-26 26H30a26 26 0 0 1-26-26z" fill="#fff" stroke="{INK}" stroke-width="5"/>'
             f'<path d="M110 300c40-60 140-60 180 0" fill="none" stroke="{INK}" stroke-width="5"/><g transform="translate(470 6) scale(.62)">{tree()}</g>'
             f'<text x="200" y="150" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="30" fill="#c7c0d2">God’s good garden</text></svg>')
    sqs = ''.join(f'<div class="sq"><svg viewBox="0 0 240 190" style="width:100%;height:100%">{use(ic, 120, 82, s*1.25)}'
                  f'<text x="120" y="176" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="22">{lab}</text></svg></div>'
                  for (ic, s), lab in zip(sq_icons, labels))
    return (f'<div class="page">{khead(w, 3)}<div class="task">{ICON_SCISSORS}Cut out the squares. Glue them into God’s garden!</div>{scene}'
            f'<div class="scissor-line" style="margin-top:.16in"><span>✂</span></div><div class="cutrow">Cut on the dashed lines</div><div class="squares" style="margin-top:.06in">{sqs}</div>{kfoot(w)}</div>')

def two_part_craft(w, top_svg, under_img, under_pos, task, under_note):
    """Top half: a wall/gate with doors that open. Bottom half: the picture that goes behind."""
    return (f'<div class="page">{khead(w, 3)}<div class="task" style="font-size:14.5pt">{ICON_SCISSORS}{task}</div>'
            f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto">{top_svg}</svg>'
            f'<div class="scissor-line" style="margin-top:.05in"><span>✂</span></div><div class="cutrow" style="font-size:9.5pt">Grown-ups: cut along this line first</div>'
            f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto"><rect x="2" y="2" width="756" height="396" rx="22" fill="#f6f4f9"/>'
            f'<defs><clipPath id="u{w["n"]}"><rect x="{under_pos[0]}" y="{under_pos[1]}" width="{under_pos[2]}" height="{under_pos[3]}" rx="10"/></clipPath></defs>'
            f'<image href="img/{under_img}.jpg" x="{under_pos[0]}" y="{under_pos[1] - under_pos[4]}" width="{under_pos[2]}" height="{under_pos[2]*1280/720:.0f}" clip-path="url(#u{w["n"]})" preserveAspectRatio="xMidYMin slice"/>'
            f'<text x="380" y="34" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="20" fill="#9a93a6">{under_note}</text>'
            f'<text x="380" y="388" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="20" fill="#9a93a6">Put glue on the grey edges, then press the top picture on.</text></svg>'
            f'{kfoot(w)}</div>')

DOOR = (250, 46, 260, 270)   # x, y, w, h of the opening, same in both halves

def k_door(w):
    x, y, dw, dh = DOOR
    top = (f'<rect x="2" y="2" width="756" height="396" rx="22" fill="#fff" stroke="{INK}" stroke-width="3"/>{brick_wall(6, 754, 20, 396)}'
           f'<rect x="{x-14}" y="{y-14}" width="{dw+28}" height="{dh+14}" fill="#fff" stroke="{INK}" stroke-width="4"/>'
           f'<rect x="{x}" y="{y}" width="{dw}" height="{dh}" fill="#fff"/>'
           f'<path d="M{x+dw} {y}H{x}V{y+dh}H{x+dw}" fill="none" stroke="{INK}" stroke-width="7"/>'
           f'<path d="M{x+dw} {y}V{y+dh}" stroke="{INK}" stroke-width="4" stroke-dasharray="12 10"/>'
           f'<path d="M{x+dw/2-12} {y+70}h24v44h44v24h-44v86h-24v-86h-44v-24h44z" {K4}/><circle cx="{x+30}" cy="{y+dh/2+20}" r="11" fill="{INK}"/>'
           f'<rect x="{x-40}" y="{y+dh+8}" width="{dw+80}" height="44" rx="10" fill="#fff"/><text x="{x+dw/2}" y="{y+dh+40}" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="30">Jesus is the door!</text>'
           f'<rect x="{x-225}" y="{y+128}" width="150" height="54" rx="10" fill="#fff"/><rect x="{x+dw+75}" y="{y+128}" width="150" height="54" rx="10" fill="#fff"/><text x="{x-150}" y="{y+150}" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="17" fill="#6b6478">✂ cut the</text>'
           f'<text x="{x-150}" y="{y+172}" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="17" fill="#6b6478">thick lines</text>'
           f'<text x="{x+dw+150}" y="{y+150}" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="17" fill="#6b6478">fold on the</text>'
           f'<text x="{x+dw+150}" y="{y+172}" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="17" fill="#6b6478">dashes</text>')
    return two_part_craft(w, top, 'clean', (x, y, dw, dh, 150),
                          'Cut the door on the thick lines and fold it open. Glue the top picture onto the bottom one. Open the door!',
                          'What is behind the door?')

def k_tomb(w):
    top = (f'<rect x="2" y="2" width="756" height="396" rx="22" fill="#fff" stroke="{INK}" stroke-width="3"/>'
           f'{sun(640, 80, 34, True)}<path d="M40 380C110 170 250 120 380 120s270 50 340 260z" {K}/>'
           f'<path d="M290 380v-110a90 90 0 0 1 180 0v110z" fill="#fff" stroke="{INK}" stroke-width="5"/>'
           f'<text x="380" y="300" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="34">He is</text>'
           f'<text x="380" y="342" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="34">alive!</text>'
           f'<circle cx="500" cy="300" r="9" fill="{INK}"/><text x="530" y="306" font-family="Grandstander" font-weight="800" font-size="16" fill="#6b6478">fastener here</text>'
           f'{flower(110, 330, .8)}{flower(690, 334, .8)}')
    stone = (f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto">'
             f'<circle cx="240" cy="200" r="165" fill="#fff" stroke="{INK}" stroke-width="3" stroke-dasharray="12 9"/>'
             f'<circle cx="240" cy="200" r="150" {K}/><path d="M170 150q60-30 120 10M150 240q50 30 110 10" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
             f'<circle cx="370" cy="200" r="9" fill="{INK}"/>'
             f'<clipPath id="tg"><rect x="470" y="40" width="250" height="320" rx="16"/></clipPath>'
             f'<image href="img/tomb-glow.jpg" x="470" y="0" width="250" height="444" clip-path="url(#tg)" preserveAspectRatio="xMidYMin slice"/>'
             f'<rect x="470" y="40" width="250" height="320" rx="16" fill="none" stroke="{w["col"]}" stroke-width="6"/>'
             f'<text x="240" y="380" text-anchor="middle" font-family="Grandstander" font-weight="800" font-size="18" fill="#6b6478">✂ Cut out the stone. Colour it grey!</text></svg>')
    return (f'<div class="page">{khead(w, 3)}<div class="task" style="font-size:14.5pt">{ICON_SCISSORS}Cut out the stone. A grown-up fastens it on the dot. Roll it away: He is alive!</div>'
            f'<svg viewBox="0 0 760 400" style="width:7.0in;height:3.68in;margin:0 auto">{top}</svg><div style="height:.12in"></div>{stone}{kfoot(w)}</div>')

GATE = (230, 50, 300, 270)
def k_gates(w):
    x, y, gw, gh = GATE
    mid = x + gw / 2
    def bars(x0):
        return ''.join(f'<path d="M{x0+dx} {y+20}V{y+gh-14}" stroke="{INK}" stroke-width="5"/>' for dx in (30, 75, 120)) + f'<path d="M{x0+10} {y+gh/2}h130" stroke="{INK}" stroke-width="5"/>'
    top = (f'<rect x="2" y="2" width="756" height="396" rx="22" fill="#fff" stroke="{INK}" stroke-width="3"/>'
           f'{cloud(30, 350)}{cloud(600, 350)}{cloud(60, 60)}{cloud(610, 70)}'
           f'<path d="M{x-30} {y+gh}V{y-6}q{gw/2+30}-60 {gw+60} 0V{y+gh}" fill="#fff" stroke="{INK}" stroke-width="5"/>'
           f'<rect x="{x}" y="{y}" width="{gw}" height="{gh}" fill="#fff"/>{bars(x)}{bars(mid)}'
           f'<path d="M{x} {y}H{x+gw}M{x} {y+gh}H{x+gw}M{mid} {y}V{y+gh}" stroke="{INK}" stroke-width="7"/>'
           f'<path d="M{x} {y}V{y+gh}M{x+gw} {y}V{y+gh}" stroke="{INK}" stroke-width="4" stroke-dasharray="12 10"/>'
           f'<circle cx="{mid-16}" cy="{y+gh/2+30}" r="9" fill="{INK}"/><circle cx="{mid+16}" cy="{y+gh/2+30}" r="9" fill="{INK}"/>'
           f'<rect x="250" y="352" width="260" height="44" rx="10" fill="#fff"/><text x="380" y="385" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="28">Welcome home!</text>')
    return two_part_craft(w, top, 'gates-end', (x, y, gw, gh, 70),
                          'Cut the gates on the thick lines and fold them open. Glue the top picture onto the bottom one. Who is waiting?',
                          'Who is waiting behind the gates?')

def k_page3(w):
    n = w['n']
    if n == 1: return k_garden(w)
    if n in CARDS: return k_story(w)
    return {5: k_door, 6: k_tomb, 7: k_gates}[n](w)

# ---------- extras ----------
def chart():
    P = [(1.25, 2.3), (3.75, 1.85), (6.2, 2.7), (5.5, 5.05), (2.95, 5.0), (1.3, 7.2), (4.9, 7.65)]
    D = 96
    pts = [(x * D, y * D) for x, y in P]
    d = f'M{pts[0][0]} {pts[0][1]}'
    for i in range(1, len(pts)):
        (x0, y0), (x1, y1) = pts[i - 1], pts[i]
        d += f' Q{(x0+x1)/2} {(y0+y1)/2 + (-30 if i % 2 else 30)} {x1} {y1}'
    photos = ['garden-end', 'serpent-end', 'road-end', 'scrub-end', 'door-end', 'tomb-end', 'gates-end']
    stops = ''
    for i, ((x, y), w) in enumerate(zip(P, WEEKS)):
        r = .7 if i < 6 else .85
        stops += (f'<img src="img/{photos[i]}.jpg" style="position:absolute;left:{x-r}in;top:{y-r}in;width:{2*r}in;height:{2*r}in;border-radius:50%;object-fit:cover;border:5px solid {w["col"]}">'
                  f'<div style="position:absolute;left:{x-r-.05}in;top:{y-r-.05}in;width:.46in;height:.46in;border-radius:50%;background:{w["col"]};color:#fff;text-align:center;font:900 17pt Grandstander;line-height:.46in">{i+1}</div>'
                  f'<div style="position:absolute;left:{x-1.1}in;top:{y+r+.05}in;width:2.2in;text-align:center;font:900 12pt Grandstander"><span style="background:#fff;border-radius:6px;padding:0 5px">{esc(w["title"])}</span></div>'
                  f'<div style="position:absolute;left:{x+r-.32}in;top:{y-r-.12}in;width:.62in;height:.62in;border-radius:50%;border:3px dashed #1d1a24;background:#fff"></div>')
    return (f'<div class="page"><h1 style="font-size:34pt;text-align:center;color:#1e9e5a">My Road Home</h1>'
            f'<p style="text-align:center;font:800 13pt Grandstander;margin:2pt 0 0">Every week, put a sticker in the dashed circle!</p>'
            f'<svg viewBox="0 0 {7.66*D} {9.4*D}" style="position:absolute;left:0;top:.0in;width:7.66in;height:9.4in"><path d="{d}" fill="none" stroke="#efe3c8" stroke-width="48" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#1d1a24" stroke-width="2.5" stroke-dasharray="10 9" stroke-linecap="round"/></svg>{stops}'
            f'<div style="position:absolute;left:5.85in;top:8.75in;font:900 22pt Grandstander;color:#e8a200">HOME!</div>'
            f'<div class="name"><span>My name:<span class="l"></span></span></div><div class="foot"><span>The Way Back Home · Little ones · {SITE}</span><span>Sticker chart</span></div></div>')

def cert():
    return (f'<div class="page"><div class="cert" style="border-color:#1e88e5"><p style="font:900 12pt Grandstander;letter-spacing:.14em;color:#e8a200;margin:0">WELL DONE!</p>'
            f'<h1 style="font-size:34pt;line-height:1.1;margin:.08in 0 .16in">I heard<br>The Way Back Home!</h1>'
            f'{img("gates-end", style="width:3.4in;height:3.4in;object-fit:cover;border-radius:50%;border:8px solid #1e88e5")}'
            f'<p style="font:900 18pt Grandstander;margin:.2in 0 .1in">Jesus loves</p><div style="border-bottom:3px solid #1d1a24;width:5in;margin:.3in auto 0;height:.1in"></div>'
            f'<p style="font-size:12pt;color:#6b6478;margin-top:.22in">“We love because he first loved us.” 1 John 4:19</p>'
            f'<div style="display:flex;justify-content:space-around;margin-top:.5in;font:800 11pt Grandstander"><div style="border-top:2px solid #1d1a24;width:2.3in;padding-top:4pt">Teacher</div><div style="border-top:2px solid #1d1a24;width:2.3in;padding-top:4pt">Date</div></div>'
            f'<p style="font-size:7pt;color:#8a8296;margin-top:.3in">{CSB}</p></div></div>')

def letter():
    rows = ''.join(f'<tr><td style="width:.5in"><b style="color:{w["col"]};font-family:Grandstander;font-size:13pt">{w["n"]}</b></td><td><b>{esc(w["title"])}</b></td>'
                   f'<td>“{esc(w["say"])}”</td><td>{esc(w["verse"][1])}</td></tr>' for w in WEEKS)
    return (f'<div class="page letter"><div style="display:flex;gap:.25in;align-items:center">{img("cover", style="width:1.7in;height:2.3in;object-fit:cover;border-radius:.15in")}'
            f'<div><h1>Dear families,</h1><p style="margin:.06in 0 0">For the next seven Sundays, our little ones (ages 3–5) are walking through <b><i>The Way Back Home</i></b>, '
            f'a true story from the Bible: from God’s good garden, to the sin that locked us out, to Jesus, who made the way back home.</p></div></div>'
            f'<p>Each week your child brings home three pages: a colouring page, a puzzle and a cut-and-glue page. The puzzle page has a short <b>“For grown-ups”</b> box: a question to ask and the week’s song.</p>'
            f'<h2 style="font-size:16pt;margin-top:.12in">Three easy ways to help at home</h2>'
            f'<ol><li><b>Listen together.</b> The whole book is free to read and hear at <b>{SITE}</b> (scan the code below). Little ones love hearing the same story again and again, and that repetition is how they learn.</li>'
            f'<li><b>Say it with the moves.</b> Each week has one short sentence with hand movements. Ask your child to show you!</li>'
            f'<li><b>Ask the question</b> printed on the take-home page, at bedtime or in the car.</li></ol>'
            f'<table><tr><td></td><td><b>This week</b></td><td><b>Say it!</b></td><td><b>Bible words</b></td></tr>{rows}</table>'
            f'<div style="display:flex;gap:.2in;align-items:center;margin-top:.18in"><div class="qrb" style="width:1.1in;height:1.1in;flex:none">{qr_svg()}</div>'
            f'<p style="margin:0">If your child asks questions about Jesus, or says they talked to Him, we would love to hear about it and talk with you. Thank you for sharing your child with us!</p></div>'
            f'<p style="margin-top:.16in">With love,</p><div style="border-bottom:2px solid #1d1a24;width:3in;height:.22in"></div>'
            f'<div class="foot"><span>The Way Back Home · Little ones · {SITE}</span><span>{CSB}</span></div></div>')

def build_kids():
    pages = [letter(), chart()]
    for w in WEEKS:
        pages += [k_page1(w), k_page2(w), k_page3(w)]
    pages.append(cert())
    return f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{KCSS}</style></head><body>{"".join(pages)}</body></html>'

if __name__ == '__main__':
    import weasyprint
    which = sys.argv[1] if len(sys.argv) > 1 else 'kids'
    if which == 'kids':
        open(f'{B}/kids.html', 'w').write(build_kids())
        weasyprint.HTML(f'{B}/kids.html', base_url=B).write_pdf(f'{B}/kids.pdf')
    print('ok')
