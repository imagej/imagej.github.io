---
mediawiki: Shape_Smoothing
title: Shape Smoothing
categories: [Uncategorized]
---


{% capture author%}
Undral Erdenetsogt, {% include person id='thorstenwagner' %}
{% endcapture %}

{% capture maintainer%}
Undral Erdenetsogt (erdenetsogt@biomedical-imaging.de), {% include person id='thorstenwagner' %}
{% endcapture %}
{% include info-box software='Fiji' name='Shape Smoothing Plugin' author=author maintainer=maintainer filename=' [shape-smoothing.jar](https://github.com/thorstenwagner/ij-shape-smoothing/releases/latest)' source=' [Github](https://github.com/thorstenwagner/ij-shape-smoothing)' latest-version='v1.2 (06 October 2016)' status='maintaining' %}

# General Purpose

The plugin smoothens contours of objects in binary images. The Fourier transformation combined with filtering of Fourier descriptors (FDs) are applied to conduct the smoothing. The user can define the measure of contour smoothing by setting the amount of FDs – either relative or absolute. All FDs up to the selected threshold are scale-, rotation- and translation-invariant.

# Background

The plugin at first extracts the contours of all objects found in the input image. Object recognition and contour extraction are both performed by using [IJBlob](https://github.com/thorstenwagner/ij-blob). Then the contours are processed one at a time in the following way:

1.  Discrete Fourier transformation is applied to contour data (coordinates of contour points) to gain FDs
2.  FDs are filtered according to user input – only the ones, which are close to the zero frequency (from both sides), are retained. The other ones are cut off, meaning they are set to 0+0i.
3.  Filtered (or "kept") FDs are inverse Fourier transformed to obtain the points of the smoothed contour.

For implementing the Fourier transformations [JTransforms](https://github.com/wendykierp/JTransforms) was used.

Some theoretical background of FD-filtering: the result of step 1 is a series of FDs with the zero frequency (ZF) in its middle. ZF is essential for reconstruction spatial information of the contour. A frequency or a FD contains the more information the nearer it is to ZF (regardless of the side). Therefore in step 2 the FDs on the ends of the obtained series are set to 0+0i to achieve the smoothing.

# Parameters

{% include img src="shape-smoothing-gui" width="320" caption="Shape-Smoothing parameters" %}

At first users have to choose on how they want to define the smoothing: via relative or absolute number of FDs to be "kept".

**Relative proportion FDs (%):** The relativ number of FDs (relativ to the number of available FDs) will be used for smoothing the contours.

**Absolute number FDs:** The absolute number of FDs will be used for smoothing the contours.

**Draw only contours:** If selected, only the smoothed contours of objects will be draw (without filling them).

**Output Descriptors:** If selected, a table, containing all FDs, will be shown after processing. (Filtered FDs will all have the value 0+0i.)

**Black Background:** Select this option, if the background in the input image is black and the objects are white. (The plugin prefills this parameter according to a rudimentary background detection)

# Examples

<div>

-   {% include thumbnail src='/media/plugins/shape-smoothing-original-image.png' title='none\|300px\|Original image'%}
-   {% include thumbnail src='/media/plugins/shape-smoothing-smoothed-object.png' title='none\|300px\|Smoothed object (4% of FDs retained)'%}
-   {% include thumbnail src='/media/plugins/shape-smoothing-smoothed-contour.png' title='none\|300px\|Smoothed contour (2% of FDs retained)'%}

</div>

# Installation

You could simply use our update site [biomedgroup](http://sites.imagej.net/Biomedgroup) to install the plugin.

If you use ImageJ just copy the ij\_shape\_smoothing-1.0.1.jar file in your plugins folder and copy IJBlob and JTransforms jars into the plugins/jars folder.
