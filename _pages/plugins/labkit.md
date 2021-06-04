---
mediawiki: Labkit
title: Labkit

artifact: net.imglib2:imglib2-labkit
categories: []
---

<img src="/media/plugins/labkit-illustration.jpg" width="700"/>

Labkit is a plugin for:

-   automatic image segmentation
-   labeling regions of an image

The automatic image segmentation functionality is comparable to Trainable Weka Segmenation, but it's better suited for large 3d images. And it has a nice [BigDataViewer](/plugins/bdv)-based editor.

## Installation

Labkit can be installed from [its ImageJ update site](https://sites.imagej.net/Labkit/). (For details on how to install an update site click [here](/update-sites/following).)

To start Labkit in ImageJ, first open the image you want to work with, and then select {% include bc path="Plugins | Segmentation | Labkit" %} from the main menu.

## Quick Start

Follow these steps to segment an image:

1.  Open an image in ImageJ.
2.  Start Labkit by selecting {% include bc path="Plugins | Segmentation | Labkit" %} from the menu.
3.  Labkit should start and display the image. If it shows a black window instead of the image: Click {% include key key='S' %} and adjust the contrast.
4.  Select "foreground" (In the side bar of Labkit). Select the pencil tool (top bar of Labkit) and draw on the image.
5.  Select "background" and the pencil tool, and mark some other region of the image as background.
6.  In the side bar of Labkit, under the heading "Segmentation" you will find an entry "Classifier \#1". And next to it there is a play button (black triangle). Click it, to train the Classifier. After a moment you will see the automatic segmentation of your image.
7.  From Labkit's main menu select {% include bc path="Segmentation | Show Segmentation Result in ImageJ" %}, to export your segmentation into ImageJ.

## Basic Navigation

Labkit is based on BigDataViewer. Navigation the image works as in BigDataViewer, and many shortcuts work too. Click [here](/plugins/bdv) for a description of the shortcuts.

-   {% include key keys='Ctrl|Shift|mouse-wheel' %} to zoom in and out
-   {% include key keys='right-drag' %} to move the image
-   {% include key keys='left-drag' %} to rotate a 3d image
-   {% include key key='mouse-wheel' %} to scroll through the z-slices of a 3d image

## Tips & Tricks

-   If there's a black window, where the image should be? You might need to change the contrast settings: Click on the image, and then press {% include key key='S' %} on the keyboard. A dialog shows up. Use it to adjust the contrast.
-   There can be more than two labels, just click on the "Add label" button...
-   Labels can be renamed, by double clicking on them.
-   To change the label color, just click on the colored rectangle left of the labels name.
-   {% include key keys='D|mouse-wheel' %} to change the size of the brush tool.

## Drawing Tool Shortcuts

-   {% include key keys='D|left-click' %} to draw with the pencil tool.
-   {% include key keys='E|left-click' %} to erase with the pencil tool.
-   {% include key keys='F|left click' %} to use the flood fill tool.
-   {% include key keys='R|left-click' %} to remove a connected component.
-   {% include key key='N' %} - switch to next label

## Open & Save - Import & Export

-   Things you can save, open, import or export:
    -   Labeling - As `*.tif` or `*.labeling`
    -   Bitmap - (One layer of the labeling) As `*.tif`
    -   Classifier - As `*.classifier`, only Labkit is able to work with them.
    -   Segmentation result - As `*.tif`, or show to ImageJ
    -   Segmentation's probability Map - As `*.tif`, or show in ImageJ
-   The word "labeling" is used to refer to the colorfully displayed areas overlayed on top of the image.
-   Labkit's file format for labelings is `*.labeling`. It works great for very large files with very few labels. (This file format is likely to be improved and changed in the future.)
-   The labeling can be saved and opened as `*.tif` as well. (This is a good option for not-too-big images. And can be used by any other tool.)
