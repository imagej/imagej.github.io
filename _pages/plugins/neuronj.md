---
mediawiki: NeuronJ
title: NeuronJ
categories: [ImageScience,Neuroanatomy]
---


{% capture maintainer%}
{% include person id='emeijering' %}
{% endcapture %}

{% capture author%}
{% include person id='emeijering' %}
{% endcapture %}

{% capture source%}
{% include github org='imagescience' repo='NeuronJ' %}
{% endcapture %}
{% include info-box software='ImageScience' name='NeuronJ' maintainer=maintainer author=author source=source status='' category='Plugins' website='http://imagescience.org/meijering/software/neuronj/' %}[NeuronJ](http://imagescience.org/meijering/software/neuronj/) is an ImageJ plugin to facilitate the tracing and analysis of elongated image structures, such as neuronal processes, complementing [SNT](/plugins/snt).

NeuronJ features a friendly interface and a detailed [online manual](https://imagescience.org/meijering/software/neuronj/manual/) but can only be used to reconstruct 2D images and is not capable of [SWC](http://www.neuronland.org/NLMorphologyConverter/MorphologyFormats/SWC/Spec.html) export, the most common format used in neuronal reconstructions. If you need to reconstruct three-dimensional imagery and require a program aware of SWC, we recommend using [SNT](/plugins/snt) instead.
