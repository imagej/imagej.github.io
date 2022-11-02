---
title: SNT › Modeling
nav-links: true
nav-title: Modeling
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
doi:
- 10.1038/s41592-021-01105-7
- 10.3389/neuro.10.025.2009
---

Modeling in SNT is performed through [Cortex3D (Cx3D)](https://github.com/morphonets/cx3d) and [sciview](/plugins/sciview). Cx3D was developed in 2009 as a computational modeling tool for simulating neurodevelopmental processes and is well known for generative models of cortical circuits. The [Morphonets](http://morphonets.org) distribution of Cx3D was modified by {% include person id='kephale' %} to be compatible with SNT and the ImageJ ecosystem. This includes using [sciview](/plugins/sciview) for 3D visualization, and support for image-based modeling.

Currently, an [IDE](/develop/ides) is the most effective way to implement custom models, using the [minimal-cx3d-example-project](https://github.com/morphonets/minimal-cx3d-example-project) as a template. For more information refer to the [GitHub project page](https://github.com/morphonets/cx3d).

{% include img align="center" name="cx3d-sciview" src="/media/plugins/snt/cx3d-sciview.png" caption="Synthetic neuron generated using the *[Random Branching](https://github.com/morphonets/cx3d/blob/master/src/main/java/sc/iview/cx3d/commands/RandomBranchingDemo.java)* demo, accessible from sciview's *Demo* menu." %}

## References

{% include citation %}
