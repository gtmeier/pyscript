from . import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def _get_postscript(self, center):
        return self._join_lines(
            "newpath",

            f"{center.x - self.width() / 2} "
            f"{center.y - self.height() / 2} moveto",

            f"{self.width()} 0 rlineto",
            f"0 {self.height()} rlineto",
            f"{-self.width()} 0 rlineto",
            "closepath",
            "stroke"
        )

    def width(self):
        return self._width

    def height(self):
        return self._height
