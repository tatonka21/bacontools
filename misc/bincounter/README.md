bincounter - an impeccable tally with no purpose
================================================
`bincounter` tallies individual bits in all input bytes.

```
$ printf 'Hello world!' | xxd
00000000: 4865 6c6c 6f20 776f 726c 6421            Hello world!
$ printf 'Hello world!' | bincounter
total: 46
dist: MSB 0 10 11 2 6 8 4 5 LSB
norm: MSB 0.000000 0.027174 0.029891 0.005435 0.016304 0.021739 0.010870 0.013587 LSB
$ printf 'ABC' | xxd
00000000: 4142 43                                  ABC
$ printf 'ABC' | bincounter
total: 7
dist: MSB 0 3 0 0 0 0 2 2 LSB
norm: MSB 0.000000 0.053571 0.000000 0.000000 0.000000 0.000000 0.035714 0.035714 LSB
```
