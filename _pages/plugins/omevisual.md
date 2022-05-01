---
mediawiki: OMEVisual
title: OMEVisual
categories: [OME]
---


{% capture author%}
{% include person id='hadim' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='hadim' %}
{% endcapture %}

{% capture source%}
{% include github org='fiji' repo='OMEVisual' %}
{% endcapture %}
{% include info-box name='OMEVisual' logo='' software='Fiji' author=author maintainer=maintainer source=source released='08/05/2016' status='v1.0.1, stable' category='' %}


## Presentation

`OMEVisual` is a Fiji plugin to easily visualize OME metadata.

Usage:

-   Open your image in Fiji.
-   Start the plugin with {% include bc path="Plugins | Utilities | Visualize OME Metadata" %}.
-   A window should open with the metadata in it.

Please note that :

-   This goal of this plugin is **not to implement** all the OME features.
-   This plugin makes several strong assumptions about the OME model in order to simplify the interface :
    -   Each image contains only one `Pixels` element.
    -   Each `TiffData` contains only one `Plane`.
    -   `Plane` and `TiffData` informations are displayed at the same location without distinction.
-   Any ideas to improve the visualization and/or add OME features is very welcome :
    -   The best way is to submit a PR.
    -   You can also open an issue and post an OME-TIFF file which contains additional OME features you would like to see added to the plugin.

{% include img src="omevisual-screenshot" width="600" caption="OMEVisual Screenshot" %}

## Related links

-   Source code on GitHub : https://github.com/fiji/OMEVisual

## Authors

`OMEVisual` has been created by [Hadrien Mary](mailto:hadrien.mary@gmail.com).

This work started in 2016 at the [Gary Brouhard laboratory](http://brouhardlab.mcgill.ca/) at the University of McGill.

 
