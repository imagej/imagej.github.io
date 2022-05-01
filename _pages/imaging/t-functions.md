---
mediawiki: T-functions
title: T-functions
section: Learn:Scientific Imaging
nav-links: true
---

## Correcting for bleaching

Often, during acquisition of a time-course, the fluorophore may bleach and the intensity of the image is reduced. This can make it harder to discern events at the end of the sequence. A stretch in contrast at the first time point may not be adequate 100 time points later. The process of bleaching and decrease in image intensity can be fitted with a mono-exponential decay, although it often follows a bi-exponential. A mono-exponential decay is described by the equation:

**Corrected intensity = (Intensity at time *t*) *÷* exp<sup>-k×*t*</sup>** where k = decay constant

<figure><img src="/media/imaging/bleach-correction-window.png" title="bleach_correction_window.png" width="257" height="112" alt="bleach_correction_window.png" /><figcaption aria-hidden="true">bleach_correction_window.png</figcaption></figure>

If you know the decay constant *k*, you can use the plugin {% include bc path="Image|Adjust|Bleach Correction" %} with the exponential fitting method. It may be worth performing a background subtraction prior to running the plugin. Note that the plugin is expecting the k value to be "per-slice" rather than per-second, per-minute, etc.

Raw time course

![](/media/imaging/bleach-raw-data.png)

Bleach corrected time course

![](/media/imaging/bleach-corrected-data.png)

The k value can be calculated in ImageJ by:

1.  Make sure the {% include bc path="Edit|Options|Profile Plot Options" %} setting "Do not save x-values" is off.
2.  Select a region of the cell or the whole image and plot the decay using the menu command {% include bc path="Image|Stacks|Plot Z-axis Profile" %}.
3.  Click the *Copy* button of the plot window.
4.  Open the curve fitting dialog {% include bc path="Analyze|Tools|Curve Fitting" %}.
5.  Delete the default data and paste in your copied data.
6.  Select "Exponential" from the option list and click the "Fit" button.
7.  In the *Log* window, scroll down to find the value labeled as "b", this is your *k* value.

Since bleaching is often not mono-exponential, quantification of fluorescence intensities after bleach correction is not possible. This plugin should only be used to enhance time-course movies for presentation rather than quantification.

![](/media/imaging/contrast-window.png)

Another way to compensate for bleaching is to use the menu item {% include bc path="Process|Enhance Contrast" %}. This method is quicker to implement than the proper bleach correction above and can be useful for correcting for fluorophore bleaching during a movie if the intensity of the fluorophore is changing only because of bleaching. Check the "Process Entire Stack" option and the plugin will scan through the stack applying brightness and contrast adjustment selected on each slice based on each slice's histogram. The intensity values are adjusted so that quantitative intensity measurements are no longer possible.

Again, use this function to enhance movies for presentation, not quantification.

## F÷F0

![](/media/imaging/f-f0-raw.png) ![](/media/imaging/f-f0-corrected.png)

There are several drawbacks with the use of single wavelength fluorescent probes; some include uneven fluorescence intensity (F) due to cell thickness and cell to cell variation in loading. These can be largely corrected by normalizing fluorescence against resting fluorescence i.e. F0. This does not correct for bleaching and dye loss during the experiment.

First ensure the image is properly background corrected:

1.  Generate an "F0" image by averaging the first few frames of the stack. This can be done with the {% include bc path="Image|Stacks|Z-project" %} menu item (Fiji assumes stacks to be z-series rather than t-series), using the "*Average Intensity*" drop-down box option. Select "Start slice" as 1 and "Stop slice" as 5-10 depending on how many frames you wish to average. Rename the new z-projected image ({% include bc path="Image|Rename" %}) "Fzero".
2.  Open the "Image Calculator" via {% include bc path="Process|Image Calculator" %}. Set Image 1 as the original stack, image 2 as "Fzero", and the operation as divide. Select "32-bit Result" and "Create New Window".
3.  Rename this result window ({% include bc path="Image|Rename" %}) FdivF0.
4.  The maximum and minimum intensity in the stack can be determined with the Analyze Histogram plugin, using the stack histogram option.
5.  Using the Brightness and Contrast dialog, set the maximum and minimum to these values.
6.  Convert the 32-bit stack to 8-bit ({% include bc path="Image|Type|8-bit" %}).
7.  The Images in FdivF0 will probably have a noisy background between the cells and will need to be cleaned up. Using your original stack, create a mask of the cells. This is done by first thresholding the original stack ({% include bc path="Image|Adjust|Threshold" %}). Hit the Auto button and then adjust the sliders until cells are all highlighted red. Then click "*Apply*". Check the tick box: "black foreground, white background". You should now have a white and black image with your cells black and background white. If you have white cells and black background, invert the image with {% include bc path="Edit|Invert" %}.
8.  Use the Image calculator {% include bc path="Process|Image calculator" %} to subtract this black and white stack from your FdivF0 stack.
9.  Pseudocolor to taste.

The F divided by F0 steps are automated in the *"F\_div\_F0"* macro. This will return the FdivF0 stack and a thresholded FdivF0 stack.

## Delta-F

![](/media/imaging/delta-f-raw.png)

**Raw**

![](/media/imaging/delta-f-corrected.png)

**Delta-F up**

Rapid frame-to-frame changes in intensity (e.g. calcium "puffs" or TMRE "depolarizations") can best be illustrated by subtracting each frame from the previous/next. Use the plugin "*Delta F up*".

For increases in intensity (e.g. a calcium "puff") the calculation is \[Frame<sub>(n+1)</sub>-Frame<sub>n</sub>\]. Use the plugin "*Delta F down*".

For drops in intensity (e.g. TMRE plus irradiation induced mitochondrial depolarisations) the calculation is \[Frame<sub>n</sub> - Frame<sub>(n+1)</sub>\].

Note: The plugin generates a second result stack. For large memory consuming stacks, run the plugin with the {% include key key='Alt' %} key down. If the plugin is run with the {% include key key='Alt' %} key down, the calculation is made on the original stack. This plugin may also be useful to clean up time courses prior to motion tracking.

## Surface plotting

![](/media/imaging/surface-plot-compare.png)

Surface plots can be generated in many ways: notably via the menu command {% include bc path="Analyze|Surface plot" %} or via the plugins "*SurfaceJ*" and *"Interactive 3D Surface Plot*". These functions will surface-plot movies as well as single frame images. Ensure the features you're interested in are "Contrast stretched" optimally. This can be done using a "Max intensity projection" on the stack. Get the max and min pixel intensities and apply these to the stack. Remember, do not perform intensity analysis on images that have had their contrast stretched.

### {% include bc path="Analyze|Surface plot" %} settings

When this function is selected, a dialog will appear. Try the settings below first and play with them to optimize the surface plot. The LUT of the final surface plot is taken from the LUT of the image.

<figure><img src="/media/imaging/analyze-surface.png" title="analyze_surface.png" width="212" height="243" alt="analyze_surface.png" /><figcaption aria-hidden="true">analyze_surface.png</figcaption></figure>

### SurfaceJ settings

You can surface plot either a single frame or a movie. Surface rendering is a slow process so it is best to pick a frame from the movie that shows the features you're trying to demonstrate. Duplicate this ({% include key keys='Ctrl|D' %}) and use it as a test image to get the best settings for surface plotting your movie.

Select the image to be rendered with the "*Source image(s)*" drop down box.

The options with three text-entry boxes along side represent x, y and z values.

"*Rotate(°)*": value of -20 in the first (*x*-axis) box gives a good 3D effect. Play with this.

"*Scale*": Set to 0.5 to render more quickly when adjusting the settings and set to 2 or more for the final surface plotting.

"*Aspect*": Surface plot can be stretched in "height" by increasing the z-axis aspect (i.e. the third) box. A value of 1 is usually OK if you've stretched the contrast properly. This will not affect the pseudocolor of the peaks which is determined by the pixel intensity.

"*Index LUT*": by default the plot will have the "spectrum" LUT. Change this drop-down box to "*Load custom*" and you'll be prompted to locate a desired LUT when you start the surface-plot.

"*Gaussian Smoothing*" value of 2-4. This slows rendering down but gives smoother surface plot.

"*Render surface plot*": starts surface plotting.

 
