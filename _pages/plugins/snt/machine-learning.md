---
title: SNT › Machine Learning
nav-links: true
nav-title: Machine Learning
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
doi:
- 10.3389/fcomp.2022.777728
- 10.1093/bioinformatics/btx180
---

{% capture version%}
**This page was last revised for [version 5.0.0](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

SNT interacts with [Labkit](../labkit) and [Trainable Weka Segmentation (TWS)](../tws), both leveraging  machine learning algorithms for semantic segmentation of images (namely, random forest classifiers). The bridge between these tools makes it possible to:

- Import a pre-trained model into SNT and directly load the probability maps of the semantic segmentation as secondary tracing layer
- Train a model with SNT paths

The table below summarizes key differences between Labkit and TWS (as of SNT v4.3.0). Note that both tools classify images using the [Weka framework](https://ml.cms.waikato.ac.nz/weka/).

|                                                      | **[Labkit](../labkit)**                              | **[TWS](../tws)**            |
|------------------------------------------------------|------------------------------------------------------|------------------------------|
| Image size                                           | Out-of-core, multiple terabytes large image data     | Smaller images (RAM-limited) |
| GPU support                                          | via [CLIJ2](https://clij.github.io/)                 | No                           |
| Underlying architecture(s)                           | [ImgLib2](/libs/imglib2) and [BigDataViewer](../bdv) | ImageJ                       |
| Support for multichannel images                      | Yes                                                  | Yes (w/ [caveats](#caveats)) |
| Support for timelapse images                         | Yes                                                  | Yes (w/ [caveats](#caveats)) |
| Scripting and IJ macro language support              | Yes. Some commands are macro-recordable              | Yes. GUI is macro-recordable |
| Batch Processing                                     | From GUI and via macros and scripts                  | Via macros and scripts       |
| Import of pre-trained models into SNT                | Yes                                                  | Yes                          |
| Direct loading of SNT paths as classification labels | Yes                                                  | Yes                          |

## Importing Models

<img align="right" width="400" src="/media/plugins/snt/import-weka-model.png" title="Import Models prompt (v4.3.0)" />

Importing of models can be done via the [Secondary layer menu](manual#tracing-on-secondary-image-layer). Once the trained model is imported, it is applied to the image being traced, and the resulting classification is loaded as a secondary tracing image. The import prompt has the following options:

- **Model file**: The file to be imported. Typically, with a .model or .classifier extension (Labkit: JSON-encoded; TWS: XML-encoded)
- **Loading engine**: How the model should be loaded and applied. Either *Labkit*, *Labkit w/ GPU acceleration* or *Trainable Weka Segmentation (TWS). NB: Labkit w/ GPU acceleration* expects [CLIJ2](https://clij.github.io/) access, and a CLIJ2-compatible graphics card
- **Load as**: Either *Probability* (p-map) or *Segmented* image. If *Probability image*, the class associated with neurite signal needs to be chosen in a follow-up prompt
- **Display**: Whether the classified image should be immediately displayed. NB: This can be done at anytime using the [View›](./manual#view) menu

## Training Models

To convert traced paths into training labels, simply select the path(s) of interest and run the respective command in the Path Manager's [Process›](manual#process-) menu. This will start up a new instance of Labkit/TWS preloaded with labels generated from selected path(s).
Paths from different channels are split into distinct classification classes 
(i.e., 1 class per channel). Note that there are some (minor) idiosyncrasies in the way Labkit and TWS handle SNT-generated labels:

<span id="caveats"></span>

|                                         | **[Labkit](../labkit)**                                   | **[TWS](../tws)**                                                                                                                                                                               |
|-----------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Single-node paths                       | Valid labels                                              | Typically skipped                                                                                                                                                                               |
| Hyperstacks (images with CT dimensions) | Displayed by [BigDataViewer](../bdv)                      | CT dimensions are displayed as a simple stack in the TWS window. IJ's {% include bc path='Stack to Hyperstack...' %} command can be used to re-apply the original image layout to output images |

<table>
  <tr style="background-color:white">
    <td style="width:50%">
    <img width="100%" src="/media/plugins/snt/snt-labkit-training.png" title="SNT Paths as classifier labels: Labkit" />
    </td>
    <td style="width:50%">
    <img  width="100%" src="/media/plugins/snt/snt-tws-training.png" title="SNT Paths as classifier labels: TWS" />
    </td>
  </tr>
  <tr style="background-color:white">
    <td style="width:50%">
    Drosophila OP neuron (3D grayscale image, SNT's <i>Demo 03</i>) being classified in Labkit.
    </td>
    <td style="width:50%">
    A triple-stained neuron (2D multichannel image, SNT's <i>Demo 06</i>) being classified in TWS.
    </td>
  </tr>
</table>

## Scripts

There are a couple of examples in SNT's neuroanatomy [template collection](scripting#bundled-templates) handling image classification, namely:

- *Apply Weka Model To Tracing Image*: Demonstrates how to apply a pre-existing Weka model to the image being traced
- *Train Weka Classifier*:   Exemplifies how to train a Weka model using traced paths and ROIs 

## References

{% include citation %}

The [Weka framework](https://waikato.github.io/weka-wiki/citing_weka/) is described in:

- Eibe Frank, Mark A. Hall, and Ian H. Witten (2016). The WEKA Workbench. 
  Online Appendix for "Data Mining: Practical Machine Learning Tools and 
  Techniques", Morgan Kaufmann, Fourth Edition, 2016. ([PDF](https://ml.cms.waikato.ac.nz/weka/Witten_et_al_2016_appendix.pdf))
