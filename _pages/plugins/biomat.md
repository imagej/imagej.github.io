---
mediawiki: Biomat
name: "Biomat"
title: Biomat
categories: [Filtering, Mathematical Morphology]
extensions: ["mathjax"]
release-date: "11/26/2024"
initial-release-date: "03/26/2019"
team-founder: 'Jiří Janáček'
team-maintainer: 'Jiří Janáček | mailto:jiri.janacek_at_fgu.cas.cz'
source-url: https://github.com/jiri-janacek/biomat
---

## Plugins for 3D image preprocessing

**Stack Linear Contrast** - multiplies images in stack by coefficient obtained by linear interpolation of the "first" and "last" parameter. A simple tool for compensation of contrast decreasing with depth within thick sample.

**Lipschitz 3D** Filter - top hat - subtracts slowly varying background calculated as lower Lipschitz envelope from the image.

Preprocessing example: [Stack of confocal microscopy images of capillaries in rat brain](/media/plugins/capillaries-brain.zip)

 {% include img align="center" name="brain" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/capillaries_brain_3Dg.gif" caption="Original data" %}
 
-   {% include bc path='Plugins | Biomat | Stack Linear Contrast'%} with "first" = 1.0 and "last" = 3.0
-   {% include bc path='Process | Filters | Gaussian blur 3D'%} with "sigma" = 1 pixel
-   {% include bc path='Plugins | Biomat | Lipschitz 3D Filter'%} with "slope" = 2 and "top hat" on

 {% include img align="center" name="brain proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/capillaries_brain_proc_3Dg.gif" caption="Processed data" %}

## Morphological operations with quadratic structuring function

**Spherical Extrusion** - tool for calculation of volume of objects from 2D projections.

Example: [Synthetic contours](https://raw.githubusercontent.com/jiri-janacek/biomat/c3f75436ccf4b863dbdf6267a352b129b28a89a7/media/simobjinv.tif)

 {% include img align="center" name="objects" src="https://raw.githubusercontent.com/jiri-janacek/biomat/d9ca3b6cfd867b04717b16a3debd45ef9157419e/media/objects.png" caption="Original data" %}

-   {% include bc path='Plugins | Biomat | Spherical Extrusion'%}

 {% include img align="center" name="objects" src="https://raw.githubusercontent.com/jiri-janacek/biomat/d9ca3b6cfd867b04717b16a3debd45ef9157419e/media/objects_Spherical_extrusion.png" caption="Height of spherical extrusion" %}

The binary image was extruded into 3D by union
of balls which equatorial circles are inside the foreground $$C$$. The
height of the extrusion $$h$$ as the function of 2D point $$x$$
is

$$
h\left(x\right)=\max_{s}\sqrt{d\left(s,C^{c}\right)^{2}-d\left(x,s\right)^{2}}
$$

where $$d$$ is Euclidean distance, $$C^{c}$$ is the background and $$sS$ is the centre of the equatorial circle. 

 {% include img align="center" name="objects" src="https://raw.githubusercontent.com/jiri-janacek/biomat/d9ca3b6cfd867b04717b16a3debd45ef9157419e/media/objects_Spherical_extrusion_res.png" caption="Area and mean height of spherical extrusion" %}

Volume = 2 * Area * Mean.

 {% include img align="center" name="objects" src="https://raw.githubusercontent.com/jiri-janacek/biomat/d9ca3b6cfd867b04717b16a3debd45ef9157419e/media/objects_SphericalExtrusion3d.gif" caption="Reconstructed objects" %}

**Distance Map 3D** - 3D Euclidean distance transform.

Example: [Ball with 40 pixels radius](https://raw.githubusercontent.com/jiri-janacek/biomat/93f0fbe74646db4588feb99e86cb3ba35288dcc2/media/testball.tif)

-   {% include bc path='Plugins | Biomat | Distance Map 3D'%}

## Plugins for detection of fibres in 3D image

**Tensor Line 3D Filter** - enhances white fibers of uniform width sparsely distributed on dark background.

Example: [Stack of confocal microscopy images of capillaries in adipose tissue](/media/plugins/capillaries-adipose.zip).

{% include img align="center" name="adipose" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/capillaries_adipose_3Dg.gif" caption="Original data" %}

-   {% include bc path='Plugins | Biomat | Tensor Line 3D Filter'%} with "sigma" = 3 pixels
-   {% include bc path='Image | Adjust | Brightness/Contrast'%}
-   {% include bc path='Process | Filters | Gaussian blur 3D'%} with "sigma" = 1 pixel

{% include img align="center" name="adipose proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/capillaries_adipose_proc_3Dg.gif" caption="Processed data" %}

**Vector Line 3D Filter** - enhances white fibers of varying width. Crossection of the fibers need not be circular. Parameter "sigma" in pixels corresponds to the largest diameter.

{% include img align="center" name="heart" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/cardio,3-18_sp.2_rec0.5mov.gif" caption="Original data" %}

{% include img align="center" name="heart proc" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/cardio,3-18_sp.2_rec0.5_4_2_3_v3dlin_mov.gif" caption="Processed data" %}

Example: [Stack of MicroCT images of capillaries in rodent embryonic heart](/media/plugins/capillaries-heart.zip).

-   {% include bc path='Plugins | Biomat | Vector Line 3D Filter'%} with "sigma" = 4 pixels and "scale number" = 2

## Plugins for evaluation of directionality in 2D images using heat equation

**2D Heat Kernel Tensor** - second order moments of heat kernel calculated from 8 bit binary image.

**2D Tensor Color Coding** - standard color coding of 2D tensor image. Symmetric tensor is coded as channels of 32 bit image stacks.

**2D Tensor Statistics** - summary of tensor image (in ROI). "Value" is average trace of the tensor, "shape" is the ratio of its eigenvalues and "angle" of the first eigenvector is measured counterclockwise from the horizontal axis.

Example: [Projection of binary images of capillaries in brain](https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/MAX_2_4cortexa1.tif).

{% include img align="center" name="binary" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/MAX_2_4cortexa1.png" caption="Binary image" %}

-   {% include bc path='Plugins | Biomat | 2D Heat Kernel Tensor'%}
-   {% include bc path='Plugins | Biomat | 2D Tensor Statistics'%}

{% include img align="center" name="results" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/MAX_2_4cortexa1_res.png" caption="Statistics" %}

-   {% include bc path='Process | Biomat | 2D Tensor Color Coding'%}
 
{% include img align="center" name="color" src="https://raw.githubusercontent.com/jiri-janacek/biomat/b9b53126134ac7e9fbca9a29de66bc7f2b7c845e/media/MAX_2_4cortexa1_tens_col.png" caption="Color coded tensor image" %}
