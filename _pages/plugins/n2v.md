---
mediawiki: N2V
title: N2V
categories: [Uncategorized]
---

{% include thumbnail src='/media/plugins/n2v-teaser.png' title='Examples of N2V denoised images.'%}

Noise2Void (N2V) is a powerful, context aware and flexible algorithm for image denoising. It uses artificial neural networks to learn about the properties of your images and how to best denoise them. N2V outperforms traditional denoising techniques.

This page describes the N2V Fiji plugin. The N2V Fiji plugin provides a very simple way to use N2V in Fiji. All you need is a computer with a NVIDIA graphics cards, a Fiji installation and your noisy images.

The execution of N2V has two steps. The first step will train the artificial neural network to remove the noise in the kind of images that you have. This training step is relatively slow, it might take around 12 h to get the best results. But don't worry. Just let your computer run the training over night. You don't need to do anything. Training only needs to happen once, and you will see a preview during the ongoing training. The result of the training is a model. The second step is called prediction. The prediction step will use the trained model to denoise your images. The same model can be used for any number of similar images. It typically takes less than a second per image. So high quality denoising of thousand images is easily possible within one day.

See the paper for a detailed description of the algorithm.

This Fiji plugin is part of CSBDeep. A set of open source neural network algorithms in Fiji. For more information, examples and images, click [here](https://csbdeep.bioimagecomputing.com/tools/n2v/).

# Publication: Noise2Void - Learning Denoising from Single Noisy Images

**Abstract**

The field of image denoising is currently dominated by discriminative deep learning methods that are trained on pairs of noisy input and clean target images. Recently it has been shown that such methods can also be trained without clean targets. Instead, independent pairs of noisy images can be used, in an approach known as Noise2Noise (N2N). Here, we introduce Noise2Void (N2V), a training scheme that takes this idea one step further. It does not require noisy image pairs, nor clean target images. Consequently, N2V allows us to train directly on the body of data to be denoised and can therefore be applied when other methods cannot. Especially interesting is the application to biomedical image data, where the acquisition of training targets, clean or noisy, is frequently not possible. We compare the performance of N2V to approaches that have either clean target images and/or noisy image pairs available. Intuitively, N2V cannot be expected to outperform methods that have more information available during training. Still, we observe that the denoising performance of Noise2Void drops in moderation and compares favorably to training-free denoising methods.

**[Full-text](https://arxiv.org/abs/1811.10980)**

# Installation

1.  Start ImageJ / Fiji
2.  Open the updater via `Help > Update...`
3.  Click on `Manage update sites`
4.  Select the <b>`CSBDeep`</b> update site
5.  Click on `Apply changes`
6.  (optional) read [this page](/develop/tensorflow) for GPU support
7.  Restart ImageJ / Fiji

You should now have access to these plugins:

![Available N2V plugins](/media/plugins/n2v-plugins.png)

# Usage

## Training

Training without GPU support is possible, but will take ages. Please read the notes on [this page](/develop/tensorflow) for how to run the tools on the GPU.

### Training on a single image

{% include thumbnail src='/media/plugins/n2v-train-parameters.png' title='N2V train parameters'%}

1.  Start ImageJ / Fiji
2.  Open a noisy image of your choice (it should be sufficiently large)
3.  (optional) open another noisy image for validation (judging how well the training is performing)
4.  Click on `Plugins > CSBDeep > N2V > N2V train` and adjust the following parameters:
    -   <b>`Image used for training`</b> Choose the image which will be used for training
    -   <b>`Image used for validation`</b> Choose the image which will be used for training (you can also choose the same for both images, in this case 10% of the tiled image will be used for validation and 90% for training)
    -   <b>`Use 3D model instead of 2D`</b> Select this checkbox if you want to train on 3D data (this needs much more GPU memory)
    -   <b>`Number of epochs`</b> How many epochs should be performed during training
    -   <b>`Number of steps per epoch`</b> How many steps per epoch should be performed
    -   <b>`Batch size per step`</b> How many tiles are batch processed by the network per training step
    -   <b>`Patch shape`</b> The length of X, Y (and Z) of one training patch (needs to be a multiple of 16)
    -   <b>`Neighborhood radius`</b> n2V specific parameter describing the distance of the neighbor pixel replacing the center pixel
5.  Click `Ok`
6.  Look below at the [What happens during and after training](#what-happens-during-and-after-training) section for what happens next

### Training and prediction on single images (one-click solution)

{% include thumbnail src='/media/plugins/n2v-trainpredict-parameters.png' title='N2V train & predict parameters'%}

1.  Start ImageJ / Fiji
2.  Open a noisy image of your choice (it should be sufficiently large)
3.  Open another noisy image you want to denoise directly after training (this will also be used for validation)
4.  Click on `Plugins > CSBDeep > N2V > N2V train & predict` and adjust the following parameters:
    -   <b>`Image used for training`</b> Choose the image which will be used for training
    -   <b>`Image to denoise after training`</b> Choose the image which will be used for prediction
    -   <b>`Axes of prediction input`</b> This parameter helps to figure out how your input data is organized. It's a string with one letter per dimension of the input image. For 2D images, this should be `XY`. If your data has another axis which should be batch processed, set this parameter to `XYB`
    -   Regarding the other parameters please have a look at the descriptions in [Training on a single image](#training-on-a-single-image)
5.  Click `Ok`
6.  Look below at the [What happens during and after training](#what-happens-during-and-after-training) section for what happens next

### Training on multiple images

{% include thumbnail src='/media/plugins/n2v-trainfolder-parameters.png' title='N2V train on folder parameters'%}

1.  Start ImageJ / Fiji
2.  Click on `Plugins > CSBDeep > N2V > N2V train on folder` and adjust the following parameters:
    -   <b>`Folder containing images used for training`</b> Choose the folder containing images which should be used for training
    -   <b>`Folder containing images used for validation`</b> Choose the folder containing images which should be used for validation (can be same as training folder, in this case 10% of the generated tiles will be used for validation and 90% for training)
    -   Regarding the other parameters please have a look at the descriptions in [Training on a single image](#training-on-a-single-image)
3.  Click `Ok`
4.  Look below at the [What happens during and after training](#what-happens-during-and-after-training) section for what happens next

## What happens during and after training

{% include thumbnail src='/media/plugins/n2v-train-progress.png' title='N2V training progress window'%} {% include thumbnail src='/media/plugins/n2v-train-preview.png' title='N2V training preview window'%} During training, you will see two windows:

-   The progress window keeps you updated of the steps the training process is going through. It also plots the current training and validation loss.
-   The preview window is generated from the first validation batch. It is slit into two parts. The upper left part displays the original noisy data, the lower right part displays the prediction at the current state of the training.

After training, two additional windows should appear. They represent two trained models. One is the model from the epoch with the lowest validation loss, the other one the model from the last epoch step. For N2V, using the model from the last epoch is almost always recommended. The windows will look similar to this:

![N2V model archive window](/media/plugins/n2v-model.png)

They are stored to a temporary location which you can see in the Overview section of the model window under `Saved to..`.

<b>Copy the model from there to another permanent destination on your disk if you want to keep this trained model.</b>

## Prediction

There are two ways to predict from a trained model.

You can <b>open the model directly</b>: {% include thumbnail src='/media/plugins/n2v-modelpredict-parameters.png' title='N2V prediction from model parameters'%}

1.  Start Fiji
2.  Open an image you want to denoise and for which you have a pretrained model available as ZIP file
3.  Click `Import > bioimage.io.zip` and choose your trained model. The model will open in a window as depicted above
4.  Click `Predict` in the model window and adjust the following parameters:
    -   <b>`Input`</b> The image you want to denoise
    -   <b>`Axes of prediction input`</b> This parameter helps to figure out how your input data is organized. It's a string with one letter per dimension of the input image. For 2D images, this should be `XY`. If your data has another axis which should be batch processed, set this parameter to `XYB`

Alternatively, you can <b>use the N2V menu</b>: {% include thumbnail src='/media/plugins/n2v-predict-parameters.png' title='N2V prediction parameters'%}

1.  Start Fiji
2.  Open an image you want to denoise and for which you have a pretrained model available as ZIP file
3.  Click `Plugins > N2V > N2V predict` and adjust the parameters as described above, with this addition:
    -   <b>`Trained model file`</b> The ZIP file containing the pretrained model (it should end with `.bioimage.io.zip`)

# Exporting trained models from Python to ImageJ / Fiji

It's possible to train a Noise2Void neural network using Python. The required code and instructions can be found [here](https://github.com/juglab/n2v). The model that has been trained in Python, can be used in Fiji as well:

1.  In Python, run this at the end of you training: `model.export_TF()`
2.  Locate the exported model file
3.  Proceed as described in [Prediction](#Prediction)

# How to handle macros / scripts / models from the first early release of N2V for Fiji

Thank you for testing the first early release version! Here is what changed, if that does not help you getting already trained models or scripts running, please write a post in the forum!

## Update Site

You don't need the N2V update site any more, the CSBDeep update site is sufficient. Please remove the N2V update site.

## Macros / Scripts

-   the `predict` command was renamed to `N2V predict`
-   the `train` command was renamed to `N2V train`
-   the `train + predict` command was renamed to `N2V train + predict`
-   the `train on folder` command was renamed to `N2V train on folder`
-   there is a new mandatory prediction parameter called `axes` (see documentation above)
-   the training parameter `batchDimLength` is gone for good
-   the training parameter `patchDimLength` was renamed to `patchShape`
-   the training output `latestTrainedModelPath` changed to `latestTrainedModel` (it's a displayable model object now)
-   the training output `bestTrainedModelPath` changed to `bestTrainedModel` (it's a displayable model object now)

## Trained models

Models trained with the first N2V for Fiji version cannot be used with the newer commands for model prediction. Please upgrade them first by using the command `Plugins > CSBDeep > N2V > Upgrade old N2V model`. ! Note: When testing this, I had to unzip and zip the new model before it was usable. I'll try to fix this, but if you run into problems with the converted model, try unzipping and zipping it again.
