---
mediawiki: ImageJ1
title: ImageJ1
section: Explore:Software
categories: [Software]
doi: 10.1038/nmeth.2089
---

{% include project content='ImageJ1' %}
{% capture author%}
{% include person id='rasband' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='rasband' %}  
{% include person id='ctrueden' %}
{% endcapture %}

{% capture source%}
{% include github org='imagej' repo='imagej1' %}
{% endcapture %}
{% include info-box name='ImageJ1' software='ImageJ' logo='<img src="/media/icons/imagej1.png" width="96"/>' author=author maintainer=maintainer source=source status='stable, active' category='' %}ImageJ 1.x, often shortened to ImageJ1 or IJ1, is a stable version of [ImageJ](/software/imagej) which has been under continuous development since 1997. It has always been, and continues to be, a one-developer project of {% include person id='rasband' %}.

ImageJ was originally developed in 1997 as a cross-platform version of [NIH Image](/software/nih-image). ImageJ grew organically over time as {% include person id='rasband' %} continued to add features according to user requests. Now there are many hundreds, probably thousands, of plugins written by members of a diverse community.

The current version of ImageJ is often referred to as [ImageJ2](/software/imagej2), to differentiate it from ImageJ 1.x. The ImageJ2 distribution actually includes the latest version of ImageJ1 as well, along with a [legacy layer](/libs/imagej-legacy) for backwards compatibility, which transparently converts between IJ1 and IJ2 data structures as needed.

## See also

-   [ImageJ 1.x documentation](https://imagej.nih.gov/ij/)

## Publication

{% include citation %}
