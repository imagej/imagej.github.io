This page documents the language used in the PointSet Demo plugin.

The PointSet demo program shows off the power of TextSpecifiedPointSets that are part of the Imglib2 OPS subproject.

The dialog shows a text field that can be used to specify complex sets of points. The resulting points are displayed as a two color image with white denoting points in the set and black denoting points outside the set.

The syntax for a text specified PointSet is as one or more axis ranges optionally followed by equations that specify additional constraints. Each term is separated by comma values.

The axis syntax follows Haskell's list comprehension syntax. You can specify an axis name and its associated single value (i.e. "x = [10]"). Or multiple values (i.e. "x=[10,20,30]"). Or a range of values (i.e. "x = [1..25]"). Or even a range of values by a defined step size (i.e. "x = [1,3..15]" which equals [1,3,5,7,9,11,13,15]).

The constraint equations use much of the same syntax as outlined here: http://wiki.imagej.net/ImageJ2/Documentation/Process/Math/Equation

Some examples:

X ranges from 1 to 10, y ranges from 5 to 15:
"x=[1..10], y=[5..15]"

Same set of points but further constrained such that x plus y is less than 20:
"x=[1..10], y=[5..15], x + y < 20"

A circular area centered at 50,50:
"x=[1..100], y=[1..100], (x-50)^2 + (y-50)^2 <= 400"

Multiple axes can be defined as well as any number of constraints as long as they are separated by commas. All constraints are applied simultaneously (in an AND fashion). And any function that is defined by the equation language (hyperlinked earlier) can be used in the specification of the constraint.
