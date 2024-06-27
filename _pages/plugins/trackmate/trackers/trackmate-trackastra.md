---
title: TrackMate Trackastra
description: Trackastra integration in TrackMate
categories: [Tracking,Deep Learning]
icon: /media/icons/trackastra-icon.png
description: Trackastra integration in TrackMate.
categories: [Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Trackastra
---

TrackMate integration of the **Trackastra** transformer-based tracking algorithm, by Benjamin Gallusser and Martin Weigert. 
If you use this tracker in your work, please be so kind as to cite the paper that describes it:

{% include citation doi="10.48550/arXiv.2405.15700" %}

## Installation

### Install Trackastra

To use this tracker in TrackMate, you first need a working installation of Trackastra on your computer.
Please follow the instructions on the GitHub repository of Trackastra:
[https://github.com/weigertlab/trackastra?tab=readme-ov-file#installation](https://github.com/weigertlab/trackastra?tab=readme-ov-file#installation)

Once done, let's test that it works. 
Supposing that you created a conda environment name `trackastra`, type the following in a terminal:

```sh
> conda activate trackastra
> trackastra track --help
```
This should print:
```sh
usage: trackastra track [-h] -i IMGS -m MASKS [--output-ctc OUTPUT_CTC] [--output-edge-table OUTPUT_EDGE_TABLE] [--model-pretrained MODEL_PRETRAINED] [--model-custom MODEL_CUSTOM]
                        [--mode {greedy_nodiv,greedy,ilp}] [--device {cuda,cpu}]

options:
  -h, --help            show this help message and exit
  -i IMGS, --imgs IMGS  Directory with series of .tif files.
  -m MASKS, --masks MASKS
                        Directory with series of .tif files.
  --output-ctc OUTPUT_CTC
                        If set, write results in CTC format to this directory.
  --output-edge-table OUTPUT_EDGE_TABLE
                        If set, write results as an edge table in CSV format to the given file.
  --model-pretrained MODEL_PRETRAINED
                        Name of pretrained Trackastra model.
  --model-custom MODEL_CUSTOM
                        Local folder with custom model.
  --mode {greedy_nodiv,greedy,ilp}
  --device {cuda,cpu}
```

### Configure conda path in Fiji

Because this integration relies on **conda**, we need to tell TrackMate where is conda on your system.
There is a command to do this in the _Edit > Options >Configure TrackMate Conda path..._

You must find the actual executable of conda or mamba or micromamba on your system, not the alias.
This is typically where you installed your conda distribution, plus something like `condabin` or `bin`. 
To find it on my system where I installed mamba I typed `which mamba` in a terminal:
```sh
> which mamba
/Users/tinevez/mambaforge/bin/mamba
```
I then browsed to this path in the configuration window then clicked the `OK` button.

{% include img src="/media/plugins/trackmate/trackmate-trackastra-01" align='center' width='400' %}