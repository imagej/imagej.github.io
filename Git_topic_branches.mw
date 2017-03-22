{{GitMenu}}
Often you want to try some new idea, or work on some new feature, without interfering with the master branch.  That is where topic branches come in.  You can easily switch back and forth between branches, so that you do not need to contribute a new feature with one big "monster" commit.

If you want to try something that might not work out, and you do not want anybody to know in such a case, you can keep the topic branches local.

= Creating a topic branch =

You can create a topic branch from any starting point like this:

 $ git checkout -b new-branch branch-point

The argument ''branch-point'' can be any commit, or tag.  If you want to branch off from the current HEAD, you do not need to pass the argument at all:

 $ git checkout -b topic1

'''Note''': if you want to start a new branch from a remote (AKA tracking) branch, this command will also set up default merge to be from that remote with that branch:

 $ git checkout -b fake2 origin/fake2
 ...
 $ git pull

will pull the branch ''fake2'' from ''origin'' into the current (''fake2'') branch.

= Switching between branches =

To switch from the current branch to another, first make sure that you have committed (or stashed) everything, and then call

 $ git checkout other-branch

This will switch to another branch (which now becomes your HEAD), and update the working directory.  Note: only the tracked files will be updated; the untracked files will be untouched.

= Cherry-picking commits =

If you have a single commit on another branch that you would like to have in the current branch, use

 $ git cherry-pick other-branch~2

In this example, the third-last commit (the 2nd order ancestor) of other-branch's tip was referenced.

Cherry-picking comes in handy if you fix something in a topic branch which needs fixing in the master branch, too:

 # current branch: topic234
 ... fix bug ...
 # git commit -s <file>
 $ git checkout master
 $ git cherry-pick topic234
 $ git checkout topic234

In this example, after fixing the bug and committing the bug fix, you switched to the branch ''master'', cherry-picked the most recent commit on the branch ''topic234'' and then switched back to the branch ''topic234''.

== Resolving conflicts ==

Note: when cherry-picking commits, conflicts can arise.  These are marked with conflict markers ("<<<" ... "===" ... ">>>").

You will have to edit the files, picking what changes you want (the first part is what the version is in the current branch, the second part is what the cherry-picked commit wanted to introduce). See [[Git Conflicts]] for details how to resolve the merge conflicts.

After editing the files, stage them for commit and commit, with

 $ git add <file>...
 $ git commit

In case of a failed cherry-pick/rebase, this will pick up the appropriate commit message for you.

= Merging/Rebasing topic branches =

If you finished a topic, and want to bring the changes to the branch ''master'', just switch to that branch and merge the topic branch:

 $ git checkout master
 $ git merge topic234

Just like cherry-pick, a merge can fail with conflicts.  See [[Git_topic_branches#Resolving_conflicts|Resolving conflicts]] for details.

Instead of merging, you might want to rebase your topic branch on top of the current master.  To see what the difference between a merge and a rebase is, consider this history (left is older than right):

 - A - B - C - D - master
     \
       E - F - G - topic234

after merge:

 - A - B - C - D - master^ - master
     \                      /
       E - F - G - topic234

after rebase:

 - A - B - C - D - master - E' - F' - G' - topic234

In other words, all the commits in topic234 were rewritten as if they were created on top of the current tip of the ''master'' branch.

As you see, the branch ''topic234'' is rewritten, and does not share any interesting history with the former tip of the ''topic234'' branch.  (You can access the former tip with ''topic234@{1}'', see [[Git_reflogs]].)

So, to incorporate your topic branch into the ''master'' branch with a rebase, you would do the following:

 # current branch is topic234
 $ git rebase master
 $ git checkout master
 # this will fast-forward, i.e. not create a merge commit, but just move master's tip to topic234's tip.
 $ git merge topic234

Typically, merges should be preferred to rebases, because merges show the history better: after a rebase, the tip of the branch is basically untested, as you only tested the commits before they were rebased.

However, a rebase comes in pretty handy from time to time, especially if you want to rewrite commit history, as described in the next section.

= Advanced topic branch editing (AKA rebase on drugs) =

Often, a topic branch becomes a collection of nice commits and fixup commits, and maybe a few commits that are no longer necessary.  In such a case, you probably want to clean up the commit history a bit.  This is where the ''interactive'' rebase comes in.

Consider such a history (the first "word" is the abbreviated commit name):

 0470894... Untrack generated files
 e0acf90... Add Fake, a specialized yet simple substitute for 'make'
 047ad28... Fake: implement up-to-date test and use it in make()
 deadbee... fixup! Add Fake, a specialized yet simple substitute for 'make'

where ''0470894'' is the tip of the ''master'' branch, and ''deadbee'' fixes some severe issue in the commit ''e0acf90'', that should not have been committed as is.

Note that the ''fixup!'' commit can be made easily by calling ''git commit --fixup <commit-to-fixup>''.

To reorder the commits and merge the two commits (''squash'' in Git terminology, as ''merge'' already means to merge branches), call

<code lang="bash">
$ git rebase -i --autosquash master
</code>

This will fire up an editor with a list of commits to be applied on top of ''master'':

 pick e0acf90 Add Fake, a specialized yet simple substitute for 'make'
 fixup deadbee fixup! Add Fake, a specialized yet simple substitute for 'make'
 pick 047ad28 Fake: implement up-to-date test and use it in make()

Note that the ''autosquash'' mode interpreted the special commit message of the fixup commit, moved the last line and substituted the command "pick" (as in "cherry-pick") with "fixup".

Save that, and exit the editor.  The rebase will be started and amend the first commit with the fixup commit.

Note: If you want to default to the ''autosquash'' mode, you can tell Git so: ''git config --global rebase.autosquash true'' (you only need to do this once).

Note: as with cherry-picking and merging, conflicts can arise.  You will [[Merge_Conflicts|have to resolve them]], "git add" the resolved files, but you do not need to commit; calling

<code lang="bash">
$ git rebase --continue
</code>

will pick up the changes, apply the correct commit author and message, and fire up an editor for you to verify the contents.  As before, save and exit, and the rebase will continue.

== Aborting an interactive rebase ==

Sometimes you realize by the sheer size of the list of commits that you made a mistake, and do not want to rebase after all.  As with "git commit", just delete the ''complete'' list, and the interactive rebase will be aborted.

Even at later stages, e.g. when you have a huge conflict and would prefer to go back and merge instead of rebase, you can abort the rebase.  Just call

<code lang="bash">
$ git rebase --abort
</code>

and Git will bring you back to where you were before you started the rebase.

== Reflogs and rebases ==

A rebase will work on a ''detached'' HEAD.  In other words, while the rebase is in progress, no branch will be updated, but a temporary branch will grow, and only when the rebase is finished successfully, the originally current branch will be updated.

This means that you can refer to the state _before_ the rebase by "branch-name@{1}" (see [[Git_reflogs]]).

Note: the same is not true for "HEAD@{1}": the reflog for "HEAD" follows every single revision that was current at some stage in the repository.

[[Category:Git]]
