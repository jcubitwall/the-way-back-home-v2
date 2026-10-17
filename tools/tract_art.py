"""Makes the tract's story pictures with the blur baked in (art/tract/01.jpg … 12.jpg).

Each picture is cropped to the panel's shape, and its lower part switches over a short band to a blurred,
slightly darkened copy of itself, so the white words below are easy to read and nothing depends on the
browser drawing blurs or masks (which looked uneven on phones and on the upside-down half of the sheet).

Run from the repo root after changing a picture or its framing:  python3 tools/tract_art.py
The panel colour tint is added in tract.html on top of these.
"""
from PIL import Image, ImageFilter, ImageEnhance
import os

# picture (art/src), focus (0 = keep the top, 100 = keep the bottom), same order as the tract's panels 1–12
PANELS = [('garden-end', 45), ('rule-point', 40), ('fruit-end', 32), ('exile-end', 45),
          ('test-2-end', 35), ('locked-end', 42), ('scrub-clip', 30), ('door-end', 35),
          ('cross-kneel', 100), ('choice-end', 95), ('tomb-end', 60), ('gates-arrive', 75)]

BACKS = ['gates-end', 'choice-end', 'clean']

W, H = 802, 1052          # 4.01 × 5.26 in at 200 dpi (the picture frame inside each panel)
BLUR_AT = 0.60            # where the blur starts (share of the height)
BAND = 0.035              # how quickly it switches over: a short, fairly sudden fade
RADIUS = 18

def crop(im, focus):
    sw, sh = im.size
    scale = max(W / sw, H / sh)
    im = im.resize((round(sw * scale), round(sh * scale)), Image.LANCZOS)
    x = (im.width - W) // 2
    y = round((im.height - H) * focus / 100)
    return im.crop((x, y, x + W, y + H))

def main():
    os.makedirs('art/tract', exist_ok=True)
    for i, (name, focus) in enumerate(PANELS, 1):
        sharp = crop(Image.open(f'art/src/{name}.jpg').convert('RGB'), focus)
        soft = sharp.filter(ImageFilter.GaussianBlur(RADIUS))
        soft = ImageEnhance.Brightness(soft).enhance(.8)
        mask = Image.new('L', (W, H), 0)
        y0, y1 = int(H * BLUR_AT), int(H * (BLUR_AT + BAND))
        px = mask.load()
        for y in range(y0, H):
            v = 255 if y >= y1 else round(255 * (y - y0) / (y1 - y0))
            for x in range(W):
                px[x, y] = v
        out = Image.composite(soft, sharp, mask)
        out.save(f'art/tract/{i:02d}.jpg', quality=84, optimize=True, progressive=True)
        print(f'{i:02d}  {name}')
    # soft backgrounds for the back, A-B-C and prayer panels
    for name in BACKS:
        im = crop(Image.open(f'art/src/{name}.jpg').convert('RGB'), 40).resize((W // 2, H // 2), Image.LANCZOS)
        im = ImageEnhance.Brightness(im.filter(ImageFilter.GaussianBlur(14))).enhance(.85)
        im.save(f'art/tract/bg-{name}.jpg', quality=80, optimize=True)
        print(f'bg  {name}')

if __name__ == '__main__':
    main()
