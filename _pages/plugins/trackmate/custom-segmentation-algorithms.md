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

### What changed in the  `Spot` class.

Starting in version 7, the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/Spot.java#L76-L81' label='Spot' %} class in TrackMate has a new field: a  {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/SpotRoi.java' label='SpotRoi' %} object.

It is basically made of the 2D polygon that stores the object contour, relative to the spot center (the `x, y, z` tuple). Its only fields are two `double[]` arrays for the `xp` and `yp` coordinates of the contour, ordered along the contour. The last point connects to the first.

The `Spot` objects returned by detection algorithms have the `SpotRoi` set to `null`. The sole difference of a segmentation algorithm in TrackMate is that it returns `Spot` objects with a non-`null` `SpotRoi` object.

### Limitations.

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

### Example: How spots are created in the StarDist detector.

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
    Spot spot = SpotRoi.createSpot( xpoly, ypoly, quality );
    // 'spots' is the list of Spot this detector will return.
    spots.add( spot );
}
```

As you can see it is fairly simple. It illustrates how you can plug anything that returns a polygon in TrackMate and make a new detector out of it. If you want to integrate a technique that returns instead a mask, a probability map or a label image, we also made utility methods for these cases.

## Creating a collection of spots from a mask image or a threshold image.

### The `MaskUtils.fromThresholdWithROI()` method.

The above method is what you could use to implement your own segmentation algorithm. We also provide a simple API to facilitate integrating existing segmentation algorithms in TrackMate. Many of the existing algorithms either return a mask image, a label image or some sort of probability map to threshold to generate objects. 
This API consists mainly of utility methods in the class {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/detection/MaskUtils.java' label='MaskUtils' %} that accept such inputs and output a collection of `Spot`s, containing the object contour.
Let's start with how to input mask images.

For the maximal flexibility, a mask image in TrackMate can be of any type provided it is using a  scalar, real pixel type. We simply say that the objects are made by connecting all the pixels that have a value strictly larger than 0.
So the method that creates spots from such a mask is the one for importing a threshold image:

{% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/detection/MaskUtils.java#L404-L439' label='MaskUtils.fromThresholdWithROI()' %}

```java
	/**
	 * Creates spots <b>with their ROIs</b> from a <b>2D</b> grayscale image,
	 * thresholded to create a mask. A spot is created for each
	 * connected-component of the mask, with a size that matches the mask size.
	 * The quality of the spots is read from another image, by taking the max
	 * pixel value of this image with the ROI.
	 * 
	 * @param <T>
	 *            the type of the input image. Must be real, scalar.
	 * @param <S>
	 *            the type of the quality image. Must be real, scalar.
	 * @param input
	 *            the input image. Must be 2D.
	 * @param interval
	 *            the interval in the input image to analyze.
	 * @param calibration
	 *            the physical calibration.
	 * @param threshold
	 *            the threshold to apply to the input image.
	 * @param simplify
	 *            if <code>true</code> the polygon will be post-processed to be
	 *            smoother and contain less points.
	 * @param numThreads
	 *            how many threads to use for multithreaded computation.
	 * @param qualityImage
	 *            the image in which to read the quality value.
	 * @return a list of spots, with ROI.
	 */
	public static final < T extends RealType< T >, S extends NumericType< S > > List< Spot > fromThresholdWithROI(
			final RandomAccessible< T > input,
			final Interval interval,
			final double[] calibration,
			final double threshold,
			final boolean simplify,
			final int numThreads,
			final RandomAccessibleInterval< S > qualityImage )
```

This method is suitable for 2D images. It will create spots with object contours. Let's review a bit its input:
* `input` is the mask input. It must be a `RandomAccessible` of type `T`, which is the classical frame that TrackMate automatically provides to its detectors. 
* `interval` is the interval in the input to analyze. Like for all other detectors, TrackMate returns the pixel infor as an unbounded `RandomAccessible` and we need to specify what part of the image we have to analyze. Again, this is common to all detectors and provided by TrackMate.
* `calibration` is a `double[]` array of 3 elements that contains the pixel size of the image (pixel width, height and depth). It is read from the input calibration that you can set in Fiji. Again, all of this is common to all detectors.
* `threshold` is a double value above above which intensities will be considered par of an object. This is spefic to this detector and is set by the user. For mask images, it is 0.
* `simplify` is a boolean flag that states whether the user requested the contours to be smoothed and simplified. This is important for measuring correctly morphological features and we document it fully elsewhere.
* `numThreads`. The creation of spots in this way is multithreaded and you can set here how many threads to use. Again, if you declare your detector to be `Multithreaded`, the `numThreads` value of your detector will be set automatically by TrackMate and you use it here. If your detector is not multithreaded, use a value of 1.
* The `qualityImage` is an image from which we will read a quality value for the spots created. It must be defined on the same interval that of the `interval` parameter, and the pixels must be of `NumericType` and scalar. If you cannot set the quality from a channel or an image (like for a mask), just pass `null` to this parameter and the quality valueof an object will be set to be its area. Otherwise it will be the maximal pixel value within the object contour in the quality image.

### Example: the mask detector.

Let's see how it is used on the mask detector. Since the mask images are treated simply as grayscale images with a threshold of 0, the mask detector is actually implemented in the {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/detection/ThresholdDetector.java' label='ThresholdDetector' %} class. (The {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/detection/MaskDetectorFactory.java' label='MaskDetectorFactory' %} returns a  `ThresholdDetector` with a threshold value set to 0. See {% include github org='fiji' repo='TrackMate' branch='master' source='fiji/plugin/trackmate/detection/MaskDetectorFactory.java#L89' label='this line' %}.)
Here is the content of the `process()` method:

```java
	@Override
	public boolean process()
	{
		final long start = System.currentTimeMillis();
		if ( input.numDimensions() == 2 )
		{
			/*
			 * 2D: we compute and store the contour.
			 */
			spots = MaskUtils.fromThresholdWithROI( input, interval, calibration, threshold, simplify, numThreads, null );

		}
		else if ( input.numDimensions() == 3 )
		{
			/*
			 * 3D: We create spots of the same volume that of the region.
			 */
			spots = MaskUtils.fromThreshold( input, interval, calibration, threshold, numThreads );
		}
		else
		{
			errorMessage = baseErrorMessage + "Required a 2D or 3D input, got " + input.numDimensions() + "D.";
			return false;
		}

		final long end = System.currentTimeMillis();
		this.processingTime = end - start;

		return true;
	}
```

Note that the detector treats differently 2D and 3D images. As stated above, the new API supports object contour only for 2D images. The method `MaskUtils.fromThreshold()` is the complement of the `MaskUtils.fromThresholdWithROI()` for 3D images, but that returns `Spot` objects that do not have a contour. Here the spots created have a radius that is such that the sphere with this radius have the same volume that of the segmented object.

The use of this API makes the detector code very short. You can imaging adapting the same approach to integrate a segmentation algorithm to would output a mask image or a threshold image. For instance this is what we did to integrate the _Traininable Weka segmentation_ plugin and the _ilastik_ pixel classifier.

### Example: the Weka detector.

The Weka detector is not very complicated. The bulk of calling Weka is done in the {% include github org='tinevez' repo='TrackMate-Weka' branch='master' source='fiji/plugin/trackmate/weka/WekaRunner.java' label='WekaRunner' %} class.
Running Weka is done in the {% include github org='tinevez' repo='TrackMate-Weka' branch='master' source='fiji/plugin/trackmate/weka/WekaRunner.java#L104-L107' label='WekaRunner.computeProbabilities()' %} method. It returns the probability of the classification for the specified input and the specified class. We won't detail it.
But creating spots from this probability is simple. The method {% include github org='tinevez' repo='TrackMate-Weka' branch='master' source='fiji/plugin/trackmate/weka/WekaRunner.java#L173-L198' label='WekaRunner.getSpots()' %} method, which resembles the method described in the previous paragraph:

```java
	public List< Spot > getSpots( final RandomAccessibleInterval< T > proba, final double[] calibration, final double threshold, final boolean simplify )
	{
		final List< Spot > spots;
		if ( isProcessing3D )
		{
			spots = MaskUtils.fromThreshold(
					proba,
					proba,
					calibration,
					threshold,
					numThreads,
					proba );
		}
		else
		{
			spots = MaskUtils.fromThresholdWithROI(
					proba,
					proba,
					calibration,
					threshold,
					simplify,
					numThreads,
					proba );
		}
		return spots;
	}
```
Here the threshold value to segment the probability map is set by the user.
Since we have a probability map, we can use it to compute a quality value derived from this probability.

### Example: the ilastik detector.

The ilastik detector works exactly in the same way. It has a  {% include github org='tinevez' repo='TrackMate-Weka' branch='master' source='fiji/plugin/trackmate/ilastik/IlastikRunner.java' label='IlastikRunner' %}  class that is in charge of calling ilastik and convert the results to a spot collection. The ilastik detector just makes a simple call to it.

However we use a special slicing of time-points for this algorithm. Indeed, the ilastik runner expects to receive _all_ the time-points to process at once, runs ilastik on them, and then return.
