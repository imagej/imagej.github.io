---
title: AnDi-J › Input data
name: AnDi-J
icon: /media/plugins/andi-j/logo.png
description: The CSV layout AnDi-J expects, and how to load and group trajectories with the Data Manager.
nav-title: Input data
nav-links:
- title: Overview
  url: /plugins/andi-j
- title: Input data
  url: /plugins/andi-j/input-data
- title: Trajectory Analysis
  url: /plugins/andi-j/trajectory-analysis
- title: Trajectory Segmentation
  url: /plugins/andi-j/trajectory-segmentation
- title: ML models
  url: /plugins/andi-j/ml-models
---

AnDi-J takes as input `.csv` files containing the trajectories of a given experiment. To ease integration with existing tools, the expected `.csv` must follow the standard layout of a [TrackMate](/plugins/trackmate) output: a header row, three further description/units rows, then one row per spot. The required columns are:

| Column | Meaning |
|---|---|
| `TRACK_ID` | trajectory identifier |
| `POSITION_X`, `POSITION_Y` | spot coordinates |
| `FRAME` | frame index |
| `POSITION_T` | time (used to estimate the frame interval) |

Spots are grouped by `TRACK_ID` and sorted by frame; gaps in `FRAME` are handled where relevant (e.g. MSD and eMSD lookups are gap-aware).

{% include notice icon="info" content="
**Generating test data.** The [`pythons_helpers`](https://github.com/gorkamunoz/andi-j/tree/main/utils/pythons_helpers) folder of the repository provides scripts that use Python and the [`andi_datasets`](https://github.com/AnDiChallenge/andi_datasets) library to produce example test `csv` files.
" %}

## Data Manager

The Data Manager is an independent window that lets you select the data to be processed by the plugin. [Trajectory Analysis](/plugins/andi-j/trajectory-analysis) and [Trajectory Segmentation](/plugins/andi-j/trajectory-segmentation) have a similar Data Manager, although each opens in its own window.

### Loading trajectories

This part of the manager is the same for both Trajectory Analysis and Trajectory Segmentation.

*   **Load as Separate / Merge** — whether the chosen files are merged into a single experiment for analysis or loaded as separate ones. Only applies if more than one file is selected.
*   **Choose Files…** — choose the CSV files (multi-select allowed).
*   **Tag** — the name by which the experiment will be tagged in the analysis. If left blank, the tag is set to the file name.
*   **Cut length** — per-file trajectory-length filter: trajectories shorter than *N* are dropped, longer ones are truncated to the first *N* points.
*   The table shows, per file: colour, tag, file name, number of trajectories, min/max trajectory length, and cut length. **Tag and cut length are editable.**
*   **Perform Analysis** — assembles the experiments and opens the analysis window. For Trajectory Analysis this is almost instantaneous. For Trajectory Segmentation, the ML models that predict the per-frame properties are run at this point, so it takes longer; see [Selecting the segmentation model](#selecting-the-segmentation-model) below for details.

The Data Manager can be accessed at any time during analysis, allowing you to add or remove experiments at will.

{% include img align="center" name="Data Manager" src="/media/plugins/andi-j/data-manager.png" caption="**Data Manager.** Three test experiments loaded as separate ones, then the same three loaded again as a merged experiment with a cut length of 10. The latter appears as a single experiment in the analysis." %}

## Selecting the segmentation model

This part of the manager exists only in [Trajectory Segmentation](/plugins/andi-j/trajectory-segmentation). By default a pre-trained model is already selected, so the analysis can be run as is.

*   **TTA** enables *test-time augmentation*: instead of a single prediction, the model is run on 8 symmetry transformations of each trajectory and the results are averaged. This typically gives a more stable prediction, at the cost of roughly 8× the compute time.
*   You can also **load your own models** for the predictions, either one model producing all outputs or one model per output. See [Custom models for Trajectory Segmentation](/plugins/andi-j/ml-models#custom-models-for-trajectory-segmentation) for the input/output contract your model must follow.

As a reference for runtime, the bundled default model with TTA off processes 500 trajectories of 200 frames in about 30 s on a laptop CPU (Intel Core i7-1165G7, 4 cores / 8 threads, no GPU). Inference uses all available cores. The current release runs entirely on CPU; GPU support is planned for a future release.

{% include img align="center" name="ML model options" src="/media/plugins/andi-j/data-manager-ml.png" caption="**ML model options** in the Trajectory Segmentation Data Manager." %}
