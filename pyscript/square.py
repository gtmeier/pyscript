from . import Polygon


# TODO: tests for _get_width, _get_height, export_postscript


class Square(Polygon):

    def __init__(self, sideLength):
        super().__init__(4, sideLength)

    def _get_width(self):
        assert round(super()._get_width()) == self._side_length
        return self._side_length

    def _get_height(self):
        assert round(super()._get_height()) == self._side_length
        return self._side_length
