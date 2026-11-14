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
from a single window, with no programming or command line.

Workflows: semantic segmentation, instance segmentation, object detection, denoising, super-resolution,
self-supervised learning, image classification and image-to-image translation, in 2D and 3D.

- **Wizard**: a few questions about your task, a check of your data (with a preview of the images next to their
  targets) and a configuration adapted to it, in the spirit of nnU-Net. It also looks for pretrained models of the
  [BioImage Model Zoo](https://bioimage.io) that fit your workflow, such as Cellpose-SAM and Cellpose-DINO for cell and
  nucleus segmentation, which can be used as they are or fine-tuned with your data.
- **Run workflow**: runs any BiaPy configuration on a GPU (NVIDIA, or Apple Silicon) or on the CPU, and shows the
  training curves, the predictions and the results as the job goes.
- **Job history**: the jobs run, to open their results or run them again.
- **Apply model** ({% include bc path='Plugins|BiaPy|Apply model' %}): applies a model trained with BiaPy or a model of
  the BioImage Model Zoo to an image open in Fiji, and opens its results in Fiji (instances, classes, points...).

## Installation

1. Start Fiji (or [download it](https://fiji.sc) first).
2. Select {% include bc path='Help|Update...' %} from the menu bar.
3. Click on {% include button label='Manage update sites' %}.
4. Tick the checkbox of the update site `BiaPy` and click {% include button label='Apply and Close' %}.
5. Click on {% include button label='Apply changes' %} and restart Fiji.
6. Open {% include bc path='Plugins|BiaPy|Apply entire workflow' %}. In the HOME tab, click on {% include button label='Install BiaPy' %}:
   it downloads BiaPy and PyTorch into the Fiji folder (several GB, only the first time).

## Documentation and support

- BiaPy's documentation: [biapy.readthedocs.io](https://biapy.readthedocs.io)
- Questions: the [image.sc forum](https://forum.image.sc/tag/biapy) with the `biapy` tag
- Bugs and suggestions for the plugin: [BiaPy-Fiji issues](https://github.com/BiaPyX/BiaPy-Fiji/issues)

## Citation

When you use BiaPy, please cite it (each job also writes the works to cite for its configuration in `CITATIONS.md`):

> Franco-Barranco, D., et al. BiaPy: accessible deep learning on bioimages. *Nature Methods* (2025).
> [https://doi.org/10.1038/s41592-025-02699-y](https://doi.org/10.1038/s41592-025-02699-y)
