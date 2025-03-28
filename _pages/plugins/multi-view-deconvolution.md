---
title: Multi-View Deconvolution
categories: [Uncategorized]

name: "Multi-view deconvolution plugin"
initial-release-date: "February 2013"
website: "http://fly.mpi-cbg.de/~preibisch"
team-founders: ['@fernandoamat', Eugene Myers, '@tomancak']
artifact: sc.fiji:SPIM_Registration
---

## Citation

Please note that the SPIM registration plugin available through Fiji, is based on a publication. If you use it successfully for your research please be so kind to cite our work:

{% include citation doi='10.1038/nmeth.2929' %}

## Overview of the multi-view deconvolution plugin

The multi-view deconvolution plugin is an image fusion plugin that computes one single image from several three-dimensional (3d) acquisitions (views) of the same specimen, taken in different orientations. The deconvolution tries to estimate the most probable image that best explains all views, given the individual point spread function (PSF) of each view. It can be computed for single timepoints or an entire timeseries.

#### Prerequisites I - Registration

Prerequisite for the fusion is an aligned dataset, an overview of the complete registration process can be found [here](/plugins/spim-registration), we suggest using the [Bead-based registration](/plugins/spim-bead-registration) as it provides a simple pipeline.

#### Prerequisites II - PSF's

The multi-view deconvolution additionally requires estimates of the PSF for each view. They can be directly and automatically measured from the data itself if fluorescent beads were added to the volume around the sample and the [Bead-based registration](/plugins/spim-bead-registration) was used to register the views.

Alternatively, an estimate or a simulated PSF can be provided as a 3d image. This is especially helpful in case the registration was achieved in any another way, for example using the [Segmentation-based registration](Segmentation-based_registration) or by an external program.

#### Prerequisites III - Cropping Area

It is highly recommended that before starting the multi-view deconvolution, to use the [Multi-view fusion](/plugins/multi-view-fusion) in order to determine the right bounding box for the image to be deconvolved.

{% include notice icon='warning' content='Do not set the bounding box too close to the imaged sample as it might result in artifacts. A distance of around 30-50 pixels between sample and the bounding box is suggested for the multi-view deconvolution.' %}

## How to use the plugin

{% include img align='right' src='spim-multiview-dialog1' width=350 caption='Shows the first dialog that queries the location of the multi-view files' %}

The multi-view deconvolution consists like the multi-view fusion of two consecutive dialogs. The first dialog queries the information necessary to analyze the dataset, i.e. locate the image files, the registration information and the location of the corresponding beads if applicable. Please note that all the parameters will be transferred from the [Multi-view fusion](/plugins/multi-view-fusion) dialog that you used before to set the bounding box (cropping area).

We omit a detailed explanation of the parameters here as it is identical to the explanation provided [Multi-view fusion dialog](/plugins/multi-view-fusion#how-to-use-the-plugin).

After providing the data the plugin will check which kind of registrations are available (\*.registration and \*.registration\_.to{tt}). Typically, the individual registration is available, and maybe also several time-series registrations to various reference timepoints. If no registration files could be found, the plugin will quit.

{% include clear style='right' %}{% include img align='right' src='mv-deconvolution' width=350 caption='Shows the second dialog that queries detailed parameters' %}

In the second dialog, you have to define the detailed instruction of how to run the multi-view deconvolution.

The available options are:

-   **Registration for channel 0:** You can choose which registration is used for this channel. You can typically choose between the individual registration of this timepoint or any registration to a reference timepoint.

-   **Crop output image offset x/y/z:** Defines the offset of the cropping area (bounding box) in the x/y/z-dimension of the output image relative to the uncropped image. A value of 0 refers to the top-front-left corner of the bounding box surrounding all views.

-   **Crop output image size x/y/z:** Defines the size of the cropping area (bounding box) in the x/y/z-dimension of the output image relative to the uncropped image. A value of 0 means no cropping.

{% include notice icon='info' content='The values defining the bounding box are identical to those provided in the multi-view fusion!' %}

-   **Type of iteration:** There are several iteration schemes that have been developed and can be used. They differ from each other by convergence time and image quality, which is of course a trade-off:

    -   *Independent (slow, very precise)* Is an ad-hoc optimization, yields reasonable results in case of very high signal-to-noise levels. In this case it is very fast.
    -   *Efficient Bayesian - Optimization I (fast, precise)* Is an optimization of the Efficient Bayesian multi-view deconvolution which approximates the conditional probabilities - the default choice.
    -   *Efficient Bayesian (less fast, more precise)* Incorporates conditional probabilities between the views into account without making any further assumptions.
    -   *Independent (slow, very precise)* assumes the individual views to be independent. This scheme converges slowest, but is least susceptible to noise and distortions (relevant at low signal-noise-ratios, imprecise alignments and inaccurate estimations of the PSFs)

-   **Number of iterations:** Typical multi-view deconvolution scenarios comprising around 4-8 views need 10-15 iterations when using *Efficient Bayesian - Optimization I (fast, precise)* as iteration scheme. The behavior relative to another number of views and different optimization schemes can be found in Supplementary Figure 4 (to be linked).

{% include notice icon='info' content='In order to determine the correct number of iterations for your dataset we suggest to use the Debug Mode (see below) on a partial volume.' %}

-   **Use Tikhonov Regularization/Tikhonov Parameter:** The regularization can be (de)activated. The behavior of the Tikhonov Parameter is shown in Supplementary Figures 5 and 6 (to be linked).

-   **ImgLib Container:** Defines which container is used to hold the image data in memory. The ArrayContainer is usually the right choice as it provides highest performance. The PlanarContainer and CellContainer might(!) help in case it runs out of memory, but they save only a few percent.

-   **Compute:** Define if the multi-view deconvolution should be computed for the entire image at once or in blocks. The result will be 100% identical! Computing in blocks saves a significant amount of RAM at the cost of higher computation time. If you run out of memory, try computing it in small blocks. If you select to choose a manually defined block size, a subsequent dialog will query the dimensions.

{% include notice icon='info' content='For computation on the CPU, specific block sizes are not important (it is not a traditional power-of-2 scheme). However, on the GPU it is highly recommended to use only power-of-two values (256, 512, etc.), or maximally a sum of power-of-two values (384, 768, etc.)' %}

-   **Compute on:** The multi-view deconvolution can be computed on the CPU or the GPU via JNA and CUDA. The CPU computation is built in Fiji, the CUDA code requires to load a native library (\*.dll, \*.so) that needs to be copied into the Fiji directory before starting Fiji. If you chose to compute the entire image at once on the GPU, a subsequent dialog will query which CUDA device to use. If you chose blocks on CUDA, you can choose in a subsequent dialog which GPU's will be used. If you have more than one CUDA device, use them both. It is usually not faster to let the CPU's compute blocks as well, but it might be.

{% include notice icon='info' content='Note that when CUDA crashes (e.g. because of out-of-memory), Java usually crashes with it.' %}

-   **PSF Estimation:** The PSFs can either be extracted from the corresponding beads that were detected during the bead-based registration or image(s) of the PSF can be provided. You can use a simulated PSF for your data or measured PSF's from another experiment (see PSF display for details how to store them). You can either use the same PSF for all views, it will be transformed according to the registrations of each view, or you specify a PSF for each view. In the latter case you can choose to transform the PSF's or you provide them already transformed. Typically, you will transform them. In case the PSFs are transformed, they to have the same calibration as the input views.

-   **PSF display:** In order to verify or store the extracted PSFs they can be displayed as maximum intensity projection along the rotation axis, as averaged three-dimensional volume or each PSF individually as three-dimensional volume. For the last two cases you can choose to display them in the same calibration as the input views or already transformed. <span style="color:#A52A2A">You can for example save them and provide them as input for another deconvolution experiment where no beads were included.</span>

{% include notice icon='info' content='All images are displayed as Virtual stacks. You might need to duplicate them in order to save them.' %}

-   **Debug Mode:** The debug mode will not only compute the final image but also show intermediate iterations in an ImageJ window. This allows to identify the correct number of iterations desired for your dataset. You will be queried in a subsequent dialog after every how many iterations you want to see current state of the iteration. It makes sense to not run the debug mode on the entire dataset but maybe a smaller part. Although the output might not be identical it gives a pretty good idea of how many iterations are required.

-   **Load images sequentially:** You usually want to activate this option as it saves a lot of memory and at the same time is just unnoticeably slower.

-   **Fused image output:** You can choose to display the result, save it the output directory as slices or create a different directory for each timepoint that is processed.

## Multi-Channel Multi-View Deconvolution

Multi-Channel deconvolution can be achieved by running the plugin on both channels individually. First, you have to make sure that both channels are aligned to each other. You have two choices:

**(1)** Run the [Bead-based registration](/plugins/spim-bead-registration) on just one channel and duplicate and rename the \*.dim, \*.beads.txt and \*.registration files for the other channels. Now when you run the deconvolution on the channel that contained the beads choose to export the PSF's in original calibration. For the other channels run the deconvolution with loaded PSFs. Alternatively use simulated PSFs. Simply merge the result of all channels.

**(2)** Run the [Multi-channel bead based registration](/plugins/spim-bead-registration#multichannel-registration), it requires that the same beads are visible in all channels and will register all to each other. Now run the deconvolution individually on both channels and extract the PSF's from the image or use simulated PSFs. Now there will be the problem that the images will most likely suffer an offset to each other, you might even need to define two different bounding boxes. The good news is that we know exactly what the offset - even with different bounding boxes - is. For that you need to note down one line in the output of the deconvolution (fusion is actually the same) of the channels:

```
Location of pixel (0,0,0) in global coordinates is: (367.39523, 452.0, 105.90103)
```

The difference between these coordinates of the different channels can for example be applied afterwards using {% include bc path="TransformJ | Translate" %}.

## How do I ... Problems, known issues and solutions

Some tips and tricks in the next few paragraphs require to change a static variable in the source code that changes the behavior of the plugin. This is done using the **script editor** and works as follows:

-   {% include bc path='File | New | Script' %}
-   {% include bc path='Language | Beanshell' %}
-   type the command, e.g.
    ```java
    System.gc();
    ```
-   click {% include button label="Run" %}

This just cleans up the RAM, which might be useful. Note that changes that are made (not in this case though) are only valid for the **currently running Fiji instance**.

### I want to change the size of the PSFs that are extracted

The plugin does some choice of what the area it is it uses to extract the PSF around the detected corresponding beads. You can change it in Beanshell by:

    fiji.plugin.Multi_View_Deconvolution.psfSize3d = new int[]{ 31, 31, 31 };

This changes the area to 31x31x31 pixel around a detected bead (in original calibration of the input views).

### I want to subtract background before running the deconvolution

You can subtract background before running the deconvolution (everything belong 0 is clipped). To do so type in the script editor:

    fiji.plugin.Multi_View_Deconvolution.subtractBackground = 100;

This for example subtracts a value of 100 from each pixel before starting, also before starting to extract the PSFs.

### How do I choose an efficient block size for the CPU

This is pretty tricky right now. You want to use as few blocks as possible given a certain size. If you choose a block size of let's say 512x512x512px you end up with an **effective block size** of maybe 475x489x432px, it depends on the size of the transformed PSF. It is computed as blocksize - kernelsize + 1. So you cannot really predict it before running a deconvolution once. It also different for each view (see [next section](/plugins/multi-view-deconvolution#how-do-i-make-all-psfs-the-same-size)). However, the **effective block size** relative to your bounding box size defines how many blocks you will require to cover your bounding box. How many blocks and **effective block size** is written to the standard out. In the future I plan to make this easier.

### How do I make all PSF's the same size

In the course of optimizing the block size you might get sick of the fact that it is different for each view. It might pose huge problems. I therefore added the option to make all transformed PSFs the same size before starting the deconvolution. This means that the **effective block size** will be the same for all views.

    fiji.plugin.Multi_View_Deconvolution.makeAllPSFSameSize = true;

Note that you might want to go to this detail of optimization if you have to deconvolve hundreds or thousands of timepoints.

### Intermediate (de)activation of the debug mode

Maybe you ran the deconvolution already for some time because the image is gigantic and computed in small blocks and you just want to check the current state at the next iteration. Or you maybe want to deactivate the the debug mode because you are afraid it runs out of memory with the next debug image. You can do so by executing

    mpicbg.spim.postprocessing.deconvolution2.debug = true; // or false

You can also change the interval

    mpicbg.spim.postprocessing.deconvolution2.debugInterval = 10;

Now, I will only debug every 10'th iteration.

### Start deconvolution with a previous result

By default, the deconvolution is initialized with a constant value for each pixel. You have, however, the chance to initialize with a different image. This way you can simply add more iterations to an existing result or even try to combine different parameters. You can do so by setting the input image

    mpicbg.spim.postprocessing.deconvolution2.initialImage = "/users/preibischs/data/psi_10.tif";

and re-running the deconvolution. Note that there is a minimal value for the deconvolved image by definition, here we use 0.0001. By default the image will be checked for anomalies. You can disable the check by executing

    mpicbg.spim.postprocessing.deconvolution2.checkNumbers = false;
