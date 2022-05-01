---
title: CIP
categories: [Uncategorized]
---

{% capture benoalo %}{% include person id='benoalo' %}{% endcapture %}
{% include info-box software='ImageJ/Fiji' name='CIP' update-site='CIP' author=benoalo maintainer=benoalo released='January 2018' filename='CIP update site' source='https://github.com/benoalo/CIP' category='Scripting' %}

{% include img src="/media/cip-basic-concept.png" width="600" caption="**Figure 1**: CIP is a simple toolbox to learn and prototype image analysis workflow in ImageJ. It hides ImageJ complexity while making it easy to combine ImageJ packages for more specific tasks." %}

# CIP : Classic Image Processing

Classic Image Processing (CIP) is an image procesing toolbox which provides functions for scripting in ImageJ. Its principal goal is to facilitate image analysis workflow construction as well as to provide an accessible entry point to learn the programming of such workflow. CIP also has a specific focus on user experience which should appear clearly in the libraries main features:

-   **Integration** to ImageJ ecosystem: CIP can be easily used in combination other ImageJ 1.x and ImageJ2 plugins. For instance, it can process seamlessly all usual imageJ image type (ImagePlus, Dataset, ImgPlus, Img) wihtout requiring any conversion.

-   **Discoverability** of its functionnalities: CIP provides a complete user documentation that explain function usage, details their parameters and provides illustration. In order to allow an intuitive learning, function parameters can be named or made optionnal while similar functions will have similar signatures. For the same reason 2D and 3D images can be processed with the same functions.

-   **Simplicity** of use: Learning programming is demanding and CIP goal is to hide unecessary difficulty when one starts scripting. For instance CIP requires no class and package import. It Also uses only 3 main data types, Image, Region Table, to simplify data representation. Finally, CIP functions never modifies functions inputs so you always know what is happening to your data.

-   An **essential** set of tools: CIP gathers the 10% of tools that will get the job done, allowing one to go straight to the tool he needs. The function selected are also well adopted by the community to facilitate exchange and understanding. Finally, CIP provides basic visualisation and measure tools that are needed in every workflow.

# Getting started

## Installation

If you want to use CIP in ImageJ script editor, simply add the CIP update site to your imageJ installation ([instruction to follow an update site](/update-sites/following)) restart imagej, open the script editor and you are good to go. For inspiration, one can look at one of the [example scripts](/plugins/cip#script-example).

If one would like to contribute or simply toy with the source code of the library, its source code and the instruction for the project set up in an IDE can be found on the [project repository](https://github.com/benoalo/CIP).

## Documentation organisation

To build a script with CIP, follow one of the examples below or try one of the [repository](https://github.com/benoalo/CIP/tree/master/scripts%7Cproject) examples.

To get information on a function follow the link in the function table in the [categories](/plugins/cip#tools-categories) section or directly go to one of the category pages: [Format](/plugins/cip/format), [Filter](/plugins/cip/filter), [Math](/plugins/cip/math), [Segment](/plugins/cip/segmentation), [Assess](/plugins/cip/utilities).

For information on the parameters, their type, whether they are optionnal or required and more one can consult the [ Parameters](/plugins/cip/parameters) page.

# Tools categories

Image analysis workflows require the user to perform stereotypic steps: enhance signal, define and characterize region, visualize and assess results. This recurring process allows to create one function per task and to organize these functions in categories with similar roles, input and output: Format, Filter, Segment, Math, Assess.

{% include img src="cip-generic-pipeline" width="700" caption="**Figure 2**: Many analysis workflow are composed of generic tasks." %}

-   **[Format](/plugins/cip/format)**: These functions are used to managed image data, combine them or reduce their dimensionnality. They take one or multiple image as input and return one image as output. These function will generally provide an ouput which size and/or dimensionality can be different from the input

-   **[Filter](/plugins/cip/filter)**: filters act on image graylevel. They creates an output image the same size as the input. Filters are used to remove noise, filter out unwanted background or enhance feature of interest such as spots and lines.

-   **[Math](/plugins/cip/math) operations and functions**: These category gathers usual mathematical operations such as addition, subtraction or trigonometric functions for instance. They can be used with scalars, images or image and scalar in combination. When use with images the operation are applied pixel wise.

-   **[Segmentation](/plugins/cip/segmentation)**: Segmentation functions allow to define regions in an image. Applied to an input image they create so called label image that defines the pixel where the object lays. Each region is attributed a particular label, an integer value, that can be used to retrieve the object later. Watershed, thresholding spot and line detection can be found here.

-   **[Assess](/plugins/cip/utilities)**: in that category are tools to facilitate data visualisation and measures that will be needed in every pipeline once the image processing is done.

Link to function user documentation are provided in the table below.

| Filter                                     | Segmentation                                       | Format                                       | Math                                                                                                                                 | Assess                                      | Experimental                               |
|--------------------------------------------|----------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------|
| [gauss](/plugins/cip/filter#gauss)       | [threshold](/plugins/cip/segmentation#threshold) | [create](/plugins/cip/format#create)       | [add](/plugins/cip/math#binary-operator), [sub](/plugins/cip/math#binary-operator)                                               | [measure](/plugins/cip/utilities#measure) | [track](/plugins/cip/experimental#track) |
| [erosion](/plugins/cip/filter#erosion)   | [maxima](/plugins/cip/segmentation#maxima)       | [duplicate](/plugins/cip/format#duplicate) | [mul](/plugins/cip/math#binary-operator), [div](/plugins/cip/math#binary-operator)                                               | [show](/plugins/cip/utilities#show)       |                                            |
| [dilation](/plugins/cip/filter#dilation) | [watershed](/plugins/cip/segmentation#watershed) | [slice](/plugins/cip/format#slice)         | [cos](/plugins/cip/math#unary-operator), [sin](/plugins/cip/math#unary-operator), [tan](/plugins/cip/math#unary-operator)      | [region](/plugins/cip/utilities#region)   |                                            |
| [opening](/plugins/cip/filter#opening)   | [label](/plugins/cip/segmentation#label)         | [project](/plugins/cip/format#project)     | [acos](/plugins/cip/math#unary-operator), [asin](/plugins/cip/math#unary-operator), [atan](/plugins/cip/math#unary-operator)   | [toIJ1](/plugins/cip/utilities#toIJ1)     |                                            |
| [closing](/plugins/cip/filter#closing)   |                                                    |                                              | [min](/plugins/cip/math#binary-operator), [max](/plugins/cip/math#binary-operator)                                               | [toIJ2](/plugins/cip/utilities#toIJ2)     |                                            |
| [tophat](/plugins/cip/filter#tophat)     |                                                    |                                              | [pow](/plugins/cip/math#binary-operator), [sqrt](/plugins/cip/math#unary-operator)                                               | [spacing](/plugins/cip/utilities#spacing) |                                            |
| [distance](/plugins/cip/filter#distance) |                                                    |                                              | [floor](/plugins/cip/math#unary-operator), [ceil](/plugins/cip/math#unary-operator), [round](/plugins/cip/math#unary-operator) | [unit](/plugins/cip/utilities#unit)       |                                            |
| [median](/plugins/cip/filter#median)     |                                                    |                                              | [log](/plugins/cip/math#unary-operator), [exp](/plugins/cip/math#unary-operator)                                                 | [axes](/plugins/cip/utilities#axes)       |                                            |
| [invert](/plugins/cip/filter#invert)     |                                                    |                                              | [sign](/plugins/cip/math#unary-operator), [abs](/plugins/cip/math#unary-operator)                                                | [list](/plugins/cip/utilities#list)       |                                            |
|                                            |                                                    |                                              |                                                                                                                                      | [help](/plugins/cip/utilities#help)       |                                            |

# Script example

The following script shows how to segment 2d object in an image and visualize them. The workflow is illustrated in the **Figure 3**.

{% include code org='benoalo' repo='CIP' branch='master' path='wiki_examples/2D_nuclei.py' %}

{% include img src="cip-example-2d" width="800" caption="**Figure 3**: Example a workflow performing the cropping, filtering segmentation and visualisation of a 2D image. Raw data: Platynereis embryo, acquisition: Mette Handberg-Thorsager from Tomancak lab, MPI-CBG, Dresden in collaboration with Keller lab, HHMI - Janelia Research Campus" %}

The following script shows a 3d nuclei segmentation and the measure and displau of nuclei size. The workflow is illustrated in the **Figure 4**.

{% include code org='benoalo' repo='CIP' branch='master' path='wiki_examples/3D_nuclei_segmentation.py' %}

{% include img src="cip-example-3d" width="800" caption="**Figure 4**: Example a workflow performing the cropping, filtering segmentation and visualisation of a 2D image. Raw data: Platynereis embryo, acquisition: Mette Handberg-Thorsager from Tomancak lab, MPI-CBG, Dresden in collaboration with Keller lab, HHMI - Janelia Research Campus" %}

# Development plan

This section provide the main development directions as well as a list of functions that we intend to implement per category

| Filter    | Segmentation | Format      | Math                 | Assess |
|-----------|--------------|-------------|----------------------|--------|
| gradient  | skeleton     | concatenate | logic operators      |        |
| laplacian | edge         |             | comparison operators |        |
| hessian   |              |             |                      |        |
| fillholes |              |             |                      |        |

# Cite

# History

-   2017-12-20 : version 0.1.0 , first public version of CIP is made available on CIP update site. The package is still under development

-   2018-01-29 : version 0.1.1 , add a help function

-   2018-05-03 : version 0.1.2 , minimal backcompatible updates of a few functions signatures for consistency. cip.show( handle\*, region\*, ...) becomes cip.show(region\*, handle, ...), if no handle is provided region are shown on the current image. Update parameter name for create, slice and show function.

-   2018-05-28 : version 0.2.0 , tracking, watershed and maxima update
    -   add an experimental cip.track function allowing to track regions in a list of labelmap. it uses trackmate LapTracker below the hood thus allowing splitting, merging and discontinous tracks. resulting track can be visualized with cip.show both in trackscheme or hyperstack viewer.
    -   cip.watershed(img, threshold, ...) labeling is more consistant, each connected component (region) has a distinct label and region with height inferior to hMin are no displayed. This feature was added with ImgAlgo-0.1.1.jar
    -   the multiscale maxima detection was debugged and now give consistant results. It works in 2d/3d and takes into account data anisotropy. As an experiment it is possible to return multiscale maxima detection as a list of measures. multiscale maxima debugging also occured in ImgAlgo-0.1.2.jar update.
    -   corresponding documentation is on the work

-   2018-06-11 : version 0.2.1 correct a regression that prevented the visualisation of 3d regions

-   2018-06-19 : version 0.2.2 bug corrections
    -   correct a bug in median measure
    -   cip.project(...): change outputType parameter name to output
    -   cip.project(...): correct a bug preventing to use output='both'
