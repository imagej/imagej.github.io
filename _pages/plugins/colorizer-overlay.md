---
mediawiki: Colorizer_Overlay
title: Colorizer Overlay
categories: [Image Annotation]
---

{% include info-box software='ImageJ 1.x' name='Colorizer\_Overlay' author='Fred Damen' filename='Colorizer\_Overlay.jar' source=' [Colorizer_Overlay.zip](/media/plugins/colorizer-overlay.zip)' released='1 April 2020' status='stable' category='Image annotation' website='' %}

The Colorizer\_Overlay plugin provides the ability to apply a LUT, colorbar, and annotation to a map, i.e., quantified image, and overlay this upon a background image. The impetus for this plugin was my inability to remember how to perform all the necessary steps and the laborious task of doing this again and again whenever my whim for the best representation of my data kicked in, usually right before an abstract deadline.

## Features

<img src="/media/plugins/colorizer-overlay.jpg" width="600"/>

The process of generating a colorized overlay is best, but not required, done in three stages.

***First...***  
**Background** identifies the background image. If unspecified the background color is used. If the specified ImageWindow contains an Roi, the image is cropped to the bounding box and cleared outside the Roi, i.e., set to background color.  
**Foreground** identifies the foreground image that is colorized. If the ImageWindow contains an Roi then only the contents of the Roi will be overlayed.  
**Range** is the colorization range that will be used. Defaults to the display range of the foreground source image. If **Query** is on, then the range will be requeried and set every time a foreground image is selected.

***then...***  
**Scale** identifies the rescaling of the images that is done before any annotation is performed. *W* and *H* are the scaling factor, 1 and 100% are the same. The *w* and *h* are columns and rows of voxels added to the resulting image before annotation.  
**Interpolation** identifies the means by which the image will be scaled.  
**Boarder** identifies the location of the source image in the resultant image, i.e., opposite of where to stick the boarder voxels.

***then...***  
**ColorBar** identifies if and where a colorbar should be placed.  
**Size** identifies the size and boarder of the colorbar. *W* and *H* identify the axial and longitudinal dimension of the colorbar; \# is in voxels and \#% is a fraction of the rescaled image. *in* and *out* specify the number of voxels added to the attachment proximal and distal side of the colorbar.  
**Label** is the string to be inserted at the top left of the image.  
**Multiplier** scales the colorized range before annotating the colorbar. If the voxel values are in meters and the annotation is in mm, then set to 1000.  
**Format** is the Java format string used to produce the colorbar annotations.  
**Font** is the font family to use for the annotations.  
**Style** is the font style to use for the annotations.  
**Color** is the foreground color to use for the annotations.  
**Background** in the overlayed annotation background. None is a transparent overlay.  
**Size** is the font size.

## Methods

`public static ImagePlus doOverlay(ImagePlus bgimp, Roi bgroi, ImagePlus fgimp, Roi fgroi, double wmin, double wmax, String lut)`  
Apply LUT to Roi'ed DisplayRange'd forground image, overlay on Roi'ed background image and crop to bounding box. Roi(s) need to explicitly identified; image(s) will not be queried for Roi(s).

`public static ImagePlus addLabel(ImagePlus imp, double x, double y, String label, Font font, Color fgc, Color bgc)`  
Add label to imp at x,y using font and colors.

`public static ImagePlus addColorBar(ImagePlus imp, String lut, String cbwhere, String cbsize, double fgll, double fgul, String format, Font font, Color fgc, Color bgc)`  
Add a properly adorned colorbar of at edge of the image.

`public static ImagePlus doScale(ImagePlus imp, String newSize, String interpolationType, String boarderType)`  
Scale the image appropriately.

`public static ImagePlus doOverlayLabelColorBar(ImagePlus bgimp, Roi bgroi, ImagePlus fgimp, Roi fgroi,` `String label, double fgll, double fgul, double multiplier,` `String lut, String cbwhere, String cbsize, String format, Font font, Color fgc, Color bgc)`  
Overlay colorbar and label.

`public static ImagePlus doOverlayScaleLabelColorBar(ImagePlus bgimp, Roi bgroi, ImagePlus fgimp, Roi fgroi,` `String label, double fgll, double fgul, double multiplier, String lut,` `String newSize, String interpolationType, String boarderType,` `String cbwhere, String cbsize, String format, Font font, Color fgc, Color gc)`  
Scale then overlay colorbar and label.

## Coding Goodies

How to not do string overlays; there are more direct ways I discovered after becoming happy with the plugin.

## Install

Unzip [Colorizer\_Overlay.zip](/media/plugins/colorizer-overlay.zip) into ImageJ 1.x plugins {% include bc path="File|Show Folder|Plugins" %} or plugins/jars directories. Source code in jar file.  
{% include bc path="Plugins|Annotation|Colarizer_Overlay..." %}

## Licence

GPL distribution licence.

## ChangeLog

1 April 2020 Initial version.

## Known Bugs

Let me know.

 
