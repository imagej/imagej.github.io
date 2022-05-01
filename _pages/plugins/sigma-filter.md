---
mediawiki: Sigma_Filter
title: Sigma Filter
categories: [Filtering]
doi: 10.1016/0734-189X(83)90047-6
---

{% include info-box software='ImageJ' name='Sigma Filter' author='Michael Schmid and Tony Collins' filename=' [Sigma_Filter_Plus.class](https://imagej.nih.gov/ij/plugins/download/Sigma_Filter_Plus.class)' source=' [Sigma_Filter_Plus.java](https://imagej.nih.gov/ij/plugins/download/Sigma_Filter_Plus.java)' released='25 October 2007' status='1st version' category='Filtering' website='https://imagej.nih.gov/ij/plugins/sigma-filter.html' %}

## Purpose

This plugin implement a spatial filter similar to the mean filter. Its particularity is that it tries to preserve edges and to discard outliers by selecting what pixels to include in the mean.

## Documentation

This filter is based on the algorithm described in the following paper:

{% include citation %}

From the website:

"The filter smooths an image by taking an average over the neighboring pixels, but only includes those pixels that have a value not deviating from the current pixel by more than a given range. The range is defined by the standard deviation of the pixel values within the neighborhood ("Use Pixels Within ... Sigmas").

If the number of pixels in this range is too low (less than "Minimum Pixel Fraction"), averaging over all neighboring pixels is performed. With the "Outlier Aware" option, averaging over all neighboring pixels excludes the center pixel. Thus, outliers having a value very different from the surrounding are not included in the average and, thus, completely eliminated."
