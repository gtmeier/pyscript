# PyScript

CS 372 Spring 2019\
Software Construction\
George Meier\
Jake Herrmann\
Laura Lundell

## Introduction

PostScript is a programming language designed primarily for describing the
layout of printed pages. We implemented a Python library called PyScript, short
for "Python to PostScript." PyScript allows users to specify drawings at a high
level of abstraction and output the drawings as PostScript.

## Shape grammar

This is the grammar for the shape language. Lowercase words are nonterminals
and uppercase words are terminals. The grammar corresponds fairly closely to
the actual `Shape` class hierarchy, except that there are no separate base
classes for basic and compound shapes (for example, both `Rectangle` and
`LayeredShapes` inherit directly from `Shape`).

```
shape    = basic | compound
basic    = polygon | RECTANGLE | SPACER | CIRCLE
polygon  = POLYGON | SQUARE | TRIANGLE
compound = ROTATED | SCALED | LAYERED | VERTICAL | HORIZONTAL
```

## Getting started

Make sure you have Python >=3.6 by running `python3 --version`.

If you have `pip` and `setuptools` installed, you can run `pip3 install .
--user` from the project's root directory in order to install `pyscript` as a
Python package.

Otherwise, any Python source files that use `pyscript` will need to be located
in the project's root directory so that Python can find the `pyscript/`
directory.

## Usage

To create and export a shape, simply construct the shape and call its
`export_postscript` method:

```python
from pyscript import Circle, Point

circle = Circle(50)
circle.export_postscript(center=Point(100, 100), filename="circle.ps")
```

See the script [`weird-snowperson.py`](weird-snowperson.py) for an example that
incorporates every single type of shape. Run it with `./weird-snowperson.py`.

See [`pyscript/__init__.py`](pyscript/__init__.py) for a complete list of
public classes and functions.

## Fractals

We decided to use PyScript to implement fractals. So far, we have only
implemented Sierpinski's Triangle. Run it with `./sierpinski.py`.

The resulting `sierpinski.ps` PostScript file is several thousand lines long
because the recursion is implemented in Python and the PostScript for each
component triangle is simply combined into one enormous file. In order to
reduce the filesize for higher recursion depths, we should actually generate
PostScript code to handle the recursion.

## Tests

Run the tests with `./run-tests`. Tests should always be run from the project's
root directory.

In addition to unit tests for `Shape` methods such as `_get_width` and
`_get_height`, we also implemented tests for exporting `Shape` objects to
PostScript.

For each type of shape, rather than practice pure TDD, our strategy has been to
first implement the `_get_postscript` method, inspect the generated PostScript
code for formatting and readability, and inspect the result of rendering the
PostScript using an external tool (such as `ghostscript`).

Then, for each type of shape, we save examples of known-good PostScript code
and write tests to create and export shapes and then compare the results with
the saved PostScript files in order to make sure the output is still exactly
the same. We are still in the process of adding these tests for every single
type of shape, but we have also added [a test case that incorporates every type
of shape into one large composite shape](tests/test_all_shapes.py).

We chose this strategy because it would have been very difficult and
error-prone to manually create PostScript representations of all the shapes
before actually implementing the `_get_postscript` method for each shape. In
the process of implementing `_get_postscript`, our understanding of the problem
changed and we learned more about PostScript and graphical manipulation of
shapes in general. So we are glad we waited to start writing tests until after
we were fairly confident in the quality of our design and implementation.

## Critique of the shape language

Our main criticism is of using `VerticalShapes`, `HorizontalShapes`, and
`Spacer` for positioning other shapes. This has proven to be quite limiting.
For example, Jake's first attempt to implement Sierpinski's Triangle used this
method, until he realized it wouldn't be feasible to implement arbitrary
recursion depth without explicitly specifying each component shape's center
point. It seems much more flexible and convenient to construct a drawing by
simply creating any number of shapes centered at arbitrary points.

Of course, there's nothing about the language that prevents us from
implementing this method of creating drawings. It's just that we expected the
default abstractions to be more powerful than they turned out to be.

## Other reflection

What worked:

- The group had excellent communication.
- Constant refactoring kept the project readable and maintainable.
- Creating a separate source file for each shape allowed us to work in
  parallel.
- Git allowed us to track down when and where bugs were introduced.

What didn't work:

- We wrote `Polygon` correctly but later spent a few hours attempting to center
  odd-sided polygons about the given center point, before realizing that we had
  already met the requirement of centering the bounding box. We should have
  more carefully read and understood the assignment description before
  implementing `Polygon`.
