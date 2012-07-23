#coding: utf-8

from os import path, listdir

from calculate import _open_image, _convert, _get_colors


def _build_path():
    return 'screenshot'


def _get_images(dest):
    allow_extensions = ['.png', '.jpg', '.bmp']
    ret = []
    for img in listdir(dest):
        if path.splitext(img)[1].lower() in allow_extensions:
            ret.append((img, path.join(dest, img)))

    return ret


def _process(filename, color_count):
    size = 800, 800
    raw = _open_image(filename, size)
    img = _convert(raw, color_count)
    return _get_colors(img, color_count, True)


def _main():
    dest = _build_path()
    for f in _get_images(dest):
        print f
        print _process(f[0], 8)


if __name__ == '__main__':
    _main()
