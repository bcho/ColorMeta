#coding: utf-8


def rgb2xyz(r, g, b):
    # RGB to CIE XYZ REC 709
    # http://www.easyrgb.com/index.php?X=MATH&H=02#text2
    def _rgb(c):
        percentage = c / 255.0
        if percentage > 0.04045:
            return ((percentage + 0.055) / 1.055) ** 2.4 * 100
        else:
            return percentage / 12.92 * 100

    R = _rgb(r)
    G = _rgb(g)
    B = _rgb(b)

    x = R * 0.4124 + G * 0.3576 + B * 0.1805
    y = R * 0.2126 + G * 0.7152 + B * 0.0722
    z = R * 0.0193 + G * 0.1192 + B * 0.9505

    return (x, y, z)


def xyz2lab(x, y, z):
    # CIE XYZ REC 709 to CIE L*ab
    # http://www.easyrgb.com/index.php?X=MATH&H=07#text7
    ref = (95.047, 100.000, 108.883)

    def _xyz(c, ref_c):
        percentage = c / ref_c
        if percentage > 216 / 24389.0:
            return percentage ** (1 / 3.0)
        else:
            return ((24389 / 27.0) * percentage + 16) / 116.0

    X = _xyz(x, ref[0])
    Y = _xyz(y, ref[1])
    Z = _xyz(z, ref[2])

    L = (116 * Y) - 16
    a = 500 * (X - Y)
    b = 200 * (Y - Z)

    return (L, a, b)


def rgb2lab(r, g, b):
    x, y, z = rgb2xyz(r, g, b)
    return xyz2lab(x, y, z)


def rgb2hex(r, g, b, leading='#'):
    return '%s%02x%02x%02x' % (leading, r, g, b)


def deltaE(a, b):
    # Delta E CIE76
    # http://en.wikipedia.org/wiki/Color_difference#Delta_E
    # JND = 2.3
    delta_e = 0
    for pair in zip(a, b):
        delta_e += (pair[0] - pair[1]) ** 2

    return delta_e ** 0.5
