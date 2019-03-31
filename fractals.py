# TODO: clean up, refactor

from pyscript import (
    Circle,
    Triangle,
    LayeredShapes,
    RotatedShape,
    HorizontalShapes,
    VerticalShapes,
    Spacer,
    Point
)

# http://jwilson.coe.uga.edu/emat6680/parsons/mvp6690/essay1/sierpinski.html

# start w/ big triangle right-side up

# at same center, draw 180-degree rotated triangle w/ 1/2 the big triangle's
# side length

# draw three triangles, each 1/2 the smaller rotated triangle's side length,
# each also rotated 180 degrees

# top triangle's center: original center + smaller triangle's height

# left triangle's center: original center - smaller triangle's height - smaller
# triangle's width

# left triangle's center: original center - smaller triangle's height + smaller
# triangle's width


def concat(*shape_centers):
    code = '\n'.join(
        shape._get_postscript(center) for shape, center in shape_centers
    )
    with open('fractals.ps', 'w+') as f:
        f.write(code)


def inverted_triangle(side_len, center, rec):
    triangle = RotatedShape(Triangle(side_len), 180)

    if rec != 0:
        small = Triangle(side_len / 2)
        small1 = inverted_triangle(
            side_len / 2,
            Point(center.x, center.y + 1.5 * small._get_height()),
            rec - 1
        )

        small2 = inverted_triangle(
            side_len / 2,
            Point(center.x - side_len / 2, center.y - small._get_height() / 2),
            rec - 1
        )

        small3 = inverted_triangle(
            side_len / 2,
            Point(center.x + side_len / 2, center.y - small._get_height() / 2),
            rec - 1
        )

        return (
            (triangle, center),
            *small1,
            *small2,
            *small3
        )

    return ((triangle, center),)


if __name__ == '__main__':
    big_triangle = Triangle(200)
    big_triangle_center = Point(250, 250)
    big_base_y = big_triangle_center.y - big_triangle._get_height() / 2

    med_triangle = RotatedShape(Triangle(100), 180)
    med_triangle_center = Point(
        250, big_base_y + med_triangle._get_height() / 2
    )

    invt = inverted_triangle(100, med_triangle_center, 3)
    concat((big_triangle, big_triangle_center), *invt)

    # big_triangle = Triangle(200)
    # big_triangle_center = Point(250, 250)
    # big_base_y = big_triangle_center.y - big_triangle._get_height() / 2

    # med_triangle = RotatedShape(Triangle(100), 180)
    # med_triangle_center = Point(
    #     250, big_base_y + med_triangle._get_height() / 2
    # )

    # small = RotatedShape(Triangle(50), 180)
    # small_center1 = Point(
    #     250, med_triangle_center.y + 1.5 * small._get_height()
    # )

    # small_center2 = Point(
    #     250 - 50, med_triangle_center.y - small._get_height() / 2
    # )

    # small_center3 = Point(
    #     250 + 50, med_triangle_center.y - small._get_height() / 2
    # )

    # triangles = (
    #     (big_triangle, big_triangle_center),
    #     (med_triangle, med_triangle_center),
    #     (small, small_center1),
    #     (small, small_center2),
    #     (small, small_center3),
    # )
    # concat(*triangles)

    # fractal = LayeredShapes(
    #     Triangle(200),
    #     VerticalShapes(
    #         RotatedShape(Triangle(100), 180),
    #         Spacer(0, Triangle(100)._get_height())
    #     ),
    #     VerticalShapes(
    #         Spacer(0, Triangle(50)._get_height()),
    #         RotatedShape(Triangle(50), 180),
    #     ),
    #     VerticalShapes(
    #         HorizontalShapes(
    #             RotatedShape(Triangle(50), 180),
    #             Spacer(50 * 2, 0),
    #         ),
    #         Spacer(0, Triangle(150)._get_height()),
    #     ),
    #     VerticalShapes(
    #         HorizontalShapes(
    #             Spacer(50 * 2, 0),
    #             RotatedShape(Triangle(50), 180),
    #         ),
    #         Spacer(0, Triangle(150)._get_height()),
    #     ),

    #     VerticalShapes(
    #         Spacer(0, Triangle(125)._get_height()),
    #         RotatedShape(Triangle(25), 180),
    #     ),
    # )
    # fractal.export_postscript(
    #     center=Point(250, 250), show_center=True, filename='fractals.ps'
    # )
