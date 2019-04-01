from . import Polygon


class Triangle(Polygon):

    def __init__(self, sideLength):
        super().__init__(3, sideLength)
