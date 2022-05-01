---
title: 2010-12-26 - ImageJ2 status update
---

The following is a status update on the [ImageJ2](/software/imagej2) project as of 26 December 2010.

{% include img align="right" src="/media/news/ij2-gui-ij1-plugins.png" caption="**ImageJ2 user interface with discovered plugins**: We have created a very simple Swing user interface, with menus populated with both IJ1 and IJ2 plugins loaded using the new plugin discovery mechanism. (We will address the out-of-order menus very soon.)" %}

{% include img align="right" src="/media/news/ij2-gui-open-dialog.png" caption="**ImageJ2 user interface loading data**: The new interface invokes an IJ2 plugin to load images." %}

{% include img align="right" src="/media/news/ij2-gui-image-window.png" caption="**ImageJ2 user interface displaying an image**: The new interface displays the image in a simple N-dimensional image browser." %}

### Core ImageJDev work

#### Unit tests

We have created {% include github org='imagej' repo='ij1-tests' label='extensive unit tests' %} for approximately 40 of ImageJ's core classes. These tests are useful for verifying that new versions of ImageJ still perform identically to previous versions. The tests are fully automated, and run whenever we make a change to the ImageJ codebase, via our [Hudson continuous integration system](/develop/travis).

#### ImageJ2 architecture

We have designed initial versions of several aspects of the ImageJ2 architecture, including the [image data model](/libs/imagej-common), and [IJ2 plugin architecture](/develop/architecture#extensibility). At this point, everything is completely subject to change, with many things not yet ready for public review.

#### ImageJ2 user interface

Though our eventual goal is to create a [rich ImageJ client application](/develop/architecture#modularity) using the NetBeans RCP, for the time being we have created a barebones, proof-of-concept user interface to test the feasibility of the current architecture.

### Spectral lifetime visualization

We are actively developing tools for working with combined spectral-lifetime (SLIM) image data. This type of data is a perfect use case for extending ImageJ beyond 5D. Currently, we have a [SLIMPlugin](/plugins/slim-curve) for performing single- and double-exponential curve fits on binned lifetime data.

### Integrating web applications with ImageJ

Web tools and {% include wikipedia title='Cloud computing' text='cloud computing'%} are rapidly becoming more powerful and have many advantages versus traditional desktop applications. We want to leverage such tools where appropriate, and are exploring ways to integrate such web-based software with the ImageJ client application. Currently we have two such plugins: {% include github org='imagej' repo='workflow-pipes' label='Work Flow Pipes' %} and a [Deep Zoom plugin](/plugins/deep-zoom).

### OpenCL-based image processing

We spent some time exploring how to integrate GPU processing with Java, with the ultimate goal of enabling use of multi-core OpenCL programs from ImageJ. At the moment, we have created a {% include github org='uw-loci' repo='opencl-demo' label='web-services-based OpenCL plugin' %} that performs 3D iterative deconvolution.

 
