---
mediawiki: Max_Inscribed_Circles
title: Max Inscribed Circles
categories: [Segmentation, Feature Extraction]
---


{% capture source%}
{% include github org='ptbiop' repo='ijp-max-inscribed-circles' %}
{% endcapture %}
{% include info-box name='Max Inscribed Circles' software='Fiji' author='Olivier Burri, Romain Guiet' maintainer='Olivier Burri' filename='Max_Inscribed_Circle.jar' released='August 2015' latest-version='July 2016' source=source status='stable' website=' [BIOP Staff Page](https://www.epfl.ch/research/facilities/ptbiop/staff/)' %}

## Purpose

This is an implementation of the Largest Inscribed Circle algorithm using an euclidean distance map. The algorithm is looped until a circle diameter smaller than the defined minimum diameter is found. The code for this plugin was inspired by this [Matlab Central function](http://www.mathworks.ch/matlabcentral/fileexchange/30805-maximum-inscribed-circle-using-distance-transform)

{% include img src="max-largest-circ-dialog2" width="500" caption="Plugin Dialog choices" %}

## Details

As of July 26th 2016, the plugin has been rewritten with a new algorithm to make it run much faster.. See the faster implementation details figure. <img src="/media/plugins/max-circles-algorithm-overview.png" title="fig:Faster implementation details" width="400" alt="Faster implementation details" />

The previous implementation would calculate a distance map, then find the max value, place a circle and repeat. This was making it very slow for small circle diameters or large images as it needed to make one distance map calculation per circle on the whole image.

By using a Local Maxima Finder, we can draw multiple circles on a single pass, provided that these are

1.  The largest distances on the distance map image
2.  Not overlapping with one another

That way when there are plenty of circles that are the same size, we can draw them all at the same time.

## Installation

This plugin is available from the [PTBIOP Update Site](/list-of-update-sites). This places it in a "BIOP" Folder in the plugins directory of Fiji/ImageJ

## Use

Call up the plugin using {% include bc path="Plugins|BIOP|Image Analysis|Binary|Max Inscribed Circles..." %}.

You can select the smallest circle diameter after which it will stop looking, and whether you want the plugin to run on the current selection or the current image mask.

It will add all the found circles to the ROI Manager.

Setting the Minimum Disk Diameter to 0 will return a single ROI with the largest inscribed circle.

{% include img src="max-largest-circ-beforeafter" width="400" caption="Result of Plugin on whole image" %}

## Macro Recordable

Making use of the GenericDialog class, the plugin is macro-recordable.

```java
run("Max Inscribed Circles...", "minimum=20");
```

## Running from a Plugin

What you need to run this in a plugin is

```java
import ch.epfl.biop.MaxInscribedCircles;
```

And then call the static method

```java
//imp must be an 8-bit binary image
ArrayList<Roi> circles = MaxInscribedCircles.findCircles(ImagePlus imp, double minD, boolean isSelectionOnly);
```

Set the last argument `isSelectionOnly` to true if you want to fit circles in the current selection. If you'd like to use the pixel mask, set it to false.

## Notes

The accuracy is not perfect as we are using the distance map which has finite values. But for most practical purposes (Circles larger than 2 pixels in diameter), it should be sufficient.
