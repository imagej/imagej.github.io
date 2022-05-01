---
mediawiki: KymographBuilder_:_Yet_Another_Kymograph_Fiji_plugin
title: KymographBuilder  › Yet Another Kymograph Fiji plugin
categories: [Uncategorized]
---


{% capture author%}
{% include person id='hadim' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='hadim' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='KymographBuilder' %}
{% endcapture %}
{% include info-box name='KymographBuilder' logo='' software='Fiji' author=author maintainer=maintainer source=source released='24/04/2016' status='v1.2.2, stable' category='' %}

## Presentation

*KymographBuilder is Yet Another Kymograph Fiji plugin.*

Features are :

-   Build kymograph from a straight or segmented line (a polyline).
-   Build kymograph for images with multiple channels.
-   Take into account the width of the line using maximum projection along its thickness.
-   Built from scratch and use the ImageJ2 Ecosystem.
-   Fast and easy to use.

How to use :

-   Draw a line: it can be a polyline and you can also set the thickness that will be taken into account by the plugin.
-   Launch KymographBuilder : {% include bc path='Plugins|Kymograph|KymographBuilder'%}
-   You're done.

<figure><img src="/media/plugins/kymograph-construction.png" width="600" /></figure>

## Scripting

You can script the plugin. Here is an example:

{% include code org='fiji' repo='KymographBuilder' branch='master' path='src/main/resources/script_templates/Examples/MultiKymographBuilder.py' %}

## Related links

-   [Multi_Kymograph](/plugins/multi-kymograph) : The first kymograph bundled with Fiji, with support for multiple Line ROIs
-   Source code on GitHub : https://github.com/fiji/KymographBuilder
-   Maven : https://maven.scijava.org/#nexus-search;quick~kymographbuilder
-   Travis CI : https://travis-ci.org/fiji/KymographBuilder

## Authors

KymographBuilder has been created by Hadrien Mary.

This work started in 2016 at the Gary Brouhard laboratory (http://brouhardlab.mcgill.ca) at McGill University.
