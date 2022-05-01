---
mediawiki: Op_Finder
title: Op Finder
categories: [Ops]
artifact: net.imagej:op-finder
---

The Op Finder is a utility for the browsing, learning, and running of all available {% include github org='imagej' groupId='imagej-ops' label='Ops' %}. Because Ops are plugins and can be dynamically extended and specialized for particular inputs, it is not practical to have static documentation on a given Op. By using the Op Finder, you are able to explore the actual list of Ops available in *your* installation. The purpose of this guide is to familiarize yourself with the basic capabilities of the Op Finder, enabling you to learn and experiment with Ops.

# Getting started

There are two ways to start up the Op Finder:

1.  Using the shortcut: {% include key keys='Shift|L' %}
2.  Using the menu path: {% include bc path='Plugins|Utilities|Find Ops...'%}

# Parts of the Op Finder


![](/media/plugins/labeledopfinder.png)

**Labeled components**

1.  Search bar for [filtering](#Filtering) the list of Ops.
2.  Toggle button to change between a [user](#for-users) and [developer](#for-developers) view.
3.  Play button for [running the selected Op](#running-ops).
4.  Copy button to copy the selected cell contents.
5.  Help button to open up the [Wiki reference](/libs/imagej-ops) page in your browser.
6.  Status area showing success/failure notifications e.g., for copying or running Ops.
7.  Namespaces and Op types: these can be expanded to explore the tree-based organization of Ops.
8.  Op implementation: the leaves of this tree tell us what parameter options are available for each Op type. We interpret this particular example as "There is an Add Op in the Math namespace, that operates on an image and a numeric value".
9.  Progress area showing progress when performing lengthy operations, such as filtering the Ops.
10. Details pane toggle. Click this button to show/hide a pane containing additional information about the currently selected Op.

**Additional features**

-   Hover your mouse over any part of the Op Finder to get a descriptive tool-tip.
-   Double-click any cell to copy its contents to your clipboard.

# Views

Because of the extensibility of Ops, there is a lot of information to process when looking at which Ops are actually available. One goal of the Op Finder is to present this information in a way that can be easily understood. To facilitate this, multiple views are available, each tailoring the content of the Op Finder to a specific audience.

## For Users

{% include notice icon="warning" content='This view provides an abstract representation of available Ops e.g., one entry could be many Ops merged together. An Op call is ultimately defined by the combination of requested **Op type** + **parameters**.' %}

Ops in this view are focused on answering the question "What can I do *right now* with Ops?" For example, in this example we see that we can call the `Convolve` Op with either a base image, or the base and kernel:


<img src="/media/plugins/useropfinder.png" title="fig:UserOpFinder.png" width="800" alt="UserOpFinder.png" />

**User View Contents**

-   Only Ops directly involving images are displayed
-   Parameter types are abstracted ("Image", "Number")
-   Optional parameters are hidden

## For Developers

This view provides a comprehensive list of available Ops implementations. For example, contrasting with the [User view](#for-users), we see there are actually four concrete implementations of the `Convolve` Op, with a plethora of optional parameters.


<img src="/media/plugins/devopfinder.png" title="fig:DevOpFinder.png" width="800" alt="DevOpFinder.png" />

**Developer View Contents**

1.  Precise Op signature
2.  Code snippet for use
3.  Defining Op class

# Things to do

## Filtering

The Op Finder includes [fuzzy filtering](Wikipedia_Approximate_string_matching) to find Ops of interest. When filtering:

-   Namespaces are hidden
-   In [User view](#for-users), the complete simplified Op entry is filtered.
-   In [Developer view](#for-developers), the Op namespaces + class name are filtered.

<figure><img src="/media/plugins/filter-op-finder.png" title="Filter-op-finder.png" width="600" alt="Filter-op-finder.png" /><figcaption aria-hidden="true">Filter-op-finder.png</figcaption></figure>

## Code Snippets

Code snippets are available in the [Developer view](#for-developers). These are intended to help you rapidly build up scripts around the available Ops. The following is a step-by-step guide to take you through the process of finding an Op of interest to using it in a functional script.

1\. The first thing to do is find an Op of interest. In this case, we start from the [User view](#for-users) and see that there is a Convolve Op we want to try:

![](/media/plugins/1-select-op.png)

2\. In the [Script Editor](/scripting/script-editor) (the keyboard shortcut {% include key key='{' %} (open curly bracket) opens the editor), we need to add a reference to the `OpService` which will be our entry point for Op usage:

```
#@ OpService ops
```

{% include notice icon="note" content="This guide is written in [Python](/scripting/jython) but any scripting language will work." %}

3\. Now we need the code call for our Convolve Op, so we switch to the [Developer view](#for-developers). The code is long, but remember we can [copy](#parts-of-the-op-finder):


<img src="/media/plugins/2-op-snippet.png" title="fig:2-op-snippet.png" width="1200" alt="2-op-snippet.png" />

<!-- -->


and paste:

<!-- -->

    #@ OpService ops

    ops.run("filter.convolve", Img, Img, RandomAccessibleInterval, long[], OutOfBoundsFactory, OutOfBoundsFactory, RealType, ImgFactory)

4\. Looking at the Op call, we see that there are *a lot* of parameters. To get a better idea of what these are, we look at the `Op Signature` column of the Op Finder:


<img src="/media/plugins/3-op-signature.png" title="fig:3-op-signature.png" width="1200" alt="3-op-signature.png" />

<!-- -->


All of the parameters with a {% include key key='?' %} are **optional**. For our purposes, let's just work with the input image, kernel, and returned image:

<!-- -->

    #@ OpService ops

    out = ops.run("filter.convolve", Img, RandomAccessibleInterval)

5\. At this stage, we can not actually run our code yet. The pasted snippet serves as a guideline for what types of parameters are needed and produced. The next step is to ask the framework for instances of these parameters by adding [@Parameters](/scripting/parameters) to our script:

    #@ OpService ops
    #@ Dataset input
    #@ Dataset kernel
    #@ OUTPUT ImgPlus out

    out = ops.run("filter.convolve", input, kernel)

{% capture minimum-class-requirement %}
The types we copied and pasted (`Img` and `RandomAccessibleInterval`) represent a *minimum class requirement*. Open images can always be requested as `Dataset`s, which have a type hierarchy including {% include bc path='ImgPlus|Img|RandomAccessibleInterval' %}. `Dataset` is thus a good starting point as it can satisfy any of these parameters. If you want to have multiple input image parameters, you **must** use `#@ Dataset`.
{% endcapture %}
{% include notice icon="note" content=minimum-class-requirement %}

6\. Our script is done! If we open a base image and kernel in ImageJ we can run our script. The `OpService` is populated automatically by the ImageJ framework, and an input window is automatically created to select the images:

[border"1200px](File_4-run-op.png)

## Running Ops

Although you can run selected Ops through the Op Finder, this method **lacks reproducibility** and should not be used as a substitute for a proper script or plugin when using Ops in a scientific workflow. This functionality *is* intended to allow a rapid preview of what effect an Op will have on a dataset.

The [play button](#parts-of-the-op-finder) essentially automates the process of turning an Op [into a script](#code-snippets): optional parameters are discarded and required parameters are [annotated](/scripting/parameters). Because of this, Ops with arcane or unusual parameters may fail to run because the framework does not know how to provide them.

Thus it is recommended to run Ops primarily from the [User view](#for-users), as these Ops focus on images and numbers, which can automatically be provided by the framework (via open images and input panels, respectively).

# Further Reading

-   For more in-depth development information, see [the guide to writing plugins](/develop/plugins).
