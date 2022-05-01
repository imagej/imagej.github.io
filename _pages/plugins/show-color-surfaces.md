---
mediawiki: Show_Color_Surfaces
title: Show Color Surfaces
categories: [Uncategorized]
---


{% capture source%}
{% include github org='fiji' repo='3D_Viewer' branch='master' source='isosurface/Show_Colour_Surfaces.java' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Show Color Surfaces' author='Mark Longair' maintainer='Mark Longair' filename='VIB\_.jar' source=source status='stable' %}

This plugin allows you to add surfaces generated from *label field stacks* to a new or existing 3D viewer.

A *label field* is an 8-bit image stack where the numbers attached to each pixels refer to a specific class rather than an intensity. Usually, label fields are visualized using a lookup table so that different classes are shown as different colors.

The *Show Color Surfaces* command calculates surfaces embedded into the [3D Viewer](/plugins/3d-viewer) from label fields:

![](/media/plugins/show-color-surfaces-reduced.png)

## Menu path

{% include bc path='Plugins | Process | Show Color Surfaces'%}


