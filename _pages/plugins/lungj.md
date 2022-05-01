---
mediawiki: LungJ
title: LungJ
categories: [Segmentation,Binary,Filtering,Image Annotation]
doi: 10.5258/SOTON/401280
---


{% capture LWollatz -%} {% include person id='LWollatz' %} {%- endcapture %}
{% capture source -%} {% include github org='LWollatz' repo='LungJ' %} {%- endcapture %}
{% include info-box name='LungJ' author=LWollatz maintainer=LWollatz software='ImageJ/Fiji' logo='<img src="/media/icons/lungj.png" title="fig:LungJ-logo.png" width="200" alt="LungJ-logo.png" />' source=source released='Nov 10<sup>st</sup>, 2016' latest-version='0.5.1, November 10<sup>th</sup>, 2016 (LungJ v0.5.1)' status='stable, new' category='Segmentation, Binary, Filtering, Image annotation' %}


## Installation

1\) {% include bc path='Help | Update...'%}

2\) Manage update sites

3\) Add update site

4\) Name: LungJ

5\) URL: http://sites.imagej.net/LungJ/

6\) Close

7\) {% include bc path='Help | Update...'%}

8\) Restart Fiji/ ImageJ to apply changes.

9\) A new subdirectory called LungJ appears under Plugins.

10\) Future versions of LungJ will be updated together with the normal Fiji plugin updates.

## Function Documentation

### 3D Blocks - Concatenate (Concatenate\_3D)

{% include bc path='Plugins | LungJ | 3D Blocks | 3D Blocks - Concatenate'%}

Combines 3D blocks in a directory into a single image.

### 3D Blocks - Create (Subdivide\_3D)

{% include bc path='Plugins | LungJ | 3D Blocks | 3D Blocks - Create'%}

Divides a 3D image into 3D blocks and saves them into a directory along with header information in a txt file.

### 3D Blocks - Halo Exchange (Halo\_Exchange)

{% include bc path='Plugins | LungJ | 3D Blocks | 3D Blocks - Halo Exchange'%}

Exchanges the halos of a 3D Blocks image. This function can be applied between filters. Halos allow the avoidance of boundary errors/ inconsistencies.

### 3D Blocks - Histogram (Block\_Histogram)

{% include bc path='Plugins | LungJ | 3D Blocks | 3D Blocks - Histogram'%}

Opens the blocks of a 3D Blocks image, calculates all the relevant statistics and displays a histogram for all the blocks combined. Optionally saves the statistics to the properties directory.

### 3D Blocks - Run Macro (Run\_Macro\_3D)

{% include bc path='Plugins | LungJ | 3D Blocks | 3D Blocks - Run Macro'%}

Runs a macro for each 3D block in a directory and saves the resulting image blocks to a new directory.

### Apply Binary Threshold (Create\_Threshold\_Mask)

{% include bc path='Plugins | LungJ | Tools | Apply Binary Threshold'%}

Creates a truly binary mask based on a fixed global threshold.

### Apply Mask (Apply\_Mask)

{% include bc path='Plugins | LungJ | Tools | Apply Mask'%}

Applies a mask to an image, leaving the foreground as it is and replacing the background by black.

### Apply Weka Classifier (Apply\_Weka\_Classifier)

{% include bc path='Plugins | LungJ | Tools | Apply Weka Classifier'%}

Applies a Weka classifier based on the filename of an image and the filename of a classifier model. This implements the whole application process in a single function and does not require loading the original image into memory twice. This function is likely to suffer from updates to the weka-segmentation plug-in.

### Average ROIs Colour (Average\_ROI\_Colour)

{% include bc path='Plugins | LungJ | Other | Average ROIs Colour'%}

Finds the average value or RGB of active ROIs. The expected value range is overlaid on the histogram of the active image. Error calculations are based on

Keith Dear, "An Online Text in Introductory Statistics." (1999) University of Newcastle, Australia \[online\]. Was available at http://surfstat.newcastle.edu.au/ and

Hans-Jürgen Andreß "Students T-Verteilung" (2001) \[online\]. Available at http://psydok.sulb.uni-saarland.de/volltexte/2004/268/html/surfstat/t.htm, last accessed: 22. July 2015.

### Colour by Segment (Colorize\_)

{% include bc path='Plugins | LungJ | Other | Colour by Segment'%}

Combines a set of segmented images into a colour image.

### Compare Map to Mask (Compare\_MapMask)

{% include bc path='Plugins | LungJ | Statistics | Compare Map to Mask'%}

Compares a probability map to a binary masks by combining them into a single colour-coded image. Agreed foreground is white and agreed background black. Foreground detected as background is blue and background detected as foreground red.

### Compare Masks (Compare\_Masks)

{% include bc path='Plugins | LungJ | Statistics | Compare Masks'%}

Compares two binary masks by combining them into a single colour-coded image. Agreed foreground is white and agreed background black. Foreground detected as background is blue and background detected as foreground red.

### Convert Mask to STL (mask\_to\_stl)

{% include bc path='Plugins | LungJ | Other | Convert Mask to STL'%}

Takes a mask and converts and saves it as an STL file using Image Viewer 3D. This is useful if an image should be 3D printed.

### Create MCTV Tiles (Create\_MCTV\_Tiles)

{% include bc path='Plugins | MCTV | Create MCTV Tiles'%}

Creates jpg tiles and metadata file compatible with MCTV (code <doi:10.5258/SOTON/400332> , paper <doi:10.1109/eScience.2015.42>).

### Entropy

{% include bc path='Plugins | LungJ | Filter | Entropy'%}

Calls the Entropy filter from Trainable Segmentation/src/main/java/trainableSegmentation/filters/Entropy Filter.java

### Fill Holes Manual 3D (Fill\_Holes\_Manual\_3D)

{% include bc path='Plugins | LungJ | Tools | Fill Holes Manual 3D'%}

Aims to fill holes of a mask. Ideal for filling a mask with many holes in the foreground but only one or few connected background(s).

### Gabor (Weka\_Gabor)

{% include bc path='Plugins | LungJ | Filter | Gabor'%}

Applies the Gabor filter from Trainable Segmentation/src/main/java/trainableSegmentation/FeatureStack.java

### Invert Values (Invert\_Values)

{% include bc path='Plugins | LungJ | Tools | Invert Values'%}

LungJ code for inverting the values in an image. This code changes the actual values and mirrors them around the centre between minimum and maximum. Values which exceed the minimum or maximum specified are being cut of at the boundary. The GUI looks up the minimum and maximum value in an image and suggests them as defaults.

### Label Hyperstack (Label\_Hyperstack)

{% include bc path='Plugins | LungJ | Other | Label Hyperstack'%}

Consistently labels the slices of a hyperstack.

### Lipschitz

{% include bc path='Plugins | LungJ | Filter | Lipschitz'%}

Calls the Lipschitz filter from Trainable\_Segmentation/src/main/java/trainableSegmentation/filters/Lipschitz\_.java

### LungJ Settings (LungJ\_Settings)

{% include bc path='Plugins | LungJ | LungJ Settings'%}

Allows to change standard settings for LungJ. This affects mainly 3D Blocks - Run Macro but also changes the default values for some other functions.

### Matrix Operation (Matrix\_Operation)

{% include bc path='Plugins | LungJ | Filter | Matrix Operation'%}

Applies a 2D matrix onto an image. Can be used for GUI implementation of non standard matrix based filters.

### Membrane Projections (Weka\_Membrane\_Projections)

{% include bc path='Plugins | LungJ | Filter | Membrane Projections'%}

Applies the Membrane Projections filter from Trainable Segmentation/src/main/java/trainableSegmentation/FeatureStack.java

### Neighbors (Weka\_Neighbors)

{% include bc path='Plugins | LungJ | Filter | Neighbors'%}

Applies the Neighbors filter from Trainable Segmentation/src/main/java/trainableSegmentation/FeatureStack.java

### Set Calibration (Set\_Calibration)

{% include bc path='Plugins | LungJ | Other | Set Calibration'%}

Allows to set the Calibration of an image, similar to {% include bc path="Image | Properties" %} but with pixel value calibration function included.

### Stretch Histogram (Stretch\_Histogram)

{% include bc path='Plugins | LungJ | Tools | Stretch Histogram'%}

Linearly stretch the values of an image.

### Test WEKA Filter (Test\_WEKA\_Filter)

{% include bc path='Plugins | LungJ | Filter | Test WEKA Filter'%}

Allows to compare WEKA filters visually. Note that the Gabor filter is currently not working.

## Publications

Please note that LungJ, as well as other plug-ins available through Fiji, is based on a publication. If you use it successfully for your research please be so kind to cite our work:

{% include citation %}
