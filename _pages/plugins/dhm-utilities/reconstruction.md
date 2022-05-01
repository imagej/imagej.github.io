---
mediawiki: DHM_Utilities/Reconstruction
title: DHM Utilities/Reconstruction
project: /plugins/dhm-utilities
name: Reconstruction
source-url: https://github.com/sudgy/reconstruction
license-url: /licensing/lgpl
license-label: LGPLv3
dev-status: Active
support-status: Active
team-founders: David Cohoe | mailto:dcohoe@pdx.edu
team-leads: David Cohoe | mailto:dcohoe@pdx.edu
team-developers: David Cohoe | mailto:dcohoe@pdx.edu
team-debuggers: David Cohoe | mailto:dcohoe@pdx.edu
team-reviewers: David Cohoe | mailto:dcohoe@pdx.edu
team-support: David Cohoe | mailto:dcohoe@pdx.edu
team-maintainers: David Cohoe | mailto:dcohoe@pdx.edu
---

Reconstruction is a plugin to reconstruct holograms and perform numerical propagation, with a focus on holograms produced by DHM. The plugin is highly extendable, with anybody able to add new plugins within it to perform whatever process they want at any point in the reconstruction pipeline. By default, it includes support for angular spectrum propagation, and for various noise removal techniques such as a reference hologram and a polynomial fit algorithm.

## Overview

To run the command, run {% include bc path="Plugins | DHM | Reconstruction" %}. When running the command, a dialog box will pop up asking for parameters for all enabled plugins. The parameters that are always there are as follows:

-   Hologram(s): The hologram stack to reconstruct. This plugin is capable of reconstructing a stack of images through time.
-   Wavelength: The wavelength of light used to acquire the hologram.
-   Image Width: The width of the hologram, in real units.
-   Image Height: The height of the hologram, in real units.
-   t slice selection: The time slices to reconstruct from the original hologram stack. See below for more info on how each choice works.
-   Z plane selection: The z planes to propagate to. See below for more info on how each choice works.

Once you have finished with the dialog, the command will perform the following algorithm:

-   From the original hologram, get the filter on the Fourier transform of the hologram to use.
-   For each time slice selected, do the following:
    -   Filter the hologram
    -   For each z plane selected, do the following:
        -   Propagate the field

Plugins can insert their own operations at any point during this process. For example, the Reference Hologram plugin removes noise after filtering each time slice, and the Result plugin gets the final result after propagating the field.

You can run the entire thing yourself in code using `ReconstructionOp`. See the documentation for more details on how to use it.

### t slice selection

The t slice selection sets which frames of the hologram stack you want to reconstruct. It will not show up if the hologram you selected only has one time slice. The different options for choosing t slices are as follows:

-   Single: Reconstruct only a single frame from the hologram stack.
-   Current Frame: Reconstruct only the current selected frame from the hologram stack.
-   All: Reconstruct all frames from the hologram stack.
-   List: Reconstruct any arbitrary frames, as a comma-separated list of time values.
-   Range: Reconstruct a range of t slices, given a starting point, ending point, and step size. For example, if your starting point was 2, your ending point 8, and your step size 2, it would reconstruct slices 2, 4, 6, and 8.
-   Continuous Range: The same as Range, but with the step size set to one.

### Z plane selection

The Z plane selection sets which z values you want to propagate to. The different options for choosing z value are as follows:

-   Single: Propagate only to a single particular z value.
-   List: Propagate to any arbitrary z values, as a comma-separated list of time values.
-   Range: Propagate to a range of z planes, given a starting point, ending point, and step size. For example, if your starting point was -1 μm, your ending point 1 μm, and your step size 0.5 μm, it would propagate to -1 μm, -0.5 μm, 0 μm, 0.5 μm, and 1 μm.

## Default Plugins in Detail

### Filter

The Filter plugin acquires and applies a filter on the Fourier transform of the hologram. When run from the command, it will show a window with the Fourier transform and ask the user to select an ROI for the filter. When running the command from code, you may use whatever ROI you wish. Many other plugins use the Filter plugin as well so that they can use the same filter.

### Polynomial Tilt Correction

The Polynomial Tilt Correction plugin performs tilt correction using a polynomial fit to the phase, as specified in [this](https://www.osapublishing.org/ao/abstract.cfm?uri=ao-45-5-851) paper. The gist of the algorithm is that you find horizontal and vertical lines that <em>should</em> be flat, then find a polynomial fit to those lines, and subtract those polynomials from the phase. When you use this plugin, on the dialog it will ask for the polynomial degree to use. In our use, the only issues we have had were a linear tilt from a bad selection for the filter, but you may use whatever you wish.

The flat line determination is the interesting part. This is configurable through plugins, with three defaults:

#### Auto

The Auto plugin determines the flat lines automatically. For each direction, it picks up to ten lines and finds the polynomial fit on each one. It then uses a least-squares approach to find which polynomial fits its respective line the best, and then chooses that line. It has no extra parameters.

#### Middle

The Middle plugin uses the lines crossing through the middle of the image as the flat lines. It has no extra parameters.

#### Manual

The Manual plugin lets the user input their own lines. Because the edges of the reconstructed images are always a little strange, it is advised to not use values near the edge. It has several extra parameters:

-   Pixel value for horizontal line: The y pixel value that the horizontal line will be on.
-   Horizontal line start: The x pixel value that the horizontal line will start at.
-   Horizontal line end: The x pixel value that the horizontal line will end at.
-   Pixel value for vertical line: The x pixel value that the vertical line will be on.
-   Vertical line start: The y pixel value that the vertical line will start at.
-   Vertical line end: The y pixel value that the vertical line will end at.

### Reference Hologram

The Reference Hologram plugin corrects noise issues using a reference hologram as specified in [this](https://www.osapublishing.org/oe/abstract.cfm?uri=oe-14-10-4300) paper. The plugin also has support for using the reference hologram to deal with amplitude noise as well, as specified in [this](https://iopscience.iop.org/article/10.1088/0957-0233/19/7/074007/pdf) paper. When the reference hologram is enabled, you have the option to use it to cancel phase and/or amplitude. There still seems to be a few issues with the amplitude reference hologram, so use it at your own discretion. Also, for most reference hologram algorithms, there is the option to use the same ROI. Checking this box will make the reference hologram use the same filter as everything else.

The method of acquiring the reference hologram is configurable through plugins, with several defaults:

#### None

Don't use a reference hologram.

#### Single Image

Use a single image as your reference hologram.

#### Single Image With Offset

Use a single image at a time as your reference hologram, but pick them relative to the current time slice being reconstructed. The offset is added to the original hologram time slice, and the result is what time slice to use for the reference hologram.

#### Median

Use the median of an image stack as your reference hologram. You may select certain time slices here like for the time parameter above.

#### Median With Offset

Use the median of an image stack as your reference hologram, but pick the slices relative to the current time slice being reconstructed. You may select certain time slices here like for the time parameter above. The offset is added to the original hologram time slice, and the result is what is considered frame 1 for calculating the median.

#### Self

Use the current hologram itself as the reference hologram. The idea is to use the very center of the Fourier transform to remove just the large-scale issues while keeping the small-scale samples intact. As such, this doesn't allow you to use the "use same ROI" option.

### Propagation

The Propagation plugin sets up the data for propagation. Because there are different methods of propagation, this is configurable through plugins. Currently, the only default method of propagation is Angular Spectrum.

#### Angular Spectrum

This plugin actually propagates the data. It is based off of Opto-Digital's [Numerical Propagation](https://unal-optodigital.github.io/NumericalPropagation/) plugin, but it has been changed slightly to allow for faster computations when propagating to many z and time slices.

### Result

The Result plugin gets the result of the whole command and finds a way to display it to the user. It adds four checkboxes to the dialog near the bottom for which parts of the resulting fields you want: the amplitude, the phase, the real part, and the imaginary part. It also adds a choice for if you want an 8-bit, 16-bit, or 32-bit image. Finally, to actually get the result, in the command you can either save it to a file, or if not, it will display it directly. If running the command in a program, you can set the method it calls once it's finished to whatever you like.

### Status

The Status plugin just updates the status bar during the command's running.

## Options

Every plugin has options that can be changed in the {% include bc path="Plugins | DHM | Reconstruction Options" %} command. Here the units for some of the values can be changed, plugins can be enabled/disabled, and plugins can put their own options here too. Here are the options that the default plugins have:

### Propagation/Angular Spectrum

The Angular Spectrum plugin can cache a lot of its processing to speed up the process. However, when performing a large amount of reconstructions, the memory used could increase too much. You can change the cutoff point of the cache size here, or disable caching entirely.

## Creating Your Own Plugin

To create your own plugin type, you must implement `ReconstructionPlugin`. If you want the plugin to show up in the normal command, you must use the `@Plugin` annotation. If you do this, you must implement either `MainReconstructionPlugin` or `SubReconstructionPlugin`. The plugin interface has methods for all of the different parts of the reconstruction pipeline. Override whichever you wish, and your plugin will be executed along with all of the other plugins. For more information on how to make your own plugin, please consult the documentation on github.


