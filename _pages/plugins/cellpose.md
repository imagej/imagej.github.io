---
title: Cellpose
---

## Running Cellpose in Fiji

{% include img name="cellpose-icon" src="/media/icons/cellpose.png" %} ![External image](https://fiji.sc/site/logo.png){:width="64px"}

[Cellpose](https://www.cellpose.org/) is a very efficient framework to segment cell or nucleus. 
It can run on a large variety of dataset or be retrained for specific dataset.

While Cellpose is a python package, several options exists in Fiji to run it:

- [Fiji-Cellpose](https://imagej.net/plugins/cellpose-appose): handles `Cellpose` thanks to [Appose](https://apposed.org/).
  Appose creates and activates python virtual environment automatically, without any action from the user.
  This [youtube tutorial](https://www.youtube.com/watch?v=orySPQ2Hk-w) shows how to use this plugin.
  
- [TrackMate-Cellpose](https://imagej.net/plugins/trackmate/detectors/trackmate-cellpose) allows to both run Cellpose to segment objects and track them in time.
  In the current version, the user has to install a virtual environment with `Cellpose` to be able to use it but in coming versions, it will be automatically handled also thanks to Appose.
  This [tutorial](https://github.com/AlexHego/Cellpose_TrackMate_LiveCell) guide you through the installation and usage of TrackMate-Cellpose, including creation of the python environment.
  
- [BioP](https://github.com/BIOP/ijl-utilities-wrappers) offers the possibility to run several deep learning algorithms, including `Cellpose` from Fiji.
  It also requires the user to install a virtual environment before to be able to use it.

  {% include icon name='info' content="You can find several resources to help you install the BioP plugin along with the virtual environment. This [youtube tutorial](https://www.youtube.com/watch?v=A_PW_N0np9A) shows you how to install a virtual environment, the BIOP plugin and run it. This [tutorial](https://www.protocols.io/view/installing-cellpose-for-fiji-on-a-multiuser-window-kxygxyr4wl8j/v1) guide you for a full installation in Windows operating system. This [repository](https://github.com/BioImaging-NKI/Cellpose-Fiji) provides macro to use the plugin and match labels from cell and nuclei." %}

- More generally, this page [https://imagej.net/scripting/python](https://imagej.net/scripting/python) indicates how to run python programs, as Cellpose, from Fiji.
