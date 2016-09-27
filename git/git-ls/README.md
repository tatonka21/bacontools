git-ls - you can't read them all
================================
Print a Github-like human-readable Git repo directory listing.

```
$ git ls
web            24 hours ago   3259fc2 Makefiles: require 'all' by 'install'              Ilya Terentyev
maturity.txt   18 hours ago   d418408 add git-repo-list                                  Ilya Terentyev
patches        10 days ago    b096393 refactor patches/apply                             Ilya Terentyev
LICENSE        3 months ago   2ad4a81 limit LICENSE width to 79 instead of 80            Ilya Terentyev
media          7 minutes ago  7a159ba togif: add manpage                                 Ilya Terentyev
TOOLS.md       18 hours ago   d418408 add git-repo-list                                  Ilya Terentyev
CHANGELOG.md   7 minutes ago  7a159ba togif: add manpage                                 Ilya Terentyev
Makefile       2 days ago     bf29c43 Makefile: refactor targets                         Ilya Terentyev
.gitignore     6 weeks ago    eebf256 add .gitignore                                     Ilya Terentyev
.mailmap       3 months ago   4e32e37 add .mailmap                                       Ilya Terentyev
snippets       4 days ago     7a8b961 snippets/shell.md: add parallel batch snippet      Ilya Terentyev
misc           18 hours ago   c455c98 bitcount: display true bits / all bits ratio       Ilya Terentyev
text           24 hours ago   3259fc2 Makefiles: require 'all' by 'install'              Ilya Terentyev
.travis.yml    2 weeks ago    0cc51a1 travis, gitlab-ci: minor apt-get syntax fixes      Ilya Terentyev
linux          34 minutes ago 9955810 devrestore: fix minor errors in manpage formatting Ilya Terentyev
.gitlab-ci.yml 2 weeks ago    0cc51a1 travis, gitlab-ci: minor apt-get syntax fixes      Ilya Terentyev
CHECKLIST.md   13 days ago    77b95aa CHECKLIST: add a CHANGELOG entry                   Ilya Terentyev
README.md      18 hours ago   d418408 add git-repo-list                                  Ilya Terentyev
```
Print current directory listing.

```
$ git ls ~/Sources/git-fire
git-fire  9 months ago  6fa092b Prevent word splitting Dennis Meckel
README.md 9 months ago  7284b9c Update README.md       Nimit Kalra
LICENSE   10 months ago dbcffbf Initial commit         Nimit Kalra
```
Print arbitrary directory listing.

```
$ git ls ~/Sources/linux/Makefile ~/Sources/linux/README
Makefile 10 days ago  a99cde4 Linux 4.7-rc6                      Linus Torvalds
README   3 months ago cfaf790 README: remove trailing whitespace Jonathan Corbet
```
Print arbitrary file listing.

```
$ git ls --noalign ~/Sources/linux
```
Do not align each field with spaces.
