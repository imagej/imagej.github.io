---
title: 3D Objects Counter - StarDist
description: StarDist-powered detection and 3D measurement of touching objects in Z-stacks by linking slice-wise detections through Z.
categories: [Analysis, 3D, Segmentation, Machine Learning]
source-url: https://github.com/Jay2owe/3DObjectsCounter-StarDist
update-site: 3DObjectsCounter-StarDist
release-version: 0.1.0
release-date: 2026-08-06
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: https://github.com/Jay2owe/3DObjectsCounter-StarDist/blob/main/LICENSE
license-label: GPL-3.0-or-later
---

3D Objects Counter - StarDist offers StarDist-powered 3D object analysis for images where conventional thresholding can merge touching objects. [StarDist](/plugins/stardist) detects objects independently on each Z slice, [TrackMate](/plugins/trackmate) links them into complete 3D objects, and the plugin generates measurements, label images, visual maps, and reproducible batch outputs.

## Installation

3D Objects Counter - StarDist is distributed through the ImageJ update site:

{% include link-banner url="https://sites.imagej.net/3DObjectsCounter-StarDist/" %}

To install it:

1. Start Fiji.
2. Choose {% include bc path="Help|Update..." %}.
3. Click **Manage update sites**.
4. Enable **3DObjectsCounter-StarDist** if it is listed, or click **Add Unlisted Site** and use:
   - Name: `3DObjectsCounter-StarDist`
   - URL: `https://sites.imagej.net/3DObjectsCounter-StarDist/`
5. Apply changes and restart Fiji.
6. Run {% include bc path="Analyze|3D Objects Counter - StarDist" %}.

### First-run runtime setup

StarDist detection requires TrackMate, TrackMate-StarDist, StarDist, CSBDeep, and TensorFlow components. If the tested runtime is missing or incompatible, the plugin opens **Install StarDist runtime**. Click **Install Runtime** to download and verify the known-working versions, then restart Fiji and run the command again.

A completely missing runtime is about 159 MB. Conflicting JARs are renamed with a dated `.disabled` suffix rather than deleted, and Fiji is not restarted automatically.

## How the 3D objects are built

The Fiji StarDist detector is two-dimensional. This plugin therefore runs StarDist independently on every Z slice and uses TrackMate's LAP tracker to link detections through Z. Each linked chain becomes one labelled 3D object whose measurements are calculated from the resulting 3D label image.

This approach is designed for objects that overlap themselves between adjacent slices and is particularly useful when touching objects are separated by StarDist but would merge under intensity thresholding. It is not native 3D StarDist segmentation. Strongly concave objects, coarse Z spacing, or objects that also touch in Z can require careful linking settings.

The output reports how many objects occupy only one slice and how many short objects were rejected by **Min. slices per object**, making weak Z-linking visible rather than hiding it in the final count.

## Main workflow

Open a stack with at least two Z slices and run {% include bc path="Analyze|3D Objects Counter - StarDist" %}. The dialog is divided into **Input**, **Detection**, **Linking through Z**, **Filters**, and **Output**.

### Input

- **Channel** selects the channel analysed in a multichannel image.
- **Redirect intensities from** optionally uses another open image for intensity measurements and intensity-weighted centres of mass. `None` measures the analysed image itself. A redirect image must match the width, height, and Z depth of the analysed stack.

### Detection

- **Model** accepts `versatile_fluo`, the bundled versatile fluorescence model, or the full path to a compatible custom StarDist `.zip` model.
- **Probability** controls the minimum detection confidence.
- **Overlap (NMS)** controls non-maximum suppression of overlapping StarDist detections.

### Linking through Z

- **Linking max distance** is the greatest allowed movement between detections on consecutive slices.
- **Gap closing max distance** controls linking across missing detections.
- **Max slice gap** sets the number of missing slices that may be bridged.
- **Min. slices per object** rejects linked objects that span too few slices.

Distances use the image's calibrated spatial unit when calibration is available; otherwise they are measured in pixels. The dialog also shows the linking distance in pixels for calibrated images.

### Filters

- **Min size (voxels)** and **Max size (voxels)** set the accepted object-size range.
- **Exclude objects on edges** removes objects touching an image boundary.

Shape is measured but is deliberately not used as an automatic filter. Sphericity, compactness, elongation, and Feret diameter remain available in the result table for downstream analysis.

## Outputs

For an interactive run, the selected **Output** controls can produce:

- **Objects map**, showing each complete linked shape on every occupied Z slice with its object number
- **Surfaces map**, containing labelled surface voxels
- **Centroids map**, marking geometric centroids
- **Centres of mass map**, marking intensity-weighted centres of mass
- **Statistics table**, with one row per object
- **Summary**, with aggregate measurement statistics
- **Keep 3D label image**, retaining the numeric 3D label image for downstream tools

The per-object table includes volume, surface area, object and surface voxel counts, integrated density, mean, standard deviation, median, minimum and maximum intensity, centroid, centre of mass, bounding box, label, sphericity, compactness, elongation, and maximum 3D Feret diameter.

When **Summary** is selected, the ImageJ Log reports the final object count, model and detection settings, linking settings, single-slice object count, filtered-object counts, and elapsed time. The result object count is therefore available even when visual maps are not needed.

The 3D label image is a reusable segmentation output: non-zero integer labels identify objects from `1` through `N`, so it can be passed to other ImageJ tools that accept label images.

## Batch processing

Run {% include bc path="Analyze|3D Objects Counter - StarDist Batch..." %} to analyse a folder. Batch mode supports:

- recursive or single-folder discovery
- a configurable extension list; the default is `tif,tiff,lif,nd2,czi,lsm,oib,oif`
- optional filename regular expressions and capture-group-based grouping
- a **Confirm groups** step before the expensive detection run
- optional 3D label images and visual maps
- per-image, per-folder, and per-group tables

The completion dialog reports the number of images processed, the total number of objects, any failed images, and the output location.

Results are written beneath a `3D Objects Counter - StarDist/` folder:

```text
3D Objects Counter - StarDist/
  Labels/    <image>_labels.tif
  Objects/   <image>_objects.csv
  Maps/      <image>_objects_map.tif, <image>_surface_map.tif, ...
  Groups/    <group>_objects.csv, <group>_summary.csv
  Summary/   summary.csv, per_folder_summary.csv, groups.csv, manifest.csv
  README.txt
```

`manifest.csv` records the source file, grouping, calibration, model and linking parameters, object counts, filtering counts, elapsed time, and success or failure status for every image.

## Macro and headless usage

Both commands are macro-recordable. The single-image command can be called as:

```ijm
run("3D Objects Counter - StarDist",
    "channel=1 model=versatile_fluo probability=0.5 overlap=0.4 " +
    "linking_distance=5.0 gap_distance=5.0 slice_gap=1 min_slices=1 " +
    "min=10 exclude_edges save_labels hide_display");
```

`hide_display` suppresses result windows for scripted use. Output choices can also be controlled with `hide_labels`, `hide_surfaces`, `hide_centroids`, `hide_centers_of_mass`, `hide_stats`, `hide_summary`, and `save_labels`.

## Java API

The public API is under `sc.fiji.oc3dsd.api`. It opens no dialogs, displays no windows, and writes no files:

```java
OC3DSDParameters params = OC3DSDParameters.builder(stack)
    .channel(1)
    .probability(0.5)
    .overlap(0.4)
    .linkingDistance(5.0)
    .minSlices(1)
    .build();

OC3DSDResult result = OC3DSD.run(params);
int count = result.getObjectCount();
ResultsTable objects = result.getObjects();
ImagePlus labels = result.getLabelImage();
```

TensorFlow inference is process-global and is serialised internally, so running concurrent API calls does not speed up inference across images.

## Related tools

[3D Objects Counter+](/plugins/3d-objects-counter-plus) uses intensity thresholding instead of StarDist. It is faster and needs no machine-learning runtime, making it suitable when objects are already well separated. Because the two plugins segment images differently, their counts are not expected to agree on the same image.

## Citing

Please cite the plugin using the `CITATION.cff` metadata in its [source repository](https://github.com/Jay2owe/3DObjectsCounter-StarDist). Please also cite the methods it builds on:

- Schmidt, Weigert, Broaddus, and Myers (2018), [*Cell Detection with Star-convex Polygons*](https://doi.org/10.1007/978-3-030-00934-2_30).
- Tinevez et al. (2017), [*TrackMate: An open and extensible platform for single-particle tracking*](https://doi.org/10.1016/j.ymeth.2016.09.016).
- Ershov et al. (2022), [*TrackMate 7: integrating state-of-the-art segmentation algorithms into tracking pipelines*](https://doi.org/10.1038/s41592-022-01507-1).
- Bolte and Cordelieres (2006), [*A guided tour into subcellular colocalization analysis in light microscopy*](https://doi.org/10.1111/j.1365-2818.2006.01706.x), for the object-measurement definitions.
