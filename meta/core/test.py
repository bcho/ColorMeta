#coding: utf-8

import color
import models


if __name__ == '__main__':
    image = models.PixelImage('xx.png')
    image.save('test.png')
    for c in image.colors(10):
        print color.rgb2hex(*c)
