---
mediawiki: Minimum_Cost_Z_surface_Projection
title: Minimum Cost Z surface Projection
categories: [Projection]
---

{% capture benoalo %}{% include person id='benoalo' %}{% endcapture %}
{% include info-box software='ImageJ/Fiji' name='Min Cost Z Surface' author=benoalo maintainer=benoalo released='03 August 2016' filename='![](/media/mincostzsurface-1.1.0.jar.zip)' source=' [MPI-CBG git](https://git.mpi-cbg.de/bioimage-informatics/MinCostSurface_Projection)' category='Plugins, Projection' %}

## Introduction

This plugin detects minimum cost z-surface in a 3D volume. A z surface is a topographic map indicating the altitude z as a function of the position (x,y) in the image. The cost of the surface depends on pixel intensity the surface is going through. This plugin find the z-surface with the lowest intensity in an image.

The detected surface can be used to remove signal close to the surface. For instance if the surface is occluding other objects of interest. Inversely, if one wants to visualize a surface ocluded by other object the signal far from the surface can be attenuated. Figure 1 and 2 are illustrate these use cases.

![](/media/mincostsurf-ex2-surfaceselection.png)

<div align="center">

**Figure 1** shows the projection of a wing with and without the detection of a minimum cost z surface. The use of surface detection allows to remove signal degrading the details of the wing structure. Data credit: Andreas Sagner, Eaton lab, MPI-CBG, Dresden

</div>

![](/media/plugins/mincostsurf-ex1-removesurface.png)

<div align="center">

**Figure 2** shows how the surface of a drosophyla embryo can be virtually removed to ease the observation and analysis of internal organs. Data credit: Shradha Das, Knust Lab, MPI-CBG, Dresden

</div>

## Usage

Both examples illustrated in the previous section can be reproduced with the Min\_Cost\_Surface plugin. Below is a tutorial to reproduce the example from figure 1. First of all load an image with a surface structure you would like to detect. In our example it is portion of a fly wing. the wing is not flat and can not be visualized in a single slice. Max Projection of the image give poor result in visualizing the wing in a single plane since other structures present in the volume hide the details of the wing. The plugin allows to detect the wing surface and to select a region with a user defined thickness around it.

-   If your surface appears with high intensity value you need to duplicate it and invert it. With this manipulatiuon you should have a volume where your surface appears with low intensity. It will be used by the plugin to measure the cost of the surface. Any kind of preprocessing that can enhance the surface can be used to favor a good detection of the surface.

![](/media/plugins/mincostsurf-inputimage.png)

<div align="center">

Input image (left) and cost image (right) for the detection of fly winf with the min cost surface plugin

</div>

-   Start the plugin. an interface requesting parameters will open
    -   **input image**: image with the surface to extract
    -   **cost image**: image used to measure the cost of the surface. The surface should appear with low intensity in that image
    -   **rescale x,y**: factor by which the image length and width will be divided for the processing. It serve to speed up the algorithm as well as regularizing the results in case there are holes in the surface
    -   **rescale z**: factor by which the image depth will be divided for the processing.
    -   **Max delta z between adjacent voxels**: This indicates the maximum variation of the z map altitude between 2 neighbor pixels (in downsampled image). if z was very large the results would be a max projection. A value of 0 would output a flat plane. A value of 1 or 2 allow to construct slowly varying surface.
    -   **display volume(s) adjacent to the surface**: if checked, a volume adjacent to the surface will be outputed
    -   **volume number of slices**: the total number of slice of the volume adjacent to the surface
    -   **2 surfaces**: if checked 2 surfaces will be detected in the volume (based on the single cost image inputed)
    -   **Max distance between surfaces**: maximum distance in pixel between the 2 detected surfaces
    -   **Min distance between the surfaces**: minimum distance in pixel between the 2 detected surfaces

![](/media/plugins/mincostsurf-gui.png)

<div align="center">

user interface of the plugin with the parameter used for this example

</div>

-   the plugin will output3 images:
    -   The downsampled cost image used for the calculation
    -   the altitude map of the surface with minimum cost. Altitude is in pixel between 0 and the number of slice of the original image
    -   A volume showing the intensity on the surface on the center slice. Other slice correspond to the intensity if the original image on tranlated version of the surface.

![](/media/plugins/mincostsurf-output.png)

<div align="center">

Plugin output: an altitude map (left) and a volume showing intensity on the surface (right) moving the slider is equivalent to translating the surface

</div>

## Methods and Implementation

The initial development of the plugin was initially proposed by Dagmar Kainmueller (Myers lab MPI-CBG, Dresden ). The plugin was implemented after the method of Li et al. \[1\]. One can refer to that paper for the principle of the surface detection. The mincut maxflow problem is solved using the GraphCut solver implemented in Fiji [Graph\_Cut plugin by Jan Funke](https://fiji.sc/Graph_Cut).

Also If the plugin allows to detect only two surface with one input function, the underlying class has more flexibility and can handle any number of surface and cost function. It also allow to add crossing or non crossing constraints on any pair of surfaces as described in Li et al.

\[1\] Li, K., Wu, X., Chen, D. Z., & Sonka, M. (2006).[Optimal surface segmentation in volumetric images, a graph-theoretic approach](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2646122/). Pattern Analysis and Machine Intelligence, IEEE Transactions on, 28(1), 119-134.

## History

**2016-08-03 : version 1.1.0**

**2017-11-30 : update to version 1.1.3**

-   2 ops were added to the package to call 1 and 2 surface projection from script and 1 for image reslice.
-   the reslicing from script uses linear interpolation.
-   from script, a new relative surface weight can be used to support surface detection

 
