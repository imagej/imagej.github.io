---
title: Non Local Means Denoise
categories: [Denoising]
team-founders:
- Pascal Behnel
- "@thorstenwagner"
team-maintainer: "@thorstenwagner"
dev-status: Stable
support-status: Limited
source-url: https://github.com/thorstenwagner/ij-nl-means
release-version: v1.4.6
release-date: 13 Mar 2016
doi:
- 10.5201/ipol.2011.bcm_nlm
- 10.1109/ISBI.2008.4541250
---

# Purpose

This is an ImageJ plugin for denosing images via the non-local-means algorithm described in

{% include citation doi="10.5201/ipol.2011.bcm_nlm" %}

including the changes proposed by

{% include citation doi="10.1109/ISBI.2008.4541250" %}

It is numerically optimized and multithreaded. It works with all image types (RGB, 32 Bit, 16 Bit, 8 Bit).

This plugin was developed within the scope of a study work of Pascal Behnel and is maintained by Thorsten Wagner (Both are members of the Biomedical Imaging Group).

# Settings

**Sigma:** The sigma of the noise.

**Smoothing factor:** In most cases, the default value (1) should not be changed. However, sometimes a more smoothed image is desired which can be achieved by selecting values &gt; 1.

**Auto estimate sigma:** If this option is selected, the sigma is automatically estimated by the method descriped in *Immerkaer, J., 1996. Fast noise variance estimation. Computer Vision and Image Understanding.*

Both, the value for the (estimated) sigma and the smoothing factor are saved in the imagej preferences and are accessible with the keys "nlmean.sigma" / "nlmeans.smoothingfactor".

# Example

The left image shows a noisy (sigma=25) image, and right image the denoised version using the non local means plugin with auto-estimated sigma and smoothing factor of 1:

{% include img src="clown-noise-25" width="250px" %} {% include img src="clown-denoised" width="250px" %}

# Installation

You could simply use our update site "[Biomedgroup](/list-of-update-sites)" to install the non local means plugin, or copy the jar file into your plugins folder.

# How to cite

We think the best way is to cite the formal method and the used implementation:

**Method:**

{% include citation %}

**Implementation:**

<a href="https://zenodo.org/badge/latestdoi/18649/thorstenwagner/ij-nl-means"><img src="/media/plugins/zenodo.35114.svg" width="174px"/></a>
