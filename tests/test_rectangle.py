import unittest

import pyscript


class RectangleTestCase(unittest.TestCase):

    def test_width_0(self):
        rectangle = pyscript.Rectangle(0, 5)
        self.assertEqual(rectangle.width(), 0)

    def test_width_1(self):
        rectangle = pyscript.Rectangle(1, 5)
        self.assertEqual(rectangle.width(), 1)

    def test_width_37(self):
        rectangle = pyscript.Rectangle(37, 5)
        self.assertEqual(rectangle.width(), 37)
