imgur - download Imgur albums
=============================

Aptly named `imgur` downloads pics from an Imgur gallery album to a
subdirectory.

Usage
-----

```
$ imgur http://imgur.com/gallery/IVYHl
```

Save one or several albums to the working directory, to subdirectories namedi
like `IVYHl - Long time lurker wallpaper dump (+3500!)`.


```
$ imgur -d ~/Pictures/Wallpapers/SomeImgurWallpaperDump
```

Specifying `-d`/`--dir` will override the default destination directory. Files
from all specified albums will be saved there, so it's probably not a good idea
to use `-d` with multiple albums. Note that when `-d` is specified, `imgur`
won't create a subdirectory for images: in the example above, they'll go
straight to `SomeImgurWallpaperDump`.
