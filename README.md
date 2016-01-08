termdraw - ASCII/Unicode art data visualizer
--------------------------------------------

`termdraw` is a utility written in Python 3 that draws CSV data of form `x,y`
as text graphs.

` $ termdraw data.csv`

Assume data.csv contains a list of (x,y) points, graph those points, print the
result to stdout.

` $ termdraw data.csv -a`

Only use ASCII symbols in output.

` $ termdraw data.csv -s`

Draw a solid graph (fills values at or below the points).

` $ termdraw data.csv -p`


` $ termdraw data.csv -si`

Draw a solid graph with linear interpolation between points.

` $ termdraw -h`

Print a help message.
