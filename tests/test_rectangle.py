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
