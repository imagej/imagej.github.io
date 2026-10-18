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


| | {{ stream }} SNT Stream | {{ crop }} In-Memory Image |
|---|---|---|
| **Image data** | Streamed and tiled. Only the displayed region/resolution is loaded | Fully loaded in memory |
| **Tracing algorithm** | A* only (currently). See [limitations](./big-data#limitations-and-idiosyncrasies) | A*, NBA*, Fast Marching |
| **Filters, widgets requiring entire images, and ImageJ-specific workflows (ROIs, etc.)** | [Materialized regions](#materialized-regions) only | Available |
| **Lasso selection, path orientation, brightest-voxel click, paint mode** | [Materialized regions](#materialized-regions) only |  Available |
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

1. Choose **Materialize Region...** in the [Options tab](./manual#-views) of the main SNT window.
2. Choose what to crop: the image being traced (or its secondary layer) and the bounding box: around all paths, around selected paths, one of several presets (e.g., 1024×1024×512 px), or custom dimensions. The box is centered on the scene by default, or on custom coordinates, and is padded by the specified amount (10 calibrated units, by default).
3. Check the estimated size shown at the bottom of the dialog. The region must fit in 80% of the memory still available to Fiji. Regions of 500 MB or more take a while to assemble.
4. Click **Materialize**. The region opens as a traditional image (_Materialized Region_), and {{ crop }} features are enabled.

While a region is materialized, tracing is scoped to its bounds. Note that:

- Only path geometry is retained. Pixel edits made on the crop are not saved.
- A* and automated tracing started after materializing are limited to the region, until another region is materialized.
- Only the channel and timepoint currently traced are copied. To crop another one, make it the one being traced and open the dialog again.
- If the voxel size of the dataset could not be read, SNT warns about it: Please verify that the calibration is correct, since a wrong calibration would crop the wrong location.


## Editing

Edit Mode ({% include key keys='Shift|E' %}) works as in any SNT canvas. In addition to _Connect To..._ ({% include key key='C' %}), Stream offers [Quick Connect](./manual#-quick-connect--8679-shiftc) ({% include key keys='Shift|C' %}), which does not require the child path to be pre-selected.


## Performance Tips for Stream Mode (BVV)

Streaming large pyramidal datasets (N5, OME-Zarr, or even HDF5/IMS files), especially from remote storage such as S3, is limited by how
quickly tiles can be fetched and uploaded to the GPU. The settings below can be adjusted in either the [preferences dialog](./manual#misc)
(if a restart is required) or in BVV's [scene controls](#scene-controls) toolbar.

The defaults _should_ be suitable for most cases, and the guidance below is based on benchmarks of a remote 62708x52320x25187 OME-Zarr (16 MB chunks)
navigated along the waypoints of a large reconstruction.

### Render Quality

| Preset | Use it for |
|---|---|
| Low (256x256, 15 ms, dithered) | Remote data, slow GPUs, laptops. Fewest tile requests and the smoothest navigation |
| **Medium (512x512, 30 ms)** | Default. Good balance for everyday navigation and tracing |
| High (768x768, 60 ms) | Analysis and screenshots, once the view has settled |
| Max (1024x1024, 100 ms) | High-end GPUs only. Slowest rendering |

Lower presets render fewer pixels per frame and request fewer tiles: on remote data, *Low* required about 3x fewer
chunk downloads and caused about 4x fewer GUI stalls than *Medium*. If navigation feels laggy, lowering this
setting is the most effective change. **Applies the next time a BVV window is opened**

### GPU Tile Cache (MB)

Leave at **0 (automatic)** for default performance: about 1 GB per displayed channel, limited to 2 GB or 25% of the JVM's maximum memory,
whichever is lower. Increase it only if tiles flicker or reload while panning and zooming (symptoms that the cache is too small
and cannot hold the tiles of the current view). The value is bounded by the memory of your graphics card. **Applies the next time a BVV
window is opened**.

### Tile Fetcher Threads

Leave at **0 (automatic)** for default performance: 64 threads for remote data (S3/HTTPS), and the number of CPU cores minus one for local
files. For remote data, 64 threads performed better than 32, but more threads don't seem to help further: throughput is then
limited by the network and the server (about 16 chunks/s for 16 MB chunks in our tests). Since every chunk in flight
is held in memory, 64 threads and 16 MB chunks require about 1 GB of heap. On computers with little memory, lower the value (and see
{% include bc path="Edit|Options|Memory & Threads..." %}). **Applies the next time a dataset is opened**.

### Advanced Options

These are not in the Preferences dialog, and are only needed for troubleshooting, benchmarking, or expert fine-tuning.
They are set at startup as system properties, e.g., `-Dsnt.bvv.gpuBlock=32`.

| Property | Default | Description |
|---|---|---|
| `snt.bvv.gpuBlock` | 64 | Edge length (voxels) of the tiles uploaded to the GPU: 32, 64 or 128. Larger tiles mean fewer uploads and less padding overhead (about 10% at 64 vs. 20% at 32). 64 felt more responsive than 32 in our tests, but the difference was within the run-to-run noise |
| `snt.bvv.noQueueSync` | off | Disables dropping of stale tile requests when the view changes (enabled by default: roughly halves chunk downloads and GUI stalls) |
| `snt.profile` | off | Prints timing statistics of tile loading, rendering and GUI responsiveness (additional flags: `snt.profile.n5`, `snt.profile.edt`) |

See [Performance Profiling](./extending#profiling-snt) for details.

### Rendering Accuracy

The *maximum ray-marching step* (Stream mode toolbar) trades rendering fidelity for speed: 1 voxel (default) samples
every voxel along each ray, larger values are faster but can miss thin structures. It does not affect the placement of
nodes.

### Measuring Performance

For reproducible comparisons, scripts can play a walkthrough along paths at constant speed and report how well the viewer kept up:

```groovy
// Groovy: 100 um/s along the selected paths, 500 um wide field of view

#@ SNTService snt
def bvv = snt.getUI().getActiveBigViewer()
def player = bvv.playPaths(snt.getSelectedPaths(), 100, 500)
player.onFinished { println player.getSummary() }
```

Compare the *elapsed* and *ideal* times (and the number of long gaps) between settings, and repeat each measurement
several times: results on remote data vary with network conditions.


## See Also

- [Big Data](./big-data): Loading data, supported file formats, BVV vs BDV, Slab View, and current limitations
- [Key Shortcuts](./key-shortcuts): Shortcuts for both traditional and streamed canvases
