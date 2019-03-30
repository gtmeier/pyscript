from pyscript import LayeredShapes, Circle, Rectangle

from shape_test_case import ShapeTestCase


class LayeredShapesTestCase(ShapeTestCase):

    def test_get_width_no_shapes(self):
        shape = LayeredShapes()
        self.assertEqual(shape._get_width(), 0)

    def test_get_width_single_shape(self):
        shape = LayeredShapes(Circle(3))
        self.assertEqual(shape._get_width(), 6)

    def test_get_width_multiple_shapes(self):
        shape = LayeredShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(shape._get_width(), 42)

    def test_get_height_no_shapes(self):
        shape = LayeredShapes()
        self.assertEqual(shape._get_height(), 0)

    def test_get_height_single_shape(self):
        shape = LayeredShapes(Rectangle(1, 5))
        self.assertEqual(shape._get_height(), 5)

    def test_get_height_multiple_shapes(self):
        shape = LayeredShapes(
            Circle(1),
            Rectangle(5, 10),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(shape._get_height(), 10)
