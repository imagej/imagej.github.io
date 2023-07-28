---
title: Hill Shade
categories: [Visualization]
dev-status: "stable"
icon: /media/icons/plugin_icon_ImageJColor.png
---

# Hill Shade

**Produces relief shading as in topographic maps, assuming that the pixel value is the height of a surface at the given position (x, y).**

## Description

The plugin needs an 8-bit, 16-bit or float (=32-bit) input image; pixel value (height) calibration of 8-bit and 16-bit input images is taken into account. The plugin produces a new 8-bit grayscale output image, irrespective of the type of input image. Preview is shown as an overlay of the input image, however.

The math behind it: When 'Nonlinear Contrast' and 'Half Brightness for Flat Areas' are off, the brightness of the output image is proportional to the cosine of the angle between the direction perpendicular to surface and the direction to the light source (sun), i.e., the surface is shows {% include wikipedia title="Lambertian reflectance" %}. If that angle is 90 degrees or more, i.e. if the slope that is directed away from the sun, the output is black. It is assumed that the "Mountains" do not cast a shadow, however.

## Dialog parameters

![Dialog screen shot](/media/plugins/hillshade/hillshade-screenshot.jpg)

-   **x Pixel Size** - Size of one pixel in x direction, in the same units as the height (pixel value).
-   **y Pixel Size** - Size of one pixel in y direction, in the same units as the height (pixel value).
-   **Elevation of Sun** - height of the light source in degrees, typically between 30 and 60
-   **Azimuth of Sun** - direction to the light source in degrees, 0 is north, 90 east etc.
-   **Nonlinear Contrast** - when &gt; 0, contrast for gentle slopes gets enhanced. Typical values are 1-5.
-   **Half Brightness for Horizontal** - when selected, a gamma correction is applied to the output, such that a horizontal plane will appear with half brightness (pixel value = 128), irrespective of the elevation of the sun. When not selected, the pixel value of a horizontal plane will be roughly 256\*sin(Sun\_Elevation). In that case, a horizontal plane gets half brightness only at sun elevation of 30°, the output gets brighter if the sun elevation is higher, and darker if it is lower.

## Tips

-   If the slopes are very gentle, you can try setting smaller values of the pixel size to enhance the contrast.
-   To create an output like a topographic map, display the input (elevation data) with a suitable lookup table and superimpose the hill shade output:
    -   Run *Hill Shade*.
    -   Apply a suitable lookup table to the input image.
    -   Convert the input image to RGB.
    -   Use {% include bc path="Process|Image Calculator" %} with 'Operation=Average' to combine the input image and the shaded image.
    -   Typically, you will then want to enhance the colors a bit, using {% include bc path="Image|Adjust|Color Balance" %}.
    -   The image below shows an example, based on Space Shuttle Radar Topography Mission data of the area around Austria's highest mountain, the Großglockner.
-   Such a superimposed map can be also loaded as 'Texture' when using the [Interactive 3D surface plot](https://imagej.net/ij/plugins/surface-plot-3d.html) plugin.

{% include img src="hillshade/hillshade-overlay-example" width="280" caption="Topographic map created by superposition, click to enlarge" %}


## Download
* Source code `Hill_Shade.java` {% include github org='imagej' repo='imagej.github.io' branch='main' path='media/plugins/hillshade/Hill_Shade.java' %} (make sure you download the **raw** file, use the button near the top right)
* Class file `Hill_Shade.class` {% include github org='imagej' repo='imagej.github.io' branch='main'  path='media/plugins/hillshade/Hill_Shade.class' %}

## Installation
- Copy the raw `Hill_Shade.java` file into the ImageJ plugins folder or a subfolder thereof. Make sure that you name the downloaded file ”Hill_Shade.java”; uppercase/lowercase matters.
- Compile with “Compile and Run” and press “OK”. Note that "Compile and Run" is currently broken on Fiji; as a workaround use File>New>Script, open the `Hill_Shade.java` file and press “Run“.
- Alternatively, directly save the .class file `Hill_Shade.class` into the ImageJ/plugins directory or an immediate subdirectory thereof. Again, make sure that you name the file correctly, uppercase/lowercase matters.
- Use Help>Update Menus or restart ImageJ to make it appear in the Plugins menu (not necessary if you have used the Fiji Script Editor).

## Version History
-   2014-Nov-22 Michael Schmid: enhanced version of the plugin released on the ImageJ mailing list a few days earlier


## Related Links

-   Get elevation maps in tiff format for a given place at this website: https://srtm.csi.cgiar.org/srtmdata/

