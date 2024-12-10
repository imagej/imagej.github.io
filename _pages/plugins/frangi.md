---
title: Frangi
project: /software/imagej2
artifact: net.imagej:imagej-ops
icon: /media/icons/imagej2.png
doi: 10.1007/BFb0056195
categories: [Uncategorized]
---

_Frangi vesselness_ is an algorithm for detection of tube-like structures (such as in imagery of filamentous structures (blood vessels, neurites, etc.). It applies to both 2D and 3D images and was first described by Frangi et al 1998.[^1] ([PDF](https://link.springer.com/content/pdf/10.1007%252FBFb0056195.pdf)). In many cases, this method is known to be a better alternative to single-scale [Tubeness](/plugins/tubeness) filtering (at least for isotropic images), but it is slower. There are two ImageJ implementations of the algorithm:

- A legacy plugin (In Fiji registered under {% include bc path='Process|Filters|Frangi Vesselness' %} ([source code](https://github.com/fiji/Feature_Detection)). This is a deprecated implementaton with expected inaccuracies.

- An [ImageJ Op](/libs/imagej-ops/index)  (In Fiji registed under {% include bc path='Plugins|Process|Frangi Vesselness' %}). This version superseeds previous implementations and has been validated/benchmarked againgst other implementations (namely ITK and MATLAB) ([details](https://forum.image.sc/t/frangi-vesselness-filter-feedback/6747)). It requires 3 inputs:
 
  1. Scale(s): Radii of the structures to be filtered
  2. Spacing: the physical spacing between image data points (i.e., the pixel/voxel dimensions)
  3. Whether or not a gaussian filter should be applied at each scale before the filter runs

SNT's uses this filter internally. Its [Secondary Layer Wizard](/plugins/snt/manual#tracing-on-secondary-image) provides a convenient way to preview the effect of scale size in the result.

{% include img align="center" width="600px" src="/media/plugins/frangi-before-and-after.png" caption="Frangi Vesselness: Left: Original image. Right: Filtered image." %}



{% include citation fn=1 %}
