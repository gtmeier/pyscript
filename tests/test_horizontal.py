from pyscript import HorizontalShapes, Circle, Rectangle, Point

from shape_test_case import ShapeTestCase


class HorizontalShapesTestCase(ShapeTestCase):

    def test_get_width_no_shapes(self):
        horizontal_shapes = HorizontalShapes()
        self.assertEqual(horizontal_shapes._get_width(), 0)

    def test_get_width_single_shape(self):
        horizontal_shapes = HorizontalShapes(Circle(3))
        self.assertEqual(horizontal_shapes._get_width(), 6)

    def test_get_width_multiple_shapes(self):
        horizontal_shapes = HorizontalShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shapes._get_width(), 2 + 5 + 42 + 0 + 3)

    def test_export_postscript_circles_half_off_page(self):
        self._test_export_postscript(
            HorizontalShapes(
                Circle(10),
                Circle(20),
                Circle(30),
                Circle(20),
                Circle(10)
            ),
            Point(0, 30)
        )

    def test_export_postscript_circles_on_page(self):
        self._test_export_postscript(
            HorizontalShapes(
                Circle(10),
                Circle(20),
                Circle(30),
                Circle(20),
                Circle(10)
            ),
            Point(90, 30)
        )

    def test_export_postscript_circles_and_rectangles(self):
        self._test_export_postscript(
            HorizontalShapes(
                Circle(10),
                Rectangle(20, 20),
                Circle(20),
                Rectangle(40, 40),
                Circle(30),
                Rectangle(120, 60),
                Circle(20),
                Rectangle(80, 40),
                Circle(10),
                Rectangle(40, 20),
                Rectangle(20, 40)
            ),
            Point(300, 200)
        )
