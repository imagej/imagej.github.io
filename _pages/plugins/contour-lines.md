---
mediawiki: Contour_Lines
title: Contour Lines
categories: [Uncategorized]
---

{% include info-box software='ImageJ' name='ContourLines' author=' [Eugene Katrukha](http://katpyxa.info)' maintainer='[Eugene Katrukha](mailto:katpyxa_at_gmail.com)' filename=' [ContourLines\_.jar](https://github.com/ekatrukha/ContourLines/blob/master/target/ContourLines_-0.0.4.jar?raw=true)' source=' [github](https://github.com/ekatrukha/ContourLines)' released='07 March 2019' latest-version='07 March 2019' status='stable' website='https://github.com/ekatrukha/ContourLines' %}

Plugin generating contour lines with equal spacing on top of an image (using overlay). Based/inspired by [streamlines](https://github.com/anvaka/streamlines) project by [anvaka](https://github.com/anvaka) and [this publication](http://web.cs.ucdavis.edu/~ma/SIGGRAPH02/course23/notes/papers/Jobard.pdf) (use it for citation).

http://katpyxa.info/software/ContourLines/CL2.gif

## Parameters

After plugin launch, rendering parameters window will appear

http://katpyxa.info/software/ContourLines/CL_parameters_dialog.png

### Smoothing radius

To find the "vector field of an image", plugin calculates convolution of image with [derivative of Gaussian](http://campar.in.tum.de/Chair/HaukeHeibelGaussianDerivatives) in \*x\* and \*y\* to estimate intensity gradient at each point. You can specify smoothing radius (SD of Gaussian). The larger the value, less small intensity details are available. For example, here are two images, the left one is build with smoothing radius of 2.0, while the right one with smoothing radius of 10.0 pixels.

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3.png> <http://katpyxa.info/software/ContourLines/smoothing_10_line_0.05_distance_3.png

Notice that the small spot in the right top corner "disappeared".

### Line integration step

This parameter defines, how precisely contour generation routine follows gradient vector field of the image. Smaller value result in more precise contour lines, but also take longer time to generate them. Example below illustrates integration step of 0.05 (left) versus 0.5 pixels (right).

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3.png> <http://katpyxa.info/software/ContourLines/smoothing_2_line_0.5_distance_3.png

### Distance between lines

Well, how densely you want contour lines to be plotted. Left image is 3 px, right image is 10 px.

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3.png> <http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_10.png

### Stop line at fraction of distance

This parameter is a fraction of previous and it defines when the line integration will stop. I.e. end of each line cannot come closer than this distance to already existing lines. For example, on the left image parameter's value is 0.5, while on the right it is 0.1.

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_x.png> <http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_single_color_end_0.1.png

### Use single color

With this option checked, plugin will use current selected color (in toolbar or Color Picker) to build lines. Example:

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_single_color.png

### Use color lookup tables (LUT)

Plugin will use one of the installed ImageJ/Fiji lookup tables (LUTs) to color code each contour with its average intensity. Pay attention, that current minimum and maximum of intensity would be taken from "Brightness/Contrast" settings of the image. In works better if your image uses "dark-to-bright" LUT and you check "Invert LUT" option for contours. In this case brighter lines would be on top of dark image areas and vice versa. In the example below the left image uses inverted "Thermal" LUT for contours, while contour LUT of the image on the right is not inverted.

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3.png> <http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_not_inverted_thermal.png

### Remove open contours

Plugin will remove open contours (contours with free ends). Examples are below, left image includes open contours, while the right one not.

http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_x.png> <http://katpyxa.info/software/ContourLines/smoothing_2_line_0.05_distance_3_single_color_closed_only.png

## Updates history

-   v.0.0.4 added criteria for line integration end. Added a possibility to remove open contours.
