---
title: DenoiSeg
categories: [Machine Learning, Denoising, Segmentation]
---

{% include thumbnail src='/media/plugins/denoiseg-teaser.png' title='Teaser of what DenoiSeg can compute on your data.'%}

DenoiSeg is a neural network based algorithm for instance segmentation. The interesting thing about DenoiSeg is, that - although primarily meant for segmentation - the algorithm also learns to denoise your images. The knowledge acquired by denoising the images, improves the segmentation results. DenoiSeg can solve hard segmentation tasks, just like other neural network bases algorithms. But it requires less training data, you only need to manually generate segmentation for about 2 to 10 images. (Other methods usually require much manual segmentations for at least 50 image.)

This website describes the DenoiSeg Fiji Plugin. Which makes it very easy to use DenoiSeg. All you need is your images, manually generated segmentations for a few of them, a computer with a NVIDIA graphics card and Fiji installed.

Segmenting your data with DenoiSeg requires 3 steps:

1.  Create manual segmentations for few of your images. (This might take around 8 h of manual work.)
2.  Train the neural network. The result is a trained neural network, which is called: model. (Training keeps your computer busy for around 12 h. This can be done over night, as you don't need do anything.)
3.  Prediction: Use the train model to segment as much images as you want. This step is much faster, just 1 second per image.

This Fiji plugin is part of CSBDeep, a collection of neural network algorithm in Fiji. For more information about our open source implementation , examples and images, click [here](https://csbdeep.bioimagecomputing.com/tools/denoiseg/).

# Publication: DenoiSeg - Joint Denoising and Segmentation

**Abstract**

Microscopy image analysis often requires the segmentation of objects, but training data for this task is typically scarce and hard to obtain. Here we propose DenoiSeg, a new method that can be trained end-to-end on only a few annotated ground truth segmentations. We achieve this by extending Noise2Void, a self-supervised denoising scheme that can be trained on noisy images alone, to also predict dense 3-class segmentations. The reason for the success of our method is that segmentation can profit from denoising, especially when performed jointly within the same network. The network becomes a denoising expert by seeing all available raw data, while co-learning to segment, even if only a few segmentation labels are available. This hypothesis is additionally fueled by our observation that the best segmentation results on high quality (very low noise) raw data are obtained when moderate amounts of synthetic noise are added. This renders the denoising-task non-trivial and unleashes the desired co-learning effect. We believe that DenoiSeg offers a viable way to circumvent the tremendous hunger for high quality training data and effectively enables few-shot learning of dense segmentations.

**[Full-text](https://arxiv.org/abs/2005.02987)**

# Installation

The DenoiSeg Fiji Plugin is part of the CSBDeep update site. Look [here](/update-sites/following), for detailed instructions on how to install an update site. Or just follow these steps:

1.  Start ImageJ / Fiji
2.  Open the updater via `Help > Update...`
3.  Click on `Manage update sites`
4.  Select the <b>`CSBDeep`</b> update site
5.  Click on `Apply changes`
6.  (optional) read [this page](/develop/tensorflow) for GPU support
7.  Restart ImageJ / Fiji

You should now have access to these plugins:

![Available DenoiSeg plugins](/media/plugins/denoiseg-plugins.png)

# Usage

## Training

Read [this page](/develop/tensorflow) for how to get GPU support. With out a GPU the training will take ages.

### Prepare your data

-   create two folders for training and two folders for validation, name them e.g. `X_train`, `Y_train`, `X_val`, and `Y_val`
-   Put noisy images into `X_train`, the more the better
-   Label some of them carefully - the more the better, but a handful labelings of high quality can be sufficient as well. Each labeling should be zero where there is background and the same integer number for each pixel of the same object.
-   Put the labels into `Y_train` - each labeling file needs to have the same name as the matching raw data in `X_train`
-   Do the same for `X_val` and `Y_val`. Aim for having about 10% validation data and 90% training data. If in doubt, use more data for training.

### Example data

If you just want to test the Fiji plugin you may use this [data](https://cloud.mpi-cbg.de/index.php/s/Mayv4JHOlR6ykBh). It was used to create the screenshots below.

Please note: You may not use this training data to segment your images. You need to prepare your own training data to get good results for your images.

### Train plugin

{% include thumbnail src='/media/plugins/denoiseg-train-parameters.png' title='N2V train parameters'%}

1.  Start ImageJ / Fiji
2.  Click on `Plugins > CSBDeep > DenoiSeg > DenoiSeg train` and adjust the following parameters:
    -   <b>`Folder containing training raw images`</b> Choose the folder we called `X_train` in the above data preparation section. It contains raw noisy data.
    -   <b>`Folder containing training labeling images`</b> Choose the folder we called `Y_train` in the above data preparation section. It contains some labelings matching the raw noisy data.
    -   <b>`Folder containing validation raw images`</b> Choose the folder we called `X_val` in the above data preparation section. It contains raw noisy data for judging the quality of the training progress.
    -   <b>`Folder containing validation labeling images`</b> Choose the folder we called `Y_val` in the above data preparation section. It contains some labelings matching the raw noisy validation data.
    -   <b>`Number of epochs`</b> How many epochs should be performed during training
    -   <b>`Number of steps per epoch`</b> How many steps per epoch should be performed
    -   <b>`Batch size per step`</b> How many tiles are batch processed by the network per training step
    -   <b>`Patch shape`</b> The length of X, Y (and Z) of one training patch (needs to be a multiple of 16)
    -   <b>`Neighborhood radius`</b> N2V specific parameter describing the distance of the neighbor pixel replacing the center pixel
3.  Click `Ok`
4.  Look below at the [What happens during and after training](#what-happens-during-and-after-training) section for what happens next

### Train & predict plugin (one-click solution)

{% include thumbnail src='/media/plugins/denoiseg-trainpredict-parameters.png' title='N2V train & predict parameters'%}

1.  Start ImageJ / Fiji
2.  Open a noisy image you want to denoise and segment directly after training
3.  Click on `Plugins > CSBDeep > DenoiSeg > DenoiSeg train & predict` and adjust the following parameters:
    -   <b>`Raw prediction input image`</b> Choose the image which should be denoised and segmented after training
    -   <b>`Axes of prediction input`</b> This parameter helps to figure out how your input data is organized. It's a string with one letter per dimension of the input image. For 2D images, this should be `XY`. If your data has another axis which should be batch processed, set this parameter to `XYB`
    -   Regarding the other parameters please have a look at the descriptions in [Train plugin](#train-plugin)
4.  Click `Ok`
5.  Look below at the [What happens during and after training](#what-happens-during-and-after-training) section for what happens next

## What happens during and after training

{% include thumbnail src='/media/plugins/denoiseg-train-progress.png' title='DenoiSeg training progress window'%} {% include thumbnail src='/media/plugins/denoiseg-train-preview.png' title='N2V training preview window'%} During training, you will see two windows:

-   The progress window keeps you updated of the steps the training process is going through. It also plots the current training and validation loss.
-   The preview window is generated from the first validation batch. It is split into five parts.
    1.  the original noisy data
    2.  the predicted denoised image
    3.  the predicted probability if each pixel being on the background
    4.  the predicted probability if each pixel being on the foreground
    5.  the predicted probability if each pixel being on the border

After training, two additional windows should appear. They represent two trained models. One is the model from the epoch with the lowest validation loss, the other one the model from the last epoch step. For DenoiSeg, using the model from the last epoch is almost always recommended. The windows will look similar to this:

![DenoiSeg model archive window](/media/plugins/denoiseg-model.png)

They are stored to a temporary location which you can see in the Overview section of the model window under `Saved to..`.

<b>Copy the model from there to another permanent destination on your disk if you want to keep this trained model.</b>

## Prediction

There are two ways to predict from a trained model. For both cases, the resulting image will consist of four channels:

1.  the denoised image
2.  the probability of each pixel being on the background
3.  the probability of each pixel being on the foreground
4.  the probability of each pixel being on the border

The user currently has to use these probabilities to compute the segmentation themself. In the future, further postprocessing steps will be available to automatically compute segmentations based on the output of the trained model.

You can <b>open the model directly</b>: {% include thumbnail src='/media/plugins/denoiseg-modelpredict-parameters.png' title='DenoiSeg prediction from model parameters'%}

1.  Start Fiji
2.  Open an image you want to denoise and segment and for which you have a pretrained model available as ZIP file
3.  Click `Import > bioimage.io.zip` and choose your trained model. The model will open in a window as depicted above
4.  Click `Predict` in the model window and adjust the following parameters:
    -   <b>`Input`</b> The image you want to denoise
    -   <b>`Axes of prediction input`</b> This parameter helps to figure out how your input data is organized. It's a string with one letter per dimension of the input image. For 2D images, this should be `XY`. If your data has another axis which should be batch processed, set this parameter to `XYB`

Alternatively, you can <b>use the DenoiSeg menu</b>: {% include thumbnail src='/media/plugins/denoiseg-predict-parameters.png' title='DenoiSeg prediction parameters'%}

1.  Start Fiji
2.  Open an image you want to denoise and for which you have a pretrained model available as ZIP file
3.  Click `Plugins > DenoiSeg > DenoiSeg predict` and adjust the parameters as described above, with this addition:
    -   <b>`Trained model file`</b> The ZIP file containing the pretrained model (it should end with `.bioimage.io.zip`)

# Exporting trained models from Python to ImageJ / Fiji

It's possible to train a DenoiSeg neural network using Python. The required code and instructions can be found [here](https://github.com/juglab/DenoiSeg). The model that has been trained in Python, can be used in Fiji as well:

1.  In Python, run this at the end of your training: `mode.export_TF()`.
2.  Locate the exported model file
3.  Proceed as described in [Prediction](#Prediction)

# Creating labelings for the training

There are many possibilities for how to create labelings. But since we get this question a lot, here is how we do it:

{% include thumbnail src='/media/plugins/updatesite-labkit.png' title='Update site Labkit'%} {% include thumbnail src='/media/labkit.png' title='Labkit'%} {% include thumbnail src='/media/plugins/3dobjectscounter.png' title='3D Objects counter options'%}

1.  Install the Labkit update site via `Help > Update...`, clicking on `Manage update sites`, and selecting `Labkit`
2.  Restart Fiji
3.  Open the image you want to label
4.  Click `Plugins > Segmentation > Labkit`
5.  Carefully label your data. Use e.g. the pencil tool to outline your labelings and the bucket tool to fill the outlines.
6.  Export the mask by clicking the meny item `Labeling > Show Labeling in ImageJ`
7.  Convert the exported mask (with zero for background and one for foreground into an indexed labelimage
    1.  Click `Analyze > 3D Objects Counter`
    2.  Make sure to deselect `Exclude objects on edges`
    3.  Save the displayed labeling to disk
