---
mediawiki: Mixture_Modeling_Thresholding
name: "Mixture Modeling"
title: Mixture Modeling Thresholding
categories: [Segmentation]
initial-release-date: "15 December 2003"
website: "https://imagej.nih.gov/ij/plugins/mixture-modeling.html"
dev-status: "unknown"
team-founders: [Christopher Mei, Maxime Dauphin]
---

{% include info-box filename=' [Mixture\_Modeling.jar](https://imagej.nih.gov/ij/plugins/download/jars/Mixture_Modeling.jar) (18,454 Bytes)' source='in .jar file' %}

## Purpose

This plugin automatically threshold an image using the Mixture Modeling algorithm. It is an histogram-based technique that assumes that the histogram distribution is represented by two Gaussian curves.

## Documentation

This algorithm separates the histogram of an image into two classes using a Gaussian model. It then calculates the image threshold as the intersection of these two Gaussians. This thresholding technique has the advantage of finding a threshold that is in certain cases closer to real world data. The Gaussian parameters can also be used to describe the two regions obtained.

The plugin returns a histogram with the two Gaussians, the parameters obtained (average, standard deviation, threshold) and the thresholded image.

It has the same drawbacks as the [Otsu Thresholding](Otsu_Thresholding) plugin (by the same author), which is that it behaves annoyingly with stacks.

 
