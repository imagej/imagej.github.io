---
title: 2015-07-27 - Janelia Hackathon
---

From Sunday, July 27, 2015 through Friday, July 31, 2015, {% include person id='axtimwalde' %} at HHMI Janelia in Ashburn, Virginia hosted [LOCI](/orgs/loci)'s {% include person id='ctrueden' %} and {% include person id='hinerm' %} for a hackathon to unify [SCIFIO](/libs/scifio)/[ImgLib2](/libs/imglib2) development efforts (with MPI-CBG's {% include person id='tpietzsch' %}), improve support for the [Janelia KLB format](https://bitbucket.org/fernandoamat/keller-lab-block-filetype) (with Janelia's Burkhard Hoeckendorf), and improve the development tools available for [Fiji](/software/fiji) developers.

## Executive summary

-   SCIFIO is headed in a great direction:
    -   Will integrate it better into modern, powerful software tools including ImgLib2 and [BigDataViewer](/plugins/bdv).
    -   Big step toward breaking the limitations of [ImageJ 1.x](/software/imagej), in particular the 2GPix plane barrier and limited image types.
    -   Will make possible things like more transparent and rapid ability to work with multi-position and multi-angle datasets (mosaics, light sheet, etc.).
-   Stability of [ImageJ](/software/imagej) and Fiji—and other applications built on [SciJava](/libs/scijava) components—is now easier to validate.

## Technical discussions

-   Unify BigDataViewer and SCIFIO/SciJava cell caches, and caching in general
-   Unify SCIFIO and ImgLib2 metadata data structures
-   Improve Maven tooling for releases and testing.
-   KLB block-based file format:
    -   Generalize SCIFIO's core API to use N-D blocks instead of planes.
    -   Consider pure Java implementation of KLB to avoid native lib issues.
    -   Enable multithreaded I/O in SCIFIO as painlessly as possible.

## Progress this week

-   Curtis wrote a "melting pot" script for testing component changes in the context of a larger application (e.g.: "Would this change to TrakEM2 break Fiji?") \[[1](https://github.com/scijava/scijava-scripts/commit/d611704204d607dc94654a6810d00a1ab0e9280e)\].
-   Curtis made some ImageJ improvements in response to feedback from Burkhard \[[2](https://github.com/imagej/imagej-plugins-commands/commit/6fafbc9c3444e3fe70420244699d02acfb72abfd), [3](https://github.com/imagej/imagej-plugins-commands/commit/ea9596b2d905eff9f7a9b2177dca5fe44b65ae6e)\].
-   Mark fixed bugs in SCIFIO cell caching in preparation for unification \[[4](https://github.com/imglib/imglib2-ij/pull/5)\].
-   Mark and Curtis planned out the new SCIFIO API for "blockization".
-   Mark began work on ImageJ data model changes for SCIFIO "blockization" \[[5](https://github.com/imagej/imagej-common/compare/calibrated-interval), [6](https://github.com/scifio/scifio/compare/blocks-are-so-plane)\].

## Future directions

-   Jenkins automation of melting-pot for Fiji testing.
-   Wiki documentation on how to use the melting-pot for testing your components.
-   Completion of development on the SCIFIO "blockization" and unification of ImgLib2 data structures and caching.
-   Convert KLB native code to a pure Java SCIFIO format implementation.

   
