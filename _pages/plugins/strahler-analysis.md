---
mediawiki: Strahler_Analysis
title: Strahler Analysis
categories: [Skeleton,Analysis,Plugins,Neuroanatomy]
doi: 10.5281/zenodo.49399
tags: strahler,plugin,arbor,neuron,morphometry,dendrite
---

<div style="float:right;">

{% capture maintainer%}
{% include person id='tferr' %}
{% endcapture %}

{% capture author%}
{% include person id='tferr' %}
{% endcapture %}

{% capture source%}
{% include github org='tferr' repo='hIPNAT' %}
{% endcapture %}
{% include info-box software='Fiji' name='Strahler Analysis' maintainer=maintainer author=author filename='hIPNAT_.jar ([Neuroanatomy update site](/plugins/Neuroanatomy))' source=source released='April 2016' category='[Plugins](/plugin-index), [Neuroanatomy](/plugin-index#neuroanatomy), [Analysis](/plugin-index#analysis), [Skeleton](/plugin-index#skeleton)' %}

</div>

A plugin from the [Neuroanatomy update site](/plugins/Neuroanatomy) that performs Strahler analysis on topographic skeletons (2D/3D). {% include wikipedia title='Strahler number' text='Strahler numbering'%} is a numerical procedure that summarizes the branching complexity of mathematical trees.

{% include notice icon="info" content='This page describes how to perform Strahler Analysis on skeletonized images. For analysis of traced structures have a look at [SNT](/plugins/snt).' %}

## Description

<span id="StrahlerAnimation"></span><img src="/media/plugins/strahleranimation.gif" title="fig:Strahler Analysis by iterative elimination of end-point branches" width="300" alt="Strahler Analysis by iterative elimination of end-point branches" /> The analysis occurs through progressive pruning of terminal branches, *iterative tree simplification*, a method that requires detecting all terminal branches (i.e., branches that contain an end-point) and all the degree-one paths leading to them.

*Strahler Analysis* takes a <u>binary</u> or <u>8-bit grayscale</u> image (2D or 3D) containing a <u>single arbor</u>, and calls [AnalyzeSkeleton](/plugins/analyze-skeleton) iteratively to retrieve [Horton-Strahler numbers](#References) from the [skeletonized centerlines](/plugins/skeletonize3d) of the input image. Each iteration includes three operations: 1) a (re)-skeletonization step to ensure that arbor remains represented by its centerlines, 2) an elimination step in which terminal-branches are pruned from the image and 3) an analysis step in which pruned branches are counted and measured. The iteration ceases as soon as all branches have been eliminated or a unresolved [closed loop](#elimination-of-skeleton-loops) has been detected in the pruned arbor.

## Parameters

Tree Classification:  

:;Infer root end-points from rectangular ROI

::This option is only available when a rectangular ROI is present. It is described in [Non-radial arbors](#non-radial-arbors).

:;Ignore single-point arbors (Isolated pixels)

  
  
Elimination of end-point branches may give rise to single point arbors. Such 'debris' have 1 end-point but no slab branches or junctions. When this option is selected, single-point arbors will be discarded on each iteration. If deselected, the total number of end-points may be overestimated.

<!-- -->

Elimination of Skeleton Loops:  

:;Method

::*Strahler Analysis* cannot process skeletons containing closed loops and will output a warning message when such structures have been detected. The available methods in this drop-down menu define how closed loops should be resolved by and are described in the [AnalyzeSkeleton documentation page](/plugins/analyze-skeleton#loop-detection-and-pruning).

:;Unsegmented image

  
  
The initial non-thinned image to be used by [AnalyzeSkeleton](/plugins/analyze-skeleton) for [intensity-based](/plugins/analyze-skeleton#loop-detection-and-pruning) elimination of closed loops. This option is only used if either *Lowest intensity voxel* or *Lowest intensity branch* is chosen as *Method*. Note that if an intensity-based method is selected but the chosen image is a binary one, closed loops will not be resolved.

<!-- -->

Output Options:  

:;Display Iteration stack

::If checked, an image stack that documents individual pruning cycles will be displayed. End-points and Junction-points positions are appended to the stack.

:;Show detailed information

  
  
If checked, analysis will run in *verbose* mode by outputting detailed measurements and by logging debug messages.

## Root Detection

The problem with undiscriminated elimination of terminal branches is that a root-branch containing an end-point is always eliminated on the first iteration step. In order to protect root branches from elimination, *Strahler Analysis* needs to know where root branches are located. As of version 1.4.0, root-detection is implemented by means of a rectangular ROI containing the root branch and by activating the *Infer root end-points from rectangular ROI* option. Here is an example:

<center>

|                                                                                                                                                                                                                                                                                                                                                    |                                          |                                                   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------------------:|:-------------------------------------------------:|
|                                                                                                                                                     Arbor with rectangular ROI containing root                                                                                                                                                     | Analysis ignoring ROI: Inaccurate result | Analysis taking ROI into account: Accurate result |
|                                                                                                                                                <img src="/media/plugins/strahler-rootprotection.png" width="550"/>                                                                                                                                                |                                          |                                                   |
| Root branches are spared from the iterative elimination procedure if marked by a rectangular ROI. Middle image: ROI is ignored. As a consequence, root-branch is interpreted as any other terminal-branch. Right image: Analysis infers that end-point contained by ROI belongs to a root-branch and marked branch is excluded from the iteration. |                                          |                                                   |

</center>

### Notes on Root Detection

-   Only a rectangular ROI can be used to mark the root branch. This is intentional: The way the root-detection algorithm works is by *protecting* all end-points that are contained by the ROI from end-point elimination. Using complex ROIs (e.g., discontinuous or containing internal holes) would make this task much more cumbersome.
-   The ROI only needs to contain root end-point(s) and it should not matter if its boundaries intercept other branches. However, measurements on root-branches may be inaccurate if the ROI contains junction(s) points. The best way to ensure the algorithm ran as expected is to visually inspect all the slices in the *Iteration stack*.
-   Root detection may not be required in the case of radial arbors (i.e., tree-like structures that branch out evenly in multiple directions), if root(s) remain connected in the center of the arbor (as in [animation above](#StrahlerAnimation)). In neurobiology, radial-ramification is an anatomical hallmark of certain cell types such as Retinal Ganglion Cells, Chandelier neurons or Drosophila Class IV sensory neurons.
-   If you are batch processing multiple images you should work with .tif files: When saving as TIFF, ImageJ will store the active ROI in the image header, making it immediately available when the image is open.

## Results

The plugin produces three types of outputs:

Strahler Image  
A heat-map image, in which branches are color-coded by their Horton-Strahler numbers. By default, a calibration ramp ({% include bc path='Analyze|Tools|Calibration Bar...'%}) is added as an overlay. WYSIWYG versions (RGB images) of this *Strahler Color Map* image can be obtained by pressing {% include key keys='Shift|F' %} (shortcut for {% include bc path='Image|Overlay|Flatten'%}).

<!-- -->

Strahler table  
Table listing Horton-Strahler counts. The extension and format of this *Strahler Table* can be specified in {% include bc path='Edit|Options|Input/Output...'%}. It contains the following data:

\# End-point Branches  
The number of branches for each Horton-Strahler order.

:; Ramification ratios

  
  
Ramification or {% include wikipedia title='Strahler number#Bifurcation_ratio' text='bifurcation ratios'%} are the quotients between branches of consecutive orders. An overall ratio may be obtained by averaging ratios across orders.

<!-- -->

Iteration log  
If *Show detailed information* is checked, *Average branch length*, *N. of trees*, *N. of branches*, *N. of junctions*, *N. of triple points*, *N. of quadruple points* are also retrieved for each iteration. These are described in the AnalyzeSkeleton's [documentation page](/plugins/analyze-skeleton#table-of-results).

## Installation

To install *Strahler Analysis* you must use Java 8 and subscribe to the [Neuroanatomy update site](/plugins/Neuroanatomy).

## Related Links

-   [AnalyzeSkeleton](/plugins/analyze-skeleton) and [Skeletonize3D](/plugins/skeletonize3d), analysis of topographic skeletons
-   [Sholl Analysis](/plugins/sholl-analysis), bitmap morphometry based on the Sholl technique

## Citing

* Plugins from the [Neuroanatomy update site](/plugins/Neuroanatomy)[^1].

* [Skeletonization](/plugins/skeletonize3d) and [Skeleton Analysis](/plugins/analyze-skeleton)[^2]

* [BoneJ](/plugins/bonej)[^3]

## Acknowledgments

To all the developers of [AnalyzeSkeleton](https://github.com/fiji/AnalyzeSkeleton/graphs/contributors).

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [Free Software Foundation](http://www.gnu.org/licenses/gpl.txt). This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## References

Original publications by {% include wikipedia title='Robert E. Horton' text='Robert E. Horton'%} and {% include wikipedia title='Arthur Newell Strahler' text='Arthur N. Strahler'%}:

{% include citation doi='10.1130/0016-7606(1945)56[275:EDOSAT]2.0.CO;2' %}

{% include citation doi='10.1130/0016-7606(1952)63[1117:HAAOET]2.0.CO;2' %}

{% include citation doi='10.1029/TR038i006p00913' %} ([PDF](http://www.uvm.edu/~pdodds/files/papers/others/1957/strahler1957a.pdf))

[^1]: {% include citation %}

[^2]: {% include citation id='plugins/analyze-skeleton' %}

[^3]: {% include citation id='plugins/bonej' %}
