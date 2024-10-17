---
mediawiki: Biomat
name: "Biomat"
title: Biomat
categories: [Filtering]
release-date: "10/17/2024"
initial-release-date: "03/26/2019"
team-founder: 'Jiří Janáček'
team-maintainer: 'Jiří Janáček | mailto:jiri.janacek_at_fgu.cas.cz'
source-url: https://github.com/jiri-janacek/biomat
---


## Plugins for 3D image preprocessing

**Stack Linear Contrast** - multiplies images in stack by coefficient obtained by linear interpolation of the "first" and "last" coefficient. A simple tool for compensation of contrast decreasing with depth within thick sample.

**Lipschitz 3D** Filter - top hat - subtracts slowly varying background calculated as lower Lipschitz envelope from the image.

 {% include img align="right" name="brain" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/capillaries_brain_3Dg.gif" %}
 
 {% include img align="right" name="brain proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/capillaries_brain_proc_3Dg.gif" %}

Preprocessing example: [Stack of confocal microscopy images of capillaries in rat brain](/media/plugins/capillaries-brain.zip)

-   {% include bc path='Plugins | Biomat | Stack Linear Contrast'%} with "first" = 1.0 and "last" = 3.0
-   {% include bc path='Process | Filters | Gaussian blur 3D'%} with "sigma" = 1 pixel
-   {% include bc path='Plugins | Biomat | Lipschitz 3D Filter'%} with "slope" = 2 and "top hat" on

## Plugins for detection of fibres in 3D image

**Tensor Line 3D Filter** - enhances white fibers of uniform width sparsely distributed on dark background.

{% include img align="right" name="adipose" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/capillaries_adipose_3Dg.gif" %}

{% include img align="right" name="adipose proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/capillaries_adipose_proc_3Dg.gif" %}

Example: [Stack of confocal microscopy images of capillaries in adipose tissue](/media/plugins/capillaries-adipose.zip).

-   {% include bc path='Plugins | Biomat | Tensor Line 3D Filter'%} with "sigma" = 3 pixels
-   {% include bc path='Image | Adjust | Brightness/Contrast'%}
-   {% include bc path='Process | Filters | Gaussian blur 3D'%} with "sigma" = 1 pixel

**Vector Line 3D Filter** - enhances white fibers of varying width. Crossection of the fibers need not be circular. Parameter "sigma" in pixels corresponds to the largest diameter.

{% include img align="right" name="heart" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/cardio,3-18_sp.2_rec0.5mov.gif" %}

{% include img align="right" name="heart proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/cardio,3-18_sp.2_rec0.5_4_2_3_v3dlin_mov.gif" %}

Example: [Stack of MicroCT images of capillaries in rodent embryonic heart](/media/plugins/capillaries-heart.zip).

-   {% include bc path='Plugins | Biomat | Vector Line 3D Filter'%} with "sigma" = 4 pixels and "scale number" = 2

## Plugins for evaluation of directionality in 2D images using heat equation

**2D Heat Kernel Tensor** - second order moments of heat kernel calculated from 8 bit binary image.

**2D Tensor Color Coding** - standard color coding of 2D tensor image. Symmetric tensor is coded as channels of 32 bit image stacks.

**2D Tensor Statistics** - summary of tensor image (in ROI). "Value" is average trace of the tensor, "shape" is the ratio of its eigenvalues and "angle" of the first eigenvector is measured counterclockwise from the horizontal axis.

{% include img align="right" name="binary" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/MAX_2_4cortexa1.png" %}

{% include img align="right" name="results" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/MAX_2_4cortexa1_res.png" %}

{% include img align="right" name="color" src="https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/MAX_2_4cortexa1_tens_col.png" %}

Example: [Projection of binary images of capillaries in brain](https://raw.githubusercontent.com/jiri-janacek/biomat/master/media/MAX_2_4cortexa1.tif).

-   {% include bc path='Plugins | Biomat | 2D Heat Kernel Tensor'%}
-   {% include bc path='Plugins | Biomat | 2D Tensor Statistics'%}
-   {% include bc path='Process | Biomat | 2D Tensor Color Coding'%}
 
