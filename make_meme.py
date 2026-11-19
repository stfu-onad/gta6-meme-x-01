#!/usr/bin/env python3
"""Composite the GTA 6 meme captions onto the base art.

The base art (base-art.png) shows a gamer faking sick on launch day,
thermometer in mouth, controller in hand, Vice City neon on the TV,
with make.fun's white ghost mascot beside him holding its magenta
star coin. This script burns the two caption lines into the picture
in classic meme style: bold white letters with a thick black stroke,
one line across the top, one across the bottom, sized so both stay
readable when the picture is shrunk to 480x480.

Output: meme.png in this directory.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BASE_ART = HERE / "base-art.png"
OUTPUT = HERE / "meme.png"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

TOP_LINE = "WAITED 13 YEARS FOR GTA 6"
BOTTOM_LINE = "CALLED IN SICK ON LAUNCH DAY"


def fit_font(draw: ImageDraw.ImageDraw, text: str, width: int, start_size: int) -> ImageFont.FreeTypeFont:
    """Shrink the font until the line fits inside `width` pixels."""
    size = start_size
    font = ImageFont.truetype(FONT_PATH, size)
    while draw.textlength(text, font=font) > width and size > 20:
        size -= 4
        font = ImageFont.truetype(FONT_PATH, size)
    return font


def draw_caption(draw: ImageDraw.ImageDraw, text: str, y: int, width: int, start_size: int) -> None:
    font = fit_font(draw, text, int(width * 0.94), start_size)
    x = (width - draw.textlength(text, font=font)) / 2
    draw.text(
        (x, y),
        text,
        font=font,
        fill="white",
        stroke_width=max(3, start_size // 14),
        stroke_fill="black",
    )


def main() -> None:
    img = Image.open(BASE_ART).convert("RGB")
    width, height = img.size
    draw = ImageDraw.Draw(img)
    start_size = int(width * 0.062)
    draw_caption(draw, TOP_LINE, int(height * 0.015), width, start_size)
    draw_caption(draw, BOTTOM_LINE, int(height * 0.925), width, start_size)
    img.save(OUTPUT)
    print(f"wrote {OUTPUT} ({width}x{height})")


if __name__ == "__main__":
    main()
