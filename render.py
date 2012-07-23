#coding: utf-8

from jinja2 import Environment, FileSystemLoader

from config import tpl_path


ENV = Environment(loader=FileSystemLoader(tpl_path))


def render(tpl_name, var):
    tpl = ENV.get_template(tpl_name)
    return tpl.render(data=var)


def write(content, dest):
    fp = open(dest, 'w')
    fp.write(content)
    fp.close()
