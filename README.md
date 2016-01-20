termdraw - ASCII/Unicode art data visualizer
--------------------------------------------

`termdraw` is a utility written in Python 3 that draws CSV data of form `x,y`
as text graphs.

` $ termdraw data.csv`

Assume data.csv contains a list of (x,y) points, graph those points, print the
result to stdout.

` $ echo "1,2 2,3 3,4;4,5" | termdraw -`

Read standard input and graph x,y points. Data received via stdin must have the
following format: `x,y[%Sx,y...]`, where %S is a separator (a single space or
semicolon).

` $ termdraw data.csv --width=50 -h 20`

Draw graph limited to the width of 50 characters and height of 20 lines.

` $ termdraw data.csv -a`

Only use ASCII symbols in output.

` $ termdraw data.csv -s`

Draw a solid graph (fills values at or below the points).

` $ termdraw data.csv -p`

Draw a point graph (does not fill below the values). This flag is on by
default.

` $ termdraw data.csv -si`

Draw a solid graph with linear interpolation between points.

` $ termdraw --help`

Print a help message.
