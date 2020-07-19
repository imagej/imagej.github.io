{{GitMenu}}
Here are some common git operations for which we often find ourselves searching.

== Workflow ==

=== Checkout a remote branch 'develop' and keep it linked to the origin ===

<source lang="bash">git checkout -t origin/develop</source>
It should report: "Branch develop set up to track remote branch develop from origin."


=== List all branches (both local and remote) ===

<source lang="bash">git branch -a</source>

=== List local branches and their corresponding upstream remote branches ===

<source lang="bash">git branch -vv</source>

=== Revert local changes to a file (prior to commit) ===

<source lang="bash">git checkout file</source>

=== Revert all local changes to the current subtree (prior to commit) ===

<source lang="bash">git checkout .</source>

=== Cute hack to revert all local changes (prior to commit) ===

<source lang="bash">git stash git stash drop</source>

=== Undo a commit ===

<source lang="bash">git reset --soft HEAD^</source>

=== Undo multiple commits ===

<source lang="bash">git reset --soft HEAD@{2}</source>
Where <code>2</code> is the number of commits to undo.


=== Update to latest HEAD, preserving local changes and local commits on top ===

<source lang="bash">
git stash
git pull --rebase
git stash pop
</source>

=== Push changes on master to origin ===

<source lang="bash">git push origin master</source>

=== Delete untracked files and directories ===

<source lang="bash">git clean -df</source>

=== Interactively stage patches from changed file(s) ===

<source lang="bash">git add -p &lt;path&gt;</source>

=== Roll back the last commit's changes to a particular file ===

<source lang="bash">git checkout HEAD@{1} -- file</source>

== Branches ==

=== Branch master to a new local branch "new_branch" ===

<source lang="bash">git checkout -b new_branch master</source>

=== Push local branch to remote ===

<source lang="bash">git push -u origin new_branch</source>

=== Make the current local branch start tracking a corresponding remote branch ===

<source lang="bash">git branch --set-upstream-to origin/new_branch</source>
This is not necessary if you used <code>git push -u</code> as suggested above.

=== List the local branches that have already been merged to this one ===

<source lang="bash">git branch --merged</source>

=== Diff a file between two branches ===

<source lang="bash">git diff branch1 branch2 -- file</source>

=== Delete a branch both locally and remotely ===

<source lang="bash">
git branch -rd origin/branch_to_kill
git branch -d branch_to_kill
git push origin :branch_to_kill
</source>

=== Move a commit from bad_branch to good_branch ===

<source lang="bash">
# First cherry-pick the commit onto the correct branch:
git checkout good_branch
git cherry-pick deadbeef

# Then remove the commit from the bad branch:
git checkout bad_branch
git rebase -i
# Change the undesirable commit to "noop"
</source>
For more on branching, see [[Git topic branches]].


=== Rename the current branch ===

<source lang="bash">git branch -m <new branch name></source>

== Git + SVN ==

=== Clone an SVN repository to a local Git repository ===

<source lang="bash">git svn clone -s http://svn.code.sf.net/p/jhotdraw/svn/</source>

=== Commit and push changes, even with local changes in the working copy ===

<source lang="bash">git commit git stash git svn dcommit git stash pop</source>

=== Update to latest trunk, preserving local changes and local commits on top ===

<source lang="bash">git stash git svn rebase git stash pop</source>

== Searching ==

=== Recursively search for HelloWorld.file (and display the most recent commit modifying it) ===

<source lang="bash">git ls-tree -r HEAD | grep HelloWorld.file</source>

=== Recursively search for all files containing the phrase 'import HelloWorld' ===

<source lang="bash">git grep 'import HelloWorld'</source>

=== Recursively search for all files ''in any topic branch'' containing the phrase 'import HelloWorld' ===

<source lang="bash">git grep 'import HelloWorld' $(git rev-list --all --no-walk)</source>

== History ==

=== Display a log with colored word diffs ===

<source lang="bash">git log -p --color-words</source>
Add <code>-S</code> to <code>less</code> to virtually wrap long lines.


=== Display a diff with colored words between a file in one commit and a file in another commit ===

<source lang="bash">git diff <commitA>:<file> <commitB>:<file> --color-words</source>
Add <code>-S</code> to <code>less</code> to virtually wrap long lines.


=== Display all contributing authors of a project including their e-mail ===

<source lang="bash">git log --format='%aN <%ae&>' | sort -u</source>
Respects <code>.mailmap</code>.


=== Viewing the history for a single file ===

<source lang="bash">git log --follow HelloWorld.file</source>
This history is algorithmically calculated and must be carefully preserved.

Simultaneous (within a single commit) significant changes + file renaming (including relocation) can prevent the algorithm from successfully tracing the file's history, or cause it to begin tracing the wrong file.

Keeping code changes separate from renames should prevent this confusion, but it is good practice to check <code>log --follow</code> before pushing to a remote repository.


=== See commits in branch B not present in branch A ===

There are two main options. The first:
<source lang="bash">git log A..B</source>
will display the different commits in full git log format. NB: the <code>..</code> between commits is important to sure only the difference in commits is considered.

The second:
<source lang="bash">git cherry -v A B</source>
will display a simple list of the different commits, one per line, with commit message and hash.


== Scripts ==

There are some Git-related scripts available in the [https://github.com/scijava/scijava-scripts scijava-scripts] project.


=== List information about all remote branches including last author, commit date and unmerged commit count ===

<source lang="bash">$SCIJAVA/bin/remote-branch-info.sh</source>

== Advanced and/or dangerous ==

=== Create a repository with g+w permissions ===

<source lang="bash">git init --shared=group</source>
Or for a bare repository:
<source lang="bash">git init --bare --shared=group</source>
(Bare repositories are meant for a remote server repository that all your coworkers push into and pull/fetch from.)


=== Push all remote branches from one remote (e.g., "origin") to another (e.g., "github") ===

<source lang="bash">
git push github $(git for-each-ref refs/remotes/origin | \
  grep -v HEAD | \
  while read sha1 type ref
  do
    echo $ref:refs/heads/${ref#refs/remotes/origin/}
  done)
</source>

=== Another way to push all remote branches between remotes ===

<source lang="bash">
eval git push github $(git for-each-ref | \
  sed -n 's/.*\t\(refs\/remotes\/origin\/\(.*\)\)$/\1:refs\/heads\/\2/p')
</source>

=== Fully garbage collect and compact the repository (deletes all orphaned refs!) ===

<source lang="bash">
git reset --hard git for-each-ref --format="%(refname)" refs/original/ | \
  xargs -n 1 git update-ref -d git reflog expire --expire=now --all git gc --aggressive --prune=now
</source>

== Rewriting history ==

=== Split a subdirectory into a separate git repository ===

See these posts on Stack Overflow:
* [http://stackoverflow.com/questions/359424/detach-subdirectory-into-separate-git-repository Detach subdirectory into separate Git repository]
* [http://stackoverflow.com/questions/6638019/detach-subdirectory-that-was-renamed-into-a-new-repo Detach subdirectory (that was renamed!) into a new repo]
* [http://stackoverflow.com/questions/3910412/split-large-git-repository-into-many-smaller-ones Split large Git repository into many smaller ones]


=== Throw away git-svn-id metadata ===

<source lang="bash">git filter-branch --msg-filter ' sed -e "/^git-svn-id:/d" '</source>

=== Combine the first two commits of a Git repository ===

See this post on Stack Overflow:
* [http://stackoverflow.com/questions/435646/how-do-i-combine-the-first-two-commits-of-a-git-repository How do I combine the first two commits of a Git repository?]


=== Change the author of a commit ===

<source lang="bash">git commit --amend --author="Author Name"</source>

=== Change the author of many commits ===

See this post on Stack Overflow:
* [http://stackoverflow.com/questions/750172/how-do-i-change-the-author-of-a-commit-in-git How do I change the author of a commit in git?]


=== Merge multiple repositories ===

See these posts on Stack Overflow:
* [http://stackoverflow.com/questions/277029/combining-multiple-git-repositories Combining multiple git repositories]
* [http://stackoverflow.com/questions/4039682/git-retroactively-introduce-several-merges git: Retroactively introduce several merges]


== Tutorials ==

=== Creating a shared remote repository ===

<source lang="bash">
ssh you@server
mkdir repos/remote.git
cd repos/remote.git
git --bare init --shared=group
logout

cd ~/local
git remote add origin ssh://you@server/home/you/remote.git
git push origin master
git config branch.master.remote origin
git config branch.master.merge refs/heads/master
</source>
Creates a bare remote repository at <code>ssh://server/home/you/remote.git</code> that tracks your local repository in <code>/home/you/local</code>. Adopted from [http://toolmantim.com/articles/setting_up_a_new_remote_git_repository Tim Lucas].

=== Displaying a filtered set of commits ===

Assume you want to see commits in branch <code>stephan</code>, but only those that are <u>not</u> part of the history of branch <code>saalfeld</code>:

<source lang="bash">git log stephan ^saalfeld</source>
More realistically, if you want to see all the commits which are in a topic branch, but not yet merged into master:

<source lang="bash">git log --all ^master</source>
If you want to see the changes which come from a topic branch which was merged in commit <code>deadbeef</code>, use this command line:

<source lang="bash">git log deadbeef^..deadbeef^2</source>
Explanation: <code>deadbeef</code> is a merge commit, so its first parent (<code>deadbeef^</code>, can also be written as <code>deadbeef^1</code>) was the current <code>HEAD</code> when the merge was performed, and the second parent (<code>deadbeef^2</code>) is the tip of the branch which was merged. The argument <code>A..B</code> is short form of <code>^A B</code>, i.e. all commits reachable from <code>B</code> excluding those which are also reachable from <code>A</code>.

[[Category:Git]]
