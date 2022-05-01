---
title: MaMuT
project: /software/fiji
description: MaMuT, the plugin to track and lineage cells in large, multi-view images.
categories: [Tracking]
artifact: sc.fiji:MaMuT
logo: /media/icons/mamut.png
doi: 10.7554/eLife.34410
---

*A Fiji plugin for the annotation of massive, multi-view data.*

## Installation.

Enable the [MaMuT update site](http://sites.imagej.net/MaMuT/) in the [Fiji updater](/plugins/updater) to get MaMuT.



## Publication.

{% include citation doi='10.7554/eLife.34410'%}

## Presentation.

MaMuT is an end user plugin that combines the [BigDataViewer](/plugins/bdv) and [TrackMate](/plugins/trackmate) to provide an application that allow browsing, annotating and curating annotations for large image data.

<figure><img src="/media/plugins/mamut/mamut-presentation.png" title="MaMuT_presentation.png" width="600" alt="MaMuT_presentation.png" /><figcaption aria-hidden="true">MaMuT_presentation.png</figcaption></figure>

The main window resembles the display panel of [TrackMate](/plugins/trackmate). It controls how the annotations are displayed. Using the *MaMuT Viewer* button, several views of the data can be launched. They will all be in sync. Each of them is an instance of the [BigDataViewer](/plugins/bdv).

![](/media/plugins/mamut/mamut-windowsinsync.png)

We privileged annotations that are like lineages, or object followed over time (which is what [TrackMate](/plugins/trackmate) does). MaMuT ships [TrackScheme](/plugins/trackmate/trackscheme), the lineage browser taken from TrackMate.

![](/media/plugins/mamut/mamut-withtrackscheme.png)

However, MaMuT itself does not ship any fully-automated or tracking algorithm. It is meant for manual or semi-automatic annotation. Still, we made the GUI comfortable enough so that you can quickly generate rather large annotations. A semi-automated segmentation can help you generating quickly lineage branches from single cells.

![](/media/plugins/mamut/mamut-largeannotationsquickly.png)

## User documentation.

The following pages are tutorials that will guide you through MaMuT and walk you though its features.

-   [Getting started with MaMuT](/plugins/mamut/getting-started) is an introduction tutorial. It will show you how to prepare a dataset for MaMuT and make your first annotations with it.

<!-- -->

-   [Example mamut.properties file](/plugins/mamut/example-properties-file) contains an example of a `mamut.properties` file, that is used to customize the key-bindings in the MaMuT viewer.

