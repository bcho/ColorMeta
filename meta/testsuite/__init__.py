#coding: utf-8

import unittest


class MetaTestCase(unittest.TestCase):
    eps = 0.001

    def assertEqualFloat(self, a, b):
        return self.assertTrue(abs(a - b) < self.eps)


class BetterLoader(unittest.TestLoader):

    def loadTestsFromName(self, name, module=None):
        # run all the tests
        return suite()


def suite():
    from meta.testsuite import color
    suite = unittest.TestSuite()
    suite.addTest(color.suite())

    return suite


def main():
    try:
        unittest.main(testLoader=BetterLoader(), defaultTest='suite')
    except Exception as e:
        print 'Error: %s' % e
