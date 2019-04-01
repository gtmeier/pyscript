import unittest

from pyscript import (
    Point, Rectangle, Spacer, Square, Circle, HorizontalShapes, VerticalShapes,
    LayeredShapes, ScaledShape, RotatedShape, Triangle, Polygon
)

from shape_test_case import ShapeTestCase


class AllShapesTestCase(unittest.TestCase):

    rectangle = Rectangle(100, 60)
    spacer = Spacer(40, 40)
    square = Square(80)
    base_circle = Circle(80)
    polygon = Polygon(5, 20)
    triangle = Triangle(20)
    vertical_shapes = VerticalShapes(
        base_circle,
        LayeredShapes(
            ScaledShape(base_circle, 0.75, 0.75),
            polygon
        ),
        LayeredShapes(
            ScaledShape(base_circle, 0.5, 0.5),
            RotatedShape(triangle, 180)
        )
    )

    shape = HorizontalShapes(
        rectangle,
        spacer,
        square,
        vertical_shapes,
        square,
        spacer,
        rectangle
    )

    def test_get_width(self):
        self.assertEqual(self.shape._get_width(), 600)

    def test_get_height(self):
        self.assertEqual(self.shape._get_height(), 360)
