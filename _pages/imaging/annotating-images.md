---
title: Annotating Images
section: Learn:Scientific Imaging
nav-links: true
---

## Scale bar

All images for publications should include a scale bar. A standard size should be used for the scale bars on all images if possible to help avoid confusion.

### Spatial calibration

An image's spatial calibration can be edited using {% include bc path="Image|Properties" %}. Note that the units "um" will automatically change to "µm".

Some microscope models (e.g., Biorad PIC, and Zeiss LSM confocal image files) will use the zoom and objective magnification settings for internal calibration. However, it is important to keep in mind that some file formats (e.g. Perkin Elmer) are not calibrated while some "exported" image files (e.g. Zeiss zvi's exported as TIFFs) will lose their calibration information completely.

In the case that the files have no calibration, you can apply the calibration using images of a stage micrometer with the same settings as your experiment. These settings include camera binning, frame size, objective, confocal zoom, etc. Then the calibration can be applied using {% include bc path="Analyze|Set Scale" %} ([see below](#set-scale)). Spatial calibration can also be found and set in the {% include bc path="Image|Properties" %} dialog. The "*Microscope Scale*" plugin is another alternative and can be customized using a drop-down box of objectives to apply spatial calibrations.

{% include img src="set-scale-plugin" width="179" height="200" %}

Sometimes the spatial calibration may be lost after applying an image processing function. In this case, use the original file's spatial calibration (located under {% include bc path="Image|Properties" %}) to update the {% include bc path="Image|Properties" %} values of the final, processed image.

There are three ways to reapply spatial calibration: manually via the {% include bc path="Image|Properties" %} dialog; using the "Copy Pixel Size" plugin that applies pixel size of one image to a second image; or with the "Set Scale" plugin.

#### Copy-calibration

{% include img src="copy-pixel-size" %}

1.  Open the image with the original calibration
2.  Run the "Copy Pixel Size" plugin.
3.  In the "*from*" drop-down box select the original image; in the "*to*" box, select the processed image. Click OK.
4.  In the new dialog, enter a value by which the receiving image has been scaled.

{% include img src="copy-pixel-size-values" width="180" height="240" %}

#### Set Scale

If you know the size of a feature (for example, a previously applied scale bar) you can use this command to apply a calibration.

1.  Using the line selection tool, draw a line along the length of the feature or scale bar. Do not choose {% include bc path="Edit|Draw" %} after adding the line.
2.  Run the menu command {% include bc path="Analyze|Set scale..." %}.
3.  Enter the dimensions of the object/scale bar in the "*known distance*" box and set the units in the "*Unit of length*" box.
4.  Do not check *Global* unless you want all your images to have this calibration. Click OK.

### Adding scale-bar

First, use the line ROI tool to draw a line with approximately the desired location and length.

Run the scale bar dialog via the "Add Scale Bar" plugin. Change the "*Width in \*\*\**" value to something sensible (5, 10, 50 etc.). "*Height*" will determine how many pixels fat your bar will be.

If you've used the "Green" LUT, then the "white" (i.e. gray level 255) scale-bar will appear green. Convert the image from 8-bit color to RGB with {% include bc path="Image|Type|RGB color" %} before adding the scale bar to get a white scale-bar on a pseudocolored image.

Check the "*Label all slices*" box to add a scale-bar to the whole stack.

This plugin points to the native menu command {% include bc path="Analyze|Tools|Scale bar..." %}.

## Text and lines

### Issues with adding text

Adding text to single frame images should be done in CorelDRAW or a similar application so the text does not become part of the image and can therefore be edited at any time. Adding text to an image/movie is irreversible so it should not be done on raw data. Images can be copied to and pasted from the system clipboard between programs by using the *"Copy to System"* and *"Paste"* options in the {% include bc path="Edit" %} menu. This supersedes the System Clipboard plugin (Plugin documentation found [here](https://imagej.nih.gov/ij/plugins/clipboard.html)). In the case that an image is not pasting accurately, use {% include bc path="Edit|Paste Special" %} in the receiving application, then select "*Device independent bitmap*".

Always save your images before adding text. Text color is set via the color picker button on the tool bar. Double-click on it to open the palette and choose a color.

Pseudocolored images should be converted to RGB ({% include bc path="Image|Type|RGB color" %}) prior to adding text. The text is "anti-aliased". This means that instead of being completely white in color, some pixels on the curved edges of letters are averaged with neighboring pixels. This makes these pixels gray and helps the text to appear smoother.

{% include img src="aliased-text" %}

Since some of the pixels in anti-aliased text do not have the gray-scale value of 255, some LUTS will display the pixels as other colors such as orange or green. This will lose the smoothing affect from antialiasing.

{% include img src="antialiased-lut" %}

Frame 1 counter text when used with Hot Green LUT.

Another potential problem is that if you use the red or blue LUT then the text will appear red or blue even though you selected the text to be "white" via the color picker.

To avoid this, convert the pseudocolored image from its current format (i.e. *8-bit color*) to an RGB image with {% include bc path="Image|Type|RGB color" %} before adding the text.

{% include img src="corrected-lut" %}

Text on converted image.

### Adding Text/Line/Box

Drawing lines/boxes is achieved by first using the line/rectangle ROI tool from the toolbar or defining the box via the *Specify Line* or *Specify ROI* plugins. The line/box can then be stamped in to the image through {% include bc path="Edit|Draw" %} or the shortcut {% include key keys='Ctrl|D' %}. If you're drawing the ROI on a stack, you'll be asked if you want to process all of the slices. Choosing 'yes' will draw the ROI on every slice while choosing 'no' will result in the ROI only being added to the current frame. The color is determined by the color picker toolbar button and the width in pixels is defined in {% include bc path="Edit|Options|Line width" %}. The line width must be determined before it is drawn on the image.

Adding text is done with the toolbar's text button. Click the toolbar, click the image, and write the desired text. Double click on the toolbar-text button to set the font size and style. Color is determined by the color picker toolbar button. Antialiasing can be turned on/off via the menu item {% include bc path="Edit|Options|Fonts" %} and unchecking the "Smooth" option (although this option does not affect the Stamper plugins which have antialiasing on permanently). The text is stamped onto the image through the same methods of drawing on a box or line ({% include bc path="Edit|Draw" %} or {% include key keys='Ctrl|D' %}).

It is possible to add a line, box, or text to each slice in a stack. After adding to a single slice and selecting {% include bc path="Edit|Draw" %}, you will be asked if you want to apply the selection to every slice. Keep in mind that there is no undo option for this operation.

Adding text to a stack is a slightly different process. You can draw a text box by following the same steps, but on a stack, keyboard shortcut {% include key keys='Ctrl|B' %} will overlay the text on the current slice, while shortcut {% include key keys='Ctrl|D' %} will draw the text on every slice of the stack.

### Adding timestamps

Open the *Time Stamper2* plugin. From here, you can specify the location, interval, format, and other properties of the time stamp.

{% include img src="/media/time-stamper.png" width="166" height="237" %}

Alternatively, you can also draw a rectangular ROI at the location and approximate size of the desired counter. The text will, by default, be the same height as the ROI and aligned to its left edge. Note that if the rectangle is drawn on the right side of the image, the text could be cut off on the right in the case that the size is too large.

Remember: bigger text will typically look smoother and the timestamp will be easier to read. It may be worth changing it to a consistent value for all of your movies.

Also, bear in mind that the interval doesn't necessarily need to be "time". The Time Stamper can also be used to add "z-axis depths" to z-stacks and "angle of rotation" to rotating volume movies (° = {% include key keys='Alt|2' %}-{% include key key='4' %}-{% include key key='8' %}; µ = {% include key keys='Alt|2' %}-{% include key key='3' %}-{% include key key='0' %}).

### Adding event markers to a movie

The *Event Stamper* plugin can be used to add text to a movie for a designated number of frames. Set the desired text in the "Text" box, enter the start frame and end frame and click OK. The text size and location are taken from the current ROI and can be changed once the dialog is open.

### Series Labeler plugin

The [Series Labeler](/plugins/series-labeler) plugin, allows quite flexible text labeling for movies and z stacks, with preview functionality, so you can see what you are going to get.

 
