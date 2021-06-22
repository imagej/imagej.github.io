---
title: TrackMate-Mask-Detector
description: TrackMate detector that creates objects from a mask image.
categories: [Segmentation,Tracking]
logo: /media/logos/trackmate-300p.png
project: /software/fiji
---

This page describes a detector for [TrackMate](/plugins/trackmate/index) that creates objects from a black and white channel in the source image. You can add the mask as an extra channel in the source image. The objects will be built based on all the pixels have a value strictly larger than 0, which solves the issue of having a mask on 8-bit, 16-bit or 32-bit images.

