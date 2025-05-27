---
title: Mastodon
description: Mastodon is a large-scale tracking and track-editing framework for large, multi-view images, such as the ones that are typically generated in the domain Development Biology or Stem-Cell Biology or Cell Biology.
categories: [Segmentation,Tracking]
artifact: org.mastodon:mastodon
---

*Mastodon is a large-scale tracking and track-editing framework for large, multi-view images, such as the ones that are typically generated in the domain Development Biology or Stem-Cell Biology or Cell Biology.*

{% include img name="Mastodon logo" src="/media/plugins/mastodon/Mastodon-logo_jy-01-512.png" width="250px" %}

Why using Mastodon?

Modern microscopy technologies such as light sheet microscopy allows live sample in toto 3D imaging with high spatial and temporal resolution. Such images will be 3D over time, possibly multi-channels and multi-view. Computational analysis of these images promises new insights in cellular, developmental and stem cells biology. However, a single image can amount to several terabytes, and in turn, the automated or semi-automated analysis of these large images can generate a vast amount of annotations. The challenges of big data are then met twice: first by dealing with a very large image, and second with generating large annotations from this image. They will make interacting and analyzing the data especially difficult.

Mastodon is our effort to provide a tool that can harness these challenges.

You can find its documentation, tutorials and technical informations [here](https://mastodon.readthedocs.io/en/latest/index.html).

{% include gallery content=
"
/media/plugins/mastodon/A_Illustratrion.png | Tracking in _Tribolium castanum_ embryo.
/media/plugins/mastodon/Mastodon_visibilities_01.png | Tracks visibility.
/media/plugins/mastodon/Vlado_01.png | Tracking large movies 1.
/media/plugins/mastodon/Vlado_04.png | Tracking large movies 2.
/media/plugins/mastodon/Screenshot 2022-05-12 at 13.45.49.png | Lineage tracing 1.
/media/plugins/mastodon/Mastodon_TracSchemeColoring_03.png | Lineage tracing 2.
"
%}

{% include video 
src="/media/plugins/mastodon/BDVCapture2-trimmed.mp4" 
name="Exporting tracking data to movie."
align="center" %}

{% include video 
src="/media/plugins/mastodon/BDVCapture3.mp4" 
name="More Tribolium."
align="center" %}

{% include video 
src="/media/plugins/mastodon/Mastodon-Grapher-withContext.mov"
name="Explore numerical results."
align="center" %}

