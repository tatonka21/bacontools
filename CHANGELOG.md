bacontools change log
=====================
Notable changes to `bacontools` are documented in this file.

***

Unreleased
----------
### Added
+ `togif`: manpage
+ `git-repo-list`
+ `wget-page`
+ `stopwatch`
+ `readable`: manpage
+ `vimless`: `-N` option for less; line numbers are now not printed by default

### Changed
+ `checkreboot`: don't print "reboot-required.pkgs" prompt
+ `bitcount`: display true bits / all bits ratio
+ `vimless`: loop over each file argument
+ `baconplaylist`: ignore case in artist names
+ `baconplaylist`: display top N artists
+ `git-ls`: separate cols with 1 space instead of 2
+ `vimless`: exit if $# = 0 and stdin is a tty
+ `myzuka`: print output except filenames to stderr
+ `togif`: use `set -e` to check for failing commands

### Fixed
+ `git-ls`: verify that argument paths exist
+ `git-ls`: list subdirectories and files correctly

***

[2016.07.05]
------------
### Added
+ `curl-tt`
+ `bincounter`: total bytes and normalized bit counts
+ `morseconv`
+ `baconplaylist`
+ `vimless`
+ `CHECKLIST.md`
+ `togif`: implement `$QUIET` and `$NOSTATS`
+ `snippets/shell.md`

### Changed
+ `bincounter` -> `bitcount`

***

[2016.06.29]
------------
### Added
+ `single-urxvt`

### Changed
+ `netinfo`: deduce active interface via `ip link`
+ `devbup`: prefer `dcfldd` if it's installed

### Fixed
+ `netinfo`: check if nmcli is installed
+ `preptrack`: check if files exist

***

[2016.06.17]
------------
### Added
+ `myzuka-dl`: handle `DIR` environment variable
+ `du1`
+ `respcode`
+ `ringcat`
+ `bincounter`
+ `preptrack`: notify-send notification
+ `maturity.txt`
+ `devrestore`

### Changed
+ Makefile: run `patches/apply` on install
+ `devbup`: move up from Untested to Moving

### Fixed
+ `togif`, `preptrack`: fix `$(command ...)` invocations
+ `imgur-dl`: downgrade to commit dfd26dc
+ `devbup`: fix no shredding bug
+ `imgur-dl`, `myzuka-dl`: eschew Bundler on Raspbian with a patch
+ `togif`: check if dependencies are installed
+ `devbup`: run MAT on each file before tarballing

***

[2016.05]
---------
### Added
+ `httpdf`
+ `TOOLS.md`
+ `preptrack`: handle embedded pictures
+ `myzuka-dl`: `-n`/`--index` option
+ `myzuka-dl`: Gemfile
+ `imgur-dl`: Gemfile
+ `preptrack`: man page
+ Tool maturity classification
+ `git-ls`: support arbitrary paths
+ `patches` directory, `no-haskell` patch
+ `userls`
+ `myzuka`: `-d`/`--dir` option
+ `readable`
+ `imgur`: support non-album gallery posts
+ `tasktags`
+ `devbup`
+ `bananaglee`
+ `togif`
+ `termdraw` v0.2 dev branch
+ `trimline`
+ `ruler`
+ Multiple indices in `myzuka`.
+ `lines`

### Changed
+ `imgur-dl`, `myzuka-dl`: print prompts to stderr
+ `preptrack`: silence unnecessary output
+ `gitlab-ci`: run `patches/apply` in `make`
+ `imgur-dl`: don't print "Scrolling down" anymore
+ Rename `myzuka` to `myzuka-dl`
+ Rename `imgur` to `imgur-dl`
+ `myzuka`: tabulate result list
+ `preptrack`: run MAT on converted files
+ Convert NOTES to CHANGELOG
+ Move text-related tools to `text/`.

### Fixed
+ `imgur-dl`: fix title substitution
+ `myzuka`, `imgur`: don't escape slashes in paths
+ `myzuka`: fix fatal error in search prompt
+ `togif`: check for unset variables

***

[2016.04]
---------
### Added
+ `imgur`
+ `myzuka`
+ `EncodingConverter`
+ `ImageValidator`
+ `pip-upgrade-all`
+ `termdraw v0.1`
+ `git-ls`
+ `apdiff`
+ `netinfo`
+ `checkreboot`
+ `vidinfo`
+ `update-all`
+ soreutils: `balance`, `bitdiff`, `byteat`, `corrupt`, `maybe`, `n7m`
+ `preptrack`

[2016.04]: https://gitlab.com/bacondropped/bacontools/tags/2016.04
[2016.05]: https://gitlab.com/bacondropped/bacontools/tags/2016.05
[2016.06.17]: https://gitlab.com/bacondropped/bacontools/tags/2016-06-17
[2016.06.29]: https://github.com/bacondropped/bacontools/releases/tag/2016.06.29
[2016.07.05]: https://github.com/bacondropped/bacontools/releases/tag/2016.07.05
