---
title: TrackMate-Thresholding-Detector
description: TrackMate detector that creates objects by thresholding a grayscale image.
categories: [Segmentation,Tracking]
logo: /media/logos/trackmate-300p.png
project: /software/fiji
---

## Usage.

This page describes a detector for [TrackMate](/plugins/trackmate/index) that creates objects from a grayscale image (it can be one channel in a multi-channel image). You have to specify a threshold value to segment the objects.

## Step-by-step tutorial.

Download the tutorial dataset from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5220796.svg)](https://doi.org/10.5281/zenodo.5220796)

- Open Fiji.
- Open your image in Fiji.
- Open TrackMate {% include bc path='Plugins | Tracking | TrackMate' %}. The start panel will open and display information about your image dimensions. Click `Next`.
- The _Select a detector_ panel opens. From the pull-down menu, select `Thresholding detector`. Click `Next`.

{% include img src="/media/plugins/trackmate/trackmate-thresholding-detector-tutorial-1.png" width='250'  align='center' %}

- A panel with the description of the detector opens. You can set the threshold yourself or click on the `Auto` button for automatic thresholding. With our test image, the automatic thresholding value is 92. You can also select to `Simplify the contours` to smoothen the edges of the segmented objects. By clicking on the `Preview` button, you will see a preview of the segmentation. On the left, the number of detected objects is displayed. Once a suitable threshold has been chosen, click on `Next`.
- The objects will be detected. Click `Next` again.

{% include img src="/media/plugins/trackmate/trackmate-thresholding-detector-tutorial-2.png" width='250'  align='center' %}

- A panel to filter the detected spots according to their quality opens (more information about this filtering can be found here). With our test image, this part can be ignored. Click `Next`.
- Next, a panel to filter spots according to their properties (*i.e.* size, shape, location, or signal intensity) opens. In this exercise, do the following:
  - Click the green `+` sign at the bottom of the panel - a filter appears.
  - Click the pull-down menu and select `Area`. Here we will filter out the smallest detected objects. Make sure the `Above` button is selected.
  - Drag the horizontal line (pink dashed line) to 20. The small objects become invisible.

- Click `Next`.

{% include img src="/media/plugins/trackmate/trackmate-thresholding-detector-tutorial-3.png" width='250'  align='center' %}

- A tracking panel opens. In this panel, you can select a method for tracking your objects. In this exercise, we use the `LAP tracker`. Please select it from the pull-down menu, and click `Next`.
- A panel for the LAP tracker settings opens. First, with the `Frame to Frame linking` parameter, you give the maximum distance to link two objects between frames. Here use **20 microns**. Then, you can choose how many spots can be missing, and they could still be the same track. Tick the `Allow gap closing` box and add values: Max distance: **20 microns** and `Max frame gap`: **4**. Next, you let TrackMate know if the tracks are allowed to split. Splitting can be caused, for example, due to cell division. Tick the box `Allow track segment splitting` and insert value Max distance: **20 microns**. Below you will also see settings for Track segment merging. Here this box should remain unticked. Click `Next`.
- A Track filter panel opens. In this panel, you can filter tracks according to their properties (*i.e.*, length, speed, or location). With our test image, we do not need to filter any tracks. Click `Next`.

{% include img src="/media/plugins/trackmate/trackmate-thresholding-detector-tutorial-4.png" width='250'  align='center' %}

- A Track filter panel opens. In this panel, you can filter tracks according to their properties (i.e., length, speed, or location). With our test image, we do not need to filter any tracks. Click `Next`.

- Next, a panel with multiple display options appears. Here you can define how the objects and tracks are labelled. In this exercise, we will label the objects and tracks according to their mean speed.

- First, make sure that the `Display spots`, `as ROIs` and `Display tracks` boxes, are ticked.
- Select `Track mean speed` from the `Color spots by` and `Color tracks by` pull-down menus and click `auto`.
- In this panel, you can also export the results as CSV files. Please do so by clicking `Tracks` at the bottom of the panel. A window with a lot of data shows up. Ensure you export the `Spots` (information about the spot) and the `Tracks` (information about the tracks) files. Close the results window and click `Next`.
- You will see a plot features panel - again, click `Next`.

{% include img src="/media/plugins/trackmate/trackmate-thresholding-detector-tutorial-5.png" width='250'  align='center' %}

- In the next panel, you can perform multiple operations. For this exercise, we will export a tracking image of our experiment. Then from the pull-down menu, please select `Capture overlay`. As you click on `Execute` below, a pop-up window opens. Here you can define the time interval you want to save. You can hide the image if you wish by ticking the box `Hide image` and click `OK`. TrackMate will generate a video of the experiment. Remember to save the image with {% include bc path='File | Save as...' %}.

Joanna W. Pylvänäinen - July 2021

