---
title: GitHub
section: Extend:Development:Tools
---

In the [ImageJ](/software/imagej) and related [SciJava](/libs/scijava) projects, we make extensive use of [GitHub](https://github.com/), a website that hosts [open source](/licensing/open-source) projects for free.

Here are a few tips how to interact via GitHub more effectively:

# Referring to source code

GitHub offers really powerful ways to refer to specific lines of code. And not only that, it also offers powerful ways to find those specific lines of code to begin with.

## Finding a file – quickly

After pointing the web browser to a specific repository, typing the {% include key key='T' %} key will let you type out parts of the file name and press {% include key key='Enter' %} when the file in question is at the top of the list (you can also navigate the list using the cursor keys).

## Linking to specific lines

Hitting the {% include key key='L' %} key lets you jump to a specific line (and modifies the URL which you can then send around to refer to that line).

After one line is selected already, you can select a line *range* by {% include key key='Shift' %}-clicking on the line number of the other end of the line range.

## Permalinks

After you found the link for the file in question, it most likely refers to the current version of the file.

However, once development advances, the file's contents might change in the meantime, or the file might even go away! To provide a link to a specific revision of the file, just press the {% include key key='Y' %} key to modify the URL to a permanent link (it will then reference the exact commit, instead of a branch).

## Ignore whitespace changes in diffs

Sometimes, a commit will mix whitespace changes with other changes, making the functional changes more difficult to isolate. Fortunately, there is an easy workaround:

-   On the command-line, Git [understands the `-w` flag](https://github.com/git/git/blob/v2.1.3/Documentation/diff-options.txt#L466-L470) to ignore whitespace changes.
-   GitHub provides the same functionality, too: just append `?w=1` to the URL (or `&w=1` if there are already GET parameters).

# Editing files

If you want to modify some file's contents and you are certain that the changes do not need to be tested locally, you can press the `Edit` button on the upper right corner after navigating to the file in question (in case you don't have *Push* permission on the repository in question, this will *fork* the project at the same time). This will let you edit the file online and commit the changes after providing a commit message (you should still try to write a [meaningful commit message](/develop/coding-style#scm-history), of course).

# Working with Pull Requests

Pull Requests are a really neat way to work together. The idea is that Git makes it very easy and efficient to clone a project's entire revision history, develop a bit, and then offer the improvements in a manner that is easy for the original project's developers to merge.

## Common workflow

Let's assume that you want to provide a fix for a vexing bug in one of your favorite [Fiji](/software/fiji) plugins. The first thing is to *fork* it – meaning to copy the entire revision history into your personal GitHub space – unless you have done so already. Then you clone that onto your computer (again, unless you have done so already). Make your changes, commit them, push them and then make a Pull Request. See the excellent page [How to contribute to an existing plugin or library](/develop/improving-the-code) for a detailed walk-through.

## Testing Pull Requests before merging them

GitHub makes it very, very easy to merge Pull Requests simply by pressing a button. Of course you should review the changes before you do so: remember that the quality of open-source software is high only because many developers throw their cumulative expertise together to make something that is better than each individual developer could have developed on their own.

You might even want to test the code locally before merging. This is really easy because GitHub provides not only the test whether a Pull Request can be merged cleanly, but it also offers the revision in the form of the `refs/pull/`<ID>`/merge` pseudo branches.

Please note that those pseudo branches (which are called *refs* in Git Speak) are not fetched or cloned automatically, they have to be fetch *explicitly*.

Example: let's assume for a moment that you want to test the [Pull Request number \#6 of the SPIM Registration plugin](https://github.com/fiji/SPIM_Registration/pull/6). You can fetch and check out the pseudo-branch with the tentative merge result thusly:

```shell
git fetch origin refs/pull/6/merge
git checkout FETCH_HEAD
```

Please note that

-   `FETCH_HEAD` is overwritten with every call to `git fetch`
-   `FETCH_HEAD` does not really refer to a branch, hence you will end up on an unnamed branch that is *not* updated when fetching
-   after testing, you should switch back to, say, *main* using `git checkout main`
-   once the Pull Request is merged, the pseudo-branch will reflect the final merge result, not a tentative one.

 
