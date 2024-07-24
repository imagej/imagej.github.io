---
title: TrackMate-Omnipose
categories: [Segmentation,Tracking,Deep Learning]
icon: /media/icons/omniposelogo.png
description: omnipose integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Cellpose
---

{% include img src="/media/plugins/trackmate/trackmate-omnipose-01.png" align='center' width='500' %}

The Omnipose integration in [TrackMate](/plugins/trackmate/index) works roughly as the [Cellpose integration](trackmate-cellpose) one. 
It requires Omnipose to be installed on your system and working independently. This page gives installation details and advices at how to use the omnipose integration in TrackMate.

## Omnipose

[Omnipose](https://github.com/kevinjohncutler/omnipose) is a segmentation algorithm based on Deep Learning techniques, and inspired from the Cellpose architecture. Omnipose is well suited for bacterial cell segmentation, and achieves remarkable performances on mixed bacterial cultures, antibiotic-treated cells and cells of elongated or branched morphology.

If you use the Omnipose TrackMate module for your research, please don't forget to cite the Omnipose paper:

_{% include citation doi='10.1038/s41592-022-01639-4' %}_

## Example

{% include video 
src="https://github.com/marieanselmet/TrackMate-Omnipose/assets/32811540/3c2365c9-8d1b-4057-b4d1-2939e4e2b818" 
width='800' 
align="center" %}

*E. coli, Marie Anselmet and Rodrigo Arias Cartin, [Barras lab](https://research.pasteur.fr/en/team/stress-adaptation-metabolism-enterobacteria/), Institut Pasteur*


## Installation

### TrackMate-Cellpose update site

The TrackMate-Omnipose module is part of the TrackMate-Cellpose Fiji extension.	
Please check the installation instruction on the [TrackMate-Cellpose page](trackmate-cellpose#TrackMate-Cellpose update site).

### Omnipose installation

The integration works with Omnipose version 1.0.6.

Like for the cellpose integration, you need to have a working Python installation of omnipose on the computer you want to use this extension with.
To install Omnipose, you can refer directly to the installation guide provided on the [Omnipose release page on PypI](https://pypi.org/project/omnipose/), but some steps may generate errors.

We give below a tested procude to install omnipose on a Mac Intel, Mac M1 to M3 and Windows with GPU support via mamba. 

An example Windows installation working on GPU (may need to adapt the cuda version to your drivers):
```sh
mamba create -n omnipose-106 'python==3.9.18' pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia -y
mamba activate omnipose-106
pip install natsort
pip install scipy==1.11.4
pip install omnipose==1.0.6
```

An example Mac Intel installation:
```sh
mamba create -n omnipose-106 'python==3.9.18'
mamba activate omnipose-106
mamba install pytorch torchvision -c pytorch
pip install natsort
pip install scipy==1.11.4
pip install fastremap==1.12.2
pip install omnipose==1.0.6
```

An example Mac M1 to M3 installation:
```sh
mamba create -n omnipose-106 'python==3.9.18' 
mamba  activate omnipose-106 
mamba install pytorch torchvision -c pytorch
pip install natsort
pip install scipy==1.11.4
pip install omnipose==1.0.6
```

### Troubleshooting "Found 0 spots" errors with pretrained models

On some systems we have noticed that sometimes TrackMate returns 0 detections for the cellpose and omnipose detectors, even when the installation of these two programs worked correctly.
In most cases, this is due to the fact that the pretrained models have not been downloaded prior to running the TrackMate integration. If the model your trying to call doesn't exist on your computer, a message should appear in the TrackMate logger after the preview step.
To fix this, the easiest way is to launch the omnipose Python GUI, and segment a single small image.
This will trigger the download of the pretrained models.
After this, the TrackMate Omnipose integration should work as expected.

### Custom models

You can use in this TrackMate-Omnipose integration your own custom models that were trained on the same version 1.0.6 of Omnipose. 
In the last versions of Omnipose, some changes were made, in particular in the way to call the models and the default parameters values. We made our code as robust as possible to deal with these changes but we can't ensure this TrackMate integration of Omnipose is compatible with custom models trained on all the previous versions of Omnipose.

### Omnipose advanced detector

There is an [advanced version of this detector](trackmate-omnipose-advanced), that gives the possibility to tune the values of the mask and the flow threshold.
Details about the meaning of the mask and flow thresholds can be found [here](https://omnipose.readthedocs.io/settings.html).


## Usage

The integration is really close to the cellpose integration, with parameters that are almost identical (and a lot of shared code).
The main thing that changed is the list of pretrained models.
We refer to the [TrackMate-Cellpose](trackmate-cellpose) page for details. 

### Tutorial

Here is a brief tutorial where we segment and track individual bacteria in several colonies.
The source video follows  _E. coli_ bacteria imaged in phase contrast. 
We want to segment them, track them, and plot the growth curve for the bacteria imaged. 

The image file can be found on Zenodo:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8182297.svg)](https://doi.org/10.5281/zenodo.8182297)
Download it and save it somewhere convenient.

After executing the installation procedure above, launch Fiji and open the image.
It is a relatively large image with a small pixel size (70 nm). 
Each 2D frame is 1824 x 1896 and a bacteria of length 4 um is imaged over about 50 pixels.
With this image selected, run TrackMate (_Plugins > TrackMate_).

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-01.png" align='center' width='500' %}

In the detector selection panel, pick the **omnipose detector**.

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-02.png" align='center' %}

The configuration panel is quasi identical to that of the cellpose detector.
The list of pretrained models is however specific to omnipose.
Also, since in TrackMate we give the size of objects to detect in microns, we can expect to use a `diameter` value comparatively smaller for bacteria. 
Here, the default values will give us satisfactory results. 
You just need to edit the path to the python executable on your computer. 
For a windows computer where omnipose has been installed following the instructions above, this path is something like `C:\Users\tinevez\anaconda3\envs\omnipose\python.exe`

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-03.png" align='center' %}

Click the `Preview` button to check that the settings give correct results.
Here the quality is equal to the number of pixels inside detected objects.
We see that there are some very small objects with settings we have, but otherwise the results are excellent with the default parameters. 

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-04.png" align='center' width='500' %}

We can now run the detection over the whole movie by clicking the `Next` button.
On my windows machine with a NVIDIA 2080Ti, it takes about 3 to 4 seconds per frame. 

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-05.png" align='center' %}

When done, click `Next` to reach the initial filtering panel.
The quality histogram displays a small peak at low quality, corresponding to small spurious objects.
We can filter them out by setting the threshold in between the two peaks in the histogram.

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-06.png" align='center' %}

We can skip filtering objects.
Click `Next` until you reach the tracker selection panel.
The bacteria do not move much, but divide, pushing each other away.
We found out that for this kind of dynamics the **Overlap tracker** gives good tracking results.

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-07.png" align='center' %}

A few parameter needs to be tuned. 
For the `Min IoU` we use **0.1**.
For the `Scale factor` we use **1.3**.
Click `Next`.

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-08.png" align='center' %}

This yields a good lineage of the bacteria.
We see each "colony" grows, and mix with the close ones. 
With the tracker settings we picked above, the lineage of each mother bacteria is preserved rather well, even when a colony touches its neighbors.

To color each bacteria by its colony, on the **Display options** panel click on the `Edit settings` button.
In the display settings window that appear, make the following changes:
- select `draw spots filled`
- set the `spot alpha transparency` to 0.7
- for `spot color`, select **Track index**
- uncheck `draw tracks`

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-09.png" align='center' %}

The lineages that we see in the [TrackScheme](/plugins/trackmate/views/trackscheme) window show that for some bacteria, there might be some linking errors late in the movie.
But overall we could correctly detect the division events over 5 generations in this movie.

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-10.png" align='center' %}

In the very last panel of TrackMate, an action called **Plot N spots vs time** highlights the exponential growth of the bacteria:

{% include img src="/media/plugins/trackmate/trackmate-omnipose-tutorial-11.png" align='center' %}



