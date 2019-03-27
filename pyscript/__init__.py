from collections import namedtuple

from .shape import Shape
from .circle import Circle
from .rectangle import Rectangle


Point = namedtuple("Point", ("x", "y"))


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


# TODO remove main when done with project

# FIXME
# if name is main, code is executed, otherwise its'being imported as module
# if __name__ == "__main__":
#     shape = Circle(40)
#     # shape = Rectangle(40, 80)
#     # export_postscript(shape)
#     export_postscript(shape, Point(100, 100))
