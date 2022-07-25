---
mediawiki: Ellipse_split
name: "Ellipse Splitting Plugin"
title: Ellipse split
doi: 10.5281/zenodo.834339
categories: [Uncategorized]
release-date: "v0.4.0 (15 May 2016)"
dev-status: "active"
team-founder: "@thorstenwagner"
team-maintainer: "@thorstenwagner"
---

{% include info-box filename='ij-ellipsesplit.jar [\[1](https://github.com/thorstenwagner/ij-ellipsesplit/releases/latest) \]' source='Github [\[2](https://github.com/thorstenwagner/ij-ellipsesplit) \]'  %}

## Purpose

The ellipse splitting plugin splits binary objects which could approximated by an ellipse. The used ellipse fitting algorithm was proposed in

*A. Fitzgibbon, M. Pilu, and R. B. Fisher, "Direct least square fitting of ellipses," IEEE Trans. Pattern Anal. Mach. Intell., vol. 21, no. 5, pp. 476–480, May 1999.*

Here we used the implementation of [BoneJ](https://fiji.sc/BoneJ).

The general approach of the ellipse fitting plugin is as follows:

1. Given the binary input image I
2. Then image W is the split using ImageJ's watershed approach
3. XOR I and W to get all watershed lines L
4. Extract all contours in W using ijblob
5. Remove those parts of the contours which are neighbor of L
6. Fit an ellipse to each remaining contour part
7. Merge ellipses if possible
8. Filter ellipses by geometric features

## Examples

Suppose you have the following input image:

<figure><img src="/media/plugins/ellipsesplit-input.png" title="Ellipsesplit_input.png" width="300" alt="Ellipsesplit_input.png" /><figcaption aria-hidden="true">Ellipsesplit_input.png</figcaption></figure>

Then the watershed approach ({% include bc path="Process | Binary | Watershed" %}) would give this result:

<img src="/media/plugins/ellipsesplit-watershed.png" width="300"/>

The ellipse splitting plugin applied to the input image will combine the watershed result and direct ellipse fitting. This leads to the following result:

![](/media/plugins/ellipsesplit-result.png)

Furthermore it outputs several important features:

<img src="/media/plugins/ellipsesplit-resultstable.png" width="600"/>

## Parameters

{% include img src="ellipsesplit" width="350" caption="GUI of Ellipse Split Plugin" %}

**Binary splitted image:** If set to "Use standard watershed" it will use ImageJ's watershed technique to split the binary object. If there are better techniques for splitting available, you could select here the binary image splitted by that technique.

**Add to manager:** (true/false) If true, the ellipses will be added to the ROI manager.

**Add to results table:** (true/false) If true, some geometrical features of the ellipses will be added to the results table.

**Overlap threshold in %:** If the image is oversegmentated, two ellipses could belong the same real object. If that is the case, it is likely that the ellipses are strongly overlapping. In those cases the ellipses will be merged. The *overlap threshold in %* is the proportion of one ellipse containing another ellipse.

**Major axis length:** The length of major axis.

**Minor axix length:** The length of minor axis.

**Aspect ratio:** Ratio of Major axis length and minor axis length.

## Installation

Simply turn on the [Biomedgroup update site](https://fiji.sc/How_to_follow_a_3rd_party_update_site), which includes the ellipse splitting plugin.

If you use ImageJ just copy the ij-ellipessplit.jar file in your plugins folder and copy the [GPCJ 2.2.0](http://sourceforge.net/projects/geom-java/files/gpcj/) and the latest [ij-blob](https://fiji.sc/IJ_Blob) jar file into the plugins/jars folder.

## How to cite

Please get the lastest DOI for this plugin here: https://zenodo.org/badge/latestdoi/18649/thorstenwagner/ij-ellipsesplit
