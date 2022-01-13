---
title: TrackMate-Cellpose
categories: [Segmentation,Tracking,Deep Learning]
logo: /media/icons/cellposelogo.png

---

# TrackMate-Cellpose.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-screenshot.png" %}

This page describes a detector module for [TrackMate](/plugins/trackmate/index) that relies on [Cellpose](https://cellpose.readthedocs.io/en/latest/) to segment cells in 2D. It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following). It also requires Cellpose to be installed on your system and working independently. This tutorial page gives installation details and advices at how to use the Cellpose integration in TrackMate.

Cellpose is a segmentation algorithm based on Deep-Learning techniques, written in Python 3 by Carsen Stringer and Marius Pachitariu. The TrackMate-Cellpose module, which is written in Java, is an example of integration via sub-processes. The integration technique is similar to that of the [TrackMate-Ilastik](trackmate-ilastik) module, except that the iastik authors offer a ready-to-use Java bridge that took care of launching ilastik from Fiji. For the TrackMate-Cellpose module, we built our own, based on ideas proposed by [Olivier Burri](/people/lacan), [Romain Guiet](/people/romainGuiet) and [Nicolas Chiaruttini](/people/NicoKiaru) from the [BIOP](https://www.epfl.ch/research/facilities/ptbiop/) team in the EPFL.

If you use the Cellpose TrackMate module for your research, please also cite the Cellpose paper:

_{% include citation doi='10.1038/s41592-020-01018-x' %}_

## Installation.

We need to subscribe to an extra update site in Fiji, and have a working installation of Cellpose on your system.

### TrackMate-Cellpose update site.

In Fiji, go to {% include bc path='Help|Update...' %}. Update and restart Fiji until it is up-to-date. Then go to the update menu once more, and click on the `Manage update sites` button, at the bottom-left of the updater window. A new window containing all the known update sites will appear. Click on the  **TrackMate-Cellpose** check box and restart Fiji one more time. 

### Install Cellpose on your system.

This step is completely independent of Fiji. If you have already a working Cellpose installation, you can skip this section entirely. But we absolutely need a working Cellpose. The installation of Cellpose with GPU support requires some knowledge of Python and of Conda to manage Python packages. If you are unfamiliar with Conda and are keen on having GPU support we suggest you get in touch with someone that knows them well.

#### Cellpose installation links.

You can install Cellpose using Anaconda or via precompiled executables. Both ways (conda or executable files) will work with TrackMate. 
The executables do not support GPU but work out of the box and do not require a local Python installation. And there is no support for GPU on MacOS anyway.

##### With Anaconda.

Go to the Cellpose GitHub webpage and follow the [installation procedures](https://github.com/MouseLand/cellpose#local-installation).

##### MacOS and Windows precompiled executables.

The authors also provide two precompiled executables for MacOS and Windows available here:
- For Mac: [https://www.cellpose.org/mac](https://www.cellpose.org/mac)
- For Windows: [https://www.cellpose.org/windows](https://www.cellpose.org/windows)

On Mac you need to make the fille executable by opening a terminal, browsing to the folder containing it and running:
```sh
chmod 777 cellpose_mac
```
or
```sh
chmod 777 cellpose_mac.dms
```
depending on what file you downloaded.

In a second step you need to run the Cellpose GUI by double-clicking on the file to unblock it from Mac security system. When run it for the first time, this message will appear:
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-01.png"  width='300' align='center' %}

Click OK then go the settings of your Mac. In the Security and Privacy panel the Cellpose executable should be mentioned. Click on `Open Anyway`.
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-02.png"  width='400' align='center' %}

Finally, click `Open` on one last confirmation panel:
{% include img src="/media/plugins/trackmate/trackmate-cellpose-installation-03.png"  width='300' align='center' %}

Once you Cellpose installed, run the GUI to confirm that it works and can segment images on your system.

#### BIOP Conda installation for GPU support on Windows.

The excellent people of the BIOP facility mentioned above also prepared a Conda spec list and recommendations for libraries dependencies to robustly achieve GPU support with Cellpose. We give a procedure here, but all credits should go to them. It supports an older version of Cellpose but works really well. Also the procedure describes one and one only way of getting GPU support with Python, that might not stand any deviation from it. Such is Python.

For this procedure to apply, you need to have Windows 10 or 11 as an OS, to have Python installed on your system using [Anaconda](https://www.anaconda.com/) and a NVIDIA GPU card. Ideally you would not have installed the Cuda library yet.

Go to the [BIOP GitHub page](https://github.com/BIOP/ijl-utilities-wrappers/blob/master/README.md#-conda-cellpose-gpu-) and fetch the YAML file corresponding to Cellpose v0.6. Save it somwhere convenient.

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
It specifies the versions of dependencies and constraints them, but they work.

Open an anaconda terminal and create a new Conda environment from this file.
TODO TODO

## Usage.

### Tip: Passing RGB images to TrackMate for Cellpose.

On the Cellpose webiste you can find a collection of test images to test with Cellpose. They will work with the TrackMate integration as well, but they are RGB images. TrackMate does not support RGB images. So we give here a short optional procedure on how to feed RGB images to TrackMate and have them still segmented by Cellpose as expected. Again, if you don't have RGB images as input, you can skip this section.

Cellpose can and does work with RGB images. They are single-channel but encode red, green and blue components of each pixel in one value, effectively behaving as a 3-channels 8-bit image. However, TrackMate cannot deal with RGB images. If you launch TrackMate with an RGB image you will receive an error message. The workaround is to convert them to a proper 3-channels 8-bit image before running TrackMate. Cellpose will be able to run with them anyway. Here is how to do it. 

- With the RGB image opened, go to the {% include bc path='Image|Type' %} menu and select `RGB Stack`. This will convert the 1-channel RGB image in a 3-channels 8-bit image. 

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-01.png" %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-02.png" %}

- Most likely Fiji will display only one of the 3 channels in grayscale. To overlay again the 3 channels in a composite image, first display the **Channels tool** by selecting the {% include bc path='Image|Color|Channels Tool…' %} menu item.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-03.png" align='center' %}

-  A new floating window title **Channels** appears. Click on the `More »` button to bring an additional menu, and select the `Make Composite` item. You image should be now properly displayed, but made of 3 independent components. This way you can run it through TrackMate and still have it properly segmented by its Cellpose integration.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-04.png" %}
{% include img src="/media/plugins/trackmate/trackmate-cellpose-convert-rgb-05.png" %}

### Tracking cells stained for cytoplam with Cellpose.

One of the central  advantage of Cellpose is its ability to give robuset segmentation results for cells stained for cytoplasm. We will use such a movie in this tutorial. You can download the example movie here TODO TODO


{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-01" align='center' width='400' %}

These are breast cancer cells moving collectively. We are tracking them to analyze how their migration parameters change in various conditions.

The movie comes from RGB images that have already been split in 3 separated components. The blue channel is empty. The red channel display the cell nuclei. The cells are stained for cytoplams in the green channel, with a lot of variability from one cell to another. The texture and sometimes the intensity hints the cell border. This is an image that would be considered very hard to segment with classical techniques. 

Open Fiji and load the image. Then launch TrackMate in {% include bc path='Plugins|Tracking|TrackMate' %}.
In the second panel, select the **Cellpose detector**:

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-02" align='center' width='400' %}

then click the `Next` button. You should see the configuration panel for Cellpose. There are several parameters to specify, both specifying where is Cellpose and how to run it.

{% include img src="/media/plugins/trackmate/trackmate-cellpose-tutorial-03" align='center' width='400' %}

#### Cellpose parameters in the TrackMate UI.

We document these parameters from top to bottom in the GUI.

##### `Path to Cellpose / Python executable`

We must specify where is the Cellpose executable, as it was installed outside of Fiji. Because there are several ways of installing Cellpose (with Conda or using the precompiled executables), we have to accommodate several cases we document here.

##### If you installed the precompiled executables.
Simply browse or enter the path to the executable itself. For instance on a Mac it could be `/Users/tinevez/Applications/cellpose_mac`.
On a Mac, do not forget to change the file permission to make the file executable, as [documented above](#macos-and-windows-precompiled-executables)

##### If you installed Cellpose with Anaconda.
In that case you need to specify the path to the**_Python executable** of the conda environment you created for Cellpose. For instance if on a Mac you created a conda environment named `cellpose` and installed Cellpose in it, the path to enter is:

```
/opt/anaconda3/envs/cellpose/bin/python
```

On Windows, following for instance the BIOP installation procedure mentioned [above](#biop-conda-installation-for-gpu-support-on-windows), the path should be something in the lines of: TODO TODO

##### `Pretrained model`
Right now we only support three pretrained models of Cellpose:
- the `cyto` model ("Cytoplasm"), to segment cells stained for their cytoplasm;
- the `nuclei` model ("Nuclei") to segment cell nuclei;
- the `cyto2` model ("Cytoplasm 2.0"), which is augmented from the `cyto` model with user-submitted images.
There is also the possibility to specify a custom model you would have trained or downloaded, and that is documented below.









