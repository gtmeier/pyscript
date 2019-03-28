import os

from pyscript import HorizontalShapes, Circle, Rectangle, Point

from shape_test_case import ShapeTestCase


class HorizontalShapesTestCase(ShapeTestCase):

    def test_width_no_shapes(self):
        horizontal_shapes = HorizontalShapes()
        self.assertEqual(horizontal_shapes.width(), 0)

    def test_width_single_shape(self):
        horizontal_shapes = HorizontalShapes(Circle(3))
        self.assertEqual(horizontal_shapes.width(), 6)

    def test_width_multiple_shapes(self):
        horizontal_shapes = HorizontalShapes(
            Circle(1),
            Rectangle(5, 10),
            Circle(21),
            Rectangle(0, 1),
            Rectangle(3, 9)
        )
        self.assertEqual(horizontal_shapes.width(), 2 + 5 + 42 + 0 + 3)

    # TODO: store known-good code in a file
    def test_get_postscript_circles_half_off_page(self):
        code = HorizontalShapes(
            Circle(10),
            Circle(20),
            Circle(30),
            Circle(20),
            Circle(10)
        )._get_postscript(Point(0, 30))
        self.assertEqual(
            code,
            "newpath\n"
            "-80.0 30 10 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "-50.0 30 20 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "0.0 30 30 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "50.0 30 20 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "80.0 30 10 0 360 arc\n"
            "stroke\n"
        )

    def test_get_postscript_circles_on_page(self):
        code = HorizontalShapes(
            Circle(10),
            Circle(20),
            Circle(30),
            Circle(20),
            Circle(10)
        )._get_postscript(Point(90, 30))
        self.assertEqual(
            code,
            "newpath\n"
            "10.0 30 10 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "40.0 30 20 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "90.0 30 30 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "140.0 30 20 0 360 arc\n"
            "stroke\n\n"

            "newpath\n"
            "170.0 30 10 0 360 arc\n"
            "stroke\n"
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

    def check_with_saved_code(self, test_code, save_file_name):
        with open(self.save_file_path(save_file_name), "r") as save_file:
            self.assertEqual(test_code, save_file.read())

    @staticmethod
    def save_file_path(save_file_name):
        return os.path.join("tests", "postscript-code", save_file_name)
