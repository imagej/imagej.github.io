== Introduction ==

Subversion is a decent version control program that does not require much thought to operate. Unfortunately, if you want to avoid clunky, unreviewable monster commits ([http://www.crealytics.de/blog/2010/07/09/5-reasons-keeping-git-commits-small-mluedtke/ a known worst practice]), you will need third-party programs to prepare any non-trivial set of patches.

One such third-party program is called [[Git]]... While Git is usually meant to be used as a standalone version control system (and we have hints [[Git Notes|here]] and links [[Git|here]] how to use it), its [[Git topic branches|<code>git rebase -i</code>]] functionality lends itself to a patch series based workflow.

== The <code>git svn</code> workflow ==

Our recommended <code>git svn</code> workflow was described in our chatroom by [[User:Bdezonia|Barry]]:

<ol>
<li><code>git svn fetch</code></li>
<li><code>git checkout -b NewBranch trunk</code></li>
<li>&lt;do some edits and test, git adds, git commits, etc.&gt;</li>
<li><code>git svn fetch</code></li>
<li><code>gitk ...trunk</code>
<ul>
<li>&lt;if not linear development then&gt;<br />
<code>git rebase -i trunk</code></li></ul>

&lt;finally&gt;</li>
<li><code>git svn dcommit</code></li></ol>

The idea is to first synchronize the local branches with the the Subversion repository (step 1).

Then start and work on a new topic branch (steps 2 &amp; 3). This may involve heavy rewriting and even sharing the branch with other developers just as you are wont from [http://schacon.github.com/git/gitworkflows.html regular Git workflows].

When you are ready to publish the patch series in Subversion, synchronize again (step 4) and make sure that no merge commits are present on top of Subversion's ''trunk''. This is necessary because <code>git svn</code> can really only apply a number of patches, it cannot create merge commits. Should there be non-linear development, use Git's <code>rebase</code> command to linearize it.

After everything was prepared for Subversion, use the <code>dcommit</code> command of <code>git svn</code> to commit all changes that are in the current branch but not yet in ''trunk''. (If you are interested why it is called <code>dcommit</code>: the original <code>commit</code> subcommand of <code>git svn</code> is a historic wart...)

== Setting up the local working directory ==

To get started with <code>git svn</code>, you need an initial <code>git-svn</code> clone. The easy way to do this would be to start

<code>git svn clone -s https://code.imagej.net/svn/imagej</code>

However, this is relatively slow since it uses Subversion to check out every revision in the complete history. You can instead hook up a fresh Git working tree with our pre-imported Git repository like this:

<ol>
<li><code>git init</code></li>
<li><p>add these sections to the .git/config file<br />
</p>
<pre>[remote &quot;origin&quot;]
        url = git://code.imagej.net/imagej.git
        pushURL = git@code.imagej.net:imagej.git
        fetch = +refs/heads/*:refs/remotes/origin/*
        fetch = +refs/heads/svn/*:refs/remotes/*
[svn-remote &quot;svn&quot;]
        url = http://code.imagej.net/svn/imagej
        fetch = trunk:refs/remotes/trunk
        branches = branches/*:refs/remotes/*
        tags = tags/*:refs/remotes/tags/*</pre></li>
<li><code>git fetch</code></li>
<li><code>git svn fetch</code>  (this step takes some time...)</li>
<li><code>git checkout -b master -t trunk</code></li></ol>

Explanation: rather than letting <code>git svn</code> do its job from the get go, we first initialize the ''origin'' remote (steps 1 to 3). It is initialized such that the Subversion branches -- which our Git repository exposes in the ''svn/*'' namespace -- are fetched into the place where <code>git svn</code> will pick them up rather than going through the tedious multi-hour process of any bootstrap <code>git svn</code> import.

In step 4, <code>git svn</code> indeed picks up those pre-imported branches.

Lastly, we initialize the local ''master'' branch to track Subversion's ''trunk''.

[[Category:News]]
[[Category:ImageJ2]]
