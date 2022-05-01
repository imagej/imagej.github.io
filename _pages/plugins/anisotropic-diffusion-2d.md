---
mediawiki: Anisotropic_Diffusion_2D
title: Anisotropic Diffusion 2D
project: /software/fiji
categories: [Filtering]
artifact: sc.fiji:Anisotropic_Diffusion_2D
doi: 10.1109/TPAMI.2005.87
extensions: ["mathjax"]
---

This plugin implement the anisotropic diffusion filter in 2D. Anisotropic filters are a class of filter that reduces noise in an image while trying to preserve sharp edges. See also [this page of the ImageJ 1.x website](https://imagej.nih.gov/ij/plugins/anisotropic-diffusion-2d.html).

## Documentation

**Parameters:**

-   *Number of iterations* - Maximum number of complete iterations, default value is 20.
-   *Smoothings per iteration* - Number of smoothings by anisotropic Gaussian with 3x3 mask per iterations, default value is 1. Size of the smoothing per one complete iteration is proportional to the square root of this number.
-   *Keep each* - Number of iterations between successive savings of the results. Default value is 20.
-   *a1 (Diffusion limiter along minimal variations)* - a1 influences the shape of the smoothing mask. f1(l1,l2)= (1.0+l1+l2)^-a1. The smoothing in each iteration is defined by a tensor (2x2 matrix), that is linear combination of tensors corresponding to minimal and maximal eigenvalue of structure tensor. f1 and f2 are weights of the tensors (see Tschumperlé and Deriche, 2005).
-   *a2 (Diffusion limiter along maximal variations)* - a2 influences the shape of the smoothing mask. $$ f_2(l_1,l_2) = (1.0+l_1+l_2)^{-a_2} $$.
-   *dt (Time step)* - Default value is 20. The result of the filter is proportional to the step, but too long time step yields numerical instability of the procedure.
-   *Edge threshold height* - Defines minimum "strength" of edges that will be preserved by the filter. Default value is 5.
-   *Show filter stats* - Display filter statistics for each iteration.
-   *Show time stats* - Display elapsed times.
-   *Add labels* - Add labels to output stack. Double click on the eye dropper tool to set the label color.

## Citation

The algorithm used by this plugin is an implementation of Anisotropic Diffusion from:

{% include citation %}
