import unittest
import math

from pyscript import Triangle


class TriangleTestCase(unittest.TestCase):
    def test_side_length_0(self):
        triangle = Triangle(0)
        self.assertEqual(triangle._side_length, 0)

    def test_side_length_1(self):
        triangle = Triangle(1)
        self.assertEqual(triangle._side_length, 1)

    def test_side_length_54(self):
        triangle = Triangle(54)
        self.assertEqual(triangle._side_length, 54)

    def test_num_sides_3(self):
        triangle = Triangle(1)
        self.assertEqual(triangle._num_sides, 3)

    def test_width(self):
        triangle = Triangle(1)
        self.assertEqual(triangle._get_width(), 1)

    def test_width(self):
        triangle = Triangle(39)
        self.assertEqual(triangle._get_width(), 39)

    def test_width(self):
        triangle = Triangle(71)
        self.assertEqual(triangle._get_width(), 71)

    def test_height(self):
        triangle = Triangle(1)
        self.assertEqual(triangle._get_height(), math.sqrt(1**2-(1/2)**2))

    # def test_height(self):
    #     triangle = Triangle(51)
    #     self.assertEqual(triangle._get_height(),
    #         math.sqrt(51**2 - (51/2)**2))
    #
    # def test_height(self):
    #     triangle = Triangle(137)
    #     self.assertEqual(triangle._get_height(),
    #         math.sqrt(math.pow(137, 2)-math.pow((137/2), 2)))
