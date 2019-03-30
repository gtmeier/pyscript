from . import Shape, Point


# TODO: tests


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
        # TODO
        pass

    # TODO: tests
    def _get_height(self):
        return sum(shape._get_height() for shape in self._shapes)
