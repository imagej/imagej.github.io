---
title: Colocalization by Cross Correlation
layout: page
categories: Colocalization,Plugins
description: How to use the Colocalization by Cross Correlation plugin
---
{% include info-box software='Fiji' name='Colocalization by Cross Correlation' maintainer=' [Andrew McCall](https://imagej.net/User:Amccall)' author=' [Andrew McCall](https://imagej.net/User:Amccall)' source=source status='active' released='2020' category='[:Category:Plugins](Category_Plugins), [:Category:Colocalization](Category_Colocalization)' %}

## Colocalization by Cross Correlation

This plugin attempts to determine the average distance between non-randomly spatially associated particles, the standard deviation of that distance (which should also reflect the width of the PSF in the image for diffraction limited images), and a statistical measure of confidence of the association. It does this by performing a cross-correlation function (CCF) between the two images, operating in a similar manner to Van Steensel's CCF but this plugin performs the CCF in all directions and provides additional information, such as a confidence level. It currently works on 2D/3D single-channel images, and requires a mask of all possible localizations for the signal in one of the images.

### Installing the Plugin:

Available on the list of [ImageJ updates sites](Update_Sites). Requires Fiji.

### How to use Colocalization by Cross Correlation:

1. Prepare a mask for the Costes randomization: To get the best possible results, you will want to create and save a [segmented mask](Segmentation) for one of your images. This mask should contain all possible localizations for that stain/dye. As an example, say you are studying correlation between two nuclear proteins, then you would want your mask to cover the nucles, which could be done easily using a DAPI or Hoechst stain (the mask itself does not need to be generated from either image your are trying to correlate). If you were studying cytoplasmic proteins, you would want your mask to cover the entire cytoplasm. The mask is very important and not using it could easily lead to undesired correlations. This is because without a mask this plugin will find correlations at any distance, and can easily correlate one cell to another neighboring cell (cells are often highly repitive and correlate with one another). However, when an appropriate mask is used, these cell-cell correlations will be subtracted out prior to analysis.
2. Prepare your correlation images: The two images should undergo appropriate background subtraction to lower the background pixel values to zero or near zero. Even low level background (pixel values of 10 to 20 on a 16 bit image) can lower the confidence level and result in false negatives. Additionally, the images (particularly 3D) need to be correctly scaled (Image > Properties), otherwise all axes will be assumed to have the same scale and your mean correlation distance will be in pixels.
3. Determine your point-spread function (PSF) dimensions: During a Costes randomization images are randomized by PSF-sized chunks, rather than individual pixels. To facilitate this, the plugin needs to know the approximate size of the image PSF in pixels (rounded to the nearest whole unit). The PSF size can be calculated using the Abbe diffraction formula for fluorescence microscopy (lateral - 0.5λ/NA, axial - 2λ/NA^2), and then simply needs to be divided by the corresponding pixel size. 
4. The plugin can be found in the Analyze > Colocalization menu after it has been installed. Currently, due to a persistant bug, the plugin only works on saved image files, though I hope to fix this in the future. At the dialog menu, select the two images and the randomization mask to be used, and enter the PSF width and height in pixel units. For the Costes’ randomization cycles count, you can typically input a low number (3-5), however if you have sparse signal within a large mask volume you will probably want to do more cycles. If the “Show intermediate data” box is checked, the plugin will open images showing the correlations (before and after subtraction of random associations), and a sample randomization image. This can be useful for understanding the function of the plugin, or for visualizing the direction of the correlation if your sample has a polarized axis.

### Interpreting the results:

{% include figure-right name="Radial profile" image_path="/media/ColocByCorrelate-Graph.jpeg" content="Radial profile of correlation image shown above" %}

After the plugin has finished, two new windows will be open:

{% include figure-right name="Gaussian fit results" image_path="/media/ColocByCorrelate-GaussFit.jpg" content="Example result of a gaussian fit to the above radial profile" %}

Correlation plot: A radial profile plot will be displayed, it contains the radial profile of the original correlation image (black line), the radial profile of the correlation after subtraction of random associations (red line), and a Gaussian curve fit to the subtracted profile (blue dots). The Y-axis is the result of the average correlation function at a given distance. While not arbitrary, it is most easily viewed as a measure of relative correlation. The range of the graph is set automatically to fit the Gaussian curve. If you wish to view all the data select More > Set Range to Fit all…

Gaussian fit analysis: This text window will contain (in scaled units), the mean distance for the discovered correlation, and the standard deviation of that correlation (sigma), as well as an estimation of confidence for this correlation (range 0-100). The confidence is determined by taking the area under the curve (AUC) of the subtracted correlation radial profile (in range of mean ± 3×sigma) divided by the AUC of the original correlation radial profile (in same range). Values closer to 100 indicate a strong likelihood of true correlation. Values near zero indicate low to no correlation between the two images. I currently estimate that values of \~20 or greater indicate some degree of correlation (within the range specified by the Gaussian curve), though this is with very limited data. Confidence values can be affected by many things, including image noise and background, an inappropriate randomization mask, and optical abberations. Performing a simple background subtraction can improve confidence scores signficantly.

### How it works:

{% include figure-right name="Correlation Image" image_path="/media/ColocByCorrelation-CorrelationImage.jpg" content="**Correlation Image**: Example image produced by the correlation function of two images." %}

The plugin performs a cross-correlation in frequency space to create a correlation image. To remove non-specific correlations (from background, or high signal density), a correlation image generated from randomized images is then subtracted from the original correlation image. This occurs through cycles of:

1. Randomizing Image1 using the [Costes randomization method](/media/Costes etalColoc.pdf) and a mask of all theoretically possible localizations for the signal in Image1 (i.e. a mask of the cells, or the nuclei).

2. Calculating the cross-correlation of the randomized image with Image2, then averaging this over successive cycles.

After the subtraction of non-specific correlations, we generate a radial profile of this data and fit a gaussian curve to it, showing the correlation between the images at different offsets. We also generate a radial profile for the original correlation data before subtraction, as this is needed to establish a measure of confidence. The confidence is calculated as the area under the curve (AUC) of the subtracted correlation radial profile (in the range of mean ± 3×sigma) divided by the AUC of the original correlation radial profile (in same range) as a percentage. The confidence value, along with the mean and sigma of the gaussian fit are displayed in a log window. Higher values of confidence, closer to 100, indicate that two images likely have a true spatial correlation at the indicated distance.





 
