---
title: How to extract a subproject
section: Extend:Development:Git
---


 Sometimes, a piece of functionality is developed as part of one project, but grows so much as to warrant becoming its own, separate project.

This tutorial describes how to split part of a Git repository into its own dedicated Git repository, preserving only the history relevant to the subproject being extracted.

## Extract the revision history

1.  Use Git's *filter-branch* feature to extract the Git history of only the subproject:

    ```bash
    git filter-branch -f --prune-empty --subdirectory-filter <subdir>
    ```
    
    Where `<subdir>` is the folder containing the subproject's source code.

## Update the Maven build

Assuming you are using [Maven](/develop/maven) to build the subproject:

1.  Add an *\<scm\>* section to the *pom.xml* to reflect the new remote repository's URL (see [example](https://github.com/scijava/jep/commit/b76f4a1df830c090fc96ab99bb145dd67e8e69ce)):

    ```bash
    vi pom.xml
    git commit -m 'Add SCM location' pom.xml
    ```

2.  Replace the old *\<parent\>* with a new one, such as [pom-scijava](https://github.com/scijava/pom-scijava), [pom-imagej](https://github.com/imagej/pom-imagej) or [pom-fiji](https://github.com/fiji/pom-fiji) (see [example](https://github.com/scijava/jep/commit/336c0a46fad855508aaa905a9f82e5d88136df91))—or remove the *\<parent\>* altogether.

3.  Add a *\<developers\>* section to the *pom.xml* to indicate the project developers (see [example](https://github.com/fiji/plugins/trackmate/commit/f0c2cf6cca3e198ba5b9283a71fc564f41c642d5)). You can also add *\<contributors\>* if desired and relevant.

4.  Make sure the project still builds:

    ```bash
    mvn clean package
    ```

5.  Add (or adjust) the *.gitignore* file (see [example](https://github.com/fiji/spimreconstruction/commit/cf95dcc06b31c0044b58213c12f886027a5eb3ba)).

## Push the changes

1.  Make sure that all your changes look good:

    ```bash
    git status
    git diff
    ```
    This is good advice in general: check `git status` and `git diff` *every time* before you commit, to prevent making a fool out of yourself.

2.  Commit everything, mentioning the commit of the parent project from which history was rewritten (see [example](https://github.com/scijava/jep/commit/660930836860c6f67ecb53d091eb1730ecb68c80)):

    ```bash
    git add . && git commit -s
    ```

3.  Create a new repository somewhere for the new project—we recommend [GitHub](/develop/github).

4.  Connect your repository with the remote one:

    ```bash
    git remote set-url origin git@github.com:my-org/my-new-project
    ```
    Where *git@github.com:my-org/my-new-project* is the remote URL for the new project's dedicated repository.
5.  Push the resultant history to the project's new repository:

	```bash
	git push -u origin master
	```

## Change any online resources

1.  Edit the relevant web page(s) to reflect the new Git repository location
2.  Update any other known links to the project


