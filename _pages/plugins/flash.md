---
title: FLASH
description: Batch fluorescence microscopy analysis in Fiji with guided project setup, StarDist and Cellpose segmentation, spatial and morphometric analysis, statistics, presentation figures, and auditable outputs.
categories: [Analysis, Automation, Colocalization, Segmentation, Statistics]
source-url: https://github.com/Jay2owe/FLASH
update-site: FLASH
release-version: 5.0.0
release-date: 2026-07-20
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: https://github.com/Jay2owe/FLASH/blob/master/LICENSE
license-label: BSD-3-Clause
---

FLASH (Fluorescence Automated Spatial Histology) is an ImageJ/Fiji plugin for reproducible batch analysis of multi-channel fluorescence microscopy projects. It combines project and ROI setup, image preparation, classical and AI-powered segmentation, fluorescence intensity measurement, 3D object quantification, colocalisation, spatial and morphometric analysis, statistics, presentation-image export, and run records in one workflow.

FLASH is designed for projects containing many images, animals, regions, hemispheres, or experimental conditions that need the same analysis decisions and consistently organised outputs.

## Installation

FLASH is distributed through the ImageJ update site:

{% include link-banner url="https://sites.imagej.net/FLASH/" %}

To install it:

1. Start Fiji.
2. Choose {% include bc path="Help|Update..." %}.
3. Click **Manage update sites**.
4. Enable **FLASH** if it is listed, or click **Add Unlisted Site** and enter:
   - Name: `FLASH`
   - URL: `https://sites.imagej.net/FLASH/`
5. Apply changes and restart Fiji.

Open the pipeline with {% include bc path="Plugins|FLASH" %}. The installation also adds {% include bc path="Plugins|FLASH Runs..." %} for run history and {% include bc path="Help|About FLASH" %}.

## Projects and Main Window

FLASH opens at **FLASH Home**. Its **RECENT PROJECTS** panel shows previously opened projects, while **START SOMETHING** accepts a dropped project folder or offers **Browse for folder** and **+ New project**.

The **FLASH project** builder can assemble a project from multiple folders or individual files. It provides:

- **Project name** and an **Output root** that can differ from the source-image folder
- **Add folder...**, **Add files...**, **Open project...**, and **Open recent...**
- per-file and per-series inclusion, animal, hemisphere, region, condition, and notes fields
- additional condition axes such as genotype, timepoint, sex, or treatment
- roster import/export, naming-grammar editing, identity inference, and review of low-confidence metadata
- **Save & Open** to write the project manifest and enter the pipeline

The main window is titled **FLASH - The Pipeline for Fluorescence Automated Spatial Histology**. Its **Quick start** panel says **Pick a recipe or tick analyses individually.** Built-in buttons include:

- **Standard 3D + Intensity**
- **Quick cell count**
- **Full pipeline**
- **Presentation**
- **Fast Presentable Results**
- **Last run**
- **Clear Recipe**
- **Save selection as recipe...**

The top panel also shows **Current Project** with **Change project...** and **Edit setup...**, plus **Conditions** with **Review conditions...**.

The visible analysis rows are grouped as follows:

- **Setup**: **Set Up Configuration**; **Draw ROIs and Orientate Images**
- **Image Preparation**: **3D Deconvolution**; **Spectral Decontamination (Experimental)**
- **Display**: **Make Presentation Images**; **Make Representative Image Figure**
- **Image Analysis**: **Fluorescence Intensity Analysis**; **3D Object Analysis**; **Spatial Analysis**
- **Results and Validation**: **Combine results per condition / animal**; **Statistical Analysis**; **Excel Summary Export**

Each row has a status indicator and a help button. The footer contains **Check my data**, **Options**, and **Dependencies**; the primary **Run** button starts the selected modules.

## Guided Setup and Preview

**Set Up Configuration** defines the channel configuration reused by downstream analyses. It records channel identity and colour, filters, display ranges, intensity and object thresholds, object-size limits, segmentation engines, and optional Z-slice selections.

The main configuration is stored at:

```text
FLASH/Config/.settings/channel_config.json
```

`Channel_Data.txt` in the same folder is a derived compatibility file. Incomplete setup can be resumed, and cancellation offers **Save & Exit**, **Keep Working**, or **Discard & Exit** so partial work is not silently lost.

Representative setup images can be chosen manually, randomly, by **Min and max overall**, or by **Min and max per condition**. The per-condition option samples image intensity and selects weak and bright examples within every condition, helping users check thresholds and display ranges against both ends of each condition's data before batch processing.

Setup quality control uses an embedded FLASH preview with the source image above the adjusted or output image. **Large view** opens a larger comparison where useful. Display-range and threshold changes update live; filter, StarDist, Cellpose, deconvolution, and 3D-object previews rerun from explicit preview buttons.

Depending on the selected settings, setup reviews include filter parameters, display min/max, intensity and object thresholds, particle-size filtering, deconvolution, and the selected segmentation engine. **Parameter Variations...** can render comparison grids for supported filter, deconvolution, classical, StarDist, and Cellpose settings before a parameter set is accepted.

## Filters and Macro Building

FLASH includes preset filters for common fluorescence-image problems:

- **Default**
- **Punctate Signal / High Background**
- **Ramified Cells (Microglia/Astrocytes)**
- **Clustered Small**
- **Clustered Large**
- **Overlapping Cellular Marker**
- **Puncta Resolve**
- **Diffuse Object**
- **Custom**

When **Custom** is selected, users can choose:

- **Build it step-by-step**
- **Record what I do in Fiji**
- **Import an existing macro file**

The visual filter builder exposes **Available steps**, **Your filter**, **Step settings**, and **Merge branches**, with support for parallel branches. **Start from a preset...**, **Preview up to selected step**, and **Preview full filter** help users build and inspect the chain on an actual project image.

Custom filters are saved as an ImageJ macro (`.ijm`) and, for visual graphs, a `.dag.json` sidecar so the graph can be reopened and edited. Custom filter presets can be reused in later setup runs.

## Segmentation Engines

Different channels in one project can use different segmentation engines. For example, a nuclear channel can use StarDist while a whole-cell or ramified marker uses Cellpose, with both label outputs feeding the same object, colocalisation, spatial, aggregation, and export steps.

The setup UI supports:

- **Classical**: filter, threshold, and size-based segmentation
- **Enhanced Classical**: classical segmentation with additional 3D object filtering
- **StarDist 3D**: StarDist detection applied in 2D per slice and linked through Z to produce 3D labels
- **Cellpose**: Python Cellpose segmentation with model, diameter, probability, flow, companion-channel, GPU, and size controls

The normal setup UI can register project-specific models through the **Custom Model Manager**. StarDist imports must be Fiji-compatible TensorFlow SavedModel `.zip` exports. Cellpose can use supported model files or registered model names.

FLASH v5 pins Cellpose `3.1.1.2`; Cellpose 4, Cellpose-SAM, and `cpsam` models are not supported. The click-training route is hidden while that workflow is being redesigned, so the normal setup UI does not collect preview clicks or offer click-derived parameter suggestions.

Project model files and metadata are stored under:

```text
FLASH/Config/Segmentation models/
```

## Parallel Batch Processing

FLASH applies a saved project configuration across many images rather than requiring one-image-at-a-time setup. **Pipeline Options** exposes:

- **Parallel Processing**
- **Thread Count**
- **GPU Inference Permits (0 = auto-detect)**
- **Cache Images as TIFs**
- **File Overwrite Behavior**: **Auto-Overwrite** or **Skip Existing**
- **Auto-Save Aggregated Summaries**
- **Generate QC Report**

Parallel execution uses memory-aware worker sizing, bounded image-loading queues, and nested-parallelism checks. StarDist and Cellpose share the GPU inference permit limit so simultaneous deep-learning jobs do not exceed the configured concurrency. Auto-detection considers GPU memory, Java heap, and system RAM.

The TIF cache is stored under `FLASH/Cache/TIF/`, allowing repeated analyses of large Bio-Formats containers to reuse extracted image data.

## ROIs, Orientation, and Image Preparation

**Draw ROIs and Orientate Images** opens each image with ROI drawing plus rotate and flip controls. ROI sets, ROI metadata, and saved orientation transforms are reused by later analyses and ROI reruns. The workflow can also save named anatomical reference lines for optional distance measurements in **Spatial Analysis**.

**3D Deconvolution** can sharpen Z-stacks before segmentation or intensity measurement. Its setup covers engine choice, PSF source, microscope metadata, channel wavelengths, Z spacing, iterations, regularisation, preview, and caching. Available engines depend on the Fiji installation and can include CLIJ2 FFT, DeconvolutionLab2, and Iterative Deconvolve 3D, with EPFL PSF generation where installed.

**Spectral Decontamination (Experimental)** supports bleed-through and autofluorescence correction workflows. It can write corrected images, masks, fitted coefficients, parameter maps, object scores, configuration and summary tables, and QC previews.

## Presentation Images and Representative Figures

**Make Presentation Images** is the display-export workflow. It can apply saved LUTs and display ranges, create split channels and merged composites, annotate images, tile outputs, and write OME-TIFF files. These outputs are intended for visual review and figure preparation; contrast changes are not substituted into quantitative measurements.

**Make Representative Image Figure** creates condition-aware image figures through the visible stages **Statistic**, **Conditions**, **Select Images**, **Display Ranges**, **Layout**, and **Build**. Image selection can use:

- **Quick**: brightest 1% mean per channel
- **Existing result**: a numeric column from an existing result CSV
- **None**: manual selection without a guiding statistic

Users can choose one image series per condition, review display ranges, arrange conditions and channel tiles, add annotations, set output DPI, and preview the final layout. The workflow writes a full-resolution PNG plus the selected individual channel/merge PNGs and original TIFFs under `FLASH/Results/Presentation Images/Representative Figures/`.

## Intensity and 3D Object Analysis

**Fluorescence Intensity Analysis** measures fluorescence inside saved ROIs or channel-derived masks. It supports whole-ROI mean signal, thresholded positive signal, percent area, integrated density, raw integrated density, and intensity restricted by another channel. Per-channel tables are written under:

```text
FLASH/Results/Tables/Intensity/
```

**3D Object Analysis** segments, counts, and measures objects using the configured engine for each channel. Outputs can include object tables, calibrated centroids and coordinates, volumes and shape measurements, label images, masks, segmentation comparisons, redirected intensity values, process-length results, and analysis details.

Cross-channel measurements include volumetric overlap, centroid coincidence (CPC), intensity colocalisation, and optional bounding-box overlap or centroid measures.

The **Object Intensity Profiling** controls can measure how partner-channel signal is distributed within or around every object using:

- **Radial profile (distance from centre)**
- **Marginal X / Y / Z profile (image axes)**
- **Principal-axis profile (object's own axes)**
- **Angular profile (ring completeness)**
- **Concentric-shell coloc (inner/mid/outer)**
- **Within-box correlation (Pearson / overlap)**

Profile tables are written to `FLASH/Results/Tables/Object Intensity Profiling/`; aggregate profile figures are written to `FLASH/Results/Analysis Images/Object Intensity Profiling/` when enabled.

## Spatial, Morphometric, and Texture Analysis

**Spatial Analysis** works from existing object CSVs and label images rather than rerunning segmentation. It can add:

- nearest-neighbour distances and closest-object identities between channel pairs
- Ripley's K/L/G statistics
- CPC summaries and multi-target spatial summaries
- Voronoi territories and interaction matrices
- spatial heatmaps
- population phenotyping
- 2D and 3D morphometry, protrusion descriptors, and spatial-morphometric indices
- distance from objects to named anatomical reference lines

The **Object Texture and Complexity** section adds per-object measurements from the raw signal and existing label maps:

- **Object texture (GLCM; slow)**
- **Object complexity (fractal + lacunarity; slow)**
- **Object texture classes (slow)**
- **Native-3D texture (GLCM + texture classes; very slow)**

Results are added to the per-channel object CSVs using `Morph_` and `MorphTexture_` columns. Spatial tables, morphometry details, heatmaps, and updated object tables are organised under `FLASH/Results/Tables/` and `FLASH/Results/Analysis Images/`.

## Aggregation, Statistics, and Excel Export

**Combine results per condition / animal** combines per-image and per-ROI tables into project summaries. It supports grouping by animal, condition, hemisphere, region, section, ROI, or image, with raw and per-volume outputs where the required ROI volume data exist.

The project-level files are written under `FLASH/Results/Tables/Project Summary/`, including:

```text
3D Objects.csv
Image Intensities.csv
Image Intensities_MIP.csv
Image Intensities_3D.csv
Conditions.csv
Statistics.csv
```

**Statistical Analysis** runs configured independent or paired group comparisons from the project summary tables. It supports automatic distribution routing, forced parametric or non-parametric analysis, multiple-group post-hoc tests, adjusted p-values, and recorded skip reasons for metrics without sufficient usable data.

**Excel Summary Export** packages the existing project summaries, conditions, optional statistics, and analysis details into:

```text
FLASH/Results/Summary.xlsx
```

Depending on the selected export preset, the workbook can contain experimental conditions, data summaries, raw and summary metric sheets, statistics, and a methods appendix. Export does not rerun segmentation, measurement, aggregation, or statistical testing.

## Run Records, Quality Control, and Outputs

FLASH writes a start page at `FLASH/Results/START_HERE.html` and, when enabled, an HTML quality-control report at `FLASH/Results/QC/QC_Report.html`. QC content can include global settings, per-analysis parameters, segmentation overlays, deconvolution checks, and spectral previews.

Each analysis run records its settings, inputs, outputs, status, timing, and FLASH version under `FLASH/Results/Run Records/`. {% include bc path="Plugins|FLASH Runs..." %} opens **FLASH Runs**, where runs can be filtered by analysis, status, or date. Available actions include **Open output folder**, **View settings...**, **Reproduce verbatim**, and **Diff with parent**. Reproduced runs write to separate replay workspaces instead of overwriting the original output tree.

The main output layout is:

```text
Project/
|-- input images
`-- FLASH/
    |-- Config/
    |   |-- .settings/
    |   |   |-- project.json
    |   |   |-- channel_config.json
    |   |   `-- Channel_Data.txt
    |   `-- Segmentation models/
    |-- Results/
    |   |-- START_HERE.html
    |   |-- Summary.xlsx
    |   |-- Tables/
    |   |-- Presentation Images/
    |   |-- Analysis Images/
    |   |-- QC/
    |   `-- Run Records/
    |-- .settings/
    |   |-- Presets/
    |   `-- status.json
    `-- Cache/
        `-- TIF/
```

Typical outputs include configuration JSON, filter macros and graph sidecars, ROI sets, orientation metadata, CSV tables, label images and masks, presentation PNGs and OME-TIFFs, representative figures, deconvolved or decontaminated images, heatmaps, profile figures, quality-control reports, run records, replay workspaces, and the Excel summary workbook.

## Supported Inputs

FLASH is designed for multi-channel fluorescence microscopy projects. It uses Fiji and Bio-Formats for common microscopy containers and TIFF workflows, including:

- Leica LIF
- Zeiss CZI
- Nikon ND2
- OME-TIFF and TIFF stacks

Project metadata can come from filenames, source folders, image metadata, project-table edits, naming grammars, or imported rosters.

## Runtime Dependencies

FLASH opens even when optional dependencies are missing. Features that need them show a dependency message and repair guidance when used.

The main-window **Dependencies** button opens **Pipeline Dependencies**, which checks each runtime and identifies the affected features. Depending on the selected workflow, optional runtimes can include Bio-Formats, 3D Objects Counter, 3D Objects Counter+, mcib3d, StarDist/TrackMate, TensorFlow native libraries, Cellpose, Apache POI, JTS, Coloc 2, deconvolution engines, PSF Generator, and supporting image-processing libraries.

## Macro and Headless Use

FLASH can be driven from ImageJ macros and headless workflows after a project configuration exists. For example:

```ijm
run("FLASH", "dir=[/path/to/project] run_3d run_intensity run_aggregate run_excel");
```

CLI options can select analyses and control parallel processing, thread count, caching, overwrite behaviour, presets, aggregation, statistics, Excel export, and saved representative-figure rerendering. Interactive setup itself requires the GUI unless a setup preset or explicit channel options are supplied.
