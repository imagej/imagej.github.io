---
title: FAST-HIPPOS
categories: [Analysis]
icon: /media/icons/FAST-HIPPOS-icon.png
source-url: "https://github.com/Jalink-lab/FAST-HIPPOS"
update-site: "FAST-HIPPOS"
release-version: v0.9
support-status: Active
team-founders: ['@Jalink-lab']
team-maintainers: ['Jalink-lab', '@BioImaging-NKI', '@bvandenbroek']
---
{%- assign github            = page.github            -%}
{%- assign release-version   = page.release-version   -%}
{%- assign release-date      = page.release-date      -%}
{%- assign dev-status        = page.dev-status        -%}
{%- unless team-maintainers  -%} {%- assign team-maintainers  = page.team-maintainer  -%} {%- endunless -%}

# FLIM Analysis of Single-cell Traces for Hit Identification of Phenotypes in Pooled Optical Screening

FAST-HIPPOS is a collection of Fiji scripts to analyze and visualize multi-cell time-lapse experiments, detect hit cells based on user-set criteria and output their stage coordinates for e.g. photoactivation.
For non-screening applications it can function as a valuable tool for single-cell trace analysis, visualization and inspection.

<hr>

## Installation & requirements
Required activated [Fiji Update Sites](https://imagej.net/update-sites/following) (via Help -> Update... -> Manage Update Sites):
- FAST-HIPPOS
- CLIJ
- CLIJ2
- CSBDeep
- ImageScience
- IJ-PB Plugins
- PTBIOP
- SCF MPI CBG
(- StarDist)

Additionally, you need a working Cellpose (2.0 or higher) environment in Python. See the [Cellpose GitHub Readme](https://github.com/MouseLand/cellpose#installation) for installation instructions. (Note: FAST-HIPPOS was tested up to Cellpose 3. Although it may just as well work with Cellpose 4 (Cellpose-SAM), the last Cellpose 3 version can be installed with `pip install cellpose[gui]==3.1.1.2`.)

Before running FAST-HIPPOS, make sure that the [BIOP Cellpose wrapper](https://github.com/BIOP/ijl-utilities-wrappers/blob/master/README.md#cellpose) works correctly: follow their [installation instructions](https://github.com/BIOP/ijl-utilities-wrappers/blob/master/README.md#i-installation). Then make sure that the wrapper knows where your Cellpose environment is located and which type it is (conda or venv), by filling in the top two fields in `Plugins` -> `BIOP` ->  `Cellpose/Omnipose` -> `Cellpose...`:

<img src="https://github.com/user-attachments/assets/fefd2857-6880-40f2-901f-c9cdc08971aa" title="BIOP Cellpose wrapper" width="500">

You will find the FAST-HIPPOS commands in the Fiji menu under `Plugins` -> `Macros`. Below follows a description of the main command: FAST-HIPPOS. Details on the other commands follow below.
<hr>

## FAST-HIPPOS Workflow
1. *[Input images](https://github.com/Jalink-lab/dynamic-pooled-screening/#1-input-images)*
2. *[Pre-processing](https://github.com/Jalink-lab/dynamic-pooled-screening/#2-pre-processing)*
3. *[Cell segmentation](https://github.com/Jalink-lab/dynamic-pooled-screening/#3-cell-segmentation)*
4. *[Measuring single-cell (FLIM/intensity) traces](https://github.com/Jalink-lab/dynamic-pooled-screening/#4-measuring-single-cell-flimintensity-traces)*
5. *[Visualization](https://github.com/Jalink-lab/dynamic-pooled-screening/#5-visualization)*
6. *[Hit selection](https://github.com/Jalink-lab/dynamic-pooled-screening/#6-screening-hit-selection)*
7. *Output files*

## 1. Input images
Input images are multi-channel `.tif` files, or any proprietary microscopy format that is [supported by Bio-Formats](https://bio-formats.readthedocs.io/en/v8.2.0/supported-formats.html), including files containing multiple images.
FLIM is supported in several ways (mostly for Leica images):
  - Confocal TCSPC: lifetime component images, fitted with a double-exponential and exported from LASX (as 'raw ImageJ tif'). 
  - TauSeparation, directly from the `.lif` file
  - Fast FLIM
  - TauContrast
  - Lambert Instruments Frequency Domain FLIM (`.fli` files)

  Supported non-FLIM images are:
  - Ratio Imaging (2-channel `.tif` files)
  - Intensity (single-channel `.tif` files)

The macro can batch-process multiple files as well.

## 2. Pre-processing
Optionally, image corrections can be performed as preprocessing steps:
1. Stitching of mylti-tiled experiments, with the separate command `Stitch tiles` (tested for Leica `.lif` files). Fast 'no-calculation' stitching is done using the [Grid/Collection Stitching plugin](https://imagej.net/plugins/grid-collection-stitching) to ensure correct pixel size[^1] and to prevent image distortion. XY-Stage coordinates of image tiles are extracted from the OME metadata of the `.lif` file and stored in the stitched `.tif` file, together with the grid layout, the tile size and the tile overlap percentage.
2. Drift correction. A cross-correlation (cc) of image frames is performed with either the first frame, the previous frame or the last frame. CLIJ2 image projection functions are used to quickly determine the coordinates of the maximum pixel in the cross-correlation image, its distance from the center representing the shift. Drift correction is performed on the calculated intensity image (i.e. the addition of the two components, if applicable).
3. Bidirectional scanning phase mismatch correction. The even and odd lines are split and turned into two separate images. Cross-correlating these images and locating the peak yields the shift between the phases. The two images are both shifted half this distance and interleaved again:
[^1]: The exported pixel size is not entirely correct, causing an increasing deviation in the cell coordinates for increasing x and y.

![image](https://github.com/user-attachments/assets/66408493-ec41-4c4b-9413-3d6ae136e932)

After these optional steps, a 'weighted lifetime' image is created. For single-component FLIM images ('FAST FLIM', 'TauContrast', Frequency-domain FLIM) this is simply the lifetime; for a two-component FLIM image this is equal to the *intensity-weighted* lifetime. (Note that the intensities here are the intensities of the lifetime components!)
Additionally, an 'RGB overlay image' is created, where a (x,y,t) smoothed version of this lifetime image is multiplied (overlayed) by the total intensity image, yielding a denoised visualization of the experiment.  

![Cos7H250_ADRB2KO_1 (weighted lifetime)](https://github.com/user-attachments/assets/c66ad486-1d79-4c6b-9b3c-e95d7b4d6683)
![Cos7H250_ADRB2KO_1 (lifetime   intensity RGB overlay)](https://github.com/user-attachments/assets/3aba7cb8-d64b-4d65-964f-4af346cb6eb5)

## 3. Cell segmentation
cell segmentation can be performed with [CellPose](https://github.com/MouseLand/cellpose) (2 or 3), operated from Fiji using [a wrapper](https://github.com/BIOP/ijl-utilities-wrappers). The image stack is first 'collapsed' using a summed-intensity projection of a subset or all of the time-lapse images, resulting in a single imageto segment. This procedure works well if the imaging is short enough that the cells do not move (a lot).
The user can select the segmentation model (pretrained or custom) and needs to provide a few key parameters, e.g. cell diameter and [flow threshold](https://cellpose.readthedocs.io/en/v3.1.1.1/settings.html#flow-threshold). Additionally, restrictions on cell size and circularity can be imposed.

![Cos7H250_ADRB2KO_1 (lifetime   intensity RGB overlay)](https://github.com/user-attachments/assets/eb3099c0-e9e6-4d8c-8000-a7d5b41892c9)

## 4. Measuring single-cell (FLIM/intensity) traces
After cell segmentation ROIs are created from the obtained label image, after which intensities and average fluorescence lifetimes are computed for every cell, at every time point. This average lifetime is the weighted lifetime, where each pixel of a cell is linearly weighted with its intensity fraction.

The script automatically tries to determine the time points of a(nta)gonist stimulation and calibration by detecting peaks in the second derivative of the average trace of all cells. If the peaks are higher than a set number of times the stddev of the signal it is picked up. If successful, cell traces are divided into three parts: *baseline*, *response*, and *calibration*. If not, manual input of the time points is also possible. These three partitions are used for detection of hit cells when screening for dynamic phenotypes. If no stimulation and calibration frame are found or set, the full trace is regarded as *response*.

<img src="https://github.com/user-attachments/assets/52832275-d256-4162-8a86-7ee22ab6f2df" title="first and second derivative of the average trace" width="500">

## 5. Visualization
The data is visualized in various graphs and images:
### Time traces plot
<img src="https://github.com/user-attachments/assets/a23f8818-b754-4b01-93ab-b5e1a6dff63e" title="lifetime traces plot" width="510">

### Timelapse Lifetime histogram and scatterplots
<img src="https://github.com/user-attachments/assets/87c92c02-cf5d-4e7f-b391-40c858a6ffa9" title="Kymograph" width="400">
<img src="https://github.com/user-attachments/assets/d750ebd6-a1d4-4687-83cc-bfae930cc858" title="Sorted Kymograph" width="400">

### Kymographs
This is an image with time as y-coordinate, Cell ID as x-coordinate and cell lifetime as value. Additionally, a 'sorted kymograph' is created, where the X-axis is sorted on the average response lifetime.

![Cos7H250_ADRB2KO_1 (kymograph)](https://github.com/user-attachments/assets/5c64cad6-374c-481d-8b0c-273819a7bcce)
![Cos7H250_ADRB2KO_1 (kymograph sorted)](https://github.com/user-attachments/assets/bd32872a-b9af-4a52-b63e-8e685f17850e)

### Density plot
A 2D histogram with lifetime on the y-axis and time on the x-axis. This image allows a better visual assessment of the heterogeneity of traces compared to the Time Traces plot.

<img src="https://github.com/user-attachments/assets/9b904263-e3ae-46f2-ab06-7fdb56b0b5af" title="Density plot" width="400">

## 6. Screening: hit selection
When `activate screening` is selected in the starting dialog, cells showing certain kinetic behaviour can be detected, and the stage coordinates of these 'hit'cells are written to a `.rgn` file for subsequent photoactivation (or e.g. high-resolution imaging, run FRAP experiments, etc.). This file can then be loaded into the Leica LAS X Navigator, where the hit cells will be marked as imaging positions.
Because many possible interesting dynamic phenotypes exist, the script provides several possible rules and criteria, that can be combined (AND / OR) when desired:

### Hit criteria panel
![image](https://github.com/user-attachments/assets/774ae993-dc11-41e1-8f26-1f59d42c270c)


### Time traces plot of hits
After hit detection, a graph is generated showing only the traces of the hit cells. Here, the selected time window used in the hit selection (in this example the full response time) is highlighted in blue. Compare with the plot containing all the single-cell traces:

<img src="https://github.com/user-attachments/assets/3ea842f1-83b4-49fc-842f-ce76d3c63542" title="lifetime traces plot - hits only" width="510">
<img src="https://github.com/user-attachments/assets/a23f8818-b754-4b01-93ab-b5e1a6dff63e" title="lifetime traces plot" width="510">

The hit cells are also displayed in a table, as well as their positions graphically:

<img src="https://github.com/user-attachments/assets/07703a58-82ac-4303-b720-fc5a0f071c2b" title="lifetime traces plot" width="500">
<img src="https://github.com/user-attachments/assets/fca0f6d1-65bb-4f7a-8b42-6208eda40602" title="lifetime traces plot" width="450">
