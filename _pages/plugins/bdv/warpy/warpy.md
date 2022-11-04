---
title: Warpy
artifact: ch.epfl.biop:bigdataviewer-biop-tools
nav-links: true
toc: true
---

{% include notice icon="info"
  content="For questions and issues, please use [forum.image.sc](https://forum.image.sc/)" %}

{% include notice icon="info"
  content="Do you find this workflow useful ? Please cite us: **[An Open-Source Whole Slide Image Registration Workflow at Cellular Precision Using Fiji, QuPath and Elastix - Frontiers in Computer Science](https://doi.org/10.3389/fcomp.2021.780026)**" %}

**Warpy** is a workflow that provides a way to register whole slide images in [Fiji](https://fiji.sc/) and analyze their result in [QuPath](https://qupath.github.io/) (v0.3+). It is designed to register slides that require transformations which are **more complex than affine transform**, by using the [ImgLib2 library](https://imagej.net/libs/imglib2/), [elastix](https://github.com/SuperElastix/elastix), and [BigWarp](https://github.com/saalfeldlab/bigwarp).

It consists of two components:

* **[Warpy](/plugins/bdv/warpy/warpy-extension)** itself is the component that allows to perform the registration, by using Fiji as an intermediate step. It outputs a transformation which is readable in QuPath and which allows to transfer regions of interest from one image to the registered ones. However, the image itself is not transformed. **Installation instructions are included in this part of the documentation**

* **[Image Combiner Warpy](/plugins/bdv/warpy/warpy-image-combiner)** allows to use Warpy outputs to generate an on-the-fly composite image combining one or several transformed images as a new QuPath Entry (=image). These new QuPath entries can be stored, visualized, exported and analyzed (with caution).

{% include notice icon="info"
  content="Warpy Image Combiner itself can be used independently of Warpy. In this case, only affine transformations are supported, which can be sufficient for many use cases." %}

{% include img name="Warpy general workflow" src="/media/plugins/bdv/warpy/warpy-general-workflow.jpg" %}
*Workflow overview - The set of images to be registered are all put into a single QuPath project. Registrations are performed in Fiji, images are opened from a QuPath project and each registration result is stored as a file within the Redundant project entry folder. For the analysis, thanks to the registration result found between two images, regions of interest can be transferred in QuPath from one image to another, in order to generate correlated data. It is additionally possible to create a new combined image within QuPath.*

# Videos tutorials

[Playlist](https://www.youtube.com/watch?v=cgRA9NZ-AOo&list=PL2PJpdamvnti8PqyMdcezGLeAtH6LSy69)

## Installation

{% include video platform="youtube" id="cgRA9NZ-AOo" aspect="1:1" %}

## Registration

{% include video platform="youtube" id="s5GoNND6Mho" aspect="1:1" %}

## Analysis

{% include video platform="youtube" id="ckqdrx0OvsI" aspect="1:1" %}


# Code

All code of the Warpy workflow can be found within these repositories:

* [bigdataviewer-playground](https://github.com/bigdataviewer/bigdataviewer-playground)
* [bigdataviewer-biop-tools](https://github.com/BIOP/bigdataviewer-biop-tools)
* [qupath-extension-warpy](https://github.com/BIOP/qupath-extension-warpy)

# Legacy

There is a legacy version of this workflow which was working with QuPath v.0.2.3. [It can be accessed here](https://c4science.ch/w/bioimaging_and_optics_platform_biop/image-processing/wsi_registration_fjii_qupath/).