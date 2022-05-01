---
mediawiki: MyofibrilJ
title: MyofibrilJ
categories: [Scripting,Analysis]
---

<seo metak="Fourier analysis, autocorrelation" metad="Fourier analysis, autocorrelation" /> 
{% capture maintainer%}
{% include person id='giocard' %}
{% endcapture %}

{% capture author%}
{% include person id='giocard' %} and Maria Spletter
{% endcapture %}

{% capture source%}
{% include github org='giocard' repo='MyofibrilJ' %}
{% endcapture %}
{% include info-box software='ImageJ/Fiji' name='MyofribilJ' maintainer=maintainer author=author source=source released='November 2017' category='Analysis, Scripting, Plugins' %}

## Introduction

The MyofibrilJ plugin provides two scripts to analyse fibril morphology. Given a fluorescence image of muscle fibers, the scripts measure myofibrils dimensions and sarcomere length. The scripts were initially developed for the analysis of both longitudinal and cross sections of myofibrils stained with rhodamine-phalloidin.

## Usage

Two distinct commands, *analyse myofibrils crosswise* and *analyse myofibrils lengthwise*, are provided to analyse cross-sections and longitudinal sections of fibers, respectively. In both cases:

-   open one or more images to analyse, all of them displaying either only longitudinal or only cross sections of fibrils
-   for each multi-channel or stack image, display the slice and the channel of interest. Optionally, draw a ROI to focus on a portion of the image (recommended to exclude empty regions)
-   launch the script specific for the images displayed

The script will process all the images and generate a table with results, along with some control images

**Note**: when analysing longitudinal sections, fibrils need to be aligned horizontally. If they are not displayed horizontally, rotate the images before the analysis.

## Details

### Longitudinal sections

The sarcomere length is estimated by means of Fourier analysis. Because of the periodic nature of sarcomere organization, the position of the periodic peaks on the horizontal axis of the Fourier transformed imaged is strictly related to the length of sarcomeres. The thickness of the fibrils is estimated in two different manners. One estimate is obtained from the autocorrelation image, by measuring the position of the first minimum in its vertical intensity profile. Furthermore, the width of the cross-profile of multiple fibrils is measured in the original image and combined to provide an additional average width.

### Cross sections

An initial estimate of the diameter of the fibrils is obtained by finding the first minimum in the radial average profile of the autocorrelation image, while their position is determined by examining the peak intensities. This estimate is used to determine the optimal crop area around all the cross-sections in the image. All of the detected fibrils cross sections are then cropped from the image, the size of the crop being proportional to the the initial diameter estimate, and combined to obtain a noise-free average representation of the fibril section. The diameter is estimated from this average as the full width of its radial profile, where the intensity is 26% of the maximum range. In addition to their diameter, the level of clustering of the fibrils is characterized by nearest neighbor analysis and summarized by the Nearest Neighbor Index (NNI).

## References

## Installation

The easiest way to install *MyofibrilJ* is by [adding](/update-sites/following#add-update-sites) its update site. Specifically:

-   launch Fiji and go to the menu {% include bc path="Help|Update..." %}
-   once the dialog window *ImageJ Updater* is opened, click on the *Manage update sites* button
-   click on the *Add update site* button in the site management dialog, and a new, empty line will appear at the end of the list
-   in the column *Name*, fill in a name of your choice, e.g. Myofibril
-   in the column *URL*, type http://sites.imagej.net/MyofibrilJ/
-   mark the check button at the beginning of the line, in order to subscribe
-   click on the *Close* button and then on *Apply changes*
-   after the update process is completed, close Fji and reopen it. From the main menu you can now select *MyofibrilJ* and launch one of the scripts available.

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [Free Software Foundation](http://www.gnu.org/licenses/gpl.txt). This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  
