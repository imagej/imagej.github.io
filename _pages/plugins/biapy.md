---
title: BiaPy
name: BiaPy
description: Deep learning for bioimage analysis in Fiji, with BiaPy's workflows, a wizard that adapts them to your data and BioImage Model Zoo models.
categories: [Machine Learning, Segmentation]
icon: /media/icons/biapy.png
website: https://biapyx.github.io
doi: 10.1038/s41592-025-02699-y
update-site: BiaPy
source-url: https://github.com/BiaPyX/BiaPy-Fiji
license-label: MIT
forum-tag: biapy
dev-status: Active
support-status: Active
team-founders: ['@iarganda', 'Daniel Franco-Barranco']
team-maintainers: ['Daniel Franco-Barranco']
---

<img src="/media/icons/biapy.png" alt="BiaPy logo" width="128"/>

## Overview

[BiaPy](https://biapyx.github.io) is an open-source library to build deep learning workflows for bioimage analysis. This
plugin brings it to Fiji: it installs BiaPy in its own Python environment and lets you create, run and follow BiaPy jobs
from Fiji, with no programming or command line.

**Supported workflows** (2D and 3D): semantic segmentation, instance segmentation, object detection, denoising,
super-resolution, self-supervised learning, image classification and image-to-image translation.

The plugin adds two entries to the **Plugins > BiaPy** menu:

| Menu entry | What it is for |
|---|---|
| {% include bc path='Plugins|BiaPy|Run BiaPy' %} | Create, train and test models on **folders of images**, with a wizard. |
| {% include bc path='Plugins|BiaPy|Apply model' %} | Apply a trained model to an **image already open in Fiji**. |

### Run BiaPy

{% include video platform="youtube" id="htIGUCJJlAk" %}

A single window with three tabs:

- **HOME**: links (project, forum, documentation, templates, notebooks, citation), the status of the Python environment
  (install BiaPy with one click, or point to an existing Python that has BiaPy) and the GPUs detected.
- **WIZARD**: a short questionnaire about your task, followed by a check of your data. After each data folder is
  checked, it shows a preview of the images next to their targets and warns about anything that looks wrong for the
  chosen workflow. The Wizard then creates a configuration file **adapted to your data**, following the rules of
  [nnU-Net](https://github.com/MIC-DKFZ/nnUNet): patch and batch size from the image shapes and your GPU memory,
  network topology from the voxel spacing, class and foreground statistics, and so on. For instance segmentation it
  measures the shape of your training instances and suggests the representation the network should predict
  (foreground + contour, distance map, StarDist, Cellpose flows, affinities...), with an explanation of each. It also
  searches the [BioImage Model Zoo](https://bioimage.io) for pretrained models that fit your data (for example
  Cellpose-SAM and Cellpose-DINO for cell and nucleus segmentation), which you can use as they are or fine-tune with
  your data.  
- **RUN WORKFLOW**: select a configuration, an output folder, a job name and a device (NVIDIA GPU, Apple Silicon or
  CPU), run BiaPy and follow its output (training curves, predictions and results) as the job goes. The job can be
  stopped at any time.

The plugin also keeps a **job history**, to open the results of previous jobs or run them again.

### Apply model

{% include video platform="youtube" id="JOdaSDS_rvA" %}

Applies a model to the image you have open in Fiji and opens the results in Fiji (labeled instances, classes, points...):

- The model can be a **BiaPy checkpoint** (`.pth`) or a **BioImage Model Zoo** model.
- Zoo models are downloaded only when you press Apply. You can keep a copy in your computer's cache so they are not
  downloaded again.
- The model stays loaded between images, so applying it to several images is fast.
- You can choose which outputs to open (`raw`, `final` or `post`, i.e. raw network output, final result and
  post-processed result) and the device to use.

It can also be used from macros and scripts, without the window. When you apply a model in the window, the command
is recorded with {% include bc path='Plugins|Macros|Record...' %}:

```java
run("Apply model", "model=[/path/to/model.pth] outputs=[final post] device=0");
run("Apply model", "model=affable-shark device=cpu keep");
```

| Option | Meaning |
|---|---|
| `model` | A `.pth` checkpoint, or the nickname of a BioImage Model Zoo model (e.g. `affable-shark`). |
| `outputs` | Optional. Any of `raw`, `final`, `post`. By default, the ones the window opens. |
| `device` | Optional. A GPU number, `mps` (Apple Silicon) or `cpu`. By default, the device used last, otherwise the GPU with the most free memory. |
| `keep` | Optional. Keeps a zoo model in the cache so it is not downloaded again. |

## Requirements and compatibility

- Fiji-Stable (Java 8) and Fiji-Latest (Java 21), on Windows, macOS and Linux.
- An internet connection and several GB of free disk space for the first installation.
- A GPU is optional (NVIDIA, or Apple Silicon), but recommended for training.

## Installation

1. Start Fiji (or [download it](https://fiji.sc) first).
2. Select {% include bc path='Help|Update...' %} from the menu bar.
3. Click on {% include button label='Manage update sites' %}.
4. Tick the checkbox of the update site `BiaPy` and click {% include button label='Apply and Close' %}.
   If it is not in the list yet, click {% include button label='Add Unlisted Site' %} and use the URL
   `https://sites.imagej.net/BiaPyX/`.
   <img width="830" height="436" alt="biapy_update_site" src="https://github.com/user-attachments/assets/c5c749d7-a0e1-44ce-ba50-41a47d6202d9" />
5. Click on {% include button label='Apply changes' %} and restart Fiji.
6. Open {% include bc path='Plugins|BiaPy|Run BiaPy' %}. In the **HOME** tab, click on
   {% include button label='Install BiaPy' %}: it creates a Python environment inside the Fiji folder and downloads
   BiaPy and PyTorch into it (several GB, only the first time).
   {% include bc path='Plugins|BiaPy|Apply model' %} has the same installation option in its first tab.
   <img width="1062" height="762" alt="biapy_home_install" src="https://github.com/user-attachments/assets/8b10ee60-3289-47ea-bd9f-42cb9767a00c" />

If you already have a Python environment with BiaPy, use **HOME > Use existing Python...** instead.

## Documentation and support

- BiaPy's documentation: [biapy.readthedocs.io](https://biapy.readthedocs.io)
  - [Installation in Fiji](https://biapy.readthedocs.io/en/latest/get_started/installation.html)
  - [Pretrained models and BioImage Model Zoo](https://biapy.readthedocs.io/en/latest/get_started/bmz.html)
- Video demo: [BiaPy for Fiji](https://youtu.be/htIGUCJJlAk)
- Questions: the [image.sc forum](https://forum.image.sc/tag/biapy) with the `biapy` tag
- Bugs and suggestions for the plugin: [BiaPy-Fiji issues](https://github.com/BiaPyX/BiaPy-Fiji/issues)

## Citation

When you use BiaPy, please cite it (each job also writes the works to cite for its configuration in `CITATIONS.md`):

> Franco-Barranco, D., et al. BiaPy: accessible deep learning on bioimages. *Nature Methods* (2025).
> [https://doi.org/10.1038/s41592-025-02699-y](https://doi.org/10.1038/s41592-025-02699-y)

## Third-party content

The emoji of the BioImage Model Zoo models are shown with [Twemoji](https://github.com/jdecked/twemoji) images
(© Twitter, Inc and other contributors, licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)).
