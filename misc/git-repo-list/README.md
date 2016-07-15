git-repo-list - countless volumes of wisdom catalogued for a layman
===================================================================
`git-repo-list` accepts a list of Git repositories and clones each into current
directory, or recurses into subdirectories and runs `git pull` if they have
already been cloned.

```
$ ls
linux repos.txt
$ cat repos.txt
https://github.com/torvalds/linux
https://github.com/kubernetes/kubernetes
$ git repo-list repos.txt
fatal: destination path 'linux' already exists and is not an empty directory.
<pulling linux>
<cloning kubernetes>
```
