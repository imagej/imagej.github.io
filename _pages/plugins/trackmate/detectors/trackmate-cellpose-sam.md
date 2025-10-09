---
title: TrackMate-Cellpose-SAM
categories: [Segmentation,Tracking,Deep Learning]
icon: /media/icons/cellpose.png
description: cellpose-SAM integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Cellpose
---

{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-R2_multiC.gif" width='400'  %} {% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-01.png"  width='200' %}

{% include notice icon="warning"
  content="The Cellpose-SAM integration is not deleased yet! 
  It depends on the future version of TrackMate (the forthcoming v8), to be released Autumn 2025 (if everything goes well)." %}

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on the latest version of [cellpose](https://cellpose.readthedocs.io/en/latest/) to segment cells in 2D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following). It also requires cellpose to be installed on your system and working independently. This tutorial page gives installation details and advices at how to use the cellpose integration in TrackMate.

Cellpose-SAM is the latest version of cellpose (at least in August 2025) that leverages a new encoder based on SAM foundational model to achieve better generalizations performance.
Compared to the version 3 of cellpose, which integration in TrackMate is documented [here](/plugins/trackmate/detectors/trackmate-cellpose) and [here](/plugins/trackmate/detectors/trackmate-cellpose-advanced), Cellpose-SAM has fewer parameters, is more demanding computationally, and generalizes better. 

If you use this detector for your research, please also cite the cellpose paper:

_{% include citation doi='10.1101/2025.04.28.651001' %}_


## Installation

We need to subscribe to an extra update site in Fiji, and have a working installation of cellpose on your system.

### TrackMate-Cellpose update site

In Fiji, go to {% include bc path='Help|Update...' %}. Update and restart Fiji until it is up-to-date. Then go to the update menu once more, and click on the `Manage update sites` button, at the bottom-left of the updater window. A new window containing all the known update sites will appear. Click on the  **TrackMate-Cellpose** check box and restart Fiji one more time. 

### Cellpose-SAM

This step requires you to have a working conda installation, like for any of the Python tools integrated in TrackMate. 
We recommend [miniforge](https://github.com/conda-forge/miniforge).

For Cellpose specifically, we copy below the installation instruction from the [cellpose repository](https://github.com/MouseLand/cellpose?tab=readme-ov-file#option-1-installation-instructions-with-conda)

```zsh
conda create --name cellpose-sam python=3.10
conda activate cellpose-sam
python -m pip install 'cellpose[gui]'
```

On **Windows**, we noticed that it is not enough to get GPU acceleration even if you have a NVIDIA card.
You need to reinstall torch with GPU CUDA support, as follow:
- Remove the current version of torch
```zsh
pip uninstall torch
```
- Reinstall torch with GPU support. Follows the instructions [here](https://pytorch.org/get-started/locally/).
In August 2025, this amounts to:
```zsh
 pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```

Then:
```zsh
cellpose --version
```

```
Welcome to CellposeSAM, cellpose v
cellpose version:       4.0.6
platform:               win32
python version:         3.12.11
torch version:          2.8.0+cu126
```
You can ignore the warning if any.

_____


If you have not done it yet, you need to [configure the TrackMate conda path in Fiji](/plugins/trackmate/trackmate-conda-path). 


## Usage

### Cellpose parameters in the TrackMate UI

{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-01.png" align='center' width='400' %}
We document these parameters from top to bottom in the GUI.

##### `Conda environment`

Specify in what conda environment you installed Cellpose-SAM. 
If you get an error at this stage, it is likely because the conda path for TrackMate was not configured properly. Check [this page]((/plugins/trackmate/trackmate-conda-path).

##### `Pretrained model`

Cellpose-SAM has only one pretrained model now: `cpsam`, which is denoted _cellpose-SAM_ in the UI.


##### `Path to a custom model`

You can use a custom cellpose model saved on disk. 
First click on the radio button next to the `Path to a custom model` label, and enter below the path to the model. 
It will be used for detection.
Note that the path must be the an _absolute path_ to the file.

##### `Use channels`

Cellpose-SAM normally disregard the channels parameters that were used up to the version 3. 
Here however we have added the option to pass to cellpose either the full image with all channels, or just one channel. Depending on the image content, this changes the results quite a lot. 
This exemplified in the next section.

##### `Use GPU`

If this box is checked, the GPU will be used.
With modern version of cellpose, even on MacOS, there is not reason not to check this box. 
Unchecking the box will force cellpose to use the CPU even if GPU support is available, and will process the image with multithreading. 

##### `Simplify contours`

If this box is checked, the contour outlines generated by the masks returned by cellpose will be smoothed and simplified. This is the same treatment that is used by other TrackMate detectors and documented [here](/plugins/trackmate/detectors/trackmate-v7-detectors#simplifying-contours).


## Using different channels 

As stated above, we have added the possibility to pass to cellpose all channels or just one. 
We exemplified below the impact of this setting.
This image comes from the lab of Guillaume Jacquemet and was used in {% include citation doi='10.1038/s41592-022-01507-1' %}


With all channels:
{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-allchannels.png" align='center' %}

Channel 1 only, in which nuclei are painted in red:
{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-channel-1.png" align='center' %}

Channel 2 only, in which the cell cytoplasm appears in green:
{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-channel-2.png" align='center'  %}

Channel 3 only, which is empty:
{% include img src="/media/plugins/trackmate/detectors/trackmate-cellpose-sam-channel-3.png" align='center' %}

