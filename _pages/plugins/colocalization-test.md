---
mediawiki: Colocalization_Test
title: Colocalization Test
categories: [Colocalization,Color Processing]
---

{% include warning/deprecated
  old="the Colocalization Test plugin"
  new="[Coloc 2](/plugins/coloc-2)" %}

{% capture maintainer%}
{% include person id='chalkie666' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='Colocalisation_Analysis' branch='master' source='Colocalisation_Test.java' %}, modified from [MBF ImageJ](/software/mbf-imagej)
{% endcapture %}
{% include info-box name='Colocalization Test' software='ImageJ - Fiji' author='Tony Collins (and others?)' maintainer=maintainer filename='Colocalization.jar' source=source latest-version='june 2009' website='[Colocalization Analysis\#Colocalization\_Test](/imaging/colocalization-analysis#colocalization-test)' status='<span style="color:red">Deprecated, use [Coloc 2](/plugins/coloc-2) instead.</span>' %}

## Purpose

Performs one of a set of three statistical tests, comparing the Persons correlation coefficient of 2 colour channels in the real image data against a white noise image, or the same image data with one of the colour channels spatially shifted, repeated a number of times.

## Documentation

See the great documentation for this plugin at [Colocalization Analysis#Colocalization_Test](/imaging/colocalization-analysis#colocalization-test).

This tells you if the colocalization that you measure with other plugins, such as [Colocalization Threshold](/plugins/colocalization-threshold) is better than random chance. For a busy image with lots of signal in both channels and very little area with no signal, there will be lots of random overlap, and this is easy to confuse with real colocalization with some biological meaning. It gives a P vaule (not a p-value) where 1 means all the randomised images had worse correlation than the real images, as you would expect for a real colocalised signel. A P value less than 0.95 is lower than the usual 95% statistical confidence limit.

The methods implemented are White Noise Image Approximation of Costes' image randomisation (most robust, use 100 iterations), van Steensel and Fay (image shift methods). These differ in how the randomised images are generated from the real image or from white noise. None of them implement the Costes image randomisation test as described in his paper. [Coloc\_2](/plugins/coloc-2) does though.

See also the [Colocalization Analysis](/imaging/colocalization-analysis) tutorial.

  
