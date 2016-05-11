myzuka - and who are you, the proud lord said
=============================================

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
$ myzuka "double trouble"
 1  Mike Mareen        Double Trouble                             (05:22)
 2  Rob                Double Trouble                             (01:02)
 3  Double Trouble     Mary Has A Little Lamb                     (04:16)
 4  John Williams      Double Trouble                             (01:37)
 5  Double Trouble     Willie the Wimp (And His Cadillac Coffin)  (04:34)
 6  The Cars           Double Trouble                             (04:15)
 7  John Verity        Double Trouble                             (04:10)
 8  Innes Sibun        Double Trouble                             (06:51)
 9  Lynyrd Skynyrd     Double Trouble                             (02:51)
10  Eric Clapton       Double Trouble                             (08:03)
11  Double Trouble     I Swear (Single Version)                   (03:21)
12  Joe Bonamassa      Double Trouble                             (07:30)
13  Sean Costello      Double Trouble                             (07:36)
14  Nitro              Double Trouble                             (03:57)
15  Raimondo Andreolo  Double Trouble                             (06:28)
16  John Mayall        Double Trouble                             (03:22)
17  Public Image Ltd.  Double Trouble                             (03:53)
18  Double Trouble     I Swear                                    (03:21)
19  Jon Paris          Double Trouble                             (05:26)
20  Sterling Koch      Double Trouble                             (05:58)
Download track # 4
./John Williams - Double Trouble.mp3
$ myzuka
Search for professor umbridge
1  Nicholas Hooper  Professor Umbridge  (02:33)
Download track # 1
./Nicholas Hooper - Professor Umbridge.mp3
$ file John\ Williams\ -\ Double\ Trouble.mp3 Nicholas\ Hooper\ -\ Professor\ Umbridge.mp3
John Williams - Double Trouble.mp3:       Audio file with ID3 version 2.3.0 <..>
Nicholas Hooper - Professor Umbridge.mp3: Audio file with ID3 version 2.3.0 <..>
```

Downloading over Tor
--------------------

Supplying `-t`/`--tor` command line option to `myzuka` makes it download web
pages and files over Tor, assuming it runs as a SOCKS5 proxy at
`localhost:9050`. Note that `myzuka` will still leak your DNS requests to the
network, however, your IP will be masked from the target website.
