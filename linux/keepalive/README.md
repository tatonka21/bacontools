keepalive - Come on, breathe, baby. Goddamn it, breathe. Goddamn it, you bitch!
===============================================================================
`keepalive` runs a specified command line whenever it detects that no instances
of that process (not accounting for the whole command line) are currently
running.

```
$ env INTERVAL=1s keepalive sleep 10s
Fri Aug 19 20:30:35 MSK 2016: restarting sleep 10s
Fri Aug 19 20:30:46 MSK 2016: restarting sleep 10s
^CSIGINT received, exiting
```

By default, `keepalive` checks for running instances of the given process every
10 seconds; `INTERVAL` environment variable will override that value.
