bacontools - gradual descent into madness
=========================================
bacontools is a collection of small utilities I've written over the years.

Status
------
![Travis][travis]

Tool count
----------
| Directory | Description                                         | Languages                           | Count |
|-----------|-----------------------------------------------------|-------------------------------------|-------|
| linux     | Tools specific to GNU/Linux distributions           | POSIX shell, Bash                   | 7     |
| media     | Tools for editing media (audio, video, image) files | C#, POSIX shell, Bash               | 4     |
| text      | Tools for working with text                         | C, POSIX shell                      | 7     |
| web       | Internet-related tools                              | Go, Ruby                            | 4     |
| misc      | Everything else                                     | Python, C#, C, Haskell, POSIX shell | 13    |
|           |                                                     | *Total*                             | 35    |

Tool maturity
-------------
`bacontools` has many utilities which are still in their early development
phase. Different stages of a tool's development shall be outlined in parent
directory READMEs as follows:

| Maturity   | Description                                                                                               |
|------------|-----------------------------------------------------------------------------------------------------------|
| Hack       | Solution to a single specific problem. Not guaranteed to work correctly in all cases, or to be extensible |
| Untested   | Some extensions and options have been implemented, but no testing and/or debugging has been performed     |
| Moving     | Some testing/debugging was performed, and new features are being implemented                              |
| Maintained | No new features are currently implemented, debugging and testing may continue                             |

Please note that, regardless of the tool's maturity label, the responsibility
waiver in its license still applies, if present.

Snippets
--------
Little code snippets that don't deserve a separate tool are saved to
`snippets`. They are not included in total tool count.

License
-------
Unless otherwise specified in a tool's README, all tools included in this
repository are distributed under the general license in the LICENSE file.

[travis]: https://img.shields.io/travis/bacondropped/bacontools.svg
