{{GitMenu}}
{{Outdated}}
This page is a '''really''' quick 'n dirty tutorial on how to work with Git.  It is strongly biased to the work on Fiji; you should refer to [[Git workshop]], [[Git for dummies]] or to [https://git-scm.com/ Git's homepage] for much more information.

Most of these explanations are meant for the command line users.

== Nomenclature ==

A quick note on the nomenclature: ''fiji.git'' refers to the "official" repository on [https://github.com/fiji/fiji.git].  After cloning it, you will have a local repository with a working directory, which will be referred to as "fiji/" in this document (and "cd fiji/" just tells you to make sure you are in that directory).

If you are unsure about the meaning of any Git term, just consult the [http://git.or.cz/gitwiki/GitGlossary Git glossary].

= Cloning =

You need to clone ''fiji.git'':

 $ git clone git://fiji.sc/fiji.git/

= Contributing =

All contributions should go through GitHub [https://help.github.com/articles/using-pull-requests/ pull request]

= Local configuration =

You need to make sure that Git knows who you are (substitute your name/email here...):

 $ git config --global user.name "General Failure"
 $ git config --global user.email "general@failure.harddrive.org"

Likewise, if your preferred editor is not ''vi'', you might want to do something about that (substitute your pet editor here...):

 $ git config --global core.editor xemacs

= Updating =

To get the most recent changes, call

 $ cd fiji/
 $ git pull

Note: You should always commit your changes before pulling.

= Running Fiji =

A simple

 $ cd fiji/
 $ sh Build.sh run

will pick up on all changes, rebuild what needs to be rebuilt, and run Fiji.

= Making changes =

You can [[Adding_plugins_with_source|add/modify plugins]], and test by running "make".

Once you are happy with your changes, you should inspect your changes with

 $ cd fiji/
 $ git status

which will show you which tracked files were modified, and the untracked files (which might need to be added to the Git repository).  You can view the diff of your changes with

 $ cd fiji/
 $ git diff

You should stage the changed/new files for commit, and verify that all files were correctly staged, with:

 $ cd fiji/
 $ git add <files>
 $ git status

If all files that need committing were staged correctly, you commit them:

 $ cd fiji/
 $ git commit

Please make sure that your commit message is in a format like this:

 The first line is a short description
 
 After an empty line, you can go into details what this commit does, and why.  Maybe even how.

Note: a neat trick when you realize that you did not commit after all, is to delete the ''complete'' commit message, save and exit.  This will abort the commit.  The ability to abort a commit comes in pretty handy e.g. when you see an unwanted entry in the list of files to be committed.

For more advanced Git usage, see "Making changes (advanced)".

= Pushing changes upstream =

All commits are purely local before you decide to publish them.  You might want to check first what you are going to publish before actually doing that (assuming a branch name "contrib"):

 $ cd fiji/
 $ git fetch contrib
 $ gitk contrib/contrib..

(Note that the commits in the gitk window are ordered chronologically, most recent is the top-most, and please also note that the commits marked with a hollow circle on the left side are so-called "boundary" commits, i.e. commits that are already upstream).

Now you can publish your changes with

 $ cd fiji/
 $ git push contrib HEAD:contrib

Note: if somebody made changes to the branch in the mean-time, you need to pull first:

 $ cd fiji/
 $ git pull contrib contrib
 $ git push contrib HEAD:contrib

'''Note''': there might be [[Git Conflicts|merge conflicts]] that you need to [[Git_Conflicts#Resolving_merge_conflicts|resolve]] before pushing.

'''Note for CVS/Subversion users''': With Git, it is highly encouraged to commit '''first''', '''then''' pull.  Git is really good at branching and merging, and it is better for you to commit a version that you actually tested than to integrate other people's changes before committing.  It also helps [[Git_bisection|finding which commit introduced a regression]].

= Graphical user interfaces =

There are a few graphical user interfaces for working with Git.  You probably want to look at the commit history with ''gitk'', and you might want to clone/pull/add/commit/push with ''git gui''.

If you are an Eclipse user, you might want to work with the [http://git.or.cz/gitwiki/EclipsePlugin?highlight=(eclipse) Eclipse plugin].

= Making changes (advanced) =

Git is aware of three states:

* the tip of the branch (AKA the last committed version, or "HEAD")
* the staging area (also called "the index")
* the working directory

Instead of staging whole files, you can pick just a few changes to be staged:

 $ cd fiji/
 $ git add -i

This will let you choose single hunks from the unstaged changes and put them into the staging area.  It also allows you to revert to the version stored 

In ''git-gui'', you can do the same by clicking on the file and then choose ''Stage this hunk'' or ''Unstage this hunk'' from the context menu you get by right-clicking on the hunk header (the line beginning with ''@@'').

You can inspect what changes are in the staging area with:

 $ cd fiji/
 $ git diff --cached

When you are comfortable with the staged changes, just commit with

 $ cd fiji/
 $ git commit

Even more advanced Git usage involved [[Git_topic_branches|topic branches]].

[[Category:Git]]
