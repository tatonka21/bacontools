readable - and yet nobody seems to understand
=============================================
`readable` filters `stdin`, discarding human-unreadable input. The algorithm
demands improvement, but does, roughly, leave ASCII letter words and discard
garbled symbols.

```
$ readable --help
bacontools readable v1
Usage: strings some_file | readable [options...]
Filter out unreadable (garbage) lines.

COMMAND LINE OPTIONS:
 -h, --help                   Print this help text.
 -c, --cutoff                 Set the minimum readability value (default 0.5).
```
