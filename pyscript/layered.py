from . import Shape, Point

class LayeredShapes(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def _get_postscript(self, center):
        shape_exports = []
        current_x = center.x
        for shape in self._shapes:
            shape_exports.append(
                shape._get_postscript(Point(current_x, center.y))
            )
        return "\n".join(shape_exports)

    def width(self):
        return sum(shape.width() for shape in self._shapes)
















