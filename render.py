#coding: utf-8

import os
from jinja2 import Environment, FileSystemLoader

from config import tpl_path, thumbnail_path


ENV = Environment(loader=FileSystemLoader(tpl_path))


def thumbnail(name):
    return os.path.join(thumbnail_path, name)


def tohex(l):
    return "#%02x%02x%02x" % (l[0], l[1], l[2])


def render(tpl_name, var):
    tpl = ENV.get_template(tpl_name)
    return tpl.render(sites=var)


def write(content, dest):
    fp = open(dest, 'w')
    fp.write(content)
    fp.close()


ENV.filters = {
        'thumbnail': thumbnail,
        'hex': tohex
        }
