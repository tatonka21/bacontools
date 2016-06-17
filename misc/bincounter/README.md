bincounter - an impeccable tally with no purpose
================================================
`bincounter` tallies individual bits in all input bytes.

```
$ printf 'Hello world!' | xxd
00000000: 4865 6c6c 6f20 776f 726c 6421            Hello world!
$ printf 'Hello world!' | bincounter
0 10 11 2 6 8 4 5
$ printf 'ABC' | xxd
00000000: 4142 43                                  ABC
$ printf 'ABC' | bincounter
0 3 0 0 0 0 2 2
```
