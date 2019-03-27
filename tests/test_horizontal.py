import unittest

from pyscript import HorizontalShapes, Circle, Rectangle


class HorizontalShapesTestCase(unittest.TestCase):

    def test_width_no_shapes(self):
        horizontal_shapes = HorizontalShapes()
        self.assertEqual(horizontal_shapes.width(), 0)

    def test_width_single_shape(self):
        horizontal_shapes = HorizontalShapes(Circle(3))
        self.assertEqual(horizontal_shapes.width(), 6)

    def test_width_multiple_shapes(self):
        horizontal_shapes = HorizontalShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shapes.width(), 2 + 5 + 42 + 0 + 3)
