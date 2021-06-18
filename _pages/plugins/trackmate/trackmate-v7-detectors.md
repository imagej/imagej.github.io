---
title: TrackMate v7 detectors
description: New TrackMate detectors that can return the shape of objects.
categories: [Tracking, Segmentation]
logo: /media/logos/trackmate-300p.png
project: Fiji
section: Detectors with segmentation capabilities.
---
Starting with version 7.0.0, [TrackMate](/plugins/trackmate/index) offers the possibility to segment objects, and store, display and quantify their shape. We used this new API to build simple detectors that can produce objects from a *label image*, a *mask* or a *grayscale image with a threshold*. But we also  looked to integrate the state-of-the-art segmentation algorithms shipped with Fiji that do so. So we integrated the *ilastik*, *MorphoLibJ*, *StarDist* and *Weka* plugins as detectors in TrackMate.
This page lists the seven detectors that have been introduced by this version, and links to their documentation and installation procedure.


## Detectors with segmentation capabilities.

### Mask detector.

This detector creates objects from a black and white channel in the source image. You can add the mask as an extra channel in the source image. The objects will be built based on all the pixels have a value strictly larger than 0, which solves the issue of having a mask on 8-bit, 16-bit or 32-bit images.
This detector is part of the core of TrackMate. It is documented here: [trackmate-mask-detector](/plugins/trackmate/trackmate-mask-detector)


### Thresholding detector.

The thresholding detector creates objects from a grayscale image (it can be one channel in a multi-channel image). You have to specify a threshold value to segment the objects.
This detector is also part of the core of TrackMate. It is documented here: [trackmate-threholding-detector](/plugins/trackmate/trackmate-thresholding-detector)


### Label image detector.

Label images are especially convenient as an output of segmentation algorithms. Indeed, in some cases you might have different objects that are so close that they touch each other. If a segmentation algorithm can detect them, but outputs a black and white mask, they will appear as one object in the mask if they share a border.
In a label image, each object is represented by different integer values. For instance, the object #1 in a label image will be made from all the pixels that have a pixel value of 1, over a black background of 0. Object #2 will have the pixel value 2, etc. This allows resolving them even if they touch each other.
This detector is also part of the core of TrackMate. It is documented here: [trackmate-label-image-detector](/plugins/trackmate/trackmate-label-image-detector)


### TrackMate-Ilastik.

This detectors is not part of the core Fiji distribution. You need to subscribe to *two* update sites (The `ilastik` update site and the `TrackMate-Ilastik` update site) and to install [ilastik](http://ilastik.org/) to get it.
The detector installation procedure and its documentation can be found here: [trackmate-ilastik](/plugins/trackmate/trackmate-ilastik).


### TrackMate-MorphoLibJ.

This detectors is also not part of the core Fiji distribution. You need to subscribe to *two* update sites (The `IJPB-plugins` update site and the `TrackMate-MorphoLibJ` update site) to get it.
The detector installation procedure and its documentation can be found here: [trackmate-morpholibj](/plugins/trackmate/trackmate-morpholibj)


### TrackMate-StarDist.

This detectors is also not part of the core Fiji distribution. You need to have StarDist installed and running in your Fiji installation. This involves subscribing to the `CSBDeep` update site and the `StarDist` update site. And also to the `TrackMate-StarDist` update site.
The detector installation procedure and its documentation can be found here: [trackmate-stardist](/plugins/trackmate/trackmate-stardist)


### TrackMate-Weka.

This detectors is also not part of the core Fiji distribution. But since the Weka Trainable Segmentation plugin is included in the core of Fiji, we just have to subscribe to the `TrackMate-Weka` update site.
The detector installation procedure and its documentation can be found here: [trackmate-weka](/plugins/trackmate/trackmate-weka)


## Limitations.

## Simplifying contours.

## Object morphology analysis.



