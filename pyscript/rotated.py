from . import Shape, Point


# TODO: tests for export_postscript


class RotatedShape(Shape):

    def __init__(self, shape, rotation_angle):
        if rotation_angle not in (90, 180, 270):
            raise ValueError()

        self._shape = shape
        self._rotation_angle = rotation_angle

        if self._rotation_angle in (90, 270):
            self._width = self._shape._height
            self._height = self._shape._width
        else:
            assert self._rotation_angle == 180
            self._width = self._shape._width
            self._height = self._shape._height

    def _get_postscript(self, center):
        shape_postscript = self._shape._get_postscript(Point(0, 0))
        return self._join_lines(
            "gsave",
            f"{center.x} {center.y} translate ",
            f"{self._rotation_angle} rotate\n",
            f"{shape_postscript}",
            "grestore"
        )

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height
