---
title: Feature Finder
categories: [Feature Extraction]
dev-status: "stable"
icon: /media/icons/plugin_icon_ImageJColor.png
---
# Feature Finder
**An ImageJ template matching plugin, finds features equal or similar to a prototype (template). "Similarity" means that the mean square deviation between the image and the translated prototype should be low.**

## What's nice about it
- After a (slow) initial calculation, preview provides a fast way to determine the similarity threshold.
- Subpixel accuracy.
- During preview, possibility to refine the prototype by averaging over features found.

## Limitations
- Works with grayscale images only; any calibration of pixel values is ignored.
- Only searches for unrotated (or circular) and unscaled features.
- Slow except for small prototypes (brute-force algorithm, no FFT).
- During preview, while the prograss bar is active: don't change any input in the dialog box, otherwise it will restart and take even longer.
- Does not process stacks.

## Dialog Options
![Dialog screen shot](/media/plugins/feature-finder/feature-finder-screenshot.jpg)
- **Prototype from** selects the prototype. This can be a ROI of the current image or a different image.
- **Output Type** can be:
  - Point Selection: A Point ROI of the centers of all features.
  - Count: The number of features found is written to the Results Table.
  - List: A list of x and y pixel coordinates of the centers is written to the Results Table.
  - List (calibrated): like as 'List', but writes calibrated x and y coordinates to the Results Table.
  - Point Map: A separate binary image with one pixel=255 at the center of each feature.
  - Deviation Map: A separate float (32-bit) image. The value at each point indicates how much the surroundings of this position in the original image deviate from the prototype. The Deviation Map is independent of the 'Tolerance' settings.
  - Average of Features: A separate float (32-bit) output image with the average of all features shifted to the same position.
- With **Subtract Background**, features are considered the same independent of any constant (additive) background.
- **Soft Edges** gives less weight to the near-edge pixels of the prototype than to those near the center.
- If features are close together, closer than **Distance Min**, then only the one with the best match is kept.
- **Tolerance** determines how much a feature may deviate from the prototype. A value of 0 means an exact match, 100 means that the deviation equals the variance of the prototype. With 'Subtract Background' on, at a tolerance of 100% also image areas with a constant value over the prototype area qualify as features.
- During preview, after setting the tolerance you may press the **Refine** button. This calculates a new prototype from the average of all features currently selected. 'Refine' is useful, e.g., if the prototype suffers from noise.

During preview, the dialog also displays a histogram of the number of features vs. deviation from the prototype and a message with the number of features found. (Due to a Java bug, updating of the number of features may sometimes fail with Mac OS X.)

## Tips and tricks
  * During preview, the histogram often shows a broad peak at the right side. These are the false matches. Keep the threshold below this peak.
  * Features should have the same gray level contrast as the prototype. If this is not the case, it is advisable to select a template with the highest contrast that may occur in the image.
  * If thresholding fails, you can also try to create a Deviation Map and work on it (background subtraction, high-pass filter, find maxima ...)

## Download
* Source code `Feature_Finder.java` {% include github org='imagej' repo='imagej.github.io' branch='main' path='media/plugins/feature-finder/Feature_Finder.java' %} (make sure you download the **raw** file, use the button near the top right)

## Installation
- Copy the raw `Feature_Finder.java` file into the ImageJ plugins folder or a subfolder thereof. Make sure that you name the downloaded file ”Feature_Finder.java”; uppercase/lowercase matters.
- Compile with “Compile and Run” and press “OK”. Note that "Compile and Run" is currently broken on Fiji; as a workaround use File>New>Script, open the `Feature_Finder.java` file and press “Run“.
- Use Help>Update Menus or restart ImageJ to make it appear in the Plugins menu (not necessary if you have used the Fiji Script Editor).

## License
[GNU General Public License](http://www.gnu.org/licenses/gpl.html) v2, v3 or later

## Version history
- Version 2010-Dec-28, Michael Schmid: Plugin released
- Version 2012-Dec-23, Michael Schmid: Uses parallel processing on multi-core machines (faster)
- Version 2020-Mar-13, Michael Schmid: Non-blocking dialog; output type 'List (calibrated)' added

