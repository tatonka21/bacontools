cate - for when their minds are too small to comprehend ed, the standard text editor
=====================================================================================
`cate` is a solution to edit files via cat and stdin whenever you feel like
`ed` or `ex` are overly complicated for the task at hand.
```
$ cat test.txt
cat: test.txt: No such file or directory
$ cate test.txt
Hello world!
^D
$ cat test.txt
Hello world!
$ cate
Enter filename:
test.txt
Hello again, world!
^D
$ cat test.txt
Hello again, world!
```
