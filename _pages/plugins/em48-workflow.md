---
title: EM48 Workflow
description: Fiji workflow for Cellpose-SAM segmentation and EM48 puncta measurements in DAPI/NeuN/EM48 RGB overlays.
categories: [Segmentation]
---

EM48 Workflow is a Fiji plugin for the original DAPI/NeuN/EM48 RGB-overlay analysis workflow. It uses [Fiji-Cellpose](/plugins/fiji-cellpose) for nucleus segmentation, assigns EM48 puncta to nuclei, and exports measurements to Excel with supporting masks, ROIs and full-precision evidence.

[Download version 0.1.3](https://github.com/jadenjinnn/em48-fiji-workflow/releases/tag/v0.1.3) · [Project and installation guide](https://github.com/jadenjinnn/em48-fiji-workflow) · [Report an issue](https://github.com/jadenjinnn/em48-fiji-workflow/issues)

## Requirements and scope

- Fiji with Java 21 or newer.
- The **Fiji-Cellpose** and **ResultsToExcel** update sites, plus **Auto Local Threshold**.
- One 24-bit RGB overlay TIFF: DAPI in blue, NeuN in green and EM48 in red.

The workflow sets the scale to **0.16 micrometres per pixel** and retains the original filename-based worksheet routing. It is intended for that specific input and naming convention; other datasets require checking those assumptions before interpreting the measurements.

## Installation

Version 0.1.3 is currently distributed as a downloadable JAR. An EM48 update site is not yet available.

1. In Fiji, open **Help > Update... > Manage update sites**. Enable **Fiji-Cellpose** and **ResultsToExcel**, apply the changes, and restart Fiji. Make sure **Auto Local Threshold** is installed.
2. Download [EM48_Workflow-0.1.3.jar](https://github.com/jadenjinnn/em48-fiji-workflow/releases/download/v0.1.3/EM48_Workflow-0.1.3.jar).
3. Copy the JAR into Fiji's `plugins` folder. Remove any older EM48 Workflow JAR from that folder and restart Fiji.
4. The command is **Plugins > EM48 > EM48 Macro Compatibility Workflow**.

The release includes an installation guide and SHA-256 checksums. The first Cellpose call can download its Python environment and `cpsam_v2` model weights.

## Use

Save and close other images, and save/clear ROI Manager and Results before starting. Launch the workflow, choose the RGB TIFF and select an output directory. Avoid editing or closing its images during the run. Before another run in the same Fiji session, save/close the previous images and clear ROI Manager and Results.

The label-shuffling checkbox is unchecked by default, preserving the original Cellpose options and saved preference. The optional shuffle-disabled variant changes object order and can change order-dependent measurements.

Each run has its own output folder containing the three Excel workbooks, table evidence, masks and ROI ZIPs. Separate `diagnostics/diagnostics.json` and `diagnostics/diagnostics.log` files record stage timings, versions, memory observations, errors and the actual Cellpose device when observed.

## Compatibility and troubleshooting

Version 0.1.3 reduces repeated measurements and evidence-recording overhead while retaining the scientific settings and calculations. Validation covered three supplied images in the tested Fiji environment: 136 macro regression checks and 10 strict old/new output comparisons passed. This establishes compatibility with the original calculations for those cases, rather than biological validation of the formulas.

The workflow preserves the `torchversion=cpu` request. With the tested Fiji-Cellpose environment this uses CPU-only PyTorch on Windows/Linux, while supported Macs can use Apple MPS. A GPU request alone does not enable CUDA in a CPU-only environment. No minimum RAM requirement has been established for the complete workflow.

For a slow or failed run, retain the diagnostics files and the Fiji error message when reporting the issue. First-use environment setup, CPU inference and insufficient memory are different possible causes; a slow run alone does not identify which applies.
