import unittest

from pyscript import Square


class SquareTestCase(unittest.TestCase):

    def test_side_length_0(self):
        square = Square(0)
        self.assertEqual(square._side_length, 0)

    def test_side_length_1(self):
        square = Square(1)
        self.assertEqual(square._side_length, 1)

    def test_side_length_54(self):
        square = Square(54)
        self.assertEqual(square._side_length, 54)

    def test_num_sides_4(self):
        square = Square(1)
        self.assertEqual(square._num_sides, 4)

    def test_width(self):
        square = Square(1)
        self.assertEqual(square._get_width(), 1)

    def test_width(self):
        square = Square(23)
        self.assertEqual(square._get_width(), 23)

    def test_width(self):
        square = Square(59)
        self.assertEqual(square._get_width(), 59)

    def test_height(self):
        square = Square(31)
        self.assertEqual(square._get_height(), 31)

    def test_height(self):
        square = Square(79)
        self.assertEqual(square._get_height(), 79)

    def test_height(self):
        square = Square(131)
        self.assertEqual(square._get_height(), 131)

    # FIXME
    # def test_get_postscript(self):
    #     code = Square(40)._get_postscript(Point(100, 100))
    #     self.assertEqual(
    #         code,
    #         "newpath\n"
    #         "80.0 80.0 moveto\n"
    #         "40 0 rlineto\n"
    #         "0 40 rlineto\n"
    #         "-40 0 rlineto\n"
    #         "closepath\n"
    #         "stroke\n"
    #     )
