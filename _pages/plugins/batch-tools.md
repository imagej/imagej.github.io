---
title: ImageJ Batch Tools
website: "https://imagej.net/plugins/batch-tools"
release-date: "20 January 2024"
initial-release-date: "26 June 2014"
dev-status: stable, active
update-site: Batch Tools

team-founder: Neville S. Ng
team-maintainer: Neville S. Ng

---

## Description 

Toolbar for batch image processing and analysis including image extraction, channel merge, composite conversion, Z-projection, channel B&C and colour adjustment, file export, and cell area, gray value & count.

Intended for handling typical light microscopy size datasets (10s-100s of images). 

## Install

- Open ImageJ and click Help -> Update...
- Click Manage Update Sites, find and enable Batch Tools by clicking the checkbox
- Click Apply and Close then Apply Changes
- After the updated successfully message appears click Ok and restart ImageJ
- On the ImageJ Toolbar, click the More Tools ">>" icon and select "Batch Tools"

## Tools
- Batch Extract
	- For extracting images from common propriatary life science files (Bio-Formats, e.g. .nd2, .lif, .lsm, etc.) to TIFF files
	- Useful for processing raw data in absence of proprietary software and when multiple samples are saved in a single file
	- Export each item/series with separate files for separate channels, or single files with merged channels
	- Processes 1 input file at a time, or all files in a directory
- Batch Merge
	- For merging multiple channels into intended channels, useful for merging individual channel files, changing channel assignments or changing channel order
	- Assumes files have been exported into individual files with channel suffix prior to file extension (e.g. suffix "_ch00.tif" of "Image1_ch00.tif")
        - Channel suffixes are entered by user to intended channels to merge as (e.g. all files with suffix "_ch00.tif" to C3 Blue)
	- Channel Order is defined based on to be assigned channel (not source channel)
		- e.g. "431" implies a final channel order of Channel 4 (Gray), Channel 3 (Blue), Channel 2 (Green) irrespective of the original image channel colour
        - Input path can be a single file or a directory 
        - In the case of a directory ALL files matching channel suffixes in selected directory will be opened for merging; remove any unintended files
- Batch Composite
	- Converts all open images to composite images
- Batch Max Intensity
	- Creates maximal intensity projections of all open images
- Batch Channel Settings
	- Adjust B&C applies the B&C of current image to all other open images, or applies Enhances Contrast to all images 
	- Adjust channel selection changes the currently selected channel to a different colour
- Batch Export
	- Exports all open images as PNG or TIFF
- Cell Analyser
	- Obtains area, mean gray value (intensity), and count of positive objects of an open image in up to 3 channels per run, with option for colocalisation based on settings defined by Cell Analyser Parameters parameters tool 
	- Optimal settings will vary per experiment
	- For each analysis channel, select file channel to analyse (0 for none), dependent mask file channel (0 for none), and whether to perform segmentation (watershed) before analysis. Segmentation may assist edge detection in clusters. 
	- Smoothing may help segregate edges on grainy images
	- Analysis mode can be set to each individual ROI (default), average of all ROI per image, or entire image (per slice per file)
	- ROI image can be optionally generated per analysis for review
	- ROI Min and Max can be adjusted by changing "Accept" to "Change" and clicking OK, this requires an open image or a newly opened one to draw example circles to calculate intended areas
	- Per run, thresholds for target ROI channels(s) are manually adjusted by user with the ImageJ Threshold tool
	- Data is saved as a .csv file in image file location
	- Data for each channel and time point/slice if applicable will be stored in area, mean and count tables cross columns, and ROI down rows
- Batch Cell Analyser 
	- Runs cell analyser on all open/newly opened images
	- First image is used as configuration for thresholding, or optionally set per image
	- Along with per-file .csv data, a summary .csv of data from each file is also generated

## Acknowledgements

All developers and maintainers of the ImageJ community.


