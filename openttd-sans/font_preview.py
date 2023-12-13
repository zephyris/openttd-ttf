#!/usr/bin/python3

import sys
from PIL import Image, ImageDraw, ImageFont

fontpath = "OpenTTD-Sans.ttf"
size = 10
background = (131, 133, 133)
background_shade = [(168, 168, 168), (98, 101, 98)]
foreground = (252, 252, 252)
shadow = (16, 16, 16)

def shadowtext(draw, scale, position, string, font, foreground, background):
    if background is not None:
        draw.text(((position[0] + 1) * scale, (position[1] + 1) * scale), string, font=font, fill=background)
    draw.text((position[0] * scale, position[1] * scale), string, font=font, fill=foreground)

scales = [1, 2, 4]
fontmodes = [{
    "mode": None,
    "description": "anti-aliased"
}, {
    "mode": "1",
    "description": "aliased"
}]

for scale in scales:
    for fontmode in fontmodes:
        image = Image.new("RGB", (400 * scale, int(7.5 * size * scale)), background_shade[1])
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background_shade[0], outline=None)
        draw.rectangle((0 + scale, 0 + scale, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background, outline=None)
        if fontmode["mode"] is not None:
            draw.fontmode = fontmode["mode"]
        font = ImageFont.truetype(fontpath, size * scale)
        shadowtext(draw, scale, (3, 2 + size * 0), "OpenTTD Sans", font, (252, 176, 48), shadow)
        shadowtext(draw, scale, (3, 2 + size * 1), "A pixel art-style font for OᴘᴇɴTTD, inspired by Transport Tycoon Deluxe.", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + size * 2), "Numerics: 0123456789 ½¾¾ 6×7=42 95%", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + size * 3), "Upper case: ABCDEFGHIJKLMNOPQRSTUVWXYZ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + size * 4), "Lower case: abcdefghijklmnopqrstuvwxyz", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + size * 5), "Diacritics: ÀÁÂÃÄÅĀĂĄÆāàáâãäåăąæ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + size * 6), "Currencies: $£¥₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿", font, foreground, shadow)
        image.save("OpenTTD-Sans-" + str(scale * size) + "px-" + fontmode["description"] + ".png", "PNG")