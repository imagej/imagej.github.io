---
title: 2011-10-05 - The relation between ImageJA and ImageJ
---

[ImageJA](/libs/imageja) started out as a two-pronged project:

1.  We wanted to have a source code management system so that we could contribute and update patches to [ImageJ](/software/imagej).
    Originally, this was CVS, now it is [Git](/develop/git), and in the meantime [Wayne Rasband](/people/rasband), the author of ImageJ, also adopted a routine involving Git. So basically, this goal was reached.
2.  We wanted to provide support for in-browser applets that do not "pop out".
    In other words, we wanted an applet version of ImageJ which would be embedded into the webpage without having an extra main window. This code is basically working, but there are still many places where extra windows are popping up (e.g. the results table, or error messages). Plus, it has not made it back into upstream ImageJ. So this goal was not reached.

To stay up-to-date, ImageJA is synchronized with ImageJ. There are three (actually four) scripts involved in this synchronization.

The real first script is a notifier which scrapes the [News section of the ImageJ 1.x site](https://imagej.nih.gov/ij/notes.html) every hour or so and sends me an email when it changed. Whenever I get such a mail I run three scripts in succession, which are all stored in the 'tools' branch of ImageJA.git:

1.  `commit-new-version.sh`
    This script downloads the News section, detects the current version, downloads the -src package, changes line endings to standard (Unix) line endings, deletes Mac-specific files (e.g. Finder-related files which have nothing to do with Java source files) and finally commits that as new state in the 'imagej' branch.
2.  `merge-imagej.sh`
    This script tries to make sure that my current working directory is an up-to-date version of ImageJA, then merges the 'imagej' branch.
3.  `upload-imageja.sh`
    This script builds the current commit, determines which ImageJ version it is based on, adds an appropriate tag and uploads -src and signed release jar to ImageJA's sourceforge download site, to ImageJA's website, to Fiji's ImageJA site, and then pushes the 'master' and 'imagej' branches as well as the new tag to all kinds of remote repositories, including repo.or.cz, fiji.sc and dev.loci.wisc.edu.

These scripts have gone through a long history ([I](/people/dscho) started the stuff in October 2005, when I tried to get ahold of as many as possible previous source packages and committed them as history of ImageJ to document as much as possible how things developed).

Typically, the merge step ends in a merge conflict since we have quite some changes in ImageJA vs ImageJ which did not make it to the upstream for one reason or other.

In the future, my plan is to make these changes obsolete, and basically change the merge script into one that takes the current imagej state and puts the stuff into the appropriate src/main/\* subdirectories, and adjusts the version in the pom.xml. It might even be so automated that we can let Hudson perform the job.

The changes fall into three categories, with different strategies how to "make them obsolete":

1.  Changes that we provided for traditional reasons but that will be obsolete with IJ2, such as the "convert to 8-bit" in the {% include bc path='File|Import|Image Sequence...'%} support code or the "fuzzy matching" in the Command Finder.
    Roughly half of these changes I will just forget, while the other half of changes will persist in the IJ1-based Fiji through [Javassist](/develop/javassist).
2.  Changes that actually should live as add-ons to ImageJ, such as the {% include bc path='Plugins|Install Plugin...'%} plugin. Of course, having it as a Fiji plugin will move its position in the menu, but that does not matter that much.
3.  The headless stuff. I'll try to make that available both as javassist-enabled runtime adjustment as well as rewritten-by-javassist end-user packages (on demand only, for cases when you cannot have javassist do its job due to security restraints).

Some cases are hybrids, where the code will be moved outside ij.jar and be available as a plugin, but I'll use javassist to make it available from the appropriate places within IJ1.

In general, this should clean up a lot of unnecessary modifications in IJ1 and let us (read: [me](/people/dscho)) concentrate much more on IJ2.

  
