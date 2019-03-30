from . import Shape


class LayeredShapes(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        return "\n".join(
            shape._get_postscript(center) for shape in self._shapes
        )

    def _get_width(self):
        return max((shape._get_width() for shape in self._shapes), default=0)

    def _get_height(self):
        return max((shape._get_height() for shape in self._shapes), default=0)
