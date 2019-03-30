from . import Polygon


# TODO: tests


class Triangle(Polygon):

    def __init__(self, sideLength):
        super().__init__(3, sideLength)
