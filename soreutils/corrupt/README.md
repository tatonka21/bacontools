soreutils/corrupt - feels good, doesn't it?
===========================================

```
% corrupt --help
Usage: cat file1 | corrupt drop --ratio 0.01 >> file2
Corrupt data by flipping random bits or dropping random bytes.

Actions (required first argument):
  drop       Remove random bytes
  flip       Flip random bits
Options:
  --ratio f  Real number between 0 and 1 (exclusive); equals ratio of elements (bits or bytes) affected
  --help     Print this text
```
