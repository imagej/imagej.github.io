---
title: Glasbey
doi: 10.1002/col.20327
categories: [Color Processing]
project: /software/fiji
name: Glasbey
source-url: https://github.com/fiji/fiji/blob/-/luts/glasbey.lut
team-maintainer: '@landinig'
---

{% include img align="right" src="glasbey" %}

The Glasbey lookup table (LUT) is a color table structured in a maximally discontinuous manner. That is, adjacent color bins are chosen to be as distinct from one another as possible.

Like other LUTs, it is available from the {% include bc path='Image | Lookup Tables'%} menu.

The LUT called "glasbey" uses white at the first index, whereas "glasbey inverted" starts with black.

## Labelings

The Glasbey LUT has numerous uses. It can be helpful when coloring a "labeling" of integer-coded regions, since each region will then appear obviously distinct:

{% include img src="glasbey-labeling" %}

## JPEG artifacts

Glasbey can also be used to illustrate otherwise-subtle phenomena such as JPEG compression artifacts. Here is a comparison of the Boats sample image before and after being resaved as a JPEG:

{% include img src="jpeg-grayscale" caption="The grayscale LUT makes it very difficult (for most people) to see any visual difference." %}
{% include img src="jpeg-glasbey" caption="The Glasbey LUT makes it quite obvious where JPEG compression caused a loss of data fidelity." %}

## Publication

The Glasbey LUT is based on the publication:

{% include citation %}
