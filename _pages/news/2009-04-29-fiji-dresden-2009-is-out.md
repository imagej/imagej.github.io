---
title: 2009-04-29 - Fiji Dresden-2009 is out
---

Finally! Fiji "dee-dee-oh-nine" is out!

The changes:

1.  lots of bug fixes (thanks to all!)
2.  the scripting interpreters remember the previous commands (thanks to Albert Cardona): just use Cursor Up/Down to find out.
3.  we have a NRRD reader/writer now (thanks to Greg Jefferis)
4.  added the Turbo Reg plugin (thanks Philippe Thevenaz)
5.  Fiji Wiki is linked to in the Help menu (thanks Gabriel Landini)
6.  Lens Correction is a part of TrakEM2 now (thanks Stephan Saalfeld and Verena Kaynig)
7.  added the Radial Reslice plugin (thanks Julian Cooper and Albert Cardona)
8.  added Name Landmarks and Register plugin (thanks Mark Longair)
9.  updated bUnwarpJ (thanks Ignacio Arganda Carreras)
10. the bundled ImageJA now uses a method to discover a running instance that is safe in a multi-user environment
11. updated Bio\#Formats (thanks Melissa Linkert and Curtis Rueden)
12. added the {% include bc path='Help | Report a Bug'%} plugin (thanks Mark Longair)
13. added the MTrack2 plugin (thanks Nico Stuurman)
14. added the ToAST plugin (thanks Misha Kudryashev)
15. Java 1.6 is used on 64-bit MacOSX, when possible
16. added the Statistical Region Merging plugin
17. the PDF writer can now save all slices of image stacks, instead of only the current one
18. updated the AnalyzeSkeleton plugin (thanks Ignacio Arganda Carreras)
19. added the Time Stamper plugin (thanks Daniel James White)
20. added the Auto Threshold plugin (thanks Gabriel Landini)
21. if you drop a .java file into the plugins/ directory and call {% include bc path='Plugins | Scripting | Refresh Javas'%}, it will be added to the Plugins menu and be compiled transparently upon being called.
22. added scripting examples showing how to interact with the mouse and add Java listeners written in the scripting language
23. added the Arrow plugin
24. added the Stack Manipulation plugin (thanks Jean-Yves Tinevez)
25. added the FlowJ plugin (thanks Michael Abramoff and Jean-Yves Tinevez)
26. added the Edit LUT as Text script, allowing you to manipulate the numerical values of the color lookup table
27. added the Auto Local Threshold plugin (thanks Gabriel Landini)
28. added the PIV analyser plugin, for optical flow analysis (thanks Jean-Yves Tinevez)
29. updated TrakEM2 to version 0.7a (read: lots and lots and lots of bug fixes as well as enhancements, thanks Albert Cardona and Stephan Saalfeld)
30. renamed our 'Fill holes' plugin to 'Fill ROI holes' (thanks Gabriel Landini)
31. added Record Desktop and Record Window commands to record screen movies from either the whole desktop or a single (Java) window into a stack, optionally a VirtualStack to overcome memory problems (thanks Albert Cardona)
32. lots of bug fixes and enhancements to the 3D Viewer plugin (thanks Benjamin Schmid and Mark Longair)
33. lots of bug fixes and enhancements to the Simple Neurite Tracer plugin, as well as tighter integration with the 3D Viewer (thanks Mark Longair)
34. lots of bug fixes to the Segmentation Editor plugin (thanks Mark Longair and Greg Jefferis)
35. added the Show Color Surfaces plugin to show 8\#bit color stacks as colored surfaces in the 3D Viewer (thanks Mark Longair)
36. the 3D Viewer's 4D option can now load hyperstacks (thanks Benjamin Schmid)
37. the 3D Viewer can do free\#hand recordings again, as well as convenience key bindings (thanks Benjamin Schmid)
38. the Lasso/Blow Tool can optionally track dark lines, and actually respects the space/color ratio now
39. lots of changes only relevant for developers (thanks to all!)
40. FlowJ was integrated (thanks Jean-Yves Tinevez),
41. The PIV Analyser (an optic flow technique) plugin was donated by Jean-Yves Tinevez,
42. Refresh Javas is actually called on startup, so that you really can just drop .java files into plugins/ and they will be compiled and run automagically,
43. a Clojure example was fixed so it runs with our current Clojure version,
44. two Javascript examples for accessing TrakEM2 were fixed (thanks to Albert Cardona),
45. the Fiji running on MacOSX can act as a drag 'n drop target now,
46. the Dynamic Reslice plugin was contributed by Jean-Yves Tinevez and Albert Cardona,
47. AbstractInterpreters cursor up/down behavior was fixed (hopefully for good now...),
48. the Multi Thresholder plugin was removed, as we have something better in the form of Auto Threshold and Auto Local Threshold (thanks Jean-Yves Tinevez and Gabriel Landini),
49. Jean-Yves Tinevez performed a massive task in getting plugin descriptions as well as maintainer information onto our Wiki; if you have not put yourself as maintainer of your own plugins, please do so now,
50. a rather massive bug was fixed with {% include bc path='Help | Update Menus'%}; modified plugins were not loaded anew, but the old versions were retained in memory,
51. Erwin Frise made some modifications to the Level Set plugin: it remembers previously set parameters, and is substantially faster now,
52. Albert Cardona updated TrakEM2 to version 0.7c,
53. {% include bc path='Plugins | Scripting | Macro Interpreter'%} uses our AbstractInterpreter framework now (thanks to Albert Cardona), with command line history and all,
54. Gabriel Landini pointed out that our Daltonize plugin is misnamed: it simulates color blindness, rather than trying to compensate for it.
55. ImageJA no longer opens a port, requiring user consent on Windows.
56. Mark Longair and Benjamin Schmid contributed the Shape Based Average plugin based on a paper by Torsten Rohlfing.
57. Benjamin Schmid added some tools to edit videos.

Thanks to all the people who helped this release come about!


