#!/usr/bin/env python3

# Laura originally created this shape for use in an automated test, but it also
# serves as a nice demonstration of the pyscript module.

from pyscript import (
    Point, Rectangle, Spacer, Square, Circle, HorizontalShapes, VerticalShapes,
    LayeredShapes, ScaledShape, RotatedShape, Triangle, Polygon
)

if __name__ == "__main__":
    base_circle = Circle(80)
    rectangle = Rectangle(100, 60)
    spacer = Spacer(40, 40)
    square = Square(80)
    vertical_shapes = VerticalShapes(
        base_circle,
        LayeredShapes(
            ScaledShape(base_circle, 0.75, 0.75), Polygon(5, 20)
        ),
        LayeredShapes(
            ScaledShape(base_circle, 0.5, 0.5), RotatedShape(Triangle(20), 180)
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
    shape.export_postscript(
        center=Point(305, 300), filename="weird-snowperson.ps"
    )
