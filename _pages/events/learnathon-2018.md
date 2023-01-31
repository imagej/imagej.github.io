---
title: Learnathon 2018
---

The second DAIS Learnathon took place from June 3 until June 9 2018.  
[This page](learnathon-2017) is the Learnathon Wiki page of last year's event!

## Schedule

See [this page](https://indico.mpi-cbg.de/event/50/other-view?view=standard)!

## Setting up your system

Check if you have this set up:

-   Eclipse (Neon)
-   bash / zsh
-   GIT
-   Maven
-   Gitter

## Monday

### Intro session...

See [slides](https://frauzufall.github.io/imagej-universe-intro/)!

### Start a Maven project with Eclipse

See [slides](https://github.com/fiji/learnathon-2018/blob/master/Start%20a%20Maven%20Project.pdf)

Git repos to clone:

-   `git@github.com:imagej/example-imagej-command.git`

Notes: In case you want to switch to the legacy UI (ImageJ 1), you change the dependencies section in your POM to...

```xml
<dependencies>
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>imagej</artifactId>
    </dependency>
    <dependency>
        <groupId>net.imagej</groupId>
        <artifactId>imagej-legacy</artifactId>
    </dependency>
</dependencies>
```

### Introduction to ImgLib2

Git repos to clone:

-   [`https://github.com/imglib/imglib2-introductory-workshop.git`](https://github.com/imglib/imglib2-introductory-workshop.git)

([Slides](https://github.com/imglib/imglib2-introductory-workshop/blob/master/Introduction-ImgLib2.pdf) are contained in the repository.)

## Tuesday

### ImageJ2 and SciJava

-   Search for stuff in our ecosystem: [https://search.imagej.net](https://search.imagej.net)
-   [SciJava and ImageJ Ops Jupyter notebook / slides](https://github.com/fiji/learnathon-2018/blob/master/SciJava%20and%20ImageJ%20Ops.ipynb)
-   [Slides from last year's Learnathon about SciJava community](/presentations/2017-06-19-dais-learnathon/)
-   [Developing ImageJ in Eclipse](/develop/eclipse)

### ImageJ2 Ops

-   [ImageJ2 Tutorial Notebooks](/tutorials/notebooks)

### ImageJ Legacy

The ImageJ Legacy Course covered the topics: images, tables, regions of interest and command execution.

-   [ImageJ Legacy Exercises (Slides Included)](https://github.com/maarzt/imagej-legacy-course)
-   Last years [cheatsheet](https://github.com/maarzt/imagej-legacy-course/blob/master/slides/ij_legacy_cheetsheet.pdf)
-   Last years course [Slides](https://github.com/mpicbg-scicomp/ij2course-images/blob/master/slides/ij_legacy.pdf) [Old Exercise 1](https://github.com/mpicbg-scicomp/ij2course-images) [Old Exercise 2](https://github.com/mpicbg-scicomp/ij2course-regions) [Old Exercise 3](https://github.com/mpicbg-scicomp/ij2course-tables)

### Jupyter Notebooks

-   [ImageJ2 Tutorial Notebooks](/tutorials/notebooks)
-   Installation:
    -   [Anaconda](https://conda.io/miniconda.html) (we suggest miniconda) should be installed on your system.
    -   Clone to a place of your choice: `git clone `[`https://github.com/imagej/tutorials`](https://github.com/imagej/tutorials)
    -   go into the tutorials folder you just cloned
    -   create a conda environment: `conda env create`
    -   activate the new environment: `source activate scijava`
    -   start jupyter notebook: `jupyter notebook`
-   Useful link to [beakerx](https://github.com/twosigma/beakerx)
-   [Python client for ImageJ](https://github.com/imagej/imagej.py)

### Git

-   See the [Git](/develop/git) page!

## Wednesday

### KNIME Usage

-   Download and install the KNIME Analytics Platform from [here](https://www.knime.com/downloads/download-knime)

### KNIME Development Introduction

-   Make sure you have Eclipse Oxygen installed
-   Clone https://github.com/knime-ip/knip-sdk-setup
-   Clone https://github.com/knime-ip/knip-course

### Developing ImageJ Ops

-   Clone https://github.com/imagej/tutorials (but you already have it, right?)
-   Import `maven-projects/create-a-new-op` in Eclipse.
-   See also the [Adding new ops](/develop/writing-ops) guide
-   See also the "Extending ImageJ: Ops" notebook linked from [here](/tutorials/notebooks)

### ImageJ Server

-   https://github.com/imagej/imagej-server
-   [imagej.server Python module](https://github.com/imagej/imagej.py/tree/master/imagej/server)
-   [Example Jupyter notebook using imagej-server](https://github.com/CellProfiler/notebooks/blob/master/cellprofiler_with_imagej_server.ipynb)
-   [Remote HPC cluster parallelization support in SciJava plugins](http://forum.imagej.net/t/remote-hpc-cluster-parallelization-support-in-scijava-plugins/10755)

## Thursday

### ClearVolume and BDV VisTools

-   [Slides](https://github.com/fiji/learnathon-2018/blob/master/Jug_BigDataAnd3dViz.pdf)
-   Repositories to be cloned:
    -   [`https://github.com/fjug/TutorialClearVolume.git`](https://github.com/fjug/TutorialClearVolume.git)
    -   [`https://github.com/fjug/TutorialBigDataViewer.git`](https://github.com/fjug/TutorialBigDataViewer.git)
-   ImgLib2 Cache Examples (optional): [`https://github.com/imglib/imglib2-cache-examples.git`](https://github.com/imglib/imglib2-cache-examples.git)
-   Vistools live here: [`https://github.com/bigdataviewer/bigdataviewer-vistools.git`](https://github.com/bigdataviewer/bigdataviewer-vistools.git)

### scenery & sciview

-   [Slides](https://ulrik.is/sharing-a-file-named/dais-learnathon-2018-scenery-sciview.pdf) / [zipped keynote](https://ulrik.is/sharing-a-file-named/dais-learnathon-2018-scenery-sciview.zip)
-   Repositories to be cloned:
    -   [`https://github.com/skalarproduktraum/sciview-tutorial.git`](https://github.com/skalarproduktraum/sciview-tutorial.git)
-   scenery repo: [`https://github.com/scenerygraphics/scenery`](https://github.com/scenerygraphics/scenery)
-   sciview repo: [`https://github.com/scenerygraphics/sciview`](https://github.com/scenerygraphics/sciview)

### KNIME ImageJ2 Integration

-   Course: [`https://github.com/knime-ip/knip-course`](https://github.com/knime-ip/knip-course) (Take a look at the README.md)
-   KNIP ImageJ2 repo: [`https://github.com/knime-ip/knip-imagej2`](https://github.com/knime-ip/knip-imagej2)

## Friday

### Imglib2 Algorithm

-   Slides: [https://github.com/maarzt/imglib2-algorithm-workshop/blob/master/slides/presentation.pdf](https://github.com/maarzt/imglib2-algorithm-workshop/blob/master/slides/presentation.pdf)
-   Exercises: [https://github.com/maarzt/imglib2-algorithm-workshop](https://github.com/maarzt/imglib2-algorithm-workshop)

### Imglib2 Advanced
