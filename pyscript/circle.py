from . import Shape


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def _get_postscript(self, center):
        return self._join_lines(
            "newpath",
            f"{center.x} {center.y} {self._radius} 0 360 arc",
            "stroke"
        )

    def width(self):
        return self._radius * 2

    def height(self):
        return self.width()
