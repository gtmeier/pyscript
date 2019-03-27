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


def export_postscript(shape, center=Point(0, 0), filename="shape.ps"):
    postscript_code = shape.export_postscript(center) + "\nshowpage\n"

    # TODO temp comment
    # write string to file -- "context manager" takes care of opening and
    # closing
    with open(filename, "w+") as output_file:
        output_file.write(postscript_code)
