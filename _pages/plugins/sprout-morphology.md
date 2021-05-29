---
mediawiki: Sprout_Morphology
title: Sprout Morphology
artifact: angiogenesis:Sprout_Analysis
doi: 10.1186/s41232-016-0033-2
---

The **Sprout Morphology** plugin measures sprout *number*, *length*, *width* and *cell density* of endothelial cell (EC) sprouts grown in a bead sprouting assay. It optionally includes measuring the coverage of these sprouts with pericytes included in the assay, as well as the endothelial cell/pericyte ratio.

## Installation

To install the plugin, activate the **Angiogenesis** [update site](/update-sites/following) and restart Fiji.

## Usage

Open a maximum intensity projection of the multi-channel image to be analyzed, then start the plugin via {% include bc path='Analyze|Sprout Morphology'%}. The process consists of up to six dialogs:

### General configuration

{% include img src="sproutanalyzer-configuration" width="400" alt="Configuration dialog" %}

### Bead detection

{% include img src="sproutanalyzer-beaddetection" width="400" alt="Bead detection" %}

### Sprout detection

{% include img src="sproutanalyzer-sproutdetection" width="400" alt="Sprout detection" %}

### Nucleus segmentation

{% include img src="sproutanalyzer-nucleussegmentation" width="400" alt="Nucleus segmentation" %}

### Endothelial cell/Pericyte classification

{% include img src="sproutanalyzer-cellclassification" width="400" alt="Cell classification of ECs and pericytes" %}

### Pericyte coverage

{% include img src="sproutanalyzer-pericytecoverage" width="400" alt="Pericyte coverage measurement" %}

## Publication

{% include citation %}
