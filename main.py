#coding: utf-8

from os import path, listdir

from calculate import _open_image, _convert, _get_colors
from calculate import _save_image, _resize, _thumbnail
from config import src_path, allow_extensions, thumbnail_size
from config import color_count, tpl_name, out_name, thumbnail_path, row_count
from render import render, write


def _build_path():
    return src_path


def _get_images(dest):
    ret = []
    for img in listdir(dest):
        if path.splitext(img)[1].lower() in allow_extensions:
            ret.append((img, path.join(dest, img)))

    return ret


def _process(filename, filepath, color_count):
    raw = _open_image(filepath)
    raw = _thumbnail(raw, thumbnail_size)
    _save_image(raw, path.join(thumbnail_path, filename))
    img = _convert(raw)
    ret = _get_colors(img, color_count)
    count = len(ret) / row_count
    return [ret[i:i + count] for i in range(0, len(ret), count)]


def _build_data():
    data = []
    dest = _build_path()
    for f in _get_images(dest):
        data.append({
            'name': f[0],
            'pallete': _process(f[0], f[1], color_count)
            })

    return data


def _main():
    write(render(tpl_name, _build_data()), out_name)


if __name__ == '__main__':
    _main()
