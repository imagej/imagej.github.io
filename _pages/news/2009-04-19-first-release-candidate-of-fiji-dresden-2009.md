---
title: 2009-04-19 - First release candidate of Fiji Dresden-2009
---

In the aftermath of our hackathon in Dresden, we have a [first release candidate](/downloads) now!

Here is the impressive list of changes:

This is the after-hackathon release, and so far we have these changes (please correct me if I am wrong or forgot something):

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

NOTE: as often, Johannes forgot to acknowledge himself :)


