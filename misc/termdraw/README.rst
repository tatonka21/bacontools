termdraw - drawing with own's blood doesn't make it prettier
============================================================

`termdraw` is a utility written in Python 3 that draws CSV data of form `x,y`
as text graphs.

Usage examples
==============

.. sourcecode:: bash

    $ cat data.csv
    0,41.492605310851346
    1,-61.90512769272529
    2,-5.705460535578624
    3,-45.40738693881286
    4,48.57733683988141
    5,-11.09276051450491
    6,-48.857646527799886
    7,20.02380594874974
    8,3.8265498423428568
    9,-4.993006692763217
    0,17.534954337402368
    1,-12.048399887989433
    2,-67.66449062064824
    3,33.3847844218531
    4,36.73010900554392
    5,62.315666298226745
    6,-59.496317272986865
    7,74.93745996536751
    8,-7.867224323068683
    9,51.88925397139964
    $ termdraw data.csv
                          •
                    •
                •                •
    •        •  •
    •                     •
                             •
       •  •         •        •   •

             •         •
       •  •            •


Assume data.csv contains a list of (x,y) points, graph those points, print the
result to stdout.

.. sourcecode:: bash

    $ termdraw data.csv --width=10 -h 5
           •
    •   ••   •
    •  ••  ••
     ••  •  ••
     •••  •

Draw graphs with dimensions of 10 characters' width and height of 5 lines.

.. sourcecode:: bash

    $ echo "1,2 2,3 3,4;4,5" | termdraw -
                                 •


                       •


             •


    •

Read standard input and graph x,y points. Data received via stdin must have the
following format: `x,y[%Sx,y...]`, where %S is a separator (any number of
whitespace characters or semicolons).

.. sourcecode:: bash

    $ echo "1,2 2,3 3,4 4,5" | termdraw - -a
                                 o


                       o


             o


    o

Only use ASCII symbols in output.

.. sourcecode:: bash

    $ echo 1 2 3 4 5 | termdraw -a -
                                 o


                         o

                  o

           o

    o

If singular values are given, assume that Y values are given and X values are
spread evenly.

.. sourcecode:: bash

    $ echo 1 2 3 4 5 | termdraw -a -
                                 o


                         o

                  o

           o

    o

If singular values are given, assume that Y values are given and X values are
spread evenly.

.. sourcecode:: bash

    $ termdraw data.csv -s

                    ▁     █
                ▂   █     █      ▄
    ▇        ▃  █   █     █      █
    █        █  █   █     █      █
    █        █  █   █     █  ▄   █
    █  ▄  ▇  █  █   █     █  █   █
    █  █  █  █  █   █     █  █   █
    █  █  █  █  █   █  ▁  █  █   █
    █  █  █  █  █   █  █  █  █   █

Draw a solid graph (fills values at or below the points).

.. sourcecode:: bash

    $ termdraw data.csv -si

                    ▁     █
                ▂▄▆▇█     █▄     ▄
    ▇        ▃▅██████    ▃██    ▆█
    █▆      ▄████████▆   ████ ▂███
    ██▅    ▅██████████   ████▄████
    ███▄▅▆▇███████████▄ ▆█████████
    ███████████████████ ██████████
    ███████████████████▁██████████
    ██████████████████████████████

Draw a graph with linear interpolation between points.

.. sourcecode:: bash

    $ termdraw data.csv --print-paths
    data.csv
                          •
                    •
                •                •
    •        •  •
    •                     •
                             •
       •  •         •        •   •

             •         •
       •  •            •

Print file paths on a separate line before printing their graphs.

.. sourcecode:: bash

    $ termdraw --help
    Usage: termdraw.py [options] file.csv
    Draw a human-friendly CLI graph with Unicode symbols.

      --help                   Print this help message and exit
      -w X, --width X          Limit graph width to X characters
      -h Y, --height Y         Limit graph height to Y lines
      -i, --interpolate        Enable interpolation
      -n, --no-interpolate     Disable interpolation
      -s, --solid              Draw solid graph (with columns)
      -p, --point              Draw point graph (with points)
      -a, --ascii              Only use ASCII symbols
      -o file, --output file   Write to file instead of stdout
      --print-paths            Print file names before graphs

Print a help message.
