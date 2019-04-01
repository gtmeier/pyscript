import unittest

from pyscript import Spacer, Point


# TODO: tests for export_postscript


class SpacerTestCase(unittest.TestCase):

    def test_get_width_0(self):
        spacer = Spacer(0, 5)
        self.assertEqual(spacer._get_width(), 0)

    def test_get_width_1(self):
        spacer = Spacer(1, 5)
        self.assertEqual(spacer._get_width(), 1)

    def test_get_width_37(self):
        spacer = Spacer(37, 5)
        self.assertEqual(spacer._get_width(), 37)

    def test_get_height_0(self):
        spacer = Spacer(5, 0)
        self.assertEqual(spacer._get_height(), 0)

    def test_get_height_1(self):
        spacer = Spacer(5, 1)
        self.assertEqual(spacer._get_height(), 1)

    def test_get_height_37(self):
        spacer = Spacer(5, 37)
        self.assertEqual(spacer._get_height(), 37)
