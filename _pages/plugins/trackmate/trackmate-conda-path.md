---
title: Configuring TrackMate conda path
description: How to configure conda path to use Python tools in TrackMate.
categories: [Tracking, Segmentation]
artifact: sc.fiji:TrackMate
project: /software/fiji
---

The new v8 version of TrackMate ships many new detectors, trackers and actions that are based on existing Python tools. 
We introduced in TrackMate v8 a framework to facilitate the integration of Python tools that are deployed within a conda (or mamba, of any flavor) environment. 
Using these tools in TrackMate requires you to

- install a conda distribution on your computer.
- install the individual TrackMate modules that are you interested in.
- configure the path to your conda environment.

To install conda, we recommend using [miniforge](https://github.com/conda-forge/miniforge).
You can use the recommended settings for your platform.

The TrackMate modules that depend on Python and external tools are all optional and documented on this wiki.
[This path](/plugins/trackmate/index#trackmate-components) is a good starting point to find them.
If you try to use one of the Python TrackMate module without configuring conda (next step), an error will be shown in the TrackMate wizard.

To configure conda in TrackMate, launch Fiji.
In Fiji, click on the {% include bc path="Edit|Options|Configure TrackMate Conda path..."%} menu item.
This window should appear:

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-01.png" width='600' %}

The configuration panel has an `Auto-detect` button, that so far worked on all configurations we tested. 
Just press it and check the log. You should see something like this:

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-02.png" width='600' %}

If this is correct, you are all set, and there is no need to restart Fiji.

If not, let's discuss the issue on forum. 
You can use the `Test` and `Diagnosis` buttons to collect more debug information.

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-03.png" width='600' %}
