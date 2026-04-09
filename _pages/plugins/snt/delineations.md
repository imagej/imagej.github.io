---
title: SNT › Delineation Analysis
nav-links: true
nav-title: Delineations
name: Delineation Analysis
categories: [Contours,Analysis,Neuroanatomy]
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
doi: 10.1038/s41592-021-01105-7
tags: snt,tracing,neuroanatomy,contours
---


{% capture version%}
**This page was last revised for [version 5.0.6](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

# Delineation Analysis
Delineations aggregate sections of reconstructions into groups to allow measuring proportions of paths within other structures defined by ROIs or neuropil annotations (e.g., cortical layers, biomarkers, or counterstaining landmarks). Delineation analyses can be applied to disconnected paths, a single cell, or multiple cells. Some of the questions that delineation analyses can answer include:

- Do branching patterns of neurons change along strata (cell layers)?
- What is the total dendritic/axonal length contained within a cortical layer?
- Do branches near a lesion site differ from branches further away from it?
- Are there morphological differences across subregions of a neuron's receptive field?

{% capture ml-demo %}
You can use the _MouseLight dendrites_ demo dataset to follow the delineation tutorials. While this dataset does not include counterstaining images, it can still be used for both ROI-based and Atlas-based delineations:

1. Open {% include bc path='File|Load Demo Dataset...' %} and choose _MouseLight dendrites (Reconstructions only)_
2. Right-click on the _Display Canvas_ and choose _Pause SNT_ from the contextual menu
3. Follow the instructions below
{% endcapture %}
{% include notice icon="info" content=ml-demo %}

<div align="center">
  <img  src="/media/plugins/snt/snt-delineation-analysis1.png" alt="Delineation Analysis: MouseLight dendrites demo dataset delineated by cortical layers " title="Delineation Analysis: MouseLight dendrites demo dataset delineated by cortical layers " width="650" />
</div>

## Creating Delineations from ROIs
The most common way to generate delineations is by means of ROIs:

1. Activate the _Delineations_ tab in the [main dialog](/plugins/snt/manual#delineations-tab)

2. Pause SNT by right-clicking on the image and choose "Pause SNT" from the contextual menu

3. Create an area ROI. _Any_ area ROI is supported (freehand, polygon, wand-defined, rectangular, oval, etc.)

4. Press the _Assign_ button. Sections of paths with XY coordinates contained by the ROI are colored by the delineation label. Note that assignments propagate to all Z-coordinates within the ROI

5. Optional: If you prefer, press the <i class="fas fa-pen"></i> icon and type a new label in the _name_ field You can also change the delineation color by clicking its color tag

6. Repeat this process as needed until all paths of interest have been tiled by a delineation. If needed, visibility of previously assigned ROIs can be toggled using the <i class="fas fa-eye"></i> button

7. Proceed to [Measuring Delineations](#measuring-delineations)

ROIs generated programmatically or in bulk outside SNT can be applied in a single step using _Import Assignments from ROI Manager_ from the Options (gear) menu. This command will parse each area ROI in the ROI Manager as an assignment ROI. The delineation name and color will be retrieved directly from ROIs that have been renamed or colored (either stroke or fill color).


## Creating Delineations from Atlas Annotations
Delineations can also be created from [neuropil annotations](/plugins/snt/analysis#atlas-based-analysis) using the _Import Assignments from Atlas Annotation_ option from the Options (gear) menu. In this case delineations are created from selected brain compartments associated with the cell(s) being analyzed. Note that this requires cells to be tagged by atlas annotations. Currently only cells downloaded directly from the MouseLight database fulfill this criterion.


## Editing Delineations
To re-define a delineation it is sufficient to re-define or re-adjust an existing ROI and press the _Assign_ button. The Options (gear) menu lists commands for rebuilding, restoring, and deleting delineations. Most of the editing operations can be performed through the toolbar at the bottom of the delineations list, including:
- <i class="fas fa-plus"></i> Adds more entries to the delineations list
- <i class="fas fa-object-group"></i> Merges two or more delineations into one
- <i class="fas fa-swatchbook"></i> Applies one of the default color schemes to the delineations list
- <i class="fas fa-pen"></i> Enables/Disables direct editing of delineation names
- _Outside color_ widget: Defines the color for non-delineated sections, i.e., those sections that remain _outside_ delineated areas


## Measuring Delineations

Measurements are retrieved using the <i class="fas fa-chart-bar"></i> _Plot_ and <i class="fas fa-table"></i> _Measure_ buttons:

- <i class="fas fa-chart-bar"></i> _Plot_: Plots distributions of selected metrics. Plotting styles include: Box plots (one delineation per category), multi-series histograms (one delineation per series), or a montage of single-series histograms (one panel per delineation)
- <i class="fas fa-table"></i> _Measure_: Reports common metrics to a dedicated table (Total length, No. of nodes, No. of junctions, etc.) across delineations

In addition to defined delineations, plots and tables may include two other categories:

- _Non-delineated_: This category corresponds to all the path sections that remained in-between or outside delineations. _Non-delineated_ sections are labeled by [outside color](#editing-delineations)

- _Unaffected paths_: This category corresponds to full paths that have no XY coordinates inside any delineation. _Unaffected paths_  retain their rendered colors

{% include notice icon="info" content="Topological constraints may not allow certain metrics to be computed for a particular delineation. E.g., a metric that requires a [graph-theoretic tree](./analysis#graph-based-analysis) may not be computed for a delineation defined by a non-contiguous ROI." %}
