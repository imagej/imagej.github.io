---
mediawiki:
- Simple_Neurite_Tracer:_Introductory_Screencast
- Simple_Neurite_Tracer:_Old_Screencast1
- Simple_Neurite_Tracer:_Old_Screencast2
- Simple_Neurite_Tracer:_Old_Screencasts
title: Simple Neurite Tracer › Screencasts
nav-links: true
nav-title: Screencasts
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

This screencast (which needs audio) explains basic use of the plugin. It
probably won't be clear what's going on unless you make it full-screen:

{% include video platform="youtube" id="y6ZPdDfUOjI" width=420 %}

## Older screencasts

These screencasts are from very early versions of the plugin, but may still be of some use since all the functionality is still present.

This first screencast shows the basic operation of the plugin on a fairly indistinct confocal scan. After about a minute I turn on the option to use a Hessian-based cost function for the search, based on code written by Stephan Preibisch at the Janelia Farm Hackathon. You may notice that the searches after that point follows the neurons more closely. However, in some cases that finds erroneous paths or the naive cost function performs better, so in practice one switches back and forth. \[Note that this demo was recorded from an earlier version that didn't have support for branching.\]

{% include video platform='youtube' id='SSXx3DLCJD8'%}

This next video demonstrates more of the functionality that I added at Janelia Farm, in particular the fitting of centre lines and the filling-out of neurons. I use Benjamin Schmid's [3D Viewer](/plugins/3d-viewer) in this demo for visualizing the results, and as an example export the mesh and load it into Blender at the end - thanks to Albert Cardona for his advice on all matters Blender.

{% include video platform='youtube' id='sjSsNsr_2YM'%}
