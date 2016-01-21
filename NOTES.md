termdraw v0.1 release notes
===========================

Previous release: v0.1-alpha (d79c4a51)

Current version summary:

+ Add setuptools/pip-compatible `setup.py` (dde9cbb4)
+ Install manpages to /usr/local/man (2c882fb3, 3017a47e)
+ Implement -a/--ascii option to restrict used characters to ASCII charset
  (8753f351)
+ Update README.md (02661ec5)
+ Replace CLI logic with a separate CLIParser class from `togif` project
  (0d0ad387)
+ Implement --output option to redirect output to file (c0ab2cc3)
+ Move TODO files to docs/, split them by minor and major versions (277735d5)
+ Implement -w/--width and -h/--height options to control resulting graph size
+ Extract graph functions and data to graph.py (887d9003, b8a84ce7)
+ Add stdin data consumption (f93d2449)
+ Implement point graph interpolation (24d1a385)
+ Add termdraw.3 manpage (34959851)
