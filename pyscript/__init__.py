from .point      import Point
from .shape      import Shape
from .circle     import Circle
from .rectangle  import Rectangle
from .vertical   import VerticalShapes
from .horizontal import HorizontalShapes
from .spacer     import Spacer
from .polygon    import Polygon
from .square     import Square
from .triangle   import Triangle
from .scaled     import ScaledShape
from .rotated    import RotatedShape
from .layered    import LayeredShapes

# TODO check correct when done with project
# shape     = basic | compound
# basic     = polygon | RECTANGLE | SPACER | CIRCLE
# polygon   = POLYGON | SQUARE | TRIANGLE
# compound  = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL


def export_multiple_shapes(*shape_center_pairs, filename="shapes.ps"):
    code = "\n".join(
        shape._get_postscript(center) for shape, center in shape_center_pairs
    )
    with open(filename, "w+") as output_file:
        output_file.write(code)
