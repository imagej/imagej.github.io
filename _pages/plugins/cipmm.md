---
title: CIPMM plugins
categories: [Uncategorized]
---

Welcome!

This is the official plugin repository of hte department of molecular physiology at the Center for Integrative Physiology and Molecular Medicine (CIPMM) at Saarland University.

Currently, this repository contains a plugin called 'LRoi', which helps you creating sets of equally sized ROIs.

## Installation

You can install LRoi (and all future plugins) by simply adding the following update site to the ImageJ updater:

{% include link-banner url="https://sites.imagej.net/CIPMM-MolPhys/" %}

## Usage

The main purpose of LRoi is to create equally sized regions of interest (ROIs) along a seeding line (hence LRoi). To create a number of ROIs, simply select the line drawing tool of ImageJ and draw a line on an opened image or image stack.

![](/media/linetool.png) ![](/media/plugins/seedingline.png)

Open the LRoi plugin and specify the number of ROIs you want to create, the ROI width and height.

![](/media/plugins/lroi-example.png) ![](/media/plugins/lroi-length.png)

The ROI height is used to adjust the length of your seed line w.r.t. its center point. This can be used as an drawing aid, since it might sometimes be difficult to draw a line with a speciffic length by hand. LRoi ensures, that your seeding line will have the exact length you specified.

This line is then subdivided into the number of ROIs you want to create with your specified width. In our example, we create 25 ROIs along a 350µm seeding line, each having a width of 50 µm. This will result in iach ROI having an area of 14µm x 50 µm = 700 µm.

![](/media/plugins/rois-example.png)

In this example, we have created 25 ROIs, each having an area of 700 µm².

## Advanced usage

Besides creating equally sized ROIs along a seeding line, LRoi also allows to create ROIs perpendicular to that line, cross-shaped, as a regular grid or custom sized grid.

These advanced ROI creation schemes can be activated by simply clicking the respective checkbox in the LRoi window. Regular ROI grids are defined by the number of pixels they should include (If you define a grid size of 8, each grid cell will be 8 by 8 pixels large).

Custom ROI grids on the other hand ar defined by specifying the number of columns and rows of the desired ROI grid.
