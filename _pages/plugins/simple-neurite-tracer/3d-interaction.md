---
mediawiki: Simple_Neurite_Tracer:_3D_Interaction
title: Simple Neurite Tracer › 3D Interaction
nav-links: true
nav-title: 3D Interaction
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

It is now possible to select the points for traces in the [3D Viewer](/plugins/3d-viewer) rather than the 2D view.

{% include video platform='youtube' id='Vt4m55V7AjI'%}

In order to select points for tracing in the 3D Viewer, you need to use the "Wand" tool. In order to rotate the view, you need to use the "Hand" tool. Once you have selected each of these once, you should be able to switch between them by pressing the {% include key key='Esc' %} key.

![](/media/fiji-toolbar-wand-and-hand.png)

The following key shortcuts also work in the 3D Viewer:

-   {% include key key='Y' %} confirm the temporary path segment
-   {% include key key='N' %} cancel the temporary path segment
-   {% include key key='F' %} complete the current path
-   {% include key key='G' %} select the current path under the mouse pointer

You can still create branches and joins in the 3D Viewer as you would in the 2D viewer. First select the path you want to branch off, or join to by pressing {% include key key='G' %} while the mouse pointer is over that path. (It should turn green.) Then create the join or branch by holding down the join modifier key ({% include key key='Ctrl' %} on Windows and Linux, {% include key key='Alt' %} on Mac OS) and clicking at the right point on the selected path.

The dataset used in the screencast can be downloaded from [the Diadem challenge website](http://www.diademchallenge.org/olfactory_projection_fibers_readme.html).
