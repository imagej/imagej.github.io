---
mediawiki: Simple_Neurite_Tracer:_Sholl_analysis
title: Simple Neurite Tracer › Sholl Analysis
nav-links: true
nav-title: Sholl Analysis
---

{% include notice icon="warning" content='This is an old tutorial on how to call the [Sholl Analysis](/plugins/sholl-analysis) plugin from [Simple Neurite Tracer](/plugins/snt). **It is rather outdated. More up-to-date information is provided in [SNT: Analysis](/plugins/snt/analysis#sholl-analysis).** For an overview of the technique refer to the [Sholl Analysis](/plugins/sholl-analysis) documentation page.' %}

# Introduction

This tutorial assumes that you've already traced an image with Simple Neurite Tracer (SNT) and that you are familiar with the [variants of Sholl methods](/plugins/sholl-analysis#methodstable) and the [Sholl Analysis](/plugins/sholl-analysis) plugin. This tutorial will use an olfactory projection fibre image, freely available from the [Diadem challenge data set](http://www.diademchallenge.org/olfactory_projection_fibers_readme.html).

# Retrieving Profiles

When you've loaded the traces, that should look something like this: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-1.jpg" title="fig:" width="500" />

Now you have to pick a centre point for the analysis. This might be the soma or a [relevant focal point](http://forum.imagej.net/t/sholl-analysis-validation-parameters/3065/2). The centre point must be on one of your existing paths. First, select the path on which your centre point lies: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-2.jpg" title="fig:" width="500" />

Now hold down {% include key keys='Ctrl|Shift' %} (on Windows or Linux) or {% include key keys='option|shift' style='mac' %} (on Mac) and move the mouse along the path. A red cross-hair should track along the path: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-3.jpg" title="fig:" width="500" />

... when you've got the red cross-hairs at a suitable point, <i>still</i> holding down {% include key key='Ctrl' %} / {% include key key='Alt' %} and {% include key key='Shift' %}, press the {% include key key='A' %} key. Then you can release the other keys. You should see the Sholl analysis interface appear like this: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-4.jpg" title="fig:" width="500" />

Consider the first two options: you should probably select the top option *Use all N paths in analysis?* unless you're only wanting to include a subset of the paths, for example if your image stack contains multiple separate neurons. Next you can click on *Plot Profile* so that you can visualize how the intersections with concentric spheres vary with distance from your centre point: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-6.jpg" title="fig:" width="500" />

This graph shows exactly how many times a sphere of a particular radius will intersect with paths (i.e., *continuos sampling*). To consider spheres of evenly spaced radii (see definition of [Step size](/plugins/sholl-analysis#stepsize)), you have to enter a value into the *Radius step size* box. E.g., <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-7.jpg" title="fig:" width="500" />

# Data Normalization

If you need to preview the effect of [normalizing](/plugins/sholl-analysis#methodstable) the number of intersections by the volume (or area) enclosed by the sphere (or circle) - you can do that by selecting the *Normalize for volume enclosed by circle* option: <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-8.jpg" title="fig:" width="500" />

The *Use standard axes* / *Use semi-log axes* / *Use log-log axes* controls whether the analysis is based on the log of normalized intersections and distance (*log-log*), the log of normalized intersections (*semi-log*) or unmodified values (linear axes) (see [Sholl Plots](/plugins/sholl-analysis#sholl-plots) for details. Note that the [Regression coefficient](/plugins/sholl-analysis#sholldecay) is always calculated in real time even if no normalization options are chosen.

# Exporting Profiles

You can export profiles by clicking on "Save Profile" which will prompt for a CSV filename to save to. If you want to export the profile, so that you can edit in some other software or include it in a presentation, you can select *Export graph as SVG* in the graph window. You can then load the SVG file (e.g., in Inkscape):

<center>
{% include img src="sholl-analysis-10" width="350" %} {% include img src="sholl-analysis-11" width="350" %}
</center>

# Analyzing Profiles

Press *Analyze Profile* to run the [Sholl Analysis](/plugins/sholl-analysis) plugin. Once [Parameters](/plugins/sholl-analysis#parameters) have been specified, the plugin will [automatically calculate](/plugins/sholl-analysis#dratio) the normalization method thought to be the most informative. Metrics will be displayed in a [detailed table](/plugins/sholl-analysis#metrics).

{% capture analyzing-profiles-tip %}
You can perform batch analysis using [{% include bc path="Analysis | Sholl | Sholl Analysis (Existing Profiles)..." %}](/plugins/sholl-analysis#analysis-of-existing-profiles) or [{% include bc path="Analysis | Sholl | Sholl Analysis (Tracings)..." %}](/plugins/sholl-analysis#analysis-of-traced-cells)
{% endcapture %}
{% include notice icon="tip" content=analyzing-profiles-tip %}

# Sholl Image

Another option that might be useful is *Make Sholl image*, equivalent to the [Intersections mask](/plugins/sholl-analysis#output-options) created by the [Sholl Analysis](/plugins/sholl-analysis) plugin when parsing images directly. This will produce a stack which shows the number of intersections at each distance from the centre point on a colour scale. You can see the exact number of intersections corresponding to a colour by mousing over that region and looking in the status bar. For example, this shows you that the orange colour corresponds to 2 intersections ("value=2"): <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-12.jpg" title="fig:" width="500" />

If you go back to the main tracer interface, keeping that *Sholl image stack* open, you can visualize those colours on the traces by switching the *Use colors / labels from* option to *Sholl analysis of all paths* (volume of original image made transparent for clarity): <img src="/media/plugins/simple-neurite-tracer/sholl-analysis-13.jpg" title="fig:" width="500" />


