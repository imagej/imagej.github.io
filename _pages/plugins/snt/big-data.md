---
title: SNT › Big Data
nav-links: true
nav-title: Big Data
artifact: org.morphonets:SNT
icon: /media/icons/snt.svg
forum-tag: snt
update-site: Neuroanatomy
tags: snt,tracing,segmentation,neuroanatomy,big-data,snt-stream
---

{% capture version%}
**This page was last revised for [version 5.1.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice icon="snt" content=version %}

# Big Data Support

SNTv5 implemented _preliminary_ support for big data: images too large to fit in CPU/GPU memory (BDV XML/HDF5, N5, and OME-Zarr/OME-NGFF containers) can be opened virtually and browsed or reconstructed without ever loading the full volume.
Most of this support is provided through [Big Data Viewer](./manual#big-data-viewer) and [Big Volume Viewer](./manual#big-volume-viewer).
The following operations are currently supported:

| Operation | Status | Comments |
|-----------|--------|----------|
| Manual and semi-automated tracing | Supported (experimental)<sup>1</sup> | Multi-dimensional images have not been thoroughly tested |
| Automated tracing | Supported (experimental) | See [Auto-tracing](./auto-tracing#grayscale-images)<sup>1,2</sup> |
| Tracing along way-points | Supported | |
| [Path optimization](./manual#refinefit-) | Supported | |
| 3D Visualization: Interactive re-slicing browser | Supported via [BigDataViewer](./manual#big-data-viewer) | |
| 3D Visualization: Interactive volume viewer | Supported via [BigVolumeViewer](./manual#big-volume-viewer) and [sciview](./manual#sciview) | Includes [Slab View](#slab-view) for restricting rendering to a thin, adjustable region of the volume |
| Multidimensional operations | Limited support | Tracing handles one active channel/frame at a time for performance reasons. Commands that require exposing all channels/frames to be available at once [may not be supported](#limitations-and-idiosyncrasies) |

<sup>1</sup>For collaborative tracing, please use [HortaCloud](https://hortacloud.org/): This is SNT's development team recommended tool for tracing Terabyte-size datasets in a collaborative environment

<sup>2</sup>See [PySNT](https://pysnt.readthedocs.io/en/latest/)

## Getting Started
<img align="right" width="450" src="/media/plugins/snt/snt_big_data_prompt.png" alt="Big Data Prompt (v.5.1)" title="Big Data Prompt (v.5.1)" />

Choose _Big Data..._ from the [Shortcuts Window](./manual#snt-commands). In the prompt you can specify:

- **Main volume**: The primary image volume. Supported files include: standard files, IMS, BDV XML/HDF5, N5, and OME-Zarr/OME-NGFF containers

- **Secondary volume**: Optional image volume. Useful for loading a processed version of the main volume, or a secondary channel saved as a separated file

- **Reconstruction file(s)**: Optional. Either a single file ([TRACES, SWC, JSON, etc.](./manual#load-tracings-)), or a folder containing multiple reconstruction files. Reconstructions can also be imported later on using the _SNT Controls_ toolbar

- **Markers file**: Optional. A CSV file containing [bookmarked](./manual#bookmarks-tab) locations. Markers can also be imported later on using the _SNT Controls_ toolbar

- **Viewer type**: Defines the viewer type. Either:
  - **Big Data Viewer (BDV): Interactive reslicing**: Interactive re-slicing browser
  - **Big Volume Viewer (BVV): 3D rendering**: Interactive volume viewer, no tracing
  - **Big Volume Viewer (BVV): 3D rendering w/ tracing capabilities**: Same as _Big Volume Viewer (BVV): 3D rendering_, but a new SNT instance is initialized as **[SNT Stream](./snt-stream)**, turning the BVV viewer into a functional tracing canvas

{% include notice icon="info" content="**[SNT Stream](./snt-stream) remains experimental**." %}


## Limitations and Idiosyncrasies

- **One channel/frame at a time**: for performance reasons, one channel/frame is streamed for tracing at once. Commands that require all channels/frames available simultaneously (e.g., [Multispectral Refinement](./manual#multispectral-refinement)) are not supported
- **Fixed search algorithm**: the A* search algorithm is used for interactive tracing; the alternate NBA*/Fast Marching options available for in-core images may not be offered in Stream mode
- **Image statistics**: Access to cost-function tuning and [image-statistics options](./manual#algorithm-settings). _Compute Real-Time_ (the default) recalculates local statistics as you trace new regions. _Compute Now For Whole Image_ scans the entire streamed dataset once; because this can be _slow_ depending on dataset size and network/disk speed
- **3D Scene recentering on click**: whether/how the view recenters as you place tracing points is configurable from the toolbar's options menu (_Never_ / _Adaptive_ / _Always_). _Adaptive_ is the recommended default for streamed data: it skips recentering for clicks that already land close to the focal plane, and briefly gates subsequent clicks after a recenter fires, giving tile streaming time to catch up
- **Path fitting and automated tracing**: Supported the same way as for in-core images; see [Auto-tracing](./auto-tracing#grayscale-images) and [Path optimization](./manual#refinefit-)


## Slab View

Slab View restricts BVV's rendering to a thin, adjustable region of the volume, making it easier to inspect internal structure in dense or large datasets without having to rotate away obstructing tissue.
Also, it may reduce data fetched from remote sources, depending on BVV's internal caching behavior.
It is a general rendering feature, available in _Scene Controls_ whenever a BVV canvas is open, even outside active [SNT Stream](./snt-stream) tracing sessions.

- **Controls**: toggle with the _Slab View_ button; a _Position_ slider moves the slab through the volume, and a _Thickness_ spinner controls how much of the volume is included around that position
- **Orientation**: Slab View must be activated from one of the three canonical planes (XY/XZ/ZY), needed to give the slab an initial axis to work from. Once active, the view can be freely rotated; Slab View only turns itself off if the volume genuinely rotates out of the visible slab
- **Slab Paths / Slab Annotations**: optional toggles that restrict rendered reconstructions/markers to the same slab window, so paths outside the slab don't clutter the view. _Slab Paths_' on/off state is remembered as a preference across Slab View activations; _Slab Annotations_ resets each time

## Supported File Formats

[Big volume viewer](./manual#big-volume-viewer) and [Big data viewer](./manual#big-data-viewer) are at the core of Big-data support. Standard formats (TIFF, and anything readable via Bio-Formats) are loaded as regular in-memory volumes, with an option to downsample automatically if a volume exceeds the GPU's 3D texture limits. Imaris (.ims) files are supported via an automatically generated BDV-XML sidecar written next to the original file.

For genuinely large datasets, BDV XML/HDF5, N5, and OME-Zarr/OME-NGFF containers are opened virtually: data is streamed from disk in blocks as needed. N5 and Zarr containers are read directly, with no XML sidecar required.
