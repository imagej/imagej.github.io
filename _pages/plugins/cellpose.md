---
title: Cellpose
---

## Running Cellpose in Fiji

{% include img name="cellpose-icon" src="/media/icons/cellpose.png" %}

[Cellpose](https://www.cellpose.org/) is a very efficient framework to segment cell or nucleus. 
It can run on a large variety of dataset or be retrained for specific dataset.

While Cellpose is a python package, several options exists in Fiji to run it:

- [Fiji-Cellpose](https://imagej.net/plugins/cellpose-appose): handles `Cellpose` thanks to [Appose](https://apposed.org/).
  Appose creates and activates python virtual environment automatically, without any action from the user.
  
- [TrackMate-Cellpose](https://imagej.net/plugins/trackmate/detectors/trackmate-cellpose) allows to both run Cellpose to segment objects and track them in time.
  In the current version, the user has to install a virtual environment with `Cellpose` to be able to use it but in coming versions, it will be automatically handled also thanks to Appose.
  
- [BioP](https://github.com/BIOP/ijl-utilities-wrappers) offers the possibility to run several deep learning algorithms, including `Cellpose` from Fiji.
  It also requires the user to install a virtual environment before to be able to use it.
