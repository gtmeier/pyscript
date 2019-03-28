from . import Polygon
import math

class Triangle(Polygon):

    def __init__(self, sideLength):
        self._sideLength = sideLength
        self._numSides = 3
        self.determineHW()
        
    def _get_postscript(self, center):
        totalAngle = (self._numSides - 2) * 180                  # formula for interior angles 
        interiorAngle = str(180 - (totalAngle / self._numSides))
        sidesMinusOne = str(self._numSides - 1)

        translateX = str(self._sideLength / -2)
        translateY = str(self.getHeight() / -2)
        
        test = str(self.getHeight())
        
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
            
            
            
            
            
            
