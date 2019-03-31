from math import sin, cos, pi

from . import Shape


# TODO: tests


class Polygon(Shape):

    def __init__(self, num_sides, side_length):
        self._num_sides = num_sides
        self._side_length = side_length
        self._set_width_height()

    def _set_width_height(self):
        if self._num_sides % 2 != 0:
            self._set_width_height_odd()
        elif self._num_sides % 4 == 0:
            self._set_width_height_divisible_by_4()
        else:
            assert self._num_sides % 2 == 0
            self._set_width_height_even()

    def _set_width_height_odd(self):
        n = self._num_sides
        self._width = (
            self._side_length * sin(pi * (n - 1) / (2 * n)) / sin(pi / n)
        )
        self._height = (
            self._side_length * (1 + cos(pi / n)) / (2 * sin(pi / n))
        )

    def _set_width_height_divisible_by_4(self):
        n = self._num_sides
        self._width = self._height = (
            self._side_length * cos(pi / n) / sin(pi / n)
        )

    def _set_width_height_even(self):
        n = self._num_sides
        self._width = self._side_length / sin(pi / n)
        self._height = self._side_length * cos(pi / n) / sin(pi / n)

    def _get_postscript(self, center):
        sum_interior_angles = (self._num_sides - 2) * 180
        interior_angle = sum_interior_angles / self._num_sides

        # Center bounding box.
        translate_x = - self._side_length / 2
        translate_y = - self._get_height() / 2

        return self._join_lines(
            "gsave",
            f"{translate_x} {translate_y} translate",
            "newpath",
            f"{center.x} {center.y} moveto",
            f"1 1 {self._num_sides - 1} " + "{",
            f"    {self._side_length} 0 rlineto",
            f"    {180 - interior_angle} rotate",
            "} for",
            "closepath",
            "stroke",
            "grestore"
        )

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height
