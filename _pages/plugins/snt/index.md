---
mediawiki: SNT
title: SNT
categories: [Segmentation,Neuroanatomy]
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
nav-links: true
nav-title: Overview
doi: 10.1038/s41592-021-01105-7
---

{% capture author%}
{% include person id='tferr' %}, {% include person id='kephale' %}, {% include person id='carshadi' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='tferr' %}
{% endcapture %}

{% capture source%}
{% include github org='morphonets' repo='SNT' %}
{% endcapture %}
{% include info-box name='SNT' software='complete framework for quantification of neuronal anatomy' logo='<img src="/media/logos/snt.png" width="150"/>' author=author maintainer=maintainer source=source status='stable, active' category='Neuroanatomy' %}

## Overview

SNT is ImageJ's framework for semi-automated tracing, visualization, quantitative analyses and modeling of neuronal morphology. For tracing, SNT supports modern multi-dimensional microscopy data, and highly-customizable routines. For data analysis, SNT features advanced visualization tools, access to all major morphology databases, and support for whole-brain circuitry data. It supersedes the original [Simple Neurite Tracer](/plugins/snt/faq#snt) plug-in.

SNT's documentation is extensive. Please use the navigation bar on too of the page to access the different sections. The major sections are organized as follows:

-   **[Manual](/plugins/snt/manual)**: SNT's user guide for tracing operations
-   **[Walk-throughs](/plugins/snt/step-by-step-instructions)**: Detailed step-by-step instructions for specific tasks
-   **[Screencasts](/plugins/snt/screencasts)**: Video tutorials. If you are using SNT for the first time you probably want to start here
-   **[Reconstruction Viewer](/plugins/snt/reconstruction-viewer)**: SNT's entry point for visualization of pre-existing data. If you are analyzing reconstructions you may want to start here
-   **[Analysis](/plugins/snt/analysis)** Overview of all analysis commands, accessible in either the tracing interface or [Reconstruction Viewer](/plugins/snt/reconstruction-viewer)
-   **[Scripting](/plugins/snt/scripting)** Details on how to use SNT as a scripting library

{% include thumbnail src='/media/plugins/snt/simpleneuritetracer2.png' title='SNT Overview. A key feature of SNT is that *every* aspect of the program can be [scripted](/plugins/snt/scripting) in any of Fiji\'s supported languages, or from Python through [PyImageJ](/scripting/pyimagej).'%}

## Features

### Tracing

-   Support for up to 5D multidimensional images (including multichannel, and those with a time axis). While tracing, visibility of non-traced channels can be toggled at will
-   Precise placement of nodes is aided by a local search that automatically snaps the cursor to neurites wihin a 3D neighborhood
-   A-star search can be performed on a second, non-displayed image. This allows for e.g., tracing on a pre-process (filtered) image while interacting with the unfiltered image (or vice-versa). If enough RAM is available toggling between the two data sources is immediate
-   Tracing is scriptable and can be interleaved with image processing routines
-   Paths can be tagged, searched, grouped and filtered by morphometric properties (length, radius, etc.)
-   Paths can be edited, i.e., a path can be merged into a existing one, or split into two. Nodes can be moved, deleted, or inserted
-   Post-hoc refinement of node positioning by 'snapping' traces to the fluorescent signal associated with a a path

### Analysis

-   *Extensive* repertoire of metrics, namely those provided by [L-measure](http://cng.gmu.edu:8080/Lm/help/index.htm) and [NeuroM](https://github.com/BlueBrain/NeuroM). Metrics can be collected from groups of cells, single cells, or parts thereof
-   Analysis based on neuropil annotations for whole-brain data such as [MouseLight](https://ml-neuronbrowser.janelia.org/)
-   Direct access to public databases, including [MouseLight](https://ml-neuronbrowser.janelia.org/), [FlyCircuit](http://www.flycircuit.tw) and [NeuroMorpho](http://neuromorpho.org/)
-   Built-in commands for *immediate* retrieval of summary statistics, comparison plots and histograms
-   Image processing: Reconstructions can be skeletonized, converted to masks or ROIs, and voxel intensities profiled
-   [Sholl](/plugins/snt/analysis#sholl-analysis) and [Horton-Strahler](/plugins/snt/analysis#strahler-analysis) analyses. {% include wikipedia title="Graph theory" %} and {% include wikipedia title="Persistent homology" %} -based analyses
-   Modeling: access to the [Cx3D simulation engine](/plugins/snt/modeling)

### Visualization

-   [Reconstruction Viewer](/plugins/snt/reconstruction-viewer): Standalone hardware-accelerated 3D visualization tool for both meshes and reconstructions.
    -   Interactive and programmatic scenes (controlled rotations, panning, zoom, scaling, animation, "dark/light mode", etc.)
    -   Customizable views: Interactive management of scene elements, controls for transparency, color interpolation, lightning, path smoothing, etc.. Ability to render both local and remote files on the same scene
    -   Built-in support for several template brains: Drosophila, zebrafish, and Allen CCF (Allen Mouse Brain Atlas)
-   [SciView](/plugins/sciview) integration
-   Quantitative, publication-quality visualization: Display neurons color coded by morphometric traits, or neuropil annotations. Export plots, reconstructions, diagrams and histograms as vector graphics

### Backwards Compatibility

-   Special effort was put into backwards compatibility with older Simple Neurite Tracer releases (including [TrakEM2](/plugins/trakem2) and [ITK interaction](/plugins/snt/tubular-geodesics)). Inherited functionality has been improved, namely:
    -   Extended support for sub-pixel accuracy
    -   Improved synchronization of XY, ZY, and XZ views
    -   Improved calls to Dijkstra's filling and Path-fitting routines
    -   Multi-threading improvements

## Installation

SNT is currently distributed through the [Neuroanatomy](/update-sites/neuroanatomy) [update site](/update-sites). The first time you start SNT from Fiji's menu structure ({% include bc path='Plugins|Neuroanatomy|SNT'%}, or its backwards-compatible alias {% include bc path='Plugins|NeuroAnatomy|Legacy|Simple Neurite Tracer...'%} ) you should be prompted for automatic subscription and download of required dependencies. If not:

1.  Run the Fiji [Updater](/plugins/updater) ({% include bc path='Help|Update..'%}, the penultimate entry in the {% include bc path='Help|'%} menu)
2.  Click *Manage update sites*
3.  Select the *Neuroanatomy* checkbox
4.  Click *Apply changes* and restart Fiji.

**Optional**: For [SciView](/plugins/sciview) and [Cx3D](/plugins/snt/modeling) functionality, you need to subscribe to the *SciView-Unstable* update site. Note that there is nothing inherently *unstable* with this procedure: this nomenclature is adopted from the [Debian release cycle](https://www.debian.org/releases/). The minor annoyance here is that this *Bleeding Edge* site is not included in the official list (this may change in the future), so you'll have to specify its location to the updater:

1.  Re-run the updater and click on *Manage update sites*
2.  If you are currently subscribing to the *SciView* *regular* channel, please unselect its checkbox to minimize version conflicts
3.  Add the following entry to the *Update Sites Table*, by clicking on *Add update site*:
    | Name         | URL                                          |
    |--------------|----------------------------------------------|
    | SciView-edge | https://sites.imagej.net/SciView-Unstable/ |
4.  Click *Apply changes* and restart Fiji
