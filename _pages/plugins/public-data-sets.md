---
mediawiki: Public_data_sets
title: Public data sets
categories: [Example Data,Segmentation,Tracking]
---

Do you need image data to try your algorithms on? Do you lack expert ground truth to test your methods? No problem! Here you have a list of available public data sets from the Fiji community and other sources:

-   [Segmented anisotropic ssTEM dataset of neural tissue](http://figshare.com/articles/Segmented_anisotropic_ssTEM_dataset_of_neural_tissue/856713)


We provide two image stacks where each contains 20 sections from serial section Transmission Electron Microscopy (ssTEM) of the Drosophila melanogaster third instar larva ventral nerve cord. Both stacks measure approx. 4.7 x 4.7 x 1 microns with a resolution of 4.6 x 4.6 nm/pixel and section thickness of 45-50 nm.

<!-- -->


In addition to the raw image data, we provide for the first stack a dense labeling of neuron membranes (including orientation and junction), mitochondria, synapses and glia/extracellular space. The first stack serves as a training dataset, and a second stack of the same dimension can be used as a test dataset.

<!-- -->


All the data and further information is available in the {% include github org='unidesigner' repo='groundtruth-drosophila-vnc' label='GitHub repository' %}.

-   [Segmented ssTEM stack of neural tissue](http://www.ini.uzh.ch/~acardona/data.html), thanks to Albert Cardona.

![](/media/plugins/trakem2-tree-datastructure.png) ![](/media/trakem2-display-s.jpg)


30 sections from a serial section Transmission Electron Microscopy (ssTEM) data set of the Drosophila first instar larva ventral nerve cord (VNC). The microcube measures 2 x 2 x 1.5 microns approx., with a resolution of 4x4x50 nm/pixel.

**The challenge**: use this data set to train machine learning software for the purpose of automatic segmentation of neural structures in ssTEM. More information in the [ 2012 open competition page](/events/isbi-2012-segmentation-challenge).

<!-- -->


The images are representative of actual images in the real-world: there is a bit of noise; there are image registration errors; there is even a small stitching error in one section. None of these led to any difficulties in the manual labeling of each element in the image stack by an expert human neuroanatomist. A software application that aims at removing or reducing human operation must be able to cope with all these issues.

<!-- -->


See other [manually segmented serial section TEM data sets.](http://www.incf.org/about/nodes/switzerland/data)

-   [Sample data at LOCI](http://loci.wisc.edu/software/sample-data), in a variety of file formats.

<!-- -->

-   [Sample OME-TIFF data on openmicroscopy.org](http://www.openmicroscopy.org/site/support/file-formats/ome-tiff/ome-tiff-data), thanks to Josh Bembenek.<img src="/media/plugins/tubhiswt4d.png" title="fig:C. elegans embryo coexpressing tubulin histone GFP" width="140" alt="C. elegans embryo coexpressing tubulin histone GFP" />


The dataset consists of tubulin histone GFP coexpressing *C. elegans* embryos. All image planes were collected at 512x512 resolution in 8-bit grayscale.

-   [Migrating macrophages](https://fiji.sc/datasets/migrating-macrophages.tif.tar.bz2) in response to stimuli.


4D data set, kindly provided by Dirk Sieger and [Francesca Peri](http://www.embl.de/research/units/dev_biology/peri/), EMBL.<img src="/media/plugins/migrating-macrophages.gif" title="fig:Macrophages in 4D" width="140" alt="Macrophages in 4D" />

**The challenge**: trace the macrophages in 4D, and measure their shape volumes, surfaces, positions and pixel value intensities.

The file is a tif hyperstack that can be loaded directly into the [3D Viewer](/plugins/3d-viewer).

The key idea is to setup the tracking system so that it requires minimal user interaction, and is general. For example, a user clicks on one cell in one time point, and the program should find all other time points of the same cell. Then the program should learn about the statistics of that cell, and offer the means to automatically find all other cells in the volume and track them as well. In summary, a machine learning approach to 4D tracking.

-   [The Cell Image Library](http://www.cellimagelibrary.org/) has many images related to cell biology; the images come with one of 4 licenses: Public Domain, Creative Commons Attribution, Creative Commons Attribution Non-Commercial Share-Alike, and Copyrighted (you need to ask the contributor whether you may use their image explicitly). This website allows you to contribute your own data sets, too!

<!-- -->

-   [Open Connectome Project](http://openconnectomeproject.org/) hosts a 10 terabyte data set of the [mouse visual cortex](http://openconnectomeproject.org/catmaid/?pid=4&zp=45&yp=268892&xp=256060&sid0=4&s0=8) ([Bock et al., 2011](http://www.nature.com/nature/journal/v471/n7337/full/nature09802.html)) with [CATMAID](http://www.catmaid.org/), and will offer means to run arbitrary programs on the data very soon.

<!-- -->

-   [A 3D electron microscopy dataset of rodent brain](https://www.epfl.ch/labs/cvlab/data/data-em/), courtesy of [Graham Knott](http://people.epfl.ch/graham.knott) and Marco Cantoni at EPFL. In particular, a FIBSEM volume measuring 5x5x5 micrometers and taken from the CA1 hippocampus region of the brain, and imaged at the extraordinary resolution of 5x5x5 nanometers per voxel! In addition, Aurelien Lucchi from [Pascal Fua](http://people.epfl.ch/pascal.fua/bio?lang=en)'s lab has made available, in the same page, image volumes containing labels for mitochondria.

<!-- -->

-   [Broad Bioimage Benchmark Collection](http://www.broadinstitute.org/bbbc/): annotated biological image sets for testing and validation. Collection of freely downloadable microscopy image sets. In addition to the images themselves, each set includes a description of the biological application and some type of "ground truth" (expected results).
