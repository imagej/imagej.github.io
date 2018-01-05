{{Infobox
| name                   = Gabriel Graph
| software               = Fiji
| author                 = Olivier Burri
| maintainer             = Olivier Burri
| filename               = Gabriel_Graph-1.0.0.jar
| released               = August 2015
| latest version         = July 2017
| source                 = {{GitHub|org=ptbiop|repo=ijp-gabriel-graph}}
| status                 = stable
| website                = [http://biop.epfl.ch/INFO_Facility.html#staff BIOP Staff Page]
}}

== Purpose ==
Gabriel Graph Implementation for ImageJ/Fiji
See https://en.wikipedia.org/wiki/Gabriel_graph for implementation

[[File:Gabriel_Graph_Dialog.png|200px|thumb|right]]

== Details ==
The algorithm goes through each pair of points and looks for the shortest distance between two points that does not contain any other point within the circle whose diameter is defined by the two points being queried.
It is built to run in parallel as per the implementation of [http://albert.rierol.net/imagej_programming_tutorials.html Albert Cardona's ImageJ Tutorials]


== Use ==
Call up the plugin using ''Plugins->BIOP->Gabriel Graph...''.

The plugin expects an open image with a multipoint selection.

If selected, it will create a new results table with each point, its computed neighbor and the distance between them.

If selected, it will overlay the Gabriel Graph onto the image.

[[File:Gabriel_Graph_Processing_Example.png|400px|thumb|right|Result of Plugin on  image]]

== Macro Recordable ==

Making use of the GenericDialog class, the plugin is macro-recordable.
<source lang="java">
run("Gabriel Graph...", "results overlay parallel");
</source>

== Running from a Plugin == 
What you need to run this in a plugin is 
<source lang="java">
import ch.epfl.biop.GabrielGraph;
</source>

And then call the static method
<source lang="java">
ResultsTable results = GabrielGraph.getGabrielGraph(final ImagePlus imp, final boolean is_show_overlay, final boolean is_parallel);
</source>

== Notes ==

It makes little sense not to use parallel processing, the only issue might be that the order of the points will be different on multiple runs, as this will depend on how Java will manage the threads. 

[[Category:Plugins]]
