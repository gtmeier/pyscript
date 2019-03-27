from . import Shape


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def export_postscript(self, center):
        return self._join_lines(
            "newpath",
            f"{center.x} {center.y} moveto",
            f"{self._width} 0 rlineto",
            f"0 {self._height} rlineto",
            f"{-self._width} 0 rlineto",
            "closepath",
            "stroke"
        )

    def width(self):
        return self._width
