#coding: utf-8

from ._base import db
from .color import Color

__all__ = ['Image']


class Image(db.Model):
    _suffix = 'jpg'

    id = db.Column(db.Integer, primary_key=True)
    palette = db.relationship(Color, backref='image', lazy='select')

    @property
    def name(self):
        return '%d.%s' % (self.id, self._suffix)
