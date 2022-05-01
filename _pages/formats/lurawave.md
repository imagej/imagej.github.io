---
title: LuraWave
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
---

If you have Flex files from an older Opera system, you may receive a message from [Bio-Formats](/formats/bio-formats) stating that you need a LuraWave LWF license code to decode these files.

## Decoding Flex files using the MBF distribution

The [MBF Plugin Collection](/software/mbf-imagej) legally bundles the LuraWave LWF decoder module: [McMaster University](http://www.mcmaster.ca/) purchased a redistributable license from LuraTech (see below).

Steps to use:

1.  [Download ImageJ](https://imagej.nih.gov/ij/download.html) and unpack it
2.  [Download the MBF Plugins Collection](https://imagej.nih.gov/ij/plugins/mbf/)
3.  Merge the MBF plugins into your ImageJ folder
4.  Use {% include bc path='File | Open...'%} to convert your .flex files to OME-TIFF using [Bio-Formats](/formats/bio-formats)

Unfortunately, for legal reasons, we cannot elaborate on the technical details of how the MBF collection provides this functionality, nor can we legally make this feature available within [ImageJ2](/software/imagej2) or [Fiji](/software/fiji).

## Purchasing your own license

Alternately, the LuraWave decoder is proprietary software which you can (theoretically) purchase from [LuraTech](https://www.luratech.com/en/). However, we do not know the details of who to contact, nor how much it costs to do so. In October of 2015 Foxit Corporation acquired LuraTech Imaging GmbH.

## See also

-   {% include citation id="formats/bio-formats" %}
-   [OME Blog - Supporting complex formats - what we will and won't do, and what you can do to help](http://blog.openmicroscopy.org/file-formats/community/2016/01/06/format-support/)
-   [Why scientists should use open source software](/licensing/open-source)
