---
title: BIOP Lookup Tables
name: BIOP Lookup Tables
source-url: http://biop.epfl.ch/INFO_Facility.html#staff
source-label: PTBIOP staff site
release-date: Oct 2016
dev-status: Stable
team-developers: ["@romainGuiet", "@lacan"]
team-maintainers: "@romainGuiet"
categories: [Uncategorized]
---

## Purpose

Having LUTs to handle display of images with more than 3 channels. Visit [Color Image Processing](/imaging/color-image-processing) page to know more about LUTs.

## Details

Classical color space are RGB and CMY. Expressed as RGB value, CMY are equal combination of 2 components of RGB, ie Cyan is obtained by combining Green and Blue in equal proportion.

<img src="/media/plugins/biop-lut/biop-lut-rgb-hex.png" title="fig:RGB colorspace" width="200" alt="RGB colorspace" /> <img src="/media/plugins/biop-lut/biop-lut-cmy-hex.png" title="fig:CMY colorspace" width="200" alt="CMY colorspace" />

Here, we propose to use 6 LUTs, which are obtained by combining Red Green and Blue, by two, in different proportion.

<img src="/media/plugins/biop-lut/biop-lut-biop6luts-hex.png" title="fig:6 LUTs combination" width="400" alt="6 LUTs combination" />

## On 3 channels image

<img src="/media/plugins/biop-lut/biop-lut-3chs-grays-cell.jpg" title="fig:3 channels, each in Grays levels" width="600" alt="3 channels each in Grays levels" />

### RGB

<img src="/media/plugins/biop-lut/biop-lut-3chs-rgb-cell.jpg" title="fig:3 channels image, in Red Green Blue and Merge" width="800" alt="3 channels image, in Red Green Blue and Merge" />

### CMY

<img src="/media/plugins/biop-lut/biop-lut-3chs-cmy-cell.jpg" title="fig:3 channels image, in Cyan Magenta and Yellow" width="800" alt="3 channels image, in Cyan Magenta and Yellow" />

## On 4 (to 6) channels image

<img src="/media/plugins/biop-lut/biop-lut-4chs-grays-cell.jpg" title="fig:4 channels image, each in Grays levels" width="800" alt="4 channels image, each in Grays levels" />

### Appropriate BIOP-LUTs selection

<img src="/media/plugins/biop-lut/biop-lut-4chs-biop-lut-cell-ok.jpg" title="fig:4 channels image, biop luts good choice" width="1000" alt="4 channels image, biop luts good choice" />

### Unappropriate BIOP-LUTs selection

<img src="/media/plugins/biop-lut/biop-lut-4chs-biop-lut-cell-bad.jpg" title="fig:4 channels image, biop luts poor choice" width="1000" alt="4 channels image, biop luts poor choice" />

Here, channels 2 and 3 are tubular structure and it's difficult to distinguish them if both are greenish.

## Macro Language

    run("biop-Amber");
    run("biop-Azure");
    run("biop-BrightPink");
    run("biop-Chartreuse");
    run("biop-ElectricIndigo");
    run("biop-SpringGreen");

## Install

You can either use our PTBIOP update site or download [biop-luts.zip](/media/plugins/biop-lut/biop-luts.zip) and extract to the \luts folder.
