from pyscript import RotatedShape, Rectangle

from shape_test_case import ShapeTestCase


# TODO: tests for export_postscript


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

    def test_get_width_90(self):
        shape = RotatedShape(Rectangle(20, 30), 90)
        self.assertEqual(shape._get_width(), 30)

    def test_get_width_180(self):
        shape = RotatedShape(Rectangle(20, 30), 180)
        self.assertEqual(shape._get_width(), 20)

    def test_get_width_270(self):
        shape = RotatedShape(Rectangle(20, 30), 270)
        self.assertEqual(shape._get_width(), 30)

    def test_get_height_90(self):
        shape = RotatedShape(Rectangle(20, 30), 90)
        self.assertEqual(shape._get_height(), 20)

    def test_get_height_180(self):
        shape = RotatedShape(Rectangle(20, 30), 180)
        self.assertEqual(shape._get_height(), 30)

    def test_get_height_270(self):
        shape = RotatedShape(Rectangle(20, 30), 270)
        self.assertEqual(shape._get_height(), 20)
