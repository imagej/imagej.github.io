---
title: VTEA › Volumetric Tissue Exploration and Analysis
categories: [Segmentation,Visualization]
doi: 10.1681/ASN.2016091027
name: VTEA
source-url: https://github.com/icbm-iupui/volumetric-tissue-exploration-analysis
dev-status: v0.7, alpha, 1.0.a on deck.
team-developer: Seth Winfree | mailto:swinfree@unmc.edu
team-maintainer: Seth Winfree | mailto:swinfree@unmc.edu
---

# Volumetric Tissue Exploration and Analysis

**Three-dimensional tissue cytometry.** Three-dimensional tissue cytometry(3DTC) enables the quantitative measurement of whole cells while retaining their morphology, localization and associations-think of it as *in situ* flow cytometry. 

**VTEA is:**

**Free and easy to get.** We opted to use ImageJ/Fiji as the distribution platform because it has an excellent and robust community of contributors. Practically, it provides the mechanisms for updating, a number of image processing tools and is built on a simple and powerful extensible framework.

**Easy to use.** We designed VTEA to organize the most common workflow in 3DTC inclusive of image processing (to manage imaging artifacts), segmentation (extensible to bring in edge deep learning approaches into a common framework of analysis) and exploration and analysis with flow cytometry like plots, gating, subgating, mapping to image with ROI gating and tools for high dimensionality data and neighborhood analysis.

**Mesoscale 3D analysis.** We built VTEA to handle massive datasets and to operate seamlessly on an embedded database to enable analysis of >500 thousand cells (hardware limits do apply).

**Supervised and unsupervised cell classification.**  VTEA supports flow cytometry-like gating and subgating and incorporates tools for clustering and dimensionality reduction to facilitate cell classification.  Cell classifaction can include both computationally defined and expert labeled cells via imagej ROIs.  

**Neighborhood construction and analysis.**  Once cell classfication/labels are defined they may be used in a neighborhood analysis including that same tools used in VTEA for supervised and unsupervised classification and labeling of neighborhoods based on the label distributions per neighborhood (sum and fraction of total).

**Original image referencing.** The power of 3DTC in VTEA enables the localization of identified cells in the analysis space in the original image, *in situ*, and in 3D with [ClearVolume](/plugins/clearvolume).

**Extensibility.** Importantly, our solution is in its infancy. These first iteration of VTEA represent the beginning of our vision for VTEA. We  currently leverage the SciJava framework to make VTEA easily extensible and continue to build both upon existing tools in ImageJ/Fiji and our own novel approaches.

This brief [video](/media/plugins/demostration.mov) describes VTEA's core behaviors. 

We developed VTEA out of a need to unify the various tasks involved in image processing, segmenting, exploring and analyzing large 3D fluorescence light microscopy image volumes ranging from 50-100s of microns thick. Our solution is predicated upon the idea that *image processing, segmentation and analysis of 3D image volumes is best implemented with a bidirectional interactive user interface from image processing to analysis*.

## Installing

`   To install the VTEA plugin use, `[`How`` ``to`` ``follow`` ``a`` ``3rd`` ``party`` ``update`` ``site`](/update-sites/following)` and check the update site:`  
`   "Volumetric Tissue Exploration and Analysis"

## Tutorials

Please visit the new [wiki](https://vtea.wiki)!

## VTEA references

Examples of VTEA use in manuscripts:

1. Lake BB, Menon R, Winfree S, et al. An Atlas of Healthy and Injured Cell States and Niches in the Human Kidney. Genomics; 2021. [doi:10.1101/2021.07.28.454201](https://doi.org/10.1101/2021.07.28.454201)
2. Ferkowicz MJ, Winfree S, et al. for the Kidney Precision Medicine Project. Large-scale, three-dimensional tissue cytometry of the human kidney: a complete and accessible pipeline. Lab Invest. 2021;101(5):661-676. [doi:10.1038/s41374-020-00518-w](https://doi.org/10.1038/s41374-020-00518-w)
3. Black LM, Farrell ER, Barwinska D, et al. VEGFR3 tyrosine kinase inhibition aggravates cisplatin nephrotoxicity. Am J Physiol-Ren Physiol. 2021;321(6):F675-F688. [doi:10.1152/ajprenal.00186.2021](https://doi.org/10.1152/ajprenal.00186.2021)
4. Black LM, Winfree S, Khochare SD, et al. Quantitative 3-dimensional imaging and tissue cytometry reveals lymphatic expansion in acute kidney injury. Lab Invest. 2021;101(9):1186-1196. [doi:10.1038/s41374-021-00609-2](https://doi.org/10.1038/s41374-021-00609-2)
5. Varberg KM, Winfree S, Chu C, et al. Kinetic analyses of vasculogenesis inform mechanistic studies. Am J Physiol-Cell Physiol. 2017;312(4):C446-C458. [doi:10.1152/jpcell.00367.2016](https://doi.org/10.1152/jpcell.00367.2016)
6. Makki MS, Winfree S, Lingeman JE, et al. A Precision Medicine Approach Uncovers a Unique Signature of Neutrophils in Patients With Brushite Kidney Stones. Kidney Int Rep. 2020;5(5):663-677. [doi:10.1016/j.ekir.2020.02.1025](https://doi.org/10.1016/j.ekir.2020.02.1025)
7. Woloshuk A, Khochare S, Almulhim AF, et al. In Situ Classification of Cell Types in Human Kidney Tissue Using 3D Nuclear Staining. Cytometry A. 2021;99(7):707-721. [doi:10.1002/cyto.a.24274](https://doi.org/10.1002/cyto.a.24274)

The original VTEA was demonstrated in the following publication:

{% include citation %}
