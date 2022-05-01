---
mediawiki: Edge_and_symmetry_filter
title: Edge and symmetry filter
categories: [Uncategorized]
---

## Edge and Symmetry filter

3D Canny-Deriche edge detection filter and symmetry filter.

## Author

Thomas Boudier

## Description

This plugin will compute the gradients of the image based on the {% include wikipedia title="Canny edge detector" %}. The symmetry filter will vote for the voxels inside the object based on the gradient vector direction.

**Alpha parameter** refers to the smoothing in canny edge detection, the smaller the value, the smoother the edges.

![](/media/plugins/edgeandsymmetry.png)

The **radius** parameter refer to the radius of the object whose symmetry is to be detected. Normalization and scaling refer to internal values of the algorithm, see Gertych *et al.* for references. The smoothed version is smoothed using ImageJ 3D Gaussian filter with a radius 2.

The **improved seed detection** refer to a modified implementation to better detect seeds inside objects rather than objects themselves.

![](/media/plugins/edgesymmetry.png)

The gradient vector is perpendicular to the edges, voxels along the direction of the gradient are highlighted and *vote* for the symmetry.

## Download

For details go to the [3D ImageJ Suite](/plugins/3d-imagej-suite).

## Citation

When using the plugin for publication, please refer to :

J. Ollion, J. Cochennec, F. Loll, C. Escudé, T. Boudier. (**2013**) TANGO: A Generic Tool for High-throughput 3D Image Analysis for Studying Nuclear Organization. *Bioinformatics* 2013 Jul 15;29(14):1840-1. [(doi)](http://dx.doi.org/10.1093/bioinformatics/btt276)

A. Gertych *et al.*, **Computers in Biology and Medecine**, 2015 ([doi](http://dx.doi.org/10.1016/j.compbiomed.2015.04.025))

## License

GPL distribution (see [licence](http://www.cecill.info/index.en.html)). Sources are available freely.
