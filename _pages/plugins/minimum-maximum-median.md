---
mediawiki: Minimum/Maximum/Median
name: "Minimum/Maximum/Median"
title: Minimum/Maximum/Median
categories: [Uncategorized]
dev-status: "beta"
team-founder: '@bene51'
team-maintainer: '@bene51'
---

{% include info-box filename='VIB\_.jar' source='VIB\_.jar' %}

## Purpose

A 3D version of the minimum, maximum and median filter.

## Description

Each voxel is set to the minimum, maximum or median value of its neighborhood.

The neighborhood is defined by a kernel, which has a diameter of 3 voxels.

The image below shows the effect of each of the filters, using the MRI sample image which comes with ImageJ and Fiji.

![](/media/plugins/minmaxmedian.png)
