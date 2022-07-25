---
mediawiki: BoneJ1
name: "BoneJ 1.x"
title: BoneJ1
categories: [Uncategorized]
doi: 10.1016/j.bone.2010.08.023
website: "http://bonej.org/legacy"
dev-status: "Legacy"
team-maintainer: "@mdoube"
team-founder: "@mdoube"
source-url: https://github.com/mdoube/BoneJ
icon: /media/icons/bonej.png
---

BoneJ is a plugin for bone image analysis in [ImageJ](/software/imagej). It provides free, open source tools for trabecular geometry and whole bone shape analysis.

## Current release ([BoneJ2](/plugins/bonej))

There's a new modernized version of BoneJ available through the [ImageJ Updater](/plugins/updater). Read more about [BoneJ2](/plugins/bonej).

## Legacy (BoneJ v1.x) Installation

{% include icon name='ImageJ' size='24px' %} BoneJ was designed to work with the original [ImageJ](/software/imagej).

{% include icon name='Fiji' size='24px' %} BoneJ can be installed into [Fiji](/software/fiji), but you must **use the Java-6 version of Fiji, not the current Java-8 version**:

-   Download the final Java-6 version of Fiji labeled "2017 May 30" from [here](/software/fiji/downloads#java-6).
-   Unpack it somewhere beneath your home folder.
-   Download and install `BoneJ_.jar` into that installation's `plugins` folder.
-   Launch Fiji and run {% include bc path='Plugins | 3D Viewer'%} to trigger installation of the [3D Viewer](/plugins/3d-viewer).
-   Restart Fiji.

For technical details about ImageJ and Fiji using Java 6 vs. Java 8, see the [Java 8](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) page.

## BoneJ and pQCT

BoneJ and pQCT plug-ins are in the process of separation. The latter have their own [update site](/plugins/pqct), and they don't need BoneJ to work. However, if you download `BoneJ_.jar` from [bonej.org](http://bonej.org/legacy) it still includes older versions of the pQCT tools.

## Publication

{% include citation %}
