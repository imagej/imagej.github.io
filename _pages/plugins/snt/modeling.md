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

{% capture version%}
**This page was last revised for [version 4.2.0](https://github.com/morphonets/SNT/releases)**.<br>
Please help us to keep up-to-date documentation by [editing](https://github.com/imagej/imagej.github.io/edit/main/_pages/plugins/snt/modeling.md) this page directly to fill in any documentation gap. Do [reach out](https://forum.image.sc/tag/snt) if you need assistance!
{% endcapture %}
{% include notice content=version %}


Modeling in SNT is performed through [Cortex3D (Cx3D)](https://github.com/morphonets/cx3d) and [sciview](/plugins/sciview). Cx3D was developed in 2009 as a computational modeling tool for simulating neurodevelopmental processes, including cell division, migration, neurite outgrowth, and chemotaxis in 3D physical space. It is well known for generative models of cortical circuits.

Unlike electrophysiology simulators (e.g., [NEURON](https://www.neuronsimulator.org/)), Cx3D operates at the developmental time scale: it models how neurons grow and wire up, not how they fire. The [Morphonets](http://morphonets.org) distribution of Cx3D was modified by {% include person id='kephale' %} to be compatible with SNT. This includes using [sciview](/plugins/sciview) for 3D visualization, and support for image-based modeling.

{% include img align="center" name="cx3d-sciview" src="/media/plugins/snt/cx3d-sciview.png" caption="Synthetic neuron generated using the *[Random Branching](https://github.com/morphonets/cx3d/blob/-/src/main/java/sc/iview/cx3d/commands/RandomBranchingDemo.java)* demo, accessible from sciview's *Demo* menu." %}

## Key Cpabilities
- **Morphogenesis**: Cells divide, migrate, and grow neurites in a 3D physical space governed by mechanical forces and chemical gradients
- **Agent-based**: Each cell follows local rules; emergent network structure arises from those rules
- **Developmental time scales**: Hours/days of neurodevelopment
- **Encoded environmental cues**: Cues like chemical gradients/forces can be encoded by imagery

> NB: Membrane biophysics and related cable equations are not considered in Cx3D simulations

## Custom Models
Currently, an [IDE](/develop/ides) is the most effective way to implement custom models, using the [minimal-cx3d-example-project](https://github.com/morphonets/minimal-cx3d-example-project) as a template. For more information refer to the [GitHub project page](https://github.com/morphonets/cx3d).


## References

{% include citation %}
