apdiff (all paths' diff) - return the different part of the file path
=====================================================================

Find and print the contiguous differing subsequence among similarly named files
in the same subdirectory.

```
$ for i in $(seq 1 100) ; do touch somelog.$i.log ; done
$ apdiff somelog.40.log
40
```
