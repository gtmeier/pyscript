from . import Shape
import math

class Polygon(Shape):

    def __init__(self, numSides, sideLength):
        self._numSides = numSides
        self._sideLength = sideLength
        
    _width = 0
    _height = 0
        
    def numSides(self):
        return self._numSides

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
        
        
    def determine(self):
        if self._numSides % 2 != 0 :
            setHeight(sideLength*(1+math.cos(math.pi/numSides))/(2*math.sin(math.pi/numSides)))
            setWidth((sideLength*math.sin(math.pi*(numSides-1)/(2*numSides)))/(math.sin(math.pi/numSides)))
        elif self._numSides % 4 == 0 :
            setHeight(sideLength*(math.cos(math.pi/numSides))/(math.sin(math.pi/numSides)))
            setWidth((sideLength*math.sin(math.pi/numSides))/(math.sin(math.pi/numSides)))
        else:
            setHeight(sideLength*(math.cos(math.pi/numSides))/(math.sin(math.pi/numSides)))
            setWidth(sideLength/(math.sin(math.pi/numSides)))
	
        
    def _get_postscript(self, center):
        totalAngle = (self._numSides - 2) * 180                  # formula for interior angles 
        interiorAngle = str(180 - (totalAngle / self._numSides))
        sidesMinusOne = str(self._numSides - 1)

        translateX = str(self._sideLength / -2)
        translateY = str(self.getHeight() / -2)
        
        return self._join_lines(
            "newpath",
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
            
            
        # TODO fix centering. centered horizontal but not vertical
            
            
            
            
            
