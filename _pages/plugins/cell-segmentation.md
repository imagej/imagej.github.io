---
title: Cell Segmentation
categories: [Segmentation]
---

Cell Segmentation is a Fiji/ImageJ plugin for segmenting cells in RICM images.

The plugin can run fully automatically, while also providing optional interactive review steps for adjusting thresholds and detected ROIs when manual refinement is needed.

It supports:

- segmentation of single images and image stacks
- batch processing of multiple files or multi-series image containers
- optional threshold and ROI review
- watershed-based separation of touching cells
- measurement of accepted ROIs on the source image or a paired fluorescence image
- export of masks, label images, ROI sets, measurements, and segmentation parameters

The source code is available on [GitHub](https://github.com/will-f-dean-36/fiji-cell-segmentation).

## Installation

Cell Segmentation is available through the ImageJ update site:

- **Name:** `Cell Segmentation`
- **URL:** `https://sites.imagej.net/CellSegmentation/`

To install it:

1. Start Fiji.
2. Choose {% include bc path='Help | Update...' %}.
3. Click **Manage update sites**.
4. Click **Add update site**.
5. Enter `Cell Segmentation` as the name and `https://sites.imagej.net/CellSegmentation/` as the URL.
6. Enable the new update site.
7. Close the update-site window and click **Apply changes**.
8. Restart Fiji.

After installation, the plugin is available under:

{% include bc path='Plugins | Cell Segmentation' %}

with two commands:

- **Run on current image/stack...**
- **Run on multiple images...**

## Usage

### Current image or stack

Choose:

{% include bc path='Plugins | Cell Segmentation | Run on current image/stack...' %}

The active image can be either a single 2D image or a stack. When processing a stack, each slice is treated as an independent segmentation target.

The plugin provides settings for thresholding, object polarity, edge detection, minimum object area, border exclusion, and optional watershed segmentation.

### Batch processing

Choose:

{% include bc path='Plugins | Cell Segmentation | Run on multiple images...' %}

Batch mode supports several data organizations, including:

- lists of standalone RICM images
- multi-series RICM container files
- paired RICM and fluorescence files
- paired RICM and fluorescence containers
- multi-channel files containing both segmentation and measurement channels

When paired measurement images are supplied, ROIs segmented from the RICM image can be measured directly on the corresponding fluorescence image or channel.

## Interactive review

Two optional review steps are available.

### Threshold review

Threshold review pauses after edge detection and allows the segmentation threshold to be inspected or adjusted before segmentation continues.

### ROI review

ROI review displays the detected cells before they are accepted. ROIs can be:

- split
- merged
- deleted
- reset
- undone or redone

The segmentation can also be returned to the threshold-review step if the initial threshold needs to be changed.

Both review steps can be disabled for fully automatic processing.

## Outputs

Depending on the selected options, Cell Segmentation can produce:

- binary mask images
- label images
- label-overlay images
- ROI ZIP files
- measurement CSV files
- segmentation-parameter CSV files

Measurement options use standard ImageJ measurements such as area, mean intensity, perimeter, centroid, Feret diameter, shape descriptors, and integrated density.

## Source code

Development takes place on [GitHub](https://github.com/will-f-dean-36/fiji-cell-segmentation).