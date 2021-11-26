---
title: Labkit - Pixel Classification Algorithm Documentation
extensions: ["mathjax"]
---

# Pixel Classification Algorithm

(Under construction)

## Introduction

Random forest based pixel classification is an established algorithm for semantic
image segmentation. It is used, for example, in the image analysis tools: ilastik,
Trainable Weka Segmentation and QuPath.
Labkit's implementation of the algorithm is very similar to those tools but takes
a stronger emphasis on scalability.
The basic principle of the random forest based pixel classification algorithm is described in this section.

## Inputs

1. An image to calculate a segmentation of.
2. The labeling of that image, where a few representation pixels are marked as
   examples to a certain class.
3. A selection of filters and their parameters to be used for feature extraction.

Show example:

## Outputs

1. A segmentation of the image.
2. A probability map of the image.
3. A trained random forest classifier, that can be used to segment an arbitrary
   number of images.
   
Show example:

## Algorithm

The algorithm has three steps: The first step calculate a feature
vector for each pixel in the image. The second step trains a random forest.
This step uses the feature vector but also requires some user input. The user
needs to mark a few pixels in the image as they belong to a certain class - for
example: foreground / background. The final step of the algorithm uses the trained
random forest to generate a segmentation for the entire image.

First we build a feature stack.
The feature stack is build by applying a predefined list of filters image.
Each image produces an output image.
Those images are stacked to build a multi feature stack.
Than features stack can be seen as multi channel version of the input image.
For each pixel, we now get multiple intensity values - one per channel. These
different intensity values build the feature vector of an pixel.

The second step of the algorithm is the training of the random forest.
This step also takes needs additional input from the user. The user has marked
a few pixels in the image to belong to a certain class for example foreground
or background. This information together with the previously calculated feature
vectors are used to train a random forest. (cite paper)

The random forest is finally applied to all pixels in the image. By
looking at the feature vector of the pixel. The random forest predicts the
probability of the pixel to belong to a certain class. 
The probabilities are either written into a probabilty map. Or the class indicies
are written into an output image to build the segmentation.

# Filters for Feature Extraction

The pixel classification algorithm uses a set of filters to calculate pixel features.
Which filters to use and how to parameterize them can be selected by the user.
There are two settings that affect all filters.
The dimensionality 2d/3d and a list of sigma values.


### Original Image

This filter just copies the original image.

### Gaussian blur

For each sigma in the list, the image is blurred with a Gaussian of
corresponding standard derivation.

### Difference of Gaussians

For every two sigma values $$\sigma_1, \sigma_2$$ in the list of sigmas,
with $$\sigma_1 < \sigma_2$$ this filter calculates and image
$$F = gauss_{\sigma_1} I - gauss_{\sigma_2} I$$

### Gaussian gradient magnitude

This filter is applied to the original image, and to blurred version of the image.
It calculates the gradient vector in each pixel of the image and stores the magnitude
of this vector into the result.

### Laplacian of Gaussian

This filter first blurs the input image with a gaussian blur and applies
the Laplacian operator on the blurred image.
$$F = \delta_x^2 G_sigma + \delte_y^2 G_sigma$$

### Hessian eigenvalues

This filter first blurs the image, with a gaussian blur. It than calculates
the partial second order derivatives of the blurred image. In each pixel
it builds the hessian matrix:

$$ H = (G_{xx}, G_{xy}, G_{xy}, G_{yy}) $$
with
$$ G_\sigma = gauss_\sigma I $$

And calculates the eigenvalues $$\lambda_1$$, $$\lambda_2$$ of this matrix.

### Structure tensor eigenvalues (for each sigma):

### Min filter

This filter creates multiple outputs.
It produces one output image for each sigma in the list of sigma.
For each pixel in the input image the filter iterates of a square neighborhood
to find the minimum value in this neighborhood.
The minimum value is written to the output image.
The width and height of the square neighborhood is $$ floor(1 + 2\sigma) $$ pixel.

In 3d the filter uses a cubic neighborhood of with width, height and depth of again $$ floor(1 + 2\sigma) $$ pixel.

### Max filter

Same as the min filter but calculates the maximum value.

### Mean filter

Similar to the min filter but calculates the mean value it the square / cubic neighborhood.

### Variance filters

Similar to the min filter but calculates the variance value it the square / cubic neighborhood.
