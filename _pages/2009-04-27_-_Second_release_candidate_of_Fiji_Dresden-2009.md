In the aftermath of our hackathon in Dresden, we have a [[Downloads|second release candidate]] now!

This is the list of changes in addition to the changes in the first release candidate:

# FlowJ was integrated (thanks Jean-Yves Tinevez),
# The PIV Analyser (an optic flow technique) plugin was donated by Jean-Yves Tinevez,
# Refresh Javas is actually called on startup, so that you really can just drop .java files into plugins/ and they will be compiled and run automagically,
# a Clojure example was fixed so it runs with our current Clojure version,
# two Javascript examples for accessing TrakEM2 were fixed (thanks to Albert Cardona),
# the Fiji running on MacOSX can act as a drag 'n drop target now,
# the Dynamic Reslice plugin was contributed by Jean-Yves Tinevez and Albert Cardona,
# AbstractInterpreters cursor up/down behavior was fixed (hopefully for good now...),
# the Multi Thresholder plugin was removed, as we have something better in the form of Auto Threshold and Auto Local Threshold (thanks Jean-Yves Tinevez and Gabriel Landini),
# Jean-Yves Tinevez performed a massive task in getting plugin descriptions as well as maintainer information onto our Wiki; if you have not put yourself as maintainer of your own plugins, please do so now,
# a rather massive bug was fixed with {{bc | Help | Update Menus}}; modified plugins were not loaded anew, but the old versions were retained in memory,
# Erwin Frise made some modifications to the Level Set plugin: it remembers previously set parameters, and is substantially faster now,
# Albert Cardona updated TrakEM2 to version 0.7c,
# {{bc | Plugins | Scripting | Macro Interpreter}} uses our AbstractInterpreter framework now (thanks to Albert Cardona), with command line history and all,
# Gabriel Landini pointed out that our Daltonize plugin is misnamed: it simulates color blindness, rather than trying to compensate for it.

We are really close now to a final release, with just a few changes pending.  Stay tuned!

[[Category:News]]
