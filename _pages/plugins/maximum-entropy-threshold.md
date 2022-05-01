---
mediawiki: Maximum_Entropy_Threshold
title: Maximum Entropy Threshold
categories: [Segmentation]
---

{% include info-box software='ImageJ' name='Maximum Entropy Threshold' author='Jerek Sacha' filename=' [Entropy\_Threshold.class](https://imagej.nih.gov/ij/plugins/download/Entropy_Threshold.class) (1,418 Bytes)' source=' [Entropy\_Threshold.java](https://imagej.nih.gov/ij/plugins/download/Entropy_Threshold.java) (2,755 Bytes)' released='13 February 2004' status='unknown' category='Segmentation' website='https://imagej.nih.gov/ij/plugins/entropy.html' %}

## Purpose

This plugin threshold an image using the Maximum Entropy algorithm, which is similar to [Otsu Thresholding](Otsu_Thresholding) technique. Here, rather than maximizing the inter-class variance (equivalently, minimizing the within-class variance), the inter-class *entropy* is maximized.

## Documentation

The plugin requires a 8-bit image to process. It outputs directly the thresholded image, replacing the original one.

It processes stacks correctly, by operating on the whole stack histogram to determine the threshold. A new, thresholded stack replace the original one.

 
