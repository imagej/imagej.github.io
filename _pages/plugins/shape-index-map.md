---
mediawiki: Shape_Index_Map
name: "Shape Index Map"
title: Shape Index Map
categories: [Uncategorized]
release-date: "18/08/2010"
initial-release-date: "18/08/2010"
team-maintainer: "@dscho"
team-founder: '@dscho'
---



{% capture source%}
{% include github org='fiji' repo='Fiji_Plugins' branch='master' source='fiji/geom/Shape_Index_Map.java' %}
{% endcapture %}
{% include info-box source=source  %}

## Explanation

The [shape index](http://journals.cambridge.org/action/displayAbstract?fromPage=online&aid=6820324) describes the surface topology of the image interpreted as a [height field](/plugins/3d-surface-plot):

| shape index | 1   | 0.75 | 0.5   | 0.25         | 0      | -0.25      | -0.5 | -0.75  | -1  |
|-------------|-----|------|-------|--------------|--------|------------|------|--------|-----|
| meaning     | cap | dome | ridge | saddle ridge | saddle | saddle rut | rut  | trough | cup |

The shape index is calculated from the principal curvatures of the Hessian, which is very susceptible to noise. Therefore the plugin asks you to specify a radius for Gaussian blurring as a preprocessing step.

## Example

![](/media/plugins/shape-index-orig.jpg)

With radius 2, this results in the following shape index map (bright spots correspond to caps, dark to cups):

![](/media/plugins/shape-index-map.jpg)


