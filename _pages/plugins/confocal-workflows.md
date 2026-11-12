---
title: Confocal Workflows
description: Guided Fiji workflows for confocal images, from deconvolution to per-cell measurements of intensity, mitochondria, protein import, aggregates and organelle contacts.
categories: [Analysis, Deconvolution, Colocalization, Segmentation]
name: Confocal Workflows
source-url: https://github.com/vishal9045/fiji-confocal-workflows
license-url: https://github.com/vishal9045/fiji-confocal-workflows/blob/main/LICENSE
license-label: MIT
release-version: "1.0.1"
dev-status: Active
support-status: Active
forum-tag: fiji
team-founders: 'Vishal Sah | https://github.com/vishal9045'
team-maintainers: 'Vishal Sah | https://github.com/vishal9045'
---

Confocal Workflows is a set of six guided workflows for confocal image analysis in [Fiji](/software/fiji). Each one asks for its folders, channels and settings in dialogs and shows a live preview for its main threshold or cutoff. The measurement workflows apply the same rules to every image in an experiment and write an Excel workbook (summary, per-image and per-cell sheets, and the settings used, including the plugin version) together with QC images in which every measured cell is numbered, plus bar graphs when conditions are compared.

A single file can be any format Bio-Formats reads; in a folder, the workflows pick up the common microscope formats (Olympus, Zeiss, Leica, Nikon, Imaris, DeltaVision and TIFF/OME-TIFF).

## Installation

[Add](/update-sites/following#add-update-sites) the **Confocal-Workflows** update site:

1.  Select {% include bc path='Help | Update...' %} to start the [updater](/plugins/updater).
2.  Click *Manage update sites*, tick **Confocal-Workflows**, and click *Apply and Close*.
3.  Click *Apply changes* and restart Fiji.

The workflows appear under {% include bc path='Plugins | Confocal Workflows' %}. {% include bc path='Plugins | Confocal Workflows | About Confocal Workflows' %} shows the installed version.

## Workflows

### Deconvolve Confocal Stack

For 60x/100x confocal stacks. The workflow reads the optics from the file, checks Nyquist sampling and runs a trial on each channel before Richardson-Lucy deconvolution. It saves calibrated TIFFs, QC images, a methods manifest (CSV) and figure panels with one display range per channel across all images.

### Measure Cell Intensity

Measures fluorescence intensity, for example GFP, on raw images. Every ImageJ threshold method is scored on the control images and the best one is suggested in a live window; that one threshold is then applied to every image. Reports the MFI of positive objects, the percent positive area and the threshold-free mean of the whole field.

### Mitochondrial Measurements

Counts mitochondrial pieces and measures their length with any mitochondrial marker or dye, using one threshold for all images. The main readout is length per piece (total skeleton length divided by the number of pieces), alongside mean branch length and the area and perimeter per piece. An optional 2D + 3D mode repeats the measurements on the full stack.

### Measure Protein Import

Measures, cell by cell, how much of a reporter or protein gets into a compartment: organelle import (mitochondria, peroxisomes, ER or another organelle with its own marker) or nuclear import. The reporter is summed over every slice of the stack. Reports the imported fraction for organelle import, and the nuclear fraction and N/C ratio for nuclear import.

### Measure Aggregates

Reports the percentage of cells that have aggregated a protein, for endogenous (stained) or overexpressed protein, with or without an organelle marker. The percentage of control cells called aggregated is reported as a false-positive check.

### Measure Contacts

Measures how much two organelles are apposed, per cell and in 3D, against what random placement in the same cell would give, and optionally how much of a contact reporter (Contact-ID, SPLICS, split-GFP, PLA) sits at the interface. Confocal resolution is far coarser than a contact, so two markers alone measure apposition, not contact.

## Limitations

-   Time-lapse series are not supported and are listed as not processed.
-   Channels default by their names in the file; check them in each dialog.
-   2D (max projection) and 3D numbers should never be mixed.

## Support

Documentation and source code are on [GitHub](https://github.com/vishal9045/fiji-confocal-workflows). Please report bugs as [GitHub issues](https://github.com/vishal9045/fiji-confocal-workflows/issues) or ask on the [Image.sc Forum](https://forum.image.sc/).
