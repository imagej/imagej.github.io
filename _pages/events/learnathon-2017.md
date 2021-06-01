---
title: Learnathon 2017
categories: [news]
---

The first DAIS Learnathon took place from June 18 until June 24 2017.

## Schedule

See [this page](https://indico.mpi-cbg.de/event/50/other-view?view=standard)!

## Setting up your system

Check if you have this set up:

-   Jupyter + the SciJava kernel (https://github.com/scijava/scijava-jupyter-kernel)
    -   Install [Miniconda](https://conda.io/miniconda.html) if you do not have installed it or Anaconda already. (We need the version for Python 3!)
    -   Your `.bashrc` or `.zshrc` will need a line like this: `export PATH="/Users/someforders/miniconda3/bin:$PATH"`
    -   Make a new conda environment and install `jupyter` and `scijava-jupiter-kernel`:
    
             conda create --name scijava python=3
             source activate scijava
             conda install jupyter
             conda config --add channels conda-forge
             conda install scijava-jupyter-kernel

    -   Now (and in the future) you will have to activate the environment we just created: `source activate scijava`.
    -   Deactivation would work like this: `source deactivate`
    -   Get some notebook to try it out:
    
            git clone git@github.com:scijava/scijava-jupyter-kernel
            cd scijava-jupyter-kernel
            jupyter notebook

    -   Execute cells by hitting <kbd>shift</kbd>+<kbd>enter</kbd>—enjoy!
-   Eclipse (Neon)
-   bash / zsh
-   GIT
-   Maven
-   Gitter

This can happen later:

-   imglyb (forget that for now)

## Monday

Git repos to clone:

-   [`https://github.com/imagej/tutorials`](https://github.com/imagej/tutorials)
-   [`https://github.com/imagej/imagej`](https://github.com/imagej/imagej)
-   [`https://github.com/scijava/scijava-common`](https://github.com/scijava/scijava-common) (optional)
-   [`https://github.com/imagej/imagej-ops`](https://github.com/imagej/imagej-ops) (optional)
-   [`https://github.com/imglib/imglib2`](https://github.com/imglib/imglib2) (optional)

Slides online:

-   [`/presentations/2017-06-19-dais-learnathon/`](/presentations/2017-06-19-dais-learnathon/)

### Ops practical

Write your first `Command` plugin!

-   Try to do it completely on your own, using Internet resources.
-   If you get stuck, click on hint links.
-   If still stuck, ***grab a teacher***!

Details of your assignment:

-   Create a [Git](/develop/git) repository.
-   Create a [Maven](/develop/maven) project. (hints: [1](https://github.com/imagej/example-imagej-command), [2](/develop/building-a-pom))
-   Implement a `Command` plugin in your [IDE](/develop/ides), which calculates the *mean* across an image. (hints: [1](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1_-_Using_ImageJ/2_-_Introduction_to_ImageJ_Ops.ipynb), [2](https://github.com/imagej/tutorials/tree/master/maven-projects/simple-commands/src/main/java))
-   Push to [GitHub](/develop/github) (hints: [1](https://help.github.com/articles/pushing-to-a-remote/), [2](https://git-man-page-generator.lokaltog.net/)).

If you get that far, YOU WIN. {% include person id='fjug' %} has a reward for you.

Extra credit:

-   Grab fun snippets from the "Introduction to Ops" Jupyter notebook.
-   Integrate them into your command, to make it do fancier things.

### How to create a new git repository

This is, from my (Hanslovsky) point of view, the best way to create a new git repository. All commands should run on Linux, OSX, and the git bash shell on Windows.

-   Create a new repository on github.com (choose not to add a README.md or .gitignore), e.g. with name 'awesome-learnathon'
-   On your local machine create a directory where you would like to have the repository and cd into it: `mkdir 'awesome-learnathon' && cd 'awesome-learnathon'`
-   Initalize local git repository: `git init`
-   Add remote repository as origin: `git remote add -f origin git@github.com:user/awesome-learnathon` or `git remote add -f origin `[`https://github.com/user/awesome-learnathon`](https://github.com/user/awesome-learnathon) if you did not set up git through ssh. The `-f` parameter fetches from the remote repository
-   Create a first file, e.g. `pom.xml`, and stage it for a commit: `git add pom.xml`
-   Commit the stage files with commit message: `git commit -m 'Add pom.xml'`
-   Push your commit: `git push --set-upstream origin master` (you can ommit `--set-upstream origin master` in future commits)

## Tuesday

Git repos to clone:

-   Morning + early afternoon sessions:
    -   [`https://github.com/imglib/imglib2-introductory-workshop`](https://github.com/imglib/imglib2-introductory-workshop) ([slides](https://github.com/imglib/imglib2-introductory-workshop/blob/master/Introduction-ImgLib2.pdf) are in the repository)
    -   (bonus) LabelingPlus: https://github.com/TrNdy/Indago/blob/master/src/main/java/com/indago/data/segmentation/LabelingPlus.java
-   Afternoon session:
    -   The pull-request example: [to solve](https://github.com/Meyenhofer/ij-command-2/issues/)
    -   [`https://github.com/mpicbg-scicomp/ij2course-images`](https://github.com/mpicbg-scicomp/ij2course-images)
    -   [`https://github.com/mpicbg-scicomp/ij2course-regions`](https://github.com/mpicbg-scicomp/ij2course-regions)
    -   [`https://github.com/mpicbg-scicomp/ij2course-tables`](https://github.com/mpicbg-scicomp/ij2course-tables)

Optional practical for you to do on your own:

-   [`https://github.com/imglib/imglib2-advanced-workshop`](https://github.com/imglib/imglib2-advanced-workshop)

## Wednesday

Git repos to clone:

-   Morning Session on ClearVolume and BDV VisTools:
    -   [Slides](/media/events/jug-bigdataand3dviz.pdf)
    -   [`https://github.com/fjug/TutorialClearVolume.git`](https://github.com/fjug/TutorialClearVolume.git)
    -   [`https://github.com/fjug/TutorialBigDataViewer.git`](https://github.com/fjug/TutorialBigDataViewer.git)
    -   [`https://github.com/imglib/imglib2-cache-examples.git`](https://github.com/imglib/imglib2-cache-examples.git) (optional but awesome)
    -   [`https://github.com/bigdataviewer/bigdataviewer-vistools.git`](https://github.com/bigdataviewer/bigdataviewer-vistools.git)
-   Afternoon Ops Session:
    -   [`https://github.com/imagej/tutorials`](https://github.com/imagej/tutorials)
        -   Import the `maven-projects/using-ops` into your IDE
    -   [Introduction to ImageJ Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1_-_Using_ImageJ/2_-_Introduction_to_ImageJ_Ops.ipynb) Jupyter notebook
    -   [Extending ImageJ: Writing Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/2_-_Extending_ImageJ/4_-_Writing_Op_plugins.ipynb) Jupyter notebook
-   Afternoon Session on KNIME:
    -   Download & Install KNIME (app with all extensions)
        -   https://www.knime.org/downloads/overview?quicktabs_knimed=1#quicktabs-knimed
    -   Start KNIME and install all updates
    -   How to install ImageJ Integration in KNIME: https://tech.knime.org/community/imagej
    -   Set heap-size of KNIME: https://tech.knime.org/faq#q4_2
    -   [`https://github.com/knime-ip/knip-sdk-setup`](https://github.com/knime-ip/knip-sdk-setup)
        -   See installation instructions in [README.md](https://github.com/knime-ip/knip-sdk-setup/blob/master/README.md)
    -   [`https://github.com/knime-ip/knip-imagej2`](https://github.com/knime-ip/knip-imagej2)
        -   See installation instructions in [README.md](https://github.com/knime-ip/knip-imagej2/blob/master/README.md)
    -   [`https://github.com/knime-ip/knip-course`](https://github.com/knime-ip/knip-course)
        -   See instructions for exercises in [README.md](https://github.com/knime-ip/knip-course/blob/master/README.md)

<!-- -->

-   Preparation for the imglyb session on Thursday:
    -   Please follow the [installation instructions](https://gist.github.com/hanslovsky/508fb1ff7668f1e53bb769e6dccc789c) and install imglyb through conda.
    -   If you are a Windows user, please pair up with a OSX or Linux user, or download the [VirtualBox Ubuntu appliance](https://www.dropbox.com/s/gxqqzbxaff6uowe/Ubuntu%2017.04%20-%20imglyb.ova). We also have (at least) one MacBook that is available for use during that session. First come first serve!

## Thursday

### imglib2-algorithm

We will look at the examples in the *algorithm.morphology* package of the *imglib2-advanced-workshop* to get familiar with the use of existing algorithms in *imglib2-algorithm*.

-   Git repos to clone:
    -   [`https://github.com/imglib/imglib2-advanced-workshop`](https://github.com/imglib/imglib2-advanced-workshop)

### imglyb

The jupyter notebooks in the *imglyb-learnathon* repository cover basic and advanced use of the *imglyb* compatibility layer for *imglib2* and *numpy*. Please follow the instructions below to make sure your machine is prepared for the tutorial. Clone the *imagey* repository to access CPython through *ImageJ*.

-   Instructions:
    -   [`https://gist.github.com/hanslovsky/508fb1ff7668f1e53bb769e6dccc789c`](https://gist.github.com/hanslovsky/508fb1ff7668f1e53bb769e6dccc789c)

<!-- -->

-   Git repos to clone:
    -   [`https://github.com/imglib/imglib2-unsafe`](https://github.com/imglib/imglib2-unsafe)
    -   [`https://github.com/hanslovsky/imglib2-imglyb`](https://github.com/hanslovsky/imglib2-imglyb)
    -   [`https://github.com/hanslovsky/imglyb-examples`](https://github.com/hanslovsky/imglyb-examples)
    -   [`https://github.com/hanslovsky/imagey`](https://github.com/hanslovsky/imagey)
    -   [`https://github.com/hanslovsky/imglyb-learnathon`](https://github.com/hanslovsky/imglyb-learnathon)

## Friday

Git repos to clone:

-   Advanced ImgLib2 workshop: [`https://github.com/imglib/imglib2-advanced-workshop`](https://github.com/imglib/imglib2-advanced-workshop)
-   ImgLib2 caches: [`https://github.com/imglib/imglib2-cache-examples`](https://github.com/imglib/imglib2-cache-examples)
-   Write your own SciJava plugin types: [`https://github.com/mpicbg-scicomp/ij2course-scijava-plugin-mechanism`](https://github.com/mpicbg-scicomp/ij2course-scijava-plugin-mechanism)

Awesome stuff that happened too:

-   Discussion time
    -   The future of the [imagej forum](http://forum.imagej.net)...
    -   The problem of missing funding...
    -   Stable releases (coming in December).
    -   A system to track what a workflow should cite...
-   [Headless with Fiji](/scripting/headless) (ignoring legacy problems)
-   ImgLib2 ROIs (https://github.com/imglib/imglib2-roi/tree/shape-rois), a preview to what will/might come soon!

## Saturday
