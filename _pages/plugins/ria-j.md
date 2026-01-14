---
title: RIA-J
categories: [Analysis, Visualization]
icon: /media/icons/RIA-J.png
source-url: "https://github.com/Epivitae/RIA-J"
update-site: "RIA-J"
release-version: v2.0.0
support-status: Active
team-founders: ['@Epivitae']
team-maintainers: ['@Epivitae']
---
{%- assign github            = page.github            -%}
{%- assign release-version   = page.release-version   -%}
{%- assign release-date      = page.release-date      -%}
{%- assign dev-status        = page.dev-status        -%}
{%- unless team-maintainers  -%} {%- assign team-maintainers  = page.team-maintainer  -%} {%- endunless -%}

**RIA-J (Ratio Imaging Analyzer - Java Edition)** is a lightweight, high-performance ImageJ/Fiji plugin designed for interactive ratiometric fluorescence analysis. 

Developed by **Kui Wang** at the Center for Excellence in Brain Science and Intelligence Technology (CEBSIT), Chinese Academy of Sciences, it serves as the native Java counterpart to the Python-based RIA software.

Author: Kui Wang, CEBSIT, CAS. For questions please use the [GitHub Issues](https://github.com/Epivitae/RIA-J/issues) or tag @Epivitae on image.sc.

## Key Features

* **Interactive Swing Dashboard**: A non-modal control panel that allows for real-time parameter tuning (background subtraction, thresholding) without blocking the image view.
* **Smart Masking**: Implements dynamic `NaN` thresholding in the denominator channel to eliminate noise and division artifacts.
* **Scientific-Grade Processing**: Supports **Normalized Convolution**, a technique used to smooth signals while correctly handling boundaries, avoiding the "dark halo" artifacts common with standard Gaussian blurs.
* **Batch Engine**: Efficient "Apply to Stack" functionality for processing high-dimensional time-lapse (T-series) or Z-stack data.
* **Integrated Visualization**: Automated scientific LUT application (Fire, Ice, Spectrum) and calibration bar generation.

## Installation & Update

RIA-J is distributed via an official Fiji Update Site.

1. Open **Fiji / ImageJ**.
2. Navigate to **Help › Update...**
3. Click **Manage update sites**.
4. Check **RIA-J** from the list.
5. Click **Apply and Close**, then restart Fiji.

{% include notice icon="info" content="If the site is missing from the list, you can add it manually:<br>**Name:** `RIA-J`<br>**URL:** `https://sites.imagej.net/RIA-J/`" %}

## Usage Workflow

1. **Initialize**: Open your dual-channel image and click **"Import / Refresh Images"** in the RIA-J panel.
2. **Tune**: Adjust the **Background** and **NaN Threshold** sliders while observing the real-time preview.
3. **Refine**: (Optional) Apply **Normalized Convolution** for edge-aware smoothing.
4. **Export**: Click **"Apply to Stack"** to generate the final ratiometric result.

## Citation & DOI

If you use this software in your research, please cite the permanent Zenodo record:

{% include citation
   text="Wang, K. (2026). RIA-J: Ratio Imaging Analyzer (Java) - Interactive Ratiometric Analysis for ImageJ/Fiji. Zenodo."
   doi="10.5281/zenodo.18200077"
%}

* **Repository**: [https://github.com/Epivitae/RIA-J](https://github.com/Epivitae/RIA-J)

---
*Developed by Kui Wang © 2026. Part of the development for genetically encoded indicators, including GEM-CPPU1.0 and phosphate (Pi) probes.*