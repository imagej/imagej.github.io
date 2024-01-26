---
title: Ops Deconvolution
extensions: ["mathjax"]
project: /software/imagej2
---

## Overview

[ImageJ Ops](/libs/imagej-ops) is an extensible framework for algorithms. [Deconvolution](/imaging/deconvolution) is a process that is used to de-blur images. When implemented with appropriate constraints deconvolution can also de-noise images. The imagej-ops project gives algorithm developers a framework to implement, organize and test various approaches to deconvolution.

Current work is focused on:

1. Implementation of Richardson Lucy with Total Variation Regularization, Vector Acceleration and Non-Circulant Edge handling.

2. Designing a framework that will make it easy for developers to extend Richardson Lucy with other types of regularization, acceleration and edge handling.

3. Designing a framework that will make it easy for developers to implement other types of deconvolution.

## Richardson Lucy

{% include wikipedia title='Richardson%E2%80%93Lucy deconvolution' text='Richardson Lucy'%} is an iterative deconvolution algorithm that can be used to reconstruct a blurred image.

$$\mathbf{o}_{k+1}(s)=\left\{\left[\frac{i(s)}{(o_{k}*h)(s)}\right]*h(-s)\right\}{o}_{k}(s)$$


In practice the Richardson-Lucy algorithm needs to be modified to improve noise handling (regularization), improve convergence speed (acceleration) and reduce edge artifacts.

### Richardson Lucy with Total Variation Regularization

To prevent noise amplification the Richardson Lucy algorithm should be regularized. {% include wikipedia title="Regularization (mathematics)" %} "refers to a process of introducing additional information in order to solve an ill-posed problem or to prevent overfitting".

[Richardson Lucy with Total Variation Regularization](http://www.ncbi.nlm.nih.gov/pubmed/16586486)

{% raw %}$$\mathbf{o}_{k+1}(s) = \left\{\left[\frac{i(s)}{(o_{k}*h)(s)}\right]*h(-s)\right\}\frac{{o}_{k}(s)}{1-\lambda_{TV}div\left({\frac{\nabla_{ok}(s)}{|\nabla_{ok}(s)|}}\right)}$${% endraw %}

### Richardson Lucy with Vector Acceleration

Richardson Lucy and other iterative algorithms are often slow to converge. Acceleration techniques speed up convergence by taking a larger step at each iteration.

[Acceleration of Iterative Algorithms](http://www.ncbi.nlm.nih.gov/pubmed/18250863)

[Richardson Lucy with TV Regularization and Vector Acceleration](http://ceur-ws.org/Vol-446/p400.pdf)

### Edge handling with Non-circulant Richardson Lucy

The proper handling of boundary conditions is an important part of deconvolution. Images are finite and usually treated as circulant. Thus when deconvolving (or convolving) images are usually extended (padded) to prevent boundary artifacts. A novel approach, to handle edge artifacts, was introduced as part of the 2014 international grand challenge on deconvolution. This approach uses non-circulant convolution operators.

[Non-circulant Richardson Lucy](http://bigwww.epfl.ch/deconvolution/challenge2013/index.html?p=doc_math_rl)

## Scripts

A collection of scripts that use ops-deconvolution is being developed and can be found [here on github](https://github.com/imagej/imagej-scripting/tree/-/src/main/resources/script_templates/Deconvolution). The scripts can also be accessed via the {% include bc path="Templates|Deconvolution" %} menu in the Fiji script editor. Note that as new scripts are added it may take a couple of weeks for them to be available in Fiji. Thus check github for the most up to date collection of scripts.

## Preliminary Results

Preliminary results have been generated using the [C. Elegans Embryo](http://bigwww.epfl.ch/deconvolution/bio/) images and PSFs provided by the Bio-Imaging Group of EPFL. Note that this result is not yet optimal, as the image has spherical aberration (asymmetrical 'flare' in the xz view) and the provided PSF did not have SA. In the future better ops to produce a theoretical PSF with spherical aberration will be developed.

We encourage users of deconvolution to try deconvolving this image with various commercial and open source packages and discuss results on the [ImageJ Forum](http://forum.imagej.net/).

### Original

{% include img src="composite-orig-xy.jpg" width="300" %} {% include img src="composite-orig-zx.jpg" width="140" %}

### Deconvolved

{% include img src="composite-decon-xy.jpg" width="300" %} {% include img src="composite-decon-zx.jpg" width="140" %}

## References

- {% include citation id="libs/imglib2" %}

- {% include citation doi="10.1017/S143192761300576X " %}

- {% include citation doi="10.1002/jemt.20294" %}

- {% include citation doi="10.1111/j.1365-2818.2011.03486.x" %}

- {% include citation doi="10.1016/0167-2789(92)90242-F" %}

- C. Vonesch (2013), *Second International Challenge on 3D Deconvolution Microscopy*, http://bigwww.epfl.ch/deconvolution/challenge.

- {% include citation doi="10.1364/AO.36.001766" %}

- {% include citation doi="10.1007/978-3-540-93860-6_81" %}
