# pyscript.py
# Laura Lundell
# Jake Herrmann
# George Meier
# CS372 Python to PostScript


from abc import ABC, abstractmethod
from collections import namedtuple


Point = namedtuple("Point", ("x", "y"))


# TODO check correct when done with project
# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL


class Shape(ABC):

    # TODO: check method signature is consistent w/ all subclasses
    @abstractmethod
    def export_postscript(self, center):
        pass

    @abstractmethod
    def width(self):
        pass

    @staticmethod
    def _join_lines(*lines):
        return "\n".join(lines) + "\n"


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def export_postscript(self, center):
        return self._join_lines(
            "newpath",
            f"{center.x} {center.y} {self._radius} 0 360 arc",
            "stroke"
        )

    def width(self):
        return self._radius * 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def export_postscript(self, center):
        return self._join_lines(
            "newpath",
            f"{center.x} {center.y} moveto",
            f"{self._width} 0 rlineto",
            f"0 {self._height} rlineto",
            f"{-self._width} 0 rlineto",
            "closepath",
            "stroke"
        )

    def width(self):
        return self._width


class HorizontalShape(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def export_postscript(self, center):
        shape_exports = []
        current_x = center.x - self.width() / 2
        for shape in self._shapes:
            half_shape_width = shape.width() / 2
            current_x += half_shape_width
            shape_exports.append(
                shape.export_postscript(Point(current_x, center.y))
            )
            current_x += half_shape_width
        return "\n".join(shape_exports)

    def width(self):
        return sum(shape.width() for shape in self._shapes)


def export_postscript(shape, center=Point(0, 0), filename="shape.ps"):
    postscript_code = shape.export_postscript(center) + "\nshowpage\n"

    # TODO temp comment
    # write string to file -- "context manager" takes care of opening and
    # closing
    with open(filename, "w+") as output_file:
        output_file.write(postscript_code)


# TODO remove main when done with project

# if name is main, code is executed, otherwise its'being imported as module
if __name__ == "__main__":
    shape = Circle(40)
    # shape = Rectangle(40, 80)
    # export_postscript(shape)
    export_postscript(shape, Point(100, 100))
