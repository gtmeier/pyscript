from . import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def _get_postscript(self, center):
        return self._join_lines(
            "newpath",

            f"{center.x - self._get_width() / 2} "
            f"{center.y - self._get_height() / 2} moveto",

            f"{self._get_width()} 0 rlineto",
            f"0 {self._get_height()} rlineto",
            f"{-self._get_width()} 0 rlineto",
            "closepath",
            "stroke"
        )

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height
