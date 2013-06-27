#coding: utf-8

from config import DIFF
from color import rgb2lab, deltaE

import color


def colors(image, maximum):
    def _cmp(current, picked):
        def is_notice(b):
            return deltaE(rgb2lab(*current), rgb2lab(*b)) < DIFF

        return not any(map(is_notice, picked))

    def _group(colors):
        '''Pop (r, g, b) from given palette.'''
        while colors:
            yield [colors.pop(0) for i in range(3)]

    palette, ret = image.getpalette(), []
    for group in _group(palette):
        if _cmp(group, ret):
            ret.append(tuple(group))
        if len(ret) == maximum:
            break

    return ret
