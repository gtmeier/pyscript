from . import Shape


# TODO: maybe subclass from Rectangle


class Spacer(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def _get_postscript(self, center):
        return self._join_lines(
            f"% spacer centered at ({center.x}, {center.y})"
        )

    def _get_width(self):
        return self._width

    def _get_height(self):
        return self._height
