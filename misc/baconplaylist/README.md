baconplaylist - screams of the damned in various genres
=======================================================
`baconplaylist` is a personal tool to query my playlist log, which I keep in a
specific format as follows:

```
ISO-8601 Artist – Track name
```

(That's not an ASCII hyphen, that's Unicode EN DASH in UTF-8, E2:80:93,
copy-pasted from Telegram).

Therefore, the playlist looks something like that:

```
2016-02-29 Alias Conrad Coldwood – Unreasonable Behaviour
2016-02-29 Hiroyuki Sawano – Naming Sense 0-gata Itsutsuboshi Gokuseifuku

2016-03-01 ABBA – Money, Money, Money
2016-03-01 Gorillaz – Pirate Jet
2016-03-01 Eddy Louiss, Michel Petrucciani – Summertime
2016-03-01 Joe Satriani – Premonition
2016-03-01 John Williams – Theme from Jurassic Park
2016-03-01 [Shingeki no Kyojin OP] Linked Horizon – Guren no Yumiya ~TV size~
2016-03-01 Ken Ashcorp – Dunkmaster Yi
```

For readability, tracks posted on different days are separated with an empty
line.

`baconplaylist` queries the total number of audio tracks, the total number of
unique artists, and the total number of artists with only one track in the
playlist. Any arguments passed to `baconplaylist` are considered arguments to
`grep` which accepts the playlist file.
