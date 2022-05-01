---
mediawiki: BigStitcher_Deconvolution
title: BigStitcher › Deconvolution
extensions: ["mathjax"]
nav-links: true
nav-title: Deconvolution
---

## Overview

In BigStitcher we offer deconvolution using a multi-view variant of the iterative Richardson-Lucy algorithm with various optimizations. Details about the previous version of the MultiView deconvolution as well as the corresponding publication with mathematical details can be found at [Multi-View\_Deconvolution](/plugins/multi-view-deconvolution).

**TODO: nice deconvolved image**

The deconvolution can be started by selecting the views you wish to deconvolve and selecting {% include bc path='Processing|(MultiView) Deconvolution'%} in the main menu in **MultiView mode**.

## Usage

After clicking **(MultiView) Deconvolution**, you will be presented with a dialog asking for the main parameters for deconvolution:

<img src="/media/plugins/bigstitcher/bigstitcher-deconvolution-main.png" width="600"/>

Since you are also producing a fused image for the deconvolution, some parameters are the same as in [BigStitcher\_Fuse](/plugins/bigstitcher/fuse):

-   the **BoundingBox** to use for the deconvolved output
-   by how much to **Downsample** the output
-   which view combinations to **Produce one image for**
-   how to display/save the **Fused Image**

The other options are (from top to bottom):

-   **Input image(s)**:
-   **Weight image(s)**:
-   **Initialize with**:
-   **Type of iteration**: We implemented various optimizations to the iterative deconvolution, which make some assumptions about the data that typically hold for images with high signal-to-noise-ratio (SNR). Using the optimizations speeds up the deconvolution, but might lead to artifacts if the SNR of your images is not high enough.
-   **Fast sequential iterations (OSEM)** and **OSEM acceleration**: TODO explain...
-   **Number of iterations**: For how many iterations to run the iterative deconvolution.
-   **Debug mode**: In debug mode, we will show intermediate results (deconvolved image every nth iteration) while the deconvolution is still running. You can specify how often to display in a separate dialog (see below).
-   **Use Tikhonov regularization** and **Tikhonov parameter**: By activating Tikhonov regularization, and setting the Tikhonov parameter to $$&gt;0$$ you can penalize large changes in the iterations. This way, the deconvolution is less prone to amplify noise but the results will generally be less sharp.
-   **Compute**: use this to specify **block size**. We can split the image into blocks and compute the deconvolution block-by-block. This allows you to do deconvolution on systems with less RAM, but will be slower, as we have to use overlapping blocks (smaller blocks will lead to more overlap). You can choose from a few presets or choose to **specify block size manually** in an extra dialog (see below).
-   **Compute on**: Whether to compute on **CPU (Java)** or **GPU (Nvidia CUDA via JNA)**. GPU acceleration can greatly speed up the deconvolution, but you have to manually compile the required libraries and have a CUDA-capable Nvidia GPU in you system (see below for details).
-   **Adjust blending & grouping parameters**: check this to show advanced options for view grouping and blending in a separate dialog (see below).

The dialog will also preview the memory requirements for the deconvolution (green preview text indicates that ImageJ has enough memory for the process, while red text indicates that the deconvolution will run out of memory and fail - use downsampling or smaller block sizes in that case).

### Initialization with existing image

If you chose to **Initialize from TIFF file** in the main dialog, you will be asked to provide the path to the file here, by dragging and dropping the file, selecting it by clicking **Browse...** or entering the path manually.

You can choose whether to do **Exact avg and max computation from input** or not. TODO: explain...

<img src="/media/plugins/bigstitcher/bigstitcher-deconvolution-fromfile.png" width="600"/>

Using this option, you can **continue a previous deconvolution** if you think that additional iterations will improve the results.

### Manual block size setup

<img src="/media/plugins/bigstitcher/bigstitcher-deconvolution-blocksize.png" width="600"/>

### Blending & grouping parameters

<img src="/media/plugins/bigstitcher/bigstitcher-deconvolution-blending.png" width="600"/>

### Debug mode

<img src="/media/plugins/bigstitcher/bigstitcher-deconvolution-debug.png" width="600"/>

### Deconvolution on GPU

## Usage of Previous version

As this usage guide is still work in progress, please refer to [Multi-View\_Deconvolution](/plugins/multi-view-deconvolution) for now.

Go back to the [main page](/plugins/bigstitcher#documentation)
