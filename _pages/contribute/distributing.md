---
title: Distribution
section: Contribute
nav-links: true
---

If you create a useful extension of ImageJ—e.g., a [plugin](/plugins), [script](/scripting/script-editor) or [macro](/scripting/macro)—the next step is to provide it to others, which includes:

1.  **Distributing** the extension itself to users:
    -   A\) [create your own update site](/update-sites/setup); or
    -   B\) [bundle your plugin with Fiji](/contribute/fiji).
2.  Sharing the extension's **source code**:
    -   Make your project [open source](/licensing/open-source).
    -   Host it on [GitHub](/develop/github).
    -   Use [Maven](/develop/maven) to build and SemVer for [versioning](/develop/versioning).
    -   Use [GitHub Actions](/develop/github-actions) for continuous integration and artifact deployment to the [SciJava Maven repository](/develop/project-management#maven).
3.  **Documenting** how the extension works:
    -   Create a page here on the [ImageJ Wiki](/).

## Distributing your extension

{% include notice icon="fiji" content="The [original ImageJ](/software/imagej) does not support update sites; users will need to use [Fiji](/software/fiji)." %}

{% include aside content="**What about serving it from a website as a download?**

If you do not rely on the [Updater](/plugins/updater) mechanism, [Fiji](/software/fiji) will not be required to install the extension. However, users must then:

* Find your plugin via a link or web search;
* perform a manual installation procedure;
* and manually check for later updates.

You are more likely to receive bug reports about outdated versions of the extension, and extensions with significant dependencies are more likely to conflict with each other." %}

There are two good ways of getting your extension into people's hands:

### Option A: Create your own update site

You can create an [ImageJ update site](/update-sites) that offers your extension to [Fiji](/software/fiji) users.

1. [Set up your update site](/update-sites/setup), then [upload your extension to it](/update-sites/setup#uploading-files-to-your-update-site).
2. Optionally, you may add your update site to the list of built-in sites by editing the [list of update sites](/list-of-update-sites) page.
3. To release a new version, [upload it to the update site](/update-sites/setup#uploading-files-to-your-update-site).

Users [enable the update site](/update-sites/following) to receive your extension, as well as future updates.

**Benefits:**
* You do not need your own server; you can use a [hosted update site](/update-sites/setup) on `sites.imagej.net`.
* Alternately, you can retain full control by hosting your update site yourself.
* Users are notified of updates without needing to check proactively.
* The updater manages dependencies for you.
* You can automate distribution using the [command line updater](/plugins/updater#command-line-usage).

### Option B: Distribute it as part of Fiji

You can distribute your extension with Fiji, so that users have access to it immediately upon [download and install](/software/fiji/downloads).

Tag the `@fiji` team in an [ImageJ Forum](/discuss) post to initiate a request.

**Benefits:**
* Your extension is available with Fiji out of the box.
* A [Fiji maintainer](/contribute/governance) will help you to manage your project.
* You can lean on existing tools and documentation to maintain [reproducibility](/develop/architecture#reproducible-builds) of your project.
* Your project will always be compatible with the latest Fiji distribution.
* [GitHub Actions](/develop/github-actions) automatically tests your project for errors, deploying successful builds to the [SciJava Maven repository](/develop/project-management#maven).

**Caveats:**
You must abide by the [Fiji contribution requirements](/contribute/fiji), and rely on a Fiji maintainer (for now) to upload new versions for you.

## Sharing your source code

{% include aside content="**Why GitHub?**

There are many code-hosting sites to choose from, such as GitLab, BitBucket, and SourceForge.

The ImageJ and Fiji projects use GitHub because it has the most critical mass. Maybe someday, GitHub will [stop being so awesome](https://en.wikipedia.org/wiki/Enshittification) and we will be forced to migrate everything to somewhere more open like [Codeberg](https://codeberg.org/). But for now, GitHub is an incredible service, and everything being backed by [Git](/develop/git) means that we could migrate if necessary.
" %}

If you want to facilitate good science, please [share your source code](/licensing/open-source). Otherwise, your extension is a black box and its results are not verifiable.

### Steps

1. Create an account on [GitHub](https://github.com).
2. [Create a new repository](https://help.github.com/articles/create-a-repo) for your project.
3. [Push your code](https://help.github.com/articles/pushing-to-a-remote) there.
4. [Learn Git](/develop/git) to manage your code effectively.
5. Optionally, if your extension is [distributed with Fiji](/contribute/fiji), you can transfer your repository to the `fiji` organization on GitHub, so that [Fiji maintainers](/contribute/governance) help you to manage your project more easily.

### Advantages

* Git is an incredibly powerful way to keep track of your code.
* GitHub greatly facilitates collaboration: sharing ideas and patches.
* Working in public is a great way to [stop sucking and be awesome instead](http://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/).
* All of [ImageJ](/software/imagej), [Fiji](/software/fiji), and related [SciJava](/libs/scijava) projects are [hosted on GitHub](/develop/source).
* Anyone can easily browse the source code online.
* Anyone can submit suggestions (called pull requests) to improve the code.
* Your project and its code are more [Findable](https://www.go-fair.org/fair-principles/).
* Git provides a safety net, enabling you to undo mistakes and avoid lost work.
* You get an automatic changelog of what changes were made, by whom, when, and why.
* Contributors are automatically credited for their efforts.
* It is easier to track down when bugs were introduced by testing with different past versions of the codebase.
* You can easily switch between different versions of the code.
* You can explore multiple development trajectories (called branches) to try out different approaches.

The main downside? Git has a steep learning curve—but the [GitHub Desktop](https://desktop.github.com/) client makes things easier.

## Documenting your extension

Useful extensions deserve corresponding documentation explaining how to use them.

We recommend using the ImageJ wiki for this purpose because:
* It is a central repository of ImageJ-related community knowledge and documentation.
* It makes your extension more [Findable](https://www.go-fair.org/fair-principles/). E.g. your extension will appear in the wiki's search bar.
* It is more collaborative: others can improve the documentation.
* It more resilient to information loss. We have seen externally hosted documentation disappear, including that of the [3D Viewer](/plugins/3d-viewer), [VIB Protocol](/plugins/vib-protocol), and [MBF Plugin Collection](/software/mbf-imagej).

To include your extension here, just create a page! For details, see [Editing the Wiki](/editing).
