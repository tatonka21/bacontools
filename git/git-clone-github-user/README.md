git-clone-github-user - ceaseless discharge of samefaced persons
================================================================
`git-clone-github-user` accepts a Github user or organization name and clones
all their public repositories to the working directory.
```
$ git-clone-github-user google
Cloning into 'acai'...
Cloning into 'access-bridge-explorer'...
<..>
```
All command line arguments except the first one are passed to `git clone`
invocations:
```
$ git-clone-github-user google --depth=1
```
