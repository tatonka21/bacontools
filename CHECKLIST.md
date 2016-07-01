New tool checklist
==================
The following steps must be taken before merging a new tool.

1. Add a tool subdirectory, containing a functional, installable
   implementation.
2. If required, add a build entry to the subdirectory `Makefile`.
3. Add an installation entry to the subdirectory `Makefile`.
4. Add a table entry to the subdirectory `README`.
5. Add a table entry to the top-level `TOOLS` file.
6. Add an entry to the top-level `maturity.txt` file.
7. Increment relevant tool category count and the total in the top-level
   `README`.
