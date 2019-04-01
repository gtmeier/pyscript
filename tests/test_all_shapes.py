from pyscript import (
    Point, Rectangle, Spacer, Square, Circle, HorizontalShapes, VerticalShapes,
    LayeredShapes, ScaledShape, RotatedShape, Triangle, Polygon
)

from shape_test_case import ShapeTestCase


class AllShapesTestCase(ShapeTestCase):

    _base_circle = Circle(80)
    _rectangle = Rectangle(100, 60)
    _spacer = Spacer(40, 40)
    _square = Square(80)
    _vertical_shapes = VerticalShapes(
        _base_circle,
        LayeredShapes(
            ScaledShape(_base_circle, 0.75, 0.75), Polygon(5, 20)
        ),
        LayeredShapes(
            ScaledShape(_base_circle, 0.5, 0.5),
            RotatedShape(Triangle(20), 180)
        )
    )
    _shape = HorizontalShapes(
        _rectangle,
        _spacer,
        _square,
        _vertical_shapes,
        _square,
        _spacer,
        _rectangle
    )

    def test_get_width(self):
        self.assertEqual(self._shape._get_width(), 600)

    def test_get_height(self):
        self.assertEqual(self._shape._get_height(), 360)

    def test_export_postscript_all_shapes(self):
        self._test_export_postscript(self._shape, Point(305, 300))
