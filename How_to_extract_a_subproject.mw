{{GitMenu}}
Sometimes, a piece of functionality is developed as part of one project, but grows so much as to warrant becoming its own, separate project.

This tutorial describes how to split part of a Git repository into its own dedicated Git repository, preserving only the history relevant to the subproject being extracted.

== Extract the revision history ==

<ol>
<li>Use Git's ''filter-branch'' feature to extract the Git history of only the subproject:
<source lang="bash">
git filter-branch -f --prune-empty --subdirectory-filter <subdir>
</source>
Where <code><subdir></code> is the folder containing the subproject's source code.</li>
</li>
</ol>

== Update the Maven build ==

Assuming you are using [[Maven]] to build the subproject:
<ol>
<li>Add an ''<scm>'' section to the ''pom.xml'' to reflect the new remote repository's URL (see [https://github.com/scijava/jep/commit/b76f4a1df830c090fc96ab99bb145dd67e8e69ce example]):
<source lang="bash">vi pom.xml
git commit -m 'Add SCM location' pom.xml</source>
</li>
<li>Replace the old ''<parent>'' with a new one, such as [https://github.com/scijava/pom-scijava pom-scijava], [https://github.com/imagej/pom-imagej pom-imagej] or [https://github.com/fiji/pom-fiji pom-fiji] (see [https://github.com/scijava/jep/commit/336c0a46fad855508aaa905a9f82e5d88136df91 example])—or remove the ''<parent>'' altogether.</li>
<li>Add a ''<developers>'' section to the ''pom.xml'' to indicate the project developers (see [https://github.com/fiji/TrackMate/commit/f0c2cf6cca3e198ba5b9283a71fc564f41c642d5 example]). You can also add ''<contributors>'' if desired and relevant.
<li>Make sure the project still builds:
<source lang="bash">mvn clean package</source>
</li>
<li>Add (or adjust) the ''.gitignore'' file (see [https://github.com/fiji/spimreconstruction/commit/cf95dcc06b31c0044b58213c12f886027a5eb3ba example]).</li>
</ol>

== Push the changes ==

<ol>
<li>Make sure that all your changes look good:
<source lang="bash">
git status
git diff
</source>
This is good advice in general: check <code>git status</code> and <code>git diff</code> ''every time'' before you commit, to prevent making a fool out of yourself.</li>
<li>Commit everything, mentioning the commit of the parent project from which history was rewritten (see [https://github.com/scijava/jep/commit/660930836860c6f67ecb53d091eb1730ecb68c80 example]):
<source lang="bash">git add . && git commit -s</source>
</li>
<li>Create a new repository somewhere for the new project—we recommend [[GitHub]].</li>
<li>Connect your repository with the remote one:
<source lang="bash">git remote set-url origin git@github.com:my-org/my-new-project</source>
Where ''git@github.com:my-org/my-new-project'' is the remote URL for the new project's dedicated repository.</li>
<li>Push the resultant history to the project's new repository:
<source lang="bash">git push -u origin master</source></li>
</ol>

== Change any online resources ==

# Edit the relevant web page(s) to reflect the new Git repository location
# Update any other known links to the project

[[Category:Development]]
