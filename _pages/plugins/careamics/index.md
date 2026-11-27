---
title: CAREamics - Noise2Void
description: Noise2Void self-supervised denoising training and prediction via [CAREamics](https://careamics.github.io).
doi: 10.1109/cvpr.2019.00223
website : https://careamics.github.io/
icon: careamics.png
categories: [Denoising, Deep Learning]
source-url: https://github.com/CAREamics/careamics-fiji
source-label: CAREamics-Fiji

nav-links:
- title: Overview
  url: /plugins/careamics/index
- title: Training
  url: /plugins/careamics/training
- title: Prediction
  url: /plugins/careamics/prediction
- title: Export
  url: /plugins/careamics/export
---

**[CAREamics](https://careamics.github.io/)** is a library aimed at simplifying the use of state of the art image restoration deep-learning algorithms, from well-established algorithms (CARE, Noise2Void) to cutting-edge methods (MicroSplit).  

**Noise2Void** is a self-supervised denoising method. It trains by randomly masking pixels in the input image and predicting their masked value from the surrounding pixels. N2V relies on two fundamental hypotheses:
- The underlying structures are smooths (i.e. continuous).
- The noise is pixel-wise independent (i.e. the noise in one pixel is not correlated with the noise in a neighboring pixel).

This plugin uses CAREamics Noise2Void implementation for denoising:
- [Training](/plugins/careamics/training)
- [Prediction](/plugins/careamics/prediction)
- [Export](/plugins/careamics/export)
