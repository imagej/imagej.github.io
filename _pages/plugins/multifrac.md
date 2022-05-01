---
mediawiki: Multifrac
title: Multifrac
categories: [Analysis, Feature Extraction, ImageJ2, Mathematical Morphology, Stacks]
doi: 10.1016/j.softx.2020.100574
---


{% capture source%}
{% include github org='ivangtorre' repo='multifrac' %}
{% endcapture %}
{% include info-box software='ImageJ / Fiji plugins' name='Multifrac' update-site='Multifrac' maintainer=' [Ivan G Torre](https://www.ivangtorre.com/)' author=' [Ivan G Torre](https://www.ivangtorre.com/)' released='06.05.2020' latest-version='06.05.2020' source=source website='/plugins/multifrac' %}

**Multifrac** is an ImageJ plugin for fractal, multifractal and scaling analysis and characterization of 2D and 3D gray and B&W stack images. It has been particularly developed for the study of CT-scan images on soil science but it is recommended for complexity analysis in any kind of image.

## Citation

Please when using the plugin, cite:

{% include citation %}

## Installation

Run {% include bc path='Help|Update...'%} and choose *Manage update sites*. Activate the *Multifrac* checkbox in the alphabetically-sorted list of update sites. Press *OK*, then *Apply changes*. Restart ImageJ. That's it. Enjoy Multifrac!

## Description

Multifrac is an ImageJ plugin for the analysis and characterization of 2D and 3D stack images. This tool is specifically designated for the analysis of soil pore structure and scaling behaviour and patterns therein. Main features of Multifrac are:

-   Monofractal analysis of black and white images
-   Multifractal analysis with box counting and gliding box methodologies ofr gray images.
-   Lacunarity analysis
-   Characteristic length and configuration entropy analysis.

This plugin has extensively used with real soil samples and results published in high impact factor journals.

## Changelog

All changes can be seen in the [GitHub source repository](https://github.com/ivangtorre/multifrac/commits/master).

**2020/05/06**: First released
