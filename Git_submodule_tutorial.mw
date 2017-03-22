{{GitMenu}}{{TOC}}{{Outdated}}

== Submodules in Fiji ==

<p>Fiji is hosted on a main git repository which contains several declared submodules such as TrakEM2.</p>

<p>With git, any git command executed within any subdirectory of the repository affects the overall git repository.</p>

<p>Submodules, although existing as folders inside the fiji repository, are different: only the folder name, as a path pointer, is registered as belonging to fiji's git repository, together with the current revision ("commit name", i.e. that 40-digit hex string which is the unique identifier of each commit) of that submodule.</p> 

=== Checking out submodules ===

<p>Each submodule is a proper full-fledged git repository, so any git commands executed within the folders of the submodule will affect that git repository, not fiji's.</p>

<p>However, to work with a submodule you must clone that repository. See the [[Downloading and Building Fiji From Source#Submodules|Submodules]] section of the [[Downloading and Building Fiji From Source]] page for details.</p>

=== Submodule workflow ===

<p>The usual sequence of commands when working inside a submodule:</p>

<pre>
~/fiji$ cd TrakEM2
~/fiji/TrakEM2$ git status
</pre>

<p>Say you observe some unstaged changes. Just add and commit them:</p>

<pre>
~/fiji/TrakEM2$ git add path/to/some_file.java
~/fiji/TrakEM2$ git commit
</pre>

<p>You can work as much as you like inside the submodule, and if you have something you want to commit to Fiji, the superproject, first make sure you pushed the changes of the submodule!</p>

<p>Then move up and add the current revision of the submodule inside fiji.</p>

<pre>
~/fiji/TrakEM2$ git push
~/fiji/TrakEM2$ cd ..
~/fiji$ git add TrakEM2
~/fiji$ git commit
</pre>

<p><b>BE CAREFUL:</b> adding "TrakEM" and "TrakEM/" is not the same at all! The latter would add all non-ignorable files under TrakEM2's subfolder into fiji's repository, which is NOT what you want. If you screwed up, use <i>"git reset --hard"</i> before proceeding to unstage any changes in fiji's git repository.</p>

<p>After the above, fiji has been updated to track the latest TrakEM2 commit.</p>

<p>When happy with the arrangement, push the changes to the shared repository for others to see them. Remember to push both separately: the submodule and fiji's repository itself! If you push <b>only</b> fiji, then whoever pulls fiji will not see the new HEAD of the submodule branch, which will result in an error.</p>

<pre>
~/fiji$ cd TrakEM2/
~/fiji/TrakEM2$ git push
~/fiji/TrakEM2$ cd ..
~/fiji$ git push
</pre>

== Resolving Submodule Conflicts ==

When merging and rebasing fiji, you are likely to end up having to fix conflicts in the versions of submodules.  These next two sections are intended to help you to resolve these conflicts.

=== Submodule Conflicts while Merging ===

You are most likely to have submodule conflicts while merging when you run "git merge" or "git pull" (which effectively runs "git fetch" followed by "git merge"). How to resolve those conflicts can be read on the [[Git_Conflicts#Submodule_conflicts|Git Conflicts]] wiki page.

=== Submodule Conflicts while Rebasing ===

Conflicts in submodule versions while you're rebasing are slightly different.  For example, suppose I am in the following situation:

 o---o----o----o----o master
  \
   A----B----C-----D----E----F server

And I want to rebase server onto master, by doing the following:

 git checkout server
 git rebase -i master

The "-i" option means that I am first presented with a list of commits to port onto master, named A, B, C, D, E and F in the above diagram.  After possibly making some changes (there may be some commits that you don't actually want to include in the rebased version) the rebasing begins.  The first error I get is the following:

 Automatic cherry-pick failed.  After resolving the conflicts,
 mark the corrected paths with 'git add <paths>', and
 run 'git rebase --continue'
 Could not apply 1f7b713... Various changes to make the server work better

If you get a message saying you have to resolve conflicts that means that "git status" will tell you what they are.  In this case I get:

 VIB: needs merge
 # Not currently on any branch.
 # Changes to be committed:
 #   (use "git reset HEAD <file>..." to unstage)
 #
 #	modified:   run-server.sh
 #	deleted:    server-init.d-script
 #	modified:   staged-plugins/VIB_.config
 #
 # Changed but not updated:
 #   (use "git add/rm <file>..." to update what will be committed)
 #   (use "git checkout -- <file>..." to discard changes in working directory)
 #
 #	modified:   ImageJA
 #	modified:   TrakEM2
 #	unmerged:   VIB
 #	modified:   java/linux
 #	modified:   java/linux-amd64
 #	deleted:    mpicbg
 #
 # Untracked files:
 #   (use "git add <file>..." to include in what will be committed)
 #
 [... various irrelevant untracked files ...]

In this case, there's only one problem: versions of the VIB submodule conflict.

Let's say that the situation now corresponds to the following diagram:

                      A'---B' HEAD
                     /
 o---o----o----o----o master
  \
   A----B----C-----D----E----F server ORIG_HEAD

First, it's important to see what change in version that commit is trying to make, so take the partial SHA1 sum from the line "Could not apply" above and pass it to git show, so "git show 1f7b713".  This shows the patch introduced by that commit, but we're only looking out for the lines relating to the VIB submodule, which are:

 diff --git a/VIB b/VIB
 index c03c2cc..b6d78c8 160000
 --- a/VIB
 +++ b/VIB
 @@ -1 +1 @@
 -Subproject commit c03c2cc7d150087d91879012e1b312e3b2957733
 +Subproject commit b6d78c8c390072d89059956d4d3596114c6301f1

Now just to check that we understand what's going on, run three versions of the diff command.  First, show differences between the the last successful commit in this rebase and the working tree version:

  git diff --base VIB
 * Unmerged path VIB
 diff --git a/VIB b/VIB
 index c03c2cc..764f65b 160000
 --- a/VIB
 +++ b/VIB
 @@ -1 +1 @@
 -Subproject commit c03c2cc7d150087d91879012e1b312e3b2957733
 +Subproject commit 764f65baee6af310cac4879a52805d7bffcd4dd0

That shows us that the version in the old commit is as we expect (good!)  The version in the "+" line is what's in our working tree, or what you'll see if you do "( cd VIB && git show HEAD )".  So, in this case I think it's a good idea to switch VIB to be the version that the commit we're cherry-picking tried to introduce, i.e. b6d78c8c390:

 ( cd VIB && git checkout b6d78c8c390 )
 git add VIB

Now we should be able to continue, with "git rebase --continue" 

==== A note on "ours" and "theirs" ====

If you're using "git diff --theirs" and "git diff --ours" while rebasing then you may get confused.  Essentially:

* "git diff --theirs" shows the differences between the "server" branch and the working tree.
* "git diff --ours" shows the differences between the "master" or "upstream" branch and the working tree.

This is probably the opposite way round from what you expect from resolving conflicts while merging :)

== Difference between git submodule update and git pull  ==
What is the difference between calling git supmodule update from the fiji directory and changing into a submodule directory and doing a git pull? 

Most of the time you do not want to have the newest coolest version of the submodule.. You want the version that actually works with your status of fiji. Therefore, a commit of a superproject also contains the name of the submodule directories, along with the current commit of these submodules.

Now

  git submodule update

sets the submodule to the commit that is saved with the commit of fiji. 
Whereas

  cd submoduleDirectory/
  git pull

actually gives you the newest hottest version of that submodule, that is potentially not even compiling with your current status of fiji.

So what happens if I do "git submodule update", but in the submodule I am on an experimental branch, that is not valid for the superproject?
This will set the submodule to the status valid for your current fiji commit, if you are not on the branch specified, it will detach the HEAD you are on. This means you will be on a no-name branch in the submodule now (for this to work you must not have any uncommited changes in the submodule branch you were on before)



[[Category:Git]]
