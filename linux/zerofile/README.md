zerofile - priceless scriptures defaced, now lying useless
==========================================================
`zerofile` overwrites contents of each its file argument with zeros obtained
from `/dev/zero`, preserving file sizes.

```
$ echo "Hello world!" > somefile
$ xxd somefile
00000000: 4865 6c6c 6f20 776f 726c 6421 0a         Hello world!.
$ stat somefile
  File: 'somefile'
  Size: 13        	Blocks: 8          IO Block: 4096   regular file
Device: ...
Access: (0644/-rw-r--r--)  Uid: ( 1000/bacondropped)   Gid: ( 1000/bacondropped)
Access: ...
Modify: ...
Change: ...
 Birth: -
$ zerofile somefile
$ xxd somefile
00000000: 0000 0000 0000 0000 0000 0000 00         .............
$ stat somefile
  File: 'somefile'
  Size: 13        	Blocks: 8          IO Block: 4096   regular file
Device: ...
Access: (0644/-rw-r--r--)  Uid: ( 1000/bacondropped)   Gid: ( 1000/bacondropped)
Access: ...
Modify: ...
Change: ...
 Birth: -
```

If `SOURCE` environment variable is specified and contains a readable file
path, `zerofile` will read bytes from that file instead of `/dev/zero`.
