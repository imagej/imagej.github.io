---
mediawiki: RATS:_Robust_Automatic_Threshold_Selection
title: "RATS: Robust Automatic Threshold Selection"
project: /software/fiji
categories: [Segmentation,Tutorials]
artifact: sc.fiji:RATS_
---

Robust Automatic Threshold Selection (RATS) computes a threshold map for a 2d image based upon the value of pixels and their gradients.

## Background

The RATS algorithm is applied across regions of the image making it suitable for thresholding noisy images with variable background. The plugin is based upon the description in

-   Wilkinson MHF (1998) *Segmentation techniques in image analysis of microbes*. Chapter 6 in: Wilkinson MHF, Schut F (eds.) **Digital Image Analysis of Microbes: Imaging, Morphometry, Fluorometry and Motility Techniques and Applications**, Vol. John Wiley & Sons, New York.

In this implementation the input gradient of the input image is computed using the Sobel kernels. Traditionally the Sobel gradient is computed using

![](/media/plugins/rats-sobel.png)

The kernel operators are detailed in many sources including {% include wikipedia title='Sobel operator' text='here'%}. However, Wilkinson shows that eliminating the square root yields suitable results with out the added cost of a final scan across the image to compute the root. In the plugin the gradient is left simply as the sum of the squares of the kernel operations.

![](/media/plugins/rats-sobel2.png)

Pixels with gradients that fall below a user specified threshold, ![](/media/plugins/rats-lambdasigma.png) , are rejected. The threshold is defined by an estimate of the noise (![](/media/plugins/rats-sigma.png) ,the standard deviation of the expected background is a good starting point) and a scaling factor (![](/media/plugins/rats-lambda.png), 3 is a good starting point). Estimate the noise by selecting a "background" portion of the image and using ImageJ to determine the standard deviation of gray values.

The input image is then subdivided into a quadtree architecture (for more info see {% include wikipedia title='Quadtree' text='Wikipedia:Quadtree'%}). Within each of the smallest subregions, a regional threshold, ![](/media/plugins/rats-tr.png) , is computed as the gradient weighted sum of the pixels, P.

![](/media/plugins/rats-tr2.png)

Occasionally, the regional threshold fails if the sum of the weights (the denominator) falls to the level of background containing only noise. In such cases, the regional threshold is replaced by the threshold of its parent quadtree (if the parent's threshold doesn't fail). It is possible that thresholds fail all the way up the quadtree heirarchy, in which case a same threshold is applied to all regions which is identical to applying a global threshold. In our experience, regional threshold failures are rare. Once the regional thresholds are computed, they are interpolated (bilinear interpolation) across the entire image yielding a threshold map.

The user also controls the size of the smallest quadtree region (aka leaflet). As with the noise estimate and scaling factor, determining the appropriate minimum quadtree leaflet size is best done with experiment. However, a good guide is to match the size of the smallest leaflet to something just larger than the size of the smallest object expected. There is little performance loss by decreasing the size of the smallest leaflet.

## Plugin Usage

![](/media/plugins/rats-gui.jpg)

Load an single channel image (8-bit, 16-bit or 32-bit). Note that the plugin expects bright objects on dark background, so you might want to call {% include bc path='Edit | Invert'%} if your input image has dark objects. Select the RATS plugin from the Plugins menu. The following dialog will appear:

1\. NOISE THRESHOLD: An estimate of the noise. Estimate the noise by selecting a "background" portion of the image and using ImageJ to determine the standard deviation of gray values. Oddly, lower values yield smaller particles in general. (see reference, defaults to 25).

2\. LAMBDA FACTOR: A scaling factor. Higher values yield larger particles. (see reference, defaults to 3)

3\. MIN LEAF SIZE (pixels): The smallest allowed leaflet (defaults to attempts to create up to 5 levels of quadtrees that fit in the input image dimensions)

4\. VERBOSE If set then output informational messages in the log window (default is false).

That's it! A bilevel image is produced with the name "-mask" appended to the original image name.

![](/media/plugins/rats-output.png)

## Macro Usage

The plugin is recordable and can be called from a macro ....

```java
run("RATS ", "noise=25 lambda=3 min=81 verbose")
```
