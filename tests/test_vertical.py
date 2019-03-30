from pyscript import VerticalShapes, Circle, Rectangle

from shape_test_case import ShapeTestCase


class VerticalShapesTestCase(ShapeTestCase):

    def test_get_width_no_shapes(self):
        horizontal_shapes = VerticalShapes()
        self.assertEqual(horizontal_shapes._get_width(), 0)

    def test_get_width_single_shape(self):
        horizontal_shapes = VerticalShapes(Circle(3))
        self.assertEqual(horizontal_shapes._get_width(), 6)

    def test_get_width_multiple_shapes(self):
        horizontal_shapes = VerticalShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shapes._get_width(), 42)

    def test_get_height_no_shapes(self):
        horizontal_shapes = VerticalShapes()
        self.assertEqual(horizontal_shapes._get_height(), 0)

    def test_get_height_single_shape(self):
        horizontal_shapes = VerticalShapes(Circle(3))
        self.assertEqual(horizontal_shapes._get_height(), 6)

    def test_get_height_multiple_shapes(self):
        horizontal_shapes = VerticalShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shapes._get_height(), 2 + 10 + 42 + 1 + 9)
