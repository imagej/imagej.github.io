---
title: How to use the new API to create spots with ROIs in TrackMate
nav-links:
- title: Edge Feature Analyzers
  url: /plugins/trackmate/custom-edge-feature-analyzer-algorithms
- title: Track Feature Analyzers
  url: /plugins/trackmate/custom-track-feature-analyzer-algorithms
- title: Spot Feature Analyzers
  url: /plugins/trackmate/custom-spot-feature-analyzer-algorithms
- title: Viewers
  url: /plugins/trackmate/custom-viewers
- title: Actions
  url: /plugins/trackmate/custom-actions
- title: Detection Algorithms
  url: /plugins/trackmate/custom-detection-algorithms
- title: Segmentation Algorithms
- title: Particle-Linking Algorithms
  url: /plugins/trackmate/custom-particle-linking-algorithms
---

## Introduction.

Up to the version 7 of [TrackMate](/plugins/trackmate/index), detection algorithms were limited to return the position of spots and their radius. All the detection were represented by a tuple in the shape of `frame, x, y, z, radius, quality`. This is well suited to implement _detection algorithms_, that return the position of an object but omit its shape. The [previous page](/plugins/trackmate/custom-detection-algorithms) in this tutorial series showed how the base code to implement such an an algoritms as a detector for TrackMate.

With version 7, we rewrote a large part of TrackMate to remove this limitation, at least in 2D. We changed the data model so that `Spot`s in TrackMate could _possibly_ store the shape, while not affecting the exiting detectors. We made a new API to facilitate implementing _segmentation algorithms_ in TrackMate, that can return the shape of objects. Their shape is later used to compute morphology features or to measure intensity within the object contour. We used this API to implement [7 new segmentation algorithms](/plugins/trackmate/trackmate-v7-detectors) in TrackMate, integrating the some of the best segmentation tools available in Java. This page documents how you can use this API to implement your own segmentation algorithms yourself, and make it a first-class-citizen of TrackMate, like any of the other TrackMate modules we document in this series.

We need to first review the new API itself, which basically boils down to one class offering static methods. Then, as for the other detectors, we need to add some flags in the detector factory to tell TrackMate that what we build is a segmentation algorithm that returns the object shape. Finally, we will also see some find tuning of the multithreading for your detectors, made to accommodate the various existing segmentation tools you might want to integrate in TrackMate. We will use the examples of the 7 segmentation algorithms mentioned above to base this tutorial.

## Creating spots that store object contours. 

 ### What changed in the `Spot` class.

Starting in version 7, the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/Spot.java#L76-L81' label='Spot' %} class in TrackMate has a new field: a  {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/SpotRoi.java' label='SpotRoi' %} object.

It is basically made of the 2D polygon that stores the object contour, relative to the spot center (the `x, y, z` tuple). Its only fields are two `double[]` arrays for the `xp` and `yp` coordinates of the contour, ordered along the contour. The last point connects to the first.

The `Spot` objects returned by detection algorithms have the `SpotRoi` set to `null`. The sole difference of a segmentation algorithm in TrackMate is that it returns `Spot` objects with a non-`null` `SpotRoi` object.

## Limitations.

Let's start with the bad news: We can deal with object contours only for 2D images. The main reason is that we do not have yet a good way to store 3D contours in Fiji. This might change but for now all of what you will see only applies to 2D contours, so polygons.

Also, the object shape must be represented by a [simple polygon](https://en.wikipedia.org/wiki/Simple_polygon). That is: the contour must not have holes, and the line of the polygons should not intersect each other. If you create a spot with an intersecting contour, the results are undefined. If you have objects with holes and you try to create spots for them, the holes will be ignored.

### Creating a `Spot` from a polygon.

The two `double[]` arrays for the `xp` and `yp` must be set relative to the spot X and Y position. You can compute them yourself, but it is easier to use the static method `createSpot()` that returns a spot from `x` and `y` in physical coordinates:

```java
double[] xp = ...;
double[] yp = ...;
double quality = ...;
Spot spotWithShape = SpotRoi.createSpot(xp, yp, quality);
```

As for all the coordinates stored in `Spot`, the X and Y must be in physical units (_e.g._ microns if your image is calibrated in microns). This method will take care of computing the spot `x` and `y` center, compute a radius from the polygon, and sore the contours points correctly.

## Example: How spots are created in the StarDist detector.

The [Fiji StarDist implementation](https://github.com/stardist/stardist-imagej/) returns the objects it found as polygons. We therefore just used this method to bridge it to TrackMate. In {% include github org='tinevez' repo='TrackMate-StarDist' branch='master' source='fiji/plugin/trackmate/stardist/StarDistDetector.java' label='StarDistDetector.java' %} you will find the following lines:

```java
/*
 * We received the 'polygons' object from the StarDist runner.
 * As for all the other detectors, this instance have to return
 * a list of Spot 'spots' containing all the objects segmented in 
 * the current time-point.
 */

// Create spots from output.
for ( final Integer polygonID : polygons.getWinner() )
{
    // Collect quality = max of proba.
    final PolygonRoi roi = polygons.getPolygonRoi( polygonID );
    proba.setRoi( roi );
    final double quality = proba.getStatistics( Measurements.MIN_MAX ).max;

    // Create ROI.
    final Polygon polygon = roi.getPolygon();
    final double[] xpoly = new double[ polygon.npoints ];
    final double[] ypoly = new double[ polygon.npoints ];
    for ( int i = 0; i < polygon.npoints; i++ )
    {
        /*
         * Here we convert the polygon points in pixel coordinates to 
         * physical coordinates (multiplication by the calibration).
         * We also need to offset them by the interval top-left corner
         * in case the user ask to perform segmentation in a sub-region
         * of the source image.
         */
        xpoly[ i ] = calibration[ 0 ] * ( interval.min( 0 ) + polygon.xpoints[ i ] );
        ypoly[ i ] = calibration[ 1 ] * ( interval.min( 1 ) + polygon.ypoints[ i ] );
    }
    spots.add( SpotRoi.createSpot( xpoly, ypoly, quality ) );
}
```

As you can see it is fairly simple. It illustrates how you can plug anything that returns a polygon in TrackMate and make a new detector out of it. If you want to integrate a technique that returns instead a mask, a probability map or a label image, we also made utility methods for these cases.

## Creating a collection of spots from a mask image.

