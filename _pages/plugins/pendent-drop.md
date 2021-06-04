---
mediawiki: Pendent_Drop
title: Pendent Drop
doi: 10.5334/jors.97
categories: []
---

{% include info-box name='Pendent Drop' software='Fiji' author=' [Adrian Daerr](http://www.msc.univ-paris-diderot.fr/~daerr/)' maintainer=' [Adrian Daerr](http://www.msc.univ-paris-diderot.fr/~daerr/)' update-site='https://sites.imagej.net/Daerr/' source='https://github.com/adaerr/pendent-drop' released='September 28, 2010' latest-version='version 2 (September 20, 2015)' status='stable, active' %}

![](/media/plugins/eaucontrastemaxfit.jpg)

*Pendent drop profile integration and fitting*

## Brief description

This plug-in allows for interactive or automated adjustment of a profile to an image of a pendent drop. The plugin reports the capillary length providing the best fit, as well as surface tension, volume and surface associated with this profile.

## Description

The pendent drop method is commonly used to measure surface tensions of liquids. It consists in analysing the shape of a drop hanging typically from a capillary tube and about to detach (sometimes the inverse situation of a bubble forming at the bottom of a liquid is preferred, or that of a sessile drop or bubble). The shape is very sensitive to the unknown interfacial tension. The (axisymmetric) drop profile is described by only one non-dimensional parameter (tip radius over capillary length), although in practice five dimensional parameters can be adjusted within this plug-in: tip position and curvature, tilt of symetry axis and capillary length. The surface tension is calculated from the latter if the density difference is given.

## Installation

The latest stable version is uploaded to the Fiji update site http://sites.imagej.net/Daerr/

Follow the procedure described on the Fiji wiki at [How to follow a 3rd party update site](/update-sites/following) to have Fiji download and install the plugin (Fiji will keep track of updates).

## Documentation, links and ressources

-   Ask questions on the [pendent drop topic page of the ImageJ forum](http://forum.imagej.net/t/pendent-drop-plugin-how-to-use/290)
-   To cite this software, please use the following reference: A. Daerr and A. Mogne, *Pendent\_Drop: An ImageJ Plugin to Measure the Surface Tension from an Image of a Pendent Drop*. Journal of Open Research Software, 4: e3 (2016), [DOI: 10.5334/jors.97](http://dx.doi.org/10.5334/jors.97)
-   [description on author's home page](http://www.msc.univ-paris-diderot.fr/~daerr/misc/pendent_drop.html)
-   [source code on github](https://github.com/adaerr/pendent-drop)
-   [PDF document descripting both the pendent drop method and the plugin in more detail](https://github.com/adaerr/pendent-drop/blob/master/article/Goutte_pendante.pdf)
