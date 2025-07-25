---
title: Pinpoint regressions with Git
section: Extend:Development:Git
---

# How to bisect with Git

## How to find which commit introduced a regression

So you found a regression? I.e. you know that the version worked perfectly that you had yesterday of, say, the [ImageJ Ops](/libs/imagej-ops) library, but today it crashes?

Git-bisect to the rescue!

```shell
git bisect start
git bisect bad HEAD
git bisect good HEAD@{yesterday}
```

This will start the bisection process, i.e. it will try to find a revision that is as much "in the middle" between the bad commit(s) and the good commit(s) (you will mark more and more commits as good or bad in the process, and by inference, the ancestors of good commits will be considered good, and the offspring of bad commits will be considered bad, too), and let you test that.

In our case, let's just run the unit tests:

```shell
mvn clean test
```

If the test is undecided (e.g.: it does not compile, so you do not know if the unit test in question passes), mark it with

```shell
git bisect skip
```

otherwise, mark it as "bad" or "good".

Sooner or later (usually rather sooner), Git will tell you which commit is the culprit. You can look at the corresponding patch with

```shell
git show <commit name>
```

where the commit name is that 40-digit hex string Git told you was the first bad commit. Usually you end the bisection process then and there:

```shell
git bisect reset
```

This will bring you back to the revision and branch you were on before starting the bisection.

## How to forward port a fix

If there is an obvious flaw in the patch, just try to patch it. You have to move to the first bad revision first:

```shell
git checkout <commit name>
```

(This will warn you that you are not on any branch, but that is okay.) Then just apply the fix you have in mind, and commit (after making sure that it worked, of course ;-). Now, tag it with a temporary label:

```shell
git tag my-fix
```

and go back to the branch you came from:

```shell
git checkout main
```

If you are unsure which branch you came from, look at the [reflog](/develop/git/reflogs) first.

Now you can cherry-pick (or forward-port) your patch:

```shell
git cherry-pick my-fix
```

If there are conflicts, resolve them and commit ("git commit fiji.cxx").

After that, you can get rid of the now-obsolete tag:

```shell
git tag -d my-fix
```

Note: instead of using a temporary tag, you can use the [reflog](/develop/git/reflogs) of the HEAD ref (`git cherry-pick HEAD@{1}`), but if you are not familiar with the concept, tags are probably easier to handle.

# See also

-   [Binary search tutorial](http://git-scm.com/book/en/v2/Git-Tools-Debugging-with-Git#Binary-Search) in the Git book
