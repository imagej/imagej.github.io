---
title: SNT › Strahler Analysis (From Images)
nav-links: true
nav-title: Strahler
name: Strahler plugins
categories: [Skeleton,Analysis,Neuroanatomy]
tags: strahler,plugin,arbor,neuron,morphometry,dendrite,neuroanatomy
update-site: Neuroanatomy
artifact: org.morphonets:SNT
forum-tag: strahler-analysis
icon: /media/icons/snt.png
doi: 10.1038/s41592-021-01105-7
---

{% capture strahler%}
There are several entry points to Strahler Analysis in SNT. You can find those in the _Neuroanatomy Shortcuts_ panel ({% include bc path='Plugins|Neuroanatomy|'%} or "SNT" icon in Fiji's toolbar):
<br/>
<ol>
<li><i>Strahler Analysis (Image)...</i> Direct parsing of skeletonized images, bypassing tracing (described on this page)</li>
<li><i>Strahler Analysis (Tracings)...</i> Parsing of traced structures (described in 
<a href="/plugins/snt/analysis#strahler-analysis">Analysis › Strahler (Tracings)</a>)</li>
<li><i>Strahler Analysis Scripts</i>  Batch processing of files</li>
</ol>
{% endcapture %}
{% include notice icon="info" content=strahler %}

{% capture strahler%}
While _Strahler Analysis (Image)..._ remains a functional workflow, you may find its simplicity rather limiting. A more flexible approach may be to convert [skeletonized images into traced paths](/plugins/snt/walkthroughs#full-automated-tracing) and run [Strahler Analysis (Tracings)](/plugins/snt/analysis#strahler-analysis) on them.
{% endcapture %}
{% include notice icon="warning" background-color="#fffbeb" content=strahler %}

{% include img align="right" src="/media/plugins/snt/strahler-classification-example.png" caption="Strahler classification"%}
Strahler numbering is a numerical procedure that summarizes the branching complexity of mathematical trees. It is described in detail [here](./analysis#strahler-analysis).

## Description

*Strahler Analysis (Image)* takes a <u>binary</u> or <u>8-bit grayscale</u> image (2D or 3D) containing a <u>single arbor</u>, and calls [AnalyzeSkeleton](/plugins/analyze-skeleton)[^2] iteratively to retrieve [Horton-Strahler numbers](./analysis#strahler-analysis) from the [skeletonized centerlines](/plugins/skeletonize3d) of the input image. Each iteration includes three operations:

1. A (re)-skeletonization step to ensure that arbor remains represented by its centerlines
2. an elimination step in which terminal-branches are pruned from the image
3. An analysis step in which pruned branches are counted and measured. The iteration ceases as soon as all branches have been eliminated or a unresolved [closed loop](#elimination-of-skeleton-loops) has been detected in the pruned arbor.

## Parameters

### Tree Classification

**Infer root end-points from rectangular ROI**: This option is only available when a rectangular ROI is present. It is described in [root detection](#root-detection).

<span id="strahler-animation">
{% include img align="right" width="300" name="Strahler Analysis by iterative elimination of end-point branches" src="/media/plugins/snt/strahleranimation.gif" caption="Direct analysis of images occurs through progressive pruning of terminal branches, *iterative tree simplification*, a method that requires detecting all terminal branches (i.e., branches that contain an end-point) and all the degree-one paths leading to them." %}

**Ignore single-point arbors (Isolated pixels)** Elimination of end-point branches may give rise to single point arbors. Such 'debris' have 1 end-point but no slab branches or junctions. When this option is selected, single-point arbors will be discarded on each iteration. If deselected, the total number of end-points may be overestimated.


### Elimination of Skeleton Loops

**Method** *Strahler Analysis* cannot process skeletons containing closed loops and will output a warning message when such structures have been detected. The available methods in this drop-down menu define how closed loops should be resolved by and are described in the [AnalyzeSkeleton documentation page](/plugins/analyze-skeleton#loop-detection-and-pruning).

***Unsegmented image*** The initial non-thinned image to be used by [AnalyzeSkeleton](/plugins/analyze-skeleton) for [intensity-based](/plugins/analyze-skeleton#loop-detection-and-pruning) elimination of closed loops. This option is only used if either *Lowest intensity voxel* or *Lowest intensity branch* is chosen as *Method*. Note that if an intensity-based method is selected but the chosen image is a binary one, closed loops will not be resolved.

### Output Options

***Display Iteration stack*** If checked, an image stack that documents individual pruning cycles will be displayed. End-points and Junction-points positions are appended to the stack.

***Show detailed information*** If checked, analysis will run in *verbose* mode by outputting detailed measurements and by logging debug messages.

## Root Detection

{% include img align="right" width="600px" src="/media/plugins/snt/strahler-rootprotection.png" caption="**Left**: Arbor with rectangular ROI containing root. **Middle**: Analysis ignores ROI. Root-branch is interpreted as any other terminal-branch and the resulting classification is inaccurate. **Right**: Analysis takes ROI into account and infers that the end-point contained by the ROI is the root of the structure. Root branch is excluded from the iteration and the classification is accurate." %}

The problem with undiscriminated elimination of terminal branches is that a root-branch containing an end-point is always eliminated on the first iteration step. In order to protect root branches from elimination, *Strahler Analysis* needs to know where root branches are located. Root-detection is implemented by means of a rectangular ROI containing the root branch and by activating the *Infer root end-points from rectangular ROI* option. Here is an example:

### Notes on Root Detection

-   Only a rectangular ROI can be used to mark the root branch. This is intentional: The way the root-detection algorithm works is by *protecting* all end-points that are contained by the ROI from end-point elimination. Using complex ROIs (e.g., discontinuous or containing internal holes) would make this task much more cumbersome.
-   The ROI only needs to contain root end-point(s) and it should not matter if its boundaries intercept other branches. However, measurements on root-branches may be inaccurate if the ROI contains junction(s) points. The best way to ensure the algorithm ran as expected is to visually inspect all the slices in the *Iteration stack*.
-   Root detection may not be required in the case of radial arbors (i.e., tree-like structures that branch out evenly in multiple directions), if root(s) remain connected in the center of the arbor (as in the [animation above](#strahler-animation)). In neurobiology, radial-ramification is an anatomical hallmark of certain cell types such as Retinal Ganglion Cells, Chandelier neurons or Drosophila Class IV sensory neurons.
-   If you are batch processing multiple images you should work with .tif files: When saving as TIFF, ImageJ will store the active ROI in the image header, making it immediately available when the image is open.

## Outputs

The plugin produces three types of results:

1. ***Strahler Image***: A heat-map image, in which branches are color-coded by their Horton-Strahler numbers. By default, a calibration ramp ({% include bc path='Analyze|Tools|Calibration Bar...'%}) is added as an overlay. WYSIWYG versions (RGB images) of this *Strahler Color Map* image can be obtained by pressing {% include key keys='Shift|F' %} (shortcut for {% include bc path='Image|Overlay|Flatten'%}).

2. ***Strahler table*** Table listing Horton-Strahler counts. The extension and format of this *Strahler Table* can be specified in {% include bc path='Edit|Options|Input/Output...'%}. It contains the following data:

   * End-point Branches - The number of branches for each Horton-Strahler order.
   * Ramification ratios - Ramification or {% include wikipedia title='Strahler number#Bifurcation_ratio' text='bifurcation ratios'%} are the quotients between branches of consecutive orders. An overall ratio may be obtained by averaging ratios across orders.

3. ***Iteration log*** If *Show detailed information* is checked, *Average branch length*, *N. of trees*, *N. of branches*, *N. of junctions*, *N. of triple points*, *N. of quadruple points* are also retrieved for each iteration. These are described in the AnalyzeSkeleton's [documentation page](/plugins/analyze-skeleton#table-of-results).


## Limitations and Comparison to _Strahler Analysis (Tracings)_
{% include img align="right" width="800px" src="/media/plugins/snt/strahler-analysis-from-reconstructions.png" caption="[Strahler Analysis (Tracings)](/plugins/snt/analysis#strahler-analysis) provides more detailed quantifications at the expense of reconstruction." %}
There are two major limitations with parsing images directly:

1. Accuracy of skeletonization: The analysis can only be as accurate as the image segmentation. For many images (specially those depicting simpler structures) this may not be an issue, but you should always be critical of results obtained from ill-segmentation. If your images are not ameanable to direct parsing, consider reconstructing them in SNT beforehand

2. Simple morphometry: Because no reconstruction is performed, the type of measurements that is performed at each Strahler order is rather limited. For detailed morphometry, consider automatic reconstruction of the skeletonized image in SNT using the _Extract Paths from Segmented Image..._ command.


## Related Workflows

- [Sholl Analysis](./sholl)
- [AnalyzeSkeleton](/plugins/analyze-skeleton) and [Skeletonize3D](/plugins/skeletonize3d), analysis of topographic skeletons (see also [BoneJ](/plugins/bonej) that has made several improvements to skeletonization routines)


## Citing

- The [authoritative reference](faq#how-do-i-cite-snt) for *Strahler Analysis* workflows is the SNT publication: {% include citation id='plugins/snt' %}

- The authoritative reference for *AnalyzeSkeleton* is: {% include citation id='plugins/analyze-skeleton' %}


## References

The original literature by {% include wikipedia title='Robert E. Horton' text='Robert E. Horton'%} and {% include wikipedia title='Arthur Newell Strahler' text='Arthur N. Strahler'%}  is listed [here](./analysis#strahler-analysis).
