from . import Polygon


# TODO: tests for _get_width, _get_height, export_postscript


class Triangle(Polygon):

    def __init__(self, sideLength):
        super().__init__(3, sideLength)
