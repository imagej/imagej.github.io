---
title: Cellpose-Appose 
description: PLugin to use Cellpose from Fiji relying on Appose.
artifact: fiji.plugin:Cellpose_Appose
categories: [Segmentation]
---


This is a plugin to install and run [cellpose](https://www.cellpose.org/) on 2D/3D in Fiji. 
Two version of cellpose is available:
- Cellpose (v3)
- Cellpose-SAM (v4)

This plugin is based on [Appose](https://github.com/apposed/appose), that automatically install python environment and allows python script execution with shared objects with Fiji.

## Installation

You can install the plugin for the unliste update site `Appose-Playground`:
in Fiji, go to `Help>Update...` then to `Manage Update Sites` in the window that opens.
Click `Add unliste update site`, name it `Appose-Playground` and write its address `https://sites.imagej.net/Appose-Playground`.

Select the Appose-Cellpose `.jar` file to install only this plugin, or keep all proposed plugins. 
Press `Apply changes` and restart Fiji when it's done.

> [!IMPORTANT]
> You should have a recent version of Fiji, based on Java 21 or more. Download a new version if you're current installation is too old.

## Usage

From Fiji
- Open the image that you want to process.  
- Launch one of the cellpose version available in the plugin:
  - `Plugins>Segmentation>Cellpose-Appose>Cellpose...` _see [here](#cellpose) for documentation_
  - `Plugins>Segmentation>Cellpose-Appose>Cellpose-SAM...` _see [here](#cellpose-sam) for documentation_
- Configure your Cellpose run through the Graphic Interface
- Press "Ok" and Enjoy!   

> [!NOTE]
> The python environment will be automatically installed in your home `.local\shared\appose` directory and activated from the plugin when needed.


## Cellpose

The option `Plugins>Segmentation>Cellpose-Appose>Cellpose...` allows to run CellPose v3.

## Cellpose-SAM

The option `Plugins>Segmentation>Cellpose-Appose>Cellpose-SAM...` allows to run CellPose v4 with SAM.

### Cuda selection
