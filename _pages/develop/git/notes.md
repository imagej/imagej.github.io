---
title: Git Notes
section: Extend:Development:Git
---


 Here are some common git operations for which we often find ourselves searching.

## Workflow

### Checkout a remote branch 'develop' and keep it linked to the origin

```shell
git checkout -t origin/develop
```

It should report: "Branch develop set up to track remote branch develop from origin."

### List all branches (both local and remote)

```shell
git branch -a
```

### List local branches and their corresponding upstream remote branches

```shell
git branch -vv
```

### Revert local changes to a file (prior to commit)

```shell
git checkout file
```

### Revert all local changes to the current subtree (prior to commit)

```shell
git checkout .
```

### Cute hack to revert all local changes (prior to commit)

```shell
git stash git stash drop
```

### Undo a commit

```shell
git reset --soft HEAD^
```

### Undo multiple commits

```shell
git reset --soft HEAD@{2}
```

Where `2` is the number of commits to undo.

### Update to latest HEAD, preserving local changes and local commits on top

```shell
git stash
git pull --rebase
git stash pop
```

### Push changes on main to origin

```shell
git push origin main
```

### Delete untracked files and directories

```shell
git clean -df
```

### Interactively stage patches from changed file(s)

```shell
git add -p &lt;path&gt;
```

### Roll back the last commit's changes to a particular file

```shell
git checkout HEAD@{1} -- file
```

## Branches

### Branch main to a new local branch "new\_branch"

```shell
git checkout -b new_branch main
```

### Push local branch to remote

```shell
git push -u origin new_branch
```

### Make the current local branch start tracking a corresponding remote branch

```shell
git branch --set-upstream-to origin/new_branch
```

This is not necessary if you used `git push -u` as suggested above.

### List the local branches that have already been merged to this one

```shell
git branch --merged
```

### Diff a file between two branches

```shell
git diff branch1 branch2 -- file
```

### Delete a branch both locally and remotely

```shell
git branch -rd origin/branch_to_kill
git branch -d branch_to_kill
git push origin :branch_to_kill
```

### Move a commit from bad\_branch to good\_branch

```shell
# First cherry-pick the commit onto the correct branch:
git checkout good_branch
git cherry-pick deadbeef

# Then remove the commit from the bad branch:
git checkout bad_branch
git rebase -i
# Change the undesirable commit to "noop"
```

For more on branching, see [Git topic branches](/develop/git/topic-branches).

### Rename the current branch

```shell
git branch -m <new branch name>
```

## Git + SVN

### Clone an SVN repository to a local Git repository

```shell
git svn clone -s http://svn.code.sf.net/p/jhotdraw/svn/
```

### Commit and push changes, even with local changes in the working copy

```shell
git commit git stash git svn dcommit git stash pop
```

### Update to latest trunk, preserving local changes and local commits on top

```shell
git stash git svn rebase git stash pop
```

## Searching

### Recursively search for HelloWorld.file (and display the most recent commit modifying it)

```shell
git ls-tree -r HEAD | grep HelloWorld.file
```

### Recursively search for all files containing the phrase 'import HelloWorld'

```shell
git grep 'import HelloWorld'
```

### Recursively search for all files *in any topic branch* containing the phrase 'import HelloWorld'

```shell
git grep 'import HelloWorld' $(git rev-list --all --no-walk)
```

## History

### Display a log with colored word diffs

```shell
git log -p --color-words
```

Add `-S` to `less` to virtually wrap long lines.

### Display a diff with colored words between a file in one commit and a file in another commit

```shell
git diff <commitA>:<file> <commitB>:<file> --color-words
```

Add `-S` to `less` to virtually wrap long lines.

### Display all contributing authors of a project including their e-mail

```shell
git log --format='%aN <%ae&>' | sort -u
```
Respects `.mailmap`.

### Viewing the history for a single file

```shell
git log --follow HelloWorld.file
```

This history is algorithmically calculated and must be carefully preserved.

Simultaneous (within a single commit) significant changes + file renaming (including relocation) can prevent the algorithm from successfully tracing the file's history, or cause it to begin tracing the wrong file.

Keeping code changes separate from renames should prevent this confusion, but it is good practice to check `log --follow` before pushing to a remote repository.

### See commits in branch B not present in branch A

There are two main options. The first:

```shell
git log A..B
```

will display the different commits in full git log format. NB: the `..` between commits is important to sure only the difference in commits is considered.

The second:

```shell
git cherry -v A B
```

will display a simple list of the different commits, one per line, with commit message and hash.

## Scripts

There are some Git-related scripts available in the [scijava-scripts](https://github.com/scijava/scijava-scripts) project.

### List information about all remote branches including last author, commit date and unmerged commit count

```shell
$SCIJAVA/bin/remote-branch-info.sh
```

## Advanced and/or dangerous

### Create a repository with g+w permissions

```shell
git init --shared=group
```

Or for a bare repository:

```shell
git init --bare --shared=group
```

(Bare repositories are meant for a remote server repository that all your coworkers push into and pull/fetch from.)

### Push all remote branches from one remote (e.g., "origin") to another (e.g., "github")

```shell
git push github $(git for-each-ref refs/remotes/origin | \
  grep -v HEAD | \
  while read sha1 type ref
  do
    echo $ref:refs/heads/${ref#refs/remotes/origin/}
  done)
```

### Another way to push all remote branches between remotes

```shell
eval git push github $(git for-each-ref | \
  sed -n 's/.*\t\(refs\/remotes\/origin\/\(.*\)\)$/\1:refs\/heads\/\2/p')
```
### Fully garbage collect and compact the repository (deletes all orphaned refs!)

```shell
git reset --hard git for-each-ref --format="%(refname)" refs/original/ | \
  xargs -n 1 git update-ref -d git reflog expire --expire=now --all git gc --aggressive --prune=now
```

## Rewriting history

### Split a subdirectory into a separate git repository

See these posts on Stack Overflow:

-   [Detach subdirectory into separate Git repository](http://stackoverflow.com/questions/359424/detach-subdirectory-into-separate-git-repository)
-   [Detach subdirectory (that was renamed!) into a new repo](http://stackoverflow.com/questions/6638019/detach-subdirectory-that-was-renamed-into-a-new-repo)
-   [Split large Git repository into many smaller ones](http://stackoverflow.com/questions/3910412/split-large-git-repository-into-many-smaller-ones)

### Throw away git-svn-id metadata

```shell
git filter-branch --msg-filter ' sed -e "/^git-svn-id:/d" '
```

### Combine the first two commits of a Git repository

See this post on Stack Overflow:

-   [How do I combine the first two commits of a Git repository?](http://stackoverflow.com/questions/435646/how-do-i-combine-the-first-two-commits-of-a-git-repository)

### Change the author of a commit

```shell
git commit --amend --author="Author Name"
```

### Change the author of many commits

See this post on Stack Overflow:

-   [How do I change the author of a commit in git?](http://stackoverflow.com/questions/750172/how-do-i-change-the-author-of-a-commit-in-git)

### Merge multiple repositories

See these posts on Stack Overflow:

-   [Combining multiple git repositories](http://stackoverflow.com/questions/277029/combining-multiple-git-repositories)
-   [git: Retroactively introduce several merges](http://stackoverflow.com/questions/4039682/git-retroactively-introduce-several-merges)

## Tutorials

### Creating a shared remote repository

```shell
ssh you@server
mkdir repos/remote.git
cd repos/remote.git
git --bare init --shared=group
logout

cd ~/local
git remote add origin ssh://you@server/home/you/remote.git
git push origin main
git config branch.main.remote origin
git config branch.main.merge refs/heads/main
```

Creates a bare remote repository at [`ssh://server/home/you/remote.git`](Ssh___server_home_you_remote.git) that tracks your local repository in `/home/you/local`. Adopted from [Tim Lucas](http://toolmantim.com/articles/setting_up_a_new_remote_git_repository).

### Displaying a filtered set of commits

Assume you want to see commits in branch `stephan`, but only those that are <u>not</u> part of the history of branch `saalfeld`:

```shell
git log stephan ^saalfeld
```

More realistically, if you want to see all the commits which are in a topic branch, but not yet merged into main:

```shell
git log --all ^main
```

If you want to see the changes which come from a topic branch which was merged in commit `deadbeef`, use this command line:

```shell
git log deadbeef^..deadbeef^2
```

Explanation: `deadbeef` is a merge commit, so its first parent (`deadbeef^`, can also be written as `deadbeef^1`) was the current `HEAD` when the merge was performed, and the second parent (`deadbeef^2`) is the tip of the branch which was merged. The argument `A..B` is short form of `^A B`, i.e. all commits reachable from `B` excluding those which are also reachable from `A`.
