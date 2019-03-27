#!/usr/bin/env python3

# TODO: delete this script when it's no longer needed


# This is a temporary script for manual testing. Edit the main code below to
# test new shapes.


# Import everything from the pyscript module. (This is bad practice, so flake8
# will complain.)
from pyscript import *


if __name__ == "__main__":
    # shape = Circle(40)
    shape = Rectangle(40, 80)

    # Export the shape centered at the default center point:
    # export_postscript(shape)

    # Export the shape, centered at the given point, and show the center point:
    export_postscript(shape, center=Point(100, 100), show_center=True)
