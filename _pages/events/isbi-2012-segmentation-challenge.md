---
mediawiki: Segmentation_of_neuronal_structures_in_EM_stacks_challenge_-_ISBI_2012
title: Segmentation of neuronal structures in EM stacks challenge - ISBI 2012
---

{% include notice content="The ISBI 2012 challenge server has been decommissioned, but you can still [download the training and test data](https://downloads.imagej.net/ISBI-2012-challenge.zip)!" %}

<img src="/media/logos/isbi.jpg" title="fig:ISBI-logo.jpg" width="100" alt="ISBI-logo.jpg" />The [IEEE International Symposium on Biomedical Imaging (ISBI)](http://www.biomedicalimaging.org/) is the premier forum for the presentation of technological advances in theoretical and applied biomedical imaging and image computing. In the context of the [ISBI 2012](http://www.biomedicalimaging.org/2012/) conference which was held in Barcelona, Spain, from 2 to 5 May 2012, we organized a [challenge workshop](http://www.biomedicalimaging.org/2012/index.php/programme/isbi-challenges/13-challenges/49-contest-workshop-segmentation-of-neuronal) on **segmentation of neuronal structures in EM stacks**.

{% include thumbnail src='/media/events/challenge-isbi-2012-sample-image.png' title='Example of ssTEM image and its corresponding segmentation'%}In this **challenge**, a full stack of EM slices will be used to train {% include wikipedia title='Machine learning' text='machine learning'%} algorithms for the purpose of **automatic segmentation of neural structures**.

The images are representative of actual images in the real-world, containing some noise and small image alignment errors. None of these problems led to any difficulties in the manual labeling of each element in the image stack by an [expert human neuroanatomist](http://albert.rierol.net). The aim of the challenge is to compare and rank the different competing methods based on their pixel and object classification accuracy.

## Relevant dates

-   **Deadline for submitting results**: ~~February 1<sup>st</sup>~~ March 1<sup>st</sup>, 2012

<!-- -->

-   **Notification of the evaluation**: ~~February 21<sup>st</sup>~~ March 2<sup>nd</sup>, 2012

<!-- -->

-   **Deadline for submitting abstracts**: ~~March 1<sup>st</sup>~~ March 9<sup>th</sup>, 2012

<!-- -->

-   **Notification of acceptance/presentation type**: ~~March 15<sup>th</sup>~~ March 16<sup>th</sup>, 2012

The workshop competition is done but **the challenge remains open for new contributions**.

## How to participate

**Everybody** can participate in the challenge. The only requirement consists of filling up the registration form [here](http://brainiac2.mit.edu/isbi_challenge/user/register)(offline) to get a user name and password to download the data and upload the results.

This challenge was part of a [workshop](http://www.biomedicalimaging.org/2012/index.php/programme/opensourceworkshops) previous to the [IEEE International Symposium on Biomedical Imaging (ISBI) 2012](http://www.biomedicalimaging.org/2012/). After the publication of the evaluation ranking, teams were invited to submit an abstract. During the workshop, participants had the opportunity to present their methods and the results were discussed.

Each team received statistics regarding their results. **After the workshop, an overview article will be compiled by the organizers of the challenge, with up to three members per participating team as co-authors**.

If you have any doubt regarding the challenge, please, do not hesitate to contact the [organizers](/events/isbi-2012-segmentation-challenge#Organizers). There is also an **open discussion group** that you can join [here](https://groups.google.com/g/EM-segmentation-challenge-ISBI-2012).

## Training data

{% include thumbnail src='/media/events/challenge-isbi-2012-animation-input-labels.gif' title='Input training data and corresponding labels'%} The training data is a set of 30 sections from a serial section Transmission Electron Microscopy (ssTEM) data set of the Drosophila first instar larva ventral nerve cord (VNC). The microcube measures 2 x 2 x 1.5 microns approx., with a resolution of 4x4x50 nm/pixel.

The corresponding binary labels are provided in an in-out fashion, i.e. white for the pixels of segmented objects and black for the rest of pixels (which correspond mostly to membranes).

**To get the training data, please, register in the [challenge server](http://brainiac2.mit.edu/isbi_challenge/)(offline), log in and go to the "/downloads" section**.

This is the only data that participants are allowed to use to train their algorithms.

## Test data

The contesting segmentation methods will be ranked by their performance on a test dataset, also available in the [challenge server](http://brainiac2.mit.edu/isbi_challenge/)(offline), after registration. This test data is another volume from the same Drosophila first instar larva VNC as the training dataset.

## Results format

The **results** are expected to be uploaded in the [challenge server](http://brainiac2.mit.edu/isbi_challenge/)(offline) as a **32-bit TIFF 3D image, which values between 0 (100% membrane certainty) and 1 (100% non-membrane certainty).**

## Evaluation metrics

In order to evaluate and rank the performances of the participant methods, we will use 2D topology-based segmentation metrics, together with the pixel error (for the sake of metric comparison). Each metric will have an updated leader-board.

The metrics are:

-   [Minimum Splits and Mergers Warping error](/plugins/tws/minimum-splits-and-mergers-warping-error), a segmentation metric that penalizes topological disagreements, in this case, the object splits and mergers.
-   **Foreground-restricted Rand error**: defined as 1 - the maximal {% include wikipedia title='F1 score' text='F-score'%} of the foreground-restricted {% include wikipedia title='Rand index' text='Rand index'%}, a measure of similarity between two clusters or segmentations. On this version of the Rand index we exclude the zero component of the original labels (background pixels of the ground truth).
-   **Pixel error**: defined as 1 - the maximal {% include wikipedia title='F1 score' text='F-score'%} of pixel similarity, or squared Euclidean distance between the original and the result labels.

If you want to apply these metrics yourself to your own results, you can do it within Fiji using this [script](/tutorials/segmentation-evaluation-metrics).

We understand that segmentation evaluation is an ongoing and sensitive research topic, therefore we open the metrics to discussion. Please, do not hesitate to contact the [organizers](/events/isbi-2012-segmentation-challenge#Organizers) to discuss about the metric selection.

## Organizers

-   {% include person id='iarganda' %} (Howard Hughes Medical Institute, Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge, MA, USA)
-   [Sebastian Seung](http://hebb.mit.edu/people/seung/) (Howard Hughes Medical Institute, Department of Brain and Cognitive Sciences, Massachusetts Institute of Technology, Cambridge, MA, USA)
-   {% include person id='acardona' %} (Institute of Neuroinformatics, Uni/ETH Zurich, Switzerland)
-   {% include person id='dscho' %} (University of Wisconsin-Madison, WI, USA)

## References

Publications about the data:

{% include citation doi='10.1371/journal.pbio.1000502' %}

Publications about the metrics:

{% include citation doi='10.1109/CVPR.2010.5539950' %}
