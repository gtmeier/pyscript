from abc import ABC, abstractmethod


class Shape(ABC):

    # TODO: check method signature is consistent w/ all subclasses
    @abstractmethod
    def _get_postscript(self, center):
        pass

    # @abstractmethod  # TODO: uncomment
    def width(self):
        pass

    # @abstractmethod  # TODO: uncomment
    def height(self):
        pass

    @staticmethod
    def _join_lines(*lines):
        return "\n".join(lines) + "\n"
