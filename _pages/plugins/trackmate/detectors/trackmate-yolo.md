---
title: TrackMate-YOLO
categories: [Detection,icTracking,Deep Learning]
icon: /media/icons/YOLO-logo.png
description: Cellpose-SAM integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-YOLO
---

{% include img src="/media/plugins/trackmate/detectors/cellpose/trackmate-cellpose-sam-R2_multiC.gif" width='400'  %} {% include img src="/media/plugins/trackmate/detectors/cellpose/trackmate-cellpose-sam-01.png"  width='200' %}

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [YOLO](https://github.com/ultralytics/ultralytics), an AI-based detection algorithm, popular for natural images. 
It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following). 
It also requires YOLO to be installed on your system and working independently. 

If you use this detector for your research, please cite the YOLO webiste

_Jocher, G., Qiu, J., & Chaurasia, A. (2023). Ultralytics YOLO (Version 8.0.0) [Computer software]. https://github.com/ultralytics/ultralytics_


## Installation

We need to subscribe to an extra update site in Fiji, and have a working installation of cellpose on your system.

### TrackMate-YOLO update site

In Fiji, go to {% include bc path='Help|Update...' %}. Update and restart Fiji until it is up-to-date. Then go to the update menu once more, and click on the `Manage update sites` button, at the bottom-left of the updater window. A new window containing all the known update sites will appear. Click on the  **TrackMate-YOLO** check box and restart Fiji one more time. 



### Cellpose-SAM