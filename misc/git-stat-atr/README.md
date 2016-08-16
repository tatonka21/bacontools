git-stat-atr - higher powers are indifferent to suffering
=========================================================
`git-stat-atr` ("Added to Total Ratio") sorts output of a `git diff --stat`
command by the ratio of added lines to total changed lines in each file.

```
$ git diff --stat 2016.07.27..HEAD --no-color
 CHANGELOG.md                | 15 +++++++++++++++
 PKGBUILD                    |  8 ++++----
 README.md                   |  4 ++--
 TOOLS.md                    |  1 +
 linux/devbup/README.md      |  3 ++-
 linux/devbup/devbup         | 16 ++++++++++++++--
 linux/devbup/devbup.1       |  2 ++
 linux/devrestore/devrestore | 26 +++++++++++++++++++-------
 maturity.txt                |  1 +
 misc/update-all/update-all  |  2 +-
 text/Makefile               |  1 +
 text/README.md              |  1 +
 text/center/Makefile        |  6 ++++++
 text/center/README.md       | 45 +++++++++++++++++++++++++++++++++++++++++++++
 text/center/center          |  2 ++
 15 files changed, 116 insertions(+), 17 deletions(-)
$ git-stat-atr 2016.07.27..HEAD --no-color
 misc/update-all/update-all  |  2 +-
 README.md                   |  4 ++--
 PKGBUILD                    |  8 ++++----
 linux/devbup/README.md      |  3 ++-
 linux/devrestore/devrestore | 26 +++++++++++++++++++-------
 linux/devbup/devbup         | 16 ++++++++++++++--
 TOOLS.md                    |  1 +
 text/README.md              |  1 +
 text/Makefile               |  1 +
 text/center/README.md       | 45 +++++++++++++++++++++++++++++++++++++++++++++
 text/center/Makefile        |  6 ++++++
 text/center/center          |  2 ++
 maturity.txt                |  1 +
 linux/devbup/devbup.1       |  2 ++
 CHANGELOG.md                | 15 +++++++++++++++
 15 files changed, 116 insertions(+), 17 deletions(-)
```
As you can see, the second command puts refactored files on top and augmented
files on bottom.
