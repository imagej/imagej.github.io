{{GitMenu}}
= What is Git? =

Git is a distributed Version Control System ("VCS"), or Source Code Management tool ("SCM"). The purpose is to track the development of source code through time, along with useful side information: Who did it? When? Why?

= Principles of Git =

The source code lives in a ''working directory'', where you have ''tracked'' files (i.e. files which are version-controlled) and ''untracked'' files (for example, ''.class'' files; they are generated from the source code, so they are uninteresting).

The timeline of the development is made up of ''revisions'' (''commits'' in Git speak) of the source code. Each commit knows about its predecessors. In the common case, commits form something like a perl of revisions. By comparing a commit to its ''parent commit'' (i.e. comparing a revision to the previous one), one can see the changes introduced by the "child" commit.

Commits contain the names and contents of the tracked files, information about the author (and the committer, who does not need to be the author), the time of the commit, and a ''commit message'' where the author should say what the reasons for the changes are.

To make a new commit, you first tell Git what changed contents you want to be part of the new commit by ''adding'' (or ''staging'') them, and then performing the commit itself, which will open an editor in which you can type the commit message.

All Git-specific things, such as revisions, are stored in the ''repository'', which lives in the subdirectory ''.git/'' in your project's root directory.

To collaborate with others, there are also ''remote repositories'' from where you can ''clone'', and with which you can synchronize by ''fetching'' and ''pushing''.

= Why do I need Git? =

Git makes it not only to record what you did, it makes it easy to follow the development of other developers, and integrate those changes (''merge'' in Git speak).

Even if we are all brilliant developers, from time to time the program appears to be completely broken by our work. Git can tell you which changes you made relative to the current commit—quickly!

Further benefits:
* Study the history of a project to understand not only ''what'' the developers did ''when'', but also ''why'' by reading their commit messages (i.e., the log of changes).
* Recover any past revision, such as when the latest version suffers from a bug (i.e., a ''regression'') not present in an older version.
* Easily [[Pinpoint regressions with Git|find the commit which introduced such a regression]].
* Ensure the code and history is never lost, even if your machine fails—anyone with a ''clone'' of the repository has a copy of the entire history.
* Work on multiple new features or bug-fixes simultaneously, easily organizing and switching between them using ''branches''.

The only negative to Git is the activation barrier of learning it. Once you become proficient, Git is a huge asset to any development project.

If you feel comfortable in using the commandline but you are still not familiar with Git the '''[[Git workshop]]''' page might be a perfect entry point for you.

If the commandline is not your favorite playground you can have a look at the Git integration '''[[EGit]]''' in the '''[[Eclipse]]''' IDE.

= Essential Git commands =

Except for the ''clone'' command, this follows the common workflow:

* ''git diff HEAD'' will show you the changes of your working directory relative to the current commit.

* ''git add <file>...'' tells Git that you want the next commit to contain the current version of that file/these files.

* ''git commit'' tells Git that you want to commit a new revision with all staged changes.

* ''git fetch origin'' synchronizes the local copy of the default remote repository.

* ''git merge origin/master'' integrates the default remote repository's changes into your local repository and working directory (<u>never</u> do this when you have uncommitted changes!).

* ''git push origin HEAD'' publish your changes in the remote repository.

Initially, you need to start from somewhere:

* ''git clone <URL>'' will make a new local repository and initialize it from a remote one.

See also the more verbose [[Git mini howto]].

= Substantial differences to other version control systems =

If you know CVS or Subversion, you are in for some surprises:

* In Git, each repository is local. To publish your changes, you need to have a remote repository, too, and ''push'' your work there.
* In Git, [[Git topic branches|branches]] are easy and fast.
* In Git, you ''git add'' <u>content</u>, not files. In other words, when the file ''README'' is already tracked, ''git add README'' will tell Git that you want the changes in said file to be part of the next commit.
* In Git, you <u>never, ever</u> try to integrate remote changes into an uncommitted state. In other words, if you have uncommitted changes, you <u>always</u> commit them before calling ''git fetch origin; git merge origin/master''.

[[Category:Git]]
