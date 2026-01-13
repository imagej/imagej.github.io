---
title: TrackMate Detectors
description: Documentation of some of the detectors used in TrackMate.
extensions: ["mathjax"]
---

Spot detectors are [TrackMate](/plugins/trackmate) modules that detect objects in an image. 
They are detection or segmentation algorithms that produce objects that will be later filtered then tracked with other TrackMate modules. 

In TrackMate, there is two kind of detectors:

- **Spot detectors.** They can _detect_ objects, that is: they output spots characterized only by their X, Y, Z position and a radius.
These spots have no shape information.
The detection algorithms are typically fast and robust and work in 2D and 3D indifferently.

- **Segmenters.** These detectors are a novelty introduced with TrackMate v7. 
They can _segment_ objects, that is: they output the objects shape which can be used later to get morphological descriptors and accurate intensity measurements in objects.
As of today, TrackMate is limited to segmenting objects for 2D images.
Some segmenters work on 3D images, but output objects as shapeless spots.


## Spot detectors.

This class of detectors are used to identify sub-resolved particles or roundish, shapeless objects in images.
They are suitable when the shape of the objects you want to track is not relevant for the downstream analysis. 

##### Laplacian of Gaussian (LoG) detector
Builtin.

The go-to detector for sub-resolved particles or roundish objects. 
Check this [tutorial](/plugins/trackmate/tutorials/getting-started) for documentation about this detector.

##### Difference of Gaussian (DoG) detector
[difference-of-gaussian](difference-of-gaussian) - builtin 

Similar approach to that of the LoG detector, but uses an approximation that makes this detector faster for very small objects.

##### Hessian detector
[hessian-detector](hessian-detector) - builtin 

This detector extends the LoG and DoG detector above, and that are based on the Laplacian of images. 
It is based on the Hessian matrix, and is a bit slower compared to these two. 
However, it is more accurate for spots that appeats next to the border of a large objects,  its accuracy in 3D can be improved by specifying a different object shape in XY and Z, and it can process separately multiple ROIs in an image.


##### Spotiflow
[trackmate-spotiflow](trackmate-spotiflow)

Use [Spotiflow](https://github.com/weigertlab/spotiflow) to detect spots using deep-learning models. 
This tool can retrieve automatically the size of spots, get their position with sub-pixel accuracy. 
Models shipped with the tool have a good robustness against varying background and non-specific staining.

##### YOLO
[trackmate-yolo](trackmate-yolo)

Use [Ultralytics' YOLO](https://github.com/ultralytics/ultralytics) implementation in Python to detect various objects in images. 
The TrackMate integration runs the detection pipeline of YOLO, and return the bounding box approximated as TrackMate spot circle or sphere.

## Segmenters.

The new detectors introduced in the version 7 of TrackMate and that can segment objects in 2D are introduced [here](trackmate-v7-detectors). The new detectors introduced with version 8 of TrackMate were first announced [on the ImageJ forum](https://forum.image.sc/t/trackmate-v8-segmentation-editor-and-python-cli-integration/117737)

Individual documentation pages:

##### Mask detector
[trackmate-mask-detector](trackmate-mask-detector)

Import black and white masks as objects in TrackMate.

#####  Thresholding detector
[trackmate-thresholding-detector](trackmate-thresholding-detector)

Threshold a grayscale channel to generate objects in TrackMate.

#####  Label image detector
[trackmate-label-image-detector](trackmate-label-image-detector)

Import a label image as objects in TrackMate.

#####  TrackMate-Ilastik
[trackmate-ilastik](trackmate-ilastik)

Use a pixel classifier model trained with [ilastik](https://www.ilastik.org/) in TrackMate.

#####  TrackMate-MorphoLibJ
[trackmate-morpholibj](trackmate-morpholibj)

Use the [morphological segmentation](https://imagej.net/plugins/morphological-segmentation) plugin of the [MorphoLibJ](https://imagej.net/plugins/morpholibj) library to detect objects by their boundaries. 

#####  TrackMate-StarDist
[trackmate-stardist](trackmate-stardist)

Use the [StarDist](https://imagej.net/plugins/stardist) implementation of Fiji to detect nuclei and star-convex objects in fluorescence images. 
Ships two versions of the detector: a basic one that works with the fluorescent nuclei model, and an advanced one that allows specifying a custom model and fine tuned detection parameters.

#####  TrackMate Cellpose and Omnipose
A single update site ships five detectors: Two for Cellpose (for Cellpose version 3.1.1.2, simple and advanced), two for omnipose (the same), one one for Cellpose-SAM (starting version 4).
- TrackMate-Cellpose (for v3.1.1.2): [trackmate-cellpose](trackmate-cellpose)
- TrackMate-Cellpose-SAM (v4 and beyond) [trackmate-cellpose-sam](trackmate-cellpose-sam)
- TrackMate-Omnipose [trackmate-omnipose](trackmate-omnipose)

##### TrackMate-Weka
[trackmate-weka](trackmate-weka) 

Runs a [Weka](https://imagej.net/plugins/tws/) pixel classifier to detect objects. 


## Spot features generated by the spot detectors

Features in TrackMate are numerical values defined for one of the TrackMate objects.
All detectors must at least provide the following common spot features:

-   `X`, `Y`, and `Z`: the spot coordinates in space. Coordinates are expressed in physical units (μm, ...).
-   `R` the spot radius, also in physical units. The current detectors only set this radius value to be the one specified by the user. More advanced detectors - yet to be implemented - could retrieve each spot radius from the raw image.
-   `Quality`: The implementation varies greatly from detector to detector, but this value reflects the quality of automated detection. It must be a positive real number, large values indicating good confidence in detection result for the target spot. This sole feature is then used in the initial filtering step, where spots with a quality lower that a specified threshold are purely and simply discarded.

The two other time features - `T` and `FRAME` number - are set by TrackMate itself when performing detection on all the timepoints of the target raw data. `T` is expressed in physical units, and the `FRAME` number - starting from 0 - is simply the frame the spot was found in.


### Object morphology analysis

One of the main goal of generating the object shape is to measure their shape.
Detectors that return object contours trigger automatically the computation of morphological features in TrackMate. 
When relevant, these features use the physical calibration and units of the source image.
This means for instance that if your image is calibrated with a pixel size in µm, the area of objects will be expressed in µm².
These morphological features are:

#### `Area` 
Simply the area of the objects in spatial unit squared.

#### `Perimeter`
The length of the contour in spatial unit.

#### `Circularity`
The circularity is a measure of how close to a circle the shape of an object is. 
It has a value of 1 for circles and is getting close to 0 for very elongated objects.
It is computed for 2D objects as 

$$
\frac{4 \times \pi \times \text{area}}{\text{perimeter}^2}
$$

#### `Solidity`
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

#### Ellipse fit

Several 2D morphological features are best obtained by fitting on ellipse on the object contour, and reporting the ellipse parameters.
In TrackMate, we first fit an ellipse to the contour using a direct fit following the Chernov method, computed using the Moore-Penrose pseudo inverse (by Kim van der Linde) for speed and robustness.
TrackMate then reports the resulting ellipse parameters:

##### `Ellipse center x0` and `Ellipse center y0`
This the ellipse center position, with respect to the object center position.
You can get the object center position by using 
```java
double x = spot.getDoublePosition( 0 );
double y = spot.getDoublePosition( 1 );
```
to which you need to add the ellipse center values to have the absolute position of the ellipse center. 

##### `Ellipse long axis` and `Ellipse short axis`
The length of the long and short axix of the ellipse, in physical units.

##### `Ellipse angle`
The angle of the ellipse long axis with the X-axis of the image, in radians. 
Careful, in images the Y axis runs from top to bottow, so the positive angle direction is inverted compared to classical plots (positive angles are counter-clockwise) on the image.

##### `Ellipse aspect ratio`
The ellipse aspect ratio is the ratio of the major axis to the minor axis:

$$
\text{ellipse AR} = \frac{\text{major axis}}{\text{minor axis}}
$$

It ranges from 1 for ellipses that resembles circles, and gets larger for elongated ellipses.
A perfect line as a positive infinite aspect ratio.
