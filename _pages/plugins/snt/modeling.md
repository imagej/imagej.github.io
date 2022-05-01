---
mediawiki: SNT:_Modeling
title: SNT › Modeling
nav-links: true
nav-title: Modeling
doi: 10.3389/neuro.10.025.2009
---

{% capture title%}
Synthetic neuron generated using the {% include bc path='Demo|Cx3D|Random Branching'%} command <a href="https://github.com/morphonets/cx3d/blob/master/src/main/java/sc/iview/cx3d/commands/RandomBranchingDemo.java">Source Code</a>, accessible from SciView's main menu.
{% endcapture %}
{% include thumbnail src='/media/plugins/snt/cx3d-sciview.png' title=title %} Modeling in SNT is performed through [Cortex3D (Cx3D)](https://github.com/morphonets/cx3d) and [SciView](/plugins/sciview). Cx3D was developed in 2009[^1] as a computational modeling tool for simulating neurodevelopmental processes and is well known for generative models of cortical circuits.

The [Morphonets](http://morphonets.org) distribution of Cx3D was modified by {% include person id='kephale' %} to be compatible with the ImageJ and Fiji ecosystem. This includes using [SciView](/plugins/sciview) for 3D visualization, and support for image-based modeling.

Currently, an [IDE](/develop/ides) is the most effective way to implement custom models, using the [minimal-cx3d-example-project](https://github.com/morphonets/minimal-cx3d-example-project) as a template. For more information refer to the [GitHub project page](https://github.com/morphonets/cx3d).

## References

{% include citation fn=1 %}
