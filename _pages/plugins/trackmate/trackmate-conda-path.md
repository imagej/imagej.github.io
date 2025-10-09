---
title: Configuring TrackMate conda path
description: How to configure conda path to use Python tools in TrackMate.
categories: [Tracking, Segmentation]
artifact: sc.fiji:TrackMate
project: /software/fiji
---

{% include notice icon="warning"
  content="This feature is not released yet! 
  It depends on the future version of TrackMate (the forthcoming v8), to be released Autumn 2025 (if everything goes well)." %}
  
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

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-01.png"  %}

In the first text box, simply enter the path to the conda (or mamba of any flavor) executable that you have installed and use on your system. 

In the second box, enter the path where the base conda installation is located.
Classically, this will be the home directory of the executable. 

Once you click OK, and if the parameters are correct, the log should output the list of conda environments found on your computer. 

{% include img src="/media/plugins/trackmate/trackmate-configure-conda-02.png"  %}

If this is correct, you can **relaunch Fiji for the new settings to be used**.



