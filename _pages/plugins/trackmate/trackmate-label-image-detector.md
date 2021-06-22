---
title: TrackMate-Label-Image-Detector
description: TrackMate detector that creates objects from a label image.
categories: [Segmentation,Tracking]
logo: /media/logos/trackmate-300p.png
project: /software/fiji
---

This page describes a detector for [TrackMate](/plugins/trackmate/index) that creates objects from a label image image. 

Label images are especially convenient as an output of segmentation algorithms. Indeed, in some cases you might have different objects that are so close that they touch each other. If a segmentation algorithm can detect them, but outputs a black and white mask, they will appear as one object in the mask if they share a border.
In a label image, each object is represented by different integer values. For instance, the object #1 in a label image will be made from all the pixels that have a pixel value of 1, over a black background of 0. Object #2 will have the pixel value 2, etc. This allows resolving them even if they touch each other.

You can use a label image as a channel in your source image, since TrackMate can harness multi-channel image. The image types does not have to be of integer type; but the labels need to be integers even on a float type.

