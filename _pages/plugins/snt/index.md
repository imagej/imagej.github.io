---
name: SNT
title: SNT
description: The ImageJ framework for quantification of neuronal anatomy.
forum-tag: snt
categories: [Segmentation,Neuroanatomy]
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
nav-links: true
nav-title: Overview
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
update-site: Neuroanatomy
doi: 10.1038/s41592-021-01105-7
---

SNT[^1] is ImageJ's framework for tracing, visualization, quantitative analyses and modeling of neuronal morphology. For tracing, SNT supports modern multidimensional microscopy data, semi-automated and automated routines, and options for editing traces. For data analysis, SNT features advanced visualization tools, access to all major morphology databases, and support for whole-brain circuitry data.

{% capture text%}
**SNT is based on [publications](/plugins/snt/faq#how-do-i-cite-snt). Please [cite](/plugins/snt/faq#how-do-i-cite-snt) SNT in your own research!**
{% endcapture %}
{% include notice icon="info" content=text %}

## Overview

SNT is a toolbox for tracing and analyzing neuronal morphologies imaged using light microscopy. It aims to be as complete as possible, while remaining efficient to use. It can be used as a desktop application, or a [scripting library](/plugins/snt/scripting). It supersedes the original [Simple Neurite Tracer](/plugins/snt/faq#what-is-the-difference-between-snt-and-simple-neurite-tracer) software, and aggregates other tools previously scattered across the Fiji ecosystem of plugins, including [Sholl](./sholl)[^2] and [Strahler](./strahler) plugins.

The [source repository](https://github.com/morphonets/SNT) contains more details about the project, including a list of [features](https://github.com/morphonets/SNT#features), and [implementation details](https://github.com/morphonets/SNT/blob/-/NOTES.md#notes). Below is a gallery showcasing SNT's functionality:

{% include gallery align="fill" content=
"
/media/plugins/snt/snt-overview.png | Overview of SNT components &amp; SNT functionality
/media/plugins/snt/snt-4D-examples.png | [Semi-automated tracing](/plugins/snt/walkthroughs#semi-automated-tracing): Support for multi-channel and [timelapse](/plugins/snt/walkthroughs#time-lapse-analysis) images
/media/plugins/snt/snt-auto-tracing-overview.png | [Fully automated tracing](/plugins/snt/walkthroughs#full-automated-tracing) of segmented images
/media/plugins/snt/snt-v3-overview.png | [Scripted routines](/plugins/snt/scripting#bundled-templates) co-exist with graphical user interface operations
/media/plugins/snt/snt-script-example.png | [Scripting](/plugins/snt/scripting) in any of Fiji's supported languages facilitated by SNT's [Script Recorder](/plugins/snt/scripting#script-recorder)
/media/plugins/snt/snt-notebook.png | Scripting in native Python using [PySNT](https://pysnt.readthedocs.io/en/latest/)
/media/plugins/snt/snt-delaunay-triangulation.png | Delaunay tessellation: Tracings can be used in [image processing routines](/plugins/snt/manual#process-)
/media/plugins/snt/snt-density-map.png | Density maps for group(s) of cells obtained from [built-in scripts](/plugins/snt/scripting#bundled-templates)
/media/plugins/snt/snt-recviewer-convexhull-and-surface.png | [Convex hulls](/plugins/snt/analysis#convex-hull-analysis) and [surface annotations](/plugins/snt/reconstruction-viewer#geometric-annotations)
/media/plugins/snt/snt-montage-light.png | Quantitative and publication quality visualizations
/media/plugins/snt/snt-montage-dark.png | Data-rich 3D visualizations
/media/plugins/snt/snt-rec-viewer-demo2-dark.gif | [Interactive 3D scenes](/plugins/snt/reconstruction-viewer)
/media/plugins/snt/sholl-analysis-outputs.png | [Sholl](/plugins/snt/#sholl) and [Strahler](/plugins/snt/analysis#strahler) directly from images (bypassing tracing)
/media/plugins/snt/snt-angular-sholl.png | Advanced [Sholl-based quantifications](/plugins/snt/sholl#angular-sholl)
/media/plugins/snt/snt-root-angle-analysis.png | [Root Angle Analysis](/plugins/snt/analysis#root-angle-analysis)
/media/plugins/snt/snt-local-angle-surface-analysis.png | Analysis of [surface angles/arbor orientation](/plugins/snt/metrics#extension-angle)
/media/plugins/snt/snt-delineation-analysis2.png | [Delineation analyses](/plugins/snt/walkthroughs#delineation-analysis)
/media/plugins/snt/snt-growth-analysis.png | [Growth Analysis](/plugins/snt/analysis#growth-analysis)
/media/plugins/snt/snt-ferris-wheel.png | Routines to summarize [innervation patterns](/plugins/snt/analysis#graph-based-analysis)
/media/plugins/snt/graph-viewer-ferris-wheel.png | Routines to summarize data from [projectomes and connectomics](/plugins/snt/analysis#graph-based-analysis)
/media/plugins/snt/snt-2d-histogram.png | Specialized [statistics](/plugins/snt/analysis#statistics)
/media/plugins/snt/snt-labkit-training.png | [Semantic segmentation](/plugins/snt/machine-learning)
/media/plugins/snt/snt-astrocyte-example.png | Glia analysis: Bulk characterization (width and length) of astrocytic processes ([use case](https://forum.image.sc/t/determining-astrocyte-width-from-2d-images-using-fiji-snt/56426/2))
/media/plugins/snt/snt-non-neuronal-example.png | Not only neurons: SNT can be used to analyze many types of filamentous structures
"
%}

## Installation

SNT is currently distributed through [Fiji](/software/fiji)'s [Neuroanatomy update site](/update-sites/neuroanatomy). The first time you start SNT from Fiji's menu structure ({% include bc path='Plugins|Neuroanatomy|SNT'%}), you should be prompted for automatic subscription and download of required dependencies. If not:

1. Run the Fiji [Updater](/plugins/updater) ({% include bc path='Help|Update...'%}, the penultimate entry in the {% include bc path='Help|'%} menu)
2. Click *Manage update sites*
3. Search for *Neuroanatomy* (or *SNT*) and activate the *Neuroanatomy* checkbox
4. Click *Apply changes* and restart Fiji

**Optional**: For [sciview](/plugins/sciview) and [Cx3D](/plugins/snt/modeling) functionality, you need to install [sciview](/plugins/sciview). See the [official sciview documentation](https://docs.scenery.graphics/sciview) for details.

## Documentation

SNT's documentation is extensive. Please use the navigation bar on top of the page to access the different sections, organized as follows:

| Section                                                         | Contents                                                                                                                           |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **[Analysis](/plugins/snt/analysis)**                           | Overview of GUI-based analyses                                                                                                     |
| **[Contributing](/plugins/snt/contribute)**                     | How to contribute to SNT                                                                                                           |
| **[Extending](/plugins/snt/extending)**                         | Resources for developers interested in extending SNT or parsing TRACES files                                                       |
| **[FAQ](/plugins/snt/faq)**                                     | Frequently asked questions                                                                                                         |
| **[Key Shortcuts](/plugins/snt/key-shortcuts)**                 | List of SNT shortcuts (keyboard cheatsheet)                                                                                        |
| **[Machine Learning](/plugins/snt/machine-learning)**           | Semantic segmentation: Labkit and TWS integration                                                                                  |
| **[Manual](/plugins/snt/manual)**                               | User guide for main interface and tracing operations                                                                               |
| **[Metrics](/plugins/snt/metrics)**                             | Definition of metrics                                                                                                             |
| **[Modeling](/plugins/snt/modeling)**                           | Cx3D integration                                                                                                                   |
| **[Reconstruction Viewer](/plugins/snt/reconstruction-viewer)** | SNT's entry point for visualization of pre-existing data. If you are analyzing neuronal reconstructions you may want to start here |
| **[Screencasts](/plugins/snt/screencasts)**                     | Video tutorials. If you are using SNT for the first time you probably want to start here                                           |
| **[Scripting](/plugins/snt/scripting)**                         | Details on how to use SNT as a scripting library                                                                                   |
| **[Walkthroughs](/plugins/snt/walkthroughs)**     | Detailed step-by-step instructions for specific tasks                                                                              |

## References

[^1]: {% include citation id='plugins/snt' %}
[^2]: {% include citation id='plugins/snt/sholl' %}
