---
title: Reporting Issues
section: Discuss
nav-links: true
---

Please report bugs via the [Image.sc Forum](https://forum.image.sc/):

- Start a new topic in the "Usage & Issues" category.
- Add at least one label: `imagej`, `imagej2`, `fiji`, and any other relevant labels.
- Include a [minimal working example](#bug-reporting-best-practices) illustrating the issue.
- If you know who is responsible for maintaining the affected part of the software, please `@mention` them.

Or if you have a GitHub account, please feel welcome to report issues on GitHub in the [ImageJ](https://github.com/imagej/ImageJ/issues),[ImageJ2](https://github.com/imagej/imagej2/issues), [Fiji](https://github.com/fiji/fiji/issues) repositories.

Thank you! 😁

# Bug reporting best practices

A bug report is a reproducible set of steps describing a problem. They are a common communication medium between users and developers. Users willing to take the time to write helpful bug reports drive software development, making it better for everyone.

## TL;DR Summary

-   Report the issue using the [Report a Bug](/discuss/bugs) plugin (in the Help menu).
-   Provide a [minimal, complete, verifiable example](http://stackoverflow.com/help/mcve) (MCVE).
-   [Describe what you already tried](https://web.archive.org/web/20170318144207/http://mattgemmell.com/what-have-you-tried/).
-   [Put as much effort into your question](http://stackoverflow.com/help/how-to-ask) as you expect to be put into its response.

## Be concise

Here are some quick tips for [writing a shorter letter](http://en.wikiquote.org/wiki/Blaise_Pascal):

-   Use bullet points to summarize.
-   Do not inline lengthy logs; use [Gist](https://gist.github.com/) or [Pastebin](http://pastebin.com/) instead.
-   Use formatting such as **emphasis** and `code snippets` to make text easier to read.
-   Use [link syntax](https://help.github.com/articles/github-flavored-markdown) instead of relying on URL autolinking.
-   Use footnotes \[1\] for lengthy asides.
-   Most importantly, provide a [Minimal, Complete and Verifiable example](http://stackoverflow.com/help/mcve) (MCVE), ideally as a standalone project.

\[1\] For technical matters, "too much" information is certainly much preferred to "too little" information. But long paragraphs also break up the flow of information, and bog down an otherwise concise and clear bug report or question. So there is certainly a balance to be struck.

## Why put effort into bug reports

For light reading, there are numerous guides and essays on [how and why to write excellent bug reports](http://www.chiark.greenend.org.uk/~sgtatham/bugs.html). Users should be aware that the development community is diverse: from publicly-funded individuals and teams to scientists and user contributors. For a largely open-source community like this, there are several key points to consider when submitting a bug:

-   Teams developing open-source code are typically smaller and lack dedicated testing teams. Developers thus rely on an active and vocal community to provide feedback and guide the development process by identifying the areas in need of attention (complaint-driven development).
-   If you encounter a bug, it is likely interfering with your desired workflow and needs to be resolved quickly. The better the bug report, the faster a developer will be able to reproduce and address the issue. Poorly written bug reports are more likely to sit unanswered—not because developers see the issue as unimportant, rather that the time required to clarify the bug report itself presents a significant barrier when setting priorities within an overflowing schedule.
-   When you find a bug, it is unlikely that you are the only individual affected by it. By reporting a bug in a way that developers can understand, identify and resolve the issue, you are performing a necessary and valuable service to the entire community.

## Components of a complete bug report

There are three critical components in a bug report. If a report is missing any of these components, its usefulness may be limited.

### Environment information

ImageJ is a flexible and extensible platform, so the actual "ImageJ environment" can vary from user to user. A common mistake in bug reports is to report only the version of ImageJ itself (e.g. 1.49e). This is helpful, but says nothing about what plugins, update sites, etc... are in use.

Errors can appear in any component of the software, and in some cases two plugins might work individually but have some negative interaction with each other. Thus a complete view of the ImageJ environment is imperative. If you are running [ImageJ2](/software/imagej2), you can use the command {% include bc path="Plugins | Debug | System Information" %} to generate a full report of what is installed.

### Minimal and precise steps to reproduce

When we're in a hurry, it's easy to provide a brief overview a bug without actually describing how to reproduce the error. We are also prone to providing too much information, which can confuse the issue and discourage thorough reading.

The actual text of your bug report should succinctly describe the fewest steps possible to reproduce your issue. For example:

  
  1\) Open sample image "blobs"

  2\) Run auto-threshold command

  3\) Run subtract background command

  At this point, an evil kraken appears and sinks my hard drive.

Additional information is typically unnecessary... if a developer can reproduce the problem, they will do their best to fix it.

### Sample data

Developers typically have a cache of sample data for testing their application. That said, we are still striving to reproduce the original environment of the error. Having the original image that caused the error is the best possible way to test.

If your test data is small and public, you can attach it to the bug report.

If your test data is large, but can be shared, please use a cloud service link (Dropbox, Google Drive, etc.).

If your test data cannot be made public, but you are willing to share it privately with the developers, please do so.

## While you're waiting...

If you have encountered and reported a bug that is completely blocking your work, you still have options available while waiting for the issue to be resolved.

### Disable SCIFIO

[ImageJ2](/software/imagej2) provides an alternative to the hard-coded case logic of [ImageJ](/software/imagej)'s image I/O: [SCIFIO](/libs/scifio), plugin-based image I/O. While SCIFIO is more powerful, due to the vast scope of the overhaul, there are inevitably issues remaining. If your dataset used to open correctly for you, but is broken after updating, please *disable* the "Use SCIFIO when opening files (BETA!)" option in the {% include bc path='Edit | Options | ImageJ2'%} dialog. This will revert to ImageJ's classic image I/O until the SCIFIO-driven I/O is fixed or improved.

Note: even if disabling SCIFIO fixes the issue for you, **please** still report the discovered bug. The long-term vision for ImageJ is to migrate completely to the new image I/O paradigm, so if there are problems we need to know about them.

### Disable problematic update sites

The [Report a Bug](/discuss/bugs) dialog provides several pieces of critical information. Some of the most important being:

-   Activated update sites
-   Files not up-to-date

The [default update sites](/list-of-update-sites) are intended to be fairly stable, but if you have additional update sites enabled there can be a risk of skewed or out of date dependencies (due to changes in core libraries), and some update sites are intentionally experimental.

Furthermore, if you have any **LOCAL\_ONLY** or **MODIFIED** files, their behavior can not be guaranteed - as they do not match what's on the active update sites and thus can not be automatically updated in response to changes in their dependencies.

In cases where it is clear which class or classes are causing problems, you can do remove the offending component as follows:

- If the problem is in an external plugin, simply delete the file(s).
- If the problem is with an update site:

  1.  If necessary, identify the jar containing the problematic class(es), e.g. by using {% include bc path='Plugins | Utilities | Find Jar for Class'%} in Fiji.
  2.  Start the updater with {% include bc path='Help | Update...'%}
  3.  Switch to Advanced Mode
  4.  Search for the problematic components. Their associated update site will be listed here.
  5.  Select `Manage Update Sites` and disable the update site identified in 4.
  6.  Repeat 1-5 until your problem is resolved.

**NOTICE:** During this process it is critical to keep in mind that update sites take precedence in the [order they are declared](/list-of-update-sites) - update sites lower on the list will overwrite components in sites higher on the list.

#### Binary search through your external plugins

If it is not clear which update sites or external plugins are causing problems in your installation, a simple technique to help identify the cause of your problem is a {% include wikipedia title='Binary search algorithm' text='binary search'%}. The general procedure is such:

  1.  Start from your current installation
  2.  Remove half of your non-core update sites and/or local plugins.
  3.  Test to see if the erroneous behavior is resolved.
  4.  Repeat from 1) with only the "bad" pool of update sites/plugins enabled.

With this method you will continue to reduce your list of potentially bad candidates by 1/2, until you find the culprit(s).

Note: if the "erroneous behavior" is [catastrophic](#catastrophic-failure) to the point you can not start ImageJ, you can instead start from a clean build and re-introduce update sites and local plugins as detailed above until the problem is identified.

### Catastrophic failure

We maintain lifeline ImageJ distributions on the [Downloads page](/downloads). You can use these until any outstanding issues are resolved.
