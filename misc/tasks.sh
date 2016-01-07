#!/bin/sh
grep --exclude-dir=.git -C 3 -nrEI "TODO|FIXME|NOTE|HACK|BUG|XXX|CHANGED" . 2>/dev/null
