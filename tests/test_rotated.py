from pyscript import RotatedShape, Rectangle

from shape_test_case import ShapeTestCase


class RotatedShapeTestCase(ShapeTestCase):

    def test_create_90(self):
        RotatedShape(Rectangle(10, 20), 90)

    def test_create_180(self):
        RotatedShape(Rectangle(10, 20), 180)

    def test_create_270(self):
        RotatedShape(Rectangle(10, 20), 270)
