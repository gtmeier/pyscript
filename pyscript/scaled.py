from . import Shape, Point


# TODO: tests


class ScaledShape(Shape):

    def __init__(self, shape, scale_factor_x, scale_factor_y):
        self._shape = shape
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

    def _get_postscript(self, center):
        shape_postscript = self._shape._get_postscript(Point(0, 0))
        return self._join_lines(
            "gsave",
            f"{center.x} {center.y} translate ",
            f"{self._scale_factor_x} {self._scale_factor_y} scale\n",
            f"{shape_postscript}",
            "grestore"
        )

    def _get_width(self):
        pass
        # return self._shape._get_width() * self._scale_factor_x

    def _get_height(self):
        pass
        # return self._shape._get_height() * self._scale_factor_y
