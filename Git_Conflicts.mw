{{GitMenu}}
==Merge conflicts==
Sometimes you get ''merge conflicts'' when merging or pulling from a branch. Git will then tell you something like

 CONFLICT (content): Merge conflict in Fakefile

It also tells you to fix the conflicts and then to commit the result. So how to fix the conflicts?

== Resolving merge conflicts ==

First a little background: what is a merge conflict, and how does it happen? A merge conflict usually occurs when your current branch and the branch you want to merge into the current branch have diverged. That is, you have commits in your current branch which are not in the other branch, and vice versa.

Typically, there is one branch point, which is the latest common commit. This is the base commit.

Now, when Git merges the other branch into your current branch, it looks at the differences between the base commit and the current revision, and at the differences between the base commit and the other branch's latest commit. When there are unambiguous differences (i.e. only one side changed a certain piece of code), the changes are applied.

The merge conflicts occur when there are disagreeing changes. In that case, your conflicted file will have so-called ''conflict markers'':

 <<<<<<< HEAD
 my version
 =======
 the other version
 >>>>>>> deadbeef... This is the tip of the other branch

Between the ''<<<<<<<'' and ''======='', you will find the version as per the changes in your current branch, relative to the base commit.

Between the ''======='' and ''>>>>>>>'', you will find the version according to the other branch, relative to the base commit.

For convenience, after the ''<<<<<<<'' and ''>>>>>>>'' markers, you will see hints as to which commit that part of the conflict stems from, ''HEAD'' of course being the current revision.

To resolve the conflicts, you have to decide what the end result should be. This is not something you can do without thinking, otherwise Git would have done it for you.

For example, merge conflicts in ''.gitignore'' are often resolved by taking both the current version and the other version:

 <<<<<<< HEAD
 jars/VIB-lib.jar
 =======
 plugins/Gabriels_Plugin.jar
 >>>>>>> badcoffe... Add a new plugin to take over the world

could resolve into

 jars/VIB-lib.jar
 plugins/Gabriels_Plugin.jar

But beware: if lines were _removed_, you will have to resolve differently. For example,

 <<<<<<< HEAD
 jars/Blub.jar
 jars/some-lib.jar
 =======
 plugins/Blub.jar
 >>>>>>> abba123... Move Blub.jar to plugins/

might want to be resolved to

 jars/some-lib.jar
 plugins/Blub.jar

So you definitely need to think carefully about the resolution!

=== Submodule conflicts ===

The previous section talked about file conflicts. But of course, conflicts can occur between diverging submodule versions, too. Example (submodule ImageJA):

 Auto-merging ImageJA
 CONFLICT (submodule): Merge conflict in ImageJA

As a submodule's "content" in the superproject is the submodule's current commit name, the ''diff'' will show you something like this:

 diff --cc ImageJA
 index 6335c9b,d245d31..0000000
 --- a/ImageJA
 +++ b/ImageJA
 @@@ -1,1 -1,1 +1,1 @@@
 - Subproject commit 6335c9b0b39aa96001b5f9be665aabe3c854bae6
  -Subproject commit d245d31d53e1f85264113c99609b8379eaee38ee
 ++Subproject commit 7bbce1e02aa3ba1971533441e9a50c75764c8e92

To resolve this you can either make one of the commits the current one in the submodule and then ''git add'' the submodule in the superproject. Or you can use '' git checkout'' in the superproject right away:

 git checkout --theirs ImageJA

or for your version:

 git checkout --ours ImageJA

== Committing the resolution ==

After you resolved all the conflicts (if in doubt, where the conflicts are, just call ''git diff''), add the resolved file contents:

 git add <file>

and then commit the merge:

 git commit -s

== Using an external merge tool ==

For complicated conflicts, you may find it easier to do the resolution using an external merge tool, which can show three versions of the file side-by-side.  You can do this with:

 git mergetool

... which will offer you a choice of tools.  Here is a screenshot of using <tt>git mergetool --tool=meld</tt>:

[[File:Meld-example.png|750px]]

[[Category:Git]]
