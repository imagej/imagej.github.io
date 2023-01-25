---
title: Live Kymographer
description: An ImageJ plugin to generate kymographs with a live preview
categories: [Kymograph]
source-url: https://github.com/remiberthoz/imagej-live-kymographer
source-label: GitHub
license-url: /licensing/gpl
license-label: GPLv3
release-url: https://github.com/remiberthoz/imagej-live-kymographer/releases/latest
dev-status: Stable
support-status: Active
team-founders: Rémi Berthoz | https://github.com/remiberthoz
team-developers: Rémi Berthoz | https://github.com/remiberthoz
---

An ImageJ plugin to generate kymographs with a live preview
===========================================================

A *kymograph* is an image that represents spatio-temporal data on a single frame
instead of on an animation. You will find information about [Generating and
exploiting kymographs](https://imagej.net/tutorials/generate-and-exploit-kymographs)
on the ImageJ tutorials.

{% include video src="https://user-images.githubusercontent.com/1943662/214679831-c3cac787-b69e-4822-892f-cece7dcc305e.mp4 %}

ImageJ/Fiji has several built-in features to generate kymographs, and many
plugins also exist. I created this one to gather features that I find useful
when analysing data with kymographs:

- A **live preview** of the kymograph about to be generated, also featuring an
  **indication of the on-screen frame** on the temporal axis.
- A **kymograph annotation** tool, to mark interesting time periods in kymographs
  generated from time-lapses featuring many events.
- A direct **annotation of the source image**, marking the spatio-temporal
coordinates of the interesting time periods in kymographs.

The annotation parameters will be saved in a table, such that you
can import the ROI later. In addition, kymographs pixels are calibrated from
your original data. Pixel width will correspond to spatial scale, while pixel
height will correspond to frame interval.

## Missing features:

- [ ] **Removal of ROIs** from the table is not supported yet. A possible way to
  implement this features is described by the author of TrackMate [on the
  image.sc forum](https://forum.image.sc/t/add-listener-to-resultstable/814/2).
- [ ] Wide ROIs extending outside the image will have incorrect pixel values.
- [ ] RGB input time-lapses raise an ImageJ error.

Contributions are welcome!

## How to install

You can add this Plugin to your ImageJ/Fiji installation either by configuring an [Update Site](https://imagej.net/update-sites/) in ImageJ/Fiji, or by installing it manually.

**5 clicks procedure:** the easiest way is to use the Update Site.

- As stated in the [official ImageJ documentation](https://imagej.net/update-sites/following), you can navigate in ImageJ's menu to `Help > Update...`.
- Then click on the `Manage update sites` button.
- In the list that opens, find the entry named *Live-Kymographer* and tick the checkbox.
- Fiji will now display the changes it has to perform to install the plugin. If the list is very long, I would recommend reading [this page](https://imagej.net/update-sites/following#choose-and-download-plugins) on ImageJ's wiki. Otherwise, simply click on `Apply changes`
- Restart ImageJ, and you're done.

**Manual installation**: even-though the procedure is described with fewer steps, it requires more autonomy from your side. With this method, you can install any version of the plugin, but it will not be updated automatically by ImageJ.

- Head on to the [Releases page](https://github.com/remiberthoz/imagej-live-kymographer/releases) here on GitHub.
- Download the `.jar` file for the latest version (or another one).
- Copy this file into your ImageJ/Fiji plugins directory. This directory is located in your ImageJ/Fiji installation, but I cannot tell where that is as it depends on the systems.
- Restart ImageJ, and you're done.
