---
mediawiki: Iterative_Deconvolve_3D
name: "Iterative Deconvolve 3D"
title: Iterative Deconvolve 3D
categories: [Deconvolution]
doi: 10.2514/6.2005-2961
release-date: "4 June 2005"
initial-release-date: "1 May 2005"
website: "http://www.optinav.info/Iterative-Deconvolve-3D.htm"
dev-status: "stable"
team-founder: 'Bob Dougherty'
---

{% include info-box filename=' [Iterative\_Deconvolve\_3D.class](http://www.optinav.info/download/Iterative_Deconvolve_3D.class)' source=' [Iterative\_Deconvolve\_3D.java](http://www.optinav.info/download/Iterative_Deconvolve_3D.java)'  %}

## Purpose

Plugin for 2D and 3D non-negative, iterative, deconvolution. Based in part on the DAMAS algorithm by Thomas F. Brooks and William M. Humphreys, Jr., NASA-Langley Research Center. Also includes a regularized Wiener filter as a preconditioning step. Called DAMAS3 in aeroacoustics.

## Documentation

The [website](http://www.optinav.com/Iterative-Deconvolve-3D.htm) document this plugin; please refer to it.

The plugin was also the subject of a conference paper:

{% include citation %}

## See also

[Diffraction PSF 3D](/plugins/diffraction-psf-3d) for the creation of theoretical PSF.

## Version history

-   Version 0: 5/1/2005. Beta release.
-   Version 1: 5/2/2005. Improved performance for 2D images. Option to not show iterations.
-   Version 2: 5/29/2005. Added low pass filter, like Iterative Deconvolution/DAMAS2.
-   Version 3: 5/30/2005. Improved user interface and recommended settings. Corrected filters.
-   Version 3.1 5/30/2005. Convolution-based anti-ringing feature.
-   Version 4: 6/3/2005. Corrected a scaling error in the iteration. Provided an option to turn off the Wiener filter. Added divergence detection. Changed the defintion of the low pass filter parameters (multiplied by 2) to better match Iterative Deconvolution.
-   Version 5: 6/3/2005. Corrected a bug in the low pass filter in the z direction.
-   Version 5.1 6/3/2005. Improved test for 0 gamma (no Wiener filter). Renamed low pass fiter parameter for z in dialog.
-   Version 5.2 6/4/2005. Changed the recommended low pass filter settings from 4 to 1 pixels.
