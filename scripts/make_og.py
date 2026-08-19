#!/usr/bin/env python3
"""Typographic Open Graph card for the IBI Group / TTIE buyer record."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
OUT = "/workspace/assets/og.png"

BG = (17, 17, 16)
INK = (244, 243, 239)
MUTED = (168, 165, 157)
RULE = (52, 51, 48)
ACCENT = (176, 52, 28)

INTER = "/usr/share/fonts/truetype/macos/Inter-{}.ttf"


def font(weight, size):
    return ImageFont.truetype(INTER.format(weight), size)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Left rust spine
d.rectangle([0, 0, 10, H], fill=ACCENT)
# Top hairline
d.rectangle([10, 0, W, 3], fill=ACCENT)

pad_x = 72
y = 58

d.text((pad_x, y), "BUYER RECORD  ·  NOT A COURT FINDING", font=font("Medium", 20), fill=ACCENT)
y += 56

d.text((pad_x, y), "IBI Group / TTIE", font=font("Bold", 76), fill=INK)
y += 96
d.text((pad_x, y), "Efoil order  ·  DDP USA–NY  ·  Malaysia", font=font("SemiBold", 32), fill=INK)

y += 72
d.rectangle([pad_x, y, W - 72, y + 1], fill=RULE)
y += 36

facts = [
    ("~$10,000", "paid on the order"),
    ("Never arrived", "then storage / return bills"),
    ("First-person", "Ian Schechter"),
]
x = pad_x
for title, sub in facts:
    d.text((x, y), title, font=font("SemiBold", 26), fill=INK)
    d.text((x, y + 36), sub, font=font("Regular", 18), fill=MUTED)
    x += 340

d.rectangle([pad_x, H - 78, W - 72, H - 77], fill=RULE)
d.text(
    (pad_x, H - 54),
    "Mingonn  ·  Elaine  ·  Wise kharmuny  ·  Petaling Jaya",
    font=font("Medium", 18),
    fill=MUTED,
)
d.text(
    (W - 72, H - 54),
    "mrschechter.github.io",
    font=font("Medium", 18),
    fill=MUTED,
    anchor="rt",
)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, img.size)
