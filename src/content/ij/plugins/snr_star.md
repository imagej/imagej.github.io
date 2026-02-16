---
title: SNRstar – Covariance-based SNR measurement
categories: [Analysis]
doi: 10.6009/jjrt.2022-1154
---

## SNRstar – Covariance-based SNR measurement

Author: Motohiro TABUCHI

SNRstar is an ImageJ macro that estimates signal variance and noise variance using covariance between two repeated images acquired under identical imaging conditions.  
It provides an unbiased and statistically optimal estimation of SNR.

### Features

- Covariance-based signal variance estimation
- Noise variance estimation from difference of images
- Outputs SNR* [dB], ROI size, signal variance, and noise variance
- Simple workflow using ImageJ ROI tools

### Requirements

- ImageJ 1.53 or later
- Exactly two observed images of identical dimensions acquired under identical imaging conditions

### Download

[GitHub Repository](https://github.com/Motohiro-TABUCHI/SNR_star_Tool)

### Notes

- Assumes additive, zero-mean, independent noise between the two images
- Larger ROIs improve estimation stability
- Negative covariance may indicate unsuitable imaging conditions

### Reference

{% include citation %}
