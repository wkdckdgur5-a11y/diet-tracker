"""Generate PWA icon set for 내 식단 트래커.
Matches the existing favicon design: teal-deep background (#123F3D)
with an amber (#C1571C) '食' glyph.
Run: python scripts/gen_icons.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

TEAL_DEEP = "#123F3D"
AMBER = "#C1571C"
FONT_PATH = r"C:\Windows\Fonts\malgunbd.ttf"

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(OUT_DIR, exist_ok=True)


def make_icon(size, path, maskable=False, corner_radius_ratio=0.0):
    img = Image.new("RGB", (size, size), TEAL_DEEP)
    draw = ImageDraw.Draw(img)

    if corner_radius_ratio > 0:
        # Rounded-square mask for standard (non-maskable) icons
        mask = Image.new("L", (size, size), 0)
        mdraw = ImageDraw.Draw(mask)
        r = int(size * corner_radius_ratio)
        mdraw.rounded_rectangle([0, 0, size - 1, size - 1], radius=r, fill=255)
        bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        bg.paste(img, (0, 0), mask)
        img = bg
        draw = ImageDraw.Draw(img)

    # Maskable icons need extra safe-zone padding (glyph within ~66% center circle)
    glyph_scale = 0.42 if maskable else 0.6
    font_size = int(size * glyph_scale)
    font = ImageFont.truetype(FONT_PATH, font_size)

    text = "食"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) / 2 - bbox[0]
    y = (size - th) / 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=AMBER)

    img.save(path)
    print("wrote", path, img.size)


make_icon(192, os.path.join(OUT_DIR, "icon-192.png"), corner_radius_ratio=0.18)
make_icon(512, os.path.join(OUT_DIR, "icon-512.png"), corner_radius_ratio=0.18)
make_icon(512, os.path.join(OUT_DIR, "icon-maskable-512.png"), maskable=True)
make_icon(180, os.path.join(OUT_DIR, "apple-touch-icon.png"), corner_radius_ratio=0.0)
