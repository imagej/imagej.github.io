---
title: 3D Objects Counter+
description: 3D object counting in Fiji/ImageJ with fixed min/max filters for morphology, volume, Feret diameter, and intensity.
categories: [Analysis, 3D, Particle Analysis]
source-url: https://github.com/Jay2owe/3DObjectsCounterPlus
update-site: 3DObjectsCounterPlus
release-version: 0.1.0
release-date: 2026-05-17
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: https://github.com/Jay2owe/3DObjectsCounterPlus/blob/main/LICENSE
license-label: BSD-3-Clause
---

3D Objects Counter+ is a Fiji/ImageJ plugin for counting and measuring thresholded 3D objects in image stacks. It extends the native [3D Objects Counter](/plugins/3d-objects-counter) workflow with fixed min/max filters for object shape, volume, surface area, Feret diameter, and intensity.

The plugin is designed for users who want the familiar threshold, size-filter, map, statistics, measurement redirect, and macro workflow of 3D Objects Counter, with additional morphology filters before the final maps and result tables are created.

## Installation

3D Objects Counter+ is distributed through the ImageJ update site:

{% include link-banner url="https://sites.imagej.net/3DObjectsCounterPlus/" %}

To install it:

1. Start Fiji.
2. Choose {% include bc path="Help|Update..." %}.
3. Click **Manage update sites**.
4. Click **Add Unlisted Site**, or enable **3DObjectsCounterPlus** if it is already listed.
5. Use:
   - Name: `3DObjectsCounterPlus`
   - URL: `https://sites.imagej.net/3DObjectsCounterPlus/`
6. Apply changes and restart Fiji.

After restart, run the command from:

```text
Analyze > 3D Objects Counter+
```

## Main Workflow

Open a 3D stack, then run **Analyze > 3D Objects Counter+**. The dialog opens with the title `3D Objects Counter+`.

The main controls are:

- `Image`, which shows the stack that will be counted.
- `Threshold`, which sets the voxel-intensity cutoff for object detection.
- `Slice`, which changes the displayed z-slice while checking the threshold.
- `Filters:`, which contains fixed `Min` and `Max` ranges.
- `Exclude objects on edges`, which removes objects touching the stack border.
- `Maps to show:`, with `Objects`, `Surfaces`, `Centroids`, and `Centers of mass`.
- `Results tables to show:`, with `Statistics` and `Summary`.
- `Redirect measurements to:`, which measures intensity from another open image while detecting objects from the active image.
- `Preview`, `OK`, and `Cancel` action buttons.

The help button opens `About 3D Objects Counter+ Controls`, which explains the dialog controls, filter meanings, maps, result tables, and action buttons.

## Threshold And Preview

The dialog starts on the center slice and uses a center-slice IsoData threshold as the initial value. Changing `Threshold` or `Slice` updates the threshold display so voxels at or above the threshold can be inspected before object counting is run.

`Preview` runs object counting with the current settings, shows the selected preview maps, and keeps the dialog open. Preview map windows are prefixed with `[Preview]`. `OK` runs object counting with the current settings, opens the selected final outputs, records macro options when the ImageJ macro recorder is active, and closes the dialog.

## Filters

Filters are fixed min/max ranges. The default ranges are non-excluding, so objects are only removed when a user tightens a minimum or maximum value.

The available filter rows are:

- `Size (Voxels)`, with default minimum `10` and maximum set to the stack voxel count.
- `Sphericity`, from `0` to `1`.
- `Compactness`, from `0` to `1`.
- `Elongation`, from `1` to `Infinity`.
- `Volume (<unit>^3)`, shown only when the image has calibrated spatial units.
- `Surface area`, from `0` to `Infinity`.
- `Mean intensity`, from `0` to `Infinity`.
- `Max intensity`, from `0` to `Infinity`.
- `Max Feret diameter`, from `0` to `Infinity`.

Multiple filters are combined with AND logic, so an object must pass every active range to remain in the final result.

## Measurement Redirect

`Redirect measurements to:` lets the active image define the detected objects while another open image supplies intensity measurements and intensity-weighted centers of mass. This is useful when object detection is performed on a mask, filtered stack, or segmentation image, while intensity should be measured from a raw channel.

The redirect image must already be open and must match the detection image width, height, and stack depth.

## Outputs

3D Objects Counter+ can create these map windows:

- `Objects map of <image>`, a labelled object map with object numbers at centroids.
- `Surfaces map of <image>`, a labelled surface-voxel map with object numbers at centroids.
- `Centroids map of <image>`, a point map at geometric centroids.
- `Centers of mass map of <image>`, a point map at intensity-weighted centers of mass.

It can also create:

- `Results for <image>`, a per-object statistics table.
- An ImageJ log summary reporting the threshold, size range, object count, and morphology means.

The statistics table includes native-style measurements such as integrated density, mean, standard deviation, minimum, maximum, centroids (`X`, `Y`, `Z`), centers of mass (`XM`, `YM`, `ZM`), bounding-box fields, object labels, and morphology columns such as `Morph_Sphericity`, `Morph_Compactness`, `Morph_Elongation`, and `Morph_Feret3D_um`.

For very high object counts, text-number overlays can be skipped to keep map windows lighter. The map pixel labels and statistics table are still produced.

## Supported Inputs

The interactive command works on the active Fiji/ImageJ image. It expects a non-empty image stack for 3D object counting. Standard Fiji installations provide the underlying ImageJ image model and the native 3D Objects Counter components used by the plugin.

Calibrated volume filtering appears when the image has real spatial calibration units rather than pixel-only units. Intensity filters and centers of mass are measured from the detection image unless a redirect image is selected.

## Macro Usage

3D Objects Counter+ is macro-recordable and can be called from ImageJ macros:

```ijm
run("3D Objects Counter+", "threshold=128");
```

A fuller call can combine thresholding, size limits, edge exclusion, measurement redirect, morphology filters, and output visibility:

```ijm
run("3D Objects Counter+",
    "threshold=128 min=20 max=Infinity " +
    "exclude_edges sphericity>=0.6 volume>=100 " +
    "redirect=[raw.tif] hide_surfaces hide_centroids");
```

Supported direct filter tokens include `volume`, `volume_calibrated`, `surface_area`, `sphericity`, `compactness`, `elongation`, `mean_intensity`, `max_intensity`, and `feret_diameter_max`. Supported operators are `>=`, `<=`, `>`, and `<`.

Output windows can be hidden with `hide_labels`, `hide_surfaces`, `hide_centroids`, `hide_centers_of_mass`, `hide_stats`, and `hide_summary`. The British spelling `hide_centres_of_mass` is also accepted.

## Java API

The public Java API lives under `sc.fiji.oc3dplus.api`. The main entry point is `OC3DPlus`, with parameters built through `OC3DPlusParameters` and results returned as `OC3DPlusResult`.

```java
OC3DPlusParameters params = OC3DPlus.builder()
    .threshold(128)
    .minSize(20)
    .addFilter("sphericity", ">=", 0.6)
    .build();

OC3DPlusResult result = OC3DPlus.count(imp, params);
```

The API can count one image or process lists of images without opening ImageJ result windows.

## Runtime Dependencies

The plugin requires Fiji/ImageJ and uses the standard Fiji 3D object-counting stack. The update site records dependencies on ImageJ, `mcib3d-core`, the native `3D_Objects_Counter`, and `Colocalization_Image_Creator`, so normal update-site installation resolves the runtime files.

## Citing

When publishing work that uses 3D Objects Counter+, cite the plugin using the citation metadata in the source repository. Please also cite the upstream tools it builds on: the original 3D Objects Counter work by Bolte and Cordelieres, and the mcib3d work by Ollion and colleagues.
