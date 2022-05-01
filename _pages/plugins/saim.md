---
mediawiki: Saim
title: Saim
categories: [Analysis, Microscopy]
---


{% capture source%}
{% include github org='nicost' repo='saimAnalysis' %}
{% endcapture %}
{% include info-box software='ImageJ' name='SAIM (Scanning Angle Interference Microscopy)' author='Nico Stuurman (nico.stuurman at ucsf.edu)' maintainer='[Nico Stuurman](Nico_Stuurman)' filename='' source=source released='2015/11/20' latest-version='2016/09/28' category='Techniques' %}

# ImageJ/Fiji plugin to to analyze Scanning Angle Interference Microscope Data.

## Installation

To install this plugin check the "ValelabUtils" update site in the Fiji updater.

## Description

SAIM (Scanning Angle Interference Microscopy) is a technique to measure the distance of fluorescent dyes to the surface at nm resolution. To use it, one needs to place the sample on a silicon chip (that acts as a mirror) with a solicon oxide (glass) spacer). The reflection of coherent excitation light will interfere with the incoming beam and set up a standing wave pattern, resulting in fluorescence intensity that varies with distance to the surface. By varying the angle of incidence, the standing wave pattern changes in predictable ways, and a series of images at different angles can be used to deduce the height of fluorescence molecules, independent of their intensity. This technique is very well described by [Paszek et al.](http://www.nature.com/nmeth/journal/v9/n8/abs/nmeth.2077.html), and this plugin uses the equations from the Paszek et al. paper with a few [SAIM Math.pdf](/media/plugins/saim-math.pdf) extensions. A thorough description can be found in [our manuscript](http://www.nature.com/nmeth/journal/v13/n11/full/nmeth.4030.html) or in [the preprint version on BiorXiv](http://biorxiv.org/content/early/2016/04/26/050468). . If you use this plugin, please do cite that paper.

This plugin consists of three parts. "Saim Plot" plots theoretical predictions for the intensity distribution as a function of height.

<img src="/media/plugins/saimplotscreen.png" width="200"/> <img src="/media/plugins/saimplotoutput.png" width="500"/>

"Saim Inspect" and "Saim Fit" are very similar, however, Saim Inspect will act on the average values of the ROI (for instance, the pixel under the cursor) and executes only a single fit, whereas Saim Fit will analyze all pixels of the image stack. You will likely want to play with Saim Inspect first and determine reasonable guesses for A, B, and height. Note that you can fit with multiple guesses for the height (enter these as comma values, i.e. "50.0, 200.0, 350.0"), which is needed when the heights in your image span more than \~150nm. Use Saim Inspect to establish best guesses for A, B, and height (starting with a guess that is close to the final value will decrease the computation time).

![](/media/plugins/saiminspect.png) <img src="/media/plugins/saiminspectoutput.png" width="500"/>

Saim Fit will fit each pixel in the input stack and output a stack with 4 images, the first one is the height map (in nm), the second image has the r-squared values (an indication of the goodness of fit with values between 0 and 1, the closer to 1, the better the fit), the third image shows the values for "A", and the last image the values for "B". Saim Fit will use as many thread as you allow in {% include bc path="Edit | Options | Memory & Threads" %} and it is best to set that value to the number of cores in your computer. If there is significant movement while taking the stack, you will first need to "de-jitter" using another ImageJ plugin (such as StackReg). The output image will have the Fire LUT by default. Do note the "Thresholding" parameter. Only pixels that are higher in intensity than the threshold will be analyzed. This can greatly reduce the analysis time ("dark" pixels will be hard to fit and are usually uninteresting anyways).

![](/media/plugins/saimfit.png) ![](/media/plugins/saimfitoutput.jpg)

## Usage in a macro

To call the Saim analysis code in a macro, use the "Fit\_Macro" plugin. Macros can look like:

run("Fit\_Macro", "wavelength=488 sample=1.32 oxide=1900 first=-42 step=1 a=3 heights=28.0 ");

## Example Data

These datasets were obtained by imaging a phospho-lipid bilayer stained with DiO (488), DiI(561), and DiD(640nm) (data acquired by Kate Carbone). The parameters shown below were used for analysis.

[488 data set](http://valelab.ucsf.edu/~nstuurman/SAIM/160302_bilayer1_cal2_pos1_488-crop.tif)

[561 data set](http://valelab.ucsf.edu/~nstuurman/SAIM/160302_bilayer2_cal2_pos3_561-crop.tif)

[640 data set](http://valelab.ucsf.edu/~nstuurman/SAIM/160302_bilayer2_cal2_pos3_640-crop.tif)

<img src="/media/plugins/488-fit-parameters.png" title="fig:488_fit_parameters.png" width="271" alt="488_fit_parameters.png" /><img src="/media/plugins/561-fit-parameters.png" title="fig:561_fit_parameters.png" width="271" alt="561_fit_parameters.png" /><img src="/media/plugins/640-fit-parameters.png" title="fig:640_fit_parameters.png" width="271" alt="640_fit_parameters.png" />

Some of the single pixels fits we obtained look as follows:

<figure><img src="/media/plugins/example-single-pixel-fits.png" title="Example_single_pixel_fits.png" width="799" alt="Example_single_pixel_fits.png" /><figcaption aria-hidden="true">Example_single_pixel_fits.png</figcaption></figure>

## History

-   1.0.8 (2016-09-28): Added Fit\_Macro, a blocking version of the Fit plugin that can be called from a macro
-   1.0.7 (2016-04-22): Fixed bug that caused most pixels not to be fit
-   1.0.6 (2016-04-21): Added capability to export data and predictions from Inspect module.
-   1.0.5 (2016-04-05): Most settings are now shared between all 3 plugins and are remembered. Multiple start heights can now be entered in the fit module and the resulting fit with the lowest error will be reported.
-   1.0.4 (2016-4-05): Multiple heights can be entered in Inspect as a comma separated list. They will also be used to fit against the data and the best fit will be reported.
-   1.0.2 (2016-01-22): Added capability to export predicted data from Plot module
-   1.0.1 (2016-01-12): Changed calculation of rTE to what appears to be the correct formula

 
