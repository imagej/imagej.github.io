---
title: SNT › SNT Stream
name: SNT Stream
nav-links: true
nav-title: SNT Stream
artifact: org.morphonets:SNT
icon: /media/icons/snt-stream.svg
forum-tag: snt
update-site: Neuroanatomy
tags: snt,tracing,segmentation,neuroanatomy,big-data,snt-stream
---

{% include snt-modes %}
{% include notice icon="snt-stream" content="**SNT Stream remains experimental. This page may describe preliminary features**." %}


**SNT Stream** is a suite of modifications that allows SNT to trace directly against a streamed dataset rendered in [Big Volume Viewer](./manual#big-volume-viewer) or [Big Data Viewer](./manual#big-data-viewer)
without materializing the volume in memory. It allows SNT to handle [TB-sized images](./big-data): Datasets are virtually-streamed, so you never need to downsample or crop a large volume just to get it into a tracing-capable window.

## Getting Started

Choose _Big Data..._ from the [Shortcuts Window](./manual#snt-commands), specify the volume to be traced, choose a viewer type (BVV or BDV), and check _Enable tracing (SNT Stream)_. All inputs of the prompt, the [supported file formats](./big-data#supported-file-formats), and the differences between [BVV and BDV](./big-data#getting-started) are described in [Big Data](./big-data). To try Stream mode without loading your own data, use the _Load Remote Demo_ option of the prompt.

{% include notice icon="info" content="All inputs can be local paths or remote URLs. To try Stream mode without loading your own data, use the _Load Remote Demo_ option: It pre-fills all fields with a remote demo (marmoset neurons, OME-Zarr, with autotracings and soma markers, using BVV)." %}

#### Tracing
Tracing, editing, and shortcuts work the same way in both viewers. 

1. Once the viewer window opens, trace as you would in any other SNT canvas: Click to place nodes for manual tracing, or use [semi-automated tracing](./walkthroughs#semi-automated-tracing) the same way you would with an in-core image.
2. Press {% include key key='Enter' %} to finish the current path, or {% include key key='Esc' %} to discard it.
3. Press {% include key key='Z' %}, or use the **Undo Last Segment** button on the toolbar, to step back one click at a time along the path currently being traced.
4. Switch the active channel/frame from the toolbar as needed; only one is streamed for tracing at a time (see [big data limitations](./big-data#limitations-and-idiosyncrasies)).
5. Finished paths land in the Path Manager exactly as they would from any other SNT session: [save](./manual#save-tracings), [curate](./curation#curation-assistant), and [analyze](./analysis) them as usual.
6. If tracing manually, use [Re-trace With A*](./manual#re-trace-with-a) asynchronously to refine the curvature of traced paths.

## What Differs From In-Core Tracing

Most of SNT works the same way in a streamed scene and in an image loaded in memory: the same [shortcuts](./key-shortcuts) and [contextual menu](./manual#image-contextual-menu) apply, and paths are handled by the same Path Manager. The differences are summarized below. 

> Throughout the documentation, {{ crop }} flags features that require an image loaded in memory (a regular image, or a [materialized region](#materialized-regions) of a stream), and {{ stream }} flags features that only exist in SNT Stream.


| | {{ stream }} SNT Stream | {{ crop }} Image in Memory |
|---|---|---|
| **Image data** | Streamed and tiled. Only the displayed region/resolution is loaded | Fully loaded in memory |
| **Tracing algorithm** | A* only (currently). See [limitations](./big-data#limitations-and-idiosyncrasies) | A*, NBA*, Fast Marching |
| **Filters, widgets requiring entire images, and ImageJ-specific workflows (ROIs, etc.)** | Materialized regions only | Available |
| **Lasso selection, path orientation, brightest-voxel click, paint mode** | Materialized regions only |  Available |
| **[Spacebar behavior](#tracing-and-navigation)** | Panning and tracing toggle | Panning |
| **Unique workflows** | [Channel unmixing](#channel-unmixing), [slab controls](#slab-view) | Orthogonal views |

## Tracing and Navigation

Press {% include key key='Spacebar' %} to toggle between tracing and navigation (panning). Hold it down to switch to navigation temporarily: Release it to resume tracing. A message in the viewer confirms the current mode. This avoids a trip to the toolbar every time the scene needs to be repositioned.


## Showing and Hiding Annotations

The eye icon in the toolbar controls which SNT annotations are overlaid on the image:

- **Show/Hide All Annotations** toggles everything.
- **Hide Paths**, **Hide Seeds**, and **Hide Markers** toggle each layer independently, in any combination.

Hold {% include key key='H' %} to hide paths and annotations temporarily while it is pressed.


## Scene Controls

### Slab View
_BVV only._

Restricts the visible scene to a thin section of the volume, which is handy for inspecting (and tracing through) dense data. Toggle it from the _Scene Controls_ card. Thickness, position, and the options to restrict paths and markers to the slab are described in [Big Data](./big-data#slab-view). Slab View is also required by [channel unmixing](#channel-unmixing) of multi-resolution data.

### Source Label and Scale Bar

The toolbar of the _Scene Controls_ card has toggles for the source name overlay and for a scale bar:

- **Text Overlay**: Right-click to choose the position of the source name (_Top center_ or _Top right_).
- **Scale Bar**: Off by default. Right-click to override the spatial calibration (voxel size and unit), and to set the foreground and background colors of the bar.

{% include notice icon="info" content="Changing the calibration through the scale bar dialog also overrides it in SNT. If the dataset stores a different calibration (e.g., OME-Zarr), SNT offers to save the new one so that it is used next time." %}


## Channel Unmixing

Autofluorescence and bleed-through often make a structure of interest show up in more than one channel. For multichannel datasets, the _Channel Unmixing_ card (above _Scene Controls_ in the viewer) subtracts a weighted _background_ channel from a _signal_ channel:

> result = signal − w × background

with the display ranges (black/white levels) of both channels used to normalize the subtraction. The result is 16-bit and the unmixed channel replaces the original channels in the scene. Tracing proceeds against it.

1. Choose the **Signal** channel (the one to keep) and the **Background** channel.
2. Adjust the brightness and contrast of both channels so that an autofluorescent feature looks equally bright in both. The unmixed result depends on these ranges, so any later change recomputes it.
3. Toggle **Enable** and raise the weight **w** (0 to 1) until the bleed-through disappears. Higher weights may clip signal.
4. The reset button restores the original channels.

In BDV the result updates live. In BVV, it is computed when the slider is released, and only for the current slab, so activate a thin [slab](#slab-view) first (this is required for multi-resolution data). The result is single-resolution: SNT lets you know which resolution level was used.

### Unmixing the Whole Volume

The unmixing above is a preview of what the current slab would look like. To apply it to the entire dataset, choose **Unmix Full Volume...** from the **Options** menu of the card. SNT generates a Groovy script, pre-filled with the current channels, weight and display ranges, so that the offline result matches what you see in the viewer. Run it from Fiji's Script Editor (_Language ▷ Groovy_).

The script writes a multi-resolution OME-Zarr next to the input dataset. Existing files are never overwritten (a numeric suffix is added instead). Level 0 is computed one slab at a time, so volumes larger than the available memory are fine, and the result can be streamed back into BVV/BDV as any other dataset.

Note that:

- The command is only available for datasets loaded from a file (BDV XML, IMS, N5, or OME-Zarr), not for images already open in Fiji.
- All timepoints are exported, with the time stored as the last axis of the OME-Zarr.
- The script aborts if the channel count of the dataset differs from the one in the viewer.


## Materialized Regions

Some [features](#what-differs-from-in-core-tracing) need pixel data in memory. A _materialized region_ is a 3D crop of the streamed volume that is copied into memory as a regular image, so these features become available for that region.

1. Choose **Materialize Region...** in the _Options_ tab of the main SNT window (it replaces the _Create Canvas_ button of in-core tracing).
2. Choose what to crop: the image being traced (or its secondary layer) and the bounding box: around all paths, around selected paths, one of several presets (e.g., 1024×1024×512 px), or custom dimensions. The box is centered on the scene by default, or on custom coordinates, and is padded by the specified amount (10 calibrated units, by default).
3. Check the estimated size shown at the bottom of the dialog. The region must fit in 80% of the memory still available to Fiji. Regions of 500 MB or more take a while to assemble.
4. Click **Materialize**. The region opens as the SNT canvas (_Materialized Region_), and {{ crop }} features are enabled.

While a region is materialized, tracing is scoped to its bounds. Note that:

- Only path geometry is retained. Pixel edits made on the crop are not saved.
- A* and automated tracing started after materializing are limited to the region, until another region is materialized.
- Only the channel and timepoint currently traced are copied. To crop another one, make it the one being traced and open the dialog again.
- If the voxel size of the dataset could not be read, SNT warns about it: Please verify that the calibration is correct, since a wrong calibration would crop the wrong location.


## Editing

Edit Mode ({% include key keys='Shift|E' %}) works as in any SNT canvas. In addition to _Connect To..._ ({% include key key='C' %}), Stream offers **Quick Connect** ({% include key keys='Shift|C' %}), which does not require a secondary path:

1. Press {% include key keys='Shift|C' %} (or choose _Quick Connect..._ from the contextual menu) with the cursor near the node of the edited path that should be connected.
2. Move the cursor over the node to connect to: the cursor snaps to the closest node of any other path (within 150 pixels), a dotted line shows the link, and the status message reports the gap.
3. Click, press {% include key key='Enter' %}, or press {% include key keys='Shift|C' %} again to connect. Press {% include key key='Esc' %} to cancel.

The edited path becomes the child of the target. Branches of the edited path are dimmed, since connecting to them would create a loop.


## See Also

- [Big Data](./big-data): Loading data, supported file formats, BVV vs BDV, Slab View, and current limitations
- [Key Shortcuts](./key-shortcuts): Shortcuts for both traditional and streamed canvases
