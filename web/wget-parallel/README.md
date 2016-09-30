wget-parallel - hundreds upon thousands of leeches siphoning blood from the web
===============================================================================
`wget-parallel` downloads argument URLs via wget, parallelized with GNU
parallel.
```
$ wget-parallel example.com/file1.bin example.com/file2.bin
```

Two environment variables are considered, `PARALLEL_ARGS` and `WGET_ARGS`.
These variables may contain options that will be passed to GNU parallel and
each invocation of wget, respectively. They will be expanded exactly once by
the shell, so, for instance, the following invocation will be valid:
```
$ env WGET_ARGS=--progress=bar PARALLEL_ARGS="-j2 -u" wget-parallel URL1 URL2
```

`wget-parallel` also reads URLs from stdin if it's not attached to a terminal.
```
$ cat url-list.txt | wget-parallel
```
