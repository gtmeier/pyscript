from . import Triangle, RotatedShape, Point


# http://jwilson.coe.uga.edu/emat6680/parsons/mvp6690/essay1/sierpinski.html


def sierpinski_triangle(side_len, center, recursion_depth):
    outer_triangle = Triangle(side_len)
    outer_base_y = center.y - outer_triangle._get_height() / 2

    inner_triangle_side_len = side_len / 2
    inner_triangle_center_y = (
        outer_base_y + Triangle(inner_triangle_side_len)._get_height() / 2
    )
    inner_triangle_center = Point(center.x, inner_triangle_center_y)

    inner_triangles = _inverted_triangle_pattern(
        inner_triangle_side_len, inner_triangle_center, recursion_depth
    )

    _export_multiple_shapes(
        (outer_triangle, center), *inner_triangles, filename="sierpinski.ps"
    )


def _inverted_triangle_pattern(side_len, center, recursion_depth):
    assert recursion_depth >= 0

    triangle = RotatedShape(Triangle(side_len), 180)

    if recursion_depth == 0:
        return ((triangle, center), )

    small_triangle_side_len = side_len / 2
    small_triangle_height = Triangle(small_triangle_side_len)._get_height()

    def pattern(center):
        return _inverted_triangle_pattern(
            small_triangle_side_len, center, recursion_depth - 1
        )

    upper_pattern_center = Point(
        center.x, center.y + 1.5 * small_triangle_height
    )
    left_pattern_center = Point(
        center.x - side_len / 2, center.y - small_triangle_height / 2
    )
    right_pattern_center = Point(
        center.x + side_len / 2, left_pattern_center.y
    )

    upper_pattern = pattern(upper_pattern_center)
    left_pattern = pattern(left_pattern_center)
    right_pattern = pattern(right_pattern_center)

    return ((triangle, center), *upper_pattern, *left_pattern, *right_pattern)


def _export_multiple_shapes(*shape_center_pairs, filename="shapes.ps"):
    code = "\n".join(
        shape._get_postscript(center) for shape, center in shape_center_pairs
    )
    with open(filename, "w+") as output_file:
        output_file.write(code)
