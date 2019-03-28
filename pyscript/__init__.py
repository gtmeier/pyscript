from .point import Point
from .shape import Shape
from .circle import Circle
from .rectangle import Rectangle
from .horizontal import HorizontalShapes


# TODO check correct when done with project
# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL


def export_postscript(
        shape, center=Point(0, 0), show_center=False, filename="shape.ps"):
    postscript_code = shape._get_postscript(center) + "\n"

    if show_center:
        postscript_code += _show_center(center) + "\n"

    postscript_code += "showpage\n"

    # TODO temp comment
    # write string to file -- "context manager" takes care of opening and
    # closing
    with open(filename, "w+") as output_file:
        output_file.write(postscript_code)


def _show_center(center):
    return "\n".join((
        "% Show center for debugging purposes.",
        "newpath",
        f"{center.x} {center.y} 2 0 360 arc",
        "fill"
    )) + "\n"
