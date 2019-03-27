import unittest

from pyscript import Circle


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
