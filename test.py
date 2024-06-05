from MineBannerLib import create_banner as mbl
from MineBannerLib.layer import Layer

nbts = '{BlockEntityTag:{Patterns:[{Color:14,Pattern:"cre"},{Color:4,Pattern:"sku"}]}}'
color_base = 15
name = 'test'
name2 = 'test2'
parts = [Layer('hh', 2), Layer('mc', 1), Layer('cre', 3)]


def test1():
    mbl.create_banner(name, nbts, color_base)


def test2():
    mbl.create_banner(name2, parts, color_base)


if __name__ == '__main__':
    test1()
    test2()
