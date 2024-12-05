---
title: Labkit - Intuitive Pixel Classification in Fiji

artifact: sc.fiji:labkit-ui
categories: [Classification, Machine Learning]
doi: 10.3389/fcomp.2022.777728
---

## Abstract

<!--<img src="/media/plugins/labkit-illustration.jpg" width="700"/>-->

Labkit is a user-friendly Fiji plugin for the segmentation of microscopy image data.  It offers easy to use manual and automated image segmentation routines that can be rapidly applied to single- and multi-channel images as well as timelapse movies in 2D or 3D. Labkit is specifically designed to work efficiently on big image data and users of consumer laptops can conveniently work with multiple terabytes large image data. This efficiency is achieved by using Imglib2 and BigDataViewer as the foundation of our software. Furthermore, memory efficient and fast random forest based pixel classification based on the Waikato Environment for Knowledge Analysis (WEKA) is implemented, optionally exploiting the power of graphics processing units (GPUs) to gain additional performance and can even be used on high performance computing clusters (HPC) for distributed processing of big image data. Finally, manual tools for ground-truth annotation are available. 

## What It Looks Like

<img src="https://user-images.githubusercontent.com/24407711/133519201-67d6e29f-f024-4803-8eee-75831a996952.gif" style="width: 712px; height: 490px"/>

## Installation

Labkit is bundled with Fiji. All you need to do is [install Fiji](https://imagej.net/software/fiji/downloads). You will find Labkit in the main menu under `Plugins > Labkit`.

## Tutorials

- [Automatic segmentation (Quick start tutorial)](/plugins/labkit/pixel-classification-tutorial)
- [Manual segmentation (Quick start tutorial)](/plugins/labkit/manual-segmentation-tutorial)
- [Curation of segmentation results](/plugins/labkit/curation-tutorial)
- [How to improve automatic segmentation results?](/plugins/labkit/guidelines)
- [GPU acceleration](/plugins/labkit/gpu-acceleration-tutorial)
- [Using Labkit in ImageJ Macro](/plugins/labkit/batch-processing)
- [How to run Labkit on an HPC cluster to process huge data?](/plugins/labkit/hpc-cluster)

## Documentation

- [UI features & short cuts](/plugins/labkit/documentation)
- [FAQ](/plugins/labkit/faq)
- [Pixel classification algorithm description](/plugins/labkit/pixel-classification-algorithm)

## How to cite

If you find Labkit useful for your research, please cite it:

* {% include citation %}
