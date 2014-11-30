# ImageValidator

ImageValidator is a .NET utility which performs a batch analysis of raster images and detects corrupted ones.

### Flags

```sh
>ImageValidator
```
Check all image files in current directory, print corrupted image files to the standard output, don't do anything else.

```sh
>ImageValidator --help
>ImageValidator -?
```
Print help.

```sh
>ImageValidator -r
>ImageValidator --recursive
```
Search in all subfolders.

```sh
>ImageValidator -d "C:\My pics"
>ImageValidator --dir "C:\My pics"
```
Search in a specified directory, not the working one.

```sh
>ImageValidator -a
>ImageValidator --all-files
```
Don't ignore files with non-image extensions.

```sh
>ImageValidator -l "badimgs.txt"
>ImageValidator --log "badimgs.txt"
```
Write the corrupted image list to the specified file.

```sh
>ImageValidator -v
>ImageValidator --verbose
```
Print the specific exception that causes the image to be discarded. Doesn't really tell much, so don't even bother.

```sh
>ImageValidator --mute
```
Don't announce the progress.

```sh
>ImageValidator -m "/badfiles/"
>ImageValidator --move-to "/badfiles/"
```
Move all corrupted images to the specified folder. Can't use with neither --copy-to nor --delete.

```sh
>ImageValidator -c "/badfiles/"
>ImageValidator --copy-to "/badfiles/"
```
Copy all corrupted images to the specified folder. Can't use with neither --move-to nor --delete.

```sh
>ImageValidator --delete
```
Delete all corrupted images. Can't use with neither --move-to nor --copy-to.

```sh
>ImageValidator --progress-step 100
```
Define how frequently will progress be announced. Default is 100.

```sh
>ImageValidator --retain-folders
```
Copy/move files preserving their path structure in respect to the working directory.
