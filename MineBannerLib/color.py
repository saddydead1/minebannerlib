import enum


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
    Lime = 5, 8439583
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