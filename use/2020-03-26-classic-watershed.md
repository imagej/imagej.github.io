---
title: Classic Watershed
author: Ignacio Arganda-Carreras
category: Segmentation
layout: post
---

<!-- 

Use markdown to compose the content of your post. 

-------------- Images (no legend) --------------

To include images without a legend (with left, right or center,  fit alignment) simply use the markdown syntax followed by an HTML class to align the image:

![placeholder image]({{ site.baseurl }}/images/placeholder.png){: .image.left} 

{: .image.left} = left alignment
{: .image.right} = right alignment
{: .image.center} = center alignment
{: .image.fit} = centers and fits image (will expand an image to fit window size)

Note: We recommend using {: image.fit} instead of {: .image.center} to avoid images that escape the container (i.e. how the view on mobile).

-------------- Images (with legend) --------------

To include images with a legend, use the markdown/HTML syntax above nested inside a <div class="figure POSITION" markdown="1"></div> tags, where position can be: left, right and center (keep .image.fit). For example:

<div class="figure center" markdown="1">

![placeholder image]({{site.baseurl}}/images/posts/placeholder.png){: .image.fit}

This is the legend text.

</div>

Note: This is very sensitive to spacing. If you indent the nested markdown line, it will render as a code block instead of your image with legend.

For multiple images on the same line, with individual lengends, compact this syntax, place it inside a markdown table and use the "figure row" class. For example:

<div class="figure row" markdown="1">

| IMAGE 1 LEGEND 1 | IMAGE 2 LEGEND 2 | IMAGE 3 LEGEND 3 |

</div>

-------------- YouTube --------------

To include a link to a YouTube video use the following syntax, using the "video-wrapper" class to ensure your video does not escape the container. Copy the iframe video URL and past it inside <div clas="video-wrapper"></div> tags:s

<div class="video-wrapper">
    <iframe width="560" height="315" src="https://www.youtube.com/embed/4NOM-kLfDR8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

-------------- Misc --------------

<hr> = addes line seperator
<br> = break or new line

-->
<div class="figure center" markdown="1">

![Watershed example]({{site.baseurl}}/images/posts/Classic-Watershed-lines-blur-blobs.png){: .image.fit}

Overlay of watershed lines on blurred blobs.

</div>


## **Introduction**
<hr>

<div class="figure right" markdown="1">

![Watershed flooding graph]({{site.baseurl}}/images/posts/250px-Watershed-flooding-graph.png){: .image.fit}

Schematic overview of watershed flooding in 1D.

</div>

Classic Watershed is an ImageJ/Fiji plugin to perform watershed segmentation of grayscale 2D/3D images using flooding simulations as described by [Pierre Soille and Luc M. Vincent (1990)](https://imagej.net/Classic_Watershed#cite_note-Soille1990-1).

The basic idea consists of considering the input image as topographic surface and placing a water source in each regional minimum of its relief. Next the entire relief is flooded from the sources and dams are placed where the different water sources meet.

All points in the surface at a given minimum constitute the **catchment basin** associated with that minimum. The **watersheds** are the zones dividing adjacent catchment basins.

The first image points that are reached by water are the points at the lowest grayscale value h<sub>min</sub>, then all image pixels are progressively reached up to the highest level h<sub>max</sub>.

## **Usage**
<hr>

The Classic Watershed plugin runs on any **grayscale image (8, 16 and 32-bit) in 2D and 3D.**

At least one image needs to be open in order to run the plugin.

<div class="figure right" markdown="1">

![Classic watershed dialog]({{site.baseurl}}/images/posts/Classic-Watershed-dialog.png){: .image.fit}

Main dialog of the Classic Watershed plugin.

</div>

Image parameters:

- **Input** image: grayscale image to flood, usually the gradient of an image.
- **Mask** image (optional): binary image of the same dimensions as the input image which can be used to restrict the areas of application of the algorithm. Set to "None" to run the method on the whole input image.

Morphological parameters:

- **Use diagonal connectivity:** select to allow the flooding in diagonal directions (8-connectivity in 2D and 26-connectivity in 3D).
- **Min h:** minimum grayscale value to start flooding from (by default, set to the minimum value of the image type).
- **Max h:** maximum grayscale value to reach with flooding (by default, set to the maximum value of the image type).

Output:

- **Labeled image** containing the resulting catchment basins (with integer values 1, 2, 3...) and watershed lines (with 0 value).

## **Over-segmentation**
<hr>

Normally, Classic Watershed will lead to an over-segmentation of the input image, especially for noisy images with many regional minima. In that case, it is recommended to **either pre-process the image before running the plugin, or merge regions based on a similarity criterion afterwards.** Several denoising methods are available in Fiji/ImageJ, namely: median filtering, Gaussian blur, bilateral filtering, etc.

### **_Example_**

This short macro runs the plugin twice in the blobs sample, first without pre-processing and then after applying a Gaussian blur of radius 3:

```
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

<div class="figure row" markdown="1">

|![Blobs blur]({{site.baseurl}}/images/posts/200px-Blobs-blur.png)Gaussian-blurred blobs image used as input (radius = 3). | ![Blobs watershed no preprocessing]({{site.baseurl}}/images/posts/200px-Blobs-watershed-no-preprocessing.png) Watershed segmentation on original image (Min h = 0, Max h = 150). | ![Blobs blur watershed]({{site.baseurl}}/images/posts/200px-Blobs-blur-watershed.png) Watershed segmentation on Gaussian-blurred original image (radius = 3, Min h = 0, Max h = 150).|

</div>

## **Installation**
<hr>

The Classic Watershed plugin is part of the [MorphoLibJ](https://imagej.net/MorphoLibJ) library. To install it, you just need to [add](https://imagej.net/How_to_follow_a_3rd_party_update_site#Add_update_sites) the IJPB-plugins update site:

1. Select _Help_ > _Update_... from the Fiji menu to start the updater.

2. Click on _Manage update sites_. This brings up a dialog where you can activate additional update sites.

3. Activate the IJPB-plugins update site and close the dialog. Now you should see an additional jar file for download.

4. Click _Apply_ changes and restart Fiji.

You should now find the plugin under the sub-menu _Plugins_ > _MorphoLibJ_ > _Segmentation._

**Note:** Classic Watershed is only one of the plugins included in the [MorphoLibJ](https://imagej.net/MorphoLibJ) suite. By following these installation steps, you will be installing as well the rest of plugins in the suite.

## **References**
<hr>

 1. Soille, Pierre and Vincent, Luc M (1990). "[Determining watersheds in digital pictures via flooding simulations](http://dx.doi.org/10.1117/12.24211)". Proc. SPIE 1360: 240-250. doi:[10.1117/12.24211](http://dx.doi.org/10.1117/12.24211).

## **See also**
<hr>

- [Marker-controlled Watershed](https://imagej.net/Marker-controlled_Watershed), a plugin to perform watershed by flooding from specific seed points or markers.
- [Morphological Segmentation](https://imagej.net/Morphological_Segmentation), a plugin with a graphical user interface to segment images based on morphological operations and the watershed algorithm.
- [Serge Beucher's site](http://cmm.ensmp.fr/~beucher/wtshed.html), with graphic descriptions and animations of the watershed algorithms.
- [G. Bertrand's Topological Watershed site](http://www.esiee.fr/~info/tw/index.html), with papers, lecture slides and source code.

## **License**
<hr>

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.