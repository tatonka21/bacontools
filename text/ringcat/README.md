ringcat - circular feline enveloping a whole world
==================================================
`ringcat` appends standard input text to a file, truncating the beginning of
the file so it stays the same length in lines.

```
$ cat stdinfile
6
7
$ cat ringfile
1
2
3
4
5
$ cat stdinfile | ringcat ringfile
$ cat ringfile
3
4
5
6
7
```
