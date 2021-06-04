---
mediawiki: Granulometric_Filtering
title: Granulometric Filtering
categories: [Particle Analysis]
doi: 10.1016/j.jneumeth.2005.07.011
---

{% include info-box software='ImageJ' name='Granulometric Filtering' author='Dimiter Prodanov' filename=' [Gran_Filter.jar](/ij/plugins/download/jars/Gran_Filter.jar) (39,559 Bytes)' source='in .jar file' released='21 May 2005' latest-version='' status='unknown' category='' website='/ij/plugins/gran-filter.html' %}

## Purpose

This plugin can be used to identify and select structure of a certain size in a B&W image. It allows e.g. to get all circular structure of a certain radius within an image.

## Documentation

The figure is sieved with a structuring element of increasing size. Each sieving step removes structures with sizes that matches or are smaller that the structuring element size. Individual size disks are obtained by subtracting derived images (e.g. to obtain 10 px radius size, one subtract the image obtained after sieving by a structuring element of size 10 by the image sieved with size 9).

**Plugin parameters**

-   *Type of structure element*: select between circle, diamond, square, and lines to identify corresponding shape
-   *Radius of structure element*: the minimal size (radius in pixel) of the structuring element to apply
-   *Step*: the maximal size of the structuring element will be the previous value plus this one

For example, to detect all circular shapes whose radii are between 10 and 12 pixels, one would select *circle*, *10*, *2* respectively as parameters.

The plugin also works on grayscale images, tough it gives difficult to interpret results.

## Publication

This plugin and technique is described by its author (and colleagues) in the following paper, where more documentation can be found:

{% include citation %}
