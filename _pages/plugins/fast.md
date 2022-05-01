---
mediawiki: FAST
title: FAST
categories: [Analysis,Segmentation]
---

## **F**luorescence image **A**nalysi**S** **T**ool: FAST

### Description

This ImageJ macro automates tasks (open, set threshold, save Region Of Interest, measure) to process a set of single-channel fluorescence images.

## Installation

* Download the [Fiji](/software/fiji) distribution of [ImageJ](/software/imagej)/[ImageJ2](/software/imagej2).
* Use the [ImageJ Updater](/learn/updater) to [follow](/update-sites/following) the FAST update site.
* New commands should then appear in the {% include bc path='Plugins | FAST'%} menu.

## Image Processing

{% include thumbnail src='/media/plugins/fast-processing.png' title='Description of the Image processing pipeline of FAST macro.'%}

### Step 1: Auto processing of images within the selected work directory

1.  List all files containing user-defined extension (e.g. czi - zvi - tif - nd2) within selected directory and sub-directories.
2.  Apply the user-defined threshold (default 290) then analyse pixels above the threshold.
3.  Group pixels above the threshold in one Region Of Interest and save this ROI in a zip file in the image directory.

### Step 2: User confirmation of selected Regions Of Interest and measure

1.  Open images one by one to check the auto-selected ROI.
2.  User can confirm the ROI, modify it directly or remove image from further analysis.
3.  Measure of fluorescence in selected ROI.

## Startup Options

{% include thumbnail src='/media/plugins/fast-options.png' title='Options dialog box'%} The macro displays a dialog box to set analysis options:

**File type** : Select image type between CZI (Carl Zeiss Image), ZVI (Zeiss Vision Image), ND2 (Nikon) or TIFF (Tagged Image File Format).  
'Other' allow to enter a specific file extension.  
**Threshold value** : Set threshold value for pixel intensity, segmenting the image into features of interest (above threshold) and background.  

{% include notice icon="tip" content='Threshold value must be defined for each acquisition system (microscope + camera + exposure time + file-type).' %}

**Create ROIs** : Step 1, analyses pixels above the user-defined threshold value and automatically saves Regions Of Interest zip file in the image directory.  
**Measure ROIs** : Step 2 of image analysis to check individually and measure previously created ROIs. (With Step 1 unchecked and Step 2 checked, user can reanalyse previous data).  
**Overwrite existing ROIs** : If selected, the macro will overwrite ROIs zip files without prompting the user every time.  
**Silent Mode** : If selected, the macro will measure the ROI of all images without prompting the user every time. Useful for reanalysis of previous data.  
**Restart Mode** : When auto processing is cancelled accidentally, this mode checks the last ROI created and restart analysis from this point.  

## Validation of selected Regions Of Interest

<img src="/media/plugins/fast-roi-check.png" title="fig:User validation of defined ROI" width="200" alt="User validation of defined ROI" /> After completion of Step 1 of image processing, images and their corresponding ROIs need to be validated by the user.

Each image and the corresponding ROI are opened automatically. An options dialog box is displayed.

-   If the area is correct the user must click {% include button label='OK' %} to proceed with next image.
-   If the area contains non-specific signal, select {% include button label='Yes' %} to *redefine area manually* and edit the ROI.
-   The dialog box allows to exclude current image from analysis (e.g. blurred image).

Just select the radio button option needed then click {% include button label='OK' %} or {% include key key='Enter' %} to continue.

<img src="/media/plugins/fast-roi-edition.png" title="fig:Dialog box to redefine area" width="200" alt="Dialog box to redefine area" /> If you selected to *redefine area manually*, a new dialog box is displayed to get access to the ImageJ toolbar and modify the selection. The user-defined threshold is then automatically applied.

{% include img src="fast-thr-roi" width="500" caption="Example of thresholded image and corrected ROI" %}

Select the appropriate tool in ImageJ toolbar: ![](/media/freehand.png) Freehand (default) OR ![](/media/plugins/wand-tool.png) Wand tool.

-   To remove non-specific fluorescence, use selected tool and hold {% include key key='Alt' %} while unwanted area to remove it from ROI.
-   To add area to the previously selected ROI, hold {% include key key='Shift' %} while selecting new area to add.

Click {% include button label='OK' %} to confirm the new ROI. Fluorescence is then measured and the ROI zip file is automatically updated. {% include notice icon="tip" content='In case the selection is empty after manual correction, the macro discards the image from analysis.' %}

After completion of Step 2, a list of all measured images with filename is displayed in the Result Table window of ImageJ.

This table is automatically saved as a *csv* file in the work directory selected at startup.

## Related Resources

This program is free software; you can redistribute it and/or modify it under the terms of the [GNU General Public License](http://www.gnu.org/licenses/gpl.html) as published by the Free Software Foundation. [Comments or improvements are welcome](/people/cyrilturies). It is distributed in the hope that it will be useful, but **"AS IS" without warranty of any kind**. See the [GNU General Public License](http://www.gnu.org/licenses/gpl.html) for more details.

This program has been developed within the framework of the [OECD Work plan for the Test Guidelines Programme (TGP)](http://www.oecd.org/chemicalsafety/testing/oecd-guidelines-testing-chemicals-related-documents.htm) - Project 2.46: New Test Guideline for the Detection of Endocrine Active Substances, acting through estrogen receptors using transgenic cyp 19a1b-GFP Zebrafish Embryos (EASZY assay).

 
