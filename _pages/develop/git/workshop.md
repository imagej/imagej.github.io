---
mediawiki: Git_workshop
title: Git workshop
section: Extend:Development:Git
---


 These are the notes of a Git workshop held at the [Max-Planck Institute of molecular Cell Biology and Genetics](http://www.mpi-cbg.de/) on August 3rd, 2011.

# What is a version control system, why should I care?

A version control system is a database that holds multiple revisions of a project. A revision consists of

-   the file names and contents (excluding the generated files) as well as their directory structure
-   the author
-   the committer
-   the author date
-   the commit date
-   a description (*commit message*) what the change leading to this revision is about, usually divided into the first line (*subject*) and the more verbose rest (*body*)
-   zero, one or more pointers to revisions preceding the current one

In Git, *a commit* refers to a revision.

Version control usually facilitates:

-   easy backup
-   easy retrieval of specific revisions
-   documentation (who did what when and why?)
-   documentation (how do I do ...?)
-   easy synchronization (staying up-to-date, integrating changes between multiple developers/machines)
-   finding the changes introducing regressions (AKA bugs) efficiently

## Hands-on

Initial setup:

-   set up user name:

    ```
    git config --global user.name "Howard Carter"
    git config --global user.email howard@egyptian-antiquities-service.com
    ```

-   set up editor (if you do not like *vi*)

    ```
    git config --global core.editor wordpad
    ```

First steps:

-   initialize a repository

    ```
    git init
    ```

-   add contents (caveat for Subversion users: *git add* adds the <u>contents</u>, not just the <u>file name</u>)

    ```
    git add hello-world.txt
    ```

-   commit

    ```
    git commit
    ```

Notes:

-   All modified files should be added before calling `git commit`
-   Since the added files are *staged for commit*, the command `git stage` is a synonym for `git add`
-   making use of the `git status` output
-   using a `.gitignore` file
-   adding a Sign-off (AKA S-O-B)
-   `git init` creates .git/ in which all of the repository's files live
-   `git config` accesses .git/config, \~/.gitconfig and /etc/gitconfig

# What are diffs?

Before committing, it is a good idea to see what modifications are about to be committed. One mode to look at them is to let Git show a *diff*. A *diff* consists of the following parts for every modified file:

1.  a pseudo command line starting with *diff --git*
2.  a line describing the *previous* revision, starting with *---*
3.  a line describing the *next* revision, starting with *+++*
4.  one or more *hunks* starting with *@@ -<begin line>,<line count> +<begin line>,<line count>*
5.  a corresponding block of lines starting with a space for lines in both the previous and next revision, a minus for lines only in the previous one (*removed line*) and a plus for lines only in the next revision (*added line*). A modified line will show up as removed and added.

## Hands-on

-   Looking at a diff:

    ```
    git diff
    ```

-   Looking at a diff in color:

    ```
    git diff --color
    ```

-   Changing the default to color diffs:

    ```
    git config --global diff.color auto
    ```

# A word on the data model of Git (and how to reference objects)

See [Git for computer scientists](http://eagain.net/articles/git-for-computer-scientists/).

-   Everything is an object
-   Every object has a type
-   Every object has a *name* that is calculated by a one-way function (the *hash function* SHA-1) from the type and the contents
-   It is a 40-digit hex number
-   Every object is immutable (changing something changes the name).
-   Plain files are encoded as *blobs*
-   Directories are encoded as *trees*
-   Revisions are encoded as *commits*

For ease of use, in addition to their long name (40 hex characters, quite klunky but precise) commits can be referred to by

-   short name
-   HEAD
-   HEAD\~<n>

## Hands-on

-   Inspecting the version history

    ```
    git log
    ```

-   Inspecting the version history in a graphical way

    ```
    gitk
    ```

-   Inspecting the version history with diffs

    ```
    git log -p
    ```

-   Inspecting the latest 5 revisions with diffs

    ```
    git log -p -5
    ```

-   Inspecting just one commit

    ```
    git show HEAD~5
    ```

-   Looking at all commits touching a specific set of files/directories

    ```
    git log README
    ```

Note: to disambiguate between start commit and files, put a *--* between commit and/or options and files/directories, e.g. `git log HEAD -5 -- doc`

# What are branches? Why do I need them?

A branch is a named pointer into the commit graph. The main branch is called 'master' (Subversion's *trunk*, Mercurial's *default*). Since branches are just pointers, they are very easily created.

Committing while on a branch advances that pointer (if you need something that cannot advance, you need to use *tags*).

Note: branch names must be simple, i.e. not contain spaces or wild characters (although minus & underscore is okay).

Branches can be used to organize sets of changes by topic. Compare also [Fiji's tutorial on topic branches](/develop/git/topic-branches).

## Hands-on

-   Creating a branch

    ```
    git checkout -b my-new-branch
    ```

-   Switching to another branch

    ```
    git checkout master
    ```

-   Seeing all (local) branches (the current one is prefixed by a star)

    ```
    git branch
    ```

-   Switching back to the previous branch

    ```
    git checkout @{-1}
    ```

# What does "distributed" mean with regards to Git?

So far, the repository is local to the working directory. But Git can also synchronize with multiple other repositories.

Typically, there is one designated *main repository*. If you want to initialize a working directory from a given repository, use `git clone`.

A main repository usually does not need a working directory, in which case it is called a *bare repository*.

## Hands-on

-   Clone a repository

    ```
    git clone git://github.com/git/hello-world
    ```

-   Clone a repository from USB disk or file server

    ```
    git clone /path/to/hello-world
    ```

-   Set up a main repository on the file server

    ```
    git init --bare --shared=group /path/to/fileserver/my.git
    ```

# The merge concept of Git (and what is this "index" all about?)

When working with others, or with topic branches, the changes (including their complete commit history) need to be integrated into another branch, typically *master*. This integration is called *merging*.

In order to perform a merge, the file versions are put into a staging area (the *index*), and all non-overlapping changes are resolved automatically. Overlapping (read: contradicting) changes are not resolved, but marked as *merge conflicts*.

Please refer to the Fiji's page on [Git Conflicts](/develop/git/conflicts) for a detailed explanation how to resolve merge conflicts.

## Hands-on

-   Initialize and commit a file, say, *hello.txt*

    ```
    echo Hello > hello.txt
    git add hello.txt
    git commit -m initial
    ```

-   Initialize a new branch and modify hello.txt

    ```
    git checkout -b tut-anch-amun
    echo Boooh > hello.txt
    git add hello.txt
    git commit -m "On branch"
    ```

-   Switch back to old branch, modify hello.txt

    ```
    git checkout @{-1}
    echo Hi > hello.txt
    git add hello.txt
    git commit -m "On original branch"
    ```

-   Merge

    ```
    git merge tut-anch-amun
    ```

# What are reflogs? How can they help me?

We looked at the commit history previously. But every repository has its own individual history; for example, yesterday at noon, a specific branch with a specific revision was the current branch. This is stored in the reflogs (for space efficiency, reflogs are not available eternally but are pruned at some stage).

You can access the reflogs by appending *@{<number>}* or *@{<date>}* to a branch name or to *HEAD*.

## Hands-on

-   See what revision was current five minutes ago

    ```
    git show HEAD@{5.minutes.ago}
    ```

-   See the reflog history

    ```
    git log -g
    ```

# What is the stash?

Sometimes one needs to store away all modifications and go back to a clean state, but keep the modifications accessible. This is done using the *stash*.

Note: the stash is a special pseudo-branch, living in *refs/stash*. Their history is in the reflog.

## Hands-on

-   Make a change and stash it

    ```
    echo Shalom > hello.txt
    git stash
    ```

-   Get it back

    ```
    git stash apply
    ```

-   Stashing only the changes that have not been `git add`ed yet

    ```
    echo Howdy > hello.txt
    git add hello.txt
    echo Hey hey > hello.txt
    git stash -k
    ```

-   Getting a list of stashed changes

    ```
    git stash list
    ```

-   Stash with a custom message

    ```
    git stash save This is my description
    ```

-   Remove the latest changes from the stash

    ```
    git stash pop
    ```

# Accessing parts of the object database

The primary way to look at commits is by using `git show`. It can show tags, commits, trees and blobs.

To access more information about commits, use the parameter *--pretty=fuller*.

For more low-level access, use `git cat-file`.

## Hands-on

-   Show the raw commit message, with the diff

    ```
    git show --pretty=raw HEAD
    ```

-   Show a commit's corresponding top-level tree

    ```
    git show HEAD:
    ```

-   Show a blob

    ```
    git show HEAD:Documentation/README
    ```

-   Low-level access to a commit

    ```
    git cat-file commit HEAD
    ```

# What meanings do "checkout", "reset" have in Git?

We already saw that *checkout* can switch between branches and even initialize new branches.

Unfortunately, *checkout* is also the command to pick file versions from other branches without switching the branches. Thusly picked file versions are automatically added, i.e. staged for the next commit.

To unstage changes, one can use the *reset* command (without arguments, it resets all files which HEAD knows about currently).

The *reset* command can further be convinced to reset not only the index (staging area), but also the working directory.

## Hands-on

-   pick a file version from another branch

    ```
    git checkout other-branch README
    ```

-   Unstage all changes, i.e. revert all files from "to-be-committed" status to "modified"

    ```
    git reset
    ```

-   Get rid of all changes (like `git stash` but the changes are not stored)

    ```
    git reset --hard
    ```

# Git's concept of "remote repositories"

In addition to the repository from which we cloned, other repositories can be linked, too, using the `git remote` command. Such repositories are called *remote repositories* or simply *remotes*.

The repository from which we cloned is called *origin*.

Interaction with remote repositories is performed using

-   `git fetch`, which local copies of the branches of the remote repository including all required objects (but being a bit clever about avoiding to get objects we have already) and
-   `git push`, which updates remote repositories' branches to the local branches' state.

The local copies of remote branches live in a specific namespace, refs/remotes/<name>. For example, the *master* branch of the remote called *origin* will be stored in *refs/remotes/origin/master*. If unambiguous, it can be referred to as *origin/master*, too.

Note: you need to make sure that you do not mix two different projects in the same working directory's repository. Git will happily fetch from wherever into your local repository, even if it does not make sense.

Note: there is a shortcut for *fetch & merge*: *pull*. If you create a new branch from a local copy of a remote branch, you can even set it up such that *git pull* without further parameters will fetch from the correct remote and merge the correct branch: *git checkout --track origin/cool-feature*

## Hands-on

-   Add a remote

    ```
    git remote add hello git://github.com/git/hello-world
    ```

-   Fetch from a remote

    ```
    git fetch hello
    ```

-   Listing all local copies of the remotes' branches

    ```
    git branch -r
    ```

-   Push a branch

    ```
    git push origin master
    ```

-   Push the current branch

    ```
    git push origin HEAD
    ```

-   Push to a branch with a name differing from the local name

    ```
    git push origin my-new-branch:master
    ```

-   Delete a branch from a remote repository

    ```
    git push --delete origin blabla-branch
    ```

# Popular public repository hosters

If you need to have public repositories, you can use http://github.com/, http://code.google.com/, http://sourceforge.net/, http://repo.or.cz/ and quite a few others. Typically, you have a decent amount of storage, but the deal is that your version-controlled project must be Open Source.

As a goodie, all of said hosters support *gitweb*, a web interface to look at the history.

## Hands-on

Let's surf to http://github.com/git/hello-world and inspect the history

# Advanced topics

-   aliases

-   rebasing

-   cherry-picking

-   partial staging

-   interactive checkout

-   tags (simple, annotated, signed)

-   bisecting

-   blaming

-   *git apply*

-   *git diff --color-words*

-   archiving

-   scripting (plumbing/porcelain)

-   hooks

-   diff filters

-   interacting with svn

-   interacting with Mercurial

-   smudge/clean filters

-   merge drivers

-   diff drivers

-   rename handling

# Links

-   The homepage: http://git-scm.com/
-   Git for Windows: http://code.google.com/p/msysgit/
-   Git for MacOSX http://code.google.com/p/git-osx-installer/
-   An overview of the underlying data model: http://eagain.net/articles/git-for-computer-scientists/
-   Fiji's *topic branches* tutorial: https://fiji.sc/wiki/index.php/Git_topic_branches
-   The ProGit book: http://progit.org/
-   The most popular repository hoster: https://github.com/
-   The original repository hoster: http://repo.or.cz/
-   The Git Wiki: https://git.wiki.kernel.org/index.php/Main_Page

 
