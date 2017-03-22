{{GitMenu}}
= Git's reflogs =

== What is a "ref"? ==

In Git, a "ref" is a pointer into the commit graph (to visualize the commit graph, use the wonderful tool ''gitk''.

Branches are implemented as refs ("refs/heads/master"), tracking branches, too ("refs/remotes/origin/master"), and tags ("refs/tags/v1.0").  The convention is that tags do not move (advance), while branches do.  These named refs are also referred to as ''symbolic refs''.

As long as they are unambiguous, you can abbreviate symbolic refs by omitting the "refs/heads/", "refs/remotes/" and "refs/tags/" prefixes.

Each commit has a unique identifier, the 40-digit hex string also known as the ''commit name''.  Since each commit knows about its parents, by inference the commit name refers to the whole history of that commit, not just the commit itself.  Commit names are the most basic type of refs.

Often, it is cumbersome to write out the whole 40-digit hex string, but you can use an abbreviation of it, as long as it is unique (i.e. as long as there is no other object with the same name).  Typically, you take 8 digits for that.  Example: d4326e921b226639aae7dfbf8d24b934714e60d2 can be abbreviated as d4326e92.

There are a few special refs, which are upper-case by default:

* HEAD: this is a pointer to the current branch, i.e. it points to something like "refs/heads/master", usually.

* ORIG_HEAD: when pulling or merging, ORIG_HEAD refers to the previous revision.

* FETCH_HEAD: when pulling or fetching, the fetched ref is stored in FETCH_HEAD.  Note: if you use the convenient "git pull" without argument, chances are that FETCH_HEAD contains more than one ref, and it is not really useful.

And then, there are reflogs.

== Reflogs ==

As mentioned, commits contain the whole history leading to that commit by inference.

But there is another history that is often pretty useful: the history, as seen by the _local_ repository.  For example, if you did not work on Sunday, but someone else did, and you pull the changes on Monday, you can get a commit that changed the project on Sunday, 1:00pm, possibly many (if two people worked on the project, and one merged the other's changes).  But there is _exactly_ one state your current local repository was in, on that Sunday, at 1:00pm.

This type of history is called ''reflog'', and it is purely linear (at least until we can travel backwards in time, that is).

To see the reflog of a ref, just call

<pre>
~/fiji$ git reflog show master
</pre>

or

<pre>
~/fiji$ git reflog show HEAD
</pre>

As a convenience, "git reflog" without parameters shows the reflog of HEAD.

As a further convenience, you can convince "git log" to show the reflog history instead of the "true" history, by calling it with the parameter "-g":

<pre>
~/fiji$ git log -g
</pre>

The reflog entries are refs, which have the form "HEAD@{0}", "HEAD@{1}", etc. where the number 0 means the current revision, 1 the previous, and so on.

But reflogs know more than just the ordering: they know the date, too.  Just try this:

<pre>
~/fiji$ git log -g --date=relative
</pre>

It will show you something like

<pre>
commit 28b4fbcc8ba45996fa2c9b660e13f309443b55bd
Reflog: HEAD@{23 hours ago} (Johannes Schindelin <johannes.schindelin@gmx.de>)
Reflog message: pull : Fast forward
Author: Johannes Schindelin <johannes.schindelin@gmx.de>
Date:   23 hours ago

    Add a Makefile target to create a .dmg file

    For the moment, this script only works on MacOSX :-(

    Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

commit e73abb095c1905063c22d3977433edaaa1e5dac9
Reflog: HEAD@{23 hours ago} (Johannes Schindelin <johannes.schindelin@gmx.de>)
Reflog message: pull : Fast forward
Author: Johannes Schindelin <johannes.schindelin@gmx.de>
Date:   23 hours ago

    check-class-versions: do not delete the temporary macro file

    check-class-versions creates a temporary macro file which is then
    executed in headless mode.  However, when falling back on MacOSX,
    it was deleted before ImageJ saw it.

    Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

commit 433a55259e0b105420263c433a370ef5423d1976
Reflog: HEAD@{26 hours ago} (Johannes Schindelin <johannes.schindelin@gmx.de>)
Reflog message: merge origin/contrib: Fast forward
Author: Johannes Schindelin <johannes.schindelin@gmx.de>
Date:   27 hours ago

    Fix crash on Win32

    When making the error reporting better, a bug slipped in which led to
    NULL being dereferenced.  This commit fixes that.

    Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

...
</pre>

So you can also refer to the reflog with something like "HEAD@{1 day ago}".  For convenience, you can replace the spaces with dots so you do not have to quote the parameter.

Reflogs are pretty useful to refer to commits when [[Git_bisection|bisecting]]: you might happen to know that something worked two weeks ago ("git bisect good HEAD@{2.weeks.ago}", but stopped working in the current revision: ("git bisect bad HEAD").

[[Category:Git]]
