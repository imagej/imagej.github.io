{{ComponentStats:net.imagej:op-finder}}The Op Finder is a utility for the browsing, learning, and running of all available {{GitHub|org=imagej|groupId=imagej-ops|label=Ops}}. Because Ops are plugins and can be dynamically extended and specialized for particular inputs, it is not practical to have static documentation on a given Op. By using the Op Finder, you are able to explore the actual list of Ops available in ''your'' installation. The purpose of this guide is to familiarize yourself with the basic capabilities of the Op Finder, enabling you to learn and experiment with Ops.

= Getting started =

There are two ways to start up the Op Finder:

# Using the shortcut: {{Key|Shift||L}}
# Using the menu path: {{Bc|Plugins|Utilities|Find Ops...}}

= Parts of the Op Finder =

: [[File:LabeledOpFinder.png]]

'''Labeled components'''
# Search bar for [[#Filtering|filtering]] the list of Ops.
# Toggle button to change between a [[#For Users|user]] and [[#For Developers|developer]] view.
# Play button for [[#Running Ops|running the selected Op]].
# Copy button to copy the selected cell contents.
# Help button to open up the [[ImageJ_Ops|Wiki reference]] page in your browser.
# Status area showing success/failure notifications e.g., for copying or running Ops.
# Namespaces and Op types: these can be expanded to explore the tree-based organization of Ops.
# Op implementation: the leaves of this tree tell us what parameter options are available for each Op type. We interpret this particular example as "There is an Add Op in the Math namespace, that operates on an image and a numeric value".
# Progress area showing progress when performing lengthy operations, such as filtering the Ops.
# Details pane toggle. Click this button to show/hide a pane containing additional information about the currently selected Op.

'''Additional features'''
* Hover your mouse over any part of the Op Finder to get a descriptive tool-tip.
* Double-click any cell to copy its contents to your clipboard.

= Views =

Because of the extensibility of Ops, there is a lot of information to process when looking at which Ops are actually available. One goal of the Op Finder is to present this information in a way that can be easily understood. To facilitate this, multiple views are available, each tailoring the content of the Op Finder to a specific audience.

== For Users ==

{{Warning|This view provides an abstract representation of available Ops e.g., one entry could be many Ops merged together. An Op call is ultimately defined by the combination of requested '''Op type''' + '''parameters'''.}}

Ops in this view are focused on answering the question "What can I do ''right now'' with Ops?" For example, in this example we see that we can call the <code>Convolve</code> Op with either a base image, or the base and kernel:

: [[File:UserOpFinder.png|border|800px]]

'''User View Contents'''
* Only Ops directly involving images are displayed
* Parameter types are abstracted ("Image", "Number")
* Optional parameters are hidden

== For Developers ==

This view provides a comprehensive list of available Ops implementations. For example, contrasting with the [[#For Users|User view]], we see there are actually four concrete implementations of the <code>Convolve</code> Op, with a plethora of optional parameters.

: [[File:DevOpFinder.png|border|800px]]

'''Developer View Contents'''
# Precise Op signature
# Code snippet for use
# Defining Op class

= Things to do =

== Filtering ==

The Op Finder includes [[Wikipedia:Approximate_string_matching|fuzzy filtering]] to find Ops of interest. When filtering:

* Namespaces are hidden
* In [[#For Users|User view]], the complete simplified Op entry is filtered.
* In [[#For Developers|Developer view]], the Op namespaces + class name are filtered.

[[File:Filter-op-finder.png|border|600px]]

== Code Snippets ==

Code snippets are available in the [[#For Developers|Developer view]]. These are intended to help you rapidly build up scripts around the available Ops. The following is a step-by-step guide to take you through the process of finding an Op of interest to using it in a functional script.

1. The first thing to do is find an Op of interest. In this case, we start from the [[#For Users|User view]] and see that there is a Convolve Op we want to try:
: [[File:1-select-op.png|border]]

2. In the [[Script Editor]] (the keyboard shortcut {{key|{}} (open curly bracket) opens the editor), we need to add a reference to the <code>OpService</code> which will be our entry point for Op usage:

<source lang="python">
# @OpService ops
</source>

: '''Note:''' this guide is written in [[Jython_Scripting|Python]] but any scripting language will work

3. Now we need the code call for our Convolve Op, so we switch to the [[#For Developers|Developer view]]. The code is long, but remember we can [[#Parts of the Op Finder|copy]]:
: [[File:2-op-snippet.png|border|1200px]]

: and paste:

<source lang="python">
# @OpService ops

ops.run("filter.convolve", Img, Img, RandomAccessibleInterval, long[], OutOfBoundsFactory, OutOfBoundsFactory, RealType, ImgFactory)
</source>

4. Looking at the Op call, we see that there are ''a lot'' of parameters. To get a better idea of what these are, we look at the <code>Op Signature</code> column of the Op Finder:
: [[File:3-op-signature.png|border|1200px]]

: All of the parameters with a {{Key|?}} are '''optional'''. For our purposes, let's just work with the input image, kernel, and returned image:

<source lang="python">
# @OpService ops

out = ops.run("filter.convolve", Img, RandomAccessibleInterval)
</source>

5. At this stage, we can not actually run our code yet. The pasted snippet serves as a guideline for what types of parameters are needed and produced. The next step is to ask the framework for instances of these parameters by adding [[Script_parameters|@Parameters]] to our script:

<source lang="python">
# @OpService ops
# @Dataset input
# @Dataset kernel
# @OUTPUT ImgPlus out

out = ops.run("filter.convolve", input, kernel)
</source>

: '''Note:''' the types we copied and pasted (<code>Img</code> and <code>RandomAccessibleInterval</code>) represent a ''minimum class requirement''. Open images can always be requested as <code>Datasets</code>, which have a type hierarchy including {{Bc|ImgPlus|Img|RandomAccessibleInterval}}. <code>Dataset</code> is thus a good starting point as it can satisfy any of these parameters. If you want to have multiple input image parameters, you '''must''' use <code>@Dataset</code>.

6. Our script is done! If we open a base image and kernel in ImageJ we can run our script. The <code>OpService</code> is populated automatically by the ImageJ framework, and an input window is automatically created to select the images:

[[File:4-run-op.png|border"1200px]]

== Running Ops ==

Although you can run selected Ops through the Op Finder, this method '''lacks reproducibility''' and should not be used as a substitute for a proper script or plugin when using Ops in a scientific workflow. This functionality ''is'' intended to allow a rapid preview of what effect an Op will have on a dataset.

The [[#Parts of the Op Finder|play button]] essentially automates the process of turning an Op [[#Code Snippets|into a script]]: optional parameters are discarded and required parameters are [[Script_parameters|annotated]]. Because of this, Ops with arcane or unusual parameters may fail to run because the framework does not know how to provide them.

Thus it is recommended to run Ops primarily from the [[#For Users|User view]], as these Ops focus on images and numbers, which can automatically be provided by the framework (via open images and input panels, respectively).

= Further Reading =

* For more in-depth development information, see [[Writing_plugins|the guide to writing plugins]].
