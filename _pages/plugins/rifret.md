---
title: RiFRET
name: RiFRET
license-url: /licensing/gpl
license-label: GPLv3
dev-status: Active
support-status: Active
team-founders: [János Roszik, Duarte Lisboa, János Szöllosi, György Vereb]
team-leads: "@camlloyd"
team-developers: "@camlloyd"
team-debuggers: "@camlloyd"
team-reviewers: "@camlloyd"
team-support: "@camlloyd"
team-maintainers: "@camlloyd"
categories: [Analysis]
doi:
- 10.1038/s41598-023-30098-w
- 10.1002/cyto.a.20747
---

*An ImageJ plugin for intensity-based three-filter set (ratiometric) FRET which works with unknown varying donor/accepter ratios, corrects for channel crosstalk and instrument calibration, and yields quantitative FRET E values.*

## Introduction

Assesment of molecular interactions is often based on Förster (fluorescence) resonance energy transfer (FRET). Several methods rely on measuring fluorescence intensities of the donor and acceptor to determine the extent of FRET from donor quenching and/or sensitized acceptor emission. Many of these arrive at FRET indices which are semiquantitative, qualitative, or outright ignorant of actual donor-acceptor ratios.
The 3-cube approach is based on measuring donor emission upon donor-specific excitation, acceptor emission upon acceptor-specific excitation and acceptor emission upon exciting the donor. Properly describing the sources of the signal in each channel -- taking spectral crosstalk, instrument sensitivity, and varying donor-acceptor ratio into account -- allows for deriving a quantitatively correct expression for FRET efficiency. This approach has been implemented in the RiFRET plugin for analysis of microscopic images. The current version also incorporates pixel-by-pixel autofluorescence correction and batch mode analysis of large datasets.

## Installation

1. Download the latest version of [Fiji](https://fiji.sc/). 
2. Enable the FRET Imaging [update site](https://imagej.net/update-sites/following).
3. Once installed, go to _Plugins > FRET Imaging > RiFRET_.

## Usage

Download the help file as a PDF [here](/media/RiFRET_2.0.0_helpfile.pdf).

## Citation

This software is based on a publication. If you use it in your work, please cite:
{% include citation %}

## See also

If you are using the acceptor photobleaching FRET method, we recommend our other FRET plugin [AccPbFRET](/plugins/accpbfret).
