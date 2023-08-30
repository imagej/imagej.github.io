---
title: High Pass
categories: [Filtering]
dev-status: "stable"
icon: /media/icons/plugin_icon_ImageJColor.png
---

# High-Pass Filter

**A plugin-filter providing a high-pass command. It subtracts the Gaussian blurred input image from the input image.**

## Dialog Options
![Dialog screen shot](/media/plugins/high-pass/high-pass-screenshot.jpg)
- **Radius (Sigma)** is the standard deviation (blur length) of the Gaussian that will be subtracted.
- **Scaled Units** (spatially calibrated images only) should be selected if "Radius (Sigma)" is not in pixels but in physical units (e.g., micrometers).
- **Shift Values to Display Range** adds an offset so that the output will fit into the currently displayed data range. This option should be selected when processing only a selection of a 32-bit (float) image that does not have its pixel values around zero. This option is also useful for most 16-bit images.
- **Preview** is available with the Preview checkbox.
If "Shift Values to Display Range" is unchecked, the offset, i.e. the output created by flat portions of the image, will be 0 for 32-bit float, 32768 for 16-bit and 128 for 8-bit (grayscale or RGB) images.

## Pixel Value Calibration (8-bit & 16-bit images only)

If the full image is processed, for grayscale 8-bit and 16-bit images, the grayscale (pixel value) calibration will be set to have zero value at this level. Thus, one can use, e.g., Process>Math>Square after high-pass filtering to highlight all pixels deviating from their surrounding.

Note that Undo will revert only the image contents, not the calibration.

## Download
* Source code `High_pass.java` {% include github org='imagej' repo='imagej.github.io' branch='main' path='media/plugins/high-pass/High_pass.java' %} (make sure you download the **raw** file, use the button near the top right)
* Class file `High_pass.class` {% include github org='imagej' repo='imagej.github.io' branch='main'  path='media/plugins/high-pass/High_pass.class' %}

## Installation
- Copy the raw `High_pass.java` file into the ImageJ plugins folder or a subfolder thereof. Make sure that you name the downloaded file ”High_pass.java”; uppercase/lowercase matters.
- Compile with “Compile and Run” and press “OK”. Note that "Compile and Run" is currently broken on Fiji; as a workaround use File>New>Script, open the `High_pass.java` file and press “Run“.
- Alternatively, directly save the .class file `High_pass.class` into the ImageJ/plugins directory or an immediate subdirectory thereof. Again, make sure that you name the file correctly, uppercase/lowercase matters.
- Use Help>Update Menus or restart ImageJ to make it appear in the Plugins menu (not necessary if you have used the Fiji Script Editor).

## Version history
Version 2020-Jan-03, Michael Schmid: Nonblocking dialog
