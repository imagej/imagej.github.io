---
title: TrackMate-Lacss
categories: [Segmentation,Tracking,Deep Learning]
icon:
description: Lacss integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Lacss
section: TrackMate-Lacss.:Usage:Lacss parameters in the TrackMate UI.
---

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [lacss](https://github.com/jiyuuchc/lacss) to segment cells in 2D. It is not included in the core of TrackMate and must be installed via its own [update site](https://sites.imagej.net/TrackMate-Lacss/). This plugin also requires a python environment with the lacss library installed. This wiki-page offers insights for installation and how to optimize lacss integration. 

Lacss is a deep-learning model for single-cell segmentation from microscopy images. On GPU, the model is quite fast and ueful for processing large time-laspe dataset. In additon, Lacss is designed to utilize point labels for model training. Therefore experimental data such as DAPI counter stain can be used to easily train a custom model. See [lacss](https://github.com/jiyuuchc/lacss) website for more details. 

The TrackMate-Lacss module, is a thin Java wrapper around the Lacss python module which runs as a seperate process. The Java code communicates with the Python process via [anonymous pipe](https://en.wikipedia.org/wiki/Anonymous_pipe) - sending and receiving messages encoded in Google's [Protobuf](https://protobuf.dev/).

## Installation

Installation requires you to subscribe to an  update site in Fiji's plugin updater. It also requires a working python environment with the Lacss library.

### TrackMate-Lacss update site

In Fiji, go to {% include bc path='Help|Update...' %}. Update and restart Fiji until it is up-to-date. Then go to the update menu once more, and click on the `Manage update sites` button, at the bottom-left of the updater window. A new window containing all the known update sites will appear. Click on the  **TrackMate-Lacss** check box and restart Fiji one more time. 


### Lacss

This step is independent of Fiji. See the updated Lacss API for most up-to-date method [here](https://jiyuuchc.github.io/lacss/install/)

We recommend installation of GPU Version if possible. CPU, while useable, loses that advantage of processing speed and may increase segmentation time dramaticly. 

*Important* Make sure you launch FIJI within the activted virtual environemnt you use for the Lacss installation. Otherwise FIJI will not be able to find and start the python module.

## Limitations

- The plugin only offer a few pre-trained models. For best results requires own seperate model training.

## Usage

#### Lacss Parameters in the TrackMate UI

{% include img src="/media/plugins/trackmate/trackmate-lacss-ui.png" align='center' width='300' %}

As shown, these are the changeable parameters in the GUI.

##### `Path to Model Parameter`

The Path to Model Parameter can be 1 of 2 options:

- Default; Which pulls in a pre-trained model contained within the .jar file
- Custom ; Which prompts you to select the _path to a lacss model file_. For example: `C:\Users\Nick\Downloads\livecell_a431.pkl`

##### `Pre-Trained Models:`
Currently:
- the `default` model - a model trained with a combination of beight-field and fluorescence images.  Should work on most microscopy images.
- the `custom` model - several additional pretrained models can be downloaded from [hugging face](https://huggingface.co/jiyuuchc), or you can train one yourself.

##### `Minimum Cell Area`

A float type that defines the minimum area of a valid prediction. 

##### `Scaling Factor`

A Float type with default = 1. Contols a 	image scaling factor. If not 1, the input image will be resized internally before fed to the model. The results will be resized back to the scale of the orginal input image. 

##### `IOU Threshold`

A float type with default = 0. 

##### `Segmentation Treshold`

A float type with default = 0.5. Controls the minimum score value to be considered a valid prediction. 

##### `Remove Out of Bounds`

Whether to remove out-of-bound predictions. Default is False or unchecked.

##### `Multi Channel`

Whether to consider multichannel. Default is True or checked. 

_____

* This plugin and page was adopted from Jean-Yves Tinevez's Trackmate-Cellpose plugin and wiki-page* 
* Last updated - Dec 2023*
