---
title: Learnathon 2019
---

The third DAIS Learnathon will take place from June 23 until June 29 2019.  
You can also view the [2017 Learnathon](/events/learnathon-2017) and the [2018 Learnathon](/events/learnathon-2018) wiki pages!

## Instructors

**{% include person id='HedgehogCode' %}** *"I am currently a Working Student at KNIME working on KNIME Image Processing and KNIME Deep Learning. I did an internship in the Jug-Lab at MPI-CBG / CSBD working on a Fiji Plugin for CARE and bringing CARE to KNIME. I love Linux, Git and open-source software."*

**{% include person id='bnorthan' %}** *"I currently work as a contract Image Processing R&D Engineer. I have helped groups develop and commercialize deconvolution and single particle localization algorithms for novel instruments. I have strong ties to the open source community, and have made several contributions to ImageJ, specifically imagej-ops and imagej-tutorials. I've worked with groups such as the Open Science Foundation to develop reproducible workflows using KNIME. I'm also an adjunct instructor at the Department of Informatics, University at Albany, teaching Data Analysis using Python and KNIME."*

**{% include person id='frauzufall' %}** *"I started working as a Research Software Engineer at Florian Jug's lab, MPI-CBG, one year ago. After building interactive installations and visualizations as a freelancer I discovered the Fiji community while searching for jobs in open source development. I currently rethink the Updater, I am responsible for the CSBDeep / CARE Fiji plugin and for the IJ2 Ops part of CLIJ."*'

**{% include person id='fjug' %}** *"Florian is a group leader at the Center for Systems Biology Dresden (CSBD). His research aims at pushing the boundary of what computer vision and machine learning can do for the automated and semi-automated quantification of biological image data. Florian studied Computer Science at the TU Munich and obtained a PhD in the field of Computational Neuroscience from ETH Zurich. Next to developing novel methods for the (semi-)automated analysis of biomedical image data, his team is also critically involved in maintaining and developing the image analysis platform Fiji (www.fiji.sc)."*

**{% include person name='Florian Levett' %}** *"After working as an engineer in the Bordeaux Imaging Center, I am currently a researcher in the Sibarita lab at the Interdisciplinary Institute for Neuroscience in Bordeaux. I wrote several ImageJ plugins for segmenting or quantifying the apposition or the morphology of different kind of biological models. I also developed from scratch two platforms called SR-Tesseler and Coloc-Tesseler for quantifying single-molecule localization microscopy data."*

**{% include person id='bogovicj' %}** '*'I am a postdoc in the Saalfeld lab at Janelia, working on anatomical templates, and large scale, multimodal image registration. I am the author of the Bigwarp Fiji plugin, and contribute to imglib2 and bigdataviewer. There is lots of room in my heart for both the "new hotness" of deep learning and "old school" computer vision techniques."*

**{% include person id='maarzt' %}** *"I started developing for Fiji, about three years ago. I'm actively developing Labkit, a Fiji Plugin for easy but big data capable image segmentation. And I'm contributing to the core of ImageJ and Fiji. I'm a big fan of simple, powerful and working software. I'm happy to discuss: How to integrate whatever amazing tools you have into ImageJ / Fiji.*

**{% include person id='hanslovsky' %}** '*'I am currently a grad student in the Saalfeld lab at Janelia. I work on neuron reconstruction from electron microscopy data with machine learning and develop proof-reading and data annotation tools. I am an ImgLib2 and recent Kotlin enthusiast and enjoy writing efficient image processing and analysis software"*

**{% include person id='tibuch' %}** '*'I am a PhD student in the Jug-Lab at MPI-CBG / CSBD. I work on content-aware image restoration applications for electron microscopy data. I learned about the ImageJ-Universe via KNIME Image Processing, contributed to imagej-ops and I am a fan of BigDataViewer."*

**{% include person name='Pavel Moravec' %}** *"I am a researcher at IT4Innovations National Supercomputing Center and a member of a group working on making the ImageJ2 / Fiji run in massive parallel High-Performance Computing environments and solving issues associated with such tasks. Our group works on processing large image data, especially from light sheet microscopy data, with batch processing pipelines. For this task, we are developing the scijava-parallel library with ParallelService and an extensions to imagej-server and its clients. In future, we consider extending the ParallelService to cloud environment as well. I am also dealing with issues arising from the need to transfer data to and from the HPC environment.*"

**{% include person id='tpietzsch' %}** '*'I'm a postdoc in the Jug and Zechner labs at MPI-CBG / CSBD. I am the coauthor and maintainer of ImgLib2, BigDataViewer, BigVolumeViewer, Mastodon, etc."*

**{% include person id='haesleinhuepf' %}** '*'I'm a postdoc in Myers lab at MPI CBG / CSBD. I'm the creator of [CLIJ](https://clij.github.io). In my actual job, I develop, run and maintain custom smart microscopes on the [ClearControl](https://github.com/ClearControl) platform. Analysing images after acquistion but before writing them to disc is my thing. Our microscopes are so smart, they even use [twitter](https://twitter.com/XWingScope)."*

**{% include person id='skalarproduktraum' %}** '*'Hey there! I'm currently a PhD student at the Sbalzarini Lab at CSBD. I'm trying to bring VR to microscopy and systems biology in general, e.g. by enabling VR control of microscopes, or developing [scenery](https://github.com/scenerygraphics/scenery) and the new 3D viewer for ImageJ, [sciview](https://github.com/scenerygraphics/scenery)."*

## Schedule

See [this page](https://indico.mpi-cbg.de/event/162/timetable/#20190623)!

## Preparation

### Knowledge

We expect the course participants to be comfortable with:

1.  Using the Terminal / Unix Shell.
2.  Using Git Versioning Tool
3.  Programming Java

If you didn't use the Terminal / Unix yet. Please go through chapters 1 to 3 of this online tutorial https://swcarpentry.github.io/shell-novice/.

If you don't know git, please have a look at this tutorial: http://swcarpentry.github.io/git-novice/.

There many beginner books for Java. If you want to be well prepared, you may also want to learn about generics in Java.

### Software

**Bring your Laptop** and make sure you have a Terminal, Git, and a Java IDE (Eclipse or IntelliJ) installed.

## Monday

**9:00 - 10:00**

-   Welcome by [Florian Jug](https://twitter.com/haesleinhuepf/status/1143052112798060544) and Pavel Tomancak.
-   [Scientific speed dating](https://twitter.com/PavelTomancak/status/1143079972506128386)

**10:00 - 12:00 ImageJ2 API beating**

-   [slides](https://github.com/fiji/learnathon-2019/tree/master/ImageJ2_API_beating)
-   [Coding a ImageJ2 plugin template](https://github.com/haesleinhuepf/daisLEARNATHON2019/blob/step2_empty_workspace/src/main/java/de/mpicbg/imagej/CellCountingWorkflow.java)
-   [Coding a workflow with ImageJ2](https://github.com/haesleinhuepf/daisLEARNATHON2019/blob/what_we_did_at_dais_learnation_2019/src/main/java/de/mpicbg/imagej/CellCountingWorkflow.java)
-   [Translating a workflow to the GPU](https://github.com/haesleinhuepf/daisLEARNATHON2019/blob/step9_put_results_table/src/main/java/de/mpicbg/imagej/CellCountingWorkflow.java)

**13:00-14:00 Reading and Writing Images**

We will now use Simplified-IO, which is, as its creator Gaby Turek sais, putting lipstick on a pig. Never the less, it is very useful if you just want to open an image from disk or from some remote source. It is also useful to save TIFF files. The sole intention of this repository is to make loading and saving simple. (Yes, there are 1000 ways to open an image in ImageJ/Fiji, and this is yet another way... but since it is only wrapping other ways to open/save images, we will attempt to keep simplified-io stable even if we change what actually happens behind the scenes.)

For this little lecture our aim is to:

-   Start a new Maven project called `io-lecture` or similar.
-   Either use the POM from an earlier project of yours, or be inspired by [this page](/develop/building-a-pom)
-   If you do so, be sure that you also create folders `src/main/java` next to the new POM. Then import into your IDE (e.g. Eclipse).
-   Please update the version of the SciJava parent POM to the latest version. Find out what version this is by using [https://maven.scijava.org/#nexus-search;quick~pom-scijava](https://maven.scijava.org/#nexus-search;quick~pom-scijava).
-   You will have to add the suitable dependency to your POM in order to use Simplified-IO. The readme at [https://github.com/fiji/simplified-io](https://github.com/fiji/simplified-io) will tell you more...
-   Now please try to open the [t1-head.zip](https://imagej.nih.gov/ij/images/t1-head.zip) image and show it on your screen.
    -   How to load the image might be seen in the readme at [https://github.com/fiji/simplified-io](https://github.com/fiji/simplified-io).
    -   Soon we will learn more about how to view images, but for now you can, for example, use `ij.ui().show( "img", loadedImage )`, which is available as soon as you started an ImageJ2 via `final ImageJ ij = new ImageJ()`.
-   Just for fun you might also want to save the image you just loaded.

**14:00-14:30 Viewing Images**

Please download the [Learnathon repo](https://github.com/fiji/learnathon-2019). Or get the code [here](https://github.com/bnorthan/viewing-images-tutorial)

The images are [here](https://www.dropbox.com/sh/azrykz3bu4ymrjd/AADj1jhIPhEz5U1O6DsYIxDYa?dl=0)

Unzip and place the 'images' directory beside the learnathon-2019/ directory

Or if you cloned the 'viewing-images' repository independently, place 'images' directory 2 levels up.

Slides can be found [here](https://bnorthan.github.io/viewing-images-tutorial/slides/#/)

**15:00-16:00 ImageJ-Ops: DoG Pyramid**

[ImageJ Tutorials](https://github.com/imagej/tutorials)

[Widget-Demo](https://github.com/imagej/tutorials/tree/master/maven-projects/widget-demo) showing all different widgets for all available input @Parameters.

[DoG Pyramid example.](https://github.com/tibuch/DoG_Pyramid)

**16:00 - 16:30 Image and point transform concepts**

Concepts:

-   [pixels are not little squares](http://alvyray.com/Memos/CG/Microsoft/6_pixel.pdf)
-   "Forward" transforms apply to points, "inverse" transforms apply for images. [Here's why](https://github.com/bogovicj/transforms_tutorial/blob/5d9194e38898f942f00fe5e76dd4ca823aa6281d/resources/2019_DAIS.pdf)
-   Image cropping does not translate/move your image - respect the origin.
-   Save any transformation you apply to disk, because:
    -   You can retransform an image from the original image + transform,
    -   You can *not* get a transformation back from the transformed image.

## Tuesday

**9:00 - 12:00 ImgLib2 deep dive**

The course went through these examples: https://github.com/imglib/imglib2-introductory-workshop

**13:00 - 14:00 Viewers: Big Data Viewer**

The course went through these examples: https://github.com/bigdataviewer/bigdataviewer-workshop

**14:00 - 15:00 Viewers: SciView**

https://github.com/skalarproduktraum/sciview-tutorial

**15:00 - 16:00 Paintara Demo**

https://github.com/fiji/learnathon-2019/tree/master/paintera

## Wednesday

**9:00 - 10:30 ImgLib2: Neighborhoods and Labelings**

The course went through the last two examples in https://github.com/imglib/imglib2-introductory-workshop

**10:50 - 12:00 ROIs in ImageJ2**

Presentation & Exercises: https://github.com/maarzt/imagej-roi-course

**13:30 - 15:00 Spatial transformations with imglib2**

The course consisted of three examples of transforming points and images, as well as a demonstration of rendering transformed points as an image.

https://github.com/bogovicj/transforms_tutorial

## Thursday

**9:00 - 12:00: SciJava - Services, Plugins, Commands & Context**

The presentation and exercises can be found here: https://github.com/maarzt/imagej-scijava-course

**13:00 - 15:00: KNIME Introduction**

## Friday

**9:00 - 12:00 KNIME Image Processing Basics**

Material can be found here https://github.com/knime-ip/knip-course

**13:00 - 14:00 Imklib, Using imglib2 from Kotlin**

https://github.com/hanslovsky/imklib-tutorial

**14:00 - 15:00 SciJava Parallel Demonstration**

https://github.com/fiji-hpc/scijava-parallel

**15:00 - 16:00 Update Sites**

[How to set up and populate an update site](/update-sites/setup)
