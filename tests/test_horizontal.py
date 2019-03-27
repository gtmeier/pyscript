import unittest

from pyscript import HorizontalShape, Circle, Rectangle


class HorizontalShapeTestCase(unittest.TestCase):

    def test_width_no_shapes(self):
        horizontal_shape = HorizontalShape()
        self.assertEqual(horizontal_shape.width(), 0)

    def test_width_single_shape(self):
        horizontal_shape = HorizontalShape(Circle(3))
        self.assertEqual(horizontal_shape.width(), 6)

    def test_width_multiple_shapes(self):
        horizontal_shape = HorizontalShape(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shape.width(), 2 + 5 + 42 + 0 + 3)
