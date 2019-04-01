from . import Polygon


class Square(Polygon):

    def __init__(self, sideLength):
        super().__init__(4, sideLength)

    def _get_width(self):
        assert round(super()._get_width()) == self._side_length
        return self._side_length

    def _get_height(self):
        assert round(super()._get_height()) == self._side_length
        return self._side_length
