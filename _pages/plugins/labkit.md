---
mediawiki: Labkit
title: Labkit

artifact: net.imglib2:imglib2-labkit
categories: [Uncategorized]
---

<img src="/media/plugins/labkit-illustration.jpg" width="700"/>

Labkit is a user-friendly Fiji plugin for the segmentation of microscopy image data. 
It offers easy to use manual and automated image segmentation routines that can be rapidly applied to single- and multi-channel images as well as timelapse movies in 2D or 3D. 
Labkit is specifically designed to work efficiently on big image data.
Users of consumer laptops can conveniently work with multiple terabytes large image data. 
This efficiency is achieved by using Imglib2 and Big Data Viewer as the foundation of our software. Additionally, manual tools for ground-truth annotation are available. Furthermore, memory efficient and fast random forest based pixel classification based on the Waikato Environment for Knowledge Analysis (WEKA) is implemented, optionally exploiting the power of graphics processing units (GPUs) to gain additional performance. 
Labkit is easy to install on virtually all laptops and workstations.
Additionally, Labkit is prepared to be used on high performance computing clusters (HPC) for distributed processing of big image data. 

## Installation

There are two options for the installation of Labkit. Option A: The basic installation (without GPU acceleration) that works on all computers. Option B: The installation with GPU acceleration. (better performance, but requires an NVIDIA GPU).

### Option A: Basic Installation
1. Install Fiji
2. Install the [Labkit update site](https://sites.imagej.net/Labkit/). (For details on how to install an update site click [here](/update-sites/following).)

### Option B: Installation With GPU Support
(Requires a NVIDIA GPU, and propery installed graphics card drivers.)
1. Install Fijij
2. Install the “clij” and “clij2” update sites in Fiji. (see https://clij.github.io/clij2-docs/installationInFiji for details)
4. Install the “Labkit-Preview” update site, URL: https://sites.imagej.net/Labkit-Preview/
   (This update site is not in the list of official update sites. It needs to be added first.) 


## Tutorials

### Quick Start Tutorial

Follow these steps to segment an image:

1.  Open an image in ImageJ.
2.  Start Labkit by selecting {% include bc path="Plugins | Segmentation | Labkit" %} from the menu.
3.  Labkit should start and display the image. If it shows a black window instead of the image: Click {% include key key='S' %} and adjust the contrast.
4.  Select "foreground" (In the side bar of Labkit). Select the pencil tool (top bar of Labkit) and draw on the image.
5.  Select "background" and the pencil tool, and mark some other region of the image as background.
6.  In the side bar of Labkit, under the heading "Segmentation" you will find an entry "Classifier \#1". And next to it there is a play button (black triangle). Click it, to train the Classifier. After a moment you will see the automatic segmentation of your image.
7.  From Labkit's main menu select {% include bc path="Segmentation | Show Segmentation Result in ImageJ" %}, to export your segmentation into ImageJ.

### GPU Accelleration

Make sure you installed Labkit with GPU support. Labkit can be used the same way as discribed above, with one additional step to enable the GPU acceleration.
Open the "Classifier Settings" and select "Use GPU acceleration".

### Manual Segmentation

See https://github.com/juglab/EmbedSeg/wiki/Use-Labkit-to-prepare-instance-masks.

#### Workaround for plane wise manual segmentation of 3D images.

Before starting Labkit, convert the image into a 2D + time by selecting (Image > Hyperstacks > Reorder Hyperstack...)

### Segmenting a list of images with the macro recordable command

### Segmenting a large image on a Cluster

### Tips & Tricks

-   If there's a black window, where the image should be? You might need to change the contrast settings: Click on the image, and then press {% include key key='S' %} on the keyboard. A dialog shows up. Use it to adjust the contrast.
-   There can be more than two labels, just click on the "Add label" button...
-   Labels can be renamed, by double clicking on them.
-   To change the label color, just click on the colored rectangle left of the labels name.
-   {% include key keys='D|mouse-wheel' %} to change the size of the brush tool.

### Open & Save - Import & Export

-   Things you can save, open, import or export:
    -   Labeling - As `*.tif` or `*.labeling`
    -   Bitmap - (One layer of the labeling) As `*.tif`
    -   Classifier - As `*.classifier`, only Labkit is able to work with them.
    -   Segmentation result - As `*.tif`, or show to ImageJ
    -   Segmentation's probability Map - As `*.tif`, or show in ImageJ
-   The word "labeling" is used to refer to the colorfully displayed areas overlayed on top of the image.
-   Labkit's file format for labelings is `*.labeling`. It works great for very large files with very few labels. (This file format is likely to be improved and changed in the future.)
-   The labeling can be saved and opened as `*.tif` as well. (This is a good option for not-too-big images. And can be used by any other tool.)

## Keyboard Shortcuts

### Basic Navagation

Labkit is based on BigDataViewer. Navigation the image works as in BigDataViewer, and many shortcuts work too. Click [here](/plugins/bdv) for a description of the shortcuts.

-   {% include key keys='Ctrl|Shift|mouse-wheel' %} to zoom in and out
-   {% include key keys='right-drag' %} to move the image
-   {% include key keys='left-drag' %} to rotate a 3d image
-   {% include key key='mouse-wheel' %} to scroll through the z-slices of a 3d image


### Drawing Tool
-   {% include key keys='D|left-click' %} to draw with the pencil tool.
-   {% include key keys='E|left-click' %} to erase with the pencil tool.
-   {% include key keys='F|left click' %} to use the flood fill tool.
-   {% include key keys='R|left-click' %} to remove a connected component.
-   {% include key key='N' %} - switch to next label
