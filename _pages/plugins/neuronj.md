---
name: "NeuronJ"
title: NeuronJ
categories: [ImageScience,Neuroanatomy]
project: /libs/imagescience
website: https://imagescience.org/meijering/software/neuronj/
team-founder: "@emeijering"
team-maintainer: "@emeijering"
source-url: https://github.com/imagescience/NeuronJ
---

[NeuronJ](http://imagescience.org/meijering/software/neuronj/) is an ImageJ plugin to for 2D tracing and analysis of elongated image structures, such as neuronal processes. Although it was [last released](https://imagescience.org/meijering/software/neuronj/releases/) in 2015, key features of the plugin remain functional.

NeuronJ features a simple interface and a detailed [online manual](https://imagescience.org/meijering/software/neuronj/manual/) but can only be used to reconstruct grayscale 2D images, is not capable of [SWC](/plugins/snt/faq#what-is-a-swc-file) export, and is not aware of hierarchical relationships between paths. We recommend using [SNT](/plugins/snt) if you need to reconstruct multichannel or 3D imagery, require SWC export, or need to perform detailed quantifications of traced structures. Recent versions of SNT can read NDF (NeuronJ data format) files, and can convert NeuronJ paths into ImageJ ROIs.
