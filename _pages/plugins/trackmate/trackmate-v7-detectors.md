---
title: TrackMate v7 detectors
description: New TrackMate detectors that can return the shape of objects.
categories: [Tracking, Segmentation]
section: Detectors with segmentation capabilities.
extensions: ["mathjax"]
---
Starting with version 7.0.0, [TrackMate](/plugins/trackmate/index) offers the possibility to segment objects, and store, display and quantify their shape. We used this new API to build simple detectors that can produce objects from a *label image*, a *mask* or a *grayscale image with a threshold*. But we also  looked to integrate the state-of-the-art segmentation algorithms shipped with Fiji that do so. So we integrated the *ilastik*, *MorphoLibJ*, *StarDist*, *cellpose* and *Weka* plugins as detectors in TrackMate.
This page lists the eight detectors that have been introduced by this version, and links to their documentation and installation procedure.


## Detectors with segmentation capabilities

### Mask detector

This detector creates objects from a black and white channel in the source image. You can add the mask as an extra channel in the source image. The objects will be built based on all the pixels have a value strictly larger than 0, which solves the issue of having a mask on 8-bit, 16-bit or 32-bit images.
This detector is part of the core of TrackMate. It is documented here: [trackmate-mask-detector](/plugins/trackmate/trackmate-mask-detector)


### Thresholding detector

The thresholding detector creates objects from a grayscale image (it can be one channel in a multi-channel image). You have to specify a threshold value to segment the objects.
This detector is also part of the core of TrackMate. It is documented here: [trackmate-thresholding-detector](/plugins/trackmate/trackmate-thresholding-detector)


### Label image detector

Label images are especially convenient as an output of segmentation algorithms. Indeed, in some cases you might have different objects that are so close that they touch each other. If a segmentation algorithm can detect them, but outputs a black and white mask, they will appear as one object in the mask if they share a border.
In a label image, each object is represented by different integer values. For instance, the object #1 in a label image will be made from all the pixels that have a pixel value of 1, over a black background of 0. Object #2 will have the pixel value 2, etc. This allows resolving them even if they touch each other.
This detector is also part of the core of TrackMate. It is documented here: [trackmate-label-image-detector](/plugins/trackmate/trackmate-label-image-detector)


### TrackMate-Ilastik

This detector is not part of the core Fiji distribution. You need to subscribe to *two* update sites (The `ilastik` update site and the `TrackMate-Ilastik` update site) and to install [ilastik](http://ilastik.org/) to get it.
The detector installation procedure and its documentation can be found here: [trackmate-ilastik](/plugins/trackmate/trackmate-ilastik).


### TrackMate-MorphoLibJ

This detector is also not part of the core Fiji distribution. You need to subscribe to *two* update sites (The `IJPB-plugins` update site and the `TrackMate-MorphoLibJ` update site) to get it.
The detector installation procedure and its documentation can be found here: [trackmate-morpholibj](/plugins/trackmate/trackmate-morpholibj)


### TrackMate-StarDist

This detector is also not part of the core Fiji distribution. You need to have StarDist installed and running in your Fiji installation. This involves subscribing to the `CSBDeep` update site and the `StarDist` update site. And also to the `TrackMate-StarDist` update site.
The detector installation procedure and its documentation can be found here: [trackmate-stardist](/plugins/trackmate/trackmate-stardist)

### TrackMate-Cellpose

The integration of [cellpose](https://cellpose.readthedocs.io/en/latest/) in TrackMate is an example of a different type of integration, where we call a Python program from a Java program as a sub-process, and exchange data via files. To use cellpose with TrackMate you will need to have a working installation of cellpose on your computer, and subscribe to the `TrackMate-Cellpose` update site. 
Detailed installation procedures, documentation and tutorials can be found here: [trackmate-cellpose](/plugins/trackmate/trackmate-cellpose).

### TrackMate-Weka

This detector is also not part of the core Fiji distribution. But since the Weka Trainable Segmentation plugin is included in the core of Fiji, we just have to subscribe to the `TrackMate-Weka` update site.
The detector installation procedure and its documentation can be found here: [trackmate-weka](/plugins/trackmate/trackmate-weka)


## Limitations

The detection of object shape in TrackMate two some limitations now that we repeat here.

- **Object contours are only detected for 2D images**. 
Source images can be 2D + T with multiple channels, but shapes won't be detected, displayed nor analyzed in 3D. 
This boils down to the fact that there are no (not yet) easy and robust way to handle 3D segmentation results in Fiji.
This might change in the future with the work of others, but at least with version 7 we detect contours only for 2D images.
In the meantime, when presented with a 3D image, the detectors described above either return an error message (the StarDist detector) or create a spherical spot of radius computed so that the spherical spot has the same volume that of the 3D object returned by the specific segmentation algorithm.

- **Object contours must be simple polygons.**
Simple ploygons are ploygon made of one closed segmented line that does not have any self-intersection. 
TrackMate does not handle holes in objects, not objects made of several disconnected components.
This is a limitation that allows handling computing morphological features without ambiguity.

## Simplifying contours

Several of the new detectors have a configuration setting that allows to simplify contours. 
It is an important paramter that we describe here.

Object contours are polygon that wraps around individual objects, initially following individual pixels.
For instance, the initial output of the threshold detector for one spot looks like this:

{% include img src='/media/plugins/trackmate/trackmate-spot-contour-pixel.png' width='400'  align='center'  %}

Notice that the polygon follows exactly the contour of all pixels that are above the threshold.
For instance the leftmost pixel on the image above is has 3 segments for its border.
And all of the contour segments run along pixels horizontally or vertically.

Simplifying contour will yield a simplifed shape of the object, that interpolate betwen pixels and return a smoother shape with fewer segments. 
The same algorithm running with the `Simplify contours` parameter selected will yield the following:

{% include img src='/media/plugins/trackmate/trackmate-spot-contour-simplified.png' width='400' align='center'  %}

Simplifying contour generate TrackMate files that are smaller in disk space.
More importantly, they yield more accurate morphological features.
Indeed, the pixel-accurate contour overestimates the perimeter, because it sticks to invidual pixel borders.
In turn this generate contours that have an overestimated perimeter and will negatively affect the relevance of morphological feature that depend on it.

Simplifying contours somewhat tries to follow the object contour as if it would not be discretized over a pixel matrix.
But it works well only if the objects are large enough.
For small objects, below typically 10 pixels, the simplification generates inaccurate contours:

{% include img src='/media/plugins/trackmate/trackmate-spot-contour-small.png' width='400' align='center' %}

So as a rule of thumb we recommend the following:

- If your objects are big (N pixels larger than 10) and you want to measure their shape, always select the `Simplify contours` option.
- If your objects are sampled on a small number of pixels, it does not make sense to measure their morphology anyway. 
- So basically, unselect the `Simplify contours` only if you want to later generate a pixel-accurate mask from the objects (with for instance the `Export label image` action).

## Object morphology analysis

One of the main goal of generating the object shape is to measure their shape.
Detectors that return object contours trigger automatically the computation of morphological features in TrackMate. 
When relevant, these features use the physical calibration and units of the source image.
This means for instance that if your image is calibrated with a pixel size in µm, the area of objects will be expressed in µm².
These morphological features are:

### `Area` 
Simply the area of the objects in spatial unit squared.

### `Perimeter`
The length of the contour in spatial unit.

### `Circularity`
The circularity is a measure of how close to a circle the shape of an object is. 
It has a value of 1 for circles and is getting close to 0 for very elongated objects.
It is computed for 2D objects as 

$$
\frac{4 \times \pi \times \text{area}}{\text{perimeter}^2}
$$

### `Solidity`
The solidity ranges from 0 to 1 and reports how smooth and convex is the object contour.
A object with a dented contour, with many cavities will have a low solidity, close to 0. 
A perfectly convex object will have a value of 1.
To compute it we first determine the convex hull of the object.
Intuitively, this is the contour we would get if we would wrap a rubber band around the object. 
It would stretch around the object contour, and would not extend inside the cavities of the object.
The area of this convex object is therefore always larger than the area of the initial objet.
Then the solidity is computed as:

$$
\text{solidity} = \frac{\text{area}}{\text{convex area}}
$$

### Ellipse fit

Several 2D morphological features are best obtained by fitting on ellipse on the object contour, and reporting the ellipse parameters.
In TrackMate, we first fit an ellipse to the contour using a direct fit following the Chernov method, computed using the Moore-Penrose pseudo inverse (by Kim van der Linde) for speed and robustness.
TrackMate then reports the resulting ellipse parameters:

#### `Ellipse center x0` and `Ellipse center y0`
This the ellipse center position, with respect to the object center position.
You can get the object center position by using 
```java
double x = spot.getDoublePosition( 0 );
double y = spot.getDoublePosition( 1 );
```
to which you need to add the ellipse center values to have the absolute position of the ellipse center. 

#### `Ellipse long axis` and `Ellipse short axis`
The length of the long and short axix of the ellipse, in physical units.

#### `Ellipse angle`
The angle of the ellipse long axis with the X-axis of the image, in radians. 
Careful, in images the Y axis runs from top to bottow, so the positive angle direction is inverted compared to classical plots (positive angles are counter-clockwise) on the image.

#### `Ellipse aspect ratio`
The ellipse aspect ratio is the ratio of the major axis to the minor axis:

$$
\text{ellipse AR} = \frac{\text{major axis}}{\text{minor axis}}
$$

It ranges from 1 for ellipses that resembles circles, and gets larger for elongated ellipses.
A perfect line as a positive infinite aspect ratio.

