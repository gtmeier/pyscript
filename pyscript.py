# pyscript.py
# Laura Lundell
# Jake Herrmann
# George Meier
# CS372 Python to PostScript

# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL

from abc import ABC, abstractmethod

class Shape(ABC):

	@abstractmethod
	def export_postscript(self):
		pass


class Circle(Shape):

	def __init__(self, radius):
		self._radius = radius

	def export_postscript(self):
		# TODO showpage here for testing purposes
		return "newpath \n0 0 " + str(self._radius) + " 0 360 arc stroke \nshowpage"

class Rectangle(Shape):
	def __init__(self, width, height):
		self._width		= width
		self._height	= height

	def export_postscript(self):
		#todo refactor
		return ("newpath 0 0 moveto\n"
				+ str(self._width) + " 0 lineto\n"
				+ str(self._width) + " " + str(self._height) + " lineto\n"
				+ "0 "+ str(self._height)+ " lineto\n"
				+ "closepath\n"
				+ "stroke\n"
				+ "showpage\n")




def export_postscript(shape, filename):
	postscript_code = shape.export_postscript()
	# append showpage to string

	# write string to file -- "context manager" takes care of opening and closing
	with open(filename, "w+") as output_file:
		output_file.write(postscript_code)




# if name is main, code is executed, otherwise its'being imported as module
if __name__ == "__main__":
	# circle = Circle(40)
	# export_postscript(circle, "test_circle.ps")
	rectangle=Rectangle(40,80)
	export_postscript(rectangle, "test_rectangle.ps")
