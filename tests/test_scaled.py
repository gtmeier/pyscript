from pyscript import ScaledShape, Rectangle

from shape_test_case import ShapeTestCase


class ScaledShapeTestCase(ShapeTestCase):

    def test_get_width_0(self):
        rectangle = ScaledShape(Rectangle(0, 5), 2, 3)
        self.assertEqual(rectangle._get_width(), 0 * 2)

    def test_get_width_1(self):
        rectangle = ScaledShape(Rectangle(1, 5), 2, 3)
        self.assertEqual(rectangle._get_width(), 1 * 2)

    def test_get_width_37(self):
        rectangle = ScaledShape(Rectangle(37, 5), 2, 3)
        self.assertEqual(rectangle._get_width(), 37 * 2)

    def test_get_height_0(self):
        rectangle = ScaledShape(Rectangle(5, 0), 2, 3)
        self.assertEqual(rectangle._get_height(), 0 * 3)

    def test_get_height_1(self):
        rectangle = ScaledShape(Rectangle(5, 1), 2, 3)
        self.assertEqual(rectangle._get_height(), 1 * 3)

    def test_get_height_37(self):
        rectangle = ScaledShape(Rectangle(5, 37), 2, 3)
        self.assertEqual(rectangle._get_height(), 37 * 3)
