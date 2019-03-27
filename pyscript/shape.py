from abc import ABC, abstractmethod


class Shape(ABC):

    # TODO: check method signature is consistent w/ all subclasses
    @abstractmethod
    def export_postscript(self, center):
        pass

    @abstractmethod
    def width(self):
        pass

    @staticmethod
    def _join_lines(*lines):
        return "\n".join(lines) + "\n"
