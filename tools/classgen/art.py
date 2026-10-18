"""Bold, simple SVG line art for ages 3-5 (thick outlines, big shapes, white inside)."""
import math, random

INK = '#1d1a24'
K = f'fill="#fff" stroke="{INK}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"'
K4 = K.replace('stroke-width="5"', 'stroke-width="4"')

def flower(x, y, s=1.0):
    pet = ''.join(f'<circle cx="{16*math.cos(math.radians(a)):.1f}" cy="{16*math.sin(math.radians(a)):.1f}" r="12" {K}/>' for a in (0, 72, 144, 216, 288))
    return f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0v42" {K}/>{pet}<circle r="9" {K}/></g>'

def sun(x, y, r, dashed=False):
    rays = ''
    for i in range(10):
        a = math.radians(i * 36)
        rays += (f'<path d="M{x+math.cos(a)*(r+12):.1f} {y+math.sin(a)*(r+12):.1f}L{x+math.cos(a)*(r+40):.1f} {y+math.sin(a)*(r+40):.1f}" {K}'
                 + (' stroke-dasharray="1 11"' if dashed else '') + '/>')
    return f'<g>{rays}<circle cx="{x}" cy="{y}" r="{r}" {K}/></g>'

CROWN = 'M300 40c40 0 62 22 66 44 34-4 64 20 62 54 22 14 26 48 6 68-14 16-40 20-58 12-14 24-52 32-76 16-24 16-62 8-74-16-22 8-50 0-60-22-14-24-2-54 22-62-4-34 26-58 58-54 6-24 28-40 54-40z'
def tree(fruit=''):
    return f'<rect x="272" y="236" width="56" height="168" rx="10" {K}/><path d="{CROWN}" {K}/>{fruit}'
GROUND = f'<path d="M10 404c80-14 160 10 290 0s200-12 290 2" {K} fill="none"/>'

def bird(x, y, s=1):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0 0q15-18 30 0q15-18 30 0" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'

def fish(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-34 0c14-22 46-22 60 0-14 22-46 22-60 0z" {K}/>'
            f'<path d="M26 0l22-16v32z" {K}/><circle cx="-18" cy="-4" r="4" fill="{INK}"/></g>')

def butterfly(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><ellipse cx="-18" cy="-12" rx="18" ry="16" {K}/><ellipse cx="18" cy="-12" rx="18" ry="16" {K}/>'
            f'<ellipse cx="-14" cy="14" rx="13" ry="12" {K}/><ellipse cx="14" cy="14" rx="13" ry="12" {K}/><rect x="-5" y="-26" width="10" height="52" rx="5" {K}/>'
            f'<path d="M-3-26q-8-14-16-16M3-26q8-14 16-16" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/></g>')

def kid(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cy="-58" r="20" {K}/><path d="M-22-34h44l8 46h-60z" {K}/>'
            f'<path d="M-12 12v34M12 12v34M-22-28l-18 26M22-28l18 26" {K}/>'
            f'<circle cx="-7" cy="-61" r="3" fill="{INK}"/><circle cx="7" cy="-61" r="3" fill="{INK}"/><path d="M-8-51q8 7 16 0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/></g>')

# ---------- the 7 colouring pictures (viewBox 0 0 600 440) ----------
def c_garden():
    fruit = ''.join(f'<circle cx="{x}" cy="{y}" r="17" {K}/>' for x, y in [(250, 120), (330, 100), (380, 160), (290, 180), (220, 190), (350, 215)])
    return (sun(80, 78, 38) + tree(fruit) + GROUND + flower(90, 340) + flower(160, 356, .8) + flower(470, 340) + flower(540, 356, .8)
            + bird(470, 70) + bird(520, 110, .8))

def c_snake():
    p = 'M196 392c40-6 70-20 82-44s70-30 70-60-60-30-60-60 50-40 96-38'
    return (tree(f'<circle cx="235" cy="175" r="18" {K}/><circle cx="360" cy="120" r="17" {K}/>') + GROUND
            + f'<path d="{p}" fill="none" stroke="{INK}" stroke-width="38" stroke-linecap="round"/><path d="{p}" fill="none" stroke="#fff" stroke-width="27" stroke-linecap="round"/>'
            + f'<ellipse cx="400" cy="190" rx="34" ry="24" {K}/><circle cx="410" cy="182" r="5" fill="{INK}"/>'
            + f'<path d="M432 196l22 4m0 0l10-8m-10 8l10 8" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            + flower(500, 340) + flower(90, 340))

def c_mirror():
    return (f'<rect x="280" y="380" width="40" height="56" rx="12" {K}/><ellipse cx="300" cy="200" rx="170" ry="190" {K}/>'
            f'<ellipse cx="300" cy="200" rx="140" ry="160" fill="#fff" stroke="{INK}" stroke-width="3" stroke-dasharray="4 10"/>'
            f'<path d="M70 70v34M53 87h34M520 300v30M505 315h30M535 80v24M523 92h24" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>')

def c_hands():
    bub = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" {K}/>' for x, y, r in [(450, 250, 26), (520, 220, 34), (470, 160, 20), (545, 130, 24), (490, 80, 16)])
    return (f'<rect x="26" y="20" width="350" height="400" rx="26" fill="#fff" stroke="{INK}" stroke-width="4" stroke-dasharray="14 10"/>'
            f'<text x="201" y="225" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="26" fill="#b5afc0">Trace your hand here</text>'
            f'<rect x="420" y="300" width="150" height="90" rx="26" {K}/><text x="495" y="356" text-anchor="middle" font-family="Grandstander" font-weight="900" font-size="28" fill="{INK}">SOAP</text>' + bub)

def brick_wall(x0, x1, y0, y1, step=40):
    b = ''
    for y in range(y0, y1, step):
        b += f'<path d="M{x0} {y}h{x1-x0}" stroke="{INK}" stroke-width="3"/>'
        off = (y // step % 2) * 37
        for i in range(9):
            bx = x0 + 10 + i * 75 + off
            if bx < x1: b += f'<path d="M{bx} {y}v{step}" stroke="{INK}" stroke-width="3"/>'
    return b

def c_door():
    return (brick_wall(20, 580, 40, 400)
            + f'<path d="M210 404V170a90 90 0 0 1 180 0v234z" {K}/><path d="M270 404V140M330 404V140" stroke="{INK}" stroke-width="3"/>'
            + f'<path d="M292 175h16v30h30v16h-30v58h-16v-58h-30v-16h30z" {K} stroke-width="4"/><circle cx="364" cy="300" r="9" fill="{INK}"/>'
            + f'<path d="M30 430C120 430 160 360 300 404" fill="none" stroke="{INK}" stroke-width="6" stroke-dasharray="1 14" stroke-linecap="round"/>')

def c_tomb():
    return (sun(300, 110, 46, True) + f'<path d="M20 404C80 230 200 190 300 190s230 50 270 214z" {K}/>'
            + f'<path d="M220 404v-90a70 70 0 0 1 140 0v90z" {K}/><circle cx="440" cy="340" r="64" {K}/>'
            + f'<path d="M410 320q20-10 40 4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
            + GROUND + flower(110, 360, .8) + flower(530, 362, .7))

def cloud(x, y):
    return f'<path d="M{x} {y}c0-26 34-34 46-14 10-26 54-26 62 2 26-6 42 18 28 36H{x+4}c-18 0-18-24-4-24z" {K}/>'

def c_gates():
    def gate(x0):
        s = f'<path d="M{x0} 390V215q65-55 130 0v175z" {K}/>'
        for dx in (32, 65, 98):
            s += f'<path d="M{x0+dx} 390V{182 if dx == 65 else 196}" stroke="{INK}" stroke-width="5"/>'
        return s + f'<path d="M{x0} 300h130" stroke="{INK}" stroke-width="5"/>'
    return (sun(300, 70, 30) + f'<path d="M300 210c-14-28-62-28-62 6 0 28 40 48 62 66 22-18 62-38 62-66 0-34-48-34-62-6z" {K}/>'
            + gate(40) + gate(430) + f'<path d="M230 440L282 300M370 440L318 300" fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="10 9"/>'
            + cloud(20, 400) + cloud(440, 400))

COLOUR = dict(garden=c_garden, snake=c_snake, mirror=c_mirror, hands=c_hands, door=c_door, tomb=c_tomb, gates=c_gates)

# ---------- small icons for puzzles (centred at 0,0, about 100 px) ----------
def i_sun(): return sun(0, 0, 26)
def i_tree(): return f'<g transform="scale(.42) translate(-300 -230)">{tree()}</g>'
def i_bird(): return f'<g><path d="M-38 0c0-24 28-34 50-20l26-6-12 18c4 26-24 40-50 30-8 0-14-10-14-22z" {K}/><path d="M-10 -4q12 18 30 4" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round"/><circle cx="18" cy="-14" r="4" fill="{INK}"/></g>'
def i_fish(): return fish(0, 0, 1.1)
def i_flower(): return flower(0, -16, 1.15)
def i_butterfly(): return butterfly(0, 0, 1.2)
def i_kid(): return kid(0, 30, 1.0)
def i_boot():
    return (f'<g><path d="M-34-50h36v50l30 8c12 3 20 12 20 24v8h-86z" {K}/><path d="M-34 32h86" stroke="{INK}" stroke-width="5"/><path d="M-34-40h36" stroke="{INK}" stroke-width="4"/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>' for x, y, r in [(-18, -20, 5), (-8, 6, 6), (18, 20, 5), (-22, 22, 4), (36, 26, 4)]) + '</g>')
def i_plate():
    return (f'<g><ellipse rx="52" ry="42" {K}/><ellipse rx="34" ry="26" fill="none" stroke="{INK}" stroke-width="3"/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>' for x, y, r in [(-12, -6, 6), (14, 8, 5), (6, -14, 4)]) + '</g>')
def i_hand():
    return (f'<g transform="translate(0 8)"><path d="M-26 40v-46c0-8 10-8 10 0v-28c0-8 11-8 11 0v-6c0-8 11-8 11 0v6c0-8 11-8 11 0v34c4-12 18-10 14 2l-10 30c-4 10-10 18-20 18h-12c-10 0-15-6-15-10z" {K}/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>' for x, y, r in [(-8, 4, 5), (10, -12, 4), (6, 24, 5)]) + '</g>')
def i_heart():
    return (f'<g><path d="M0-20c-14-28-60-26-60 8 0 30 40 52 60 70 20-18 60-40 60-70 0-34-46-36-60-8z" {K}/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>' for x, y, r in [(-26, -6, 7), (6, 10, 8), (24, -12, 6), (-8, 30, 6)]) + '</g>')
def i_dog():
    return (f'<g><ellipse cx="6" cy="10" rx="42" ry="26" {K}/><circle cx="-34" cy="-18" r="22" {K}/><ellipse cx="-50" cy="-26" rx="9" ry="16" {K}/>'
            f'<path d="M-20 30v18M28 30v18M48 4l14-14" {K}/><circle cx="-38" cy="-20" r="3.5" fill="{INK}"/><circle cx="-52" cy="-10" r="4" fill="{INK}"/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>' for x, y, r in [(0, 2, 7), (22, 16, 6), (-14, 20, 5)]) + '</g>')

def use(icon, x, y, s=1.0):
    return f'<g transform="translate({x} {y}) scale({s})">{icon()}</g>'

# ---------- hidden snakes garden (week 2 puzzle) ----------
def snake_small(x, y, s=1.0, flip=False, rot=0):
    d = 'M-40 10c14-14 26 8 40-6s26 8 40-6'
    f = -1 if flip else 1
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s*f} {s})"><path d="{d}" fill="none" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round"/><ellipse cx="46" cy="-6" rx="13" ry="10" {K4}/>'
            f'<circle cx="50" cy="-9" r="2.8" fill="{INK}"/><path d="M58-2l10 2m0 0l5-4m-5 4l5 4" fill="none" stroke="{INK}" stroke-width="3" stroke-linecap="round"/></g>')

def hidden_snakes():
    s = ''
    # two trees, bushes, flowers
    s += f'<g transform="translate(-120 30) scale(.85)">{tree()}</g><g transform="translate(250 10) scale(.95)">{tree()}</g>'
    s += f'<path d="M0 560c100-20 220 10 330-4s240-10 330 4" fill="none" stroke="{INK}" stroke-width="5"/>'
    for bx, by, r in [(80, 520, 60), (300, 530, 70), (540, 520, 64)]:
        s += f'<path d="M{bx-r} {by+30}c-10-50 30-80 60-60 20-40 80-30 {r*1.2:.0f} 10 40 0 50 50 {r*0.6:.0f} 50z" {K}/>'
    s += flower(30, 600, .8) + flower(620, 600, .8) + flower(420, 605, .7) + flower(200, 610, .7)
    s += sun(600, 60, 30) + bird(430, 40, .8)
    # the four snakes
    s += snake_small(150, 150, 1.0)            # in the left tree
    s += snake_small(530, 230, 1.0, True)      # in the right tree
    s += snake_small(300, 492, .9, rot=-8)    # in the middle bush
    s += snake_small(560, 600, .95, True)     # in the grass
    return s

# ---------- three tombs (week 6 puzzle) ----------
def tomb_small(open_):
    s = f'<path d="M-90 70C-70-20-40-40 0-40S70-20 90 70z" {K}/><path d="M-30 70v-36a30 30 0 0 1 60 0v36z" {K}/>'
    if open_:
        s += f'<circle cx="56" cy="44" r="28" {K}/>'
        s += ''.join(f'<path d="M{math.cos(math.radians(a))*40:.0f} {-2+math.sin(math.radians(a))*40:.0f}L{math.cos(math.radians(a))*56:.0f} {-2+math.sin(math.radians(a))*56:.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>' for a in (200, 240, 270, 300, 340))
    else:
        s += f'<circle cx="0" cy="40" r="34" {K}/><path d="M-14 28q14-8 28 2" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
    return s

# ---------- maze ----------
def maze(cols, rows, cell, seed, wall=10):
    rnd = random.Random(seed)
    seen = [[False] * cols for _ in range(rows)]
    right = [[True] * cols for _ in range(rows)]
    down = [[True] * cols for _ in range(rows)]
    stack = [(0, 0)]; seen[0][0] = True
    while stack:
        r, c = stack[-1]
        nb = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= r + dr < rows and 0 <= c + dc < cols and not seen[r + dr][c + dc]]
        if not nb: stack.pop(); continue
        nr, nc = rnd.choice(nb)
        if nr == r: right[r][min(c, nc)] = False
        else: down[min(r, nr)][c] = False
        seen[nr][nc] = True; stack.append((nr, nc))
    W, H = cols * cell, rows * cell
    p = []
    # outer walls with openings top-left (entry, on the left side) and bottom-right (exit, on the right side)
    p.append(f'M0 0H{W}V{H - cell}'); p.append(f'M{W} {H}H0V{cell}')
    for r in range(rows):
        for c in range(cols):
            x, y = c * cell, r * cell
            if right[r][c] and c < cols - 1: p.append(f'M{x+cell} {y}V{y+cell}')
            if down[r][c] and r < rows - 1: p.append(f'M{x} {y+cell}H{x+cell}')
    d = ' '.join(p)
    return W, H, (f'<path d="{d}" fill="none" stroke="#e9e4f0" stroke-width="{wall+12}" stroke-linecap="round"/>'
                  f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{wall}" stroke-linecap="round" stroke-linejoin="round"/>')
