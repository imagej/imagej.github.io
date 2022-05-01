---
mediawiki: Classic_Watershed
title: Classic Watershed
categories: [Segmentation, Mathematical Morphology]
extensions: ["mathjax"]
---


{% capture author%}
{% include person id='iarganda' %}, David Legland
{% endcapture %}

{% capture maintainer%}
{% include person id='iarganda' %}
{% endcapture %}

{% capture source%}
{% include github org='ijpb' repo='ijpb-plugins' %}
{% endcapture %}
{% include info-box name='Classic Watershed' software='IJPB-plugins' author=author maintainer=maintainer source=source released='July 3<sup>rd</sup>, 2014' latest-version='July 23<sup>rd</sup>, 2019 ([MorphoLibJ](/plugins/morpholibj) v1.4.1)' status='stable, active' category='Segmentation, Mathematical Morphology' %}{\| \|<span>  
</span>style="vertical-align:top" \|{% include thumbnail src='/media/plugins/classic-watershed-lines-blur-blobs.png' title='Overlay of watershed lines on blurred blobs.'%} \|}

## Introduction

{% include thumbnail src='/media/plugins/watershed-flooding-graph.png' title='Schematic overview of watershed flooding in 1D'%}

Classic Watershed is an ImageJ/Fiji plugin to perform watershed segmentation of grayscale 2D/3D images using flooding simulations as described by Pierre Soille and Luc M. Vincent (1990)[^1].

The basic idea consists of considering the input image as topographic surface and placing a water source in each regional minimum of its relief. Next the entire relief is flooded from the sources and dams are placed where the different water sources meet.

All points in the surface at a given minimum constitute the **catchment basin** associated with that minimum. The **watersheds** are the zones dividing adjacent catchment basins.

The first image points that are reached by water are the points at the lowest grayscale value $$h_{min}$$, then all image pixels are progressively reached up to the highest level $$h_{max}$$.

## Usage

The Classic Watershed plugin runs on any **grayscale image (8, 16 and 32-bit) in 2D and 3D**.

At least one image needs to be open in order to run the plugin.

{% include thumbnail src='/media/plugins/classic-watershed-dialog.png' title='Main dialog of the Classic Watershed plugin'%} Image parameters:

-   **Input** image: grayscale image to flood, usually the gradient of an image.
-   **Mask** image (optional): binary image of the same dimensions as the input image which can be used to restrict the areas of application of the algorithm. Set to "None" to run the method on the whole input image.

Morphological parameters:

-   **Use diagonal connectivity**: select to allow the flooding in diagonal directions (8-connectivity in 2D and 26-connectivity in 3D).
-   **Min h**: minimum grayscale value to start flooding from (by default, set to the minimum value of the image type).
-   **Max h**: maximum grayscale value to reach with flooding (by default, set to the maximum value of the image type).

Output:

-   **Labeled image** containing the resulting catchment basins (with integer values 1, 2, 3...) and watershed lines (with 0 value).

## Over-segmentation

Normally, Classic Watershed will lead to an over-segmentation of the input image, especially for noisy images with many regional minima. In that case, it is recommended to **either pre-process the image before running the plugin, or merge regions based on a similarity criterion afterwards**. Several denoising methods are available in Fiji/ImageJ, namely: median filtering, Gaussian blur, bilateral filtering, etc.

### Example

This short macro runs the plugin twice in the blobs sample, first without pre-processing and then after applying a Gaussian blur of radius 3:

```java
// load the Blobs sample image
run("Blobs (25K)");
// invert LUT and pixel values to have dark blobs
run("Invert LUT");
run("Invert");
// run plugin on image
run("Classic Watershed", "input=blobs mask=None use min=0 max=150");
// apply LUT to facilitate result visualization
run("3-3-2 RGB");
// pre-process image with Gaussian blur
selectWindow("blobs.gif");
run("Gaussian Blur...", "sigma=3");
rename("blobs-blur.gif");
// apply plugin on pre-processed image
run("Classic Watershed", "input=blobs-blur mask=None use min=0 max=150");
// apply LUT to facilitate result visualization
run("3-3-2 RGB");
```

Image:Blobs-blur.png\|Gaussian-blurred blobs image used as input (radius = 3). Image:Blobs-watershed-no-preprocessing.png\|Watershed segmentation on original image (Min h = 0, Max h = 150) Image:Blobs-blur-watershed.png\|Watershed segmentation on Gaussian-blurred original image (radius = 3, Min h = 0, Max h = 150)

## Installation

The Classic Watershed plugin is part of the [MorphoLibJ](/plugins/morpholibj) library. To install it, you just need to [ add](/update-sites/following#add-update-sites) the IJPB-plugins update site:

1. Select {% include bc path='Help | Update...'%} from the Fiji menu to start the updater.

2. Click on *Manage update sites*. This brings up a dialog where you can activate additional update sites.

3. Activate the IJPB-plugins update site and close the dialog. Now you should see an additional jar file for download.

4. Click *Apply changes* and restart Fiji.

You should now find the plugin under the sub-menu {% include bc path='Plugins |MorphoLibJ | Segmentation'%}.

**Note**: Classic Watershed is only one of the plugins included in the [MorphoLibJ](/plugins/morpholibj) suite. By following these installation steps, you will be installing as well the rest of plugins in the suite.

## See also

-   [Marker-controlled Watershed](/plugins/marker-controlled-watershed), a plugin to perform watershed by flooding from specific seed points or markers.
-   [Morphological Segmentation](/plugins/morphological-segmentation), a plugin with a graphical user interface to segment images based on morphological operations and the watershed algorithm.
-   [Serge Beucher's site](http://cmm.ensmp.fr/~beucher/wtshed.html), with graphic descriptions and animations of the watershed algorithms.
-   [G. Bertrand's Topological Watershed site](http://www.esiee.fr/~info/tw/index.html), with papers, lecture slides and source code.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

# References

[^1]: {% include citation doi='10.1117/12.24211' %}
