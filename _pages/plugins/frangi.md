---
mediawiki: Frangi
title: Frangi
artifact: sc.fiji:Feature_Detection
doi: 10.1007/BFb0056195
categories: []
---

{% include notice icon="warning" content="This is an experimental plugin, and I have doubts about its correctness—in particular, the results are strange when the ratio of pixelWidth : pixelHeight : pixelDepth is other than 1:1:1. In addition, the results in any case seem to be different from those from other implementations, such as [this [MATLAB](/scripting/matlab) one](http://www.mathworks.co.uk/matlabcentral/fileexchange/24409-hessian-based-frangi-vesselness-filter). I don't have time to work on this any more (and no longer work in academia at all) so if someone were interested in taking it over, that would be brilliant."  %} This plugin implements the algorithm for detection of vessel- or tube-like structures in 2D and 3D images described Frangi et al 1998.[^1]

In my experience, this method produces consistently better results than the [Tubeness](/plugins/tubeness) plugin for isotropic image data, although it is significantly slower.

These screenshots show the results on an example file:

![](/media/plugins/frangi-before-and-after.png)

{% include citation fn=1 %}
