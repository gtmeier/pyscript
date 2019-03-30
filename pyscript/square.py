from . import Polygon


# TODO: tests for _get_width and _get_height


class Square(Polygon):

    def __init__(self, sideLength):
        super().__init__(4, sideLength)
