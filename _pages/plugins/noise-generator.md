---
mediawiki: Noise_Generator
title: Noise Generator
categories: [Noise]
extensions: ["mathjax"]
---


{% capture author%}
{% include person id='acsenrafilho' %} ([1](mailto:acsenrafilho@gmail.com))
{% endcapture %}

{% capture maintainer%}
{% include person id='acsenrafilho' %}
{% endcapture %}

{% capture source%}
{% include github org='CSIM-Toolkits' repo='ImageJ/tree/master/plugins/NoiseGenerator' label='GitHub CSIM-ImageJ Noise Generator repository' %}
{% endcapture %}
{% include info-box name='Noise Generator PlugIn' software='Fiji' author=author maintainer=maintainer source=source released='February 08<sup>th</sup>, 2015' latest-version='February 08<sup>th</sup>, 2015' status='experimental, active' category='Plugins, Noise' %}

## Noise Generator

It is well know that in every image acquisition process exist a noise level always present by different sources. Each noise has its particular characteristics and the behavior on image acquisition plays an importanto role to quantify the reliability on further image manipulations such as registration and tissue segmentation.

**Update notes:**

-   *Feb-08-2015*: Available to produce additive noise on 2D images with some specific noise probability distributions. It is produced in the majority the MRI and complex noise distributions.

## Noise Distributions

## How to use

We try to implement a simple PlugIn in order to produce additive noise on a set of different noise probability distributions. In this case, only click on the PlugIn ImageJ menu and hit the Noise Generator PlugIn.

A window will pop up where you can choose what noise you want to add and the its intensity. The intensity is relative to a percentage (0-100%), which 0% does nothing in the image. For any other value between 0-100%, our PlugIn calculate the maximum contrast for each pixel depth (8-bits and 32-bits gray images) selected in the same Noise Generator window, and with this measure it could be estimated the noise intensity based on the maximum pixel contrast.

<span style="color:#ff0000"> NOTE: </span> **The majority of noises takes no more than some milliseconds to be calculated (depending the image size). However, for the case of $$1/f^\beta$$ noises the time consuming is much higher because of the 2D Fourier Transforms used for these kinds of noises.**
