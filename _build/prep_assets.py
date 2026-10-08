"""Prepare home page assets from the harvested originals.

Reads only from site/_harvest/raw (never executes anything there) and writes
optimised WebP files to site/assets/img. Run with:  python -I prep_assets.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

SITE = Path(__file__).resolve().parent.parent
RAW = SITE / "_harvest" / "raw"
IMG = SITE / "assets" / "img"
IMG.mkdir(parents=True, exist_ok=True)


def raw(prefix):
    hits = sorted(RAW.glob(prefix + "*"))
    if not hits:
        raise SystemExit("missing raw asset: " + prefix)
    return hits[0]


def save(im, name, q=82, lossless=False):
    out = IMG / name
    im.save(out, "WEBP", quality=q, method=6, lossless=lossless)
    print(f"{name:34s} {im.size[0]}x{im.size[1]}  {out.stat().st_size // 1024} KB")


# Logo: used as-is (the only version), copied byte for byte.
logo_src = raw("logo-header_")
(IMG / "logo-dr-john-oda.webp").write_bytes(logo_src.read_bytes())
logo = Image.open(logo_src).convert("RGBA")
print("logo-dr-john-oda.webp copied as-is", logo.size)

# Favicon: the round photo at the left of the logo (no real favicon exists).
side = logo.size[1]
fav = logo.crop((0, 0, side, side))
ring = Image.new("L", (side * 4, side * 4), 0)
ImageDraw.Draw(ring).ellipse((6, 6, side * 4 - 6, side * 4 - 6), fill=255)
ring = ring.resize((side, side), Image.LANCZOS)
fav.putalpha(Image.fromarray(np.minimum(np.asarray(fav.split()[-1]), np.asarray(ring))))
fav.resize((64, 64), Image.LANCZOS).save(IMG / "favicon-64.png")
print("favicon-64.png from the logo's round photo")

# Portrait cut-out: flood the white background from the border, feather the edge.
src = Image.open(raw("about-hero-portrait_")).convert("RGB")
a = np.asarray(src).astype(np.int16)
near_white = (a.min(axis=2) > 222) & ((a.max(axis=2) - a.min(axis=2)) < 28)
cand = Image.fromarray((near_white * 255).astype(np.uint8), "L").copy()
w, h = cand.size
px = cand.load()
border = [(x, 0) for x in range(w)] + [(x, h - 1) for x in range(w)] + \
         [(0, y) for y in range(h)] + [(w - 1, y) for y in range(h)]
for xy in border:
    if px[xy] == 255:
        ImageDraw.floodfill(cand, xy, 128, thresh=0)
bg = np.asarray(cand) == 128
mask = Image.fromarray(((~bg) * 255).astype(np.uint8), "L")
mask = mask.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
cut = src.convert("RGBA")
cut.putalpha(mask)
# Art direction: cropped at the chest, the outstretched arm runs off the left edge.
cut = cut.crop((0, 70, 1060, 1330))
cut = cut.resize((848, 1008), Image.LANCZOS)
save(cut, "dr-john-oda-portrait.webp", q=84)

# Tablet mock-up (sample Growth Pressure Index report).
tab = Image.open(raw("home-hero-tablet-diagnostic_")).convert("RGBA")
tab = tab.resize((760, round(760 * tab.size[1] / tab.size[0])), Image.LANCZOS)
save(tab, "growth-pressure-index-tablet.webp", q=84)

# Book stack.
book = Image.open(raw("book-unlimited-business-growth_")).convert("RGBA")
book = book.crop(book.getbbox())
book = book.resize((880, round(880 * book.size[1] / book.size[0])), Image.LANCZOS)
save(book, "unlimited-business-growth-book.webp", q=84)

# McClendon avatar (96 px source, avatar use only).
mc = Image.open(raw("home-testimonial-mcclendon_")).convert("RGB")
save(mc, "joseph-mcclendon.webp", q=88)

# Press logos: one flat colour, shape taken from the original's alpha or contrast.
INK = (19, 29, 41)
PRESS = [
    ("home-press-yahoofinance_", "press-yahoo-finance.webp"),
    ("home-press-newyorkweekly_", "press-new-york-weekly.webp"),
    ("home-press-americadailypost_", "press-america-daily-post.webp"),
    ("home-press-disrupt_", "press-disrupt.webp"),
    ("home-press-abc_", "press-abc.webp"),
    ("home-press-pbs_", "press-pbs.webp"),
    ("home-press-oprahandfriends_", "press-oprah-and-friends.webp"),
]
for prefix, name in PRESS:
    im = Image.open(raw(prefix))
    if im.mode == "RGBA":
        shape = np.asarray(im.split()[-1]).astype(np.float32)
    else:
        g = np.asarray(ImageOps.grayscale(im)).astype(np.float32)
        corners = np.concatenate([g[:3, :3].ravel(), g[-3:, -3:].ravel(),
                                  g[:3, -3:].ravel(), g[-3:, :3].ravel()])
        diff = np.abs(g - np.median(corners))
        shape = np.clip((diff - 6) / max(diff.max() - 6, 1) * 255 * 1.4, 0, 255)
    alpha = Image.fromarray(shape.astype(np.uint8), "L")
    flat = Image.new("RGBA", im.size, INK + (0,))
    flat.putalpha(alpha)
    bbox = alpha.point(lambda v: 255 if v > 24 else 0).getbbox()
    flat = flat.crop(bbox)
    save(flat, name, lossless=True)
