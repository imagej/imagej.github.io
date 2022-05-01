---
mediawiki: Simple_Neurite_Tracer:_Selecting_paths
title: Simple Neurite Tracer › Selecting paths
nav-links: true
nav-title: Selecting Paths
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

There are three ways of selecting a particular path in [Simple Neurite Tracer](/plugins/snt).

### In the Path Window

You can select a path in the Path Window. You can also use the up and down cursor keys to go through the list quickly, and see which paths turn green in the 2D and 3D tracing views.

### In the 2D tracing view

If you press the {% include key key='G' %} key with your mouse over a path in the 2D tracing view, that path should be selected. Note that this is the nearest path to the point shown in the image, so if you're showing paths projected through all slices, this may not be the one you expect. You can make this more obvious by switching the 'View paths (2D)' option to 'parts in nearby slices'. Alternatively, just move through the stack to a nearby slice before pressing {% include key key='G' %}.

### In the 3D tracing view

There are various ways to select a path in the 3D viewer, from easiest to most difficult:

-   If you press {% include key key='G' %} when the mouse is over a path in the 3D Viewer, it will be selected.

<!-- -->

-   If you select a path in the 3D viewer, it should now also be selected in the rest of the tracing interface. One way of doing this is via the "Select" menu.

<!-- -->

-   Alternatively, you can click on the path in the 3D view. Note that you will probably have the problem that clicks in the 3D view only select the <i>volume</i> rather than the paths - you can get around this by selecting the volume and then unticking {% include bc path='Edit | Hide/Show | Show content'%} to hide the volume rendering. Then clicking on the paths will be easy.
