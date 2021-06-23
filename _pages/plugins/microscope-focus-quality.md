---
mediawiki: Microscope_Focus_Quality
title: Microscope Focus Quality
project: /software/fiji
categories: [Uncategorized]
artifact: sc.fiji:microscope-image-quality
doi: 10.1186/s12859-018-2087-4
---

 

<img src="/media/mifqc.png" width="900"/> 

This plugin assesses the focus quality of microscope images, classifying the image in tiles.

## Summary

The plugin predicts an absolute measure of image focus on a single image in isolation, without any user-specified parameters. It uses a pre-trained deep neural network, operating at the image-patch level, and also outputs a measure of prediction certainty, enabling interpretable predictions.

## Installation

-   [Enable](/update-sites/following) the TensorFlow [update site](/update-sites).
-   The command is in {% include bc path='Plugins | Classification | Microscope Image Focus Quality'%}.

## Usage

-   Open an image to analyze (see [sample images](https://storage.googleapis.com/microscope-image-quality/static/fiji_plugin_test_images.zip)).
-   Run {% include bc path='Plugins | Classification | Microscope Image Focus Quality'%}.
-   A dialog will appear allowing you to configure the output visualization. The following options are available:
    -   **Generate probability image** - When checked, a multi-channel image will be created with one channel per focus level, and each value corresponding to the probability of that sample being at that focus level.
    -   **Overlay probability patches** - When checked, each classified region of the image will be overlaid with a color whose hue denotes the most likely focus level and whose brightness denotes the confidence (i.e., probability) of the region being at that level.
    -   **Show patches as solid rectangles** - When checked, overlaid probability patches will be filled semi-transparent and solid; when unchecked, they will be drawn as hollow boundary boxes.
    -   **Displayed patch border width** - When drawing probability patches as boundary boxes, this option controls the box thickness.

The screenshot above uses the "Overlay probability patches" option with a thickness of 5.

If you wish to access the results of the classification quantitatively (e.g., as part of an automated workflow via [scripting](/scripting)), use the "Generate probability image" option.

You can can remove the probability patches overlay via the {% include bc path='Image | Overlay | Remove Overlay'%} command.

## Limitations

The plugin is currently limited to single (i.e., 2D) images of 16-bit integer data only. The model was trained with images in the intensity range of `[0, ~10000]`; your mileage may vary if the input image intensities diverge from that too greatly.

## Publication

{% include citation %}

## See also

-   [TensorFlow](/libs/tensorflow), the machine learning library this plugin uses.
-   [Using Deep Learning to Facilitate Scientific Image Analysis](https://research.googleblog.com/2018/03/using-deep-learning-to-facilitate.html) post on Google Research Blog


