#coding: utf-8

import unittest

from meta.testsuite import MetaTestCase
from meta.core import color


class ColorTestCase(MetaTestCase):

    def test_rgb2hex(self):
        self.assertEqual('#000000', color.rgb2hex(0, 0, 0))
        self.assertEqual('#cb3f20', color.rgb2hex(203, 63, 32))
        self.assertEqual('#ffffff', color.rgb2hex(255, 255, 255))

    def test_rgb2xyz(self):
        x, y, z = color.rgb2xyz(203, 63, 32)
        self.assertEqualFloat(x, 26.667)
        self.assertEqualFloat(y, 16.356)
        self.assertEqualFloat(z, 3.118)

    def test_xyz2lab(self):
        l, a, b = color.xyz2lab(26.667, 16.356, 3.118)
        self.assertEqualFloat(l, 47.438)
        self.assertEqualFloat(a, 53.887)
        self.assertEqualFloat(b, 48.187)

    def test_rgb2lab(self):
        l, a, b = color.rgb2lab(203, 63, 32)
        self.assertEqualFloat(l, 47.438)
        self.assertEqualFloat(a, 53.887)
        self.assertEqualFloat(b, 48.187)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ColorTestCase))
    return suite
