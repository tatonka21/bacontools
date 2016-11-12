ffmpeg-togif - so many ways to convert, so little time
======================================================
`ffmpeg-togif` is an alternative to `togif`. It is less configurable, but is
`ffmpeg`-only as opposed to `togif` which uses `ffmpeg` and `convert`, and it
has a ballin' progress bar. Plus, it uses ffmpeg's `palettegen`/`paletteuse`
filters for high quality GIFs.

```
$ ffmpeg-togif video.mp4 video.gif
Calculating palette...
[############--------------------------] Converting...
```
Convert video to GIF.
