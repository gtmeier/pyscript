from . import Shape, Point


class HorizontalShapes(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        shape_exports = []
        current_x = center.x - self._get_width() / 2
        for shape in self._shapes:
            half_shape_width = shape._get_width() / 2
            current_x += half_shape_width
            shape_exports.append(
                shape._get_postscript(Point(current_x, center.y))
            )
            current_x += half_shape_width
        return "\n".join(shape_exports)

    def _get_width(self):
        return sum(shape._get_width() for shape in self._shapes)

    def _get_height(self):
        # TODO
        pass
