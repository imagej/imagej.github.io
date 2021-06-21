---
title: TrackMate-StarDist
categories: [Segmentation,Tracking,Deep-Learning]
logo: /media/logos/TrackMateStarDist-logo-300p.png
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

TrackMate-StarDist ships two detectors that will appear in TrackMate.
After installing TrackMate-StarDist and restarting Fiji, the two detectors will be integrated in TrackMate in a transparent manner.
We will describe them via a simple tutorial based on the following image:

TODO

### StarDist detector with builtin versatile nuclei model.

The StarDist plugin comes with a very efficient model that can segment nuclei imaged in fluorescence in 2D, generated from the dataset in the Kaggle challenge of 2018:

{% include citation doi='10.1038/s41592-019-0612-7'%}

We use this model in the first StarDist detector. 

First open the tutorial image in Fiji, and launch TrackMate. 
In the second panel titled **Select a detector**, you should see two new choices in the list, and on of them is **StarDist detector**. 
{% include img name="TrackMate-StarDist builtin detector choice" src="/media/plugins/trackmate/trackmate-stardist-select-builtin-detector.png" %}

Select it and click ** Next**.

This simple panel appears. 
{% include img name="TrackMate-StarDist builtin detector config" src="/media/plugins/trackmate/trackmate-stardist-builtin-detector-config-panel.png" %}

You will notice that there is no configuration for this detector. 
We use the default values of this model for the score threshold and overlap threshold.
We observed that when this model with the default values do not work well with a dataset, changing the score and overlap threshold have little to no positive impact on the results.
We reasoned therefore  that if model and default values do not work well for your data, it is best then to train a specific StarDist model for your problem.

Check the results of segmentation by click on the **Preview** button.
Here is what I get on the first time-point of the tutorial image:
{% include img name="TrackMate-StarDist results" src="/media/plugins/trackmate/trackmate-stardist-preview-results.png" %}

The StarDist model works really well with this kind of data.
After that you follow through the next steps in TrackMate to segment all cells in all time-points then track them. 
Using the default tracker and default parameters each time we get this result:

{% include video src="/media/plugins/trackmate/trackmate-stardist-results.mp4" width=800 %}

### StarDist detector with a custom model.

A second detector allows for using a custom model, that you would have trained yourself and package as a zip file. 
We recommend using the dedicated notebooks on the _ZeroCostDL4Mic_ platform to do so. Check the [ZCDL4M wiki page dedicated to training StarDist](https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki/Stardist) to generate such a model.

In TrackMate, this model can be used with a second StarDist detector:
{% include img name="TrackMate-StarDist custom detector choice" src="/media/plugins/trackmate/trackmate-stardist-select-custom-detector.png" %}

Its configuration panel requires several parameters.
{% include img name="TrackMate-StarDist custom detector config" src="/media/plugins/trackmate/trackmate-stardist-custom-detector-config-panel.png" %}

- In the **Custom model file** text field, you need to enter the path to a StarDist model packaged as a zip file. 
- **Score threshold** correspond to the threshold on the probability map to identify object. It accepts values from 0 to 1.
- **Overlap threshold** correspond to the threshold used in non-maxima suppression step used to separate touching objects. object. It also accepts values from 0 to 1.

Otherwise this detector proceeds as the previous one.

## Citations.

If you use this detector for you reserach, please be so kind as to cite the StarDist and the TrackMate papers:

{% include citation doi='10.1007/978-3-030-00934-2_30'%}


