---
title: Large-scale cell tracking under segmentation uncertainty
dev-status: Beta
support-status: Active
description: Cell tracking and segmentation software
Creator: 
  - Jordão Bragantini
  - Ilan Theodoro
Developer: 
  - "@ilan-theodoro"
  - "@JoOkuma"
doi: 10.48550/arXiv.2308.04526
categories: [Tracking]
---

{% capture source%}
{% include github org='royerlab' repo='ultrack' %}
{% endcapture %}

# Overview

[Ultrack](https://github.com/royerlab/ultrack) is a method for large-scale 3D cell-tracking through a segmentation selection approach.
It is effective at tracking cells across large microscopy datasets on two fronts: (i) It can solve
problems containing millions of segmentation instances in terabyte-scale 3D+t datasets; (ii) It achieves competitive 
results with or without deep learning, which requires 3D annotated data, that is scarce in the fluorescence microscopy 
field. The proposed method computes cell tracks and segments using a hierarchy of segmentation hypotheses and selects 
disjoint segments by maximizing the overlap between adjacent frames. We show that this method achieves state-of-the-art 
results in 3D images from the cell tracking challenge and has a faster integer linear programming formulation. Moreover, 
our framework is flexible and supports segmentations from off-the-shelf cell segmentation models and can combine them 
into an ensemble that improves tracking.

# Description

## Installation 

The Ultrack plugin is a Java client for Python's Ultrack tracking software. The user needs to have
Python installed in the system, preferably managed by [conda](https://conda.io/projects/conda/en/latest/index.html).
The FIJI plugin depends on Ultrack's optional functionalities.
Therefore, installation must include `ultrack[api]`.
For example:
```bash
pip install 'ultrack[api]'
```

For additional installation instructions, please refer to the [Ultrack documentation](https://github.com/royerlab/ultrack).

This plugin will call the Ultrack routines under the hood, enabling cell tracking in 2D+t and 3D+t datasets.

### FIJI integration

The ultrack plugin is available after selecting the update site for ultrack in FIJI by clicking **HELP** → **Update** 
→ **Manage Update Sites** and then searching for **Ultrack**. To activate the update site, click the checkbox in the
**Activate** column, the leftmost one. Right after that, click **Apply and Close** and then **Apply Changes** in the now-enabled
button at the bottom of the previous **ImageJ Update** window. That will trigger the download of the Ultrack
plugin.

After that, FIJI restart is required, and then the Ultrack plugin will be available in the **Plugins**→**Tracking**→
**Ultrack** menu.

## How to Use

The steps below describe how to use the Ultrack plugin:

1. Open the image sequence to be tracked.

2. Click on the **Plugins** → **Tracking** → **Ultrack** menu. The Ultrack GUI will open.

![Ultrack GUI](media/plugins/ultrack/00_init.png)

3. (Optional but required in the first run) If Ultrack is correctly installed and accessible through the system path, 
   the user can proceed to the next step. Otherwise, the user needs to set the path to the Ultrack executable in the 
   **Environment**→**Select Conda Path** menu. It will open a dialog to select the `conda` executable, and 
   then the user needs to select the preferred environment, which should be one indicated with the `[Ultrack found]` flag.

4. Now you should be able to start the connection with the Ultrack software by clicking the **Start Ultrack Server** 
   button. The plugin will update its GUI to show the available tracking options, as shown in the figure below.

![Ultrack GUI with server started](media/plugins/ultrack/01_gui.png)

4. The user should now select the desired tracking workflow in this section:
    
![Ultrack GUI with tracking workflows](media/plugins/ultrack/03_workflows.png)
    
in which the user can select the desired tracking workflow. The options are:
 - **Auto Detection From Image**: which provides a way to track cells using solely the image as input;
 - **Foreground & edges from user**: which is suitable for tracking cells using **edge** detection and **foreground** 
   segmentation provided by the user;
 - and **Segmentation from user**: which is suitable for tracking cells using segmentation labels from your favorite 
   segmentation software, such as [Stardist](https://github.com/stardist/stardist), 
   [Cellpose](https://github.com/MouseLand/cellpose), 
   [MicroSAM](https://github.com/computational-cell-analytics/micro-sam) or any other.

5. (Optional) After selecting your desired workflow, you can tune the tracking parameters in the **Settings** section. 
   The parameters are workflow-dependent, and the user can 
   [check here](https://github.com/royerlab/ultrack-dev/blob/main/ultrack/config/README.md) for more information about
   the parameters. Not all of them are available in the FIJI interface, Python is required for full customization.

![Ultrack GUI with tracking options](media/plugins/ultrack/02_options.png)

6. After setting the parameters, the user can click the **Select Images** button to select the image to be tracked. 
   It is worth mentioning that some workflows, such as **Manual Detection**, require more than one image to be selected.

![Ultrack GUI with image opening](media/plugins/ultrack/04_image_opening.png)
![Ultrack GUI with image selector](media/plugins/ultrack/05_image_selection.png)

7. Finally, the user can click the **Run** button to start the tracking process. The user can follow the tracking 
   process in the **Ultrack Log** section. 

![Ultrack GUI with tracking progress](media/plugins/ultrack/06_run.png)

8. To visualize the tracking results, the user can click the **View Tracks** button. Then, it will request a 
   particular image to bind the tracks. In the end, The tracking results will be shown using the 
   [TrackMate](https://imagej.net/plugins/trackmate/) plugin. 

![Ultrack GUI with track image selection](media/plugins/ultrack/07_open_tracks.png)
![Tracks Viewer it Trackmate](media/plugins/ultrack/08_trackmate.png)

# Acknowledgments

We thank the ImageJ community for providing the necessary tools to develop this plugin, such as 
the FIJI platform and integrations. We also acknowledge the developers from [Trackmate](https://imagej.net/plugins/trackmate/) plugin for their work 
in the tool, which we rely on to visualize the tracking results.

# Citation
If you find ultrack useful, please cite Ultrack as follows:

{% include citation %}
