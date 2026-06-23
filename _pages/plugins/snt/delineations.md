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
tags: snt,tracing,neuroanatomy,contours,labels,segmentation
---


{% capture version%}
**This page was last revised for [version 5.0.10](https://github.com/morphonets/SNT/releases)**.
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


## Creating Delineations from Label Images
Delineations can be imported from segmentation (label) images produced by tools such as [Labkit](/plugins/labkit), [Weka](/plugins/tws), [cellpose](https://cellpose.readthedocs.io/en/latest/), or similar. Each unique non-zero integer value in the label image becomes a delineation, with path nodes assigned to whichever label they overlap. To import:

1. Open the label image in Fiji. The image should contain non-negative integer pixel values, with 0 as background. Its spatial dimensions must match those of the tracing image

2. In the Delineations tab, choose _Import Assignments from Label Image_ from the Options (gear) menu

3. If multiple candidate images are open, a dialog allows you to choose which one to import. Hyperstacks are excluded; only the first channel/frame of multi-dimensional images is considered

Each label value is mapped to a new delineation entry. Path nodes whose coordinates fall within a labeled region are assigned to the corresponding delineation. Nodes outside all labels remain non-delineated.

{% capture label-validation %}
SNT validates the selected image before importing: it must contain only non-negative integers with a bounded number of unique classes (≤ 500). If the image dimensions do not match the tracing image, a warning is displayed. Nodes whose coordinates fall outside the label image bounds are skipped.
{% endcapture %}
{% include notice icon="info" content=label-validation %}


## Exporting Delineations as Label Images
Delineation assignments can be exported back to a label image using _Export Assignments to Label Image_ from the Options (gear) menu. This generates a new image in which each voxel within a traced neurite is labeled by its delineation assignment. The export uses tube-based rasterization, filling each path's volume based on node radii. Each delineation is assigned a unique positive integer label; background voxels remain zero. This is useful for visualizing delineation assignments in 3D, or for downstream analysis in other tools.

{% capture export-note %}
Export requires paths to have delineation assignments. If all assignments were made via ROIs or atlas annotations (rather than from a label image), the export still works: it rasterizes whatever assignments exist. The output is a 16-bit image; if there are more than 65,535 unique labels, values may overflow.
{% endcapture %}
{% include notice icon="info" content=export-note %}


## Editing Delineations
To re-define a delineation it is sufficient to re-define or re-adjust an existing ROI and press the _Assign_ button. The Options (gear) menu lists commands for rebuilding, restoring, and deleting delineations. Most of the editing operations can be performed through the toolbar at the bottom of the delineations list, including:
- <i class="fas fa-plus"></i> Adds more entries to the delineations list
- <i class="fas fa-object-group"></i> Merges two or more delineations into one
- <i class="fas fa-swatchbook"></i> Applies one of the default color schemes to the delineations list
- <i class="fas fa-pen"></i> Enables/Disables direct editing of delineation names
- _Non-delineating color_ widget: Defines the color for non-delineated sections, i.e., those sections that remain "outside" delineated areas


## Hierarchical Labels and Level-split Analysis

Delineation names support hierarchical labeling using the `::` separator. For example, naming three delineations `Cortex::L1`, `Cortex::L2/3`, and `Cortex::L5` encodes both the parent region (Cortex) and the individual layers. This convention is particularly useful for atlas-imported delineations, where compartments are naturally hierarchical.

When hierarchical labels are present, the _Measure_ and _Plot_ commands prompt for a **grouping level** before running the analysis. This allows measurements to be aggregated at different levels of granularity without redefining the delineations themselves. For example, with delineations named `Cortex::L1::proximal`, `Cortex::L1::distal`, and `Cortex::L2/3`:

- **Level 1** groups everything under `Cortex` into a single entry
- **Level 2** groups by layer (`Cortex::L1` combines proximal and distal; `Cortex::L2/3` remains separate)
- **Level 3 (full)** reports each delineation individually

The level-split prompt only appears when at least one delineation name contains the `::` separator. The _Non-delineated_ and _Unaffected paths_ categories always pass through unchanged regardless of the chosen level.


## Measuring Delineations

Measurements are retrieved using the <i class="fas fa-chart-bar"></i> _Plot_ and <i class="fas fa-table"></i> _Measure_ buttons:

- <i class="fas fa-chart-bar"></i> _Plot_: Plots distributions of selected metrics. Plotting styles include: Box plots (one delineation per category), multi-series histograms (one delineation per series), or a montage of single-series histograms (one panel per delineation)
- <i class="fas fa-table"></i> _Measure_: Reports common metrics to a dedicated table (Total length, No. of nodes, No. of junctions, etc.) across delineations. When delineations were imported from a label image, the table includes additional distance-to-boundary statistics computed via calibrated Euclidean Distance Transforms (EDT): _Mean dist. to boundary_, _Min dist. to boundary_, _Max dist. to boundary_, and _Fraction inside_ (the proportion of nodes with zero distance, i.e., fully contained within the label). These columns are only populated for label-image-based delineations

In addition to defined delineations, plots and tables may include two other categories:

- _Non-delineated_: This category corresponds to all the path sections that remained in-between or outside delineations. _Non-delineated_ sections are labeled with the [non-delineating color](#editing-delineations)

- _Unaffected paths_: This category corresponds to full paths that have no XY coordinates inside any delineation. _Unaffected paths_  retain their rendered colors

{% include notice icon="info" content="Topological constraints may not allow certain metrics to be computed for a particular delineation. E.g., a metric that requires a [graph-theoretic tree](./analysis#graph-based-analysis) may not be computed for a delineation defined by a non-contiguous ROI." %}

{% capture proximity-relation %}
Delineation analysis measures _aggregate_ properties of paths within labeled regions (lengths, node counts, distance statistics). To identify _specific contact points_ where paths approach or touch labeled structures, use the [Label Proximity Detector](/plugins/snt/spines-varicosities#label-proximity-detection), which emits navigable bookmarks or ROIs at individual contact locations.
{% endcapture %}
{% include notice icon="info" content=proximity-relation %}
