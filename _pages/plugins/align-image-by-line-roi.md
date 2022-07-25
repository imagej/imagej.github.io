---
title: Align Image by line ROI
categories: [Registration]

name: "Align Image by line ROI"
initial-release-date: "2006-09-28"
artifact: sc.fiji:VIB_
source-url: https://github.com/fiji/VIB/blob/master/src/main/java/Align_Image.java
---

This plugin aligns an image to another image. You have to provide two landmarks per image by selecting a line.

## Example

Load the template (the image you want to align to) and specify the landmarks by a line selection:

{% include img src="shortnosed-sturgeon" %}

Then load the image you want to align with the template, and select a line (the order of the points is relevant: the first point will correlate with the first point of the other image's line selection):

{% include img src="blue-parrot-fish" %}

Now, start the plugin. If there was more than one other image with an active line selection, you would be asked which one is the template. Since there is only one, the plugin does not ask, but starts to work right away. The result looks like this:

{% include img src="aligned-blue-parrot-fish" %}
