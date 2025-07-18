---
title: TrackMate-Cellpose
categories: [Segmentation,Tracking,Deep Learning]
icon: /media/icons/cellpose.png
description: cellpose integration in TrackMate.
categories: [Segmentation,Tracking,Machine Learning]
artifact: sc.fiji:TrackMate-Cellpose
section: TrackMate-Cellpose.:Usage:cellpose parameters in the TrackMate UI.
---

{% include img src="/media/plugins/trackmate/trackmate-cellpose-screenshot.png" align='center' width='500' %}

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [cellpose](https://cellpose.readthedocs.io/en/latest/) to segment cells in 2D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following). It also requires cellpose to be installed on your system and working independently. This tutorial page gives installation details and advices at how to use the cellpose integration in TrackMate.

cellpose is a segmentation algorithm based on Deep Learning techniques, written in Python 3 by Carsen Stringer and Marius Pachitariu. The TrackMate-cellpose module, which is written in Java, is an example of integration via sub-processes. The integration technique is similar to that of the [TrackMate-Ilastik](trackmate-ilastik) module, except that the iastik authors offer a ready-to-use Java bridge that took care of launching ilastik from Fiji. For the TrackMate-cellpose module, we built our own, based on ideas proposed by [Olivier Burri](/people/lacan), [Romain Guiet](/people/romainGuiet) and [Nicolas Chiaruttini](/people/NicoKiaru) from the [BIOP](https://www.epfl.ch/research/facilities/ptbiop/) team in the EPFL.

If you use the cellpose TrackMate module for your research, please also cite the cellpose paper:

_{% include citation doi='10.1038/s41592-020-01018-x' %}_


## Installation

We need to subscribe to an extra update site in Fiji, and have a working installation of cellpose on your system.

### TrackMate-Cellpose update site

In Fiji, go to {% include bc path='Help|Update...' %}. Update and restart Fiji until it is up-to-date. Then go to the update menu once more, and click on the `Manage update sites` button, at the bottom-left of the updater window. A new window containing all the known update sites will appear. Click on the  **TrackMate-Cellpose** check box and restart Fiji one more time. 

### cellpose

This step is completely independent of Fiji. If you have already a working cellpose installation, you can skip this section entirely. But we absolutely need a working cellpose.

There are many ways to get cellpose installed. We give a subset of them in the [last section of this document](#installing-cellpose).


## Usage

### Cellpose parameters in the TrackMate UI

{% include img src="/media/plugins/trackmate/trackmate-cellpose-ui-01.png" align='center' width='300' %}
We document these parameters from top to bottom in the GUI.

##### `Path to cellpose / Python executable`

We must specify where is the cellpose executable, as it was installed outside of Fiji. Because there are several ways of installing cellpose (with Conda or using the precompiled executables), we have to accommodate several cases we document [later in this document](#installing-cellpose). Briefly:

- If you installed cellpose via the precompiled executables, enter the _path to the executable_. For instance:  `C:\Users\tinevez\Applications\cellpose.exe`
- If you installed cellpose via Conda, enter the _path to the Python executable of the Conda environment you created for cellpose_. For instance: `C:\Users\tinevez\anaconda3\envs\cellpose\python.exe`

##### `Pretrained model`
Right now we only support three pretrained models of cellpose:
- the `cyto` model ("Cytoplasm"), to segment cells stained for their cytoplasm;
- the `nuclei` model ("Nuclei") to segment cell nuclei;
- the `cyto2` model ("Cytoplasm 2.0"), which is the `cyto` model augmented with user-submitted images.
- the `live cell` model from Cellpose was trained on the `LIVECELL` [dataset](https://sartorius-research.github.io/LIVECell/) of label free images of cells. 
- the `TissueNet` model from Cellpose was trained on the `TissueNet` [dataset](https://datasets.deepcell.org/data) available from deepcell.
- "Custom" lets you specify a custom model you would have trained or downloaded, which is documented below.

##### `Path to custom model`

If in the `Pretrained model` selection you pick `Custom`, a text field will appear above, allowing for entering the path to a custom cellpose model. You need to browse to the actually model file generated by the training. For instance: `D:\Projects\Brightfield\Cellpose model 171121-20211118T111402Z-001\171121\cellpose_residual_on_style_on_concatenation_off_train_folder_2021_11_17_19_45_23.398850`

Note that it must be the an `absolute path` to the file.

##### `Channel to segment`

If your image has several color channels, choose here the channel to segment. The number of the channel corresponds to the _imagej channel_ in your image. 
It should be the channel where the cytoplam staining is for cell segmentation, or the nuclei staining for nuclei segmentation, e.g. with the `nuclei` model.

Note that TrackMate doesn't handle RGB stacks so you might need to convert your image if it is not already a composite image (see below for [tip on how to pass RGB images to TrackMate-Cellpose](#tip-passing-rgb-images-to-trackmate-for-cellpose))

##### `Optional second channel`

The `cyto` and `cyto2` pretrained models have been trained on images with a second channels in which the cell nuclei were labeled. It is used as a seed to make the detection of single cells more robust.
It is optional and this parameter specifies in which channel are the nuclei (the number of the imagej channel of the nuclei). Use '0' to skip using the second optional channel.
For the `nuclei` model, this parameter is ignored.

##### `Cell diameter`

cellpose can exploit an _a priori_ knowledge on the size of cells. If you have a rough estimate of the size of the cell, enter it here. In TrackMate this parameter must be specified in physical units (for instance µm if the source image has a pixel size expressed in µm).
Enter the value '0' to have cellpose automatically determine the cell size estimate.

##### `Use GPU`

If this box is checked, the GPU will be used _if cellpose was installed with required librairies and hardware to use the GPU_. If the GPU support is absent or incorrect, this setting will be safely ignored and the computation will rely on CPU only. Unchecking the box will force cellpose to use the CPU even if GPU support is available.

##### `Simplify contours`

If this box is checked, the contour outlines generated by the masks returned by cellpose will be smoothed and simplified. This is the same treatment that is used by other TrackMate detectors and documented [here](/plugins/trackmate/trackmate-v7-detectors#simplifying-contours).


### (Re)Training of a cellpose model

To optimize CellPose on your data, you can retrain one its model and use it in TrackMate-CellPose. You can do the retraining easily through [CellPose 2.0 GUI](https://www.nature.com/articles/s41592-022-01663-4). When the model gives acceptable results, select it in TrackMate interface with the `custom_model` parameter. 

Note that in 3D stacks, it can be worth it to create xy, yz and xz images of the stack corrected for anisotropy and to draw annotations on it to train the model to make it more performant for the segmentation with the `3D mode`.




## Tutorials

### Tracking cells stained for cytoplam with cellpose

One of the central  advantage of cellpose is its ability to give robuset segmentation results for cells stained for cytoplasm. We will use such a movie in this tutorial. You can download the movie from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5864646.svg)](https://doi.org/10.5281/zenodo.5864646)

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-01" align='center' width='400' %}

These are breast cancer cells moving collectively. We are tracking them to analyze how their migration parameters change in various conditions.

The movie comes from RGB images that have already been split in 3 separated components. The blue channel is empty. The red channel display the cell nuclei. The cells are stained for cytoplasms in the green channel, with a lot of variability from one cell to another. The texture and sometimes the intensity hints the cell border. This is an image that would be considered very hard to segment with classical techniques. 

Open Fiji and load the image. Then launch TrackMate in {% include bc path='Plugins|Tracking|TrackMate' %}.
In the second panel, select the **cellpose detector**:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-02" align='center' width='400' %}

then click the `Next` button. You should see the configuration panel for cellpose. 

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-03" align='center' width='300' %}

We want to segment the touching cells and obtain their contour. So we will use the **Cytoplasm** model. The cytoplasm is imaged in the second channel (it happens to use the green LUT, but it would not matter) so we enter **2** for the `Channel to segment` parameter. The channel **1** contains the nuclei so we can specify it in the `Optional second channel` parameter. Finally, we can measure a rough estimate of the cell size using ImageJ ROI tools, which is about **40 µm**, and enter this value in the `Cell diameter` field.

The movie is quite big, and will take several minutes to process using only the CPU (on my Mac it takes about 20 minutes without multithreading). Having a cellpose installation with GPU support really accelerate segmentation, but this is not available on Mac. Instead, for  we developed TrackMate-cellpose so that on Mac, it can accelerate processing using multithreading. CPU multithreading is used only on Mac and if the `Use GPU` box is unchecked, which is why it is the case on the image above.

Finally, for this movie we want the cell contour to follow the pixels of the masks generated by cellpose, so we unchecked the `Simplify contour` box.

Then we are ready to launch segmentation. Click the `Next` button. The log window will echo the messages from cellpose. On a windows machine with GPU support, the detection step takes about 2 minutes. On a Mac with multithreading using 8 cores, it takes about 4 minutes.

The **Initial thresholding** reports the quality histogram for all detections. Here, the quality is just the area of detections in pixel units. We see that there are some detections with very little size, probably for spurious objects. We can filter them out by setting a threshold value around 220.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-04" align='center' width='300' %}

Click the `Next` button.  In the **Spot filter** panel TrackMate first computes all the spot features. Then the results are shown. Given the difficulty of the segmentation task, the results are surprisingly good, and we should thank cellpose for it. They are not perfect though. For some big and faint cells, we can see a few events of oversegmentation, probably caused by red granules drifting in some cells. Still, we can follow cell division by eye and see that the vast majority of them is detected properly.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-05" align='center' width='400' %}

We don't need to filter the detections so click the `Next` button. Our aim is to detect cell divisions as they migrate, so we have to pick either the LAP tracker of the Overlap tracker. Given the cell density we would normally use the LAP tracker. However it would introduce too many false positive in the cell division detection. Indeed, the cells migrate "downwards" in the image, and new cells appear in the field-of-view from the top of the image. These new cells would be elected as candidates to be the daughter emerging from a non-existent division of the cell just below it. The overlap tracker will be more robust against this artifact so we elect to chose it. 

We use the following parameter:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-06" align='center' width='400' %}

We dilate the cells with a `Scale factor` of *1.2* so that if the daughter cells moved away from the mother cell they are still linked to the mother. A `Minimal IoU` value of *0.3* mitigate false cell division detections. Choosing the *Precise* method for `IoU calculation` has some cost on tracking time (5 s. versus 1 s. for the *Fast* method) but it is so short in our case that we still use it.

Here is what the tracking results look like:

{% include video src="/media/plugins/trackmate/trackmate-cellpose-tutorial-07.mp4" width='600' align="center" %}

In the movie above the cells are colored by their track ID, which tends to highlight tracking mistakes and missed detections. Indeed, some cell divisions are missed. Still the results are better than what they would be with the LAP tracker, due to the bias for low Y value discussed above.

### Using a custom cellpose model to track cells imaged in bright-field

Another key advantage of cellpose is that it is relatively easy and fast to train or augment a model to harness difficult use cases that are not handled well by the pretrained model.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-01" align='center' width='400' %}

For instance the cells above were imaged in bright-field at high resolution. They are Glioblastoma-astrocytoma U373 cells migrating on a polyacrylamide gel. They have a rather complex shape and a low contrast. The segmentation of cells in such images is normally difficult with classical image processing techniques. In the following we will use the trackMate-Cellpose intragration to segment and track them. Our goal is to see if we discriminate between two types of cell locomotion based on dynamics and morphological features of single cells. We will see how to give more robustness to the analysis by filtering out some detections close to image border.

The data can be obtained from Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5863317.svg)](https://doi.org/10.5281/zenodo.5863317)

The dataset contains a custom cellpose model. We have trained a it using the [ZeroCostDL4Mic platform](https://github.com/HenriquesLab/ZeroCostDL4Mic/wiki). This cellpose model was trained for 500 epochs on 214 paired image patches (image dimensions: 520x 696), with a batch size of 8, using the [Cellpose ZeroCostDL4Mic notebook (v 1.13)](https://colab.research.google.com/github/HenriquesLab/ZeroCostDL4Mic/blob/master/Colab_notebooks/Beta%20notebooks/Cellpose_2D_ZeroCostDL4Mic.ipynb). The cellpose `cyto2` model was used as a training starting point. The training was accelerated using a Tesla K80 GPU.

To use the model you need to unzip the `Cellpose model 171121-20211118T111402Z-001.zip` file. The cellpose model file itself is the `cellpose_residual_on_style_on_concatenation_off_train_folder_2021_11_17_19_45_23.398850` file in the `171121` folder.
We can use it in TrackMate by specifying "Custom" as a model in the interface:
{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-02" align='center' width='350' %}

Here I am running TrackMate on a Windows machine, and I used the cellpose installation recommended by BIOP people ([see below](#biop-conda-installation-for-gpu-support-on-windows)). So in the `Path to cellpose / Python executable` I have: `C:\Users\tinevez\anaconda3\envs\cellpose_biop_gpu\python.exe` 

As `Pretrained model` I picked **Custom** and in the `Path to custom model` text field I entered the path to the model file (in this case, ending in `.398850`).

There is only one channel, so I used **0** for both the target and optional channels. The cell size measured with ImageJ is about 60 µm.

On this Windows machine and with this cellpose installation I have GPU support, so I left the corresponding box checked. Later we will measure shape descriptors for the cell, so it is important to simplify their contours, and the corresponding box is also checked. 

Clicking `Next` starts the segmentation. In my case it completes in about 1 minute. In the **Initial thresholding** panel, choose a threshold of 0 to include all detections in the next step. We get the following results displayed in the **Spot filter** panel:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-03" width='300' %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-04" width='300' %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-05" width='150' %}

The contours are not absolutely perfect. In a few cases they miss a cell extrusion or include a debris that touches the cell. Some cells that touch the border of the image are not detected. But overall the results are very good and there is no spurious detection. We don't need to add spot filters at tis step.

For this movie, the tracking part should be simple as the cells are well separated and move by a distance smaller than their size from one frame to the next. Yet, we have to bridge over the missed detections when cells were close to the border. The **Simple LAP tracker** is suitable for this case:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-06" width='300'  align='center' %}

The max distance are taken from the cell size. Note the large max frame gap, chosen to accommodate several missed detections near the image borders. As final results we get:

{% include video src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-07.mp4" width='600' align="center" %}

We can distinguish roughly two modes of motion for the cells in this movie. The two cells in the bottom-left part of the image display saltatory movements with extrusion forming on changing sides of the cell, followed by a retraction and a large but brisk movement of the nucleus. The other cells display a large lamellipodium and exhibit a smooth motion in the direction of the protrusion.

We can use the **Plot features** panel to investigate these behaviors quantitatively. For instance, one of the two cells in the bottom-left (in blue in the movie above and in the figure below) display this dynamics for the cell area and speed:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-08" width='600'  align='center' %}

We see that brisk changes in area, corresponding to retraction events, correlate with peaks in velocity. 

To generate these plots first select the cell of interest by clicking inside it in the image. In the **Plot features** panel, select first the **Spots** tab and choose **T** as a feature for the X axis, and **Area** for the Y axis. There are 3 radio buttons that allow selecting what objects will be used to plot features. In our case we want to select **Tracks of selection** to have the data from only the cell we selected. Click the **Plot features** button to generate a first graph. 

The velocity is defined for links (edge between two detection across time), so click on the **Links** tab, and choose **Edge time** for X and **Speed** for Y. Click the **Plot features** button to generate the second graph. 

The same metrics are different for the cell on the right:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-09" width='600'  align='center' %}

There seems to be a peak in velocity at late times along with a decrease in area, but this might be due to the cell crossing the right border of the image. We can prune these incorrect data points by filtering out the cells that touch the borders of the image. 

To do this, navigate back in TrackMate to the **Spot filter** panel. We will add a filter on the cell position to hide the detections too close to the border. Let's add a filter that keeps cells which center is below 420 µm:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-10" width='300'  align='center' %}

Then proceed as before for the tracking step and the plot generation. The area and velocity plots for the filtered cell track does not show the peak in velocity we had without filtering.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-b-11" width='600'  align='center' %}


### 3D segmentation with cellpose

A tutorial in the documentation for the [advanced version of the cellpose detector](trackmate-cellpose-advanced) demonstrates how to use cellpose for 3D cell segmentation and tracking.


## Additional informations

### Tip: Passing RGB images to TrackMate for cellpose

On the cellpose webiste you can find a collection of test images to test with cellpose. They will work with the TrackMate integration as well, but they are RGB images. TrackMate does not support RGB images. So we give here a short optional procedure on how to feed RGB images to TrackMate and have them still segmented by cellpose as expected. Again, if you don't have RGB images as input, you can skip this section.

cellpose can and does work with RGB images. They are single-channel but encode red, green and blue components of each pixel in one value, effectively behaving as a 3-channels 8-bit image. However, TrackMate cannot deal with RGB images. If you launch TrackMate with an RGB image you will receive an error message. The workaround is to convert them to a proper 3-channels 8-bit image before running TrackMate. cellpose will be able to run with them anyway. Here is how to do it. 

- With the RGB image opened, go to the {% include bc path='Image|Type' %} menu and select `RGB Stack`. This will convert the 1-channel RGB image in a 3-channels 8-bit image. 

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-01.png" width='400' %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-02.png" width='400' %}

- Most likely Fiji will display only one of the 3 channels in grayscale. To overlay again the 3 channels in a composite image, first display the **Channels tool** by selecting the {% include bc path='Image|Color|Channels Tool…' %} menu item.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-03.png" align='center' width='400' %}

-  A new floating window title **Channels** appears. Click on the `More »` button to bring an additional menu, and select the `Make Composite` item. You image should be now properly displayed, but made of 3 independent components. This way you can run it through TrackMate and still have it properly segmented by its cellpose integration.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-04.png" %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-05.png" %}

### Installing cellpose

This step is completely independent of Fiji. If you have already a working cellpose installation, you can skip this section entirely. But we absolutely need a working cellpose. The installation of cellpose with GPU support requires some knowledge of Python and of Conda to manage Python packages. If you are unfamiliar with Conda and are keen on having GPU support we suggest you get in touch with someone that knows them well.

There are several ways to install cellpose. We give example of using Anaconda or via precompiled executables. Both ways (conda or executable files) will work with TrackMate. 
The executables do not support GPU but work out of the box and do not require a local Python installation. And there is no support for GPU on MacOS anyway.

#### cellpose precompiled executables

The cellpose authors provide two precompiled executables for MacOS and Windows available here:

- For Mac: [https://www.cellpose.org/mac](https://www.cellpose.org/mac)
- For Windows: [https://www.cellpose.org/windows](https://www.cellpose.org/windows)

##### Windows

Just download the executable file and save it in a convenient place. Test that it works by double-clicking it The cellpose UI should show up.
In the `Path to cellpose / Python executable` text field in the detector UI, you will just need to enter the path to this executable.

##### Mac

On Mac you need to make the fille executable by opening a terminal, browsing to the folder containing it and running:

```sh
chmod 777 cellpose_mac
```
or
```sh
chmod 777 cellpose_mac.dms
```
depending on what file you downloaded.

In a second step you need to run the cellpose GUI by double-clicking on the file to unblock it from Mac security system. When run it for the first time, this message will appear:
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-01.png"  width='300' align='center' %}

Click OK then go the settings of your Mac. In the Security and Privacy panel the cellpose executable should be mentioned. Click on `Open Anyway`.
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-02.png"  width='400' align='center' %}

Finally, click `Open` on one last confirmation panel:
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-03.png"  width='300' align='center' %}

Once you cellpose installed, run the GUI to confirm that it works and can segment images on your system. Again, in the `Path to cellpose / Python executable` text field in the TrackMate detector UI, you will just need to enter the path to this executable.

#### With conda, mamba environment managers

{% include notice icon="tech"
  content="This is the recommended way to install Python tools to be used with TrackMate." %}

Using mamba (a better conda) is the most common way to run scientific Python tools on your computer. Recommendations keep evolving and we try to update this page.
If you don't have mamba, follow these instructions to install it: https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html 

Go to the cellpose GitHub webpage and follow the [installation procedures](https://github.com/MouseLand/cellpose#local-installation).

If you chose Anaconda to install cellpose, and put it in a dedicated environment, you need to enter the path to the _python executable_ of this conda environment. For instance if made a conda environment named `cellpose` for cellpose, it will be something like this:

`C:\Users\tinevez\anaconda3\envs\cellpose\python.exe`

##### Install cellpose 3 on a Mac

For instance on Mac: (on the computer used in example below, conda is an alias to microsmamba)

```zsh
>> conda create --name cellpose-3 python=3.10
>> conda activate cellpose-3
>> pip install 'cellpose[gui]==3.1.1.2'
>> cellpose --version
cellpose version: 	3.1.1.2 
platform:       	darwin 
python version: 	3.10.18 
torch version:  	2.7.1
```

This will install the version 3 of cellpose. As mid 2025, GPU-acceleration is used on this OS, as you can attest in the log when running cellpose:
```
2025-07-11 11:13:53,625 [INFO] ** TORCH MPS version installed and working. **
2025-07-11 11:13:53,625 [INFO] >>>> using GPU (MPS)
```

#### BIOP Conda installation for GPU support on Windows

The excellent people of the BIOP facility mentioned above also prepared a Conda spec list and recommendations for libraries dependencies to robustly achieve GPU support with cellpose. We give a procedure here, but all credits should go to them. It supports an older version of cellpose but works really well. Also the procedure describes one and one only way of getting GPU support with Python, that might not stand any deviation from it. Such is Python.

For this procedure to apply, you need to have Windows 10 or 11 as an OS, to have Python installed on your system using [Anaconda](https://www.anaconda.com/) and a NVIDIA GPU card. Ideally you would not have installed the Cuda library yet.

Go to the [BIOP GitHub page](https://github.com/BIOP/ijl-utilities-wrappers/blob/-/README.md#-conda-cellpose-gpu-) and fetch the YAML file corresponding to cellpose v0.6. Save it somwhere convenient.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-biop-yaml-page.png"  align='center' class='box' %}

Here is a [direct link to the file](https://raw.githubusercontent.com/BIOP/ijl-utilities-wrappers/master/resources/cellpose06_biop_gpu_113-821.yml) and its transcript:

```yaml
name: cellpose_biop_gpu
dependencies:
  - python>=3.8
  - pip
  - cudnn==8.2.1
  - cudatoolkit=11.3
  - pytorch::pytorch 
  - pip:
    - cellpose==0.6.5
    - jupyterlab
    - scikit-image
```
It specifies the versions of dependencies and constraints them, and they are chosen to work together.

Open an anaconda terminal and cd to the folder containing the YAML file. Create a new Conda environment from this file using:
```shell
 conda env create -f cellpose06_biop_gpu_113-821.yml
```
Now we need to install the CUDA Toolkit, with the right version. In our case it is the version 11.3. You can download it here for Windows 10 and Windows 11:

https://developer.nvidia.com/cuda-11.3.0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10

It will work with Windows 11 even if it is not stated on the webpage. After installation, your environment variable should look like this: 

{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-04.png" align='center' %}

Let's now confirm that cellpose works with GPU support. In the anaconda prompt type

```shell
(base) PS C:\Users\tinevez> conda activate cellpose_biop_gpu
(cellpose_biop_gpu) PS C:\Users\tinevez> python -m cellpose
```

The cellpose user interface should show up. Load an image, configure cellpose and click the `run segmentation` button on the GUI. In the anaconda shell, the log should confirm that the GPU was used:

```shell
2022-01-15 16:52:26,471 [INFO] WRITING LOG OUTPUT TO C:\Users\tinevez\.cellpose\run.log
2022-01-15 16:52:27,180 [INFO] ** TORCH CUDA version installed and working. **
C:/Users/tinevez/Desktop/R2_multiC-1.tif
1 (1024, 1024, 3)
removed all cells
removed all cells
cyto
2022-01-15 16:55:35,056 [INFO] ** TORCH CUDA version installed and working. **
2022-01-15 16:55:35,056 [INFO] >>>> using GPU
using model cyto
2022-01-15 16:55:35,178 [INFO] ~~~ FINDING MASKS ~~~
2022-01-15 16:55:43,181 [INFO] >>>> TOTAL TIME 8.00 sec
262 cells found with cellpose net in 8.152 sec
plane 0 outlines processed
```

If you have the `** TORCH CUDA version installed and working. **` and `[INFO] >>>> using GPU` then congratulations! You have now cellpose with GPU acceleration.

Now coming back to TrackMate, if you chose this path to install cellpose, you need to enter the path to the _python executable_ of this conda environment. In my case it is:

`C:\Users\tinevez\anaconda3\envs\cellpose_biop_gpu\python.exe`



_____

*Jean-Yves Tinevez - Jan 2022*
