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

{% include notice icon="snt-stream" content="**[SNT Stream](./snt-stream) remains experimental. This page may describe preliminary features**." %}


**SNT Stream** is a suite of modifications that allows SNT to trace directly against a streamed dataset rendered in [Big Volume Viewer](./manual#big-volume-viewer) or [Big Data Viewer](./manual#big-data-viewer)
without materializing the volume in memory. It allows SNT to handle [TB-sized images](./big-data): Datasets are virtually-streamed, so you never need to downsample or crop a large volume just to get it into a tracing-capable window


## Getting Started

1. Choose _Big Data..._ from the [Shortcuts Window](./manual#snt-commands) and select **Big Volume Viewer (BVV): 3D rendering w/ tracing capabilities** as the viewer type
2. Once the BVV window opens, trace as you would in any other SNT canvas: Click to place nodes for manual tracing, or use [semi-automated tracing](/plugins/snt/walkthroughs#semi-automated-tracing) the same way you would with an in-core image
3. Press **Enter** to finish the current path, or **Esc** to discard it
4. Press **Z**, or use the **Undo Last Segment** button on the toolbar, to step back one click at a time along the path currently being traced
5. Switch the active channel/frame from the toolbar as needed; only one is streamed for tracing at a time (see [big data limitations](./big-data#limitations-and-idiosyncrasies))
6. Finished paths land in the Path Manager exactly as they would from any other SNT session: save, curate, and analyze them as usual
7. If tracing manually, use [Re-trace With A*](manual#re-trace-with-a) asynchronously to refine the curvature of traced paths
