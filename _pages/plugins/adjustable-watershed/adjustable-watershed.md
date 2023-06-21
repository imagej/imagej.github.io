---
project: /software/imagej
title: Adjustable Watershed
categories: [Segmentation]
dev-status: "stable"
---



# Adjustable Watershed

*Watershed segmentation of binary images based on the Euclidian Distance Map, similar to Process>Binary>Watershed but with adjustable sensitivity and preview*

## Basics

Watershed segmentation based on the EDM splits a particle if the EDM has more than one maximum, i.e., if there are several largest inscribed circles at different positions. Thus, it is best for segmenting particles that roughly circular.

![](/media/adjustable-watershed/adjustable-watershed-screenshot.png)

## Dialog Options (Parameters)

**Tolerance**: 
This value determines the difference of radius between the smaller of the largest inscribed circles and a circle inscribed at the neck between the particles. The higher this value, the fewer segmentation lines. The standard ImageJ Process>Binary>Watershed algorithm uses a tolerance of 0.5. The value should not be much lower than this because low values tend to produce false segmentations, caused by the pixel quantization.

## Limitations

* The plugin should not be used if particles can have inner holes. For such particles, unpredictable segmentation lines can occur or the particle may remain unsplit. To make sure you have no such particles, you may run 'fill holes' before use and see whether anything changes.

## Download and Installation
{% include github branch='master' source='/media/adjustable-watershed/Adjustable_Watershed.java' %}
{% include github branch='master' source='/media/adjustable-watershed/Adjustable_Watershed.class' %}

* Copy Adjustable_Watershed.java into the ImageJ plugins folder or a subfolder thereof. Make sure that you name the downloaded file ”Adjustable_Watershed.java”; uppercase/lowercase matters.
* Compile with “Compile and Run” and press “OK”.
* Alternatively, directly save the .class file Adjustable_Watershed.class into the ImageJ/plugins directory or an immediate subdirectory thereof. Again, make sure that you name the file correctly, uppercase/lowercase matters.
* Use Help>Update Menus or restart ImageJ to make it appear in the Plugins menu.

