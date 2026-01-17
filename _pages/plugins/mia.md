---
title: MIA
categories: [Metadata, Utilities, Analysis]
icon: /media/icons/MIA.png
source-url: "https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer"
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

[![Release](https://img.shields.io/github/v/release/Epivitae/MIA-Metadata-Inspection-Analyzer?color=blue)](https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer/releases)

**MIA (Metadata Inspection Analyzer)** is a streamlined, user-friendly ImageJ/Fiji plugin designed for instant extraction and visualization of microscopy metadata.

Developed by **Dr. Kui Wang** at the Center for Excellence in Brain Science and Intelligence Technology (CEBSIT), Chinese Academy of Sciences, it fills the gap between basic file information and complex OME-XML parsing, offering a "drag-and-drop" solution for biologists.

Author: [Kui Wang](people/Epivitae), CEBSIT, CAS. For questions please use the [GitHub Issues](https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer/issues) or tag @Epivitae on image.sc.

## Key Features

* **Instant Inspection**: Simply **drag & drop** any microscopy file to immediately view dimensions (XYZT), pixel size, and time intervals without opening the full image.
* **Deep Extraction**: 
    * **Olympus (.oir)**: Advanced parsing of proprietary tags often hidden by standard readers (e.g., Exact Laser Lines, Emission Ranges, Real-Time Intervals).
    * **General (.czi, .lif, .nd2)**: Full standard OME-XML support via Bio-Formats integration.
* **Spectrum Mapping**: Auto-generates color-coded tags for Excitation/Emission wavelengths (e.g., <span style="color:#00bdff">● Ex488</span>), making channel identification effortless.
* **One-Click Reporting**: Exports a comprehensive CSV report (Excel compatible) containing both the summary and the full raw metadata tree for data auditing.

## Installation & Update

MIA is distributed via the **Biosensor Tools** Fiji Update Site.

1. Open **Fiji / ImageJ**.
2. Navigate to **Help › Update...**
3. Click **Manage update sites**.
4. Check **Biosensor Tools** from the list.
5. Click **Apply and Close**, then restart Fiji.

{% include notice icon="info" content="If the site is missing from the list, you can add it manually:<br>**Name:** `Biosensor Tools`<br>**URL:** `https://sites.imagej.net/Biosensor-Tools/`" %}

## Usage Workflow

1. **Launch**: Start the plugin via `Plugins › Biosensor Tools › MIA`.
2. **Inspect**: Drag and drop a microscopy file (`.oir`, `.czi`, `.nd2`, etc.) directly into the panel.
3. **Review**: Check the **Key Parameters** summary for quick acquisition details.
4. **Export**: Click **"Export Report"** to save all metadata to a local CSV file for lab notebooks or publications.

## Citation & DOI

If you use this software in your research, please cite the software and the repository:

Wang, K. (2026). MIA: Metadata Inspection Analyzer - A Lightweight Metadata Extraction Tool for ImageJ/Fiji (v1.0.0). [Software]. Available at https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer

* **Repository**: [https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer](https://github.com/Epivitae/MIA-Metadata-Inspection-Analyzer)
* **CNS Team**: [Chimeric Nano Sensor Team](https://www.cns.ac.cn/)

---
*Developed by Kui Wang © 2026. Part of the **Biosensor Tools** suite developed for genetically encoded indicators and neurochemical analysis.*