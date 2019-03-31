# Pyscript

CS 372 Spring 2019\
Software Construction

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
type of shape, but we have also added a test (TODO: link to file) that
incorporates every type of shape into one large composite shape.

We chose this strategy because it would have been very difficult and
error-prone to manually create PostScript representations of all the shapes
before actually implementing the `_get_postscript` method for each shape. In
the process of implementing `_get_postscript`, our understanding of the problem
changed and we learned more about PostScript and graphical manipulation of
shapes in general. So we are glad we waited to start writing tests until after
we were fairly confident in the quality of our design and implementation.