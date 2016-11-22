bacontools list
===============

Git utilities
-------------
| Tool                  | Maturity | Description                                            | Language    |
|-----------------------|----------|--------------------------------------------------------|-------------|
| git-clone-github-user | Hack     | Clone all repositories of a single Github user         | POSIX shell |
| git-force-pristine    | Hack     | Make the working tree identical to HEAD                | POSIX shell |
| git-ls                | Untested | Github-like human-readable Git repo directory listing  | Python      |
| git-repo-list         | Hack     | Clone or pull all repos from a remote list             | POSIX shell |
| git-stat-atr          | Hack     | Sort output of `git diff --stat` by added/total ratio  | POSIX shell |

Linux utilities
---------------
| Tool           | Maturity | Description                                    | Language    |
|----------------|----------|------------------------------------------------|-------------|
| bindump        | Hack     | Encode data to a binary dump                   | POSIX shell |
| cate           | Hack     | Rewrite files interactively with cat and stdin | POSIX shell |
| checkreboot    | Hack     | Print whether reboot is required               | POSIX shell |
| cptemp         | Hack     | Copy file/directory to /tmp                    | POSIX shell |
| cursorwiggle   | Hack     | Wiggle mouse cursor with xdotool               | POSIX shell |
| devbup         | Moving   | Backup, archive, and encrypt files and devices | Bash        |
| devrestore     | Hack     | Restore devbup archives                        | Bash        |
| docker-cleanup | Hack     | Remove old Docker containers                   | POSIX shell |
| du1            | Hack     | Print sizes of top level directories           | POSIX shell |
| keepalive      | Hack     | Restart a process if it's not running          | POSIX shell |
| netinfo        | Untested | Print current WAN IP and nmcli connection name | POSIX shell |
| setscreen      | Hack     | Change specified X RandR display resolution    | POSIX shell |
| single-urxvt   | Hack     | Launch a singleton urxvt instance              | POSIX shell |
| userls         | Hack     | Print all users on the system                  | POSIX shell |
| xclip-tofile   | Hack     | Poll xclip and append it to a file             | POSIX shell |
| zerofile       | Hack     | Overwrite files with zeros                     | POSIX shell |

Media utilities
---------------
| Tool           | Maturity   | Description                                        | Language    |
|----------------|------------|----------------------------------------------------|-------------|
| ImageValidator | Untested   | Detect corrupted images                            | C#          |
| ffmpeg-togif   | Untested   | Convert videos to high quality animated GIFs       | POSIX shell |
| preptrack      | Moving     | Reencode files to MP3s, rewrite ID3V2 tags         | Bash        |
| togif          | Maintained | Convert videos to animated GIFs                    | POSIX shell |
| vidinfo        | Hack       | Print video size, FPS, dimensions, and stream info | POSIX shell |

Text utilities
--------------
| Tool      | Maturity | Description                                          | Language    |
|-----------|----------|------------------------------------------------------|-------------|
| balance   | Untested | Detect if strings contain balanced/unbalanced parens | C           |
| center    | Hack     | Center text                                          | POSIX shell |
| lines     | Hack     | Print distribution of input lines lengths            | POSIX shell |
| morseconv | Hack     | Convert text to Morse                                | Python      |
| n7m       | Untested | Generate a numeronym (i18n, l10n, etc.)              | C           |
| readable  | Untested | Heuristically filter out garbage strings             | C           |
| ringcat   | Hack     | Append stdin to the end of the file circularly       | POSIX shell |
| ruler     | Hack     | Print length of the longest line                     | POSIX shell |
| trimline  | Hack     | Trim leading and trailing whitespaces                | POSIX shell |
| vimless   | Hack     | Display vimcat output in less                        | POSIX shell |

Web utilities
-------------
| Tool           | Maturity | Description                            | Language    |
|----------------|----------|----------------------------------------|-------------|
| checktor       | Hack     | Check if TCP connection is torified    | POSIX shell |
| content-length | Hack     | Print sum of file sizes at given URLs  | POSIX shell |
| curl-tt        | Hack     | Test server response time              | POSIX shell |
| httpdf         | Hack     | Listen to a port and return free space | Go          |
| myzuka-dl      | Moving   | Download audio tracks from myzuka.fm   | Ruby        |
| imgur-dl       | Moving   | Download Imgur albums                  | Ruby        |
| respcode       | Hack     | Return HTTP response code              | POSIX shell |
| wget-page      | Hack     | Download a web page                    | POSIX shell |
| wget-parallel  | Hack     | Download multiple files simultaneously | POSIX shell |

Miscellaneous utilities
-----------------------
| Tool              | Maturity | Description                                             | Language    |
|-------------------|----------|---------------------------------------------------------|-------------|
| EncodingConverter | Untested | Convert between different encodings                     | C#          |
| apdiff            | Hack     | Print differing parts of similar file paths             | Python      |
| baconplaylist     | Hack     | Query a list in a specific format                       | POSIX shell |
| bananaglee        | Hack     | Generate a USA federal agency-like project identifier   | Haskell     |
| bitcount          | Hack     | Tally individual bits in stdin bytes                    | C           |
| bitdiff           | Hack     | Detect different bytes in mostly similar files          | C           |
| byteat            | Hack     | Print value of byte at index                            | C           |
| corrupt           | Untested | Flip/remove random bits/bytes                           | C           |
| maybe             | Hack     | Prints yes and no randomly interleaved                  | C           |
| pip-upgrade-all   | Hack     | Upgrade all local PIP packages                          | Python      |
| stopwatch         | Hack     | Count elapsed time                                      | Bash        |
| tasktags          | Untested | Search for tags like TODO                               | POSIX shell |
| termdraw          | Moving   | Print ASCII-art graphs                                  | Python      |
| update-all        | Hack     | Update all Git repositories in level 1 subdirectories   | POSIX shell |
| watchclock        | Hack     | Display an ASCII-art clock in your terminal             | POSIX shell |
