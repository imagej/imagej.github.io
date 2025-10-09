---
mediawiki: Ridge_Detection
name: "Ridge (Line) Detection Plugin"
title: Ridge Detection
categories: [Filtering]
extensions: ["mathjax"]
release-date: "v1.4.0 (20 Aug 2017)"
dev-status: "Unmaintained"
artifact: de.biomedical-imaging.imagej:ij_ridge_detect
doi: 10.5281/zenodo.845874
---

{% include warning/unmaintained %}

{% include notice icon='info' size='large' content='As this plugin is no longer maintained... you can check out [ImageJ Ops](/libs/imagej-ops) for Ridge Detection algorithms.' %}

## Purpose

This plugin implements **and extends** the ridge / line detection algorithm described in:

*Steger, C., 1998. An unbiased detector of curvilinear structures. IEEE Transactions on Pattern Analysis and Machine Intelligence, 20(2), pp.113–125.*

It works with stacks, is parallelized, has a preview mode and is able to resolve overlapping lines. It depends on the [apache-commons-lang 3](http://commons.apache.org/proper/commons-lang/) library. For ImageJ, please copy it into plugins/jars.

## Examples

![](/media/plugins/cnt-ridge-detection-original.png) ![](/media/plugins/cnt-ridge-detection-example.png)

This example shows the application of the plugin on images of carbon nanotubes (Sigma = 1.5, Lower Threshold = 1.3, Higher Threshold = 7).

# Parameter Selection

There are three parameters which **have to** be specified. These are the mandatory parameters. The optional parameters can be used to estimate the mandatory parameters <img src="/media/plugins/ridge-detection-parameters.png" title="Ridge_Detection_Parameters.png" width="200" alt="Ridge_Detection_Parameters.png" />

## Mandatory Parameters

**Sigma:** Determines the sigma for the derivatives. It depends on the line width.

**Lower Threshold:** The lower hysteresis threshold. Line points with a response less than this threshold are rejected.

**Upper Threshold:** The uppter hysteresis threshold. Line points with a response greater than this threshold are accepted. Points with a response less than this threshold but above the lower threshold are accepted **if** connected to an accepted point.

**Darkline:** (true/false) This parameter determines whether dark or bright lines are extracted.

## Optional parameters

The following optional parameters are used to estimate the mandatory parameters:

**Line width** ($$w$$): The line diameter in pixels. It estimates the mandatory parameter 'Sigma' by:

$$\sigma=\frac{w}{2\sqrt{3}}+0.5$$

**High contrast** ($$b_{upper}$$): Highest grayscale value of the line. It estimates the mandatory parameter 'Upper threshold' by:

$$T_{U}=\left\lfloor 0.17\cdot\frac{2\cdot b_{upper}\cdot\frac{w}{2}}{\sqrt{2\pi}\sigma^{3}}e^{-\frac{\left(\frac{w}{2}\right)^{2}}{2\sigma^{2}}}\right\rfloor $$

**Low contrast** ($$b_{low}$$): Lowest grayscale value of the line. It estimates the mandatory parameter 'Lower Threshold' by:

$$T_{L}=\left\lfloor 0.17\cdot\frac{2\cdot b_{low}\cdot\frac{w}{2}}{\sqrt{2\pi}\sigma^{3}}e^{-\frac{\left(\frac{w}{2}\right)^{2}}{2\sigma^{2}}}\right\rfloor $$

## Further options (true/false)

<img src="/media/plugins/ridgedetectionwidth.png" title="Output if &quot;Estimated width&quot; is selected" width="140" alt="Output if &quot;Estimated width&quot; is selected" /> **Correct position:** Correct the line position if it has different contrast on each side of it.

**Estimate width:** If this option is selected the width of the line is estimated.

**Show junction points:** If this option is selected the junctions points will be displayed.

**Show IDs:** The ID of each line will be shown.

**Verbose mode:** If this option is selected, status information will be printed to the log while running.

**Display results:** If this option is selected, all contours and junctions are filled into a results table.

**Add to Manager:** All lines and junctions points will be added to the roi manager.

## Overlap resolution

You can select a method to attempt automatic overlap resolution. The accuracy of this method will depend on the structure of your data.

### Method: NONE

The default behavior: no assumption of overlap is made. Any point of potential intersection will be treated as an end point for the ridges involved.

### Method: SLOPE

This method makes the assumption that when two ridges overlap, it is more likely that they will continue on their path than make turns. **This is best suited to datasets with brief periods of overlap!** If two ridges have a significant portion of overlap, the accuracy of this method will rapidly diminish.

If you use this method of overlap resolution, it is recommended that you first tune the Ridge Detection parameters with `Preview` enabled to get a minimal starting set of junction points - so that each ridge matches reality as best as possible. For example:

<img src="/media/plugins/slope-detection-low-sigma.png" width="325"/>

This detection with a sigma of 1.6 produces a set of lines and junctions not suited to slope-based overlap detection.

<img src="/media/plugins/slope-detection-high-sigma.png" width="325"/>

The same image with a sigma of 3.0. These are "real" junction points that will allow reasonable overlap detection via line slope.

<img src="/media/plugins/slope-detection-bad.png" width="325"/>

In this image we see poor overlap detection. In this case due to a superfluous junction point at the bottom of one arm, leading to a misdiagnosis of what lines are overlapping.

<img src="/media/plugins/slope-detection-success.png" width="325"/>

Successful ridge detection with slope-based overlap detection enabled. Line 134 is selected to illustrate the selection of a complete line despite numerous intersections.

# Installation

Simply turn on the [Biomedgroup update site](/update-sites/following), which includes the ridge detection plugin.

If you use ImageJ just copy the RidgeDetection.jar file in your plugins folder and copy the [apache-commons-lang 3](http://commons.apache.org/proper/commons-lang/) jar file into the plugins/jars folder.

# Who used this plugin?

This is a list of publications where the plugin was used:

{% include citation doi="10.1088/1367-2630/18/5/055001" %}

{% include citation doi="10.26508/lsa.202000880" %}

# How to cite

We think the best way is to cite the formal method and the used implementation:

**Method**:

{% include citation doi="10.1109/34.659930" %}

**Implementation**:

<a href="https://zenodo.org/badge/latestdoi/18649/thorstenwagner/ij-ridgedetection"><img src="/media/plugins/ij-ridgedetection.svg" width="174px"/></a>

{% include citation %}
