---
mediawiki: CAMDU
title: CAMDU
categories: [Uncategorized]
---

CAMDU ([http://www.warwick.ac.uk/camdu](http://www.warwick.ac.uk/camdu)) is a "virtual facility" at the University of Warwick. We are home to multiple advanced light microscopes, both commercial and custom-built systems, alongside computational workstations, software development and integrated petabyte data storage. This includes our Wellcome-funded lattice light sheet microscope and visitor programme.

Currently, our Fiji update site offers the plugin autoQC for automating tasks related to microscope quality control.

## AutoQC

Usage Instructions:

**autoPSF**: expects Z-stacks with sub-resolution fluorescent beads.

**autoFOV**: expects single 2d images of a fluorescent slide (uniform sample).

**autoColoc**: expects 4d images (XYCZT) of larger-than-resolution fluorescent beads.

**autoStageRepro**: expects 3d images (timelapse). Each timepoint should be recorded after translating the stage and moving it back to its original position.

If you're using files from multiple folders, outputs will be saved on the folder where the first file is.

You can operate over multiseries files - the match string parameter tells the program what substring it should look for. For example, if you have a multiseries file and you wan to run autoPSF only over series containing "psf" on their names, use "psf" as the match string parameter.

Note that, for multiseries files (e.g. mvd2), the same calibration is used for all series - do not mix different objectives on the same file!

When in doubt, consult the [MetroloJ Manual](http://imagejdocu.list.lu/lib/exe/fetch.php?media=plugin:analysis:metroloj:metroloj.pdf) for detailed protocols.

For OMERO stuff, you need the [OMERO Plugin for ImageJ](https://www.openmicroscopy.org/omero/downloads/).

------------------------------------------------------------------------

**References:**

Schneider, C. A.; Rasband, W. S. & Eliceiri, K. W. (2012), "NIH Image to ImageJ: 25 years of image analysis", Nature methods 9(7): 671-675, PMID 22930834

Schindelin, J.; Arganda-Carreras, I. & Frise, E. et al. (2012), "Fiji: an open-source platform for biological-image analysis", Nature methods 9(7): 676-682, PMID 22743772, <doi:10.1038/nmeth.2019>

**Uses the following plugins: **

bioformats (https://www.openmicroscopy.org/bio-formats/)

Melissa Linkert, Curtis T. Rueden, Chris Allan, Jean-Marie Burel, Will Moore, Andrew Patterson, Brian Loranger, Josh Moore, Carlos Neves, Donald MacDonald, Aleksandra Tarkowska, Caitlin Sticco, Emma Hill, Mike Rossner, Kevin W. Eliceiri, and Jason R. Swedlow (2010) Metadata matters: access to image data in the real world. The Journal of Cell Biology 189(5), 777-782. doi: 10.1083/jcb.201004104

**Uses code from:**

MetroloJ (http://imagejdocu.list.lu/doku.php?id=plugin:analysis:metroloj:start)

Cédric Matthews and Fabrice P. Cordelieres, MetroloJ : an ImageJ plugin to help monitor microscopes' health, in ImageJ User & Developer Conference 2010 proceedings

TrackMate (https://imagej.net/plugins/trackmate)

Tinevez, JY.; Perry, N. & Schindelin, J. et al. (2016), "TrackMate: An open and extensible platform for single-particle tracking.", Methods 115: 80-90, PMID 27713081

**Special thanks**

\- Robert Haase

\- Jean-Yves Tinevez
