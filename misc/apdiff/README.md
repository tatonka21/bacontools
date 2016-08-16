apdiff (all paths' diff) - all paths lead to inevitable demise
==============================================================
Find and print the longest contiguous differing subsequence among similarly
named files in the same subdirectory.

```
$ for i in $(seq 1 100) ; do touch somelog.$i.log ; done
$ apdiff somelog.40.log
40
```

Specify an integer for the `MAX_NEIGHBORS` environment variable to limit number
of similar paths from which the subsequence is extracted. Default value is
`1000`.

Specify a real number in the [0, 1] interval for the `CUTOFF` environment
variable to filter paths by similarity. 1 means paths must be absolutely equal
(no diff will be printed), 0 means paths may be completely different (whole
paths may be printed).

Specify a Unix-style filename glob for the `GLOB` environment variable to limit
file paths picked for diffing. For instance, you may want to specify
`GLOB='*.log'` for the example above if files with different extensions exist
in that directory.
