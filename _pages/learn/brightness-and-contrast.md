---
title: Brightness and Contrast
categories: [Cookbook, tutorials]
---

{% include notice icon="info" content="This page refers to the version of [ImageJ2](/software/imagej2) currently in development. For more information on using [Fiji](/software/fiji) and [ImageJ 1.x](/software/imagej1), please reference the [Fiji tutorials](/plugin-index#tutorials) and [ImageJ 1.x documentation](/ij/docs/)." %}

This tool may be used to adjust the brightness and contrast of an active image.

## Usage

The Brightness and Contrast tool may be accessed through {% include bc path='Image | Adjust | Brightness/Contrast'%} or {% include key keys='Ctrl|Shift|C' %}.

{% include img src="brightness-contrast-window" width="266" height="177" align="right" %}

The upper and lower limits of the display range can be adjusted by modifying the minimum and maximum settings. Image brightness and image contrast can be modified by using the brightness and contrast sliders or by using the arrows on the right of the window to adjust the range.

Selecting 'OK' will make the specified changes to the display and close the Brightness/Contrast window. All channels in an image will be simultaneously updated automatically.

ImageJ may provide intelligent thresholding based on the image's histogram through {% include bc path='Image | Adjust | Auto-Contrast'%} or {% include key keys='Ctrl|Alt|Shift|L' %}. Repeated usage of this process will allow more pixel values to become saturated.

## Example

The below images show the effects of adjusting brightness and contrast settings.

**Before**

{% include img src="brightness-contrast-before" width="350" height="404" %}

**After**

{% include img src="brightness-contrast-after" width="350" height="404" %}
