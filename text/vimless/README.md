vimless - scarred facade of a century-old temple
================================================
`vimless` passes output of `vimcat` from the `vimpager` package to the `less`
pager.

```
$ cat hello.c
#include <stdio.h>

int main(int argc, char **argv) {
    printf("%s\n", "Hello world!");
    return 0;
};
$ vimless hello.c # You can't see the syntax coloring but it's here
1 #include <stdio.h>
2
3 int main(int argc, char **argv) {
4     printf("%s\n", "Hello world!");
5     return 0;
6 };
```
