from . import Shape, Point


# TODO: tests for export_postscript


class RotatedShape(Shape):

    def __init__(self, shape, rotation_angle):
        if rotation_angle not in (90, 180, 270):
            raise ValueError()
        self._shape = shape
        self._rotation_angle = rotation_angle

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
        pass

    def _get_height(self):
        pass
