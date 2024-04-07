---
mediawiki: PhotoBend
title: PhotoBend
categories: [Tracking]
name: PhotoBend
source-url: https://github.com/anotherche/photobend
release-date: 26 Apr 2017
dev-status: Alpha
team-founders: "@anotherche"
team-maintainers: "@anotherche"
doi: 10.1039/C7SC04863G
---

## PhotoBend plugins collection

A collection of specialized plugins for ImageJ providing tracking of a needle-like crystal shape changing during photobending process. Photobending is a phenomenon of crystal deformation caused by non-uniform crystal structure transformation due to photochemical reaction. Bending of crystals caused by light irradiation is only one of various types of mechanical response observed in chemically transforming solid substances (see the review by Naumov *et al.*, 2015[^1] ).

{% include thumbnail src='/media/plugins/photobend-demo.gif' title='Animation of the photobend time lapse (\~1500x playback speed)'%}

There are two plugins in the collection providing two methods of crystal bending measurement: Bending\_Crystal\_Track and Laser\_Spot\_Track4. Both use the template matching technique based on OpenCV library to track the movement of specific targets in the series of time lapse images organized in the virtual stack. Direct usage of movies opened as image stacks is not supported currently (movies can be transformed in the image sequences with tools like ffmpeg. <span style="color:red"> UPDATE! - movies can be used directly with the Bending\_Crystal\_Track plugin! </span> Laser\_Spot\_Track4 stil requires a series of images). Timeline of the registered process is based on exif timestamps in the images or on the constant time step if the metadata are not available.

There is an ability to monitor a folder for additional images appearing in the time lapse series thus allowing live process registration. The plugins work with 8/16/32-bit greyscale or 24-bit RGB images. The matching mode can be chosen from the intensity-based or color-based for the RGB format (the later is useful for images having weak intensity contrast but possessing sufficient color gradients). Subpixel registration is available using local quadratic approximation of the matching measure.

Although Bending\_Crystal\_Track and Laser\_Spot\_Track4 are specialized plugins they can be used in more general cases. Bending\_Crystal\_Track can be used with any images of attached bending rod-like objects, while Laser\_Spot\_Track4 is suitable for tracking of a spot-like object moving relative to the pre-made template of immobile marks to analyze the object movement in the predefined 2D coordinate system.

The plugins use ideas and code of

-   Template Matching by Qingzong Tseng (based on javacv)
-   javacv (java interface to OpenCV) by Samuel Audet
-   Exif Metadata Library by Drew Noakes

The page is still under construction. Usage instructions will be added.

## Bending\_Crystal\_Track plugin

The plugin is for the analysis of a stack of time lapse microscopic images of a bending crystal. User is instructed to select specific parts on the reference crystal image which includes: the point on the tip of free crystal's end, the point on the attached end of the crystal, the point in the middle of the crystal and a rectangle around a stable part of the image (a part supposed to be immobile during the whole process, a tip of holder or capillary to which the crystal is attached, for one).

<!-- TODO: Improve site infrastructure surrounding figures, and use it here. -->
<figure class="figure" style="max-width: 100%">
<div style="column-count: 3" markdown=1>
![](/media/plugins/photobend-processing.jpg){:style='width: 100%'}
![](/media/plugins/photobend-deformation-plot.jpg){:style='width: 100%'}
![](/media/plugins/photobend-curvature-plot.jpg){:style='width: 100%'}
</div>
<figcaption style="font-weight: bold">Crystal shape tracking in progress</figcaption>
</figure>

The plugin code uses the selected regions of the image as reference templates to find them in the series of the time lapse images. Automatic picture stabilization is provided by detection of the stable part displacement. Then the free crystal's end and its middle part are detected in new positions of the image (accounting for the displacement and rotation) with the template matching technique. The coordinates of the three points (two ends and the middle part) are used to calculate the curvature and deformation (elongation or shortening) of the crystal.

## Laser\_Spot\_Track4 plugin

{% include thumbnail src='/media/plugins/laserspotmove.gif' title='Animation of the laser spot movement obtained while registering the photobending with the laser beam deflection technique (\~70x playback speed)'%}

The plugin's goal is to automate the registering and analysis for the so-called laser beam deflection technique. The technique is the general purpose method to study various processes in which objects undergo weak change of their geometry. A laser beam reflecting from the object itself or from a mirror attached to the object deflects while the object's geometry changes. The spot of the deflected laser beam moves on a distant screen (e.g. wall). Due to long distance between the object and the screen an amplification of the geometry change is provided.

The plugin was developed to analyze weak photobending of thick crystals. To utilize the technique tiny mirror is attached to the free crystal's end. The bending then causes tilt of the mirror and corresponding deflection of the laser beam.

![400pix\|left\|Laser spot tracking in process](/media/plugins/laserspottrack.jpg)

The movement of the laser spot is registered with a camera to give the series of the time-lapse photographs (or a movie which should be transformed to the series for the analysis). The laser spot should be registered on the screen with the template attached which contains 4 marks placed in corners of a square. The usage of the template provides automatic image stabilization and correction of perspective distortion (note that only linear perspective is corrected; no spherical distortion can be corrected by the plugin, so usage of wide-angle lenses is not recommeded). The template should be made prior to the registering by any appropriate technique. For example by printing a prepared image like the one from this [archive](/media/plugins/laserdeflectionmeasurementtemplate.zip). The archive contains various vector formats of the image having measurement marks placed in the corners of the square of 100 mm side. Depending on the printer model the scale of the image may be distorted differently in vertical or horizontal direction, so the final scale should be checked and corrected if necessary (for example, by editing one of the vector file suggested).

To analyze the laser spot movement with the plugin the image sequence should be open as the virtual stack. After confirming setting of few necessary parameters (including algorithm settings, size of rectangles enclosing the laser spot part or template's corner marks, size of the template square side in mm) the plugin interface asks to specify position of centers of the spot and of four corner marks. It is important to specify the corner marks in the clockwise order! The resulting axes of the coordinate system in which the spot movement is analyzed are as following: X axis is along the direction connecting centers of mark \#1 and \#4, Y axis is along \#1 - \#2 line. The coordinates origin is in the center of mark \#1. The marks are labeled in the image contained in the [archive](/media/plugins/laserdeflectionmeasurementtemplate.zip) to ease the plugin usage.

The output of the plugin is placed in the result table containing every image filename, time, coordinates of the laser spot center and shift of the spot relative to the initial position. Coordinates are given in two forms: row coordinates of the spot center in the local image coordinates (in pixels) and corrected/stabilized coordinates in the absolute coordinate system of the 4 marks (in millimeters).

## Installation in Fiji

Add update site PhotoBend to install the plugins automatically.

-   [{% include bc path='Help|Update...'%}](/update-sites)
-   Click *Manage update sites*
-   Add and check new update site: Name=*PhotoBend*, URL="https://sites.imagej.net/PhotoBend/"
-   Click *Close*
-   (You can skip this optional step by default) In the list of new jar files that are proposed to be installed from the update site, you can unchek files that do not need to be installed (for example, files not related to your operating system or processor architecture). To do this, change "Install / Update" to "Keep as is" for those files.
-   Click *Apply changes*
-   Restart ImageJ

Warning: the plugins depend on several libraries which will be installed in local Fiji jars folder. Check for versions inconsistencies if you use these libraries with other plugins. The dependencies are:

-   javacv. Version 1.4 (opencv-version.jar file is copied into plugins folder to prevent automatic overwriting by Fiji updater)
-   xmpcore. Version 5.1.3
-   metadata-extractor. Version 2.11.0

Update: сurrent versions of the plugins use a new way of installing the javacv library, using an additional auxiliary JavaCV Installer plugin, which controls the presence of all necessary dependencies on the system.  During the installation of the plugins described above, the JavaCV Installer plugin is checked for the presence and is installed automatically if necessary. Detailed information about JavaCV Installer plugin can be found on the community page https://forum.image.sc/t/new-javacv-installer-plugin/55392.  

## Citing

We kindly ask you to cite Chizhik 2018[^1] when publishing the results obtained using these plugins. Thank you for your support.

## References

{% include citation fn=1 %}
