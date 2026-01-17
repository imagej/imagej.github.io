---
title: WinMan
categories: [Utilities, Workflow, Interface]
icon: /media/icons/RIA-J.png
source-url: "https://github.com/Epivitae/WinMan"
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

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18224551.svg)](https://doi.org/10.5281/zenodo.18224551)

**WinMan (Window Manager & Workflow Accelerator)** is a lightweight utility designed to solve the "Desktop Explosion" problem in high-throughput microscopy workflows.

Developed by **Dr. Kui Wang** at the Center for Excellence in Brain Science and Intelligence Technology (CEBSIT), Chinese Academy of Sciences, WinMan acts as a digital housekeeper. It provides granular control over open windows, batch processing tools, and system resource monitoring with a modern, compact interface.

Author: [Kui Wang](people/Epivitae), CEBSIT, CAS. For questions please use the [GitHub Issues](https://github.com/Epivitae/WinMan/issues) or tag @Epivitae on image.sc.

## Key Features

* **Smart Filtering Engine**:
    * **Close Match**: Instantly close all windows containing a specific keyword (e.g., remove all `C1-` channels).
    * **Keep Match (Inverse Logic)**: The killer feature. Type `Final` and click **Keep Match** to close everything *except* your final results.
    * **Safety First**: "Close ALL" includes a confirmation dialog to prevent accidental data loss.
* **Batch Image Tools**:
    * **Auto Contrast All**: Applies intelligent histogram stretching (`Enhance Contrast, saturated=0.35`) to **ALL** open images instantly. Eliminates repetitive manual adjustments.
    * **Reset Zoom All**: Resets all image windows to 100% zoom level for standardized viewing.
* **System Health Monitor**:
    * Features an integrated **Memory Bar** showing live RAM usage.
    * **One-Click GC**: Clicking the memory bar triggers immediate Garbage Collection to free up system resources.

## Installation & Update

WinMan is distributed via the **Biosensor Tools** Fiji Update Site.

1.  Open **Fiji / ImageJ**.
2.  Navigate to **Help › Update...**
3.  Click **Manage update sites**.
4.  Check **Biosensor Tools** from the list.
5.  Click **Apply and Close**, then restart Fiji.

{% include notice icon="info" content="If the site is missing from the list, you can add it manually:<br>**Name:** `Biosensor Tools`<br>**URL:** `https://sites.imagej.net/Biosensor-Tools/`" %}

## Usage Guide

### 1. Filter Logic Examples

| Function | Input Example | Action | Use Case |
| :--- | :--- | :--- | :--- |
| **Close Match** | `.csv` | Closes any window with ".csv" in title. | Cleaning up intermediate data tables. |
| **Keep Match** | `Final` | Closes everything **EXCEPT** "Final" windows. | Isolating processed results for export. |
| **Close Match** | `C2-` | Closes all Channel 2 images. | Removing reference channels after alignment. |

### 2. Interface Controls

* **Window Layout**:
    * **Tile**: Arranges images in a grid without overlap (Optimized algorithm).
    * **Cascade**: Stacks images diagonally with titles visible.
* **Status Footer**: Displays operation feedback (e.g., "Closed 12 windows") and real-time Memory usage.

## Citation & DOI

If you use this software in your research, please cite the permanent Zenodo record:

Wang, K. (2026). WinMan: A Modern Window Manager and Workflow Accelerator for ImageJ/Fiji (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.18224551

* **Repository**: [https://github.com/Epivitae/WinMan](https://github.com/Epivitae/WinMan)
* **CNS Team**: [Chimeric Nano Sensor Team](https://www.cns.ac.cn/)

---
*Developed by Kui Wang © 2026. Part of the **Biosensor Tools** suite.*