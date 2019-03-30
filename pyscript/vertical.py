from . import Shape, Point


# TODO: tests for export_postscript


class VerticalShapes(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        shape_exports = []
        current_y = center.y - self._get_height() / 2
        for shape in self._shapes:
            half_shape_height = shape._get_height() / 2
            current_y += half_shape_height
            shape_exports.append(
                shape._get_postscript(Point(center.x, current_y))
            )
            current_y += half_shape_height
        return "\n".join(shape_exports)

    def _get_width(self):
        return max((shape._get_width() for shape in self._shapes), default=0)

    def _get_height(self):
        return sum(shape._get_height() for shape in self._shapes)
