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

Software citation on Zenodo:

Sorensen, L., Saito, A., Poon, S., Noe Han, M., Hamnett, R., Neckel, P, Humenick, A., Mutunduwe, K., Glennan, C., Mahdavian, N., JH Brookes, S., M McQuade, R., PP Foong, J., Gómez-de-Mariscal, E., Muñoz Barrutia, A., Kaltschmidt, J. A., King, S. K., Haase, R., Carbone, S., A. Veldhuis, N., P. Poole, D., & Rajasekhar, P. (2022). Gut Analysis Toolbox [Computer software]. Zenodo. doi: 10.5281/zenodo.6095590

To download the training data, notebooks and associated models please go to the following Zenodo link:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6096664.svg)](https://doi.org/10.5281/zenodo.6096664)

