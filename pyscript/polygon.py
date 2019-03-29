from . import Shape
import math


class Polygon(Shape):

    def __init__(self, num_sides, side_length):
        self._num_sides = num_sides
        self._side_length = side_length
        self._calculate_height_width()

    def _set_width(self, width):
        self._width = width

    def _set_height(self, height):
        self._height = height

    def width(self):
        return self._width

    def height(self):
        return self._height

    def _calculate_height_width(self):
        if self._num_sides % 2 != 0:
            self._set_height(
                self._side_length
                * (1 + math.cos(math.pi / self._num_sides))
                / (2 * math.sin(math.pi / self._num_sides))
            )
            self._set_width(
                (self._side_length
                 * math.sin(math.pi
                            * (self._num_sides - 1) / (2 * self._num_sides)))
                / (math.sin(math.pi / self._num_sides))
            )
        elif self._num_sides % 4 == 0:
            self._set_height(
                self._side_length
                * (math.cos(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
            self._set_width(
                (self._side_length * math.sin(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
        else:
            self._set_height(
                self._side_length
                * (math.cos(math.pi / self._num_sides))
                / (math.sin(math.pi / self._num_sides))
            )
            self._set_width(self._side_length
                            / (math.sin(math.pi / self._num_sides)))

    def _get_postscript(self, center):
        totalAngle = (self._num_sides - 2) * 180  # formula for interior angles
        interiorAngle = str(180 - (totalAngle / self._num_sides))
        sidesMinusOne = str(self._num_sides - 1)

        translateX = str(self._side_length / -2)
        translateY = str(self.height() / -2)

        return self._join_lines(
            "gsave ",
            translateX + " " + translateY + " translate newpath ",
            f"{center.x} {center.y} moveto ",
            "1 1 " + sidesMinusOne + " { ",
            str(self._side_length) + " 0 rlineto ",
            interiorAngle + " rotate ",
            "} for ",
            "closepath",
            "stroke",
            "grestore "
            )
