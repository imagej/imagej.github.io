---
mediawiki: Segmentation
title: Segmentation
section: Learn:Scientific Imaging
nav-links: true
---

{% include notice icon="tip" content='See [this helpful workshop on Image Segmentation](/media/arganda-carreras-segmentation-bioimage-course-mdc-berlin-2016.pdf) for another great overview of Segmentation!' %}

# Introduction

Image segmentation is "the process of partitioning a digital image into multiple segments." ({% include wikipedia title='Image segmentation' text='Wikipedia'%})

![](/media/imaging/segmentation-overlay.jpg) ![](/media/imaging/segmentation-boundaries.jpg)

It is typically used to locate *objects* and *boundaries*.

More precisely, image segmentation is the process of *assigning a label* to every pixel in an image such that pixels with the same label share certain visual characteristics.

# Easy workflow

One plugin which is designed to be very powerful, yet easy to use for non-experts in image processing:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Plugin Name</strong></p>
      </td>
      <td>
        <p><strong>Short Description</strong></p>
      </td>
      <td>
        <p><strong>Highlights</strong></p>
      </td>
      <td>
        <p><strong>Plugin Snapshot</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="/plugins/tws">Trainable Weka Segmentation</a></p>
      </td>
      <td>
        <p>A tool that combines a collection of machine learning algorithms with a set of selected image features to produce pixel-based segmentations.</p>
      </td>
      <td>
        <ul>
          <li>Can be trained to learn from the user input and perform later the same task in unknown (test) data</li>
          <li>Makes use of all the powerful tools and classifiers from the latest version of <a href="http://www.cs.waikato.ac.nz/ml/weka/">Weka</a>
          </li>
          <li>Provides a labeled result based on the training of a chosen classifier</li>
          <li>Ease of use due to its graphical user interfaces</li>
        </ul>
      </td>
      <td>
        <p><img src="/media/tws-gui-after-training.png" width="500"></p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}

Give it a try—you might like it!

# Flexible workflow

One good workflow for segmentation in ImageJ is as follows:

1.  [Preprocess](#preprocessing) the given images
2.  Apply an [Auto Threshold](#adjusting-threshold)
3.  Create and manipulate a [mask](#creating-masks)
4.  [Create and transfer](#creating-selections) a selection from a mask to your original image
5.  [Analyze](#analysis) the resulting data

## Preprocessing

Preprocess the image using filters, to make later thresholding more effective. Which filter(s) to use is highly dependent on your data, but some commonly useful filters include:

-   [Deconvolution](/imaging/deconvolution)
-   [Subtract Background](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Subtract-Background...)
-   [Gaussian Blur](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Gaussian-Blur...)
-   [Find Edges](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Find-Edges)

## Adjusting Threshold

{% include img src="threshold-tree" width="300" caption="Tree ring sample image with a threshold applied for a B&amp;W image" %}

Ideally you want to use one of the auto-threshold methods, rather than manually tweaking, so that your result is reproducible later on the same data, and on multiple other datasets.

-   Open your image
-   Select {% include bc path='Image | Adjust | Threshold...'%}
-   Specify whether or not the background should be dark or light
-   Adjust the minimum and maximum sliders until you are satisfied with the saturation level of your image
    -   [More information](https://imagej.nih.gov/ij/docs/guide/146-28.html#sub:Threshold...%5BT%5D)

## Creating Masks

{% include img src="eroded-tree" width="300" caption="Over-saturated mask is eroded around the center tree ring" %}

-   Select {% include bc path='Edit | Selection | Create Mask'%}
-   Based on the image and set threshold, some portions of the image may be over/under saturated
    -   Select the portion of the image that needs to be adjusted
    -   Select [Dilate](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Dilate) to grow the included pixels to further saturate this portion of the image or [Erode](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Erode) to remove saturation
        -   [More information](https://imagej.nih.gov/ij/docs/guide/146-29.html#infobox:InvertedLutMask).
-   One quick way to split overlapping objects is the [Watershed](https://imagej.nih.gov/ij/docs/guide/146-29.html#sub:Watershed) command.

## Selections

{% include img src="selection-tree" width="300" caption="Selections on the mask" %}

### Creating Selections

-   Select {% include bc path='Edit | Selection | Create Selection'%} to select the objects within the mask
-   To deselect a portion of the image, select {% include key keys='Shift|left click' %}
    -   [More information](https://imagej.nih.gov/ij/docs/guide/146-27.html#sub:Create-Selection)

{% include img src="reverted-tree" width="300" caption="Selections on the reverted image" %}

### Transferring Selections

-   Before transferring the mask's selections, revert the image to its original form by selecting {% include key keys='Shift|E' %}
-   Select first the mask, then the original image, and select {% include key keys='Shift|E' %} to transfer the mask's selections
    -   [More information](https://imagej.nih.gov/ij/docs/guide/146-27.html#infobox:TransferSelections)

## Analysis

Do some numerical analysis on the selected data:

-   [Measure](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:Measure...%5Bm%5D) the entire selection directly.
    -   Control which measurements are done using [Set Measurements](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:Set-Measurements...).
-   Use [Analyze Particles](https://imagej.nih.gov/ij/docs/guide/146-30.html#sub:Analyze-Particles...) to extract desirable objects from your selection and report individual statistics on them.
-   Use the [ROI Manager](https://imagej.nih.gov/ij/docs/guide/146-30.html#fig:The-ROI-Manager) to **Add** the selection and then **Split** it (under the **More** button), then use **Multi Measure** (also under **More**) to report statistics on the objects.
-   [Write a macro](/scripting/macro) to automate this sort of analysis, loop over objects in the ROI manager, measure and manipulate them, etc.

# See also

-   The [Introduction to Image Segmentation using ImageJ/Fiji](/media/arganda-carreras-segmentation-bioimage-course-mdc-berlin-2016.pdf) workshop.
-   The [Segmentation with Fiji workshop slides](/presentations/fiji-segmentation/).
-   [List of extensions](/list-of-extensions), a list of ImageJ extensions, which you can filter by the Segmentation category.

 
