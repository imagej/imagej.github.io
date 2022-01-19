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

icon: /media/icons/masks-from-rois.svg

team-founders: Laurent Thomas, Pierre Trehin  
---

# Generate Masks from Rois in Fiji

## Installation
Activate the *Masks from Rois* update site (see [Activating an update site](https://imagej.net/update-sites/following)).  

Alternatively, without the Fiji updater, you can download the content of the repository, clicking the green button `code`, and choosing `Download ZIP`.  
Unzip the file, drag and drop the Fiji.app directory in the directory containing your Fiji installation (ie in the directory containing your own Fiji.app).  
This will automatically copy the files in the right location.  

In both case, make sure to restart Fiji.  
The plugins are then available at the bottom of the menu *Edit > Selection*, the  *Mask from Rois* entry.  


## Application
These plugins facilitate the generation of masks from image-regions outlined with ROIs for large datasets.  
It can be used for instance to generate ground-truth segmentation masks.  
Annotated images can be single plane images or stacks with a single dimensions slider, __HYPERSTACKS ARE CURRENTLY NOT SUPPORTED__.  
The plugin should be executed after having annotated all ROIs in an image (stored in the RoiManager), or all image-slices of a stack.   

Single images or multiple images in a stack (or Virtual stack) can be annotated. In the latter case, the Z-Position of the Rois is used to associate them to the corresponding image. One mask will be generated for every image in the stack.  

There are 2 plugins for the generation of: 

- Binary masks  
The resulting mask is black (pixel value 0) while regions outlined by rois are turned to white pixels (pixel value 255).  
Overlapping ROIs will thus be merged into a single "white blob" in the mask.  

- Multi-class/semantic mask  
This plugin takes advantage of the [group attribute of ROIs](https://f1000research.com/slides/9-183) to annotate regions belonging to the same "object-class", tissue...   
There ROIs are turned to a region with pixel values value corresponding to the ROI group. The result is a "semantic mask", where object/tissues of the same group have the same pixel value.  

Overlapping ROIs with identical group attributes will be merged into a single blob of identical pixel value.  
__Overlapping ROIs with different group attributes__ will however be assigned the pixel value of the last "painted" ROIs, ie the most bottom one in the RoiManager. 

For visualisation of such semantic masks, the plugin automatically set the "Glasbey on dark" LUT.  
When opening such saved mask, the LUT may not be automatically selected, and using a classical gray LUT does not allow to correclty visualize the mask.  
In this case, select one of the Glasbey LUT in the imageJ menu _Image > LookUp Tables_. 


## Filename suffix
When saving the mask as image files, an optional suffix can be added to the filenames, for instance if you are saving the mask in the same directory than the images.  

__Example__:  
_original.tiff_  
with suffix *-mask* and `png` extension, the mask will be    
_original-mask.png_
