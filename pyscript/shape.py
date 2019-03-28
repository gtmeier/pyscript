from abc import ABC, abstractmethod

from . import Point


class Shape(ABC):

    def export_postscript(
            self, center=Point(0, 0), show_center=False, filename="shape.ps"):
        postscript_code = self._get_postscript(center) + "\n"

        if show_center:
            postscript_code += self._show_center(center) + "\n"

        postscript_code += "showpage\n"

        # TODO temp comment
        # write string to file -- "context manager" takes care of opening and
        # closing
        with open(filename, "w+") as output_file:
            output_file.write(postscript_code)

    @abstractmethod
    def width(self):
        pass

    @abstractmethod
    def height(self):
        pass

    # TODO: check method signature is consistent w/ all subclasses
    @abstractmethod
    def _get_postscript(self, center):
        pass

    def _show_center(self, center):
        return "\n".join((
            "% Show center for debugging purposes.",
            "newpath",
            f"{center.x} {center.y} 2 0 360 arc",
            "fill"
        )) + "\n"

    @staticmethod
    def _join_lines(*lines):
        return "\n".join(lines) + "\n"
