---
title: ALPACA
dev-status: Stable
support-status: Active
description: A tool to assess cell-based assays for ciliopathy patients to improve accurate diagnosis
Creator: Cenna Doornbos
Developer: "@tschmenger"
doi: 10.1038/s41431-021-00907-9
---
# Overview
Skeletal ciliopathies are a group of disorders caused by dysfunction of the cilium, a small signaling organelle present on nearly every vertebrate cell. The cell-based assay consists of three parameters; (1) ciliogenesis, (2) cilium length and (3) retrograde intraflagellar transport (IFT). The ALPACA macro suite is able to quantify these parameters.

# Citation
Please cite ALPACA like this:

{% include citation %}

# Description
## How to use
This pipeline is based on the free to download software packages of ZEN and FIJI. After selecting the update site for ALPACA in FIJI by clicking --> **HELP** --> **Update** --> **Manage Update Sites** you will find the ALPACA macros after clicking on <span style="color: red"> >> </span> under **Cilia Tools**. You can find more information about performing the cell-based assay and taking the images in *Doornbos et. al. 2021* and the manual below.

## Using the 'Whole Cilia analysis tool' function
This macro will perform the individual macros in an all-in-one fashion. The user will asked to select the folder containing the images and to select values for several analysis variables (default values are provided). The analysis will then performed automatically, including **counting of nuclei**, **measuring of cilia length** & **assessing intraflagellar transport (IFT)**. The output will contain *.tif* images and spreadsheets. 

## Using individual macros
Instead of performing the complete analysis the user may choose to execute only a single macro at the time.

# Manual
For a detailed manual please see [The ALPACA manual](https://github.com/tschmenger/imagej.github.io/blob/ae937d6b904f3de36712dc35b1d55e879a45b42f/media/plugins/alpaca_manual.pdf).
