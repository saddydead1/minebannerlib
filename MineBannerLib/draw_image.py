from nbtlib import parse_nbt
import os
from PIL import Image
from MineBannerLib.pattern import pattern
from MineBannerLib.color import Color
from MineBannerLib.layer import Layer


def createImg(layers: list, name: str):
    w, h = 20, 40
    new_image = Image.new('RGBA', (w, h), (255, 255, 255, 255))
    new_pixels = new_image.load()

    for layer in layers:

        img = Image.open(f'{os.path.dirname(os.path.abspath(__file__))}/samples/{pattern[layer.pattern]}.png').convert("RGBA")

        pixels = img.load()

        clr = Color(layer.color)

        for i in range(w):
            for j in range(h):
                new_pixels[i, j] = maxColors(combineColors(pixels[i + 1, j + 1], clr.rgb), new_pixels[i, j])

    if not os.path.exists('./buildbanner/'):
        os.mkdir('./buildbanner')
    new_image.save(f'./buildbanner/{name}.png', "PNG")


def combineColors(a, b):
    return int(a[0] / 255.0 * b[0]), int(a[1] / 255.0 * b[1]), int(a[2] / 255.0 * b[2]), a[3]


def maxColors(a, b):
    alpha_zero = a[3] / 255.0 + b[3] / 255.0 * (1 - a[3] / 255.0)
    red_zero = zero(a[0] / 255.0, b[0] / 255.0, a[3] / 255.0, b[3] / 255.0, alpha_zero)
    green_zero = zero(a[1] / 255.0, b[1] / 255.0, a[3] / 255.0, b[3] / 255.0, alpha_zero)
    blue_zero = zero(a[2] / 255.0, b[2] / 255.0, a[3] / 255.0, b[3] / 255.0, alpha_zero)
    return int(red_zero * 255), int(green_zero * 255), int(blue_zero * 255), int(alpha_zero * 255)


def zero(a, b, alpha_a, alpha_b, alpha):
    return (a * alpha_a + b * alpha_b * (1 - alpha_a)) / alpha


def get_parts_flag_from_nbts(nbts, clr: int):
    comp = parse_nbt(nbts)
    tags = [Layer(pattern='b', color=clr)]
    for i in comp['BlockEntityTag']['Patterns']:
        layer = Layer(pattern=i['Pattern'], color=i['Color'])
        tags.append(layer)
    return tags
