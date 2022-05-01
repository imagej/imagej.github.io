---
mediawiki: Marker-controlled_Watershed
title: Marker-controlled Watershed
categories: [Segmentation, Mathematical Morphology]
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
{% include info-box name='Marker-controlled Watershed' software='IJPB-plugins' author=author maintainer=maintainer source=source released='July 3<sup>rd</sup>, 2014' latest-version='July 23<sup>rd</sup>, 2019 ([MorphoLibJ](/plugins/morpholibj) v1.4.1)' status='stable, active' category='Segmentation, Mathematical Morphology' %}{\| \|<span>  
</span>style="vertical-align:top" \|{% include thumbnail src='/media/plugins/watershed-flooding-markers-blobs-gradient.gif' title='Marker-controlled flooding on the gradient image of the blobs sample.'%} \|}

## Introduction

Marker-controlled Watershed is an ImageJ/Fiji plugin to segment grayscale images of any type (8, 16 and 32-bit) in 2D and 3D based on the marker-controlled watershed algorithm (Meyer and Beucher, 1990). This algorithm considers the input image as a topographic surface (where higher pixel values mean higher altitude) and simulates its flooding from specific seed points or **markers**. A common choice for the markers are the local minima of the gradient of the image, but the method works on any specific marker, either selected manually by the user or determined automatically by another algorithm.

## Usage

{% include thumbnail src='/media/plugins/marker-controlled-watershed-dialog.png' title='Main dialog of the Marker-controlled Watershed plugin'%} Marker-controlled Watershed needs at least two images to run:

-   The **Input** image: a 2D or 3D grayscale image to flood, usually the gradient of an image.
-   The **Marker** image: an image of the same dimensions as the input containing the seed points or markers as connected regions of voxels, each of them with a different label. They correspond usually to the local minima of the input image, but they can be set arbitrarily.

And it can optionally admit a third image:

-   The **Mask** image: a binary image of the same dimensions as input and marker which can be used to restrict the areas of application of the algorithm. Set to "None" to run the method on the whole input image.

Rest of parameters:

-   **Binary markers**: select to specify that markers are binary and need to be labeled.
-   **Calculate dams**: select to enable the calculation of watershed lines.
-   **Use diagonal connectivity**: select to allow the flooding in diagonal directions.

Output:

-   Labeled image containing the catchment basins and (optionally) watershed lines (dams).

{% include thumbnail src='/media/plugins/arabidopsis-nucleus-segmentation.png' title='Example of marker-controlled watershed segmentation on nucleus of *Arabidopsis thaliana* (image courtesy of Kaori Sakai and Javier Arpon, INRA-Versailles)'%}

## Installation

The Marker-controlled Watershed plugin is part of the [MorphoLibJ](/plugins/morpholibj) library. To install it, you just need to [ add](/update-sites/following#add-update-sites) the IJPB-plugins update site:

1\) Select {% include bc path='Help | Update...'%} from the Fiji menu to start the updater.

2\) Click on *Manage update sites*. This brings up a dialog where you can activate additional update sites.

3\) Activate the IJPB-plugins update site and close the dialog. Now you should see an additional jar file for download.

4\) Click *Apply changes* and restart Fiji.

You should now find the plugin under the sub-menu {% include bc path='Plugins | MorphoLibJ | Segmentation'%}.

**Note**: Marker-controlled Watershed is only one of the plugins included in the [MorphoLibJ](/plugins/morpholibj) suite. By following these installation steps, you will be installing as well the rest of plugins in the suite.

## References

1.  Fernand Meyer and Serge Beucher. "Morphological segmentation." Journal of visual communication and image representation 1.1 (1990): 21-46.
2.  Soille, P., "Morphological Image Analysis: Principles and Applications", Springer-Verlag, 1999, pp. 170-171.
3.  David Legland, Ignacio Arganda-Carreras, Philippe Andrey; [MorphoLibJ: integrated library and plugins for mathematical morphology with ImageJ](http://bioinformatics.oxfordjournals.org/content/early/2016/07/19/bioinformatics.btw413). Bioinformatics 2016; 32 (22): 3532-3534. doi: 10.1093/bioinformatics/btw413

## See also

-   [Interactive Marker-controlled Watershed](/plugins/interactive-marker-controlled-watershed), same idea as this plugin but with user-defined seed points.
-   [Morphological Segmentation](/plugins/morphological-segmentation), a plugin with a graphical user interface to segment 2D/3D images based on morphological operations and the watershed algorithm.
-   [Classic Watershed](/plugins/classic-watershed), plugin implementing the original watershed algorithm to segment 2D/3D grayscale images.
-   [Serge Beucher's site](http://cmm.ensmp.fr/~beucher/wtshed.html), with graphic descriptions and animations of the watershed algorithms.
-   [G. Bertrand's Topological Watershed site](http://www.esiee.fr/~info/tw/index.html), with papers, lecture slides and source code.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  
