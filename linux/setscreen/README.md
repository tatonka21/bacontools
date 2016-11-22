setscreen - rapidly shifting alien landscapes
=============================================
`setscreen` creates and applies X RandR modelines to the specified display.
In other words, it changes resolution of the specified X display.

```
$ xrandr --listmonitors
Monitors: 1
 0: +*eDP1 1600/390x900/220+0+0  eDP1
$ setscreen 1440x900 eDP1
<...changes default monitor to the 1440x900 resolution...>
```
