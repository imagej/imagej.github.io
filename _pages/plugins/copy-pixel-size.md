---
mediawiki: Copy_Pixel_Size
title: Copy Pixel Size
categories: [Image Annotation]
project: /update-sites/cookbook
---

{% capture source%}
{% include github org='fiji' repo='cookbook' branch='master' source='Copy_Pixel_Size.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Copy Pixel Size' author='J. Anthony Parker' source=source released='22 November 2001' status='stable' category='Image annotation' website='http://www.med.harvard.edu/JPNM/ij/plugins/CopyPixelSize.html' %}== Purpose ==

This plugin copies the pixel size from the calibration of one image or stack to a second image or stack. This allows one to copy the spatial calibration from one stack to another.

A second dialog allows to enter the scale factors.

## Installation

Available as part of the [Cookbook](/update-sites/cookbook) suite of plugins.
