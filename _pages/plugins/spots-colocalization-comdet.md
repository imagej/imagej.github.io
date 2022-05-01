---
mediawiki: Spots_colocalization_(ComDet)
title: Spots colocalization (ComDet)
categories: [Colocalization]
---

{% include info-box software='ImageJ' name='ComDet' author=' [Eugene Katrukha](http://katpyxa.info)' maintainer='[Eugene Katrukha](mailto:katpyxa_at_gmail.com)' filename=' [ComDet.jar](https://github.com/ekatrukha/ComDet/blob/master/target/ComDet_-0.5.1.jar?raw=true) + for ImageJ [Jama lib](https://math.nist.gov/javanumerics/jama/Jama-1.0.3.jar)' source=' [github](https://github.com/ekatrukha/ComDet)' released='23 November 2012' latest-version='7 April 2020' status='stable' category='Colocalization' website=' [wiki](https://github.com/ekatrukha/ComDet/wiki)' %}

Plugin for finding and/or analyzing colocalization of bright intensity spots (cells, particles, vesicles, comets, dots, etc) in images with heterogeneous background (microscopy, astronomy, engineering, etc).

For help with plugin installation, see [instructions](https://github.com/ekatrukha/ComDet/wiki/How-to-install-plugin).

## How to use plugin

Open the image to be analyzed in ImageJ. In general, the plugin works in two modes:

-   particles detection (whole image or ROI)
-   particles detection and colocalization analysis (whole image or ROI).

For **colocalization** you need a [color composite image](/imaging/color-image-processing#color-composite-images) containing **multiple color channels (two or more)**. Plugin auto-detects the number of channels and if it is more than one then the plugin will automatically switch to the second mode (see below).

The plugin works with time/z-stacks.

Launch the detection by choosing {% include bc path="Plugins|ComDet|Detect Particles" %}.

http://katpyxa.info/software/ComDet/ComDet_open_v.0.5.0.png

## Simple detection (1 channel)

If the image is not multi-channel image, the following dialog window will appear:

http://katpyxa.info/software/ComDet/ComDet_detection_only_v0.5.0.png

Specify estimated particles size and intensity threshold (particle brightness) and press OK. To have good detection usually you need to play with parameters and see how it goes. Checkbox "*Preview...*" allows to see detection on the current picture and simplifies this task. The "ROI shape" option allows you to choose, if you want your detection to be displayed as "Ovals" or "Rectangles".

http://katpyxa.info/software/ComDet/ComDet_preview_button.gif

By default, plugin looks only for particles of specified size. If you check "*Include larger particles?*" box, it will also try to quantify bigger spots.

If "*Segment larger particles (slow)?*" box is checked, plugin will try to further split large particles into a smaller dots, if it is possible. As its name suggests, this procedure requires computational power and can be slow, especially on big images.

If you choose *Add to ROI Manager* option ("All particles"), plugin will add detected rectangular ROIs around particles to [ROI Manager](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:ROI-Manager...). ROIs will have names in the format of ind(detection\# in Results table)\_ch(\#channel)\_sl(\#slice)\_fr(\#frame).

After pressing OK plugin runs and add ovals/rectangles in overlay on top of detected particles.

http://katpyxa.info/software/ComDet/ComDet_detection_before_after_v2.png

Also it will provide you *Results* table containing particles' coordinates (see below) and *Summary* table. I recommend to play with parameters to get a nice detection result.

## Detection in ROI

If you want detection to be performed in some specific region instead of whole image, select some ROI using any ImageJ ROI selection tools **before** launching plugin:

http://katpyxa.info/software/ComDet/ComDet_ROI_before_v2.png

In this case only particles in that ROI will be detected (also supported in "*Preview..*" mode):

http://katpyxa.info/software/ComDet/ComDet_ROI_after_v2.png

## Detection and colocalization in multi-channel image (two or more channels)

If your image contains multiple channels then after pressing *Detect Particles* the dialog will look differently:

http://katpyxa.info/software/ComDet/ComDet_detection_and_coloc_v0.5.0.png

First, the plugin will show the window above with general setup and later it will proceed with a series of parameter windows, specifying detection parameters for each channel. To get colocalization analysis you need to check "*Calculate colocalization?*" box. If you uncheck it, then only detection will be performed.

There is an additional parameter in case of colocalization: maximum distance between spots' centers. It defines at what distance (in pixels) two spots in different channels are considered to be localized.

**So colocalization is based on the distance between spots' centers!**

After you press "OK", a series of windows for detection parameters for each channel will pop-up:

http://katpyxa.info/software/ComDet/ComDet_detection_and_coloc_v0.5.0_multich.png

Take a notice that "*Preview...*" button in this case will only show detection, it will not mark/analyze colocalization.

After detection is finished ComDet marks detected particles with ovals/rectangles of their own channel (LUT) color and colocalized particles in overlapping color:

http://katpyxa.info/software/ComDet/ComDet_detection_and_coloc_mark_v2.png

Also *Add to ROI Manager* option is available. ROIs will have names in the format of ind(detection\# in Results table)\_ch(\#channel)\_sl(\#slice)\_fr(\#frame). You can add all detected particles or only those that colocalize.

*Only ROI detection* mode (as described above) also automatically works in this case.

## Results table

Here is example of *Results* table (*Summary* table is kind of self-explanatory).

http://katpyxa.info/software/ComDet/Results_v.0.5.0.png

Columns are:

1.  *Abs\_frame* = absolute frame number in stack/hyperstack (unique frame number)
2.  *X\_(px)* = *x* coordinate of spot (centroid fitting)
3.  *Y\_(px)* = *y* coordinate of spot (centroid fitting)
4.  *Channel* = corresponding channel number, where the particle was detected
5.  *Slice* = corresponding slice number (if z-stack)
6.  *Frame* = corresponding frame number (if timelapse)
7.  *xMin*, *yMin*, *xMax*, *yMax* = coordinate of rectangle around spot (in pixels)
8.  *NArea* = [thresholded area](https://github.com/ekatrukha/ComDet/wiki/How-does-detection-work%3F) of the spot in pixels
9.  *IntegrIntChX* = for each channel (marked by X number) shows spot's integrated intensity: sum of all pixels intensity inside the [thresholded area](https://github.com/ekatrukha/ComDet/wiki/How-does-detection-work%3F) minus average spot-specific backgrounds. Background value is calculated as the average intensity of pixels along the perimeter of the rectangle.
10. *ColocChX* = equals to 1, if the spot is colocalized in this channel (marked by X number) and 0 otherwise. Notice, that it is always 1 in the channel, where the particle itself is detected (so it kind of colocalizes with itself). Also keep in mind, that if three particles from three different channels are colocalized, there would be three rows in the Results table.
11. *ColocIndChX* = corresponds to the unique detection index (last column) in Results table, corresponding to the particle in another channel (if colocalized). Zero otherwise.
12. *Index* = unique index for each detection.

## Additional info

For detection explanation, see [How does detection work?](https://github.com/ekatrukha/ComDet/wiki/How-does-detection-work%3F) Also [updates history](https://github.com/ekatrukha/ComDet/wiki/Updates-history) is available.

 
