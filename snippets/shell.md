General shell snippets
======================

Files
-----
`find . -exec grep -n hello /dev/null {} \; 2>/dev/null`

Find all files containing hello, print file names and line numbers.

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

Mount a FAT filesystem without having to use root.

***

`sudo netstat -tulpn`

List active Internet connections with server processes only.
