---
mediawiki: Bleach_Correction
title: Bleach Correction
project: /software/fiji
categories: [Uncategorized]
artifact: sc.fiji:CorrectBleach_
---

## History

The plugin was made available by {% include person id='miura' %} and Jens Rietdorf and the full documentation is available [here](https://wiki.cmci.info/downloads/bleach_corrector). 

## Citation

Miura K. Bleach correction ImageJ plugin for compensating the photobleaching of time-lapse sequences [version 1]. F1000Research 2020, 9:1494 [https://doi.org/10.12688/f1000research.27171.1](https://doi.org/10.12688/f1000research.27171.1)

## Details

This plugin contains three different methods for correcting the intensity decay due to photobleaching. They all work with either 2D or 3D time series. In case of 3D time series, image properties should be appropriately set. If you are not sure, check your image header by \[Image → Properties\].

-   Simple Ratio Method:
    -   Plugin version of [Jens Rietdorf's macro](https://www.embl.de/eamnet/html/bleach_correction.html), extended further with 3D time series
-   Exponential Fitting Method:
    -   Similar to the [description on the T-functions page](/imaging/t-functions#correcting-for-bleaching). Additionally, this plugin also works with 3D time series.
    -   [MBF ImageJ](/software/mbf-imagej) suggests to use "Exponential" equation for fitting, whereas this plugin uses "Exponential with Offset"
-   Histogram Matching Method:
    -   A brand-new method for bleach correction.
    -   This algorithm first samples the histogram of initial frame, and for the successive frames, {% include wikipedia title='Histogram matching' text='histograms are matched'%} to the first frame. This avoids the increase in noise in the latter part of the sequence which is a problem in the above two methods.
    -   This method does much better restoration of bleaching sequence for segmentation but not appropriate for intensity quantification.
    -   See the blog entry, [a bit more detail on this issue](https://wiki.cmci.info/blogtng/2010-05-04/photobleaching_correction_3d_time_series)

## Video Tutorial

See here: [Youtube](https://youtu.be/xA20w-uZO8A)


