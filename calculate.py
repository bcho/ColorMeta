#coding: utf-8

from PIL import Image

from config import SAMPLE_COUNT, DIFF

from color import rgb2lab, deltaE


def _open_image(filename, size):
    ret = Image.open(filename)
    ret.thumbnail(size, Image.ANTIALIAS)
    return ret


def _save_image(image, filename):
    image.save(filename)


def _convert(image):
    try:
        return image.convert('P',
            palette=Image.ADAPTIVE, colors=SAMPLE_COUNT)
    except:
        # convert to RGB mode (without changing transparent to white)
        image = image.convert('RGB')
        return image.convert('P',
            palette=Image.ADAPTIVE, colors=SAMPLE_COUNT)


def _get_colors(image, color_count, is_hex=False):
    def __compare(sample, control_group):
        def is_notice(a, b):
            lab_a = rgb2lab(a[0], a[1], a[2])
            lab_b = rgb2lab(b[0], b[1], b[2])
            return deltaE(lab_a, lab_b) < DIFF

        for color in control_group:
            if is_notice(sample, color):
                return False
        return True

    def __pop(l):
        while l:
            yield [l.pop(0) for i in xrange(3)]

    def __hex(l):
        return "#%02x%02x%02x" % (l[0], l[1], l[2])

    payload = image.getpalette()[0:SAMPLE_COUNT * 3]
    ret = []
    for i in __pop(payload):
        if not __compare(i, ret):
            continue
        else:
            ret.append((i[0], i[1], i[2]))
        if len(ret) == color_count:
            break

    if is_hex:
        for i in xrange(len(ret)):
            ret[i] = __hex(ret[i])

    return ret
