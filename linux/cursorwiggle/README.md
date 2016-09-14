cursorwiggle - "I'm still alive, can't you see?"
================================================
`cursorwiggle` is an `xdotool` frontend for wiggling your mouse cursor a
predetermined number of times or repeatedly with delay. It is best illustrated
by the following xkcd strip:

![When designing an interface, imagine that your program is all that stands between the user and hot, sweaty, tangled-bedsheets-fingertips-digging-into-the-back sex.](https://imgs.xkcd.com/comics/command_line_fu.png)

Usage
-----
```
cursorwiggle [-v] [DELAY [COUNT]]
Wiggle the mouse cursor with xdotool.
```

Examples
--------
`cursorwiggle 10s`<br>
Wiggle the cursor repeatedly with 10 second delay.

`cursorwiggle -v`<br>
Wiggle the cursor vertically once, then exit.

`cursorwiggle 1m 5`<br>
Wiggle the cursor 5 times each minute.

Arguments
---------
+ `DELAY`: Time interval between mouse wiggles. Must be a valid time interval
  accepted by sleep(1). The default is 1m (1 minute). Does not do anything if
  `COUNT` equals to 1.
+ `COUNT`: Total number of mouse wiggles. If unset or '0', `cursorwiggle` will
   not stop wiggling the cursor unless interrupted. The default is 0 if `DELAY`
   is set as an argument, 1 otherwise.

Options
-------
+ `-v`: Wiggle the cursor vertically instead of horizontally.
+ `-d DELAY`: Equivalent to DELAY. Less preference than the DELAY argument.
+ `-c COUNT`: Ditto for COUNT.
+ `-h`: Print a small help text.

Environment
-----------
+ `DELAY`: Refer to the ARGUMENTS section. The environment variable has
  the least preference.
+ `COUNT`: Ditto for COUNT.
+ `VERTICAL`: Ditto for the `-v` option.
+ `MICROSLEEP`: Length of the sleep between each one-pixel movement of
  one wiggle. The default is 0.001 (seconds).
+ `WIGGLE_SIZE`: Length of one wiggle in pixels in one direction. The default
  is 10 (pixels).
