---
title: Figure Panel Builder
description: Build comparable publication figures from multi-channel microscopy images with guided representative-section selection, locked display ranges, an editable layout canvas, and auditable outputs.
categories: [Visualization, Analysis, Automation]
source-url: https://github.com/Jay2owe/FigurePanelBuilder
update-site: FigurePanelBuilder
release-version: 0.1.0
release-date: 2026-08-06
dev-status: Active
support-status: Active
team-maintainers: '@Jay2owe'
license-url: https://github.com/Jay2owe/FigurePanelBuilder/blob/main/LICENSE
license-label: BSD-3-Clause
---

Figure Panel Builder is an ImageJ/Fiji plugin for assembling publication figures from folders of multi-channel microscopy images. It keeps channel appearance comparable by applying one locked display range per channel across every compared image, guides the choice of an exact representative section for each group, and records the metadata and rendering decisions used to build the figure.

The plugin combines image discovery, editable experimental labels, representative-section guidance, section-level cross-group comparison, layout and annotation editing, and publication export in one five-stage workflow. A separate **Quick grid** route is available when every discovered image should be arranged without representative selection.

## Installation

Figure Panel Builder is distributed through its ImageJ update site:

{% include link-banner url="https://sites.imagej.net/FigurePanelBuilder/" %}

To install it:

1. Start Fiji.
2. Choose {% include bc path="Help|Update..." %}.
3. Click **Manage update sites**.
4. Enable **Figure Panel Builder** if it is listed, or click **Add Unlisted Site** and enter:
   - Name: `FigurePanelBuilder`
   - URL: `https://sites.imagej.net/FigurePanelBuilder/`
5. Apply the changes and restart Fiji.

Run the plugin from {% include bc path="Plugins|Figure Panel Builder" %}.

## Guided Workflow

The **Figure Panel Builder** window can switch to full-screen mode and keeps completed stages available for review. Its stages are **Images**, **Channels**, **Choose images**, **Layout**, and **Export**.

### Images

Choose an image folder and optionally enable **Include subfolders**. Group, subject, and section labels can be derived from:

- **Filename**, using editable token roles
- **Subfolder**
- **CSV**
- **Advanced...** regular-expression matching

The metadata table remains editable after labels are inferred. Double-click a cell to change it, or bulk-apply a Group, Subject, or Section value to selected rows or all rows. **Import CSV** and **Export CSV** support review and reuse outside the plugin.

Each series in a Leica LIF container is treated as a separate logical image. Its individual series name is used for label inference, and exported identifiers include the series number so that multiple images from one container remain distinct.

### Channels

The **Channels** stage detects the available channels and lets users choose which channels to include, edit their names, and assign display colours. **Z handling** can use a **Maximum projection** or the **First slice**.

Representative guidance can use either:

- **Built-in brightest 1%**, calculated from full-resolution pixels for every included channel
- **Numeric CSV column**, using an exact numeric value supplied for each image

Image previews and statistics begin loading in the background before **Choose images** is opened. Progress is reported while images load and suggestions are calculated.

### Choose Images

The guided workflow ranks subjects within each group by how close their multi-channel measurements are to that group's average. When a subject has multiple sections, its sections are averaged only for this subject-level ranking. The final choice remains one exact section for each group.

An always-visible **GROUP QUANTIFICATION** plot shows all included channels on one z-normalized axis. Every dot is one section; colours and mean bars identify groups; the zero line is the overall mean after per-channel normalization. This view is a descriptive comparison to support representative-image choice, not an inferential statistical test.

Each group has its own image tab and the current picks stay visible together. The selected section is marked in both the image row and the quantification view. Compact controls rotate an image left or right by 90 degrees or flip it horizontally or vertically.

Display-range sliders affect appearance only. A minimum and maximum must be locked for every included channel before continuing, and the same per-channel range is then used across all compared images and carried into the exported panel assets.

### Layout and Annotation Editor

The **Layout** stage renders a high-quality full-figure preview while preserving each image's aspect ratio. Groups can be distributed across rows, group titles can be renamed and aligned left, middle, or right, and scale-bar length and corner can be set from the main controls.

The canvas supports **Fit**, **100%**, **150%**, and **200%** views. Ctrl+mouse-wheel zooms continuously around the pointer, dragging pans the canvas, and Shift+mouse-wheel scrolls horizontally. Hovering over an image reveals the same rotate and flip controls used during image selection.

Four focused editors provide direct control over the final layout:

- **Edit spacing...** adjusts the image-grid spacing and margins.
- **Edit external labels...** lets users click group, column, or row labels to replace their text; drag labels to change their distance from the grid; resize label types with a handle; and control visibility, size, orientation, and group alignment.
- **Edit annotations...** lets users drag and resize the image label and scale bar, choose their appearance, and turn corner snapping on or off.
- **Edit calibration...** accepts per-image X/Y pixel sizes when embedded micron calibration is absent or needs to be overridden.

Calibration overrides are recorded in the export manifest. Label, scale-bar, orientation, and spacing edits are applied consistently to the preview and raster/SVG outputs.

### Export

The **Export** stage selects the output folder, figure resolution, export scale, and assembled formats. **Build figure** keeps the window open and reports progress until the export finishes or is cancelled.

Available assembled formats are:

- `figure.png`
- `figure.tif`
- `figure.svg`, with editable text and full-resolution embedded panel images

The overall PNG/TIFF figure resolution follows the selected DPI and export scale. Full-resolution individual panel assets are written separately, so their dimensions are not limited by the assembled figure DPI.

## Supporting Files and Reproducibility

When enabled, Figure Panel Builder writes a `Supporting files/` directory containing:

- `panels/`: full-resolution, display-adjusted panel PNGs and one calibrated channel-only TIFF stack per selected image
- `manifest.csv`: source, calibration, display range, clipping, selection, and output details for every exported panel
- `selection.csv`: the per-subject evidence used for representative guidance
- `group_quantification.png` and `group_quantification.csv`: the section-level cross-group comparison, raw values, z scores, group summaries, and chosen-section flag
- `metadata.csv`: the exact edited group, subject, and section labels used for deterministic replay
- `methods.txt`: checklist fields and suggested methods text for the completed figure
- `README.txt`: a guide to the output folder

The optional `Supporting files/All project images/` export processes every logical source image, not only the representative picks. It can write full-resolution, lossless, display-adjusted channel and merge PNGs and/or one calibrated RGB TIFF channel stack per image. TIFF channel stacks contain the selected channels and do not add a merge slice.

## Quick Grid

**Quick grid** is an express route from the **Images** stage. It loads every discovered image, derives one cohort display range per channel, and exports the complete image set without asking for group-wise representative picks. Because it does not run the guided selection workflow, Quick Grid does not claim that any image is representative.

## Supported Inputs

Figure Panel Builder discovers TIFF, PNG, JPEG, GIF, BMP, LIF, CZI, ND2, OIB, OIF, and LSM files. It uses Fiji's Bio-Formats installation for microscopy containers.

LIF files are expanded into all named series. Other multi-series container formats currently use their first series. Version 0.1.0 accepts up to 100 logical images per run.

For scale bars, the plugin verifies embedded micron calibration for each chosen image. Explicit X/Y values entered in **Edit calibration...** override embedded metadata and are identified as user-entered values in `manifest.csv`.

## Macro, Headless, and Java Use

When the ImageJ macro recorder is active, a successful guided or Quick Grid export records a complete `run("Figure Panel Builder", "...");` call. Guided replay includes explicit input, metadata strategy, channels, colours, locked display ranges, group picks, layout, and output settings. Add the `hide_display` flag for headless execution after all required options have been recorded or supplied.

The dialog-independent Java API also accepts explicit parameters and writes files only when export is requested:

```java
FPBParameters params = FPBParameters.builder(folder)
        .channel(1, "DAPI", ChannelColour.BLUE, 120, 4200)
        .pick("Control", "S3")
        .outputFolder(output)
        .build();

FPBResult result = FPB.run(params);
FPB.write(result);
```

The plugin targets Java 8 for Fiji compatibility and is released under the BSD 3-Clause License. Citation metadata is included in the source repository's `CITATION.cff` file.
