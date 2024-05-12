from nbtlib import parse_nbt
from multipledispatch import dispatch
from dataclasses import dataclass
import enum
import os
from PIL import Image, ImageOps


pattern = {"b": "base",
         "bo": "borber",
         "bri": "bricks",
         "mc": "circle",
         "cre": "creeper",
         "cr": "cross",
         "cbo": "curly_border",
         "ld": "diagonal_left",
         "rud": "diagonal_right",
         "lud": "diagonal_up_left",
         "rd": "diagonal_up_right",
         "flo": "flower",
         "glb": "globe",
         "gra": "gradient",
         "gru": "gradient_up",
         "hh": "half_horizontal",
         "hhb": "half_horizontal_bottom",
         "vh": "half_vertical",
         "vhr": "half_vertical_right",
         "moj": "mojang",
         "pig": "piglin",
         "mr": "rhombus",
         "sku": "skull",
         "ss": "small_stripes",
         "bl": "square_bottom_left",
         "br": "square_bottom_right",
         "tl": "square_top_left",
         "tr": "square_top_right",
         "sc": "straight_cross",
         "bs": "stripe_bottom",
         "cs": "stripe_center",
         "dls": "stripe_down_left",
         "drs":  "stripe_down_right",
         "ls": "stripe_left",
         "ms":  "stripe_middle",
         "rs":  "stripe_right",
         "ts": "stripe_top",
         "bt": "triangle_bottom",
        "tt": "triangle_top",
        "bts": "triangles_bottom",
        "tts": "triangles_top"}

class Color(enum.IntEnum):
    def __new__(cls, value, defuse_color):
        member = int.__new__(cls, value)
        member._value_ = value
        member.defuse_color = defuse_color
        r = ((defuse_color >> 16) & 255)
        g = ((defuse_color >> 8) & 255)
        b = (defuse_color & 255)
        member.rgb = r, g, b, 0
        return member

    White = 0, 16383998
    Orange = 1, 16351261
    Magenta = 2, 13061821
    LightBlue = 3, 3847130
    Yellow = 4, 16701501
    Lime  = 5, 8439583
    Pink = 6, 15961002
    Gray = 7, 4673362
    LightGray = 8, 10329495
    Cyan = 9, 1481884
    Purple = 10, 8991416
    Blue = 11, 3949738
    Brown = 12, 8606770
    Green = 13, 6192150
    Red = 14, 11546150
    Black = 15, 1908001


@dataclass
class Layer:
    pattern: str
    color: int


def createImg(layers: list, name: str):
    w, h = 20, 40
    new_image = Image.new('RGBA', (w, h), (255, 255, 255, 255))
    new_pixels = new_image.load()

    for layer in layers:

        img = Image.open(f'./MineBannerLib/samples/{pattern[layer.pattern]}.png').convert("RGBA")

        pixels = img.load()

        clr = Color(layer.color)


        for i in range(w):
            for j in range(h):
                new_pixels[i, j] = maxColors(combineColors(pixels[i+1, j+1], clr.rgb), new_pixels[i, j])


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


@dispatch(str, str, int)
def create_banner(name: str, nbts: str, base_color: int):
    createImg(get_parts_flag_from_nbts(nbts, base_color), name)

@dispatch(str, list, int)
def create_banner(name: str, nbts: list, base_color: int):
    nbts.insert(0, Layer(pattern='b', color=base_color))
    createImg(nbts, name)
