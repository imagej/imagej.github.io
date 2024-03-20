---
mediawiki: Nscale_segmentation
name: "Nscale_segmentation"
title: Nscale_segmentation
categories: [Segmentation]
website: "https://sites.imagej.net/Nscale_segmentation/"
dev-status: "stable"
Author: ['@Eden Tamrat']
---

The watershed algorithm and the segmentation tools within the Fiji software often dont distinguish a cluster of nuclei that are in close proximity, erroneously grouping them together. This leads to an inaccurate analysis of average nuclear size. To address this issue, this customizable segmentation plugin employs a scale parameter to calibrate the image, to give a more precise separation of touching nuclei.

## Instalation

To instal the plugin onto Fiji first copy the script from the update site (https://sites.imagej.net/Nscale_segmentation/) and save it as 
a txt. (Open notebook, paste script onto notebook and save it). To run it go to plugins>macros>install> and click on the Nscale_segmentation script you just saved. The plugin should show up like this: 


{% include img src="nscale-segmentation-1.jpg" %}

## Start

Once you have the plugin installed open the image you want to analyse. Right click the plugin icon and a pop up should appear 
asking to input a scale factor number. This number should range from 1-10. Start with a lower scale number and click ok. 

{% include img src="nscale-segmentation-2.jpg" %}

Click the icon again to set your desired Gaussian Blur radius.

{% include img src="nscale-segmentation-3.jpg" %}

And set the radius and threshold for the removal of outliers. 

{% include img src="nscale-segmentation-4.jpg" %}

Once you set all the parameters and click ok, this should segment all the cellular nuclei in your image. If the segmentation is too big or small for your cells, right click the plugin icon again and adjust the scale factor (increase/decrease accordingly) before making changes to outlier radius. 

## Demo

This tool should segment touching or merged nuclei from separate cells.  

{% include img src="nscale-segmentation-5.jpg" %}
