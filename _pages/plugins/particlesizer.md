---
mediawiki: ParticleSizer
title: ParticleSizer
categories: [Uncategorized]
---


{% capture author%}
{% include person id='thorstenwagner' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='thorstenwagner' %}
{% endcapture %}
{% include info-box software='Fiji' update-site='Biomedgroup & ParticleSizer' name='ParticleSizer' author=author maintainer=maintainer filename='ParticleSizer\_.jar [\[1](https://github.com/thorstenwagner/ij-particlesizer/releases/latest) \]' source='Github [\[2](https://github.com/thorstenwagner/ij-particlesizer) \]' latest-version='v1.0.7 (28. Ocotober 2016)' status='active' %}

# Purpose

The ParticleSizer script was developed to automatically measures the distributions of the characteristic size and shape properties of a nanomaterial. In the scope of implementing the European Commission definition of a nanomaterial, the minimal external dimension of the primary particles of a particulate material is assessed as the minimal feret diameter from electron microscopy images. Other size and shape parameters are measured simultaneously.

# Installation

The ParticleSizer script combines a number of different plugins. The most easy way (and at the moment the only way) is to [follow](/update-sites/following) Biomedgroup & ParticleSizer [update site](/update-sites).

It is recommended to install R to get better plots. When this point is skipped, a stripped-down plot will be shown:

1.  Download the latest R: https://cran.uni-muenster.de/
    1.  Download the Rserver package: https://rforge.net/bin/windows/contrib/3.0/Rserve_1.8-0.zip
    2.  Download the MASS package: https://cran.r-project.org/bin/windows/contrib/3.2/MASS_7.3-45.zip
    3.  Start R and select the packages downloaded in 1. and 2. via {% include bc path="Start Packages | Install packages from local zip files" %}
2.  Open Fiji, start the ParticleSizer Settings Manager and the R path to the R binary.

You can now start the ParticleSizer via {% include bc path="Plugins | NanoDefine -|ParticleSizer" %}

# Settings

**Segmentation:**![](/media/plugins/psizer-gui.png)

-   Circular window radius: This is a parameter of the local thresholding technique. The ParticleSizer does not use a global threshold to binarize the image. Instead it uses a local threshold which is estimated for a specific circular region with the configured radius.
-   Rolling ball radius: The background is removed by rolling a ball with this radius over the surface (intensity interpreded as hight) of the image. It should be at least as large as the largest object in image which does not belongs to the background.
-   Min. OTB intensity difference: Objects which have an object-to-background (OTB) intensity difference in the noise-reduced and background subtracted image lower than this threshold are considered as artefacts and are removed.
-   Use watershed for irregular structures: If selected, the mode for irregular structures is used.
-   Irregular watershed convexity threshold: The threshold determines, when splitted agglomerated is counted as "primary particle". If the convexity of particle is greater than this threshold, the splitting is stopped for this object. If the convexity is smaller than this value, then the ParticleSizer tries to split the particle again
-   Use single particle mode: If selected, the single particle mode is used.
-   Use ellipse fitting mode: If selected, the ellipse fitting mode is used.

**Shape constraints:**

-   Minimal area: Minimum area in pixels. Particles smaller than this threshold are removed.
-   Minimal feret min: Minimal feret diameter in pixel. Particles smaller than this threshold are removed.
-   Minimal convexity: The convexity is defined as the ratio of the perimeter of the convex hull of the particle and the perimeter of the particle. It lies between 0 and 1. The convexity increases with larger values. Particles smaller than this threshold are removed.
-   Minimal solidity: Defined as the ratio of the particle area and the area of the convex hull of the particle. It lies between 0 and 1. The solidity increases with larger values. Particles smaller than this threshold are removed.

**Ellipse shape constraints:**

-   Minimal long axis length: The length in pixels of the major direction of the fitted ellipse. Ellipses smaller than this threshold are removed.
-   Minimal short axis length: The length in pixels of the minor direction of the fitted ellipse. Ellipses smaller than this threshold are removed.
-   Maximal aspect ratio: Ratio of the length of major and minor axis. Ellipses with an aspect ratio larger than this value are removed.

**Misc:**

-   Smoothing factor: It sometimes occurs that the estimated standard deviation of the noise is lower than the true value. The smoothing factor is a multiplicative factor for the estimated standard deviation.
-   Show binary result: If selected the ParticleSizer shows the binary result.
-   Ask me to select a region: If selected, the software allows you to select a specific region to analyse.
-   Record process: If this checkbox is selected, a new image stack opens at the end of the analysis which contain images of every single step the particle

sizer made. If an image stack is analysed, than only the only the processing of the first image is recorded.

## How to find optimal settings

We distinguish two particle types:

-   E: Ellipsoidal particles
-   I: Irregular but convex particles

These particles could show some overlapping. We destinguish four different classes:

-   N: No overlapping
-   T: Touching
-   S: Slightly overlapping
-   H: High or complete overlapping

Combining both information, we could give the following advice (as a rule of thumb):

-   N+E or T+E -&gt; Keep the default settings
-   N+I or T+I or S+I -&gt; Activate the irregular watershed
-   S+E -&gt; Activate ellipse fitting
-   H -&gt; Activate single particle mode

# Use the ParticleSizer with the NanoDefiner e-tool

The ParticleSizer supports the [NanoDefiner e-tool](https://labs.inf.fh-dortmund.de/NanoDefiner/?anchor=version#version). After the analysis of a dataset is finished, you can select the results table and export the cumulative mass function of the feret min diamater by {% include bc path="Results | Export CMF" %}. The exported file can be uploaded to the [NanoDefiner e-tool](https://labs.inf.fh-dortmund.de/NanoDefiner/?anchor=version#version).

# Examples

## Gold 8 nm, Settings: Default

<img src="/media/plugins/gold-nooverlay.png" title="fig:Gold_nooverlay.png" width="300" alt="Gold_nooverlay.png" /> <img src="/media/plugins/gold-overlay.png" title="fig:Gold_overlay.png" width="300" alt="Gold_overlay.png" /> <img src="/media/plugins/hist-gold-normal.png" title="fig:Hist_gold_normal.png" width="300" alt="Hist_gold_normal.png" />

## Gold 8 nm, Settings: +Ellipse fitting mode

<img src="/media/plugins/gold-nooverlay.png" title="fig:Gold_nooverlay.png" width="300" alt="Gold_nooverlay.png" /> <img src="/media/plugins/gold-overlay-ellipsefitting.png" title="fig:Gold_overlay_ellipsefitting.png" width="300" alt="Gold_overlay_ellipsefitting.png" /> <img src="/media/plugins/gold-overlay-ellipsefitting-size.png" title="fig:Gold_overlay_ellipsefitting_size.png" width="300" alt="Gold_overlay_ellipsefitting_size.png" />

## Gold 10 nm, Settings: +Min. OTB difference=30

<img src="/media/plugins/10nm-gold-nooverlay.png" title="fig:10nm_gold_nooverlay.png" width="300" alt="10nm_gold_nooverlay.png" /> <img src="/media/plugins/10nm-gold-overlay.png" title="fig:10nm_gold_overlay.png" width="300" alt="10nm_gold_overlay.png" /> <img src="/media/plugins/10nm-gold-overlay-size.png" title="fig:10nm_gold_overlay_size.png" width="300" alt="10nm_gold_overlay_size.png" />

## Kaolin, Settings: +Single particle mode

<img src="/media/plugins/kaolin-ohne-overlay.png" title="fig:Kaolin_ohne_overlay.png" width="300" alt="Kaolin_ohne_overlay.png" /> <img src="/media/plugins/kaolin-overlay.png" width="300"/> <img src="/media/plugins/kaolin-size-distr.png" title="fig:Kaolin_size_distr.png" width="300" alt="Kaolin_size_distr.png" />

# How to cite

A publication is in preparation.

You can use Zenodo to cite the lastest release of the ParticleSizer: https://zenodo.org/badge/latestdoi/18649/thorstenwagner/ij-particlesizer

As example: Thorsten Wagner. (2016). ij-particlesizer: ParticleSizer 1.0.1. Zenodo. 10.5281/zenodo.56457

# Acknowledgements

The development of the ParticleSizer has received funding from the European Union Seventh Framework Programme (FP7/2007-2013)
