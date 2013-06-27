#coding: utf-8

from PIL import Image

from color import rgb2lab, rgb2hex, deltaE


class MetaImage(object):
    diff = 15
    thumbnail_size = 100, 100
    palette_sample = 256

    '''Provide a Image proxy object with handful function.'''
    def __init__(self, name):
        self._image = Image.open(name)
        self.thumbnail(self.thumbnail_size)
        self.convert()

    def thumbnail(self, size):
        self._image.thumbnail(size, Image.ANTIALIAS)

    def resize(self, size):
        self._image.resize(size, Image.ANTIALIAS)

    def save(self, name):
        self._image.save(name)

    def convert(self):
        try:
            self._image = self._image.convert('P', palette=Image.ADAPTIVE,
                    colors=self.palette_sample)
        except:
            # convert to RGB mode (without changing transparent to white)
            self._image = self._image.convert('RGB')
            self._image = self._image.convert('P', palette=Image.ADAPTIVE,
                    colors=self.palette_sample)

    def colors(self, maximum=5):
        pass

    @property
    def image(self):
        return self._image

    def __getattr__(self, name):
        return getattr(self._image, name)


class QuanImage(MetaImage):
    def colors(self, maximum=5):
        def _cmp(current, picked):
            def is_notice(b):
                return deltaE(rgb2lab(*current), rgb2lab(*b)) < self.diff

            return not any(map(is_notice, picked))

        def _group(colors):
            '''Pop (r, g, b) from given palette.'''
            while colors:
                yield [colors.pop(0) for i in range(3)]

        palette, ret = self.image.getpalette(), []
        for group in _group(palette):
            if _cmp(group, ret):
                ret.append(tuple(group))
            if len(ret) == maximum:
                break

        return ret


class PixelImage(MetaImage):
    def convert(self):
        self._image = self._image.convert('RGB', palette=Image.ADAPTIVE)

    def colors(self, maximum=5):
        def _cmp(current, picked):
            def is_notice(b):
                return deltaE(rgb2lab(*current), rgb2lab(*b)) < self.diff

            return not any(map(is_notice, picked))

        pixels, picked, ret = {}, [], []

        for group in list(self.image.getdata()):
            _hex = rgb2hex(*group)
            if not _hex in pixels:
                pixels[_hex] = [group, 1]
            else:
                pixels[_hex][1] = pixels[_hex][1] + 1

        pixels = pixels.values()
        pixels.sort(key=lambda x: x[1], reverse=True)
        pixels = [i[0] for i in pixels]

        for i in pixels:
            if _cmp(i, picked):
                picked.append(i)
                ret.append(i)
            if len(ret) >= maximum:
                break

        return ret
