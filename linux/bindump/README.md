bindump - to vivisect is not the same as to comprehend
======================================================
`bindump` encodes input data to a binary dump of individual bytes.

```
$ echo Hello world! | bindump
01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111
01110010 01101100 01100100 00100001
```

Specifying the `-d` option will instruct `bindump` to decode the data from the
binary dump instead.

```
$ echo Hello world! | bindump | bindump -d
Hello world!
```

Specifying the `COLUMNS` environment variable will override the default (8)
number of bytes per line.

```
$ echo Hello world! | env COLUMNS=3 bindump
01001000 01100101 01101100
01101100 01101111 00100000
01110111 01101111 01110010
01101100 01100100 00100001
```
