---
title: SNT › Seeded Tracing
nav-links: true
nav-title: Seeded Tracing
artifact: org.morphonets:SNT
icon: /media/icons/snt.svg
forum-tag: snt
update-site: Neuroanatomy
extensions: ["mathjax"]

tags: snt,seeds,points,neuroanatomy,deep-learning,segmentation,ground-truth
---

{% capture version%}
**This page was last revised for [version 5.1.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice icon="snt" content=version %}

Seeded Tracing allows for anchoring/constraining tracing algorithms around key locations ([machine learning predictions](./machine-learning#deep-learning), soma locations, neurite endpoints, manual annotations, etc.). A **seed** is a 3D point that carries a position, a confidence score, and a few optional attributes (radius, type, source, channel, frame). Seeds are overlaid on the image using a dedicated renderer, and do not affect other overlaid objects like paths or ROIs. Common sources of seeds include:

- **Deep-learning detectors** that output candidate soma/endpoint coordinates (see [Machine Learning](./machine-learning))
- **Labels/segmentation images** e.g., from [cellpose](https://www.cellpose.org/), [Stardist](https://stardist.net/), [Labkit](../labkit), or [TWS](../tws), where each label/connected component yields one seed (e.g., cellpose masks can be used to specify the soma locations when autotracing [multiple cells](./auto-tracing#multiple-cells))
- **ROIs** e.g., generated from ImageJ routines (area and line ROIs are reduced to representative points)
- **Tabular data** (CSV) exported from external tools or scripts

A typical workflow has three steps: [**get**](#getting-seeds) seeds (detect features or import them), **curate** them (filter by confidence, edit, merge, etc.) using the [Seeds tab](#seeded-tracing-assistant), and [**use**](#using-seeds) them (auto-trace, review, or export).

<span id="seeds"></span>
# Seeded Tracing Assistant
{% include img src="/media/plugins/snt/snt-seeded-tracing-assistant.png" align="right" width="350px" %}

The _Seeded Tracing Assistant_ is one of the main tabs in the [Main Dialog](./manual#main-dialog) and manages seeds. It is organized into four sections: a display toolbar, a confidence filter, a table of all loaded seeds, and a bottom toolbar for [import](#importing-seeds), [export](#exporting-seeds), [detection](#detecting-features), and [autotrace](#auto-tracing-from-seeds) actions.

## Display toolbar
Controls how seeds are rendered on the tracing canvas, and includes:

- **Show/hide seeds** toggle button for the visibility of the whole seed overlay
- **Color mode** drop-down menu defining what drives the lookup table (LUT) mapping:
  - _Confidence_: LUT sampled by the seed's confidence within the active filter window
  - _Index_: One distinct LUT slot per seed. This allows seeds to be rendered with unique colors under the _Distinct/Glasbey_ lookup table
  - _Type_/_Source_: Seeds are color-coded by _type_ or _source_
- **Color ramp** displays the LUT in use, spanning the confidence range of the [filter](#confidence-filtering)
- **Color table button** opens a menu to choose the LUT, and lists the following commands:
  - _Fallback Color..._: Color of seeds with undetermined (_NaN_) confidence, e.g., from a detector batch too small or too uniform to be normalized. Only used in _Confidence_ mode
  - _Transparency..._: Opacity of seed markers
  - _Fit Confidence Range to Data_: Sets the confidence range to the minimum/maximum confidence across all seeds, so that the _Confidence_ color mode spans the full data range again. Useful after editing confidences or loading/detecting new seeds

## Confidence Filtering

Two sliders set the inclusive $$[low, high]$$ confidence range. Seeds outside the range are hidden in both the canvas overlay and the table view; they remain in the underlying data and can be brought back by widening the range. The label beneath the sliders reports how many seeds are currently being filtered.

## Seeds Table

Each row lists a seed. Selecting rows in the table also selects the corresponding seeds on the canvas (and vice versa). The table is organized as follows:

| Column         | Meaning                                                                |
|----------------|------------------------------------------------------------------------|
| **X, Y, Z**    | Position in physical (calibrated) coordinates                          |
| **C, T**       | Channel and frame (1-based) the seed is associated with. Empty if unset |
| **Conf**       | Confidence score in $$[0, 1]$$. Drives the color mapping and the confidence-range filter |
| **Radius**     | Optional sphere radius (physical units). Zero for point-only seeds     |
| **Type**       | Free-form category (e.g., _soma_, _endpoint_, _waypoint_)              |
| **Source**     | Where this seed came from (e.g., _roi_, _labels-image:cellpose.tif_)   |

- A **color swatch** next to the column driving the active _Color mode_ (_Conf_, _Type_, or _Source_; _X_ in _Index_ mode) reports the color of each seed
- **{% include key keys='Double Click' %}** a row to navigate the canvas to that seed (channel/frame are honored when set; otherwise the active C/T is used). The _Visiting zoom level_ spinner on the bottom toolbar controls the zoom level applied during the go-to
- **{% include key keys='Right Click' %}** for selection, editing, and analysis controls (see [Contextual Menu](#contextual-menu))
- **Sort** by clicking column headers; the confidence filter survives across sorts

{% capture tipseed1%}
When tracing is paused, {% include key keys='Alt|Left Click' %} on a seed marker to edit it.
{% endcapture %}
{% include notice icon="tip" content=tipseed1 %}

## Contextual Menu

{% include key keys='Right Click' %} on the table opens a menu of commands that act on the selected seeds. Unless stated otherwise, if no seeds are selected, commands act on all the seeds listed in the table, i.e., those within the confidence range of the [filter](#confidence-filtering). Commands are grouped as follows:

- **Selection**
  - **Deselect / Select All**: Toggles the selection of all rows
  - **Select by Path Coverage ›**: Selects the listed seeds that already have a nearby traced path node (_Select Covered_), or that do not (_Select Uncovered_). A seed is considered covered if a path node exists within 1.5 times its radius or within three times the largest in-plane voxel size, whichever is larger. Useful to find detections that remain to be traced

- **Edit...** Edits the attributes of the selected seed. If several seeds are selected, edits are applied in bulk
- **Delete...** Removes the selected seeds (after confirmation)

- **Adjust**
  - **Scale Confidence ›**: _Increase Confidence..._ and _Decrease Confidence..._ scale the confidence of the selected seeds by a percentage (default 10%)
  - **Scale Radius ›**: _Increase Radius..._ and _Decrease Radius..._ scale the radius of the selected seeds by a percentage (default 10%)

- **Combine**
  - **Merge by Distance...**: Replaces seeds that lie within a maximum distance of each other (physical units) by their centroid. Only seeds sharing the same channel and frame are merged. Confidence and radius of the merged seed are averaged, and its _source_ is set to _merged_
  - **Merge Selection into One**: Replaces the selected seeds with their centroid, regardless of distance. Selected seeds must share the same channel and frame
  - **Colocalize...**: Adds a seed at the centroid of seeds from different channels that lie close together (same frame), e.g., maxima detected in each channel of a double label. The originals can be kept or replaced. Colocalized seeds have _type_ set to _colocalized_ and _source_ listing the contributing channels (e.g., _C1+C2_). Requires seeds from at least two channels

- **Analyze**
  - **Nearest Neighbor Distribution...**: Plots a histogram of nearest-neighbor distances. Helps to spot multiple hits on the same spot

- **Seed Reviews**
  - **Send to Curation Assistant ›**: Appends the selected seeds (a selection is required) to the [Curation Assistant](./curation#seed-review) list of warnings, as an advisory note, a warning, or an error. Useful for flagging detector candidates for human review

- **Table Controls**
  - **Resize/Reset Columns**: Adjusts column widths to fit contents, or resets them to their defaults
  - **Detach Table**/**Dock Table**: Moves the table into its own window for a larger working area, or back into the tab

# Creating Seeds

Seeds are obtained by detecting features (somas, tips, tufts, etc.) or by importing locations computed elsewhere. Both are done from the bottom toolbar of the Seeds tab.

## Detecting Features

The **+** button on the bottom toolbar computes seeds from images or from traced paths, adding them to the table. The following features can be detected:

| Feature      | Command                                  | Operates on      | Requires                                              |
|--------------|------------------------------------------|------------------|-------------------------------------------------------|
| **Somas**    | _Detect Somas..._                        | Image            | An image                                              |
| **Tips**     | _Detect Tips (Learn From Paths)..._      | Image            | Example paths (to learn detection parameters)         |
|              | _Detect Tips (Saved Parameters)..._      | Image            | Parameters saved from the command above              |
| **Tufts**    | _Detect Tufts..._                        | Traced paths     | Traced paths (an image if weighting by intensity)     |
| **Roots**    | _Detect Roots..._                        | Traced paths     | Traced paths                                          |
| **Swellings**| _Detect Swellings (From Radii)..._       | Traced paths     | Fitted radii                                          |
| **Maxima**   | _Detect Maxima (Around Paths)..._        | Traced paths     | An image                                              |

Swellings and maxima are detected on the paths selected in the [Path Manager](./manual#path-manager) (or on all paths, if none is selected). Tufts and roots are detected on whole structures: when several exist, a prompt asks which ones to scan. Detectors that score candidates (somas, tufts, roots, swellings, maxima) derive confidence from detection scores using a percentile-clipped normalization: scores at the 10th and 90th percentiles map to confidences of 0.1 and 0.9, respectively, and outliers are clamped to [0, 1]. When there are too few candidates (or they are too uniform) for scores to be compared, confidence is undetermined (_NaN_) and the seed is displayed using the _Fallback Color_.

{% capture detecthint %}
Not sure which detector to use? Try {% include bc path='Auto-trace|Guided Feature Detection...' %} in the main dialog: it asks what you want to detect, checks that requirements are met, and runs the appropriate detector.
{% endcapture %}
{% include notice icon="info" content=detecthint %}

### Somas

Adds one seed per soma detected in the image. Detection follows the strategy described in [Soma Detection](./auto-tracing#soma-detection). Soma seeds are natural [roots](#seeds-as-roots--somata) for auto-tracing multiple cells.

### Tips

Detects the tips of neurites and other ramified structures in large volumes. It is a two-step process:

- **Detect Tips (Learn From Paths)...** A wizard learns detection parameters from example paths (those selected in the Path Manager, or all paths if none is selected), and previews the result on the region spanned by the paths. The preview reads data directly from its source, independently of the image loaded on SNT's canvas (and thus unaffected by crops), and detection is updated live as the sliders are adjusted
- **Detect Tips (Saved Parameters)...** Detects tips in the whole volume using the parameters saved by the wizard, without needing example paths. Useful for re-running detection on new data

Tip seeds are natural [endpoints](#seeds-as-endpoints--tips) for auto-tracing.

### Tufts

Detects clusters of nearby terminal branches in traced structures. The prompt includes the following options:

- **Detect tufts using** Where in the arbor(s) tufts are expected: _Density of terminal branches_, _Terminal branches_, _Terminal branch points_, _Tips_, _Terminal locations_, _Branch points_, or _Branch density_. Hover over the option in the prompt for a description of each
- **Tuft radius** Distance threshold (physical units) defining a tuft. It acts as a clustering radius: nodes within this distance of each other are candidates for the same tuft
- **Weight by** What evidence besides crowding counts toward a tuft: _Node radii_, _Sampled intensity_ (requires an image), both, or _None_
- **Penalize short terminal branches** Applies to the _Terminal branches_ option only. Discontiguous (e.g., beaded) neurites can fragment into several short, spatially-close terminal branches that would otherwise look like a genuine tuft. If checked, branches shorter than _Tuft radius_ contribute proportionally less
- **Replace existing seeds** Whether existing seeds are replaced or detected tufts are appended

### Roots

Detects convergence of disconnected tracings. Unconnected (non-soma) primary paths that start within _Convergence radius_ (physical units) of each other are flagged as candidates for a shared, unimaged origin. Useful for neurites whose soma was not imaged. _Weight by node radii_ makes thicker root stubs count more than thin ones. Existing seeds can be replaced or appended to.

### Swellings and Maxima

These detectors flag bouton/varicosity-like features along or around traced paths:

- **Detect Swellings (From Radii)...** Detects boutons, varicosities, and blebs along paths from longitudinal radius (and, optionally, intensity) profiles. Requires fitted radii (see [Refine/Fit](./manual#refinefit-))
- **Detect Maxima (Around Paths)...** Detects intensity maxima (varicosities, spines, synaptic puncta) in annular cross-sections around paths. Requires an image

They are the same detectors available in the Path Manager's {% include bc path='Analyze|Spine/Varicosities/Labels' %} menu, which can also output other annotations (e.g., ROIs or bookmarks). Their parameters are described in [Maxima Around Paths](./spines-varicosities#maxima-around-paths) and [Swellings Along Paths](./spines-varicosities#swellings-along-paths), and the output choices in [Output Options](./spines-varicosities#output-options).

## Importing Seeds

{% capture tipseed2%}
Seeds can be imported by drag-and-drop. The following files are supported: [.csv](#from-csv-file), [.roi/.zip](#from-rois), and [.tif](#from-labelsmasks-image)
{% endcapture %}
{% include notice icon="tip" content=tipseed2 %}

### From CSV File
{% include bc path='Import|From CSV File...' %}

SNT reads a comma- or tab-separated table with a header row, with the following required columns (case-insensitive, whitespace-tolerant): `x`, `y`, `z`, `confidence`, `radius`. Optional columns include: `channel`, `frame`, `type`, `source`. Defaults are applied when absent.

**NB**: Voxel-indexed inputs can be converted to physical (spatially-calibrated) location at import time using the image's spacing

### From Labels/Masks Image
{% include bc path='Import|From Labels/Masks Image...' %}

The program will parse a labels/mask image (produced e.g., by cellpose, Stardist, [Labkit or TWS](./machine-learning#embedded-tools-labkit--tws)), and extract one seed per non-zero label. For each label, SNT computes:
- **Centroid** in physical coordinates
- **Radius** from the sphere whose volume equals the label's total volume: $$r = \sqrt[3]{\frac{3V}{4\pi}}$$
- **Confidence** linearly interpolated between _minConfidence_ (smallest label) and $$1.0$$ (largest). In the case of e.g., a cellpose mask: the label with the smallest volume would be assigned the lowest confidence, the largest, the highest confidence

**NB**: If the chosen image is a binary mask, one-seed-per-label would collapse the whole foreground into a single seed. SNT detects this case and offers to run a connected-components analysis first (8-connectivity in 2D, 26-connectivity in 3D), label each distinct object, and proceed with the labeled image.

### From ROIs
{% include bc path='Import|From ROI Manager...' %}

SNT will parse all the ROIs stored in the ROI Manager, using the following criteria:

- **Area ROIs** (oval, polygon, rectangle, freehand, traced): centroid as position; radius from the matched-area disk: $$r = \sqrt{\frac{A}{\pi}}$$)
- **Line ROIs** (straight): midpoint as position; radius is half the path length. **Polylines / freelines**: vertex centroid; radius is half the summed segment length
- **Point ROIs**: each contained point becomes its own seed (without radius)
- **Other geometries** (angle, composite): bounds-center position, no radius

**NB**: Channel and frame come from the ROI's hyperstack position when set, otherwise from the image's active C/T. When importing ROIs, it is possible to set their seeds _type_ and _confidence_ value (default 1.0).

### From Workspace
{% include bc path='Import|From Workspace...' %}

This option loads a previously-exported `seeds.csv` directly from the current [SNT session directory](./manual#save-session). Useful for quickly restoring seeds across SNT restarts.

# Using Seeds

Once curated, seeds can drive automated tracing, be sent for review, or be exported for use elsewhere.

## Auto-tracing From Seeds
Seeds can drive automated tracing in different ways, accessible through the auto-trace (robot icon) dropdown on the bottom toolbar. Each role is available for intensity images (GWDT auto-tracing) and, for _Roots_ and _Tips_, for binary/skeleton images (e.g., cellpose/StarDist labels or other pre-segmented data).
The naming convention pairs the algorithmic role with its biological interpretation: _Roots_ → _Somata_; _Endpoints_ → _Tips; _Waypoints_ → _Path Attractors_. All tracing commands inherit the paramaters documented under [Intensity](./auto-tracing#intensity-images)/ [Segmented](./auto-tracing#segmented-images) -image autotracing: Only the seed-related parameters and the role the seeds play differ.

| Role (Biological interpretation) | Intensity image                                         | Binary/skeleton image                               | Output                                          |
|----------------------------------|---------------------------------------------------------|-----------------------------------------------------|-------------------------------------------------|
| [Roots](#seeds-as-roots--somata) (Somata)        | _Intensity Image (One Tree per Seed)..._      | _Binary/Skeleton Image (One Tree per Seed)..._      | One tree per seed                               |
| [Endpoints](#seeds-as-endpoints--tips) (Tips)    | _Intensity Image (Single Cell)..._            | _Binary/Skeleton Image (Single Cell)..._            | One tree connecting the soma to every tip       |
| [Waypoints](#seeds-as-waypoints--path-attractors) (Path attractors) | _Intensity Image (Single Cell, Constrained)..._ | n/a                                     | One tree biased to route through the seeds      |

Soma seeds are natural roots, and tip seeds natural endpoints. Seeds from path-based detectors (tufts, roots, swellings, maxima) are typically used for [review](#reviewing-seeds) and annotation instead.

### Seeds as Roots / Somata
{% include bc path='Auto-trace Menu|Intensity Image (One Tree per Seed)...' %}<br>{% include bc path='Auto-trace Menu|Binary/Skeleton Image (One Tree per Seed)...' %}

Each filtered seed becomes the root of its own auto-trace; the soma-detection strategy of the autotraced is bypassed because the seed _is_ the root. The command iterates one tracer run per seed and aggregates the resulting trees into a forest: one tree per seed.
Failures (unreachable seeds, seeds in background, etc.) are logged to the Console but don't abort the run. With the _Binary/Skeleton Image_ variant, each tree is extracted from the skeleton component connected to its seed: one seed per labeled object produces one tree per object.

The seed source filter (_Visible_/_All_/_Selection only_) and type filter allow you to restrict the per-seed loop to a subset.
When invoked from rows selected, the source filter is pre-targeted to _Selection only_.

### Seeds as Endpoints / Tips

{% include bc path='Auto-trace Menu|Intensity Image (Single Cell)...' %}<br>{% include bc path='Auto-trace Menu|Binary/Skeleton Image (Single Cell)...' %}

In this modality filtered seeds become tip targets. The autotracer runs detection from the soma exactly once, then extracts the shortest path from each tip back to the root via the parent-pointer field. This is equivalent to the A* shortest-path tracing that SNT uses for interactive endpoint clicking, but batched over the entire seed set.
The soma ROI on the canvas (or its automatic detection) defines the root. The output is **one tree** connecting the soma to every reachable tip; tips that fall outside the foreground or outside the image bounds are logged and skipped. With the _Binary/Skeleton Image_ variant, the full skeleton tree is traced and then pruned to keep only paths on a root-to-tip route: tips whose nearest skeleton node lies in a different connected component than the soma are reported as unreachable.

Since seeded tips are by definition the desired endpoints, auto-traces do not perform any hierarchical pruning.

### Seeds as Waypoints / Path Attractors

{% include bc path='Auto-trace Menu|Intensity Image (Single Cell, Constrained)...' %}

In this modality filtered seeds act as _soft attractors_: the cost map used by the auto-tracer is locally biased toward each waypoint voxel, so the resulting tree preferentially routes paths through (or near) the seeds. The root-to-waypoint paths are then protected from the standard pruning passes, ensuring the biased branches survive into the final tree.

The prompt exposes three bias controls:

- **Bias source**: _From confidence_ (default: each seed's confidence value scales its attraction), _From radius_ (radius normalized across the waypoint set), or _Uniform_ (fixed factor)

- **Bias strength**: overall multiplier in `[0, 1]`. The default `0.9` means a confidence-1 seed is pulled almost all the way to a zero-cost voxel

- **Bias sphere radius (voxels)**: spatial extent of the bias around each waypoint. A small sphere (2–3 voxels) is usually enough; larger values may create phantom attractors at the bias boundary in low-contrast images

{% capture wpnote %}
The bias is a _hint_, not a hard constraint. If the surrounding terrain provides a much cheaper path that bypasses the waypoint, the trace can still detour around it. For stricter "must visit this point" semantics, use the [Tips](#seeds-as-endpoints--tips) command instead.
{% endcapture %}
{% include notice icon="info" content=wpnote %}

<span id="seeds-as-a-review-tool"></span>
## Reviewing Seeds
Seeds selected in the table can be converted into _Review locations_ and sent to the [Curation Assistant](./curation#seed-review) for inspection, using {% include bc path='Contextual Menu|Send to Curation Assistant' %} (see [Contextual Menu](#contextual-menu)). Useful for quality assessment of existing reconstructions, and for closing the loop with QC-classifier training data: each location can be tagged _accept_ / _reject_ / _unsure_ and exported as labels for the next training round.

## Exporting Seeds

### To CSV File
{% include bc path='Export|To CSV File...' %}

This option exports all seeds to a CSV file with the same column layout used by the [importer](#from-csv-file).

### To ROI Manager
{% include bc path='Export|To ROI Manager...' %}

Converts seeds to ImageJ ROIs. Seeds with set radius become circles of diameter $$2r$$; seeds without radius become point ROIs. By default, selected seeds in the table are exported; if no rows are selected, all seeds are converted. Note that Seed → ROI conversion is lossy since ROIs have no awareness of _confidence_, _type_, or _source_.

### To Workspace
{% include bc path='Export|To Workspace...' %}

Writes all seeds to a  _seeds.csv_ file into the current session directory. The counterpart [From Workspace](#from-workspace) reloads from the same location.

# Scripting
The seed overlay is accessible from [scripts](./scripting) via `snt.getSeedOverlay()`.
The same operations available in the GUI (add, remove, filter, change colors, run autotracers with seeds in different roles) can be performed programmatically.
