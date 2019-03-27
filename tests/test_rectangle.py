import unittest

from pyscript import Rectangle


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
