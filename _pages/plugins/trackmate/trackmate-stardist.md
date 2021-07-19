---
title: TrackMate-StarDist
categories: [Segmentation,Tracking,Deep-Learning]
logo: /media/icons/trackmate-stardist.png
---

# TrackMate-StarDist

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [StarDist](/plugins/stardist) to segment objects in 2D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following).

## Installation.

You need to subscribe to the **CSBDeep** update site and to the **StarDist** update site first, then to the **TrackMate-StarDist** update site:

The CSBDeep update site:
![Subscribe to the CSBDeep update site](/media/plugins/trackmate/trackmate-stardist-install-csbdeep.png)

The StarDist update site:
![Subscribe to the StarDist update site](/media/plugins/trackmate/trackmate-stardist-install-stardist.png)

And finally the TrackMate-StarDist update site.
![Subscribe to the TrackMate-StarDist update site](/media/plugins/trackmate/trackmate-stardist-install.png)

Once you have them all, please restart Fiji.
We suggest that you test StarDist by itself just to make sure it runs after installation. This way we can better find what is wrong in case it does not work. Follow for instance the instructions on the [StarDist](/plugins/stardist) page.

## Usage and tutorial.

TrackMate-StarDist ships two detectors that will appear in TrackMate. After installing TrackMate-StarDist and restarting Fiji, these two detectors will be integrated in TrackMate in a transparent manner. We describe how to use them in the  tutorial below.

### StarDist detector with builtin versatile nuclei model on a single channel image.

The StarDist plugin comes with a very efficient model that can segment nuclei imaged in fluorescence in 2D, generated from the dataset in the Kaggle challenge of 2018:

{% include citation doi='10.1038/s41592-019-0612-7'%}

We use this model in the first StarDist detector. 

First laucn Fiji and open the tutorial image in Fiji.
We use here the "stardist-tutorial/data/builtin model/cells.tif", provided in the tutorial data.

{% include img name="Cell images" src="/media/plugins/trackmate/trackmate-stardist-builtin-detector-image.png" align="center" %}

Then launch TrackMate (_Plugins > Tracking > TrackMate_).
In the second panel titled **Select a detector**, you should see two new choices in the list, and on of them is **StarDist detector**. 
{% include img name="TrackMate-StarDist builtin detector choice" src="/media/plugins/trackmate/trackmate-stardist-select-builtin-detector.png" align="center" %}

Select it and click ** Next**.



This simple panel appears. 
{% include img name="TrackMate-StarDist builtin detector config" src="/media/plugins/trackmate/trackmate-stardist-builtin-detector-config-panel.png" %}

*Note that in this panel there is no configuration for Stardist detector: we use the default values of this model for the score threshold and overlap threshold. We observed, that in cases when this model with the default values does not work well with some dataset, changing the score and overlap threshold have little to no positive impact on the results. We reasoned therefore that if the model and the default values do not work well for your data, it is best then to train a specific StarDist model for your problem.*

Check the results of segmentation by click on the **Preview** button.
Here is what I get on the first time-point of the tutorial image:
{% include img name="TrackMate-StarDist results" src="/media/plugins/trackmate/trackmate-stardist-preview-results.png" align="center" %}

The StarDist model works really well with this kind of data.
After that you follow through the next steps in TrackMate to segment all cells in all time-points then track them. 
Using the default tracker and default parameters each time we get this result:

{% include video src="/media/plugins/trackmate/trackmate-stardist-results.mp4" width=800 align="center" %}

### ERK signalling and motility assay with a multi-channel image.

In this part of the tutorial we will correlate the translocation of an ERK reported in the nuclei with cell motility. We will use images from a cell migration assay, where cells are expressing an ERK reported in the second channel, and are stained for their nuclei in the first channel. The analysis will consist in segmenting and tracking the cells in the nuclei channel and analyzing intensities in the ERK channel.

Open the ERK cells image you want to track. We use here the "stardist-tutorial/data/builtin model/cells.tif", provided in the tutorial data.

{% include img name="ERK Cell images" src="/media/plugins/trackmate/trackmate-stardist-builtin-detector-2-image.png" width="600" align="center" %}

Launch TrackMate. In the second panel titled **Select a detector**, you should have two Stardist-related entries; again choose **StarDist detector** and click **Next**. 

This time, the configuration panel lets you choose the channel to perform the segmentation on. Pick the first one, which is the nuclei channel. Check that the segmentation is working by clicking the **Preview** button.

{% include img name="Configuring the StarDist detector for the ERK cells movie" src="/media/plugins/trackmate/trackmate-stardist-select-builtin-detector2.png" width="800" align="center" %}

Here is an example of what we get on the first frame of the tutorial image: 

{% include img name="Preview result" src="/media/plugins/trackmate/trackmate-stardist-builtin-detection-2-preview.png" width="800" align="center" %}

In case the results are satisfying, click **Next** to perform detection in the full time-series. After the detection is finished, continue with the following steps same as in standard TrackMate [workflow](https://imagej.net/plugins/trackmate/getting-started#the-detection-process). Using the default tracker (Simple LAP tracker) with the default parameters we get this result without any filtering:

{% include img name="Tracking result" src="/media/plugins/trackmate/trackmate-stardist-builtin-tracking-result.gif" width="800" align="center" %}




### Tracking T-cells imaged in bright-field with a custom model in the StarDist detector.

You can also use a custom model, that you have trained yourself and packaged as a zip file.
We recommend using the dedicated notebooks on the _ZeroCostDL4Mic_ platform to do so. Check the [ZCDL4M wiki page dedicated to training StarDist](https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist) to generate such a model.

In this tutorial we will track T cells imaged in bright-field with a model we trained ourselves. 

First open the tutorial image called "stardist-tutorial/data/custom model/T cells/T_cells.tif" in Fiji.  provided in the tutorial data.

{% include img name="T cells" src="/media/plugins/trackmate/trackmate-stardist-custom-detector-2-image.png" width="800" align="center" %}

Launch TrackMate. In the second panel titled **Select a detector**, choose **StarDist detector custom model** and click **Next**. Its configuration panel requires several parameters:

{% include img name="Custom detector" src="/media/plugins/trackmate/trackmate-stardist-select-custom-detector2.png" width="800" align="center" %}

- In the **Custom model file** text field, you need to enter the path to a StarDist model packaged as a zip file (or use the **Browse** button to navigate to the folder).
- **Score threshold** correspond to the threshold on the probability map to identify object. It accepts values from 0 to 1.
- **Overlap threshold** correspond to the threshold used in non-maxima suppression step used to separate touching/overlapping objects; it accepts values from 0 to 1.

- Set these parameters and click **Preview** button to test the detector on the current frame. Here is an example of what we get on the first time-point of the tutorial image (using default parameters): 

  {% include img name="Preview result" src="/media/plugins/trackmate/trackmate-stardist-custom-detector-2-preview.png" width="800" align="center" %}

- In case the results are satisfying, click **Next** to perform detection in the full time-series. After the detection is finished, continue with the following steps same as in standard TrackMate [workflow](https://imagej.net/plugins/trackmate/getting-started#the-detection-process). Using the default tracker (Simple LAP tracker) with the default parameters we get this result:
  
  {% include img name="Tracking result" src="/media/plugins/trackmate/trackmate-stardist-custom-tracking-result.gif" width="800" align="center" %}

## Citations.

If you use this detector for you research, please be so kind as to cite the StarDist and the TrackMate papers:

{% include citation doi='10.1007/978-3-030-00934-2_30'%}

