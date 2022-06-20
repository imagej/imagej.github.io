---
title: Java Image Processing Pipeline (JIPipe)
description: Object-detection with one or multiple template images
categories: [Scripting]
icon: /media/icons/jipipe.svg


name:  JIPipe
source-url: https://github.com/applied-systems-biology/jipipe
release-date: 2022

license-url: /licensing/bsd
license-label: BSD 2-clause

team-founders: Ruman Gerst, Zoltan Cseresnyes, Marc Thilo Figge
---

{% include img name="JIPipe-GUI" src="/media/plugins/jipipe-algorithm-finder.png" %}

# About 

The **J**ava **I**mage **P**rocessing P**ipe**line (JIPipe) is a [visual programming language](https://en.wikipedia.org/wiki/Visual_programming_language) based on ImageJ that aims to simplify the creation of macros with familiar ImageJ functionality. 

Its features include ...

* Over 1000 functions from ImageJ and popular plugins encapsulated into nodes
  * Manually curated
    * Core [ImageJ1](https://imagej.net/software/imagej/) data types (Images, ROIs, tables) and filters/operations
    * [MorphoLibJ](https://imagej.net/plugins/morpholibj)
    * [FeatureJ](https://imagej.net/libs/imagescience)
    * [OMERO](https://imagej.net/software/omero) (basic functionality)
    * [Multi-Template Matching](https://imagej.net/plugins/multi-template-matching)
  * Automated integration
    * [CLIJ2](https://imagej.net/plugins/clij) functions
    * [ImageJ2](https://imagej.net/software/imagej2/index) operations (via IJ2 Ops)
  * Additional functionality
    * Deep learning via [Cellpose](https://www.cellpose.org/) (prediction + training) (see [documentation](https://www.jipipe.org/documentation/standard-library/cellpose/))
    * Interactive forms (interactivity during manual analyses)
    * Macro and Jython nodes (see [documentation](https://www.jipipe.org/documentation/standard-library/macro-node/))
    * Plots via [JFreeChart](https://www.jfree.org/jfreechart/) (see [documentation](https://www.jipipe.org/documentation/standard-library/plots-tables/))
    * Python and R via an environment system (dedicated processes; see [documentation](https://www.jipipe.org/documentation/standard-library/python/))
* [Symbiotic relationship](https://www.jipipe.org/documentation/imagej-integration/) with ImageJ: ImageJ can execute JIPipe nodes via macros/GUI (data transfer between JIPipe <-> ImageJ is extensible via plugins)
* [Graph compartmentalization](https://www.jipipe.org/documentation/create-pipelines/compartments/) to structure pipelines and make them easier to read
* Standardized [data format](https://www.jipipe.org/documentation-data-api/) for automated saving and loading results (currently file-based; API for alternative storage backends is [available](https://www.jipipe.org/apidocs/org/hkijena/jipipe/api/data/storage/package-summary.html))
* Table-based [data management](https://www.jipipe.org/documentation/basic-concepts/batch-processing/) (constrained tables to simplify the automated data processing)
* Mathematical [expression language](https://www.jipipe.org/documentation/create-pipelines/expressions/) utilized in various nodes for customization
* Supports both memory-efficient [full pipeline runs](https://www.jipipe.org/documentation/run-pipelines/run/) and [data caching](https://www.jipipe.org/documentation/run-pipelines/cache/) for semi-interactive workflow
* Project format that tracks all dependencies (ImageJ update sites, JIPipe plugins), including authors
* Documentation features to aid with the readability of pipelines and simplify the usage in teaching environments
  * Freely customizable node names and HTML descriptions
  * Comment nodes to highlight specific areas
  * Bookmarks
  * Node templates (store a set of nodes for re-use inside the project or globally) 
  * Graph permissions (e.g., prevent the deletion of nodes)
  * "Project overview" screen with a custom HTML description, list of bookmarks and configurable list of parameter references, author metadata and citations
* Java API for custom plugins (via SciJava plugin interface) (see [documentation](https://www.jipipe.org/documentation-java-api/))
* GUI editor for custom nodes (convert any pipeline into a node, creating plugin in JSON format; see [documentation](https://www.jipipe.org/documentation/create-json-extensions/))

# Installation

Activate the `JIPipe` update site and restart ImageJ. Navigate to *Plugins > JIPipe > JIPipe GUI* to start JIPipe.
On the first start, you will likely get prompted to install missing dependencies. Click *Resolve* and follow the instructions.

We also provide additional downloads, including pre-made packages for Windows and Linux, as well as the *.jar files including dependencies [on our website](https://www.jipipe.org/download/)

# Documentation

Please visit [https://www.jipipe.org/](https://www.jipipe.org/) for (video-)tutorials and documentation.

We published multiple example projects that analyze real bioimage data sets [on our website](https://www.jipipe.org/examples/), including ...

* The automated quantification of phagocytic measurements from confrontation assays of alveolar macrophages and fungi (Classical image analysis)
* Detection of bacterial growth inside picoliter microfluidic droplets (Classical + deep learning via Cellpose)
* Quantification of glomeruli in 3D light-sheet fluorescence microscopy data of murine kidneys (example data was reduced to 20 slices from 700)
* Measuring the delivery of nanoparticles into liver cells
* Training of a Cellpose-based deep learning model to automatically segment tissue in multispectral optoacoustic tomography (MSOT) data
* Quantification of toxicity to nematodes via overlap tracking

# Citations
{% include citation doi='10.5281/zenodo.6532719' %}

# Video Tutorials

{% include video platform="youtube" id="PL-b5b09600_mCAZ8ex5ded29YxMttxFL6" %}

# Similar tools

* [KNIME](https://www.knime.com/)
* [Icy protocols](https://icy.bioimageanalysis.org/)
