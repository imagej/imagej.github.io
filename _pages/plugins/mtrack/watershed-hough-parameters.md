---
mediawiki: Watershedding_and_Hough_transform_parameters
title: Watershedding and Hough transform parameters
---

In this method an intensity threshold value is used to create a binary image on which a distance transform is performed to create a distance transformed image. This distance transformed image is then segmented by watershedding. The user has one parameter to choose here which is the intensity threshold value.

-   Threshold value is an intensity value chosen to create a binary image, the minimum value is 0 and maximum value is 1 for the slider as the image intensity is always normalized between 0 and 1. An appropriate value has to be chosen to avoid over or under segmentation of the image.

The user can also display the result of the watershed operation by clicking on the display Bitimage and/or display Watershedimage option before performing the watershedding.

After the watershedding has been performed the user has to set up parameters for the Hough transform. The parameters are

-   Size of Hough space in theta : Hough transform transforms the Euclidean space to a parameter space, in our case the parameter space is that of line parameters which are defined in polar co-ordinates are theta and rho. If the size of pixel in Hough space is desired to be the same as that in Euclidean space this parameter should be set to 1. The accuracy of determining the line parameters does increase by making the size of pixel in Hough space bigger by setting the value of this parameter less than unity. However very small values such as 0.2 would not lead to an increase in the accuracy of determination of the line parameters, hence a value of 0.5 - 1 is recommended.

<!-- -->

-   Size of Hough space in rho: This parameter determines the size of Hough space in rho, ideally it's size is kept the same as that of the size in theta and also a value of 0.5 - 1 is recommended here.

<img src="/media/plugins/mtrack/advanced2.png" width="300"/>
