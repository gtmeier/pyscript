Pyscript -- a python to postscript interpreter

CS372 Project 2
George Meier
Jake Herrmann
Laura Lundell


For documentation on how to call the Pyscript functions please see the unit tests.


**********Background and project description**********
PostScript is a programming language designed primarily for describing the layout of printed pages.

In this project, our group implemented a python3 library that we called Pyscript, short for "python to PostScript." Pyscript allows its user to specify drawings at a high level of abstraction, and output the drawings as PostScript. Pyscript consists of:

1. A shape language that allows basic shapes such as squares, circles, and polygons to be defined, rotated and scaled versions, and aggregate shapes, for example a vertical "stack".

2. A shapes-to-PostScript translator that takes as input a drawing specified using Pyscript's shape language and produces a PostScript file from it.


**********Reflections***********
What worked:
1. Separating each shape into its own file let us work in parellel.
2. Use of git helped with error tracing.
3. Everyone synced their editors (4 spaces per tab, etc..) so there were no issues sharing code.
4. Constant refactoring kept the project readable and maintainable
5. The group had excellent communication.

What didn't work:
1. Reading the project assignemnt and understanding it before stating. George wrote polygon but wasn't able to explain it which lead to confusiion and wasted time trying to fix the problem of centering odd numbered shapes which wasn't actually a problem.
2. Drawing a single shape was easy to implement but made drawing difficult. This is a problem that needs to be addressed at a later time.







 







































