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

## Inputs
* Input image $I$
* A list of sigma values $\sigma_1,...,\sigma_N$, where $N$ is the number of sigma values
* The information if the input image should be processed plane by plane (2d) or as an volumetric image (3d)
## Notations
* Let $w_x$ and $w_y$ denote the size of the pixels in $x$ and $y$, usually we use $w_x = w_y = 1$. For volumetric images, $w_x$, $w_y$, $w_z$ denote the size of the voxels. For anisotropic $z$ sampling $w_z \neq 1$ is used.
* Each sigma value in the list is used to blur the input images with an according Gaussian blur filter. This produces $N$ differently blurred versions of the input image which we will denote by $G_i$:
  $$G_i := \mathrm{gauss}_{\sigma_i} I \quad \mathrm{for} \quad i=1,...,N$$
* Additional we define $G_0 := I$ to be the non blurred input image.
* We donate the first order partial derivatives of these images by $\partial_x G_i$ and $\partial_y G_i$.
  They are calculated by convolution of images with a central differences kernel:
  $$\partial_x G_i = {1 \over w_x} [-0.5 \ 0 \  0.5] \ast G_i$$
  We also use the partial derivative in $z$ for volumetric images: $\partial_z G_i$
* Similarely we denote the second oder partial by $\partial^2_x G_i$
  They are calculated by convolving the image with a kernel $[1 \ -2 \ 1]$:
  $$\partial^2_x G_i = {1 \over w_x^2}[1 \ -2 \ 1] \ast G_i$$
* The mixed second order derivative are denoted $\partial_x \partial_y G_i$ and they are calculated by two consequetive convolutions of the input image, with a kernel $[-0.5 \ 0 \ 0.5]$
  $$\partial_x \partial_y G_i := {1 \over w_y}[-0.5 \ 0 \ 0.5]_y \ast \left( {1 \over w_x}[-0.5 \ 0 \ 0.5]_x \ast G_i \right)$$

## Feature Filters

### Original Image
This filter is the simplest of them all, its output image $F^\mathrm{ID}$ is simple the input image:
$$ F^\mathrm{ID} := I$$

### Gaussian Blur
This filter outputs $N$ images which are the gaussian blurred versions of the input image:
$$ F^\mathrm{GAUSS}_i := G_i \quad \mathrm{for} \quad i = 1,...,N$$

### Difference of Gaussians
This filter outputs ${1 \over 2}N(N+1)$ images, that are the pixelwise subtraction of two gaussian blurred versions of the input image.
$$ F^\mathrm{DOG}_{i,j} := G_i - G_j \quad \mathrm{for} \quad i,j=1,...,N \quad \mathrm{with} \quad i<j$$
TODO: verify if this is correct

### Gaussian Gradient Magnitude
This filter produces $N+1$ output images. One output image for each $G_i$ with $i=0,...,N$. The output image is generated by calculating the magnitude of the gradient vector in each pixel:
$$ F^\mathrm{GGM}_i := \sqrt{(\partial_x G_i)^2 + (\partial_y G_i)^2 + (\partial_z G_i)^2}
\qquad \left(=|\ \mathrm{grad} \ G_i \ | \ \right)$$
(The square root, the sum and the squares in the equation above is calculated pixel wise.)

### Laplacian of Gaussian
This filter produces $N+1$ output images. One output image for each $G_i$ with $i=0,...,N$.
The output is the sum of the second order partial derivatives.
In 2d: $F^\mathrm{LOG}_i := \partial^2_x G_i + \partial^2_y G_i$
In 3d: $F^\mathrm{LOG}_i := \partial^2_x G_i + \partial^2_y G_i + \partial^2_z G_i$

### Hessian Eigenvalues
In 2d:

This filter produces $2(N+1)$ output images. Two output images for each $G_i$ with $i=0,...,N$.
In the next lines we will describe how the filter calculate the two outputs for a single image $G_i$. We omit the subscript $i$ to keep the equations readable.
The filter first calculates the second order partial derivatives which are (for a 2d image):
$$ H^{xx}:=\partial^2_x G \quad H^{yy}:=\partial^2_x G \quad H^{xy} := H^{yx} :=\partial _x \partial_y G$$
For each pixel $p$ in the image G, those 4 partial derivatives can be sample into 2x2 matrix.
$$ H_p := \begin{bmatrix}
H^{xx}(p) & H^{xy}(p) \\
H^{yx}(p) & H^{yy}(p)
\end{bmatrix} $$
For this matrix $H_p$ the filter calculates to two eigenvalues $\lambda_{1,p} \leq\lambda_{2,p}$. The eigenvalues are written pixel by pixel into the two output images:
$$F^\mathrm{HE}_1(p) := \lambda_{1,p} \quad F^\mathrm{HE}_2(p) := \lambda_{1,p}$$

In 3d:

The filter produces $3(N+1)$ output images. Three images for each $G_i$. There are 9 second order partial derivatives for each image $G_i$. Which are sampled into a symmetric 3x3 matrix, for each pixel. This matrices have 3 eigenvalues. Which are sorted by value, and written into the three output images.

### Structure Tensor Eigenvalues

In 2d:

This filter produces $4(N+1)$ output images. Four images for each $G_i$ with $i=0,...,N$.
Lets assume that $i$ is fixed for now. The following text will describe how the four images are calculated for $G_i$. Two of those four images are calculated with a parameter $\gamma = 1$ and two are calculated with $\gamma = 3$. This parameter $\gamma$ is called integration scale, it's use will be clear in a moment.
For the image $G$ (we again omit the subscript $i$) the filter calculates all following pixel wise products of first order derivatives:
$$
P^{XX} := \partial_x G \cdot \partial_x G \\
P^{XY} := \partial_x G \cdot \partial_y G \\
P^{YX} := \partial_y G \cdot \partial_x G \\
P^{YY} := \partial_y G \cdot \partial_y G
$$
Those images are blurred with a Gaussian blur of $\sigma=\gamma$:
$$
Q^{XX}_\gamma := \mathrm{gauss}_\gamma \ P^{XX} \\
Q^{XY}_\gamma := ...
$$
For each pixel $p$ in the image $G$ the four blurred images above can be sampled into a symmetric 2x2 matrix:
$$
Q_p = \begin{bmatrix}
Q^{XX}_\gamma(p) & Q^{XY}_\gamma(p) \\
Q^{YX}_\gamma(p) & Q^{YY}_\gamma(p)
\end{bmatrix}
$$
This matrix has two eigenvalues $\lambda_{1,p} \leq\lambda_{2,p}$. These two eigenvalues are written pixel by pixel into the two output images:
$$F^\mathrm{STEV}_1(p) := \lambda_{1,p} \quad F^\mathrm{STEV}_2(p) := \lambda_{1,p}$$

In 3d:
The filter in 3d produces $6(N+1)$ output images. It works similarly to the 2d version. There are just a few natural adaptations required. A 3d image has three first order partial derivatives. Which leads to $9=3\cdot 3$ pixel wise products. Those products are again blurred and assembled into a symmetric 3x3 matrix. That matrix has 3 eigenvalues. The eigenvalues are sorted and written into three output images.


### Min filter

This filter creates N output images. It produces one output image for each $\sigma_i$ in the list of sigma values.
For each pixel $p$ in the input image $I$ the filter iterates over a square neighborhood
to find the minimum value in this neighborhood. The minimum value is written to the output image $F^\mathrm{MIN}$ at the respective position of the pixel $p$. The width and height of the square neighborhood is $\lfloor 1 + 2\sigma_i \rfloor$ pixel.

In 3d the filter uses a cubic neighborhood of with width, height and depth of again $\lfloor 1 + 2\sigma_i \rfloor$ pixel.

### Max filter / Mean filter / Variance filter

Same as the min filter but calculates the maximum value / the mean value / the variance over the square / cubic neighborhood.
