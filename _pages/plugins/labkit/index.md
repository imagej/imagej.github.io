---
mediawiki: Labkit
title: Labkit

artifact: net.imglib2:imglib2-labkit
categories: [Uncategorized]
---

<img src="/media/plugins/labkit-illustration.jpg" width="700"/>

Labkit is a user-friendly Fiji plugin for the segmentation of microscopy image data.  It offers easy to use manual and automated image segmentation routines that can be rapidly applied to single- and multi-channel images as well as timelapse movies in 2D or 3D. Labkit is specifically designed to work efficiently on big image data and users of consumer laptops can conveniently work with multiple terabytes large image data. This efficiency is achieved by using Imglib2 and BigDataViewer as the foundation of our software. Furthermore, memory efficient and fast random forest based pixel classification based on the Waikato Environment for Knowledge Analysis (WEKA) is implemented, optionally exploiting the power of graphics processing units (GPUs) to gain additional performance and can even be used on high performance computing clusters (HPC) for distributed processing of big image data. Finally, manual tools for ground-truth annotation are available. 

<!---

## Publication

If you find Labkit useful for your research, please cite it:
-->

## Installation

1. Install [Fiji](https://imagej.net/software/fiji/downloads)
2. Install Labkit's [update site](/update-sites/following):
   1. Start Fiji
   2. From the menu, select {% include bc path="Help | Update" %}
   3. Click on `Manage Update Sites`, then select `Labkit` in the table
   4. Close, click on `Apply changes` and then `Ok`
   5. Restart Fiji
3. Find Labkit in the plugin menu of Fiji, under "Labkit".

## Tutorials

- [Automatic segmentaiton (Quick start tutorial)](pixel-classification-tutorial)
- [Manual segmentation (Quick start tutorial)](manual-segmentation-tutorial)
- [Curation of segmentation results](curation-tutorial)
- [What's the best way to annotation image for pixel classification?](scribble-guideline)
- [Improve results or performance by customizing the feature settings.](feature-settings-guideline)
- [GPU accelleration](gpu-accelleration-tutorial)
- [Using Labkit in ImageJ Macro](batch-processing)
- [How to run Labkit on an HPC cluster to precess huge data](hpc-cluster)

## Documentation

- [UI features & short cuts](documentation)
- [FAQ](faq)
- [Pixel classification algorithm description](pixel-classification-algorithm)


