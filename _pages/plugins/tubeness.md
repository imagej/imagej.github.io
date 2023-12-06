---
name: "Tubeness"
title: Tubeness
project: /software/imagej2
artifact: net.imagej:imagej-ops
icon: /media/icons/imagej2.png
doi: 10.1016/s1361-8415(98)80009-1
categories: [Uncategorized]
---

_Tubeness_ is an algorithm for enhancing filamentous structures of a specified thickness (blood vessels, neurites, and other tube-like structures)described by Sato et al 1998.[^1]. It can be applied to 2D and 3D images. It can be a faster alternative to [Frangi](/plugins/frangi). The algorithm is explained in more detail [here](https://github.com/imagej/imagej-ops/pull/527). There are three _Tubeness_ implementations in ImageJ:

- Legacy plugin (In Fiji registered under {% include bc path='Plugins|Analyze|Tubeness' %} ([source code](https://github.com/fiji/VIB/blob/-/src/main/java/features/Tubeness_.java)). This is now deprecated.

- An [ImageJ Op](/libs/imagej-ops/index). This is a modernized, multithreaded version of the initial implemenation that has been validated/benchmarked more carefully ([details](https://github.com/imagej/imagej-ops/pull/527))

- An [SNT](/plugins/snt) implementation ([source code](https://github.com/morphonets/SNT/tree/-/src/main/java/sc/fiji/snt/filter)) that extends the ImageJ Op approach to multiple scales (similarly to [Frangi](/plugins/frangi)) for better detection of neurites. SNT's [Secondary Layer Wizard](/plugins/snt/manual#tracing-on-secondary-image) can also be used to preview the effect of scale size in the result.



{% include img align="center" width="600px" src="/media/plugins/tubeness-before-and-after.png" caption="Tubeness: Left: Original image. Right: Filtered image." %}




{% include citation fn=1 %}
