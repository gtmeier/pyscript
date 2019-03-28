import unittest

from pyscript import Rectangle, Point


class RectangleTestCase(unittest.TestCase):

    def test_width_0(self):
        rectangle = Rectangle(0, 5)
        self.assertEqual(rectangle.width(), 0)

    def test_width_1(self):
        rectangle = Rectangle(1, 5)
        self.assertEqual(rectangle.width(), 1)

    def test_width_37(self):
        rectangle = Rectangle(37, 5)
        self.assertEqual(rectangle.width(), 37)

    def test_height_0(self):
        rectangle = Rectangle(5, 0)
        self.assertEqual(rectangle.height(), 0)

    def test_height_1(self):
        rectangle = Rectangle(5, 1)
        self.assertEqual(rectangle.height(), 1)

    def test_height_37(self):
        rectangle = Rectangle(5, 37)
        self.assertEqual(rectangle.height(), 37)

    def test_get_postscript(self):
        code = Rectangle(40, 80)._get_postscript(Point(100, 100))
        self.assertEqual(
            code,
            "newpath\n"
            "80.0 60.0 moveto\n"
            "40 0 rlineto\n"
            "0 80 rlineto\n"
            "-40 0 rlineto\n"
            "closepath\n"
            "stroke\n"
        )
