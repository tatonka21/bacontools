webdf - free space is scarce; the walls are caving in; I can't breathe
======================================================================
`webdf` is a simple Go webserver that listens to a port (`3000` by default),
and returns the amount of free space on the filesystem the working directory is
located in.

```
$ pwd
/home/user
$ webdf -port 2500 &
$ curl localhost:2500
21474836480
$ killall webdf
```
The filesystem `/home/user` is located on has 20GiB of free space.
