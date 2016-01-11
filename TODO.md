termdraw v0.1 "to do" list
==========================

General
-------
+ Histogram graphs
+ Line graphs (ref: http://www.algorithm.co.il/blogs/ascii-plotter/)
+ Horizontal string-value graphs (ref:
  https://pypi.python.org/pypi/ascii_graph/0.2.1)
+ Stdin data consumption
+ Write to file option
+ Point graph interpolation support
+ Graph views
+ Graph view decorations
+ Tests
+ Parse DAT files in some simple readable format (e.g. space separated)
+ Inline point graph value labels
+ Inline line graph value labels

Documentation
-------------
+ Write docs/termdraw.3 for Python modules and their public functions

termdraw/termdraw.py
--------------------
+ Graph size command line switches
+ Module docstring
+ Move all init code to `__draw_graph`
+ Make `__draw_graph` function public
+ `draw_graph` docstring
+ Extract graph functions to `graph.py`
+ Non-binary interpolation support for `_interpolate_points`

termdraw/csv.py
---------------
+ Module docstring
+ `get_csv_data` docstring

termdraw/interpolate.py
-----------------------
+ Module docstring
+ `linear_interpolate` docstring
+ Square interpolation
+ Cosine interpolation
