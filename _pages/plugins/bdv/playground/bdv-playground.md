---
title: BigDataViewer Playground
artifact: sc.fiji:bigdataviewer-playground
nav-links: true
toc: true
---

BigDataViewer playground aims at a better integration of BigDataViewer into Fiji by using the [SciJava Framework](/libs/scijava). 

It also provides support for opening big files directly from the bio-formats and the OMERO Java APIs.

# Installation

Enable the [PTBIOP update site](/update-sites/following).

# What bigdataviewer-playground brings ?

## Modularity for BigDataViewer!

BigDataViewer playground creates a way to access existing BDV instances when scripting or writing java code. Being able to combine scripts or code for display and processing is doable via scripting (Groovy, ImageJ macro, etc.)

## Use the macro recorder for BigDataViewer

To some extent, scripting basic actions on BigDataViewer with the ImageJ macro recorder is possible.

## Direct and lazy opening of multiresolution files, supported by bioformats or OMERO

It is possible to open and visualize large files in BigDataViewer without resaving files. This is particularly convenient for large 2D images (à la QuPath).
You can use bigdataviewer-playground to create a dataset that can be re-used by any of the BigDataViewer ecosystem plugins (BigStitcher, BigWarp, Labkit...)

# Documentation summary

The documentation is split into several parts:

**[1 - Create/open](/plugins/bdv/playground/bdv-playground-open-dataset)**  a dataset


**[2 - Display](/plugins/bdv/playground/bdv-playground-visualize)**  a dataset


**[3 - Script](/plugins/bdv/playground/bdv-playground-scripting)** BDV
  
# Related software

## Aligning Big Brains and Atlases - ABBA

[ABBA](https://biop.github.io/ijp-imagetoatlas/), a tool to align 2D brain sections to 3D atlases, is built on top of BigDataViewer-Playground.

## Warpy

[Warpy](/plugins/bdv/warpy/warpy) is a Fiji + QuPath workflow designed to align, in a non-rigid manner, big 2D images.
  
 
## Tutorials

**[how to manually register a bdv dataset with bigdataviewer-playground](/plugins/bdv/playground/bdv-playground-manual-registration)**
**[Inspecting multiple Tissue Cores using the BigDataViewer and BigDataViewer Playground in Fiji](https://github.com/BIIFSweden/FOM_Multiplexed/blob/main/bdvPlayground.md)


## Other

A video on BigDataViewer general concepts, followed by a presentation of BigDataViewer Playground and [BigDataProcessor](https://github.com/bigdataprocessor/bigdataprocessor2)

{% include video platform="youtube" id="LHI7vXiUUms" aspect="1:1" %}












