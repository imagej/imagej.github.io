---
title: FRETENATOR
description: Fiji plugins for segmentation, object classification, ratiometric analysis and intensiometric analysis. Includes a live updating GUI interface, a headless mode, a batch mode, object labelling, object classifier training and application and Trackmate 7 integration. This is under active development (as of 2026).
update-site: FRETENATOR
source-url: https://github.com/JimageJ/FRETENATOR2
release-version: 2.5
dev-status: Active
support-status: Active
categories: [Segmentation,  Ratiometric Imaging, 3D, Analysis]
---

# FRETENATOR2- Comprehensive segmenation and ratiometric analysis

Fiji plugins for segmentation, object classification, ratiometric analysis and intensiometric analysis. Includes a live updating GUI interface, a headless mode, a batch mode, object labelling, object classifier training and application and Trackmate 7 integration. This is under active development with latest notes on this [github repository](https://github.com/JimageJ/FRETENATOR2) (as of 2026).

New FRETENATOR2.5 implemented features:

  * Improved user interface
  * Background subtraction (Global mean or Local label based)
  * Pixel by pixel processing
  * Segmentation settings saving/loading and importing from files
  * Headless mode for batch
  * 2D image processing
  * WEKA based label classifier training and classification, using graph features for context
  * Re-editing and annotation through ROI labeller
  * Help button linking to tutorials (this github readme)
  * Replaced default 'Max projection' with 'Average projection'
  * 32 bit emission ratio image outputs (no 1000X multiplied 16 bit images) with background now assigned as NaN allowing manual ROI quantification
  * Improved pixel by pixel processing - Z projections will be an average projection of the ratioed 3D image rather than Z sum projections ratioed 
  * Quickload segmentation settings buttons
  * Bug fixes
  * Separate 'Segment and intensity' plugin implementation to quantify the intensity of each channel for every ROI.

Planned features:
  * Video tutorials of new interface/features
  
### **Installation**

Installation requires Fiji and takes between 5 and 15 minutes, depending on whether the user's copy of Fiji is up to date. FRETENATOR has been tested on Windows 10, 11, Ubuntu 20, 22, and MacOS. Typical hardware requirements are up to date video card drivers including OpenCL and enough graphics RAM (or shared RAM) to handle the image you wish to process (typically 5x the image size).

Install activating update sites: 
* Click  Help>Update...
* Click Manage update sites
* Scroll down to C and make sure Clij and Clij2 are selected
* Scroll down to F and make sure FRETENATOR2 is selected
* Scroll down to I and make sure the IJPB is selected
* Accept the dialogs, allow installation, then restart ImageJ

## **_FRETENATOR2_Segment_and_ratio_**


![nlsABACUS2 confocal image](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/image20.gif)
![nlsABACUS2 segmentation performed with FRETENATOR](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/image22.gif)
![nlsABACUS2 emission ratio, with calculations performed on a per object basis](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/image21.gif)


## **Usage**:

*FN2 Segment and ratio* is a powerful plugin to quickly perform ratiometric analysis of 2D, 3D or 4D microscopy images,  with an new user interface and a live updating preview. The plugin performs full 3D segmentation of images, which means you don't analyse background, and does all the analysis, ready for you to plot and interpret. The algorithm can be used to analyse punctate sensors (e.g. nuclear localised) on a per object basis, or diffuse sensors (e.g. cytoplasmic) on a pixel by pixel basis, with quickload settings buttons. Saturated pixels are automatically removed. Settings can be saved and used for headless processing, or even batch (alpha).

  • Results Table:    ◦ Includes the ratiometric calculation (emission ratio) your channel quantifications, and x, y, z positions. This can be saved as a .csv and then analysed in python, R or excel.
  • Label map:    ◦ An image in which every nucleus is given a value that corresponds to the “label” in the results table.
  • Emission ratio map:    ◦ An image in which every nucleus is given the value of it’s emission ratio
  • Average Z projected emission ratio map:    ◦ An average Z projection of the emission ratio map
  • Nearest point emission ratio map:    ◦ A nearest point projection of the emission ratio map, with outlines added between the nuclei NB: the scale of this image is different to the original image and other images, allowing thin outlines to be drawn.
  • Log:     ◦ Details of the image file and exact analysis settings used to keep with your metadata. Savable as a .txt file


### **_FN2 Segment and ratio_ tutorial** 

[On youtube.](https://www.youtube.com/watch?v=OdPR_2kKuzg)

### **Setting LUTs and making a colourbar**

[On youtube.](https://www.youtube.com/watch?v=rTH1vWirORI)



![cytosolic ABACUS1 confocal image](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/PixelXPixel2.png)
![cytosolic ABACUS1 analysed pixel by pixel](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/pixelXpixel1.png)



### Technical implementation (jargon)

The segmentation tool works by a DoG or Gaussian filter, then Otsu to generate a binary map. An optional watershed can then be used to split objects, but a 3D watershed it a little too severe and causes the loss of many nuclei and many shrink down much smaller than their original size. By comparing my watershed to non watersheded binary maps I can create a map of the 'lost nuclei' to add them back in later. A connected components analysis is used to generate a label map of the watersheded nuclei, and then dilated the labelmap on zero pixels only to fill all the space. I then multiply this by the orginal threshold image to get a a good segmentation with good enough split objects. But this will give incorrect labelling to the 'lost nuclei' present in the image. To correct this, I run a connected components on the 'lost nuclei' map, to generate  labels, and add on the max value of the OTHER label map. Then I use maximumImage to superimpose these labels on the other label map to get my FINAL label map.

The software will then use the segmentation to quantify statistics (postion, intesnity etc) for each nucleus for the chosen channel.
Built upon the nuclear segmentation tool. Gives a dialog with segmentation settings, which can be adjusted in real time with a live labelmap max projection preview of frame 1. Pleasse note that the DoG filter and tophat background subtraction are only used to segment the image and are not applied to the channels to be quantified.

The chosen settings will then be applied to the time series and the data for emission ratio calculation etc are output to a results table. This is useful for ratiometric biosensors. Voxels saturated in the **Donor** or **Emission (FRET)** channels are excluded from analysis.

The "nearest point Z projection" option has outline drawing between segmented objects. This will make pretty Z projections where the different objects are discernable and overlayed properly.

There are two background subtraction methods. Global mean subtraction, subtracts the average intensity of the are excluded from segmentation in each channel from each pixel before performing calculation - this is good for the global background signal that is present in many camera/detector types. Local label based subtraction will process each ROI object individually, subtracting the average intensity of nearby pixels in the excluded area surrounding it, which is good for global background as well as local background such as light scattering/autofluorescence.

## **_FN2_SaR_Headless_**

Uses the last saved settings of FRETENATOR2_Segment_and_ratio, and performs analysis without opening a dialog box (faster).


## **_FN_SaR_Batch_ (alpha)**

*Currently only reliable when run from the script editor* Uses the last saved settings of FRETENATOR2_Segment_and_ratio, and performs analysis on all images in a user defined folder, then exports the analysis into another user defined folder.


## **_FN_ROI_Labeller_**

### Implementation and usage

A follow on tool for after segmentations where users can categorise the ROI in their segmented images. As a work in progress, it currently works on single timepoint 3D label images, allowing users to visually assign labels to one of 10 categories. Results are either output to an existing results table or can be used to measure a chosen image. ***Alpha functionality:*** In the latest version, time course analysis can be performed, but usage asumes the same label usage through time (making it compatable with Trackmate exported files - see below).

**Usage:**
FRETENATOR ROI Labeller tutorial
[On youtube.](https://www.youtube.com/watch?v=EKXR4z5g8Pg)

## **_FN_Trackmate_Bridge_ (Alpha)**

A simple plugin to allow **Trackmate 7** analysed label images (Analyse the FRETENATOR label map for tracking then export the tracked label map as dots) to be combined with **FRETENATOR_Segment_and_ratio** output. This adds TrackIDs to the results table and creats a new TrackID labelmap that can be analysed with the ROI manager.

![Stomata](https://github.com/JimageJ/FRETENATOR2/blob/main/imagefiles/image29.gif)
![Stomata ROI labeled image after tracking with Trackmate](https://github.com/JimageJ/ImageJ-Tools/blob/master/images/labeled%20stomata.gif)

## **_FRETENATOR2_Segment_and_ratio_BT_ (Alpha)**

A specialised version of FRETENATOR2_Segment_and_ratio, developed for Tang et al 2025, which measures the fluorescence of an additional channel, in a dilated area surrounding and including the original ROI. This allows nearby fluorescence to be quantified and is included on the results table. Please select 'Local Label Based' from the "Background Subtraction Method" to use this functionality. This will be added as a new column to the results table.


## **Troubleshooting**

All these plugins use CLIJ/CLIJ2 to process images on the graphics card. This means image processing is lightning fast, but also means there are sometimes errors/crashes.

The majority of these crashes are due to one of two reasons:
**i.** the image stack being too large to process on the graphics card this can be solved by using a computer with more video memory, or scaling/cropping the images to be smaller. Normally 4-5x the image size is required in video memory. Running Plugins>ImageJ on GPU (CLIJ2)>Macro tools>CLIJ2 Clinfo will allow you to select GPU and provide info on the hardware’s maximum image size.

or **ii.** out of date graphics card drivers. This often presents with black/blank images. This can often be solved by downloading the latest drivers from the manufacturer website (usually AMD, Nvidia or intel). 
