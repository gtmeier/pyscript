from . import Polygon


class Square(Polygon):

    def __init__(self, sideLength):
        super().__init__(4, sideLength)
