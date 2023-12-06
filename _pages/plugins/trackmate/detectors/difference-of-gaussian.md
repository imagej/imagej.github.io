---
title: TrackMate DoG detector
description: The TrackMate Difference of Gaussian detector
categories: [Segmentation,Tracking]
extensions: ["mathjax"]
artifact: sc.fiji:TrackMate
doi: 10.1101/2021.09.03.458852
---

The Difference of Gaussian (DoG) detector is a TrackMate detector that works best when detecting  roundish objects, bright against a dark background. 
It is very close to the  [Laplacian of Gaussian (LoG)](laplacian-of-gaussian) detector.
The spots it outputs are shapeless: they just have X,Y,Z coordinates and radius.
It works in 2D and 3D.

## Principle.

This detector is based on the Difference of Gaussian (DoG) filter.
It approximates the [Laplacian of Gaussian (LoG)](laplacian-of-gaussian) filter with the aim at offering better speed.
It is commonly used when applying a collection of DoG filters tuned to a wide range of scales (see[^1]).
In TrackMate, the detector based on DoG only uses one scale, but there are still use-cases where the DoG can be faster than the LoG (see below for performance comparison).

Given d an approximate expected particle diameter, determined upon inspection, two gaussian filters are produced with standard deviation σ₁ and σ₂:

-   σ₁ = 1 / (1 + √2 ) × d
-   σ₂ = √2 × σ₁

The image is filtered using these two gaussians, and the result of the second filter (largest sigma) is subtracted from the result of the first filter (smallest sigma). 
This yields a smoothed image with sharp local maximas at particle locations. A detection spot is then created for each of these maximas, and an arbitrary quality feature is assigned to the new spot by taking the smoothed image value at the maximum. 
If two spots are found to be closer than the expected radius d/2, the one with the lowest quality is discarded.

To improve the localization accuracy, and extra step is taken to yield a sub-pixel localization of the spots.
The position of each spot is recalculated using a simple parabolic interpolation scheme, as in [^1]. 
The quality feature is also interpolated using this scheme.

A large number of spurious spots are created by finding local maximas. 
There spurious spots are discarded inn extra step, by applying a threshold on the quality feature computed during segmentation. 
The value of this threshold is set manually, to match the SNR of the input image. Thresholded spots are then retained for subsequent particle-linking.

## Performance.

This [page](performance) compares the performance of the LoG detector and the DoG detector and give hints at how to choose between the two.

## Code.

The TrackMate implementation is based on ImgLib2[^2].
The code can be found [on GitHub](https://github.com/trackmate-sc/TrackMate/blob/-/src/main/java/fiji/plugin/trackmate/detection/DogDetector.java).

## References

{% include citation fn=1 doi="10.1023/B:VISI.0000029664.99615.94" %}

{% include citation fn=2 doi="10.1093/bioinformatics/bts543" %}
