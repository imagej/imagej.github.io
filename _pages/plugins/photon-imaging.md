---
mediawiki: User:PhotonImaging
title: PhotonImaging
categories: [Uncategorized]
---

## Photon Imaging

------------------------------------------------------------------------

**About this project**

Authors: Lonneke Scheffer & Wout van Helvoirt

Version: 1.0

This plugin for ImageJ is able to process single photon event data, by locating the center point of each photon and create a combined greyscale image with all found photons per pixel mapped to the correct pixel value.

The project can be found on GitHub via https://github.com/penuts7644/PhotonImaging.

------------------------------------------------------------------------

**Getting set up**

This plugin requires at least Java 8 to function. Make sure that ImageJ is installed on your Windows/Mac/Linux device and that ImageJ uses Java 8. The source has been written in IntelliJ IDEA 2016 and the project uses Maven for package management and building.

------------------------------------------------------------------------

**How to install**

There are two ways of installing the plugin. For developers, who cloned this project and build a jar file via maven, you can install the plugin in ImageJ via {% include bc path="Plugins|Install PlugIn..." %}. Users can enable the update site 'PhotonImaging' via {% include bc path="Update...|Manage update sites" %}. This will prompt you to download the plugin the next time ImageJ searches for updates.

After you installed the plugin, restart ImageJ. When correctly installed, you'll now have {% include bc path="Plugins|Photon Image Processor" %} available. If you have enabled the update site, you will automatically receive updates for the plugin when their released.

------------------------------------------------------------------------

**How to use this plugin**

**Open TIFF Files**

This option can be used to open all TIFF files in a directory, and the directories below, as virtual stack. The opened virtual stack can be used as input for 'Process Photon Images'.

**Process Photon Images**

This option can be used to process a stack of single photon event data (images containing single photon events), and create one high resolution output image. This output image might optionally be improved by 'Threshold Photon Count' and/or 'Reconstruct Image'. There are 3 different methods to choose from to calculate the coordinates of the exact midpoints of the light blobs in the images. The available calculations modes are:

**Simple** uses the lightest pixels found as coordinates for the output image.

**Accurate** improves on 'Simple' by also checking the pixels surrounding the lightest pixel to calculate a more accurate midpoint.

**Sub-pixel resolution** uses the accurate method to calculate the midpoints but creates an output image of a higher resolution (height \* 2 and width \* 2). This requires more input images and bigger light blobs in those input images to work successfully.

**Threshold Photon Count**

This option can be used to filter noise from the output image created by 'Process Photon Images', and optionally prepare for 'Reconstruct Image'. All pixels below the threshold value are set to 0, and the remaining pixels are scaled to new values.

**Reconstruct Image**

This option can be used to reconstruct the output image created by 'Process Photon Images'. The input image is reconstructed using the algorithm of the article 'Imaging with a small number of photons', by P. A. Morris et al.

The original image is blurred and random changes are made. A check is performed to test whether the random changes have improved the image. This check includes testing for the log likelihood of the new image, and the sparsity of the new image. If there are very few possible modifications left that could improve the image, the method for changing random pixels is altered, so the modifications become less extreme and the image is fine tuned. Parameter explanation and usage:

**Dark count rate** per pixel of the camera used to record the data.

**Regularization factor** indicates how important the log likelihood and image sparsity are compared to one another. A higher regularization factor results in a greater dependency of image sparsity, and a lower regularization factor makes the log likelihood more important.

**Modification threshold** is the lower boundary for percentage of modifications that improve the image. In other words, how far the algorithm is proceeded. A higher percentage makes the algorithm quit earlier and makes the output image less defined. The lower the percentage is, the more the output image will eventually look like the input image.

**Multiply image colors** is the scaling value used to change the color of the input image, for instance when the input image is too dark to be clear.

**Blur radius** for the Gaussian blur filter. A bigger blur radius removes more detail from the original image, but also closes more gaps between pixels.
