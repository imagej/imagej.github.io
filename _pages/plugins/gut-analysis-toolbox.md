---
title: Gut Analysis Toolbox
name: "Gut Analysis Toolbox"
description: Gut Analysis Toolbox or GAT allows the semi-automated analysis of the cells within the enteric nervous system of the gastrointestinal tract in **2D**. GAT enables quantification of enteric neurons and their subtypes in gut wholemounts. It runs in Fiji, a popular image analysis software in microscopy and uses custom deep learning models to segment cells of interest. 
categories: [Analysis,Segmentation,Neuron,Gut]
website: "https://github.com/pr4deepr/GutAnalysisToolbox"
update-site: "GutAnalysisToolbox"
team-founder: '@pr4deepr'
team-maintainer: '@pr4deepr'
source-url: https://github.com/pr4deepr/GutAnalysisToolbox
---


**Gut Analysis Toolbox** enables semi-automated analysis of the neuronal and glial distribution within the gut wall (enteric nervous system). It uses a combination of `FIJI macros`, [StarDist](https://github.com/stardist/stardist), [CLIJ](https://clij.github.io/) 
and [deepImageJ](https://deepimagej.github.io/deepimagej/) for segmentation and analysis.

{% include img align="center" name="GAT_overview" src="/media/plugins/Gut_Analysis_Toolbox/summary_figure.png" %}

Click [here to access the WIKI](https://gut-analysis-toolbox.gitbook.io/docs/) detailed instructions on how to use GAT.

You can also watch tutorials for GAT on [Youtube](https://www.youtube.com/playlist?list=PLmBt1Dumq60p4mIFT4j7TP_PVRjbO55Oi).

What you can do with GAT:
* Semi-automated analysis of number of enteric neurons: Uses pan-neuronal marker Hu or anything with similar 
 labelling
* Normalise counts to the number of ganglia.
* Count number of neuronal subtypes, such as ChAT, nNOS etc..
* Spatial analysis using number of neighboring cells.
* Calcium imaging analysis: Alignment of images and extraction of normalised traces

**Reference**

To cite GAT:

Sorensen, L., A. Humenick, S. S. B. Poon, M. N. Han, N. S. Mahdavian, R. Hamnett, E. Gómez-de-Mariscal, P. H. Neckel, A. Saito, K. Mutunduwe, C. Glennan, R. Haase, R. M. McQuade, J. P. P. Foong, S. J. H. Brookes, J. A. Kaltschmidt, A. Muñoz-Barrutia, S. K. King, N. A. Veldhuis, S. E. Carbone, D. P. Poole and P. Rajasekhar (2024). "Gut Analysis Toolbox: Automating quantitative analysis of enteric neurons." bioRxiv: 2024.2001.2017.576140.

To download the training data, notebooks and associated models please go to the following Zenodo link:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6096664.svg)](https://doi.org/10.5281/zenodo.6096664)

