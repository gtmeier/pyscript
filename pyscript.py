# pyscript.py
# Laura Lundell
# Jake Herrmann
# George Meier
# CS372 Python to PostScript


from abc import ABC, abstractmethod


# TODO check correct when done with project
# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL


class Shape(ABC):

    @abstractmethod
    def export_postscript(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self._radius = radius

    def export_postscript(self):
        # TODO refactor, DRY showpage
        return ("newpath\n"
                + f"0 0 {self._radius} 0 360 arc stroke\n"
                + "showpage")


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def export_postscript(self):
        # TODO refactor, DRY showpage
        return ("newpath 0 0 moveto\n"
                + f"{self._width} 0 lineto\n"
                + f"{self._width} {self._height} lineto\n"
                + f"0 {self._height} lineto\n"
                + "closepath\n"
                + "stroke\n"
                + "showpage\n")


def export_postscript(shape, filename):
    postscript_code = shape.export_postscript()
    # TODO append showpage

    # TODO temp comment
    # write string to file -- "context manager" takes care of opening and
    # closing
    with open(filename, "w+") as output_file:
        output_file.write(postscript_code)


# TODO remove main when done with project

# if name is main, code is executed, otherwise its'being imported as module
if __name__ == "__main__":
    # circle = Circle(40)
    # export_postscript(circle, "test_circle.ps")
    rectangle = Rectangle(40, 80)
    export_postscript(rectangle, "test_rectangle.ps")
