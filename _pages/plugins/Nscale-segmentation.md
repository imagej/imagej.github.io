---
mediawiki: Nscale_segmentaion
name: "Nscale_segmentaion"
title: Nscale_segmentaion
categories: [Segmentation]
website: "https://sites.imagej.net/Nscale_segmentaion/"
dev-status: "stable"
Author: ['@Eden Tamrat']
---

The watershed algorithm and the segmentation tools within the Fiji software often dont distinguish a cluster of nuclei that are in close proximity, erroneously grouping them together. This leads to an inaccurate analysis of average nuclear size. To address this issue, this customizable segmentation plugin employs a scale parameter to calibrate the image, to give a more precise separation of touching nuclei.

## Instalation

To instal the plugin onto Fiji first copy the script from the update site (https://sites.imagej.net/Nscale_segmentaion/) and save it as 
a txt. (Open notebook, paste script onto notebook and save it). To run it go to plugins>macros>install> and click on the Nscale_segmentaion script you just saved. The plugin should show up like this: 

![image](https://github.com/EdenTamrat/imagej.github.io/assets/149198009/f5814cf6-2358-41ec-9cbb-1c3547055c9d)


## Start

Once you have the plugin installed open the image you want to analyse. Right click the plugin icon and a pop up should appear 
asking to input a scale factor number. This number should range from 1-10. Start with a lower scale number and click ok. 

![image](https://github.com/EdenTamrat/imagej.github.io/assets/149198009/0e2961b8-b846-442d-9d5c-92c88c9f9264)

Click the icon again to set your desired Gaussian Blur radius.

![image](https://github.com/EdenTamrat/imagej.github.io/assets/149198009/5a66437c-7476-4dc8-a2b5-f1eced62a911)

And set the radius and threshold for the removal of outliers. 

![image](https://github.com/EdenTamrat/imagej.github.io/assets/149198009/44d41ab2-0aca-48c8-b3bf-c3496e0a3d45)


Once you set all the parameters and click ok, this should segment all the cellular nuclei in your image. If the segmentation is too big or small for your cells, right click the plugin icon again and adjust the scale factor (increase/decrease accordingly) before making changes to outlier radius. 

## Demo

This tool should segment touching or merged nuclei from separate cells.  


![image](https://github.com/EdenTamrat/imagej.github.io/assets/149198009/969fcf8d-b06a-4536-a64a-9c82c5b50dcc)


```
