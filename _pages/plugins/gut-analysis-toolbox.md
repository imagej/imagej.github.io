---
title: Gut Analysis Toolbox
description: Gut Analysis Toolbox or GAT allows the semi-automated analysis of the cells within the enteric nervous system of the gastrointestinal tract in **2D**. GAT enables quantification of enteric neurons and their subtypes in gut wholemounts. It runs in FIJI, a popular image analysis software in microscopy and uses deep learning models to segment cells of interest. 
categories: [Analysis,Segmentation,Neuron,Gut]
---

**Gut Analysis Toolbox** enables semi-automated analysis of the neuronal and glial distribution within the gut wall (enteric nervous system). It uses a combination of `FIJI macros`, [StarDist](https://github.com/stardist/stardist) 
and [deepImageJ](https://deepimagej.github.io/deepimagej/) under the hood to do the heavy lifting with automated segmentation. 

<p align="center">
<img src="https://github.com/pr4deepr/GutAnalysisToolbox/blob/main/wiki_images/figures/summary_figure.png" alt="GAT_overview" width="600" >
</p>

A detailed how to use instructions with wiki is available here: https://github.com/pr4deepr/GutAnalysisToolbox/wiki

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

Luke Sorensen, Ayame Saito, Sabrina Poon, Myat Noe Han, Adam Humenick, Keith Mutunduwe, Christie Glennan, Narges Mahdavian, Simon JH Brookes, Rachel M McQuade, Jaime PP Foong, Sebastian K. King, Estibaliz Gómez-de-Mariscal, Robert Haase, Simona Carbone, Nicholas A. Veldhuis, Daniel P. Poole, & Pradeep Rajasekhar (2022). Gut Analysis Toolbox (1.0.0). Zenodo. https://doi.org/10.5281/zenodo.6095590

To download the training data, notebooks and associated models please go to the following Zenodo link:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6096664.svg)](https://doi.org/10.5281/zenodo.6096664)

