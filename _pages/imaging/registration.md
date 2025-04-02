---
title: Registration
section: Learn:Scientific Imaging
nav-links: true
---

## What is Registration?

{% include wikipedia title='Image registration' text='Image registration'%} is the process of transforming different sets of image data into one coordinate system. Image data may be multiple photographs, data from different sensors, times, depths, or viewpoints. It is used in computer vision, medical imaging, biological imaging and brain mapping, military automatic target recognition, and compiling and analyzing images and data from satellites. Registration is necessary in order to be able to compare or integrate the data obtained from these different measurements.

Essentially, image registration is used to align two or more images of the same scene. The transformation function, the method for modifying the spatial relationship between pixels, needs to be estimated/modeled in order to register the two images. The input image is the image that will be transformed, and the reference image is the one against which the input is registered. Geometric distortions causing differences in angle, orientation, shifting, and distance need to be taken into account. One of the most common methods to do image registration uses *points* that correspond to locations known in both the input and reference images. Tools exist in ImageJ that can automatically detect such *correspondence points* to then estimate the transformation function.

## Recommended ImageJ Plugins for Registration

Here we summarize some of the Registration plugins in ImageJ.

### [Feature Extraction](/plugins/feature-extraction)

A tool for identifying a set of corresponding points of interest in two images.

{% include img src="tem-42-33-f" width="500" caption="MOPS feature correspondences (example 1)" %}

* Interest points are detected using the Difference of Gaussian detector
* Uses the [Scale Invariant Feature Transform (SIFT)](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) and [Multi-Scale Oriented Patches (MOPS)](http://matthewalunbrown.com/papers/cvpr05.pdf) for local feature description
* Established matches are filtered using the [Random Sample Consensus (RANSAC)](https://en.wikipedia.org/wiki/Random_sample_consensus)
* The extracted sets of corresponding landmarks and the calculated transformations are used in [TrakEM2](/plugins/trakem2), [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices) and [BUnwarpJ](/plugins/bunwarpj) for image registration.

### [Linear Stack Alignment with SIFT](/plugins/linear-stack-alignment-with-sift)

A tool for aligning image stacks.

* A lightweight SIFT implementation for Java after the paper of David Lowe[^1].

Landmark Correspondences

### [Landmark Correspondences](/plugins/landmark-correspondences)

A simple tool for manual alignment of image planes.

{% include img src="plugins/transform-roi-mls" width="500px" %}

* Place corresponding points of interest on each of two images.
* Useful for images of heterogeneous resolution and/or modalities where correspondences cannot be automatically detected.

### [BUnwarpJ](/plugins/bunwarpj)

A tool for elastic and consistent image registration.

{% include img align="center" src="plugins/bunwarpj/scheme" width="500" %}

* Performs 2D image registration based on elastic deformations represented by B-splines
* Invertibility of the deformations is enforced through a consistency restriction
* Get started with the detailed [BUnwarpJ user manual](/plugins/bunwarpj#user-manual)

### [TrakEM2](/plugins/trakem2)

A tool for morphological data mining, three-dimensional modeling and image stitching, **registration**, editing and annotation.

{% include img src="trakem2-snap" width="500" %}

* Registers floating image tiles to each other using SIFT and global optimization algorithms.
* See the [TrakEM2 user manual section on registration](https://www.ini.uzh.ch/~acardona/trakem2_manual.html#registration)

### [Register Virtual Stack Slices](/plugins/register-virtual-stack-slices)

A tool that takes a sequence of image slices stored in a folder and delivers a list of registered image slices

{% include img src="rvs-scheme" width="500" %}

* The plugin can perform 6 types of image registration techniques: Translation, Rigid (translation + rotation), Similarity (translation + rotation + isotropic scaling), Affine, Elastic (via [BUnwarpJ](/plugins/bunwarpj) with cubic B-splines), and Moving least squares
* All models are aided by automatically extracted [SIFT features](/plugins/feature-extraction)

### [Fijiyama](/plugins/fijiyama)

A registration tool for 3D multimodal time-lapse imaging

{% include img src="reg-present-1" width="500" %}

* User-friendly, generic and versatile
* Automatic 3D registration (two algorithms available)
* Manual registration (using the [3D_Viewer](/plugins/3d-viewer))
* Movie tutorials and example datasets
* Settings automatically adjust based on your data
* Transformations: linear or non-linear
* Tested on specimens: human, vine trunk,
* Tested on modalities: MRI, X-ray CT, Photograph
* Limitations: should be avoided for big datasets (more than 15 time points or 1GB+).

## Other pages and tools for Registration in ImageJ

Filter by the Registration category on the [list of extensions](/list-of-extensions) to see other ImageJ pages and tools about image registration.

# References

{% include citation fn=1 id='plugins/linear-stack-alignment-with-sift' %}
