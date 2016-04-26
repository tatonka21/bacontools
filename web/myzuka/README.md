myzuka - download songs from myzuka.fm
======================================

`myzuka` is a CLI frontend for the music hosting website
[myzuka.fm](https://myzuka.fm). It runs Capybara and Poltergeist, leveraging
PhantomJS for web crawling. Yes, I know this might be an overkill. No, I'm
probably not changing the architecture.

For each command line option, `myzuka` queries the website, retrieves top 20
search results, and prompts the user for the exact track to download. The file
will be saved to the working directory. If no arguments are supplied, `myzuka`
prompts the user for a search string.

Usage example
-------------

```
$ web/myzuka/myzuka double\ trouble
1. Mike Mareen - Double Trouble (05:22)
2. Rob - Double Trouble (01:02)
3. John Williams - Double Trouble (01:37)
4. Double Trouble - Mary Has A Little Lamb (04:16)
5. The Cars - Double Trouble (04:15)
6. Double Trouble - Willie the Wimp (And His Cadillac Coffin) (04:34)
7. John Verity - Double Trouble (04:10)
8. Innes Sibun - Double Trouble (06:51)
9. Lynyrd Skynyrd - Double Trouble (02:51)
10. Eric Clapton - Double Trouble (08:03)
11. Joe Bonamassa - Double Trouble (07:30)
12. Sean Costello - Double Trouble (07:36)
13. Nitro - Double Trouble (03:57)
14. Raimondo Andreolo - Double Trouble (06:28)
15. John Mayall - Double Trouble (03:22)
16. Public Image Ltd. - Double Trouble (03:53)
17. Jon Paris - Double Trouble (05:26)
18. Sterling Koch - Double Trouble (05:58)
19. Double Trouble - I Swear (Single Version) (03:21)
20. Paul Gilbert - Double Trouble (03:08)
Download track # 3
Saving to John Williams - Double Trouble.mp3
$ web/myzuka/myzuka
Search for professor umbridge
1. Nicholas Hooper - Professor Umbridge (02:33)
Download track # 1
Saving to Nicholas Hooper - Professor Umbridge.mp3
$ file John\ Williams\ -\ Double\ Trouble.mp3
John Williams - Double Trouble.mp3: Audio file with ID3 version 2.3.0 <...>
$ file Nicholas\ Hooper\ -\ Professor\ Umbridge.mp3
Nicholas Hooper - Professor Umbridge.mp3: Audio file 2.3.0 <...>
```

Downloading over Tor
--------------------

Supplying `-t`/`--tor` command line option to `myzuka` makes it download web
pages and files over Tor, assuming it runs as a SOCKS5 proxy at
`localhost:9050`. Note that `myzuka` will still leak your DNS requests to the
network, however, your IP will be masked from the target website.
