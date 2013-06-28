#coding: utf-8

from ._base import db

from meta.core import color

__all__ = ['Color']


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hexcode = db.Column(db.String(6), null=False)

    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))

    @property
    def rgb(self):
        return color.hex2rgb(self.hexcode)

    @property
    def xyz(self):
        return color.rgb2xyz(*self.rgb)
