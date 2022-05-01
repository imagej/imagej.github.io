---
mediawiki: Simple_Neurite_Tracer:_Step-By-Step_Instructions
title: Simple Neurite Tracer › Step-By-Step Instructions
nav-links: true
nav-title: Step-By-Step Instructions
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

# Step-by-Step Tracer Instructions

These "step-by-step" instructions below assume that you have done the preliminary steps described on the [Simple Neurite Tracer: Basic Instructions](/plugins/simple-neurite-tracer/basic-instructions) page including starting up the plugin and turning on "Hessian-based analysis". Note that the screenshots here are from an early pre-release version of the plugin. The path list in the current version is in a separate window, but otherwise the interface is the same.

## Trace a basic path:

### 1. Pick a start point

Before you pick a start point for your first path, the tracer will look like this: ![](/media/snt-cropped-before-starting.png) Move through the image stack to find the start point of a path, then click there with the left mouse button.

### 2. Click a subsequent point

A small blue square should appear, showing the start of the path: ![](/media/snt-cropped-after-starting.png) Move through the stack to find a subsequent point further along the same neuron, blood vessel, or whatever, and click there. During tracing, if a part cannot be found immediately, you may see the progress of the search in cyan: ![](/media/snt-cropped-mid-tracing.png) You can scroll through the stack while such a search is in progress - if it appears not be making good progress, it's probably best to click "Abandon search" (or press {% include key key='Esc' %}) and pick a point closer to the start point.

### 3. Confirm the temporary path

Once the search has found that point, it is shown in blue (to indicate that this is still a temporary path) and you are asked to confirm (by clicking "Yes" or pressing {% include key key='Y' %}) that this path is following the route through the stack that you expect. If it is not, then click "No" {% include key key='N' %} and you'll go back to step 2. ![](/media/snt-cropped-confirmation.png)

### 4. After confirming the temporary path

Assuming you confirmed the path, the confirmed path will appear in red, like this: ![](/media/snt-cropped-confirmed.png) Now you are essentially back at step 2. Normally you will go on top pick further points along the structure. However, if you have finished with that path, click "Finish Path" {% include key key='F' %} and you will go back to step 1.

### 5. After completing a path

If you completed that path it will be shown in magenta: ![](/media/snt-cropped-completed-path.png)

## Branching: Start a path on an existing path

Before you pick a start point for your first path, the tracer will look like this: (We've zoomed in on the region of interest) ![](/media/plugins/simple-neurite-tracer/snt-sb-before-selecting.png)

### 1. Select the path to branch off

To select the path you want to branch off from, you can either select it in the path list, or press {% include key key='G' %} while your mouse pointer is over the path. When the path is first selected, it will be shown in the default green color, as below: ![](/media/plugins/simple-neurite-tracer/snt-sb-before-starting-path.png)

### 2. Click while holding the branch modifier to start the branch

To force the start of the new path to be a branch off the selected path, hold down the {% include key keys='Ctrl|Shift' %} keys while you move the mouse to find the right point under the red cross-hairs. Then click with the left mouse button - {% include key keys='Ctrl|Shift' %} should still be held down. Finally release the keys. **N.B. on MacOS you must use {% include key keys='Alt|Shift' %} instead.** Once you've started a path, it looks like this: ![](/media/snt-sb-started-branch.png)

### 3. Continue adding to the path as normal

From this point on, you can carry on adding to the path as above, e.g. create a temporary path: ![](/media/snt-sb-temporary-path.png) ... and confirm it: ![](/media/snt-sb-confirmed-path.png) When you decide to complete the path you should see in the path list that it has been recorded as starting on the existing path: ![](/media/snt-sb-completed-branch.png)

## Joining: End a path on an existing path

Supposing you want the end of a path that you're tracing to join onto an existing path, you just use the same modifier key when selecting the end point of the last part of the path. To go into that in more detail, if you're half way through tracing a path like this: ![](/media/snt-ej-cropped-half-finished.png)

... and you want the final part of that path to join up with the existing path running from the bottom to the top of the image. First, select that path in the path list, so that it turns green: ![](/media/snt-ej-cropped-selected-destination-path.png)

Now hold down {% include key keys='Ctrl|Shift' %} (or {% include key keys='Alt|Shift' %} on MacOS) to restrict the end point to be a "join" on that existing path. Click (while still holding down the modifier keys) to start the search for that end point and make it join the existing path. If the search can find a path to the end point, the result should look like this: ![](/media/snt-ej-cropped-end-join-created.png)

If you're happy with that, confirming the temporary path will automatically complete the whole path, since if you're creating an end join there cannot be any more to the path. The result will look like this: ![](/media/snt-ej-cropped-path-completed.png)

Note that the path list indicates that this new path (1) ends on the existing one (0).
