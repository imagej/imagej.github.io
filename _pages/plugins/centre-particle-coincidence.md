---
title: Centre-Particle Coincidence
description: Object-based colocalization from label images or ROI sets using centroid-in-object coincidence.
categories: [Analysis, Colocalization, Segmentation]
source-url: https://github.com/Jay2owe/CPC
update-site: Center-Particle-Coincidence
release-version: 1.3.0
release-date: 2026-05-05
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: /licensing/public-domain
license-label: CC0-1.0
---

Centre-Particle Coincidence (CPC) is an ImageJ/Fiji plugin for object-based colocalization analysis. CPC classifies segmented objects as coincident when their centroid falls inside a segmented object in another channel, and it also reports the reciprocal "contains" relationship: how many partner-object centroids fall inside each object. This keeps segmentation separate from colocalization, so objects can come from StarDist, Cellpose, thresholding, manual ROI sets, or any other workflow that produces label images or ROI `.zip` files.

## Installation

CPC is distributed through the ImageJ update site:

{% include link-banner url="https://sites.imagej.net/Center-Particle-Coincidence/" %}

To install it:

1. Start Fiji.
2. Choose {% include bc path="Help|Update..." %}.
3. Click **Manage update sites**.
4. Enable the **Centre-Particle Coincidence (CPC)** update site if it is listed, or click **Add Unlisted Site** and use:
   - Name: `Center-Particle-Coincidence`
   - URL: `https://sites.imagej.net/Center-Particle-Coincidence/`
5. Apply changes and restart Fiji.

After restart, run CPC from:

```text
Plugins > CPC
```

## What CPC Does

CPC compares segmented objects across 2 to 5 channels. For each object in a source label image, it reads the target label image at the source object's centroid position. If that position falls inside a target object, CPC reports the source object as coincident with that target object.

CPC also runs the reciprocal centroid test so users can see containment from the other direction:

- **Colocalized with B**: this A object's centroid lands inside a B object.
- **Contains B**: one or more B object centroids land inside this A object.

These results are not always symmetric. A small object can be colocalized with a large object without containing it, while a large object can contain several partner centroids even if its own centroid does not fall inside any one partner object.

## Inputs

CPC supports two input modes:

- **Label images**: 2 to 5 open or file-backed label/object maps. Each object is represented by a non-zero integer label.
- **ROI sets**: a reference image plus 2 to 5 ImageJ ROI `.zip` files.

If raw intensity images are available, CPC can use intensity-weighted centroids instead of geometric centroids. Raw images must match the dimensions of their corresponding label images.

## Outputs

CPC can produce:

- per-object pairwise result tables
- pairwise summary tables with counts and percentages
- bidirectional "colocalized" results and reciprocal "contains" counts
- multi-target combination summaries showing which target channels each source object coincides with
- optional centroid label maps for visual checking
- auto-saved output folders with CSV tables and map images

When auto-save is enabled, CPC writes results into a `CPC/` folder containing object tables, multi-target summaries, map images, and small README files describing the outputs.

## Batch Processing

The **Batch...** button opens a folder workflow for processing many label images. Batch mode supports recursive folder scanning, regular-expression grouping of filenames, group preview before running, and aggregated output tables across groups and folders.

## Method Notes

CPC is intentionally object-based rather than voxel-overlap-based. It answers two related questions: "Does this object's centroid fall inside an object in another channel?" and "Which partner centroids fall inside this object?" This makes it useful for workflows where channels are segmented independently, where objects differ in size, or where label images are produced by different segmentation tools.

Because CPC uses object centroids, users should inspect segmentation quality and choose geometric or intensity-weighted centroids according to the biology and image quality of the dataset.

## Citation

If you use CPC in published work, cite the software repository:

```text
Malcolm, J. (2026). CPC - Centre-Particle Coincidence (v1.3.0) [Software].
https://github.com/Jay2owe/CPC
```
