---
title: TrackMate FAQ
description: Frequently asked questions about TrackMate.
categories: [Tracking, Segmentation]
logo: /media/logos/trackmate-300p.png
project: /software/fiji
---

This list of frequently asked questions is compiled from several questions we have seen several times on the [ImageJ forum](http://forum.imagej.net/). It will be updated as questions appear there.

### Only the first time-point of the track is displayed after loading.

*I have an issue after loading a TrackNate file. I can retrieve my TrackScheme with the tracks I was working on, however my stack doesn't go from one time frame to the next and only the first point of the track is displayed. Do you have any idea of what is happening. I don't think there was any update between the time I saved the file and now. There is no error message. I can't add more points to the TrackScheme...*

This looks like a classical dimensionality problem. Is your image a Z-stack (1 time-point many Z slices) after loading? Check the image properties of the image.

### Limitations of TrackMate for spot detection.

*We are using TrackMate to generate lineages of X cells in live Y and are interested in how the intensity of a signal of interest changes over time, but also in the cell volume. Since most of our cells are not spherical and some are clustered close together, the LoG detector yields rather unsatisfying results. Is it possible to detect these cells based on their actual shape instead of assuming they are all spheres and measure the volume of such segmented cells?*

Yes! Starting with TrackMate v7 (Summer 2021).

You are looking for *segmentation* algorithm, that can return the contour of an object, and harness complex object shapes. TrackMate now ships several algorithms that can do that, and exploit the object shape in 2D. See [TrackMate v7 detectors](/plugins/trackmate/trackmate-v7-detectors)


### Signification of the Quality value in LoG Detector.

*I'm using the LoG detector and couldn't find any documentation as to how the 'quality' value is determined, only that it is an arbitrary measure. Is there an equation/description of how this works so I'm able to set a threshold based on experimental values?*

The TrackMate PDF manual gives information about this (page 51):

The LoG detector is the best detector for Gaussian-like particles in the presence of noise. It is based on applying a LoG filter on the image and looking for local maxima. The Laplacian of Gaussian result is obtained by summing the second order spatial derivatives of the gaussian- filtered image, and normalizing for scale.

Local maxima in the filtered image yields spot detections. Each detected spot is assigned a quality value by taking the local maxima value in the filtered image.

So by properties of the LoG filter, this quality value is larger for :

-   bright spots;
-   spots which diameter is close to the specified diameter.


### Exporting TrackMate spots to ImageJ 1.x ROIs.

*TrackMate found my particles, and the preview function is usefeul. However I can't seem to figure out how to export all the TrackMate overlays to individual ROIs, so that I can analyse them with other plugins.*

We had a plugin that did that prior to v7, but has not been ported to the new v7 yet (Summer 2021). 


### Copying TrackMate tracking data to another image file.

*We would like to know if there is any tool to copy the spots/track created in one stack (fluorophore 1, file 1) and paste them in another stack (fluorophore 2, file 2). We explored the option `Copy overlay to` but it did not work for more than a single frame of the stack.*

The simplest solution consists in editing the TrackMate XML file, and have it point to another tif file.

-   Make a copy of the XML file, and edit it in a good text editor;
-   Find in the XML file the line that points to the TIF file on which you did the analysis. It looks like this:

<!-- -->

      <Settings>
        <ImageData filename="DUP_TIM1 GFP clat dsred TIRF-5.tif" folder="/Users/tinevez/Desktop/" width="310" height="362" nslices="1" nframes="113" pixelwidth="0.1" pixelheight="0.1" voxeldepth="1.0" timeinterval="2.463" />

-   Change the `filename` tag to point to the other TIF file on which you want to copy the overlay.
-   Next time you open the edited file in TrackMate, it will also open the new TIF file and put the annotation on it.


### Exporting TrakMate overlay to a movie.

*In TrackMate after completing tracking, is there any way to export/save a movie with all tracks and moving spots (exactly as it appears after using the TrackMate)?*

If you keep clicking on the Next button on the GUI, you will reach the last panel of the GUI, which collects miscellaneous actions.

One of them is called **Capture TrackMate overlay** and does what you need. It generates a RGB stack with the tracks burned-in. After that you have to export the stack to AVI and you are done.

Careful: the frame capture is simple and brutal. If you have something that passes over the TrackMate viewer while the capture is going on, it will be captured in the final movie.


### Customizing the look of tracks during movie export.

*I am aware of **Capture TrackMate overlay** function but it only provides the final picture of the track(s) overlayed on the moving particle. I'm interested in showing that the tracks are (or a single track) being formed as the particles move.*

The overlay capture abides to the display settings you set in the **Display Settings** GUI panel. By changing the **Track display mode** here, you can get what you need. For instance choosing the `Show local tracks, backward` will generate a "dragon tail" aspect for the tracks in the movie.


### Tracks looked jagged.

*The particle traces resemble jagged line rather than a smooth curve of the path. I'm measuring the average speed of the particles and it's crucial the software calculates the distance traveled accurately.*

<figure><img src="/media/plugins/trackmate/trackmate-jaggedlines.png" title="TrackMate_JaggedLines.png" width="600" alt="TrackMate_JaggedLines.png" /><figcaption aria-hidden="true">TrackMate_JaggedLines.png</figcaption></figure>

Make sure the `Do sub-pixel localization` is checked. It will mitigate this problem. Also make sure that you choose a blob diameter that actually matches the objects you tracking.


### Various `java.lang.NoClassDefFoundError`s upon execution.

These errors may popup when you try to launch TrackMate, or plot features. A stack trace will show in the console and the second line will resemble this:

    Exception in thread "TrackMate plot spot features thread" java.lang.NoClassDefFoundError: 
    com/itextpdf/text/DocumentException
        at fiji.plugin.trackmate.features.SpotFeatureGrapher.render(SpotFeatureGrapher.java:115)
        at fiji.plugin.trackmate.gui.GrapherPanel.plotSpotFeatures(GrapherPanel.java:189)
        at fiji.plugin.trackmate.gui.GrapherPanel.access$100(GrapherPanel.java 
    ...

This kind of error is caused when a Java class is missing in your installation. In most cases, this happens because your Fiji installation did not update properly. Possible solutions are

-   [Update](/plugins/updater) Fiji.
-   Check if you have the [Java8](/news/2015-12-22-the-road-to-java-8) update site in the Fiji [Updater](/plugins/updater)
-   Finally, if nothing works, rather than digging in your Fiji installation in details, just install Java 8 and [re-download](/downloads) a fresh Fiji application.
