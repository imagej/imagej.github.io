---
title: 2012-02-17 - Using git-svn to develop ImageJ2
---

## Introduction

Subversion is a decent version control program that does not require much thought to operate. Unfortunately, if you want to avoid clunky, unreviewable monster commits ([a known worst practice](http://www.crealytics.de/blog/2010/07/09/5-reasons-keeping-git-commits-small-mluedtke/)), you will need third-party programs to prepare any non-trivial set of patches.

One such third-party program is called [Git](/develop/git)... While Git is usually meant to be used as a standalone version control system (and we have hints [here](/develop/git/notes) and links [here](/develop/git) how to use it), its [`git rebase -i`](/develop/git/topic-branches) functionality lends itself to a patch series based workflow.

## The `git svn` workflow

Our recommended `git svn` workflow was described in our chatroom by {% include person id='bdezonia' %}:

1.  `git svn fetch`
2.  `git checkout -b NewBranch trunk`
3.  &lt;do some edits and test, git adds, git commits, etc.&gt;
4.  `git svn fetch`
5.  `gitk ...trunk`
    -   &lt;if not linear development then&gt;  
        `git rebase -i trunk`

    &lt;finally&gt;
6.  `git svn dcommit`

The idea is to first synchronize the local branches with the the Subversion repository (step 1).

Then start and work on a new topic branch (steps 2 & 3). This may involve heavy rewriting and even sharing the branch with other developers just as you are wont from [regular Git workflows](http://schacon.github.com/git/gitworkflows.html).

When you are ready to publish the patch series in Subversion, synchronize again (step 4) and make sure that no merge commits are present on top of Subversion's *trunk*. This is necessary because `git svn` can really only apply a number of patches, it cannot create merge commits. Should there be non-linear development, use Git's `rebase` command to linearize it.

After everything was prepared for Subversion, use the `dcommit` command of `git svn` to commit all changes that are in the current branch but not yet in *trunk*. (If you are interested why it is called `dcommit`: the original `commit` subcommand of `git svn` is a historic wart...)

## Setting up the local working directory

To get started with `git svn`, you need an initial `git-svn` clone. The easy way to do this would be to start

```
git svn clone -s https://code.imagej.net/svn/imagej
```

However, this is relatively slow since it uses Subversion to check out every revision in the complete history. You can instead hook up a fresh Git working tree with our pre-imported Git repository like this:

1.  `git init`
2.  add these sections to the .git/config file  
	```ini
	[remote "origin"]
	url = git://code.imagej.net/imagej.git
	pushURL = git@code.imagej.net:imagej.git
	fetch = +refs/heads/*:refs/remotes/origin/*
	fetch = +refs/heads/svn/*:refs/remotes/*
	[svn-remote "svn"]
	url = http://code.imagej.net/svn/imagej
	fetch = trunk:refs/remotes/trunk
	branches = branches/*:refs/remotes/*
	tags = tags/*:refs/remotes/tags/*
	```
3.  `git fetch`
4.  `git svn fetch`  (this step takes some time...)
5.  `git checkout -b master -t trunk`

Explanation: rather than letting `git svn` do its job from the get go, we first initialize the *origin* remote (steps 1 to 3). It is initialized such that the Subversion branches -- which our Git repository exposes in the *svn/\** namespace -- are fetched into the place where `git svn` will pick them up rather than going through the tedious multi-hour process of any bootstrap `git svn` import.

In step 4, `git svn` indeed picks up those pre-imported branches.

Lastly, we initialize the local *master* branch to track Subversion's *trunk*.

 
