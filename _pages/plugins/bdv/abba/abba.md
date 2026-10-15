---
title: Aligning Big Brains & Atlases
artifact: ch.epfl.biop:ImageToAtlasRegister
nav-links: true
toc: true
---

Aligning Big Brains & Atlases, or ABBA for short, is a Fiji plugin to register thin serial sections of brains to
3D atlases, in coronal, sagittal and horizontal orientations.

The complete documentation of ABBA is at
[https://abba-documentation.readthedocs.io](https://abba-documentation.readthedocs.io).

## Features

* **Atlases**: the [Allen mouse brain atlas](http://atlas.brain-map.org/atlas?atlas=602630314) (CCFv3), the
  [Waxholm Space atlas of the Sprague Dawley rat brain](https://www.nitrc.org/projects/whs-sd-atlas), and all the
  [BrainGlobe atlases](https://brainglobe.info/), opened directly in Fiji.
* **Automated registration**: [DeepSlice](https://github.com/PolarBean/DeepSlice) positions the sections along
  the atlas, [elastix](https://elastix.dev/) refines each one with affine and spline registrations. Both are
  installed by ABBA itself the first time they are used: nothing else to install or configure.
* **Manual correction**: position sections by hand, and edit any registration, with
  [BigWarp](/plugins/bigwarp) for spline registrations.
* **Large images**: ABBA uses [BigDataViewer](/plugins/bdv) to display and transform multiresolution images, the
  typical output of whole slide imaging, on the fly.
* **QuPath**: a [QuPath](https://qupath.github.io) project can be the input of ABBA, and the registered atlas
  regions are imported back into QuPath for cell detection and counting per region.
* **AI assistant** (experimental): through [abba-mcp](https://github.com/unige-biochem/abba-mcp), an AI
  assistant (in VS Code, Claude, Codex...) can run a registration in ABBA's window, where you can take over at any
  time.

## Installation

In Fiji, enable the `UNIGE-Biochem` [update site](/update-sites/following), then restart Fiji. ABBA needs Java 21,
which an up-to-date Fiji has.

ABBA can also be installed with an AI assistant, with a standalone installer, or from Python: see the
[installation page](https://abba-documentation.readthedocs.io/en/stable/installation/installation.html).

## Getting started

* [Getting started](https://abba-documentation.readthedocs.io/en/stable/getting_started/first_registration.html):
  a first registration, step by step, on demo sections that ABBA downloads for you.
* [Video tutorial](https://abba-documentation.readthedocs.io/en/stable/resources/video_tuto.html).
* Questions and bug reports: the [image.sc forum](https://forum.image.sc/tag/abba), with the `abba` tag.

## Citation

If you use ABBA, please cite:

Chiaruttini, N., Castoldi, C., Requie, L. et al. **ABBA+BraiAn, an integrated suite for whole-brain mapping,
reveals brain-wide differences in immediate-early genes induction upon learning**. *Cell Reports* (2025).
[doi:10.1016/j.celrep.2025.115876](https://doi.org/10.1016/j.celrep.2025.115876)

After the registration, [BraiAn](https://silvalab.codeberg.page/BraiAn/) analyses whole-brain datasets aligned with
ABBA.

ABBA was started at the [BioImaging & Optics Platform](https://www.epfl.ch/research/facilities/ptbiop/) of EPFL,
and is developed at the University of Geneva. Its sources are on
[GitHub](https://github.com/BIOP/ijp-imagetoatlas).
