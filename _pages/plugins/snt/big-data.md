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

SNTv5 implemented _preliminary_ support for big data. The support remains basic but currently supports the following operations:

| Operation          | Status                | Details |
|--------------------|-----------------------|---------|
| Tracing operations | Headless support only | A* tracing performed using pre-existing coordinates is fully supported via scripting in headless operations. [Example implementation](https://github.com/AllenNeuralDynamics/neuron-tracing-utils). For interactive tracing, please use [HortaCloud](https://hortacloud.org/): This is SNT's development team recommended tool for tracing Terabyte-size datasets |
| Path optimization  | Headless support only | [Optimization of curvatures](./manual#refinefit-), including extraction of radii |
| 3D Visualization   | Supported via [sciview](./manual#sciview) and [BigVolumeViewer](./manual##big-volume-viewer)  | Visualization of 3D reconstructions, including [color mappings](./manual#color-mapping-), etc. |
