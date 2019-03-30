from . import Shape


# TODO: maybe subclass from Rectangle
# TODO: tests


class Spacer(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def _get_postscript(self, center):
        return self._join_lines(
            f"% spacer centered at ({center.x}, {center.y})"
        )

    def width(self):
        return self._width

    def height(self):
        return self._height
