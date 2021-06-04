---
mediawiki: BIOP_Lookup_Tables
title: BIOP Lookup Tables
categories: []
---

{% include info-box name='BIOP luts' software='Fiji' author='Romain Guiet, Olivier Burri' maintainer='Romain Guiet' filename='biop-\*.lut' released='October 2016' latest-version='October 2016' source='PTBIOP update site' status='stable' website=' [BIOP Staff Page](http://biop.epfl.ch/INFO_Facility.html#staff)' %}

## Purpose

Having LUTs to handle display of images with more than 3 channels. Visit [Color Image Processing](/imaging/color-image-processing) page to know more about LUTs.

## Details

Classical color space are RGB and CMY. Expressed as RGB value, CMY are equal combination of 2 components of RGB, ie Cyan is obtained by combining Green and Blue in equal proportion.

[200px ](File_RGB_hex.png) [200px ](File_CMY_hex.png)

Here, we propose to use 6 LUTs, which are obtained by combining Red Green and Blue, by two, in different proportion.

[400px ](File_BIOP6Luts_hex.png)

## On 3 channels image

{% include img src="3chs-grays-cell" width="600" title="3 channels, each in Grays levels. " %}

### RGB

{% include img src="3chs-rgb-cell" width="800" title="3 channels image, in Red Green Blue and Merge. " %}

### CMY

{% include img src="3chs-cmy-cell" width="800" title="3 channels image, in Red Green Blue and Merge. " %}

## On 4 (to 6) channels image

{% include img src="4chs-grays-cell" width="800" title="4 channels image, each in Grays levels. " %}

### Appropriate BIOP-LUTs selection

{% include img src="4chs-biop-lut-cell-ok" width="1000" title="4 channels image, biop luts good choice" %}

### Unappropriate BIOP-LUTs selection

{% include img src="4chs-biop-lut-cell-bad" width="1000" title="4 channels image, biop luts poor choice" %}

Here, channels 2 and 3 are tubular structure and it's difficult to distinguish them if both are greenish.

## Macro Language

    run("biop-Amber");
    run("biop-Azure");
    run("biop-BrightPink");
    run("biop-Chartreuse");
    run("biop-ElectricIndigo");
    run("biop-SpringGreen");

## Install

You can either use our PTBIOP update site or [download biop-luts.zip](/media/plugins/biop-luts.zip) and extract to the `luts` folder.

## Notes
