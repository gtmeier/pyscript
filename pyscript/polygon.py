from . import Shape
import math


class Polygon(Shape):

    def __init__(self, numSides, sideLength):
        self._numSides = numSides
        self._sideLength = sideLength
        self.determineHW()

    def sideLength(self):
        return self._sideLength

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def determineHW(self):
        if self._numSides % 2 != 0:
            self.setHeight(
                self._sideLength
                * (1 + math.cos(math.pi / self._numSides))
                / (2 * math.sin(math.pi / self._numSides))
            )
            self.setWidth(
                (self._sideLength
                 * math.sin(math.pi
                            * (self._numSides - 1) / (2 * self._numSides)))
                / (math.sin(math.pi / self._numSides))
            )
        elif self._numSides % 4 == 0:
            self.setHeight(
                self._sideLength
                * (math.cos(math.pi / self._numSides))
                / (math.sin(math.pi / self._numSides))
            )
            self.setWidth(
                (self._sideLength * math.sin(math.pi / self._numSides))
                / (math.sin(math.pi / self._numSides))
            )
        else:
            self.setHeight(
                self._sideLength
                * (math.cos(math.pi / self._numSides))
                / (math.sin(math.pi / self._numSides))
            )
            self.setWidth(self._sideLength/(math.sin(math.pi/self._numSides)))

    def _get_postscript(self, center):
        totalAngle = (self._numSides - 2) * 180  # formula for interior angles
        interiorAngle = str(180 - (totalAngle / self._numSides))
        sidesMinusOne = str(self._numSides - 1)

        translateX = str(self._sideLength / -2)
        translateY = str(self.getHeight() / -2)

        return self._join_lines(
            "gsave ",
            translateX + " " + translateY + " translate newpath ",
            f"{center.x} {center.y} moveto ",
            "1 1 " + sidesMinusOne + " { ",
            str(self._sideLength) + " 0 rlineto ",
            interiorAngle + " rotate ",
            "} for ",
            "closepath",
            "stroke",
            "grestore "
            )
