{{GitMenu}}
= How to bisect with Git =

== How to find which commit introduced a regression ==

So you found a regression?  I.e. you know that the version worked perfectly that you had yesterday of, say, the [[ImageJ Ops]] library, but today it crashes?

Git-bisect to the rescue!

<source lang="bash">
git bisect start
git bisect bad HEAD
git bisect good HEAD@{yesterday}
</source>

This will start the bisection process, i.e. it will try to find a revision that is as much "in the middle" between the bad commit(s) and the good commit(s) (you will mark more and more commits as good or bad in the process, and by inference, the ancestors of good commits will be considered good, and the offspring of bad commits will be considered bad, too), and let you test that.

In our case, let's just run the unit tests:

<source lang="bash">
mvn clean test
</source>

If the test is undecided (e.g.: it does not compile, so you do not know if the unit test in question passes), mark it with

<source lang="bash">
git bisect skip
</source>

otherwise, mark it as "bad" or "good".

Sooner or later (usually rather sooner), Git will tell you which commit is the culprit.  You can look at the corresponding patch with

<source lang="bash">
git show <commit name>
</source>

where the commit name is that 40-digit hex string Git told you was the first bad commit.  Usually you end the bisection process then and there:

<source lang="bash">
git bisect reset
</source>

This will bring you back to the revision and branch you were on before starting the bisection.

== How to forward port a fix ==

If there is an obvious flaw in the patch, just try to patch it.  You have to move to the first bad revision first:

<source lang="bash">
git checkout <commit name>
</source>

(This will warn you that you are not on any branch, but that is okay.)  Then just apply the fix you have in mind, and commit (after making sure that it worked, of course ;-).  Now, tag it with a temporary label:

<source lang="bash">
git tag my-fix
</source>

and go back to the branch you came from:

<source lang="bash">
git checkout master
</source>

If you are unsure which branch you came from, look at the [[Git_reflogs|reflog]] first.

Now you can cherry-pick (or forward-port) your patch:

<source lang="bash">
git cherry-pick my-fix
</source>

If there are conflicts, resolve them and commit ("git commit fiji.cxx").

After that, you can get rid of the now-obsolete tag:

<source lang="bash">
git tag -d my-fix
</source>

Note: instead of using a temporary tag, you can use the [[Git_reflogs|reflog]] of the HEAD ref (<code>git cherry-pick HEAD@{1}</code>), but if you are not familiar with the concept, tags are probably easier to handle.

= See also =

* [http://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git#Binary-Search Binary search tutorial] in the Git book

[[Category:Git]]
