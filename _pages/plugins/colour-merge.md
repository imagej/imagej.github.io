---
mediawiki: Colour_merge
title: Colour merge
categories: [Color Processing]
project: /update-sites/cookbook
---

{% include info-box software='ImageJ' name='Colour merge' author='unknown' filename='Colour\_merge.class' source='not found' released='unknown' latest-version='unknown' status='unknown' category='Color Processing' %}

## Purpose

This plugin allows you to merge two grayscale stacks into a single RGB stack. It is useful e.g. to merge a brightfield with the corresponding fluorescence image, or two different dye images of the same series.

## Documentation

Adapted from the [MBF ImageJ](/software/mbf-imagej) manual:

The {% include bc path='Plugins | Color functions | Color Merge'%} function gives the user the option of using the **Difference** arithmetic processing on the image stacks you select. This is not strictly a merge (when cyan and magenta merge they produce white, not yellow) but facilitates visualization of the separate channels[^1]. You can perform a true merge if you turn off the "Difference" option.

Run the plugin and select the two images or stacks to be merged. It can be 8-bit, 16-bit, RGB... Select the desired colors from the drop-down options. <Current> uses the LUT that the image currently has (this is often the desired LUT). The "Difference" option performs a "difference" arithmetic operation rather than a "addition". If the "Pre-sub 2 from 1" option is checked the second image is subtracted from the first prior to merging.

## References

[^1]: {% include citation doi='10.1046/j.1365-2818.1997.1470704.x' %}
