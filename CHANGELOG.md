bacontools change log
=====================
Notable changes to `bacontools` are documented in this file.

***

Unreleased
----------
### Added
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
+ `imgur-dl`, `myzuka-dl`: eschew Bundler on Raspbian with a patch
+ `togif`: check if dependencies are installed
+ `devbup`: run MAT on each file before tarballing

***

[2016.05] - 2016-05-28
----------------------
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

[2016.04] - 2016-05-01
----------------------
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
