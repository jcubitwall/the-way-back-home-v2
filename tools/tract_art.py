"""Makes the tract's story pictures with the blur baked in (art/tract/01.jpg … 12.jpg).

Each picture is cropped to the panel's shape, and its lower part switches over a short band to a blurred,
slightly darkened copy of itself, so the white words below are easy to read and nothing depends on the
browser drawing blurs or masks (which looked uneven on phones and on the upside-down half of the sheet).

Run from the repo root after changing a picture or its framing:  python3 tools/tract_art.py
The blur is fitted to each panel's own words: run tools/tract_measure.py first whenever the tract text changes.
"""
from PIL import Image, ImageFilter, ImageEnhance
import os, json
import numpy as np

# picture (art/src), focus (0 = keep the top, 100 = keep the bottom), book page whose chapter colour it takes;
# same order as the tract's panels 1–12
PANELS = [('garden-end', 45, 'garden'), ('rule-point', 40, 'rule'), ('fruit-end', 32, 'fruit'), ('exile-end', 45, 'exile'),
          ('test-2-end', 60, 'test'), ('locked-end', 62, 'locked'), ('scrub-clip', 30, 'scrub'), ('door-end', 35, 'door'),
          ('cross-kneel', 100, 'cross'), ('choice-end', 95, 'choice'), ('tomb-end', 60, 'gates'), ('gates-arrive', 75, 'gates')]

BACKS = ['gates-end', 'choice-end', 'clean']

W, H = 802, 1052          # 4.01 × 5.26 in at 200 dpi (the picture frame inside each panel)
MARGIN = 0.012            # the blur is full just this far above the words (share of the height)
RAMP = 0.10               # how far above the words the softening begins: short, so little picture is lost
LEVELS = [0, 2.5, 5, 8, 12, 17, 23]   # blur radii, blended row by row: a progressive blur like the book's

def crop(im, focus):
    sw, sh = im.size
    scale = max(W / sw, H / sh)
    im = im.resize((round(sw * scale), round(sh * scale)), Image.LANCZOS)
    x = (im.width - W) // 2
    y = round((im.height - H) * focus / 100)
    return im.crop((x, y, x + W, y + H))

def smooth(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)

def page(sharp, tint, text_top):
    """The book's look: the picture grows softer toward the bottom (no visible edge), then deepens into the
    chapter colour, exactly as app.css does it (tint x 0.5 at half strength where the words start, tint x 0.42 at 72 % at the bottom)."""
    stack = [np.asarray(sharp.filter(ImageFilter.GaussianBlur(r)) if r else sharp, dtype=np.float32) for r in LEVELS]
    y = np.arange(H, dtype=np.float32) / H
    # blur grows over the 20 % of the height above the words, reaching full softness just inside them
    full = text_top - MARGIN
    level = smooth((y - (full - RAMP)) / RAMP) * (len(LEVELS) - 1)
    lo = np.floor(level).astype(int); hi = np.minimum(lo + 1, len(LEVELS) - 1); f = (level - lo)[:, None, None]
    S = np.stack(stack)                                   # levels × H × W × 3
    rows = np.arange(H)
    out = S[lo, rows] * (1 - f) + S[hi, rows] * f
    # chapter colour, deepening toward the bottom
    t = np.array([int(tint[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.float32)
    mid, deep = t * 0.5, t * 0.42
    top = full - 0.06
    a = np.zeros(H, dtype=np.float32); c = np.zeros((H, 3), dtype=np.float32)
    for i, yy in enumerate(y):
        if yy <= top: continue
        if yy <= full:
            k = (yy - top) / (full - top); a[i] = 0.64 * k; c[i] = mid
        else:
            k = (yy - full) / (1 - full); a[i] = 0.64 + 0.18 * k; c[i] = mid * (1 - k) + deep * k
    out = out * (1 - a[:, None, None]) + c[:, None, :] * a[:, None, None]
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))

def main():
    # where the words start on each panel, measured by tools/tract_measure.py (tallest text of any language)
    fit = json.load(open('tools/tract_fit.json'))
    tints = {p['id']: p['tint'] for p in json.load(open('content/story.json'))['pages']}
    os.makedirs('art/tract', exist_ok=True)
    for i, (name, focus, pid) in enumerate(PANELS, 1):
        sharp = crop(Image.open(f'art/src/{name}.jpg').convert('RGB'), focus)
        page(sharp, tints[pid], fit[str(i)]).save(f'art/tract/{i:02d}.jpg', quality=86, optimize=True, progressive=True)
        print(f'{i:02d}  {name}  {tints[pid]}  words at {fit[str(i)]:.0%}')
    # soft backgrounds for the back, A-B-C and prayer panels
    for name in BACKS:
        im = crop(Image.open(f'art/src/{name}.jpg').convert('RGB'), 40).resize((W // 2, H // 2), Image.LANCZOS)
        im = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(14))).enhance(.85)
        im.save(f'art/tract/bg-{name}.jpg', quality=80, optimize=True)
        print(f'bg  {name}')

if __name__ == '__main__':
    main()
