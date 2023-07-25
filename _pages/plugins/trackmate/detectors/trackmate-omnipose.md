---
title: TrackMate-Omnipose
categories: [Segmentation,Tracking,Deep Learning]
icon: /media/icons/omnipose.png
description: omnipose integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Cellpose
---

{% include img src="/media/plugins/trackmate/trackmate-omnipose-01.png" align='center' width='500' %}

# Omnipose integration in TrackMate.

The Omnipose integration in TrackMate works roughly as the [Cellpose integration](trackmate-cellpose) one. 
It requires Omnipose to be installed on your system and working independently. This page gives installation details and advices at how to use the omnipose integration in TrackMate.

## Omnipose

[Omnipose](https://github.com/kevinjohncutler/omnipose) is a segmentation algorithm based on Deep-Learning techniques, and inspired from the Cellpose architecture. Omnipose is well suited for bacterial cell segmentation, and achieves remarkable performances on mixed bacterial cultures, antibiotic-treated cells and cells of elongated or branched morphology.

If you use the Omnipose TrackMate module for your research, please also cite the Omnipose paper:

_{% include citation doi='10.1038/s41592-022-01639-4' %}_

## Example

{% include video 
src="https://github.com/marieanselmet/TrackMate-Omnipose/assets/32811540/3c2365c9-8d1b-4057-b4d1-2939e4e2b818" 
width='800' 
align="center" %}

*E. Coli, Marie Anselmet and Rodrigo Arias Cartin, [Barras lab](https://research.pasteur.fr/en/team/stress-adaptation-metabolism-enterobacteria/), Institut Pasteur*


## Installation

### TrackMate-Cellpose update site

The TrackMate-Omnipose module is part of the TrackMate-Cellpose Fiji extension.	
Please check the installation instruction on the [TrackMate-Cellpose page](trackmate-cellpose#TrackMate-Cellpose update site).

### omnipose

The integration  works with the Omnipose version 0.3.6. It doesn't work with the last version of Omnipose.

Like for the cellpose integration, you need to have a working python installation of omnipose on the computer you want to use this extension with.
To install Omnipose, you can refer directly to the installation guide provided on the [Omnipose repository](https://github.com/kevinjohncutler/omnipose#how-to-install-omnipose).
We also give below a tested procude to install omnipose on a Windows machine via conda. 

An example Windows installation working on GPU:
```
conda create -n omnipose
conda activate omnipose
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install omnipose==0.3.6
pip install cellpose-omni==0.7.3
```

The default models *bact_phase_omni* and *bact_fluor_omni* are stored in the cellpose pretrained models folder.

### Troubleshooting "Found 0 spots" errors

On some systems we have noticed that sometimes TrackMate returns 0 detections for the cellpose and omnipose detectors, even when the installation of these two programs worked correctly.
In most cases, this is due to the fact that the pretrained models have not been downloaded prior to running the TrackMate integration.
To fix this, the easiest way is to launch the cellpose or omnipose Python GUI, and segment a single small image.
This will trigger the download of the pretrained models.
After this, the TrackMate integration should work as expected.


