---
mediawiki: 3D_Binary_Filters
name: "Minimum/Maximum/Median"
title: 3D Binary Filters
categories: [3D, Binary]
release-date: "3.0.0, December 17, 2015"
dev-status: "beta"
team-founder: '@bene51'
team-maintainer: '@bene51'
---


{% capture filename %}
{% include maven g='sc.fiji' a='VIB_' %}
{% endcapture %}

{% capture source %}
{% include github org='fiji' repo='VIB' %}
{% endcapture %}
{% include info-box filename=filename source=source  %}

## Purpose

A 3D version of binary filters like erode and dilate.

## Description

These plugins require an 8-bit image and apply the corresponding filter to the specified iso-value.

The applied kernel has a diameter of 3 voxels.

The image below shows the effect of the 'Erode' and 'Dilate' filters, using the Bat Cochlea image which comes as one of ImageJ's and Fiji's sample images. Both filters are applied three times, to make the effect clearer.

![](/media/plugins/erodedilate.png)
