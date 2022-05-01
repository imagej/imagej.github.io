---
mediawiki: Graph_Cut
title: Graph Cut
project: /software/fiji
categories: [Segmentation,Tutorials]
artifact: sc.fiji:Graph_Cut
---

 <img src="/media/plugins/mito-sample.png" width="350"/>

The Graph Cut plugin provides a way to obtain a globally smooth binary segmentation. As input, you have to provide a gray-scale image that represents the pixel affinities for belonging to the foreground. Via a single parameter you can adjust the smoothness of the segmentation.

## Publication

This plugin is based on a reimplementation of Kolmogorov's [maxflow v3.01](http://pub.ist.ac.at/~vnk/software.html#maxflow) library, which was written in C++. If you intend to use it for a publication, please cite:

Yuri Boykov and Vladimir Kolmogorov, <b>An Experimental Comparison of Min-Cut/Max-Flow Algorithms for Energy Minimization in Computer Vision.</b>, In IEEE Transactions on Pattern Analysis and Machine Intelligence, September 2004.

The plugin can be found under {% include bc path='Plugins|Segmentation|Graph Cut'%}.

## Settings

The only available setting so far is the "smoothness" value. Use it to adjust the penalty for label changes in the segmentation. The higher this value, the less label changes you will have, thus the segmentation gets smoother. A value of zero corresponds to thresholding the input image.

## Tutorial

Assume we want to segment the following image into foreground/background, such that the foreground is the mitochondria and the background everything else:

<img src="/media/mito.png" width="200"/>

### Probability Image

First, we create a probability image that reflects the per-pixel probability of belonging to the foreground. For that, we can use the [Trainable Weka Segmentation](/plugins/tws) plugin. We train a classifier for the mitochondria and everything else. Instead of using the classifier directly for the segmentation, however, we create a probability image:

<img src="/media/plugins/mito-prob.png" width="200"/>

### Running Graph Cut

Now we start the Graph Cut plugin on the probability image. With the "smoothness" slider we can adjust the smoothness of the segmentation to avoid some small extrema to corrupt our segmentation. In our example, we found that a value of about 600 gives reasonable results. The outcome of the plugin is a binary image, with white being the foreground segmentation:

<img src="/media/plugins/mito-seg.png" width="200"/>

### Result

Finally, we merge the original image and the segmentation for illustration purposes:

{% include img src="mito-comp" width="100" %}
