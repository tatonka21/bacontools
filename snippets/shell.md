General shell snippets
======================

Files
-----
`find . -exec grep -n hello /dev/null {} \; 2>/dev/null`

Find all files containing hello, print file names and line numbers.

***

`env LC_COLLATE=C ls -lAXh --group-directories-first --color=auto "$@"`

Pretty portable and intuitive `ls` in columns.

***

VCS
---
`find -maxdepth 1 -mindepth 1 -type d -print0 |\
xargs -0 -I'{}' -- sh -c 'cd "{}" ; figlet "$(basename "$(pwd)")" ; git pull'`

Recurse in all level 1 subfolders, print directory name with `figlet`, and run
`git pull`.

***

System
------
`sudo mount /dev/sdb1 $MEDIA/sdb1 -o user,rw,auto,nofail,umask=111,dmask=000,flush`

Mount a FAT filesystem so that current user could use it without sudo.

***

```
#/etc/cron.d/oom_disable
*/1 * * * * root pgrep -f "/usr/sbin/sshd" | while read PID; do echo -17 > /proc/$PID/oom_adj;
done
```

Disable OOM killer for `sshd`.

***

`sudo netstat -tulpn`

List active Internet connections with server processes only.

Media
-----
`env FRAMES=40 PIXELS=40000 DELAY=25 togif VIDEO PREFIX`

Convert a video file to bacongifdiary format.

***

`env FRAMESETS="${FRAMESETS-"467 470 473 475 477 480 485 490"}" parallel -j2 bash -c 'FRAMES=$3 togif "$1" "$2"' funcname VIDEO PREFIX -- $FRAMESETS`

Create several candidates for a `/r/fullmoviegifs` post.

***

```
#!/bin/sh

FRAMESETS="${FRAMESETS-"467 470 473 475 477 480 485 490"}"

for f in $FRAMESETS; do
       FRAMES=$f togif "$1" "$2"
done
```

Same, but more boring and not in parallel.
