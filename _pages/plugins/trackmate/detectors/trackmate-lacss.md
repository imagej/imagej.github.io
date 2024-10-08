---
title: TrackMate-Lacss
description: Lacss integration in TrackMate.
categories: [Segmentation,Tracking,Deep Learning,Machine Learning]
pom-url: https://github.com/jiyuuchc/TrackMate-Lacss/blob/main/pom.xml
website: https://github.com/jiyuuchc/TrackMate-Lacss
---

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [lacss](https://github.com/jiyuuchc/lacss) to segment cells in 2D or 3D. It is not included in the base installation of TrackMate and must be installed via its own [update site](https://sites.imagej.net/TrackMate-Lacss/).

Lacss itself is a deep-learning model for single-cell segmentation from microscopy images. On GPU, the model is very fast for processing large time-lapse datasets. In addition, Lacss is designed to utilize point labels for model training, and offers several efficient paths for adapting an existing model to new data characeristics. See the [lacss website](https://github.com/jiyuuchc/lacss) for more details. 

The design of TrackMate-Lacss follows a server/client model, using the [GRPC](https://grpc.io/) communication protocol. In such case, the Lacss program runs as a GRPC server, listening on a TCP port, which the thin client TrackMate-Lacss uses to communicates with the server, sending the image data and receiving the segmentation results.

From the users' perspective, the most important advantage of such design is so that they can run the server on a different computer than the one they run Fiji on. Modern deep learning algorithms heavily rely on sophisticated GPU hardware for speed. Our design allows the user to utilize a dedicated server for faster computation and for multiple users to share computational resources. 

On the other hand, there is also nothing wrong with running the server locally on the same machine running Fiji. It is entirely the users' choice in how to set it up.

## Limitations

3D segmentation results will not be rendered in full. Instead, only a single point per cell will be displayed. This is a limitation of TrackMate itself and will be resolved in the next major release of TrackMate.

## Installation

You need to install both the *Lacss*, which is a Python package, and *TrackMate-Lacss*, which is a Fiji/ImageJ plugin.

### Install Lacss

The short version:

```shell
pip install lacss
```

Slightly longer version: See the [Lacss Documentation](https://jiyuuchc.github.io/lacss/install/) for more details. We recommend installation on a Linux computer with a dedicated GPU.

_Lacss installation is independent of Fiji._

### Install TrackMate-Lacss

In Fiji, go to {% include bc path='Help|Update...' %}, update, and click on {% include button label="Manage update sites" %} (bottom-left). A new window containing all the known update sites will appear. Check the  **TrackMate-Lacss** box and restart Fiji. 

## Usage

#### Starting the Lacss server

To start Lacss on a remote server:
```
python -m lacss.deploy.remote_server --modelpath=<path_to_model_file>
```
The server should print out a randomized token string, which serves as the key for access. You should copy and save it somewhere. 
```
> COPY THE TOKEN BELOW FOR ACCESS.
> =======================================================================
> adK11qJ7-LcnIsFRbcPKy8x46Pz6bxJpsXodOhd4P_k
> =======================================================================
```
The `<path_to_model_file>` is the local path to the file that contains the model parameters. You can get the download links of model files by calling the above command without arguments:
```
python -m lacss.deploy.remote_server
```

To start Lacss locally:
```
python -m lacss.deploy.remote_server --modelpath=<path_to_model_file> --local
```

#### Lacss Parameters in the TrackMate UI

##### `Server`

The address to the GRPC server in the format of `hostname:port`. The default is for a local server.

##### `Access token`

The token printed out by the server. Leave it empty for a local server.

##### `Minimum Cell Area`

The minimum cell area/volume in units of pixels.

##### `Scaling Factor`

If not 1, the input image will be resized internally before sent to the model. This is useful if your cell sizes (in pixels) differ significantly from those of the training data.

##### `Score Treshold`

Minimum score needed to be considered a valid prediction. 

##### `NMS IOU`

Lacss is an object detection model, and can detect cells that are right on top of each other. If you want to disable this behavior, set a non-zero IOU threshold to remove overlapping cells.

##### `Multi-Channel`

By default the segmentation is performed by considering all color channels. Uncheck this to use only a single channel. 

-----

* This plugin and page was adapted from Jean-Yves Tinevez's Trackmate-Cellpose plugin and wiki page.
* Last updated: July 2024*
