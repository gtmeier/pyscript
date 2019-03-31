from .point      import Point
from .shape      import Shape
from .circle     import Circle
from .rectangle  import Rectangle
from .spacer     import Spacer
from .polygon    import Polygon
from .square     import Square
from .triangle   import Triangle
from .scaled     import ScaledShape
from .rotated    import RotatedShape
from .layered    import LayeredShapes
from .vertical   import VerticalShapes
from .horizontal import HorizontalShapes

from .fractals   import sierpinski_triangle
from .fractals   import sierpinski_triangle_pages
from .fractals   import write_postscript

# TODO check correct when done with project
# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL
