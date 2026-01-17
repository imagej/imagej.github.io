---
title: NIA
categories: [Denoising, Machine Learning, Restoration]
icon: /media/icons/RIA-J.png
source-url: "https://github.com/Epivitae/NIA-Denoise"
update-site: "Biosensor Tools"
release-version: v1.0.0
support-status: Active
team-founders: ['@Epivitae']
team-maintainers: ['@Epivitae']
---
{%- assign github            = page.github            -%}
{%- assign release-version   = page.release-version   -%}
{%- assign release-date      = page.release-date      -%}
{%- assign dev-status        = page.dev-status        -%}
{%- unless team-maintainers  -%} {%- assign team-maintainers  = page.team-maintainer  -%} {%- endunless -%}

[![DOI](https://zenodo.org/badge/1134239045.svg)](https://doi.org/10.5281/zenodo.18244343)


**NIA (Neural Inference Assistant)** is a native, AI-powered denoising plugin that brings deep learning to ImageJ/Fiji without the configuration headache.

Developed by **Dr. Kui Wang** at the Center for Excellence in Brain Science and Intelligence Technology (CEBSIT), Chinese Academy of Sciences, NIA is built on the embedded **ONNX Runtime**. It allows biologists to run advanced denoising models directly in Java, eliminating the need for external Python environments, Conda, or complex CUDA setups.

Author: [Kui Wang](https://imagej.net/people/Epivitae), CEBSIT, CAS. For questions please use the [GitHub Issues](https://github.com/Epivitae/NIA-Denoise/issues) or tag @Epivitae on image.sc.

## Key Features

* **Zero Configuration**: Runs natively in Fiji. No Python installation, no Conda environments, and no dedicated GPU setup required.
* **Proven Architecture**: Comes with a built-in, optimized **DnCNN** model (based on *Zhang et al., 2017*) specifically tuned for fluorescence microscopy.
* **Extensible**: Supports loading custom user-trained models in the standard `.onnx` format.
* **5D Hyperstack Support**: Seamlessly processes complex datasets (X, Y, Channel, Z-Slice, and Time-lapse) with auto-iterating logic.
* **Smart Normalization**: Auto-detects bit-depth (8/16/32-bit) and applies consistent normalization to prevent "flickering" artifacts in time-lapse videos.

## Installation & Update

NIA is distributed via the **Biosensor Tools** Fiji Update Site.

1.  Open **Fiji / ImageJ**.
2.  Navigate to **Help › Update...**
3.  Click **Manage update sites**.
4.  Check **Biosensor Tools** from the list.
5.  Click **Apply and Close**, then restart Fiji.

{% include notice icon="info" content="If the site is missing from the list, you can add it manually:<br>**Name:** `Biosensor Tools`<br>**URL:** `https://sites.imagej.net/Biosensor-Tools/`" %}

## Usage Guide

1.  **Open Image**: Load your noisy image or stack in Fiji.
2.  **Launch**: Go to `Plugins › Biosensor Tools › NIA Denoise (AI)`.
3.  **Select Model**:
    * **Built-in (DnCNN)**: Recommended for general fluorescence microscopy (confocal/widefield).
    * **Custom ONNX**: Select this to load your own `.onnx` model file.
4.  **Run**: Click **Start Denoising**. The plugin will process the stack and output a new denoised window.

## Citation & References

If you use NIA in your research, please cite the software DOI:

**Wang, K. (2026).** NIA Denoise: User-Friendly AI Denoising Plugin for ImageJ/Fiji (v1.0.0). *Zenodo*. https://doi.org/10.5281/zenodo.18206931

* **Repository**: [https://github.com/Epivitae/NIA-Denoise](https://github.com/Epivitae/NIA-Denoise)
* **CNS Team**: [Chimeric Nano Sensor Team](https://www.cns.ac.cn/)

### Methodology Reference
The built-in model relies on the DnCNN architecture. Please also credit the original methodology:

> **Zhang, K., Zuo, W., Chen, Y., Meng, D., & Zhang, L. (2017).** Beyond a Gaussian Denoiser: Residual Learning of Deep CNN for Image Denoising. *IEEE Transactions on Image Processing*, 26(7), 3142–3155.

---
*Developed by Kui Wang © 2026. Part of the **Biosensor Tools** suite.*