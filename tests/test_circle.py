import unittest

from pyscript import Circle, Point


class CircleTestCase(unittest.TestCase):

    def test_width_0(self):
        circle = Circle(0)
        self.assertEqual(circle.width(), 0)

    def test_width_1(self):
        circle = Circle(1)
        self.assertEqual(circle.width(), 2)

    def test_width_37(self):
        circle = Circle(37)
        self.assertEqual(circle.width(), 74)

    def test_height_0(self):
        circle = Circle(0)
        self.assertEqual(circle.height(), 0)

    def test_height_1(self):
        circle = Circle(1)
        self.assertEqual(circle.height(), 2)

    def test_height_37(self):
        circle = Circle(37)
        self.assertEqual(circle.height(), 74)

    def test_get_postscript_80_80_80(self):
        code = Circle(80)._get_postscript(Point(80, 80))
        self.assertEqual(
            code,
            "newpath\n"
            "80 80 80 0 360 arc\n"
            "stroke\n"
        )

    def test_get_postscript_20_160_40(self):
        code = Circle(40)._get_postscript(Point(20, 160))
        self.assertEqual(
            code,
            "newpath\n"
            "20 160 40 0 360 arc\n"
            "stroke\n"
        )
