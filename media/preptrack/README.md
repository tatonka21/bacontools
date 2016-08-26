preptrack - please wake up, Matthew, we miss you
================================================
Recodes an audio file with custom ID3V2 tags, removing all garbage metadata.

Usage
-----
```
$ preptrack ~/Downloads/never_gonna_give_you_up.mp3 ~/Downloads/sad_song.avi
```

`preptrack` accepts one or more file paths, prompts the user for artist, album,
title, and bitrate values, re-encodes these files, removes all metadata, and
saves them to a directory of your choice (`$DIR` if specified, `$HOME/Music`
otherwise), applying specified ID3V2 tags.

If MAT (Metadata anonymization toolkit) is present, `preptrack` will run `mat
newfile` after conversion and before applying new ID3 tags, unless `$DONT_MAT`
is set to anything.

If `$V1` environment variable is set to anything, `preptrack` will tell `eyeD3`
to write IDv1 metatags.

Use cases
---------
+ Normalize your music library for publishing: `preptrack` renames files like
  `~/Downloads/03_darren_korb_-_spike_in_a_rail.mp3` to
  `~/Music/Darren Korb - Spike In A Rail.mp3`.
+ Hide your download sources: `preptrack` will remove all metadata including
  ID3 comments, effectively recreating the original track.

Features
--------
+ As an `ffmpeg` frontend, accepts all kinds of media, including videos.
  `preptrack` will read the first audio stream available.
+ Reads ID3 tags and bitrate (if available) of the source file, and fills in
  these values as default when prompting.

Requirements
------------
+ Bash (any version with the `read` built-in that allows default values)
+ file
+ mat (optional)
+ rev
+ cut
+ sed
+ grep
+ ffmpeg
+ ffprobe
+ eyeD3
