---
title: Mask(s) from ROI(s)
name: Mask(s) from ROI(s)
description: Generate mask images (0/255) from list of ROIs
categories: 
  - Image Annotation
  - Segmentation

source-url: https://github.com/LauLauThom/MaskFromRois-Fiji
release-date : 2021

license-url: /licensing/mit
license-label: MIT

team-founders: Laurent Thomas
---

# Generate Masks from Rois in Fiji

<img src="https://github.com/LauLauThom/MaskFromRois-Fiji/blob/main/GUI.png" width=50% height=50%>

This plugin facilitates the generation of mask images (0/255) from image-regions outlined with ROIs for large datasets.  
It can be used for instance to generate ground-truth mask annotations.  
Annotated images can be single plane images or stacks with a single dimensions slider, HYPERSTACKS ARE CURRENTLY NOT SUPPORTED.  

This plugin should be called after annotating image-regions with ROIs, stored in the RoiManager.  
Single images or multiple images in a stack (or Virtual stack) can be annotated. In the latter case, the Z-Position of the Rois is used to associate them to the corresponding image.

For each image (or stack slice), a mask image is generated with regions outlined by rois represented by white-pixels (value=255), while the background area is black (value=0).
Overlapping ROIs will result in a single "white blob" in the mask. 

The plugin should be executed after having annotated all ROIs in an image, or all image-slices of a stack.  

## Mask images
The resulting mask images (0/255 pixel values) can be displayed in ImageJ, and saved to a custom directory on disk, in one of the proposed format.    
Filenames for the mask will be identical to the original filename when available (read from the fileinfo, slice label or window title).  

## Filename suffix
An optional suffix can be added to the filenames, for instance if you are saving the mask in the same directory than the images.  

__Example__:  
original.tiff  
with suffix *-mask* and `png` extension  
original-mask.png

## Installation
The plugin can be installed by activating the MasksFromRoi update site (soon).  
The plugin is then available in the menu *Edit > Selection > Mask(s) from Roi(s)*.
