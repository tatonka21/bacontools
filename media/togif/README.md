togif - faces frozen in timeless agony
======================================
`togif` is a shell script that converts a video file to an animated gif with
given number of frames.

```
$ togif ~/Downloads/Movie.mp4 Movie
```
Convert Movie.mp4 to Movie475.gif with 475 frames sampled evenly from
Movie.mp4, downscaled so that the number of pixels in every frame is roughly
100k, multithreaded as much as possible.

```
$ FRAMES=1000 PIXELS=200000 THREADS=1 togif ~/Downloads/Movie.mp4 Movie
```
Convert Movie.mp4 to Movie1000.gif with 1000 frames, scaled to 200k pixels
without multithreading.

```
$ QUIET=1 FRAMES=1000 THREADS=4 togif ~/Downloads/Movie.mkv Movie
```
`$QUIET` supresses any output by the script, `$NOSTATS` makes `ffmpeg` use the
`-nostats` flag.
