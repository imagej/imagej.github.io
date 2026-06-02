---
title: SNT › Seeded Tracing
nav-links: true
nav-title: Seeded Tracing
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
extensions: ["mathjax"]

tags: snt,seeds,points,neuroanatomy,deep-learning,segmentation,ground-truth
---

{% capture version%}
**This page was last revised for [version 5.1.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

Seeded Tracing allows for anchoring/constraining tracing algorithms around key locations ([machine learning predictions](./machine-learning#deep-learning), soma locations, neurite endpoints, manual annotations, etc.). A **seed** is a 3D point that carries a position, a confidence score, and a few optional attributes (radius, type, source, channel, frame). Seeds are overlaid on the image using a dedicated renderer, and do not affect other overlaid objects like paths or ROIs. Common sources of seeds include:

- **Deep-learning detectors** that output candidate soma/endpoint coordinates (see [Machine Learning](./machine-learning))
- **Labels/segmentation images** e.g., from [cellpose](https://www.cellpose.org/), [Stardist](https://stardist.net/), [Labkit](../labkit), or [TWS](../tws), where each label/connected component yields one seed (e.g., cellpose masks can be used to specify the soma locations when autotracing [multiple cells](./auto-tracing#multiple-cells))
- **ROIs** e.g., generated from ImageJ routines (area and line ROIs are reduced to representative points)
- **Tabular data** (CSV) exported from external tools or scripts


# Seeded Tracing Assistant
{% include img src="/media/plugins/snt/snt-seeded-tracing-assistant.png" align="right" width="350px" %}

The _Seeded Tracing Assistant_ is one of the main tabs in the [Main Dialog](./manual#main-dialog) and manages seeds. It is organized into four sections: a display toolbar, a confidence filter, a table of all loaded seeds, and a bottom toolbar for [import](#importing-seeds), [export](#exporting-seeds), and [autotrace](#auto-tracing-from-seeds) actions.

## Display toolbar
Controls how seeds are rendered on the tracing canvas, and includes:

- **Show/hide seeds** toggle button for the visibility of the whole seed overlay
- **Color table controls** set the lookup table (LUT), transparency, and the _Color mode_ that drives the LUT mapping:
  - _Confidence_: LUT sampled by the seed's confidence within the active filter window
  - _Index_: One distinct LUT slot per seed. This allows seeds to be rendered with unique colors under the _Distinct/Glasbey_ lookup table
  - _Type_/_Source_: Seeds are color-coded by _type_ or _source_

## Confidence Filtering

Two sliders set the inclusive $$[low, high]$$ confidence range. Seeds outside the range are hidden in both the canvas overlay and the table view; they remain in the underlying data and can be brought back by widening the range. The label beneath the sliders reports how many seeds are currently being filtered.

## Seeds Table

Each row lists a seed. Selecting rows in the table also selects the corresponding seeds on the canvas (and vice versa). The table is organized as follows:

| Column         | Meaning                                                                |
|----------------|------------------------------------------------------------------------|
| **X, Y, Z**    | Position in physical (calibrated) coordinates                          |
| **Confidence** | Score in $$[0, 1]$$. Drives the color mapping and the confidence-range filter |
| **Radius**     | Optional sphere radius (physical units). Zero for point-only seeds     |
| **Type**       | Free-form category (e.g., _soma_, _endpoint_, _waypoint_)              |
| **Source**     | Where this seed came from (e.g., _roi_, _labels-image:cellpose.tif_)   |
| **Status**     | Coverage indicator (see below). Only present when SNT has tracing data |

- **{% include key keys='Double Click' %}** a row to navigate the canvas to that seed (channel/frame are honored when set; otherwise the active C/T is used). The _Visiting zoom level_ spinner on the bottom toolbar controls the zoom level applied during the go-to
- **{% include key keys='Right Click' %}** for selection and editing controls. Choose _Detach_ to move the table into its own window for a larger working area
- **Sort** by clicking column headers; the confidence filter survives across sorts

{% capture tipseed1%}
When tracing is paused, {% include key keys='Alt|Left Click' %} on a seed marker to edit it.
{% endcapture %}
{% include notice icon="tip" content=tipseed1 %}


# Importing Seeds

{% capture tipseed2%}
Seeds can be imported by drag-and-drop. The following files are supported: [.csv](#from-csv-file), [.roi/.zip](#from-rois), and [.tif](#from-labelsmasks-image)
{% endcapture %}
{% include notice icon="tip" content=tipseed2 %}

## From CSV File
{% include bc path='Import|From CSV File...' %}

SNT reads a comma- or tab-separated table with a header row, with the following required columns (case-insensitive, whitespace-tolerant): `x`, `y`, `z`, `confidence`, `radius`. Optional columns include: `channel`, `frame`, `type`, `source`. Defaults are applied when absent.

**NB**: Voxel-indexed inputs can be converted to physical (spatially-calibrated) location at import time using the image's spacing

## From Labels/Masks Image
{% include bc path='Import|From Labels/Masks Image...' %}

The program will parse a labels/mask image (produced e.g., by cellpose, Stardist, [Labkit or TWS](./machine-learning#embedded-tools-labkit--tws)), and extract one seed per non-zero label. For each label, SNT computes:
- **Centroid** in physical coordinates
- **Radius** from the sphere whose volume equals the label's total volume: $$r = \sqrt[3]{\frac{3V}{4\pi}}$$
- **Confidence** linearly interpolated between _minConfidence_ (smallest label) and $$1.0$$ (largest). In the case of e.g., a cellpose mask: the label with the smallest volume would be assigned the lowest confidence, the largest, the highest confidence

**NB**: If the chosen image is a binary mask, one-seed-per-label would collapse the whole foreground into a single seed. SNT detects this case and offers to run a connected-components analysis first (8-connectivity in 2D, 26-connectivity in 3D), label each distinct object, and proceed with the labeled image.


## From ROIs
{% include bc path='Import|From ROI Manager...' %}

SNT will parse all the ROIs stored in the ROI Manager, using the following criteria:

- **Area ROIs** (oval, polygon, rectangle, freehand, traced): centroid as position; radius from the matched-area disk: $$r = \sqrt{\frac{A}{\pi}}$$)
- **Line ROIs** (straight): midpoint as position; radius is half the path length. **Polylines / freelines**: vertex centroid; radius is half the summed segment length
- **Point ROIs**: each contained point becomes its own seed (without radius)
- **Other geometries** (angle, composite): bounds-center position, no radius

**NB**: Channel and frame come from the ROI's hyperstack position when set, otherwise from the image's active C/T. When importing ROIs, it is possible to set their seeds _type_ and _confidence_ value (default 1.0).

## From Workspace
{% include bc path='Import|From Workspace...' %}

This option loads a previously-exported `seeds.csv` directly from the current [SNT session directory](./manual#save-session). Useful for quickly restoring seeds across SNT restarts.

# Exporting Seeds

## To CSV File
{% include bc path='Export|To CSV File...' %}

This option exports all seeds to a CSV file with the same column layout used by the [importer](#from-csv-file).

## To ROI Manager
{% include bc path='Export|To ROI Manager...' %}

Converts seeds to ImageJ ROIs. Seeds with set radius become circles of diameter $$2r$$; seeds without radius become point ROIs. By default, selected seeds in the table are exported; if no rows are selected, all seeds are converted. Note that Seed → ROI conversion is lossy since ROIs have no awareness of _confidence_, _type_, or _source_.


## To Workspace
{% include bc path='Export|To Workspace...' %}

Writes all seeds to a  _seeds.csv_ file into the current session directory. The counterpart [From Workspace](#from-workspace) reloads from the same location.

# Auto-tracing From Seeds
Seeds can drive automated tracing in different ways, accessible through the auto-trace dropdown on the bottom toolbar.
The naming convention pairs the algorithmic role with its biological interpretation: _Roots_ → _Somata_; _Endpoints_ → _Tips; _Waypoints_ → _Path Attractors_. All tracing commands inherit the paramaters documented under [Grayscale](./auto-tracing#grayscale-images)/ [Segmented](./auto-tracing#segmented-images) -image autotracing: Only the seed-related parameters and the role the seeds play differ.

## Seeds as Roots / Somata
{% include bc path='Run Auto-Tracers|Grayscale Image (One Tree per Seed)...' %}

Each filtered seed becomes the root of its own auto-trace; the soma-detection strategy of the autotraced is bypassed because the seed _is_ the root. The command iterates one tracer run per seed and aggregates the resulting trees into a forest: one tree per seed.
Failures (unreachable seeds, seeds in background, etc.) are logged to the Console but don't abort the run.

The seed source filter (_Visible_/_All_/_Selection only_) and type filter allow you to restrict the per-seed loop to a subset.
When invoked from rows selected, the source filter is pre-targeted to _Selection only_.

## Seeds as Endpoints / Tips

{% include bc path='Run Auto-Tracers|Grayscale Image (Single Cell)...' %}

In this modality filtered seeds become tip targets. The autotracer runs detection from the soma exactly once, then extracts the shortest path from each tip back to the root via the parent-pointer field. This is equivalent to the A* shortest-path tracing that SNT uses for interactive endpoint clicking, but batched over the entire seed set.
The output is **one tree** connecting the soma to every reachable tip; tips that fall outside the foreground or outside the image bounds are logged and skipped.

Since seeded tips are by definition the desired endpoints, auto-traces do not perform any hierarchical pruning.

## Seeds as Waypoints / Path Attractors

{% include bc path='Run Auto-Tracers|Grayscale Image (Single Cell, Constrained)...' %}

In this modality filtered seeds act as _soft attractors_: the cost map used by the auto-tracer is locally biased toward each waypoint voxel, so the resulting tree preferentially routes paths through (or near) the seeds. The root-to-waypoint paths are then protected from the standard pruning passes, ensuring the biased branches survive into the final tree.

The prompt exposes three bias controls:

- **Bias source**: _From confidence_ (default: each seed's confidence value scales its attraction), _From radius_ (radius normalized across the waypoint set), or _Uniform_ (fixed factor)

- **Bias strength**: overall multiplier in `[0, 1]`. The default `0.9` means a confidence-1 seed is pulled almost all the way to a zero-cost voxel

- **Bias sphere radius (voxels)**: spatial extent of the bias around each waypoint. A small sphere (2–3 voxels) is usually enough; larger values may create phantom attractors at the bias boundary in low-contrast images

{% capture wpnote %}
The bias is a _hint_, not a hard constraint. If the surrounding terrain provides a much cheaper path that bypasses the waypoint, the trace can still detour around it. For stricter "must visit this point" semantics, use the [Tips](#seeds-as-endpoints--tips) command instead.
{% endcapture %}
{% include notice icon="info" content=wpnote %}

# Seeds as a Review Tool
In this modality, seeds are converted into _Review locations_ and sent to the [Curation Assistant](./curation#seed-review) for inspection. Useful for quality assessment of existing reconstructions, and for closing the loop with QC-classifier training data: each location can be tagged _accept_ / _reject_ / _unsure_ and exported as labels for the next training round.

# Scripting
The seed overlay is accessible from [scripts](./scripting) via `snt.getSeedOverlay()`.
The same operations available in the GUI (add, remove, filter, change colors, run autotracers with seeds in different roles) can be performed programmatically.
