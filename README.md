# ImageValidator

ImageValidator is a .NET utility which performs a batch analysis of raster images and detects corrupted ones.

### Flags

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
Print the specific exception that causes the image to be discarded.

```sh
>ImageValidator --mute
```
Don't announce the progress.

```sh
>ImageValidator -m "/badfiles/"
>ImageValidator --move-to "/badfiles/"
```
Move all corrupted images to the specified folder. Mutually exclusive with --copy-to and --delete.

```sh
>ImageValidator -c "/badfiles/"
>ImageValidator --copy-to "/badfiles/"
```
Copy all corrupted images to the specified folder. Mutually exclusive with --move-to and --delete.

```sh
>ImageValidator --delete
```
Delete all corrupted images. Mutually exclusive with --move-to and --copy-to.

```sh
>ImageValidator --progress-step 100
```
Define how frequently will progress be announced.

```sh
>ImageValidator --retain-folders
```
Copy/move files preserving their path structure in respect to the working directory.