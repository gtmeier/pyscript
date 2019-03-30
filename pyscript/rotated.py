from . import Shape, Point


# TODO: tests


class RotatedShape(Shape):

    def __init__(self, shape, rotation_angle):
        self._shape = shape
        # TODO Enforce rotation angle value 90, 180, 270
        # TODO or ask if we can allow arbitrary rotation angle
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
