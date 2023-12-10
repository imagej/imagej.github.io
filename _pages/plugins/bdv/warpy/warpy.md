---
title: Warpy
artifact: qupath.ext.warpy:qupath-extension-warpy
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

# Troubleshooting

Something's wrong in this documentation ? Please post your issue or question in the [image.sc forum](forum.image.sc).

List of solved issues encountered and reported in the forum:

[https://forum.image.sc/search?q=warpy%20status%3Asolved](https://forum.image.sc/search?q=warpy%20status%3Asolved)

# References

## Papers
- [Fiji](http://www.nature.com/nmeth/journal/v9/n7/full/nmeth.2019.html)
- [QuPath](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5715110/) 
- [BigWarp](http://ieeexplore.ieee.org/document/7493463/)
- [Elastix (1)](http://dx.doi.org/10.1109/TMI.2009.2035616) [Elastix (2)](http://dx.doi.org/10.3389/fninf.2013.00050)
- [BigDataViewer](http://www.nature.com/nmeth/journal/v12/n6/full/nmeth.3392.html)

## Source code

The code to perform this workflow is splitted in several parts:

[Qupath warpy extension](https://github.com/BIOP/qupath-extension-warpy) and several repositories for the Fiji side. On the Fiji side, the main components are [Bigdataviewer-playground](https://github.com/bigdataviewer/bigdataviewer-playground) for the management of multiple sources and [Bigdataviewer-biop-tools](https://github.com/BIOP/bigdataviewer-biop-tools).

# Legacy

There is a legacy version of this workflow which was working with QuPath v.0.2.3. [It can be accessed here](https://c4science.ch/w/bioimaging_and_optics_platform_biop/image-processing/wsi_registration_fjii_qupath/).
