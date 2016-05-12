devbup - how's the faith-based backup strategy working out for you?
===================================================================
`devbup` (short for "device backup") accepts files (perhaps, block devices or
large datasets), signs them, and creates a tarball, which is then compressed,
encrypted, and split.

Usage
-----
```
$ devbup /dev/sda $HOME/Documents/dataset.tar
```
Copy `sda` and `dataset.tar` to working directory, verify checksums, tarball
them, and be on our way.

Environment variables
=====================
```
$ NAME=music devbup ~/Music/*
```
Override default naming scheme (`$(date +%s%z).devbup`). This will create split
files with prefix `music`, like `musicaa`, `musicab`, etc.

```
$ DD_COMMAND=dcfldd devbup /dev/sdb
```
Use another command instead of `dd`. `devbup` will use the default `dd` syntax
with `if` and `of`. If `DD_COMMAND` equals to `dcfldd`, `devbup` will add a
`statusinterval` option to monitor progress.

```
$ DCFLDD_STATINT=32 DD_COMMAND=dcfldd devbup /dev/sdb
```
Override default `statusinterval` for `dcfldd`.

```
$ CKSUM_COMMAND=md5sum devbup /dev/sdb
```
Override default (`sha512sum`) checksum command. Useful with large files, when
SHA512 is too slow.

```
$ IGNORE_CKSUMS=1 devbup /dev/sdb # I aint gonna unmount that
```
Ignore mismatched checksums on source and result files, don't exit, continue
as if nothing went wrong.

```
$ ADD_PADDING=1 devbup ~/Documents/SizeSensitiveDocuments/*
```
Add a randomized binary file to the archive.

```
$ PADDING_SIZE=8141M ADD_PADDING=1 devbup ~/Documents/SizeSensitiveDocuments/*
```
Override default padding file size (which is `$(( RANDOM % 4096 ))M`,
i.e. from 0 to 4 GB).

```
$ RUN_MAT=1 devbup ~/Torrents/SomePiratedMovie.mkv
```
If installed, run MAT (Metadata anonymization toolkit) on the target tarball.

```
$ GPG=gpg2 devbup /dev/sdb
```
Override default (`gpg`) GnuPG command.

```
$ SIGN_KEY="dr.no@acme.io" devbup ~/Documents/Sensitive/*
```
Sign every input file with specified GnuPG key.

```
$ DIGEST_ALGO=SHA512 SIGN_KEY="dr.no@acme.io" devbup ~/Documents/VerySensitive/*
```
Override default GnuPG digest algorithm when signing.

```
$ ENCRYPT_KEY="dr.no@acme.io" devbup ~/Documents/MostSensitive/*
```
Encrypt the resulting tarball with specified GnuPG key.

```
$ HIDE_RECIPIENT=1 ENCRYPT_KEY="dr.no@acme.io" devbup ~/Documents/MostestSensitivest/*
```
Use `--hidden-recipient` so that the key user-id is not transmitted

```
$ SPLIT_SIZE=512M devbup ~/Stuff/GonnaBackupOverStableConnection
```
Override default (`256M`) split size.
