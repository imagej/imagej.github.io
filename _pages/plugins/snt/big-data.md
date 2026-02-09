---
title: SNT › Big Data
nav-links: true
nav-title: Big Data
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
tags: snt,tracing,segmentation,neuroanatomy,big-data
---

{% capture version%}
**This page was last revised for [version 5.0.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

## Big Data support

SNTv5 implemented _preliminary_ support for big data. The support remains basic but the following operations are currently supported:

| Operation                | Status                                                                                      | Details                                                                                                                              |
|--------------------------|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Automated tracing        | Supported (experimental)                                                                    | See [Auto-tracing](./auto-tracing#grayscale-images)<sup>1,2</sup>                                                                    |
| Tracing along way-points | Headless support only<sup>2</sup>                                                           | A* tracing performed using pre-existing coordinates is fully supported via scripting<sup>2</sup> in headless operations<sup>1</sup>. |
| Path optimization        | Headless support only<sup>2</sup>                                                           | [Optimization of curvatures](./manual#refinefit-), including extraction of radii<sup>2</sup>                                         |
| 3D Visualization         | Supported via [sciview](./manual#sciview) and [BigVolumeViewer](./manual#big-volume-viewer) | Visualization of 3D reconstructions, including [color mappings](./manual#color-mapping-), etc.                                       |

<sup>1</sup>For interactive tracing, please use [HortaCloud](https://hortacloud.org/): This is SNT's development team recommended tool for tracing Terabyte-size datasets

<sup>2</sup>See [PySNT](https://pysnt.readthedocs.io/en/latest/)
