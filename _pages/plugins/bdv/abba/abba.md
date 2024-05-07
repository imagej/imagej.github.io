---
title: Aligning Big Brains & Atlases
artifact: ch.epfl.biop:ImageToAtlasRegister
nav-links: true
toc: true
---

The complete documentation of ABBA can be found here: 
[https://abba-documentation.readthedocs.io](https://abba-documentation.readthedocs.io).

You can use ABBA by activating the PTBIOP update site, but more functionalities are acessible through other installation means. Check the full documentation for instructions.

## [ABBA](https://www.youtube.com/watch?v=8haRfsY4-_s) - Aligning Big Brains & Atlases

Aligning Big Brains & Atlases or ABBA for short, is a Fiji plugin which allows to register thin serial sections to several atlases, in coronal, sagittal and horizontal orientations.

Within Fiji, you have access to the [3D mouse Allen Brain atlas](http://atlas.brain-map.org/atlas?atlas=602630314), and the [Waxholm Space Atlas of the Sprague Dawley Rat Brain](https://www.nitrc.org/projects/whs-sd-atlas). With [ABBA-Python](https://github.com/NicoKiaru/ABBA-Python), you can access all [BrainGlobe atlases](https://brainglobe.info/).

ABBA is typically used in conjunction with [QuPath](https://qupath.github.io): a QuPath project can serve as an input for ABBA, and the registration results can be imported back into QuPath for downstream processing.

<video autoplay loop muted style="width: 100%;">
  <source src="https://user-images.githubusercontent.com/20223054/149301605-07b27dd0-4010-4ca4-b415-f5a9acc8963d.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

-----


ABBA uses [BigDataViewer](https://imagej.net/plugins/bdv/index) and [BigWarp](https://imagej.net/plugins/bigwarp) for the display and on-the-fly computation of spline-transformed multiresolution images (typical output of Whole Slide Imaging).

It has been developed by the [BioImaging & Optics Platform](https://www.epfl.ch/research/facilities/ptbiop/) at EPFL. This page contains the reference documentation of ABBA. If you require additional help, please check the troubleshooting section at the bottom of this page.



## Documentation

You will find the complete documentation in [https://abba-documentation.readthedocs.io](https://abba-documentation.readthedocs.io)




