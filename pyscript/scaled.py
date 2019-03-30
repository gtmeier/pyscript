from . import Shape


# TODO: tests


class ScaledShape(Shape):

    def __init__(self, shape, scale_factor_x, scale_factor_y):
        self._shape = shape
        self._scale_factor_x = scale_factor_x
        self._scale_factor_y = scale_factor_y

    def _get_postscript(self, center):
        shape_postscript = self._shape._get_postscript(center)

        # TODO: gsave and grestore
        return self._join_lines(
            f"{self._scale_factor_x} "
            f"{self._scale_factor_y} ",
            "scale",
            f"{shape_postscript}")

    def width(self):
        return self._shape.width() * self._scale_factor_x

    def height(self):
        return self._shape.width() * self._scale_factor_y
