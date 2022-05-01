---
mediawiki: Gabriel_Graph
title: Gabriel Graph
categories: [Uncategorized]
---


{% capture source%}
{% include github org='ptbiop' repo='ijp-gabriel-graph' %}
{% endcapture %}
{% include info-box name='Gabriel Graph' software='Fiji' author='Olivier Burri' maintainer='Olivier Burri' filename='Gabriel\_Graph-1.0.0.jar' released='August 2015' latest-version='July 2017' source=source status='stable' website=' [BIOP Staff Page](http://biop.epfl.ch/INFO_Facility.html#staff)' %}

## Purpose

{% include wikipedia title="Gabriel graph" %} implementation for ImageJ/Fiji.

<figure><img src="/media/plugins/gabriel-graph-dialog.png" title="Gabriel_Graph_Dialog.png" width="200" alt="Gabriel_Graph_Dialog.png" /><figcaption aria-hidden="true">Gabriel_Graph_Dialog.png</figcaption></figure>

## Details

The algorithm goes through each pair of points and looks for the shortest distance between two points that does not contain any other point within the circle whose diameter is defined by the two points being queried. It is built to run in parallel as per the implementation of [Albert Cardona's ImageJ Tutorials](http://albert.rierol.net/imagej_programming_tutorials.html)

## Use

Call up the plugin using {% include bc path="Plugins|BIOP|Gabriel Graph..." %}.

The plugin expects an open image with a multipoint selection.

If selected, it will create a new results table with each point, its computed neighbor and the distance between them.

If selected, it will overlay the Gabriel Graph onto the image.

{% include img src="gabriel-graph-processing-example" width="400" caption="Result of Plugin on image" %}

## Macro Recordable

Making use of the GenericDialog class, the plugin is macro-recordable.

```
run("Gabriel Graph...", "results overlay parallel");
```

## Running from a Plugin

What you need to run this in a plugin is

```
import ch.epfl.biop.GabrielGraph;
```

And then call the static method

```
ResultsTable results = GabrielGraph.getGabrielGraph(final ImagePlus imp, final boolean is_show_overlay, final boolean is_parallel);
```

## Notes

It makes little sense not to use parallel processing, the only issue might be that the order of the points will be different on multiple runs, as this will depend on how Java will manage the threads.
