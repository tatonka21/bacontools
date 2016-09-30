xclip-tofile - rewriting dusty volumes with bloody hands
========================================================
`xclip-tofile` appends X clipboard entries to a text file. It will try not to
repeat itself, i.e. it will not append xclip contents if they are the last line
in the file (other than that, it's pretty much `xclip -o` polling).
