---
title: TrackMate-Weka
categories: [Segmentation,Tracking,Machine Learning]
icon: /media/icons/trackmate-weka.png
artifact: sc.fiji:TrackMate-Weka
---

# TrackMate-Weka.

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on the [Trainable Weka Segmentation](/plugins/tws/index) plugin to segment objects in 2D or 3D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following).

## Installation.

For this module to work, you just need to install the TrackMate module. Subscribe to the  **TrackMate-Weka** update site.

{% include img src='/media/plugins/trackmate/trackmate-weka-install.png' align='center'  %}

## Tutorial: Tracking focal adhesions.

Trainable Weka Segmentation is a machine learning pixel-based segmentation, a classifier for the objects of interest in the image is trained from user annotation, the classifier is then used for segmentation. The following image is employed to demonstrate the usage of the Weka classifier within TrackMate and can be downloaded from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5226842.svg)](https://doi.org/10.5281/zenodo.5226842)

The movie included show human dermal microvascular blood endothelial cells expressing Paxillin, imaged with a spinning-disk confocal microscope.

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image8.png' align='center'  %}

The goal is to track the focal adhesions staying at the cell periphery. 
They are in general brighter than the cell body and the image background, but with a high variance in their intensities. 

### Weka classifier.

We provide in the tutorial dataset an already trained Weka classifier for detection of the focal adhesions. 
Only the first image frame was extracted to do the annotation. The default features plus the Gabor filter were selected for training. 
The figure below illustrates the Weka GUI with two classes: one in red for focal adhesions and one in green for the others (cell body, image background). 
More details on training the classifier can be found from on the [plugin documentation page](/plugins/tws).

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image5.png' align='center'  width='400' %}

### Using Weka in TrackMate.

Now open the image in Fiji and launch TrackMate, click Next and select Weka detector from the dropdown menu

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image4.png' align='center'  width='250' %}

In the next panel, browse the classifier file, choose the target class as `FocalAdhesion` and set the threshold probability as 0.5. 

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image7.png' align='center'  width='250' %}

Click on `Preview` button to check the segmentation result, then click Next to run the segmentation for all time frames. This step takes about 8 minutes on a standard pc. 

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image2.png' align='center'  width='400' %}

Once the detection process is done, click `Next` until the step `Select a tracker`, here we choose the `Simple LAP tracker` and set the `Linking max distance` and the `Gap-closing max distance` are both equal 2.0 microns, the `Gap-closing max frame gap` is set as 2.
Click `Next` and wait for the tracking process to finish.

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image1.png' align='center'  width='250' %}


One purpose of tracking the focal adhesions is to study how they shrink or expand over time. TrackMate provides an option to color the tracks by time. Click Next until the step Display options and select Frame in Color tracks by, then click auto.

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image3.png' align='center'  width='250' %}

Looking at the tracking result shown in the movie below, the focal adhesions localizing at the top are shrinking whereas the ones at the bottom right are expanding.

{% include img src='/media/plugins/trackmate/trackmate-weka-detector-image6.gif' align='center'  %}

__________________
Minh-Son Phan, August 2021
