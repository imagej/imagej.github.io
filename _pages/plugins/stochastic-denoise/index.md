---
title: Stochastic Denoise
categories: [Denoising]
name: Stochastic Denoise
dev-status: Unreleased
support-status: Unreleased
doi: 10.5244/C.23.117
team-founder: "@funkey"
team-maintainer: "@funkey"
source-url: https://github.com/fiji/Stochastic_Denoise
---

The Stochastic Denoise plugin implements a current state of the art denoising algorithm. It is based on random walks through the image along paths of similar pixels, as [proposed by Francisco Estrada et al.](https://www.cs.utoronto.ca/~strider/Denoise/)

If you intend to use this plugin in a publication, please cite:

{% include citation %}

## Settings

The plugin provides two parameters: The noise standard deviation **sigma** and the number of **samples** per pixel.

With the sigma setting, you can adjust the expected amount of noise in the image. The higher you choose this value, the blurrier the result will be.

To get more pleasing results, you can increase the number of samples (i.e., the number of random walks) per pixel. However, this will result in longer runtime.

{% include img src="settings" width="529px" %}

## Tutorial

{% include img src="clown" %} {% include img src="clown-denoised" %}

Open the image you would like to denoise and start the plugin. Try the default settings first and click {% include button label="Denoise" %}. After some seconds, the denoised image will pop up. You can change the settings and retry&mdash;the denoised image will get updated.
