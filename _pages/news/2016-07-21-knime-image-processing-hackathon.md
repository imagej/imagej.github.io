---
title: 2016-07-21 - KNIME Image Processing hackathon
---

From Tuesday, July 5, 2016 through Thursday, July 14, 2016, {% include person id='dietzc' %} of the [University of Konstanz](http://www.uni-konstanz.de/en/welcome/) hosted \~20 developers at the [KNIME Konstanz Regional Office](https://www.knime.org/contact) for a [hackathon](/events/hackathons) to develop the [KNIME](/software/knime) Image Processing extensions along with the underlying [ImageJ Ops](/libs/imagej-ops) library, as well as other supporting technologies such as [ImgLib2](/libs/imglib2), [ClearVolume](/plugins/clearvolume) and the [BigDataViewer](/plugins/bdv).

## Timeline

The following chart illustrates when everyone was present:

{% include img name="timeline" src="/media/news/2016-knime-hackathon-timeline.png" %}

<!-- The above image was rendered by MediaWiki. Original data, as converted, follows:

<timeline> Preset = TimeHorizontal_AutoPlaceBars_UnitYear

ImageSize = width:600

Colors =

 id:c01 value:blue
 id:c02 value:red
 id:c03 value:green
 id:c04 value:black
 id:c05 value:magenta
 id:c06 value:teal
 id:c07 value:yelloworange
 id:c08 value:skyblue
 id:c09 value:claret
 id:c10 value:oceanblue
 id:c11 value:purple
 id:c12 value:powderblue
 id:c13 value:coral
 id:c14 value:redorange
 id:c15 value:kelleygreen
 id:c16 value:orange
 id:c17 value:lightpurple
 id:c18 value:tan2
 id:c19 value:gray(0.3)
 id:c20 value:blue
 id:c21 value:red
 id:c22 value:green
 id:c23 value:black
 id:c24 value:magenta
 id:c25 value:teal
 id:gridLine value:gray(0.5)
 id:gridCanvas value:gray(0.8)

BackgroundColors = canvas:gridCanvas

Period = from:5 till:14

ScaleMajor = unit:year increment:1 start:5 grid:white

LineData =

 at:5 color:gridLine layer:back width:0.5
 at:6 color:gridLine layer:back width:0.5
 at:7 color:gridLine layer:back width:0.5
 at:8 color:gridLine layer:back width:0.5
 at:9 color:gridLine layer:back width:0.5
 at:10 color:gridLine layer:back width:0.5
 at:11 color:gridLine layer:back width:0.5
 at:12 color:gridLine layer:back width:0.5
 at:13 color:gridLine layer:back width:0.5
 at:14 color:gridLine layer:back width:0.5

BarData=

 barset:Hackers

PlotData=

 width:15 
 fontsize:M
 textcolor:white
 align:left 
 anchor:from 
 shift:(4,-4) 
 color:black

 barSet:Hackers
 color:c01 from:11 till:14 text:"Tim-Oliver Buchholz (UniKN)"
 color:c02 from:8 till:9 text:"Joshy Cyriac (USB, 4Quant)"
 color:c03 from:7 till:13 text:"Richard Domander (RVC)"
 color:c04 from:7 till:10 text:"Kevin Mader (4Quant, ETHZ)"
 color:c05 from:7 till:10 text:"Simon Schmid (UniKN)"
 color:c06 from:7 till:9 text:"Marcel Wiedenmann (UniKN)"
 color:c07 from:7 till:8 text:"Jan Eglinger (FMI Basel)"
 color:c08 from:5 till:13 text:"Kyle Harrington (HMS)"
 color:c09 from:6 till:12 text:"Curtis Rueden (UW-Madison)"
 color:c10 from:5 till:14 text:"Christian Dietz (UniKN)"
 color:c11 from:5 till:14 text:"Patrick Winter (UniKN)"
 color:c12 from:5 till:14 text:"Tobias Pietzsch (MPI-CBG)"
 color:c13 from:5 till:14 text:"Ulrik Günther (MPI-CBG)"
 color:c14 from:5 till:14 text:"Martin Horn (UniKN)"
 color:c15 from:5 till:14 text:"Andreas Burger (UniKN)"
 color:c16 from:5 till:14 text:"Alexander FIllbrunn (UniKN)"
 color:c17 from:5 till:14 text:"David Hörl (LMU Munich / MDC Berlin)"
 color:c18 from:5 till:13 text:"Jonathan Hale (UniKN)"
 color:c19 from:5 till:12 text:"Nico Hoffmann (TUD)"
 color:c20 from:5 till:9 text:"Stefan Helfrich (UniKN)"
 color:c21 from:5 till:8 text:"Cyril Mongis (Uni-Heidelberg)"

</timeline>
-->

## Gallery

{% capture gallerycontent %}
/media/news/hackathon-2016-konstanz-hackers.jpg | Hackers!
/media/news/hackathon-2016-konstanz-dinner.jpg | Hackers at dinner
/media/news/hackathon-2016-konstanz-rueden.jpg | {% include person id='ctrueden' %}
/media/news/hackathon-2016-konstanz-harrington.jpg | {% include person id='kephale' %}
/media/news/hackathon-2016-konstanz-domander.jpg | {% include person id='rimadoma' %}
/media/news/hackathon-2016-konstanz-hoerl.jpg | {% include person id='hoerldavid' %}
/media/news/hackathon-2016-konstanz-dietz-and-rueden.jpg | {% include person id='dietzc' %} and {% include person id='ctrueden' %}
/media/news/hackathon-2016-konstanz-harrington-and-gunther.jpg | {% include person id='kephale' %} and {% include person id='skalarproduktraum' %}
/media/news/hackathon-2016-konstanz-helfrich-and-pietzsch.jpg | {% include person id='stelfrich' %} and {% include person id='tpietzsch' %}
/media/news/2016-hackathon-konstanz-sushi.jpg | KNIME 3.2: sushi edition
/media/news/hackathon-2016-konstanz-amazing-salt.jpg | The gravity-defying salt shaker!
{% endcapture %}
{% include gallery content=gallerycontent %}

## Hackathon progress

### Christian Dietz

-   Continued work on KNIME SciJava Nodes and KNIME SciJava Scripting

### Richard Domander

-   Added first ops from BoneJ legacy code - topology namespace and ops for calculating the {% include wikipedia title="Euler characteristic" %} ({% include github org='imagej' repo='imagej-ops' pr='413' label='imagej-ops\#413' %})

### Kyle Harrington

-   Added 3D Mesh Voxelization to {% include github org='imagej' repo='imagej-ops' label='imagej-ops' %} ({% include github org='imagej' repo='imagej-ops' pr='419' label='imagej-ops\#419' %})
-   Began [ThreeDViewer](/plugins/sciview) and reached a moderately usable level
-   Refactored [Funimage](/software/funimagej) to be more Clojure idiomatic

### Stefan Helfrich

-   Proof-of-principle implementations of MatrixType and VectorType ({% include github org='stelfrich' repo='imglib2' label='matrixType' %})
-   Enable using global thresholds as local thresholds in Ops
-   Improve default OOBF handling for filters
    -   i.e. do not apply an OOBF if an image already is extended
    -   Add defined bounds for RandomAccessibles ([imglib2/random-access-defined-bounds](https://github.com/stelfrich/imglib2/tree/random-access-defined-bounds))
    -   Implement Shape.getBoundingBox() ({% include github org='imglib' repo='imglib2' pr='27' label='imglib2\#27' %})

### Martin Horn & Alexander Fillbrunn

-   Started JavaScript based Image Viewer with BigDataViewer as tile-server

### Curtis Rueden

-   Made major progress on improved op lookups using Nil (a.k.a. "typed null") objects—work still ongoing on the `nil` branch of {% include github org='imagej' repo='imagej-ops' label='imagej-ops' %}; prep work already on master ([1](https://github.com/imagej/imagej-ops/compare/fd2d9c5b8974d77976dabc53ba973d2a52ee465a%5E...226fc2114f0d68786f4a27b8fa498f18681379bf), {% include github org='imagej' repo='imagej-ops' commit='4135609f471352cbd32b048d32f0d5bb33343273' label='2' %})
-   Cleaned up the dependencies of ImageJ Ops; in particular, use SCIFIO for I/O, not ImageJ 1.x and AWT ({% include github org='imagej' repo='imagej-ops' pr='413' label='imagej-ops\#413' %})
-   Helped clean up {% include person id='rimadoma' %}'s "Topology namespace and ops" PR ({% include github org='imagej' repo='imagej-ops' pr='415' label='imagej-ops\#415' %})
-   Created a (not yet functional) [Kotlin](https://kotlinlang.org/) SciJava script engine ({% include github org='scijava' repo='scripting-kotlin' label='scijava/scripting-kotlin' %})

## Technical discussions

-   The future of ImageJ user interfaces: ImageJFX? KNIME? JavaScript + RESTful image server?
-   Languages on the JVM: using Scala, Kotlin and/or Groovy for future SciJava components

   
