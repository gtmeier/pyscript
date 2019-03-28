from . import Shape


class RotatedShape(Shape):

    def __init__(self, shape, rotation_angle):
        self._shape = shape
        # TODO Enforce rotation angle value 90, 180, 270
        self._rotation_angle = rotation_angle

    def _get_postscript(self, center):
        shape_postscript = self._shape._get_postscript(center)

        return self._join_lines(
            f"100 100 translate ",
            f"{self._rotation_angle} "
            "rotate",
            f"{shape_postscript}")

    def width(self):
        pass

    def height(self):
        pass
