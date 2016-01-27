termdraw v0.2 to-do list
========================

Docs
----
+ Migrate README to RST, use it at PyPi project page
+ Docstrings for view.py

Graphs
------
+ Horizontal string-value graphs (ref:
  https://pypi.python.org/pypi/ascii_graph/0.2.1)
+ Graph view decorations
+ Automatic equal step x value generation for data of form [(y), ...]

Bugs
----
+ If passed a file path that does not exist, termdraw throws an uncaught
  exception; catch it and display an error message
