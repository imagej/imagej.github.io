---
title: TrackMate-Ilastik
categories: [Segmentation,Tracking,Machine Learning]
logo: /media/icons/trackmate-ilastik.png
---

# TrackMate-Ilastik.

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [Ilastik](https://www.ilastik.org/) to segment objects in 2D or 3D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following).

## Installation.

For this module to work, you need three things:

1. Download and Install Ilastik on your machine. Follow the instructions on [this page](https://www.ilastik.org/download.html).

2. Subscribe to the **ilastik** [update site](/update-sites/following). 

Run _Fiji > Help > Update_.
From the ImageJ Updater window, Open the ```Manage update sites``` window.

![](/media/plugins/trackmate/trackmate-ilastik-install-ilastik.png)

3. And finally, subscribe to the **TrackMate-Ilastik** update site.

![](/media/plugins/trackmate/trackmate-ilastik-install.png)

We rely on the capabilities of the **ilastik Fiji import/export plugin**, built by the ilastik team. It is documented in detail [in the ilastik website](https://www.ilastik.org/documentation/fiji_export/plugin).

**Issue**:

- If ilastik not installed in the default location, the path to executable must be specified in Fiji in _Fiji > Plugins > ilastik > Configure ilastik executable location_.

## Preferences

ilastik allowed ressources on the system can be tuned in _Fiji > Plugins > ilastik > Configure ilastik executable location_. By default, it uses all ressources available. This can be heavy for some computer and can be tuned down, at the cost of the processing speed.

- number of threads ilastik can use
- maximum RAM ilastik can use

## Tutorial.

For this tutorial we will work with the Neisseria meningitidis bacterial growth dataset, that you can download on Zenodo.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5419619.svg)](https://doi.org/10.5281/zenodo.5419619)

The dataset contains the ILP file, which is the ilastik project file. We trained a pixel classifier on several images that Laure acquired previously, and that are distinct from the movie we will track. We will use the same ILP file in TrackMate so that it can run ilastik to yield objects.

### Start trackmate.

1. Load the `NeisseriaMeningitidisGrowth.tif` movie into Fiji, and start TrackMate _Plugins > Tracking > TrackMate_.
   - (**optional**) specify a ROI with the selection tool of your choice.
2. After verifying the movie calibration settings are correct, go to the next step.

{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_0.png' width='400px'  %}
{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_1.png' width='400px'  %}


### Select the detector.

3. In the **Detector** menu, choose the ilastik detector and go next.
4. Browse to the location to the NeisseriaMeningitidisGrowth pre-trained ilastik project file (e.g. `NeisseriaMeningitidisGrowth.ilp` file). Number of classes to detect and probability threshold can be defined. In this case, use the default values.
   - (**optional**) It is possible to test the detector and chosen parameters on the current timepoint using the preview button.
   - If you want to use your ilastik model, please follow the ilastik [pixel classifier tutorial](https://www.ilastik.org/documentation/pixelclassification/pixelclassification).

{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_2.png' width='400px'  %}
{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_3.png' width='400px'  %}

5. The ilastik classifier will be applied to the data. Wait for the process to be done and go to the next step.
   - **Issues**: a few WARNING and ERRORS in the consol windows, in addition to DEBUG messages. No direct impact on the processing.
6. You have the option to apply various filtering on computed features to remove some spots of the detection. This step has a direct impact on the quality of the tracking, it is worth to spend time on it to provide a clean spot detection before going to the next step. 


{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_4.png' width='400px'  %}
{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_5.png' width='400px'  %}



### Select the tracker.

7. Now that objects are detected in each timepoint, we can select a **tracker**. Multiple choices are available and is dependent of the data to process. Please see the [Tracker tutorial](/plugins/trackmate/getting-started#configuring-the-simple-lap-tracker) for more information on each tracker and help you decide which to choose. For this example, we will choose **LAP Tracker** as it allows split and merge behaviour.

{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_6.png' width='400px'  align='center' %}

1. Define tracker options. Those options depends on the chosen tracker and your data. In this example, as the LAP Tracker is use, we set Frame to frame linking to `1.0μm` and gap closing at `2.0μm`. We will also enable segment spliting with a max distance to `2.0μm`.
2. Run the tracker. It is possible to return at the previous step to improve tracker parameters if needed. Continue to the next step. 
3. Similarly as in the detection part, it is possible to filter the tracks based on various features. Here we can filter the Track start feature to only keep track which start at the first frame.

{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_7.png' width='400px'  %}
{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_8.png' width='400px'  %}

### Explore results.

10. The last steps allows you to explore the tracking and computed features for the spots and tracks. It is also possible to export various results (e.g. tracks, lineage, segmentation, etc.) for further analysis.

{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_9.png' width='400px'  %}
{% include img src='/media/plugins/trackmate/trackmate-ilastik-tutorial_10.png' width='400px'  %}


________
Stéphane Rigaud - September 2021
