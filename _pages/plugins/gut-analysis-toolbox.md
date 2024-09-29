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
* Semi-automated analysis of enteric neuronal distribution: Uses pan-neuronal marker Hu or any marker with similar 
 labelling
* Normalise counts to the number of ganglia.
* Count number of neuronal subtypes, such as ChAT, nNOS etc..
* Spatial analysis with number of neighboring cells.
* Calcium imaging analysis: Alignment of images and extraction of normalised traces
* Multiplex image registration

**Reference**

To cite GAT:

Luke Sorensen, Adam Humenick, Sabrina S. B. Poon, Myat Noe Han, Narges S. Mahdavian, Matthew C. Rowe, Ryan Hamnett, Estibaliz Gómez-de-Mariscal, Peter H. Neckel, Ayame Saito, Keith Mutunduwe, Christie Glennan, Robert Haase, Rachel M. McQuade, Jaime P. P. Foong, Simon J. H. Brookes, Julia A. Kaltschmidt, Arrate Muñoz-Barrutia, Sebastian K. King, Nicholas A. Veldhuis, Simona E. Carbone, Daniel P. Poole, Pradeep Rajasekhar; Gut Analysis Toolbox: Automating quantitative analysis of enteric neurons. J Cell Sci 2024; jcs.261950. doi: https://doi.org/10.1242/jcs.261950

To download the training data, notebooks and associated models please go to the following Zenodo link:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6096664.svg)](https://doi.org/10.5281/zenodo.6096664)

