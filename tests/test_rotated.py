from pyscript import RotatedShape, Rectangle

from shape_test_case import ShapeTestCase


class RotatedShapeTestCase(ShapeTestCase):

    def test_create_90(self):
        RotatedShape(Rectangle(10, 20), 90)

    def test_create_180(self):
        RotatedShape(Rectangle(10, 20), 180)

    def test_create_270(self):
        RotatedShape(Rectangle(10, 20), 270)

    def test_value_error_0(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), 0)

    def test_value_error_negative(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), -90)

    def test_value_error_45(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), 45)

    def test_value_error_100(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), 100)

    def test_value_error_360(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), 360)

    def test_value_error_720(self):
        with self.assertRaises(ValueError):
            RotatedShape(Rectangle(10, 20), 720)
