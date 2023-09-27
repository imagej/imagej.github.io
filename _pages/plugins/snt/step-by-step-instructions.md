---
title: SNT › Step-By-Step Instructions
nav-links: true
nav-title: Walk-throughs
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
extensions: ["mathjax"]
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
---

{% capture version%}
**These instructions were last revised for version 4.3.0**.<br>
Please help us to keep these walk-throughs up-to-date by [editing](https://github.com/imagej/imagej.github.io/edit/main/_pages/plugins/snt/manual.md) this page directly to fill in any documentation gap. Do [reach out](https://forum.image.sc/tag/snt) if you need assistance!
{% endcapture %}
{% include notice content=version %}

# Semi-automated Tracing
{% capture op1-demo-incomplete%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _Drosophila OP neuron (Complete 3D reconstruction)_ dataset. All the neuronal processes are traced in this dataset, so you may want to delete some of the existing paths beforehand.
{% endcapture %}

{% include notice icon="info" content=op1-demo-incomplete %}

These instructions assume that you have read the [Manual](/plugins/snt/manual), including starting up the plugin, enabling [Cursor Auto-snapping](/plugins/snt/manual#cursor-auto-snapping), and [Auto-tracing](/plugins/snt/manual#auto-tracing) options. Parts of this section are also documented in a [Screencast](/plugins/snt/screencasts#introduction-to-tracing).

## Starting A Path

### I. Pick The Starting Point

<img align="right" src="/media/plugins/snt/snt-cropped-before-starting-2.png" title="Choosing a starting point" width="33%" alt="Choosing a starting point" />
You may notice that, by default, the cursor [snaps](/plugins/snt/manual#cursor-auto-snapping) to the brightest pixel in its vicinity. If you prefer to manually control the placement of nodes, feel free to toggle this feature by pressing {% include key key='S' %}. Now, to begin tracing, move through the image stack to find the start point of a path then click there with the left mouse button.

### II. Pick A Subsequent Point

<img align="right" src="/media/plugins/snt/snt-cropped-after-starting-2.png" title="First point of a path selected" width="33%" alt="First point of a path selected" />
A small circle should appear, highlighting the start of the path. Move through the stack to find a subsequent point further along the same structure to be traced (neuron, blood vessel, etc.), and click there.

If a path between the two points cannot be found immediately, you may see the animated progress of the search. You can scroll through the stack while such a search progresses: If it appears to not be making good progress, it's probably best to press the "Cancel/Esc" button (shortcut: {% include key key='C' %}/{% include key key='Esc' %}) and pick a point closer to the start point.
<img align="right" src="/media/plugins/snt/snt-cropped-mid-tracing-2.png" title="A* search animated progress" width="33%" alt="A* search animated progress" />

NB:
- Increasing *Z* in the *Cursor Auto-snapping* panel allows for automated Z-navigation on signal mouseover
- You can increase the contrast (opacity, size, etc.) of Path nodes in the _Path rendering_ widget of the [Options tab](/plugins/snt/manual#options-tab)


### III. Confirm The Temporary Segment

Once the search has reached the target point, the path is shown in cyan (to indicate that this is still a temporary path) and you are asked to confirm (by clicking "Yes" or pressing {% include key key='Y' %}) that this path is following the route through the image that you expect. If it is not, then click "No" {% include key key='N' %} and you'll go back to the [previous step](#ii-pick-a-subsequent-point). Assuming you confirmed the path, the confirmed path will appear in red. Now you are essentially back at [step II](#ii-pick-a-subsequent-point). Normally you will go on to pick further points along the structure. However, if you have finished with that path, click "Finish Path" {% include key key='F' %} and you will go back to [step I](#i-pick-a-start-point). If you completed that path it would be shown in magenta.

<div align="center">
  <img src="/media/plugins/snt/snt-cropped-confirmation-2.png" title="A* search completed" width="33%" alt="A* search completed" />
  <img src="/media/plugins/snt/snt-cropped-confirmed-2.png" title="A confirmed segment" width="33%" alt="A confirmed segment" />
  <img src="/media/plugins/snt/snt-cropped-completed-path-2.png" title="A completed path" width="33%" alt="A completed path" />
</div>

NB: Once you become familiarized with the software you may want to disable the confirmation of temporary segments in _Temporary Paths_ section of the [Options tab](/plugins/snt/manual#options-tab)


## Branching: Start A Path On An Existing Path

### I. Select The Path To Branch Off

<img align="right" src="/media/plugins/snt/snt-sb-selecting-by-g.gif" width="33%" title="Holding &#39;G&#39; (Group paths around cursor) will select the closest path to the mouse pointer" >
To select the path you want to branch off from, you can either select it in the Path Manager, or press {% include key key='G' %} while the mouse pointer is near the path. When the path is first selected, it will be shown in the default green color. Note that you can also right-click on the image and choose _Select Paths by 2D ROI_ from the contextual menu: This will allow you to draw coarsely around the path of interest to activate it.

### II. Select The Fork Point

To force the start of the new path to be a branch of the selected path, hold down the {% include key keys='Alt|Shift' %} keys while you move the mouse to find the branch point under the red cross-hairs, now decorated with a "Fork Point" annotation. With {% include key keys='Alt|Shift' %} held down, click with the left mouse button. Finally, release the keys.
<img align="right" src="/media/plugins/snt/snt-sb-started-branch-2.png" title="A newly created fork point" width="33%" alt="A newly created fork point" />
NB:
- It is also possible to zoom into the branch point, right-click on the image and choose *Fork at Nearest Node* from the contextual menu
- The forking shortcut can also be simplified (_Temporary Paths_ section of the [Options tab](/plugins/snt/manual#options-tab))

### III. Extend The Path

From this point on, you can carry on adding nodes to the branched path as [above](#ii-pick-a-subsequent-point), i.e., Create a temporary path and confirm it. When you decide to complete the path you should see in the Path Manager that it has been recorded as a child of the existing path.

<div align="center">
  <img src="/media/plugins/snt/snt-sb-temporary-path-2.png" title="1) Temporary path branching-off" width="33%" alt="1) Temporary path branching-off" />
  <img src="/media/plugins/snt/snt-sb-confirmed-path-2.png" title="2) Temporary path confirmed" width="33%" alt="2) Temporary path confirmed" />
  <img src="/media/plugins/snt/snt-sb-completed-branch-2.png" title="3) Branched (child) path completed" width="33%" alt="3) Branched (child) path completed" />
</div>

## Accurate Point Placement
{% include notice icon="info" content=op1-demo-incomplete %}
<table>
  <tbody>
    <tr style="background-color:white">
      <td>
        <p>Accurate node placement requires <em>XY</em>, <em>ZY</em> and <em>XZ</em> views to be visible. You can do so at <a href="/plugins/snt/manual#startup-prompt">startup</a>, by making sure that <em>Default: XY, ZY and XZ views</em> is selected, or by clicking in <em>Display ZY/XZ Views</em> in the <a href="/plugins/snt/manual#options-tab">Options tab</a> if you have already started SNT.</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-three-pane-view-enabled-startup-prompt.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>Find the approximate location of your start point by moving your mouse in the XY window, holding down {% include key key='Shift' %} to synchronize the view in the other panes.</p>
        <p>At this point, you should enable cursor <a href="/plugins/snt/manual#cursor-auto-snapping">auto-snapping</a> in the <a href="/plugins/snt/manual#main-tab">Main tab</a> using suitable parameters for your image. When this option is enabled, the cursor will automatically 'sniff' for local maxima and 'snap' to their average X,Y,Z position. The pixel that is most likely to be on a neurite is indicated by the red cross-hair cursor.</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-1.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>When you press {% include key key='+' %} to zoom in, all the panes will zoom in on the point that the crosshair is over, so each time you press {% include key key='+' %}, make sure you move your mouse pointer over the neurite so that it's still over the structure of interest. You may want to adjust in the <a href="/plugins/snt/manual#views">Views</a> widget (<a href="/plugins/snt/manual#options-tab">Options tab</a>) whether all views should zoom synchronously.<br>
        At this point, you should adjust a suitable <a href="/plugins/snt/manual#cursor-auto-snapping">snapping neighborhood</a> both in XY (2D), and optionally Z (3D).</p>
        <p>Note that when Z-snapping is enabled, all views become synchronized,</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-2.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>Locate the center of the structure to be clicked on. If <a href="/plugins/snt/manual#cursor-auto-snapping">cursor auto-snapping</a> is enabled, simply mouse over the structure, otherwise, try moving the mouse and scroll wheel in each of the panes (holding down {% include key key='Shift' %} so synchronize the views in all three panes). Note that you can toggle the cursor auto-snapping feature at will, by pressing the <a href="/plugins/snt/key-shortcuts">shortcut</a> {% include key key='S' %}. Also, note that you can "click" on the <a href="/plugins/snt/key-shortcuts#tracing">brightest voxel</a> of a voxel column, by pressing {% include key key='M' %}.</p>
        <p>When you're happy with the point under the crosshairs, left-click to start the path:</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-3.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>Zoom out again with the {% include key key='-' %} key, and similarly zoom in on the next point you want to be on your path to place it precisely:</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-4.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>The path along the neuron may not follow the center line perfectly:</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-5.png" width="300">
      </td>
    </tr>
    <tr style="background-color:white">
      <td>
        <p>... but you can later improve that with the {% include bc path='Refine/Fit|Fit Path...'%} option in the <a href="/plugins/snt/manual#path-manager">Path Manager</a>, which tries to align the path to the midline of the structure to sub-voxel accuracy:</p>
      </td>
      <td>
        <img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-6.png" width="300">
      </td>
    </tr>
  </tbody>
</table>

## Tracing in the Legacy 3D Viewer

### I. Starting the Viewer

<img align="right" src="/media/plugins/snt/snt-3d-dialog.png" title="The legacy 3D Viewer remains a functional canvas" width="300px"/>
It remains possible to trace in the legacy 3D Viewer. To open it, select the *3D* menu tab in the SNT dialog and look for *Legacy 3D Viewer*. You will see 3 parameters:

- Select *New with image* from the *Viewer* drop-down menu (selecting *New without image* would only allow you to look at reconstructions without the underlying signal). Note that you can recycle existing viewers you may have open by choosing their window titles from the drop-down menu.

- Select the preferred rendering style from the *Mode* drop-down menu.

- Once you *Apply* the viewer choice, a prompt will appear asking you to choose the resampling factor for the image. Then, the viewer window will appear with the currently open image.
  <img align="right" src="/media/plugins/snt/snt-image-resampling-factor.png" title="Legacy 3D Viewer resampling prompt" width="300px"/>

### II. Tracing and Navigation
<img  align="left" src="/media/plugins/snt/snt-legacy-3d-viewer.png" title="3D viewer showing OP_1.tif" width="300"/>

###### Selecting points for tracing
Select the *Wand tool* ({% include key key='W' %} [shortcut](/plugins/snt/key-shortcuts#legacy-3d-viewer)) in the main ImageJ toolbar and click over the region you want to trace. Tracing works the same way as in the 2.5D view, i.e., click somewhere in the image to create a starting point, then click further along the structure of interest to find a path between the two points, then confirm or deny the temporary segment as described [above](#iii-confirm-the-temporary-segment). Similarly, branching occurs as [described for 2D canvas(es)](#branching-start-a-path-on-an-existing-path), by holding the {% include key keys='Alt|Shift' %} modifier.

###### Navigation
**Rotation** Either use the *Hand tool* ({% include key key='H' %} [shortcut](/plugins/snt/key-shortcuts#legacy-3d-viewer)) tool and left-click while dragging the mouse or drag mouse while holding the scroll wheel

**Translation** Hold {% include key key='Shift' %} and the scroll wheel while dragging the mouse.

**Adjusting zoom depth** Scroll using the mouse wheel.

NB: Once you have selected the Wand and Hand tools once, you should be able to switch between them by pressing the {% include key key='Esc' %} key. See [Key Shortcuts](/plugins/snt/key-shortcuts#legacy-3d-viewer) for the list of all supported shortcuts.

# Merging/Joining Paths

{% include notice icon="info" content=op1-demo-incomplete %}
Two paths can be merged or joined in *Edit Mode*. To do so:

1. Select a path and enter *Edit Mode* (by right-clicking on the image canvas to access its [contextual menu](/plugins/snt/manual#contextual-menu)
2. Activate the node to be merged by hovering over it
3. Select the second path by using the {% include key key='G' %} [shortcut](/plugins/snt/key-shortcuts) and activate the second merging node by hovering over it
4. Open the contextual menu and select the initial path from the *Connect To (Start Join)* / *Connect To (End Join)* menu

<div style="text-align: center;">
<img style="vertical-align:top" src='/media/plugins/snt/snt-edit-path-connect-to-step-1.png' width="20%" title='1) Select parent path and activate first join node'>
<img style="vertical-align:top" src='/media/plugins/snt/snt-edit-path-connect-to-step-2.png' width="20%" title='2) Select child path and activate second join node'>
<img style="vertical-align:top" src='/media/plugins/snt/snt-edit-path-connect-to-step-3.png' width="24%" title='3) Use the contextual-menu option to connect child path to parent path'>
<img style="vertical-align:top" src='/media/plugins/snt/snt-edit-path-connect-to-result.png' width="20%" title='4) Joined result'>
</div>


**Important Notes**:
- If both nodes are terminal, the paths are merged together. Otherwise, one path will become a child of the other. Note that one of the nodes must be terminal, to ensure no loops are created.
- The direction of merge matters, and it is assumed to be always from parent to child. If the child path is oriented in the wrong direction (i.e., moving “towards” its parent at the point of merge), it will be re-oriented so that single root connectivity is maintained
- Loop-forming connections are not allowed
- The recommended way to concatenate or combine paths is to use the respective commands in Path Manager's [Edit menu](/plugins/snt/manual#edit)

# Full-automated Tracing
{% capture ddac-demo%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _Drosophila ddaC neuron (Autotrace demo)_. It will load a binary (thresholded) image of a Drosophila space-filling neuron (ddaC) displaying autotracing options for automated reconstruction.
{% endcapture %}
{% include notice icon="info" content=ddac-demo %}

## Input Image(s)
Full automated tracing requires two types of inputs:

1. **Segmented Image (*Mandatory*)** The pre-processed image from which paths will be extracted. It will be [skeletonized](/plugins/skeletonize3d) by the extraction algorithm. If thresholded (recommended), only highlighted pixels are considered, otherwise all non-zero intensities in the image will be considered for extraction.

2. **Original Image (*Optional*)** The original (un-processed) image used to resolve any possible loops in the segmented image using brightness criteria. If available: loops will be nicked at the dimmest voxel of the dimmest branch in the detected loop. If unavailable: Loops will be nicked at the shortest branch in the loop.

## Soma/Root Detection
Root detection requires an area ROI marking the root of the arbor exists on the image. With neurons, this typically corresponds to an area ROI marking the soma. Three strategies are possible:

- **Place root on ROI's centroid** Attempts to root all of primary paths intersecting the ROI at its centroid. Typically, this option is used when 1) multiple paths branch out from the soma of the cell, 2) the ROI defines the contour of the soma, and 3) somatic segments are expected to be part of the reconstruction.

- **Place roots along ROI's edge** Attempts to root all of primary paths intersecting along the perimeter of the ROI. As above, this option is typically used when multiple paths branch out from the soma of the cell and the ROI defines the contour of the soma, but somatic segments are not expected to be included in the reconstruction.

- **ROI marks a single root** Assumes a polarized morphology (e.g., apical dendrites of a pyramidal neuron), in which the arbor being reconstructed has a single primary branch at the root. Under this option, the 'closest' end-point (or junction point) contained by the ROI becomes the root node. In this case the ROI does not need to reflect an accurate contour of the soma.

- **None. Igore any ROIs** If no ROI exists an arbitrary root node is used.

When parsing 3D images, toggling the *Restrict to active plane* checkbox clarifies that the root(s) marked by the ROI occurs at the active ROI's Z-plane. This ensures that other possible roots above or below the ROI will not be considered.

## Gaps and Disconnected components
It is almost impossible to segment structures into a single, coherent volume. These options define how gaps in the segmentation should be handled.

- **Settings for handling small components** These options determine whether the algorithm should ignore segments (connected components that are disconnected from the main structure) that are too small to be of interest. Disconnected segments with a cable length below the specified *length threshold* will be discarded by the algorithm.<br>Increase this value if too many isolated branches are being created. Decrease it to bias the extraction for larger, contiguous structures.

- **Settings for handling adjacent components** If the segmented image is fragmented into multiple components (e.g., due to 'beaded' staining): Should the algorithm attempt to connect nearby components? If so, what should be the maximum allowable distance between disconnected components to be merged?<br>You should increase *Max. connection distance* if the algorithm produces too many gaps. Decrease it to minimize spurious connections.

Information on other options in the prompt can be accessed through the tooltip text that is displayed when hovering the mouse above them.

<div align="center">
  <img src="/media/plugins/snt/snt-fully-automated-reconstructions.png" title="Fully automated reconstructions (ddaC demo dataset)" width="850" />
</div>

# Spine/Varicosity Analysis
{% capture spines-demo%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _L-systems fractal (Toy neuron)_ dataset, as it contains pre-placed multipoint ROIs emulating markers for dendritic spines.
{% endcapture %}
{% include notice icon="info" content=spines-demo %}

This type of analysis uses (manually placed) multi-Point ROIs along paths as markers for neurite features such dendritic spines or axonal varicosities. Currently only counts and densities are supported. A typical workflow would proceed as follows.

 1. Right-click on the image being traced and choose _Count Spine/Varicosities_ from the [contextual menu](/plugins/snt/manual#contextual-menu). SNT will pause, the multipoint tool will be selected, and a floating dialog (that can be dismissed at will) displays a summary of these instructions
 2. Click over the features to be counted. Point placement may not need to be accurate, but with 3D images points should be placed on the same plane (Z-plane) the feature being counted
 3. Once you have placed all the points, select the Path(s) associated with the features (or select none, if all Paths are to be considered) and run Path Manager's {% include bc path='Analyze|Spine/Varicosity Utilities|Extract Counts from Multi-point ROIs...' %}. The dialog allows you to specify:
   
    - **Source of Multi-point ROI(s)** The location of the markers. Particularly useful if the ROIs are being generated programmatically and stored in the ROI Manager
   
    - **Max. association distance** The maximum allowed distance between a point and its path in physical units. This option is ignored if set to -1 (the default). This works as follows: for every point ROI, the closest path node is identified. ROI is only considered to be associated with Path if its distance to the closest path node is less than or equal to _Max. association distance_.
   
    - **Add extracted counts to ROI Manager** Generates new ROIs from the assigned counts and adds them to the ROI Manager. This allows you to validate the extraction and ensure the assignments are correct, as each ROI gets tagged by its associated Path.

NB:

- Point ROIs can also be generated programmatically or in a semi-automated way, e.g.:
  - Create a freehand area ROI around the path(s) of interest
  - Run ImageJ's {% include bc path='Process|Find Maxima...' %}. Detection will be restricted to freehand selection

- SNT only keeps a tally of the features being counted and location of ROIs are not saved in .traces files, so you may want to save the multipoint ROis for future reference

- ImageJ has several ways to expedite handling of multipoint ROIs:
  - {% include key key='left click' %} on a point and drag to move it
  - {% include key key='alt|left click' %} on a point to delete it
  - To delete multiple points, create an area selection while holding down {% include key key='alt' %}
  - Use {% include bc path='Edit|Selection|Select None' %} to delete a multi-point selection
  - Use {% include bc path='Edit|Selection|Restore Selection' %} to restore a deleted multipoint selection
  - {% include key key='double click' %} on the Multi-point tool in the ImageJ toolbar for further options

# Time-lapse analysis
{% capture timelapse-demo%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _Hippocampal neuron (DIC timelapse)_ dataset: It features a timelapse video of a cultured neuron in which neurites have been traced across time.
{% endcapture %}
{% include notice icon="info" content=timelapse-demo %}

1. Specify the first time-point to be traced using the [Data Source](/plugins/snt/manual#data-source) widget.
2. Trace the path of interest
3. Repeat 1. and 2. for all the frames to be traced
4. Run Path Manager's {% include bc path='Analyze|Time-lapse Utilities|Match Path(s) Across Time...' %}. The dialog allows you to match paths in the same time-series, by specifying several criteria:

    - **Time points** Only paths associated with these time-points (frames) will be considered for matching. Range(s) (e.g. <tt>2-14</tt>), and comma-separated list(s) (e.g. <tt>1,3,20,22</tt>) are accepted. Leave empty or type <tt>all</tt> to consider all frames

    - **Matching criteria** These are a series of conditions that matching paths must fulfill. Some require no further adjustments (e.g., _channel_, _path order_, _type tag_, _color tag_) while others (described below) have configurable settings. Criteria can be combined E.g., if _channel_ and _type tag_ are selected, paths need to share the same channel and the same type tag ('Axon', 'Dendrite', etc.) to be matched. 

       The criteria with configurable settings are perhaps the most commonly used:

      - **Starting node location** If selected, matching paths need to share a common origin (starting node) in terms of (X, Y, Z) coordinates. Sample movement and focus drift are common during time-lapse sequences. To account for this, it is possible to specify a (X, Y, Z) 'motion-shift' neighborhood: Paths that originate within this neighborhood (in spatially calibrated units) are considered to share the same starting node location

      - **Custom tag** If selected, matching paths need to share the specified (case sensitive) tag. A regex pattern can also be specified

5. Once paths have been matched across the time-lapse future analysis becomes simplified. {% include bc path='Analyze|Time-lapse Utilities|Time Profile...' %} can be used to e.g. plot growth across time. {% include bc path='Time Profile...' %} includes the following options:

      - **Metric** the measurement to be profiled across time

      - **Grouping strategy** Typically this would be set to _Matched path(s) across time_ to reflect the matching performed in 4. However, if there are many short-lived neurites (i.e., only visible in few frames) it may be beneficial to choose  _Matched path(s) across time (≥2 time-points)_. This will only consider paths present in two or more frames. A _no grouping_ strategy is also available for cases where step 4 was skipped.

      - **Output** Whether a plot, a table or both should be created

# Filling
{% capture op1-demo-full%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _Drosophila OP neuron (Complete 3D reconstruction)_ dataset.
{% endcapture %}
{% include notice icon="info" content=op1-demo-full %}
<img align="right" src="/media/plugins/snt/fill-manager-v420.png" title="Fill Manager (v4.2.0)." width="275" />
Paths can be "filled out" to volumes, i.e., converted into 3D images that can be used to improve the visualization of the shape of a neuron beyond what can be seen from traced center-lines, and/or subsequent image processing routines. The filling algorithm uses the center-line path coordinates as seeds in a '[signal search](#iii-understanding-fill-distances-and-distance-threshold)' that expands along neurites to encapsulate the neurite in 3D. The result can be exported as different types of images, including distance maps, binary masks or labeled image.

Fillings are controlled by the Fill Manager and share many of the same properties of auto-tracing:

- Fillings can be performed on the main image or secondary tracing layer

- The same cost function used in auto-tracing is used for filling

- Fillings will be more accurate once SNT is aware of properties of the image being traced, so before filling imported paths you may need to re-trace a representative neurite (you can discard the result)


### I. Starting the Fill

First, select the one or more paths that you want to fill out from in the Path Manager and select {% include bc path="Fill|Fill Out..." %} in the Path Manager (or select none if you want to fill all the existing paths). Once the filling starts, you should be able to see a thick green surround the path while scrolling through the 3D stack:

The filler continues to explore the image until you click "Pause" or "Stop" in the dialog, or until all the image has been fully explored. However, the fill which is shown only includes those points up to a certain threshold distance from the path. Note that this "distance" doesn't mean a real physical distance, but instead a 'likelihood-distance': a measure which takes into account the intensity values of the pixels which must be [passed through when moving away from the path](#iii-understanding-fill-distances-and-distance-threshold). Information about the current threshold and the progress of the search is shown in the dialog. Note that if your image is rather small, the entire image may be fully explored before you have time to interact with prompt.
<img align="right" src="/media/plugins/snt/snt-initial-filling-2.png" title="A few seconds after selecting 'Fill Out...' with 1 path selected" width="350" />
The "Cursor position:" state under "Search Status" is updated as you move your mouse over the image. If the point under the mouse has been reached by the search then it will show you that point's distance from the path. Otherwise, it will read "Not reached by search yet". 

The _Search status_ shows your current [threshold distance](#iii-understanding-fill-distances-and-distance-threshold): so if this is set to 0.2 then that means that all points less than 0.2 from the path are included in the fill (and highlighted in green in the image). The "Max. explored distance:" shows the maximum distance from the path that has been completely explored.

### II.Adjusting the Fill Threshold

You can change the fill threshold in one of three ways:

- Clicking on a point in the image that has been reached by the search (This is the most intuitive way of altering the threshold). It may be helpful to disable the "Enable Snapping within: XY-Z" feature for the cursor while doing this

- Manually changing the threshold in the "Specify manually:" input box and clicking the "Apply" button beside it.

- Clicking the "Use explored maximum" button below the threshold input box and click "Apply", which sets the threshold to the maximum explored distance (the value shown in "Max. explored distance:" under the "Search Status" dialog).

We will assume that you want to use the first of these approaches:

- It is difficult to set the threshold accurately from the image unless you zoom in, so first zoom on part of the path that you want to set the threshold for.

- Since the solid green fill obscures the intensity value of the points in the fill, you may want to activate the _Transparent overlay_ checkbox. Note that this _could_ slow down filling, although the performance hit is usually negligible. 

- As you can see in the middle image, the threshold is set too far from the path, since there are many background voxels under the green fill, as well as voxels on different paths than those of interest. Experiment with clicking on different locations closer to the path in order to adjust the threshold until you are satisfied with thr result. You might end up with something like the rightmost image:

<div align="center">
  <img src="/media/plugins/snt/snt-zoomed-filling-2.png" title="Fill, opaque" width="250" alt="Fill, opaque" />
  <img src="/media/plugins/snt/snt-transparent-filling-2.png" title="Fill, with 'Transparent overlay' on" width="250" alt="Fill, with 'Transparent overlay' on" />
  <img src="/media/plugins/snt/snt-refined-filling-2.png" title="Fill, refined" width="250" alt="Fill, refined" />
</div>

### III. Understanding Fill Distances and Distance Threshold

Fill distances must be interpreted as  ‘likelihood distances’.

> Pixels associated with *low distances* are likely associated with the traced path. Pixels associated with *high distances* are unlikely to be associated with the path.

The smallest distance  corresponds to a perfect match to whatever information the filler has on the center-line of the traced path, and the highest distance correspond to the _worst_ match. When a threshold is set, pixels are clustered into two groups: those that ‘fill’ the path and those above threshold that don't.

Note that *likelihood distances* are under an arbitrary range. Consider a scale ranging from ]0 to 1]: If the threshold distance is set at 0.2, paths are only ‘filled’ with voxels that share at least 80% *likelihood* with the traced center-lines. In practice, the upper limit of this distance depends on much of the image has been explored by the algorithm. Thus, it is not trivial to define _a priori_ a sensible threshold. It should be  assumed that the range of possible distances falls between 0 (perfect likelihood, i.e., center-line voxels themselves) and a _maximum_ corresponding to the most distinct voxel to the path center-line. Such voxel of "maximum difference" is expected to belong to the image background (unlabeled neurite). Distances can be studied by exporting fills as [Distance maps](#v-exporting).

While adjusting the _distance threshold_ is the single most effective way to improve 'fills', other approaches can also improve the result:

- **Adopt secondary layers**: Currently, the filler only looks at pixel intensities, and thus likelihood is a simple comparison of gray value intensities, but note that other _features_ can be used by the algorithm, when a [secondary tracing layer](/plugins/snt/manual#tracing-on-secondary-image-layer) is used. E.g., If the filling occurs in a [Tubeness](/plugins/tubeness) flavor of the image, then distances reflect likelihoods of association with tube-like structures.

- **Optimize center-lines**: Since center-line pixes function as seeds, ensuring they follow closely the curvatures of the fluorescence signal using [Path fitting](/plugins/snt/manual#refinefit) may improve the result

### IV. Completing the Fill

If the search is still active, you might as well click "Pause" so halt exploration of the image. Then you can either:

- Save the fill (which will add it to the fill list) by clicking "Store"

- Discard the fill by either clicking "Cancel/Discard" while filling is in progress or, if you stashed the fill, select it in the fill list and click "Delete"

### V. Exporting 

- The "Export" button provides several export options, including:

  - Binary mask: Only the points in the fill are preserved under a constant value. This is useful to e.g., mask out structures outside the neuron being traced, or to train a [Weka model](/plugins/tws).

  - Grayscale: Only the points in the fill are preserved under the original pixel intensities. This is useful to e.g., render the structure in the [legacy 3D Viewer](/plugins/3d-viewer) or [sciview](/plugins/sciview) to do a surface rendering of the neuron.

  - Labels: Each group of paths (Tree) gets assigned a unique pixel value so that such groups are distinguishable from each other. Note that scripting can be used to extend this option to individual paths so that each path in a group gets assigned a unique label (see the *Fill_Demo.py* script and this [discussion](https://forum.image.sc/t/batch-filling-in-snt/58733/7) for details)

  - Annotated Distance map: Points along the fill are assigned the _explored distance_ as described earlier. Useful for debugging and/or perusing the fill operation

  - CSV export: Exports details of the filling operation as tabular data. This includes [distance thresholds](#iii-understanding-fill-distances-and-distance-threshold), algorithms used, and volumes of filled paths

<div align="center">
  <img src="/media/plugins/snt/filling-output-examples.png" title="Fill Manager export options as demoed by the Fill_Demo.py script. Properties of fills can also be exported to CSV files." width="850" />
</div>

{% capture text%}
Currently, only the output images/CSV summary of fills can be exported. TRACES files contain only the search parameters of fill operations which allows SNT to recapitulate the search when files are reopened. No information on fills is stored in [SWC files](/plugins/snt/faq#in-which-format-should-i-save-my-tracings-traces-or-swc).
{% endcapture %}
{% include notice icon="info" content=text %}

# Generating *Filtered Images* in Bulk

This section describes how to generate [Filtered Images](/plugins/snt/manual#tracing-on-secondary-image-layer) outside SNT in bulk. Note that there are [many tutorials](/scripting/batch) on this topic. Arguably, the easiest way to process multiple images is to 1) record a macro that processes a single image, then 2) wrap it in a loop to iterate over all files in a directory. For example, using IJ1 macro language:

{% highlight javascript %}
d = getDirectory("Select a directory");
files = getFileList(d);
extension = ".tif";

for( i = 0; i < files.length; ++i ) {
    filename = files[i];
    if( endsWith(filename,extension) ) {
        l = lengthOf(filename);
        el = lengthOf(extension);
        basename = substring(filename,0,l-el);
        expected_window_name = "result";
        output_filename = d + File.separator + basename + ".tubes.tif";
        open(filename);
        run("Gaussian Blur...", "sigma=2 scaled stack"); // processing step here
        selectWindow(expected_window_name);
        saveAs("Tiff", output_filename);
    }
}
{% endhighlight %}

The same process can be accomplished more completely in a script using [ImageJ Ops](/libs/imagej-ops). For example, in Jython:

{% include code org='morphonets' repo='SNT' branch='master' path='src/main/resources/script_templates/Neuroanatomy/Batch/Filter_Multiple_Images.py' label='Filter Multiple Images (Python)' %}
