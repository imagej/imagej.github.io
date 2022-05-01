---
title: 2009-04-27 - Second release candidate of Fiji Dresden-2009
---

In the aftermath of our hackathon in Dresden, we have a [second release candidate](/downloads) now!

This is the list of changes in addition to the changes in the first release candidate:

1.  FlowJ was integrated (thanks Jean-Yves Tinevez),
2.  The PIV Analyser (an optic flow technique) plugin was donated by Jean-Yves Tinevez,
3.  Refresh Javas is actually called on startup, so that you really can just drop .java files into plugins/ and they will be compiled and run automagically,
4.  a Clojure example was fixed so it runs with our current Clojure version,
5.  two Javascript examples for accessing TrakEM2 were fixed (thanks to Albert Cardona),
6.  the Fiji running on MacOSX can act as a drag 'n drop target now,
7.  the Dynamic Reslice plugin was contributed by Jean-Yves Tinevez and Albert Cardona,
8.  AbstractInterpreters cursor up/down behavior was fixed (hopefully for good now...),
9.  the Multi Thresholder plugin was removed, as we have something better in the form of Auto Threshold and Auto Local Threshold (thanks Jean-Yves Tinevez and Gabriel Landini),
10. Jean-Yves Tinevez performed a massive task in getting plugin descriptions as well as maintainer information onto our Wiki; if you have not put yourself as maintainer of your own plugins, please do so now,
11. a rather massive bug was fixed with {% include bc path='Help | Update Menus'%}; modified plugins were not loaded anew, but the old versions were retained in memory,
12. Erwin Frise made some modifications to the Level Set plugin: it remembers previously set parameters, and is substantially faster now,
13. Albert Cardona updated TrakEM2 to version 0.7c,
14. {% include bc path='Plugins | Scripting | Macro Interpreter'%} uses our AbstractInterpreter framework now (thanks to Albert Cardona), with command line history and all,
15. Gabriel Landini pointed out that our Daltonize plugin is misnamed: it simulates color blindness, rather than trying to compensate for it.

We are really close now to a final release, with just a few changes pending. Stay tuned!


