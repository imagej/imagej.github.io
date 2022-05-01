---
mediawiki: TAPAS
title: TAPAS
categories: [Automation,Analysis,Filtering,Segmentation]
---


{% capture author%}
{% include person id='mcib3d' %}
{% endcapture %}

{% capture source%}
{% include github org='mcib3d' repo='tapas-core' %}
{% endcapture %}
{% include info-box name='TAPAS' software='tapas' update-site='TAPAS' author=author maintainer=' [Thomas Boudier](https://github.com/mcib3d)' source=source released='14/08/2019, V0.4' latest-version='22/06/2020, V0.6.3' status='stable, active' category='Automation, Analysis, Filtering, Segmentation' %}

## TAPAS : An integrated tool for batch processing

Updated content will be available at [Framagit](https://mcib3d.frama.io/tapas-doc/).

**TAPAS** (Towards an Automated Processing and Analysis System) is a framework for processing and analysis workflow for multi-dimensional images. A workflow is a series of modules linked together to process an image, each module should perform one simple task.

The first idea is to design a framework where **users** can share the pipeline as simple text file. The second idea is to create a simple programming template so **developers** can create their own module.

Finally, the pipeline should be separated from the set of images to process, so a same pipeline can be used for different images. The results of the processing and the analysis should be stored along with the processed images.

Here we propose modules to process and analyze images stored in an OMERO database, but the system should work fine with files stored locally or on a server.

## Author

Thomas Boudier

## Features

Basically we will propose modules from the [3D\_ImageJ\_Suite](/plugins/3d-imagej-suite), ImageJ/Fiji, along with other modules.

As for stable version 0.5 the following modules are available :

-   Input/Output to files (using BioFormats)
-   Input/Output to OMERO
-   2D/3D filtering
-   Auto-threshold, hysteresis and Iterative thresholding
-   2D/3D labeling
-   Objects measurements, signal quantification and numbering
-   Colocalisation and distances
-   Calling ImageJ macros and executables

## Installation

-   Install [ImageJ](https://imagej.nih.gov/ij/) or [Fiji](http://fiji.sc/).

<!-- -->

-   Install [3D\_ImageJ\_Suite](/plugins/3d-imagej-suite). It is also available as a update site in Fiji. **ImageScience** should be installed too, either from [here](http://www.imagescience.org/meijering/software/featurej/) or via the update site in Fiji.

<!-- -->

-   Install **Bioformats**, either by downloading [bioformats\_package.jar](https://www.openmicroscopy.org/bio-formats/downloads/) or by enabling the update site in Fiji.

<!-- -->

-   If you have an OMERO server, download [OMERO-insight](https://www.openmicroscopy.org/omero/downloads/), unzip OMERO.insight-ij-xxx.zip into the plugins directory of ImageJ or Fiji. The version number should match the version number of your server. Please do not install OMERO-insight from the Fiji update site.

<!-- -->

-   Download ![](/media/plugins/bundle-tapas0.6.3.zip) and unzip it into the ImageJ or Fiji directory.

TAPAS was tested successfully with OMERO.insight 5.5.5 and Bioformats 6.0.1.

## Usage / Tutorials

-   If you want to process data stored on an Omero server, connect first to your server using **TAPAS Connect** inside the TAPAS menu.

<!-- -->

-   **Create your pipeline** in a text editor, check available tapas modules and how to use it in the documentation provided.

<!-- -->

-   Run *TAPAS OMERO* if you want to process data from Omero or *TAPAS FILES* for data on files.

A list of tutorials :

-   Basic **Input/Ouptput** functionalities [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/input_output_i/start).
-   Create your first **processing pipeline** [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/create_your_processing_pipeline/start).
-   **Segmentation** modules [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/segmentation/start).
-   **Measurement** modules [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/measurement/start).
-   **Signal quantification** and **numbering** modules [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/signal_quantification/start).
-   **Co-localisation** [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/colocalisation/start).
-   How to use the **analyzeParticles** module for segmentation and measurement [here](https://imagejdocu.list.lu/plugin/utilities/tapas_tutorial/2d_measurements_with_analyze_particles/start).
-   How to quantify **layers distribution** [here](https://imagejdocu.list.lu/plugin/utilities/layers_analysis/start).

The list of available modules is described in [Tapas description0.6.3.pdf](/media/plugins/tapas-description0.6.3.pdf).

## Citation

2018 Whitehead, L., Wimmer, V., Lafouresse, F., Ratnayake, D., Currie, P., Groom, J., Rogers, K. and Boudier, T. Towards an Automated Processing and Analysis System for multi-dimensional light-sheet microscopy big data using ImageJ and OMERO. International Microscopy Congress IMC 19. ([Abstract 1848 thomasboudier.pdf](/media/plugins/abstract-1848-thomasboudier.pdf))

Gilles JF and Boudier T. TAPAS: Towards Automated Processing and Analysis of multi-dimensional bioimage data. F1000Research 2020, 9:1278 [doi](https://doi.org/10.12688/f1000research.26977.1)

## License

Version 0.5 and later are under GPL distribution (see [license](http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html)).

Source code is available on **github** : [tapas-core](https://github.com/mcib3d/tapas-core), [tapas-plugins](https://github.com/mcib3d/tapas-plugins).

## Change log

-   22/06/2020 V0.6.3 : new modules (CLIJFilters, EDT+EVF, localThickness, CloseLabels). Changed ?name? by ?image?. Generic image processing, default is ImagePlus.Folder *attachments* for TAPAS-FILES.
-   19/09/2019 V0.51 : minor change, new module load attachment from Omero
-   29/08/2019 V0.5 : stable version. New modules (see list)
-   06/05/2019 V0.41beta : fix bug in input/output on Windows
-   05/03/2019 V0.4beta : channels and frames now start at 1, new binning option in Omero Load, module 3dfilters is renamed filters and has parameter radxy (instead of radx and rady), new tutorials on measurements and quantification
-   01/02/2019 V0.3beta : first beta release
