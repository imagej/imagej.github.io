---
mediawiki: TensorFlow
title: TensorFlow
section: Explore:Software
categories: [Software,Citable,SciJava]
doi: 10.5281/zenodo.4724125
---


{% capture author%}
{% include wikipedia title='Google Brain' text='Google Brain'%} team
{% endcapture %}

{% capture source%}
{% include github org='tensorflow' repo='tensorflow' %}
{% endcapture %}
{% include notice icon="info" content='Plugin' software='TensorFlow' name='TensorFlow' logo='<img src="/media/logos/tensorflow.png" width="128"/>' author=author maintainer='TensorFlow developers' source=source website='https://www.tensorflow.org/' %}[TensorFlow](https://www.tensorflow.org/) is an [open-source](/licensing/open-source) software library for {% include wikipedia title='Artificial intelligence' text='machine intelligence'%}.

The [ImageJ-TensorFlow](https://github.com/imagej/imagej-tensorflow) project enables TensorFlow to be used from ImageJ commands and scripts. Some ImageJ plugins currently use TensorFlow to classify images according to pre-trained models. Future plugins are planned which will support refining models based on additional training images from ImageJ.

## Publication

{% include citation %}

## See also

-   {% include github org='imagej' repo='imagej-tensorflow' label='ImageJ-TensorFlow on GitHub' %}.
-   The TensorFlow [update site](/update-sites) to make TensorFlow features available in ImageJ.
-   [Microscope Focus Quality](/plugins/microscope-focus-quality), an ImageJ plugin which uses TensorFlow.

  
