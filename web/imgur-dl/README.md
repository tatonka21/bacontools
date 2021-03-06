imgur-dl - surely these wallpapers will help with your existential crises
=========================================================================
Aptly named `imgur-dl` downloads pics from an Imgur gallery album to a
subdirectory.

Usage
-----
```
$ imgur-dl http://imgur.com/gallery/IVYHl
```
Save one or several albums to the working directory, to subdirectories named
like `IVYHl - Long time lurker wallpaper dump (+3500!)`.

```
$ imgur-dl -d ~/Pictures/Wallpapers/SomeImgurWallpaperDump
```
Specifying `-d`/`--dir` will override the default destination directory. Files
from all specified albums will be saved there, so it's probably not a good idea
to use `-d` with multiple albums. Note that when `-d` is specified, `imgur-dl`
won't create a subdirectory for images: in the example above, they'll go
straight to `SomeImgurWallpaperDump`.

```
$ imgur-dl --unique
```
Specifying `-u`/`--unique` will make `imgur-dl` remove duplicate images (by
URL) from each album. If there are several albums to be downloaded, duplicate
images across albums are _not_ removed.

```
$ env TIMEOUT=120 imgur-dl
```
Override default resource timeout of `60` seconds.
