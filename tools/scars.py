"""Paint nail scars on Jesus' hands in the book pictures (art/hd).
Each entry: picture, centre x/y (fractions), scar length (fraction of width), angle (deg).
Originals are kept in art/hd/pre-scar/ so this can be re-run safely."""
import math, os, shutil, sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
SCARS = {
 'gates-open':   [(.313, .518, .026, 35)],
 'gates-arrive': [(.313, .518, .026, 35)],
 'gates-end':    [(.338, .486, .032, 20)],
 'gates-run':    [(.570, .478, .034, 15), (.639, .594, .032, 10)],
 'new-earth-end':[(.866, .412, .024, 75)],
 'new-earth-hands':[(.797, .380, .021, 80)],
}
def scar(W, H, cx, cy, L, ang):
    k = 4; m = Image.new('L', (W*k, H*k), 0); d = ImageDraw.Draw(m)
    cx, cy, L = cx*W*k, cy*H*k, L*W*k; a = math.radians(ang); ux, uy = math.cos(a), math.sin(a); vx, vy = -uy, ux
    lay = []
    # soft pink halo
    h = Image.new('L', m.size, 0); hd = ImageDraw.Draw(h)
    hd.ellipse((cx-L*.42, cy-L*.3, cx+L*.42, cy+L*.3), fill=200); h = h.filter(ImageFilter.GaussianBlur(L*.07))
    lay.append((h, (185, 85, 80)))
    # radiating hairlines
    r = Image.new('L', m.size, 0); rd = ImageDraw.Draw(r)
    for i, (t, ln) in enumerate([(0,.42),(35,.26),(-145,.26),(180,.42)]):
        b = a + math.radians(t); rd.line((cx, cy, cx+math.cos(b)*L*ln, cy+math.sin(b)*L*ln), fill=150, width=max(2, int(L*.03)))
    lay.append((r.filter(ImageFilter.GaussianBlur(L*.006)), (120, 45, 38)))
    # the wound slit (lens shape)
    s = Image.new('L', m.size, 0); sd = ImageDraw.Draw(s); pts = []
    for i in range(41):
        t = -1 + i/20; w = (1-t*t)*L*.09
        pts.append((cx+ux*t*L*.3 + vx*w, cy+uy*t*L*.3 + vy*w))
    pts += [(cx+ux*(-1+i/20)*L*.3 - vx*(1-(-1+i/20)**2)*L*.09, cy+uy*(-1+i/20)*L*.3 - vy*(1-(-1+i/20)**2)*L*.09) for i in range(40, -1, -1)]
    sd.polygon(pts, fill=240)
    lay.append((s.filter(ImageFilter.GaussianBlur(L*.012)), (80, 20, 18)))
    return [(np.asarray(l.resize((W, H), Image.LANCZOS), dtype=np.float32)/255, np.array(c, np.float32)/255) for l, c in lay]
def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); hd = os.path.join(root, 'art', 'hd'); bk = os.path.join(hd, 'pre-scar')
    os.makedirs(bk, exist_ok=True)
    for name, ss in SCARS.items():
        p = os.path.join(hd, name + '.jpg'); b = os.path.join(bk, name + '.jpg')
        if not os.path.exists(b): shutil.copy(p, b)
        im = np.asarray(Image.open(b).convert('RGB'), dtype=np.float32)/255; H, W = im.shape[:2]
        for (x, y, L, ang) in ss:
            for a, c in scar(W, H, x, y, L, ang):
                a = a[..., None]; im = im*(1 - a + a*c)        # multiply, so it takes the skin tone
        Image.fromarray((im*255).clip(0, 255).astype('uint8')).save(p, quality=93)
        print(name, len(ss))
main()
