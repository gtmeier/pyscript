from . import Shape, Point


class HorizontalShape(Shape):

    def __init__(self, *shapes):
        self._shapes = shapes

    def export_postscript(self, center):
        shape_exports = []
        current_x = center.x - self.width() / 2
        for shape in self._shapes:
            half_shape_width = shape.width() / 2
            current_x += half_shape_width
            shape_exports.append(
                shape.export_postscript(Point(current_x, center.y))
            )
            current_x += half_shape_width
        return "\n".join(shape_exports)

    def width(self):
        return sum(shape.width() for shape in self._shapes)
