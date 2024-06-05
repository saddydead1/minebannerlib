from multipledispatch import dispatch
from MineBannerLib import draw_image as dr
from MineBannerLib.layer import Layer


@dispatch(str, str, int)
def create_banner(name: str, nbts: str, base_color: int):
    dr.createImg(dr.get_parts_flag_from_nbts(nbts, base_color), name)


@dispatch(str, list, int)
def create_banner(name: str, nbts: list, base_color: int):
    nbts.insert(0, Layer(pattern='b', color=base_color))
    dr.createImg(nbts, name)
