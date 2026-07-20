---
title: SNT › Big Data
nav-links: true
nav-title: Big Data
artifact: org.morphonets:SNT
icon: /media/icons/snt.svg
forum-tag: snt
update-site: Neuroanatomy
tags: snt,tracing,segmentation,neuroanatomy,big-data
---

{% capture version%}
**This page was last revised for [version 5.1.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

# Big Data support

SNTv5 implemented _preliminary_ support for big data. The following operations are currently supported:

| Big Data Operation       | Status                                                                                      | Comments                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Manual tracing           | Supported<sup>1</sup> | |
| Semi-automated tracing   | Supported (experimental)<sup>1</sup> | Multi-dimensional images remain untested |
| Automated tracing        | Supported (experimental)                                                                    | See [Auto-tracing](./auto-tracing#grayscale-images)<sup>1,2</sup>                               |
| Tracing along way-points | Supported in headless scripts<sup>2</sup>                                                   | A* tracing performed using pre-existing coordinates is fully supported via scripting<sup>2</sup>|
| Path optimization        | Supported in headless scripts<sup>2</sup>                                                   | [Optimization of curvatures](./manual#refinefit-), including extraction of radii<sup>2</sup>   |
| 3D Visualization: Interactive re-slicing browser | Supported via [BigDataViewer](./manual#big-data-viewer) | Visualization of reconstructions, including [color mappings](./manual#color-mapping-), etc.  |
| 3D Visualization: Interactive volume viewer       | Supported via [BigVolumeViewer](./manual#big-volume-viewer) and [sciview](./manual#sciview) | Visualization of 3D reconstructions, including [color mappings](./manual#color-mapping-), etc.  |

<sup>1</sup>For collaborative tracing, please use [HortaCloud](https://hortacloud.org/): This is SNT's development team recommended tool for tracing Terabyte-size datasets

<sup>2</sup>See [PySNT](https://pysnt.readthedocs.io/en/latest/)


## Getting Started
<img align="right" width="450" src="/media/plugins/snt/snt_BVVCmd.png" alt="BDV/BVV Prompt (v.5.1)" title="BDV/BVV Prompt (v.5.1)" />

Choose _BDV/BVV..._ from the [Neuroanatomy Shortcuts Window](./manual#snt-commands). In the prompt you can specify:

- **Main volume**: The primary image volume. Supported files include: standard files, IMS, BDV XML/HDF5, N5, and OME-Zarr/OME-NGFF containers

- **Secondary volume**: Optional image volume. Useful for loading a processed version of the main volume, or a secondary channel saved to a separated file

- **Reconstruction files**: Optional. Either a single file (TRACES, SWC, JSON, etc.), or a folder containing multiple reconstruction files. Reconstructions can also be imported later on

- **Markers file**: Optional. A CSV file containing bookmarked locations. Markers can also be imported later on

- **Viewer type**: Defines the viewer type. Either:
  - **2D: Big Data Viewer (BDV)**: Interactive re-slicing browser
  - **3D: Big Volume Viewer (BVV)**: Interactive volume viewer
  - **3D: Big Volume Viewer (BVV) with tracing capabilities**: Similar to _3D: Big Volume Viewer (BVV)_ but tracing is possible. A new SNT is initialized in "big data mode" side-by-side the viewer

{% include notice icon="info" content="**Tracing in BVV remains experimental**." %}


## Supported File Formats

[Big volume viewer](./manual#big-volume-viewer) is at the core of Big-data support. Standard formats (TIFF, and anything readable via Bio-Formats) are loaded as regular in-memory volumes, with an option to downsample automatically if a volume exceeds the GPU's 3D texture limits. Imaris (.ims) files are supported via an automatically generated BDV-XML sidecar written next to the original file.

For genuinely large datasets, BDV XML/HDF5, N5, and OME-Zarr/OME-NGFF containers are opened virtually: data is streamed from disk in blocks as needed. N5 and Zarr containers are read directly, with no XML sidecar required.
