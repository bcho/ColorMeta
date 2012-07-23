#coding: utf-8

from os import path, listdir

from calculate import _open_image, _convert, _get_colors
from config import src_path, allow_extensions, thumbnail_size
from config import color_count, tpl_name, out_name
from render import render, write


def _build_path():
    return src_path


def _get_images(dest):
    ret = []
    for img in listdir(dest):
        if path.splitext(img)[1].lower() in allow_extensions:
            ret.append((img, path.join(dest, img)))

    return ret


def _process(filename, color_count):
    raw = _open_image(filename, thumbnail_size)
    img = _convert(raw, color_count)
    return _get_colors(img, color_count, True)


def _build_data():
    data = []
    dest = _build_path()
    for f in _get_images(dest):
        data.append({
            'name': f[0],
            'path': f[1],
            'pallete-data': _process(f[1], color_count)
            })

    return data


def _main():
    write(render(tpl_name, _build_data()), out_name)


if __name__ == '__main__':
    _main()
