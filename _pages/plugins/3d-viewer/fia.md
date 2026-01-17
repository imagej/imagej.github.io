---
title: FIA
categories: [Registration, Motion Correction, Analysis]
icon: /media/icons/FIA.png
source-url: "https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner"
update-site: "Biosensor Tools"
release-version: v3.1.0
support-status: Active
team-founders: ['@Epivitae']
team-maintainers: ['@Epivitae']
---
{%- assign github            = page.github            -%}
{%- assign release-version   = page.release-version   -%}
{%- assign release-date      = page.release-date      -%}
{%- assign dev-status        = page.dev-status        -%}
{%- unless team-maintainers  -%} {%- assign team-maintainers  = page.team-maintainer  -%} {%- endunless -%}

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18206931.svg)](https://doi.org/10.5281/zenodo.18206931)

**FIA (Fluorescence Image Aligner)** is a robust motion correction plugin designed to solve the full spectrum of motion artifacts in biological time-lapse microscopy.

Developed by **Dr. Kui Wang** at the Center for Excellence in Brain Science and Intelligence Technology (CEBSIT), Chinese Academy of Sciences, FIA bridges the gap between high-precision rigid alignment and non-rigid deformation correction. It is specialized for Calcium Imaging (G/R-CaMP), Voltage Imaging, and long-term live cell monitoring.

Author: [Kui Wang](people/Epivitae), CEBSIT, CAS. For questions please use the [GitHub Issues](https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner/issues) or tag @Epivitae on image.sc.

## Key Features

* **Dual-Engine Core**:
    * **OpenCV ECC**: Best for high-precision, sub-pixel rigid alignment (Rotation/Translation).
    * **Dense Flow (New Standard)**: State-of-the-art local deformation correction using Farnebäck optical flow. Handles internal tissue warping and soft tissue deformation better than rigid methods.
* **Scientific Integrity (Intensity Preservation)**:
    * FIA guarantees that your **ΔF/F** analysis remains valid.
    * *Navigation*: Motion vectors are calculated using noise-reduced (CLAHE), contrast-enhanced temporary frames.
    * *Transport*: These vectors are applied to your **original raw data** using cubic interpolation. No artificial contrast is written to your final image.
* **Smart "Super Reference"**:
    * In **Dense Flow** mode, FIA creates a reference anchor by averaging `N` frames. This eliminates the "floating anchor" problem caused by shot noise in single-frame references.

## Installation & Update

FIA is distributed via the **Biosensor Tools** Fiji Update Site.

1.  Open **Fiji / ImageJ**.
2.  Navigate to **Help › Update...**
3.  Click **Manage update sites**.
4.  Check **Biosensor Tools** from the list.
5.  Click **Apply and Close**, then restart Fiji.

{% include notice icon="info" content="If the site is missing from the list, you can add it manually:<br>**Name:** `Biosensor Tools`<br>**URL:** `https://sites.imagej.net/Biosensor-Tools/`" %}

## Usage Guide

### 1. Mode Selection

FIA offers three operational modes tailored to different biological samples:

| Mode | Type | Best Application |
| :--- | :--- | :--- |
| **Global** | Rigid / Affine | **General Drift Correction.** Corrects XY translation and rotation. Recommended for behaving animal tracking or whole-brain imaging. |
| **Dense Flow** | Non-Rigid (Optical Flow) | **95% of Biological Samples.** Uses *Super Reference + CLAHE*. Best for noisy fluorescence, brain slices, and in vivo imaging where local deformation occurs. |
| **Elastic** | Non-Rigid (Raw) | **High-SNR Data.** Uses raw optical flow without preprocessing. Best for binary masks, artificial beads, or clean data where contrast enhancement is unnecessary. |

### 2. Parameter Tuning

The **Smart UI** adapts based on your selected mode.

#### For Dense Flow Mode:
* **Flow WinSize**: The "field of view" for local alignment.
    * *Small (5)*: Captures fine jitter.
    * *Large (15+)*: Captures global tissue waves.
* **Ref Depth**: Number of frames averaged to create the "Super Reference" (Default: 5). Higher values reduce noise in the reference anchor.
* **Poly N**: Smoothing factor. *5* provides sharper motion borders, while *7* offers smoother flow fields but may blur distinct motion boundaries.

#### For Global Mode:
* **Max Iterations**: The loop limit for Rigid/Affine calculation.
* **Precision**: Convergence threshold (epsilon).

## Algorithms

FIA is built upon established computer vision algorithms to ensure reliability:

1.  **Non-Rigid Registration**: Based on Farnebäck's polynomial expansion (2003) combined with CLAHE (Contrast Limited Adaptive Histogram Equalization) for robustness against uneven illumination.
2.  **Rigid Alignment**: Utilizes Parametric Image Alignment using Enhanced Correlation Coefficient (ECC) Maximization (Evangelidis & Psarakis, 2008).
3.  **Legacy Stabilization**: Includes a fallback engine based on the classic Lucas-Kanade optical flow.

## Citation & DOI

If you use FIA in your research, please cite the permanent Zenodo record:

Wang, K. (2026). FIA: Fluorescence Image Aligner - Robust Motion Correction for ImageJ/Fiji (v3.1.0). Zenodo. https://doi.org/10.5281/zenodo.18206931

* **Repository**: [https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner](https://github.com/Epivitae/FIA-Fluorescence-Image-Aligner)
* **CNS Team**: [Chimeric Nano Sensor Team](https://www.cns.ac.cn/)

---
*Developed by Kui Wang © 2026. Part of the **Biosensor Tools** suite.*