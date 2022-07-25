---
mediawiki: Image_Synthesizer
name: "Image Synthesizer"
title: Image Synthesizer
categories: [Uncategorized]
release-date: "24.05.2020"
initial-release-date: "19.03.2018"
website: "http://wiki.imagej.net/Image\_Synthesizer"
team-founder: 'Maximilian Maske'
team-maintainer: 'Maximilian Maske'
---

{% include info-box %}

## Overview of 'Image Synthesizer'

This plugin generates images from mathematical functions and primitive patterns in all ImageJ image types. It can be used to generate synthetic test-cards to analyze for example the behavior of filter-operations or to test the functionality of various algorithms in image-processing. The tool can also be used in a teaching environment, where example images for presentations can be prepared or even to demonstrate basic principles of digital image processing (e.g. by showing the relation between function values and the generated images). Further on an artistic use to create images stacks or videos is also imaginable.

## Modes

\- Functions to image: The function value of a two- or three-dimensional function f(x, y) or f(x, y, z) is interpreted as the intensity value of the image.

\- Conditional to image: Generate primitive patterns using boolean expressions with ImageJ macro code. The conditional will be executed for each pixel in the image inside the given coordinate range.

## Source

See the source code: https://github.com/IamMM/Image_Synthesizer
