---
title: BioVoxxel 3D Box
name: Jan Brocher
affiliation: BioVoxxel
forum: biovoxxel
github: biovoxxel
website: https://www.biovoxxel.de
icon: https://biovoxxel.github.io/bv3dbox/images/bv3dbox-logo.png
categories: [Particle Analysis, Segmentation]
release-url: https://github.com/biovoxxel/bv3dbox/releases/tag/v1.0.1a
dev-status: Active
support-status: Active
license-url: https://github.com/biovoxxel/bv3dbox/blob/main/LICENSE
license-label: BSD-3
source-url: https://github.com/biovoxxel/bv3dbox
source-label: bv3dbox
---

# BioVoxxel 3D Box (bv3dbox)

Most of the known [BioVoxxel Toolbox](https://github.com/biovoxxel/BioVoxxel-Toolbox) functions now for 2D and 3D images in one place. All functions are heavily based on GPU computing via the fabulous [CLIJ2 library](https://clij.github.io/). Segmentation output is based stronger on labels (intensity coding of objects) instead of ROIs. Those labels can be equivalently used like ROIs with many CLIJ2 functions. Also label images created via other tools such as [MorphoLibJ](https://imagej.net/plugins/morpholibj) are suitable inputs for any plugin using labels.

![image](https://user-images.githubusercontent.com/10721817/152758424-ec724aa7-7202-4047-a530-8420b87f38c9.png)

---

## Version
![GitHub](https://img.shields.io/github/license/biovoxxel/bv3dbox?style=plastic)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/biovoxxel/bv3dbox?include_prereleases&style=plastic)

---

## Functionalities and Details
**All functions are described in detail here: [BioVoxxel 3D Box Github page](https://biovoxxel.github.io/bv3dbox/)**

---

## Installation
The BioVoxxel 3D Box are distributed via the [BioVoxxel 3D Box (bv3dbox) update site](https://imagej.github.io/list-of-update-sites/)

---

### Citation
If you use this library and its functions to generate and publish results, please condider to acknowledge and cite the toolbox using the DOI.

[![DOI](https://zenodo.org/badge/434949702.svg)](https://zenodo.org/badge/latestdoi/434949702)

---

### Issues

![GitHub issues](https://img.shields.io/github/issues/biovoxxel/bv3dbox?style=plastic)

**REMARK: This is currently still in alpha release stage and should be handled with care when creating results. Please inform me about any [issues](https://github.com/biovoxxel/bv3dbox/issues) you encounter!**

[https://github.com/biovoxxel/bv3dbox/issues](https://github.com/biovoxxel/bv3dbox/issues)

---

### Acknowledgement
The BioVoxxel 3D Box funtions are heavily based and rely strongly on the CLIJ library family.
Therefore, this development would have not been possible without the work of Robert Haase and colleagues.

Robert Haase, Loic Alain Royer, Peter Steinbach, Deborah Schmidt, Alexandr Dibrov, Uwe Schmidt, Martin Weigert, Nicola Maghelli, Pavel Tomancak, Florian Jug, Eugene W Myers. [CLIJ: GPU-accelerated image processing for everyone. Nat Methods (2019)](https://doi.org/10.1038/s41592-019-0650-1)

J. Ollion, J. Cochennec, F. Loll, C. Escudé, T. Boudier. (2013) TANGO: A Generic Tool for High-throughput 3D Image Analysis for Studying Nuclear Organization. Bioinformatics 2013 Jul 15;29(14):1840-1. http://dx.doi.org/10.1093/bioinformatics/btt276
