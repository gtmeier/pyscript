#!/usr/bin/env python3


from pyscript import sierpinski_triangle_pages, write_postscript, Point


if __name__ == "__main__":
    write_postscript(
        sierpinski_triangle_pages(400, Point(250, 350), 7), "sierpinski.ps"
    )
