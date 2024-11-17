---
title: TrackMate-Lacss
description: Lacss integration in TrackMate.
categories: [Segmentation,Tracking,Deep Learning,Machine Learning]
pom-url: https://github.com/jiyuuchc/TrackMate-Lacss/blob/main/pom.xml
website: https://github.com/jiyuuchc/TrackMate-Lacss
---

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [LACSS](https://github.com/jiyuuchc/lacss) to segment cells in 2D or 3D. It is not included in the base installation of TrackMate and must be installed via its own [update site](https://sites.imagej.net/TrackMate-Lacss/). Lacss itself is a deep-learning (DL) model for single-cell segmentation from microscopy images.

The design of TrackMate-Lacss follows a server/client architecture, using the [GRPC](https://grpc.io/) communication protocol. In such case, the Lacss program runs as a GRPC server, listening on a TCP port, which the thin client TrackMate-Lacss uses to communicates with the server, sending the image data and receiving the segmentation results.

By default, Trackmate-Lacss will contact the open server (lacss.cam.uchc.edu) we have setup for this purpose. This simplify the workflow for most users, as they only need to install a small Fiji plugin to fully take advantage of the DL model's capability. The server-client design allows the user to perform computation quickly on limited hardware resources, becasue most of the computation is done on the server-side.

The user can also setup their own inference server. See [section](#running-your-own-server) below.

## Limitations

3D segmentation results will not be rendered in full. Instead, only a single point per cell will be displayed. This is a limitation of TrackMate itself and will be resolved in the next major release of TrackMate.

## Installation

In Fiji, go to {% include bc path='Help|Update...' %}, update, and click on {% include button label="Manage update sites" %} (bottom-left). A new window containing all the known update sites will appear. Check the  **TrackMate-Lacss** box, perform update, and restart Fiji. 

## Usage

#### Lacss Parameters in the TrackMate UI

##### `Server`

The address to the GRPC server in the format of `hostname:port`. The default is `lacss.cam.uchc.edu`.

##### `Access token`

An optional security token. Only used if you are running your own server.

##### `Minimum Cell Area`

The minimum cell area/volume in units of pixels.

##### `Scaling Factor`

If not 1, the input image will be resized internally before sent to the model. This is useful if your cell sizes (in pixels) differ significantly from those of the training data.

##### `Score Treshold`

Minimum score needed to be considered a valid prediction. 

##### `NMS IOU`

Lacss is an object detection model, and can detect cells that are right on top of each other. If you want to disable this behavior, set a non-zero IOU threshold to remove overlapping cells.

##### `Multi-Channel`

By default the segmentation is performed by considering all channels. Uncheck this to segment on only the first channel.


## Running your own server

TrackMate-Lacss runs on a client-server architecture. By default, TrackMate-Lacss will contact the open-server at lacss.cam.uchc.edu:443. But some may want to run your own server (e.g. on your own intranet to improve data transfer speed).

### Install Lacss

The short version:

```shell
pip install lacss[cuda12]
```

Slightly longer version: See the [Lacss Documentation](https://jiyuuchc.github.io/lacss/install/) for more details. We recommend installation on a Linux computer with a dedicated GPU.

_Lacss installation is independent of Fiji._

### Starting the server

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
The `<path_to_model_file>` is the local path to the file that contains the model parameters. See [Lacss](https://github.com/jiyuuchc/lacss) page for download linkes.


## Running a Cellpose server

You can also run a "Lacss" server backed by the [cellpose](https://cellpose.readthedocs.io/en/latest/do3d.html) model as its backend. To do that

#### Install cellpose
In most cases, this is simply
```shell
pip install cellpose
```
But see [full documentation](https://cellpose.readthedocs.io/en/latest/do3d.html) for more details.

#### Install Lacss
```shell
pip install lacss
```
Note that in this case, you do not need the `cuda12` option.

#### Start server
```shell
python -m lacss.deploy.cellpose_server
```


-----

* This plugin and page was adapted from Jean-Yves Tinevez's Trackmate-Cellpose plugin and wiki page.
* Last updated: July 2024*
