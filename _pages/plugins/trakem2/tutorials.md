---
mediawiki: TrakEM2_tutorials
title: TrakEM2 tutorials
categories: [TrakEM2,Tutorials]
---

## Video tutorial on 3D reconstruction from serial section

TODO GOOGLE SPREADSHEET WIDGET

{% include clear%}


## Video tutorial on the basic recipe for TrakEM2

{% include img src="/media/plugins/trakem2/screenshot-trakem2-basics-tutorial.png" alt='TrakEM2 basic tutorial' link='/plugins/trakem2/basics-tutorial' align='right' width='255'%}

This is the [basic tutorial for TrakEM2](/plugins/trakem2/basics-tutorial). **If you are new to TrakEM2, please start by watching [this tutorial](/plugins/trakem2/basics-tutorial)**. It includes:

-   Importing an image stack.
-   Registering stack slices manually, using color overlays and affine transforms.
-   Defining a template tree structure for your segmentations.
-   Segmenting cells across multiple sections.
-   3D visualization.

{% include clear%}


## Video tutorial on segmenting/outlining objects over multiple sections in 3D

{% include img src="/media/plugins/trakem2/arealists-brushing.jpg" alt='TrakEM2 brushing ' link='http://www.ini.uzh.ch/~acardona/movies/arealist-create-and-edit.mp4' align='right' width='255'%} This mp4 [video tutorial](http://www.ini.uzh.ch/~acardona/movies/arealist-create-and-edit.mp4) was made by Albert Cardona. To visualize it, you need a mp4 player. It covers:

-   How to use the PEN tool with "area lists" segmentation type (paint an area, flood-fill, erase, flood-erase).
-   How to use ROIs (selections like polygon and freeroi) to edit "area lists".

See also the list of [key bindings for AreaList](http://www.ini.uzh.ch/~acardona/trakem2_manual.html#edit_arealist).

{% include clear%}


## Video tutorial on aligning sections

{% include img src="/media/plugins/trakem2/screenshot-trakem2-align-sections-tutorial.png" alt='TrakEM2 align sections tutorial' link='/plugins/trakem2/align-sections-tutorial' align='right' width='255'%}

[This video tutorial](/plugins/trakem2/align-sections-tutorial) is focused on:

-   Automatically registering sections.
-   Selecting feature extraction parameters.

See also the feature extraction and alignment [parameters explained](http://www.ini.uzh.ch/~acardona/howto.html#sift_parameters).

{% include clear%}


## Video tutorial on manual segmentation modes

{% include img src="/media/plugins/trakem2/screenshot-trakem2-manual-segmentation-modes-tutorial.png" alt='TrakEM2 manual segmentation modes' link='/plugins/trakem2/segmentation-modes-tutorial' align='right' width='255'%}

[Tutorial on how to manually segment cells using the 3 segmentation modes](/plugins/trakem2/segmentation-modes-tutorial):

Overlap  
multiple arealists can coexist in space (the normal mode; arealists are independent).

Exclude  
when painting in an arealist, do not allow paint to occur over any other existing arealist.

Erode  
when painting in an arealist, paint in the current but erase any other arealist.

{% include clear%}


## Video tutorial on semi-automatic segmentation

{% include img src="/media/plugins/trakem2/screenshot-trakem2-tutorial-automatic-segmentation.png" alt='TrakEM2 semi-automatic segmentation' link='/plugins/trakem2/semi-automatic-segmentation-tutorial' align='right' width='255'%}

In [this video tutorial](/plugins/trakem2/semi-automatic-segmentation-tutorial) you will learn:

-   How to segment cells by only one click.
-   Fast marching method tool in TrakEM2.
-   Selecting segmentation parameters.

{% include clear%}


## Video tutorial on measuring surfaces and volumes

{% include img src="/media/plugins/trakem2/screenshot-trakem2-tutorial-measure-surfaces.png" alt='TrakEM2 measuring surfaces and volumes' link='/plugins/trakem2/measurements-tutorial' align='right' width='255'%}

In [this video tutorial](/plugins/trakem2/measurements-tutorial) you will learn how to:

-   Extract information from TrakEM2 project objects.
-   Save measurements into files.

See also [AreaList measurements](http://www.ini.uzh.ch/~acardona/trakem2_manual.html#measure_arealist) in the TrakEM2 manual, with figures.

{% include clear%}


## Video tutorial on adding sections/layers to an existing project

{% include img src="/media/plugins/trakem2/screenshot-trakem2-tutorial-add-layers.png" alt='TrakEM2 adding layers to existing project' link='/plugins/trakem2/add-more-sections-layers-tutorial' align='right' width='255'%}

[Here](/plugins/trakem2/add-more-sections-layers-tutorial) you will learn how to:

-   Open an image sequence as a virtual stack in Fiji.
-   Calibrate the virtual stack.
-   Import the virtual stack into TrakEM2 as a sequence of layers (sections), one image per layer.

In the tutorial, the layers are imported following an existing set of layers, i.e. concatenating to enlarge the collection of sections.

{% include clear%}


## Video tutorial on saving a project

{% include img src="/media/plugins/trakem2/screenshot-trakem2-save-project.png" alt='TrakEM2 saving a project' link='/plugins/trakem2/saving-project-tutorial' align='right' width='255'%}

-   [Saving a TrakEM2 project](/plugins/trakem2/saving-project-tutorial) into an .XML file.

## See Also

-   [TrakEM2 Scripting](/plugins/trakem2/scripting)
-   [TrakEM2](/plugins/trakem2) wiki page
-   [TrakEM2 web page](http://www.ini.uzh.ch/~acardona/trakem2.html)

 
