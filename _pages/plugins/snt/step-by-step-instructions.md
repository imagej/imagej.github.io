---
mediawiki: SNT:_Step-By-Step_Instructions
title: SNT › Step-By-Step Instructions
nav-links: true
nav-title: Step-By-Step Instructions
---

# Tracing

These instructions assume that you have read the [Overview](/plugins/snt/manual) page, including starting up the plugin, enabling [Cursor Auto-snapping](/plugins/snt/manual#auto-snapping), and [Auto-tracing](/plugins/snt/manual#auto-tracing) options. This section is also documented in a [Screencast](/plugins/snt/screencasts#introduction-to-tracing).

## Starting A Path

### I. Pick The Starting Point

<img src="/media/plugins/snt/snt-cropped-before-starting-2.png" title="fig:Choosing a starting point" width="400" alt="Choosing a starting point" /> You may notice that, by default, the cursor [snaps](/plugins/snt/manual#auto-snapping) to the brightest pixel in its vicinity. If you prefer to manually control the placement of nodes, feel free to toggle feature by pressing {% include key key='S' %}. Now, to begin tracing, move through the image stack to find the start point of a path then click there with the left mouse button.

### II. Pick A Subsequent Point

<img src="/media/plugins/snt/snt-cropped-after-starting-2.png" title="fig:First point of a path selected" width="400" alt="First point of a path selected" /> <img src="/media/plugins/snt/snt-cropped-mid-tracing-2.png" title="fig:A* search animated progress" width="400" alt="A* search animated progress" /> A small circle should appear, highlighting the start of the path. Move through the stack to find a subsequent point further along the same structure to be traced (neuron, blood vessel, etc.), and click there.

If a path between the two points cannot be found immediately, you may see the animated progress of the search. You can scroll through the stack while such a search progresses: If it appears to not be making good progress, it's probably best to press the "Cancel/Esc" button (shortcut: {% include key key='C' %}/{% include key key='Esc' %}) and pick a point closer to the start point. {% include notice icon="tip" content='Increase *Z* in the *Cursor Auto-snapping* panel for automated Z-navigation on signal mouseover.' %}

### III. Confirm The Temporary Segment

Once the search has reached the target point, the path is shown in cyan (to indicate that this is still a temporary path) and you are asked to confirm (by clicking "Yes" or pressing {% include key key='Y' %}) that this path is following the route through the image that you expect. If it is not, then click "No" {% include key key='N' %} and you'll go back to the [previous step](#ii-picking-a-subsequent-point). Assuming you confirmed the path, the confirmed path will appear in red. Now you are essentially back at [step II](#ii-picking-a-subsequent-point). Normally you will go on to pick further points along the structure. However, if you have finished with that path, click "Finish Path" {% include key key='F' %} and you will go back to [step I](#i-picking-a-start-point). If you completed that path it would be shown in magenta.

<div align="center">

-   <img src="/media/plugins/snt/snt-cropped-confirmation-2.png" title="fig:A* search completed" width="400" alt="A* search completed" />
-   <img src="/media/plugins/snt/snt-cropped-confirmed-2.png" title="fig:A confirmed segment" width="400" alt="A confirmed segment" />
-   <img src="/media/plugins/snt/snt-cropped-completed-path-2.png" title="fig:A completed path" width="400" alt="A completed path" />

</div>

## Branching: Start A Path On An Existing Path

### I. Select The Path To Branch Off

To select the path you want to branch off from, you can either select it in the Path Manager, or press {% include key key='G' %} while the mouse pointer is near the path. When the path is first selected, it will be shown in the default green color. <img src="/media/plugins/snt/snt-sb-selecting-by-g.gif" title="fig:Holding &#39;G&#39; (Group paths around cursor) will select the closest path to the mouse pointer" width="600" alt="Holding &#39;G&#39; (Group paths around cursor) will select the closest path to the mouse pointer" />

### II. Select The Fork Point

<img src="/media/plugins/snt/snt-sb-started-branch-2.png" title="fig:A newly created fork point" width="400" alt="A newly created fork point" /> To force the start of the new path to be a branch of the selected path, hold down the {% include key keys='Alt|Shift' %} keys while you move the mouse to find the branch point under the red cross-hairs, now decorated with a "Fork Point" annotation. With {% include key keys='Alt|Shift' %} held down, click with the left mouse button. Finally, release the keys. Note that it is also possible to zoom into the branch point, right-click on the image and choose *Fork at Nearest Node* from the contextual menu.

### III. Extend The Path

From this point on, you can carry on adding nodes to the branched path as [above](#ii-pick-a-subsequent-point), i.e., Create a temporary path and confirm it. When you decide to complete the path you should see in the Path Manager that it has been recorded as a child of the existing path.

<div align="center">

-   <img src="/media/plugins/snt/snt-sb-temporary-path-2.png" title="fig:1) Temporary path branching-off" width="400" alt="1) Temporary path branching-off" />
-   <img src="/media/plugins/snt/snt-sb-confirmed-path-2.png" title="fig:2) Temporary path confirmed" width="400" alt="2) Temporary path confirmed" />
-   <img src="/media/plugins/snt/snt-sb-completed-branch-2.png" title="fig:3) Branched (child) path completed" width="400" alt="3) Branched (child) path completed" />

</div>

## Joining: End A Path On An Existing Path

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>Supposing you want the end of a path that you're tracing to join onto an existing path, you just use the same modifier key when selecting the end point of the last part of the path. To go into that in more detail, if you're halfway through tracing a path like [1]:</p>
      </td>
      <td>
        <figure>
          <img src="/media/plugins/snt/snt-ej-cropped-half-finished-2.png" title="[1] Unfinished join segment, in red - disconnected" width="350" alt="[1] Unfinished join segment, in red - disconnected">
          <figcaption aria-hidden="true">
            <span style="text-align:center;font-size:90%">[1] Unfinished join segment, in red - disconnected</span>
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <td>
        <p>... and you want the final part of that path to join up with the existing path running from the top-left to top-right of the image. First, select that path in the path list (or using the {% include key key='G' %} shortcut) as in [2]:</p>
      </td>
      <td>
        <figure>
          <img src="/media/plugins/snt/snt-ej-cropped-selected-destination-path-2.png" title="[2] Selected path to join to, in green" width="350" alt="[2] Selected path to join to, in green">
          <figcaption aria-hidden="true">
            <span style="text-align:center;font-size:90%">[2] Selected path to join to, in green</span>
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <td>
        <p>Now hold down {% include key keys='Alt|Shift' %} to restrict the endpoint to be a "join" on that existing path. Click (while still holding down the modifier keys) to start the search for that endpoint and make it join the existing path. If the search can find a path to the end point, the result should look like [3]:</p>
      </td>
      <td>
        <figure>
          <img src="/media/plugins/snt/snt-ej-cropped-end-join-created-2.png" title="[3] Connected path to join, unconfirmed" width="350" alt="[3] Connected path to join, unconfirmed">
          <figcaption aria-hidden="true">
            <span style="text-align:center;font-size:90%">[3] Connected path to join, unconfirmed</span>
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <td>
        <p>If you're happy with the result, confirming the temporary path will automatically complete the whole path, since if you're creating an end join there cannot be any more to the path. Note that the path list indicates that this new <em>Path (1)</em> ends on the existing <em>Path (0)</em>. The result will look like [4]:</p>
      </td>
      <td>
        <figure>
          <img src="/media/plugins/snt/snt-ej-cropped-path-completed-2.png" title="[4] Confirmed join" width="350" alt="[4] Confirmed join">
          <figcaption aria-hidden="true">
            <span style="text-align:center;font-size:90%">[4] Confirmed join</span>
          </figcaption>
        </figure>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## Merging/Joining Paths

Two paths can be merged or joined in *Edit Mode*. To do so:

1.  Select a path and enter *Edit Mode* (by right-clicking on the image canvas to access its [Contextual menu](/plugins/snt/manual#contextual-menu))
2.  Activate the node to be merged by hovering over it
3.  Select the second path by using the {% include key key='G' %} [shortcut](/plugins/snt/key-shortcuts) and activate the second merging node by hovering over it
4.  Open the contextual menu and select the initial path from the *Connect To (Start Join)* / *Connect To (End Join)* menu.

If both nodes are terminal, the paths are merged together. Otherwise, one path will become a child of the other. Note that one of the nodes must be terminal, to ensure no loops are created.

<div align="center">

-   {% include thumbnail src='/media/plugins/snt/snt-edit-path-connect-to-step-1.png' title='none\|250px\|1) Select parent path and activate first join node'%}
-   {% include thumbnail src='/media/plugins/snt/snt-edit-path-connect-to-step-2.png' title='none\|250px\|2) Select child path and activate second join node'%}
-   {% include thumbnail src='/media/plugins/snt/snt-edit-path-connect-to-step-3.png' title='none\|250px\|3) Use contextual-menu option to connect child path to parent path'%}
-   {% include thumbnail src='/media/plugins/snt/snt-edit-path-connect-to-result.png' title='none\|250px\|4) Joined result  
     '%}

</div>

## Tracing in the Legacy 3D Viewer

It remains possible to trace in the legacy 3D Viewer. ![](/media/plugins/snt/snt-3d-dialog.png)

### I.Starting the Viewer

To open the viewer, select the *3D* menu tab in the SNT dialog and look for *Legacy 3D Viewer*. You will see 3 parameters: ![](/media/plugins/snt/snt-image-resampling-factor.png)

-   Select *New with image* from the *Viewer* drop-down menu (selecting *New without image* would only allow you to look at reconstructions without the underlying signal). Note that you can recycle existing viewers you may have open by choosing their window titles from the drop-down menu.
-   Select the preferred rendering style from the *Mode* drop-down menu.
-   Once you *Apply* the viewer choice, a prompt will appear asking you to choose the resampling factor for the image. Then, the viewer window will appear with the currently open image.

<figure><img src="/media/plugins/snt/snt-legacy-3d-viewer.png" title="3D viewer showing OP_1.tif" width="300" alt="3D viewer showing OP_1.tif" /><figcaption aria-hidden="true">3D viewer showing OP_1.tif</figcaption></figure>

### II.Tracing and Navigation

-   **Selecting points for tracing** Select the *Wand tool* ({% include key key='W' %} [shortcut](/plugins/snt/key-shortcuts#legacy-3d-viewer)) in the main ImageJ toolbar and click over the region you want to trace. Tracing works the same way as in the 2.5D view, i.e., click somewhere in the image to create a starting point, then click further along the structure of interest to find a path between the two points, then confirm or deny the temporary segment as described [above](#Tracing). Similarly, branching occurs as [described for 2D canvas(es)](#Branching:_Start_A_Path_On_An_Existing_Path), by holding the {% include key keys='Alt|Shift' %} modifier.
-   **Rotation** Either use the *Hand tool* ({% include key key='H' %} [shortcut](/plugins/snt/key-shortcuts#legacy-3d-viewer)) tool and left-click while dragging the mouse or drag mouse while holding the scroll wheel.
-   **Translation** Hold {% include key key='Shift' %} and the scroll wheel while dragging the mouse.
-   **Adjusting zoom depth** Scroll the mouse wheel.

Once you have selected each of these tools (Wand and Hand) once, you should be able to switch between them by pressing the {% include key key='Esc' %} key. See [Key Shortcuts](/plugins/snt/key-shortcuts#legacy-3d-viewer) for the list of all supported shortcuts. ![](/media/plugins/snt/fiji-toolbar-wand-and-hand-2.png)

# Filling

There is a simple facility in this plugin for "filling out" paths to volumes. This is not particularly sophisticated, but often good enough for a rough visualization of the shape of a neuron beyond what can be seen from the traced path.

### I.Starting the Fill

First, select the one or more paths that you want to fill out from in the Path Manager and select {% include bc path="Fill | Fill Out..." %} in the Path Manager menu options. The selected paths are shown in green so that you can check that you're starting from the right ones. After a couple of seconds if you scroll through the stack you should be able to see a thick green surround the path:

<figure><img src="/media/plugins/snt/snt-initial-filling-2.png" title="A few seconds after selecting &quot;Fill Out...&quot; with 1 path selected" width="400" alt="A few seconds after selecting &quot;Fill Out...&quot; with 1 path selected" /><figcaption aria-hidden="true">A few seconds after selecting "Fill Out..." with 1 path selected</figcaption></figure>

The filler continues to explore the image starting from the path until you click "Pause" or "Stop" in the dialog. However, the fill which is shown only includes those points up to a certain threshold distance from the path. (Note that in this section "distance" doesn't mean a real physical distance, but a measure which takes into account the intensity values of the pixels which must be passed through when moving away from the path.) Information about the current threshold and the progress of the search is shown in the dialog. ![The filling-related part of the dialog.](/media/plugins/snt/snt-filling-statistics-2.png) The "Cursor position:" state under "Search Status" is updated as you move your mouse over the image. If the point under the mouse has been reached by the search then it will show you that point's distance from the path. Otherwise, it will read "Not reached by search yet". Two lines above, the "Current threshold distance:" shows your current threshold distance: so if this is set to 0.2 then that means that all points less than 0.2 from the path are included in the fill (and shown in green in the image.) The "Max. explored distance:" state under this line shows the maximum distance from the path that has been completely explored.

### II.Adjusting the Fill Threshold

You can change the fill threshold in one of three ways:

-   Clicking on a point in the image that has been reached by the search (This is the most intuitive way of altering the threshold). It may be helpful to disable the "Enable Snapping within: XY-Z" feature for the cursor while doing this.
-   Manually changing the threshold in the "Specify manually:" input box and clicking the "Apply" button beside it.
-   Clicking the "Use explored maximum" button below the threshold input box and click "Apply", which sets the threshold to the maximum explored distance (the value shown in "Max. explored distance:" under the "Search Status" dialog).

Anyway, assuming that you want to use the first of these approaches, you should use the approach described below. It is difficult to set the threshold accurately from the image unless you zoom in, so first zoom on part of the path that you want to set the threshold for.

Since the solid green fill obscures the intensity value of the points in the fill, I suggest that you switch to the semi-transparent view of the fill at this stage by selecting the "Transparent overlay" option in the "Rendering Options" dialog. Note that this may slow down filling.

As you can see in the middle image, the threshold is set too far from the path, since there are many completely dark points under the green fill, as well as points on different paths than those of interest. Experiment with clicking on different points closer to the path in order to adjust the threshold until you are happy with it. You might end up with something like the rightmost image:

<div align="center">

-   <img src="/media/plugins/snt/snt-zoomed-filling-2.png" title="fig:Fill, opaque" width="250" alt="Fill, opaque" />
-   <img src="/media/plugins/snt/snt-transparent-filling-2.png" title="fig:Fill, with &quot;Transparent overlay&quot; on" width="250" alt="Fill, with &quot;Transparent overlay&quot; on" />
-   <img src="/media/plugins/snt/snt-refined-filling-2.png" title="fig:Fill, refined" width="250" alt="Fill, refined" />

</div>

{% include clear%}


### III.Completing the Fill

If you are happy with this, then you might as well click "Pause" so that your computer isn't spending all its CPU on continuing to explore the image. Then you can either:

-   Save the fill (which will add it to the fill list) by clicking "Stash Progress".
-   Discard the fill by either clicking "Stop" while filling is in progress or, if you stashed the fill, select it in the fill list and click "Delete Fill(s)".
-   Use the "Image Stack..." button to view the same image stack, but with only the points in that fill preserved. You can choose either a grayscale image or a binary mask. One reason why you might want to do this is that you can then smooth that image and use the [3D Viewer](/plugins/3d-viewer) to do a surface rendering of the neuron. Perhaps then you could overlay that onto a volume rendering of the complete image (see available [tutorials](/plugins/snt#tutorials)). Or, you could save those fill stacks for each of the neurons you fill and then combine them in ImageJ using "RGB Merge".

The image stack you would get from the image used in this example might look something like this: <img src="/media/plugins/snt/snt-filling-viewed-2.png" title="fig:Having selected the &quot;Image Stack... -&gt; As Grayscale Image...&quot; option" width="500" alt="Having selected the &quot;Image Stack... -&gt; As Grayscale Image...&quot; option" />

# Generating *Filtered Images*

This section describes how to generate [Filtered Images](/plugins/snt/manual#tracing-on-filtered-image) outside SNT. Note that the filtering used in this walk-through (*[Frangi](/plugins/frangi) Vesselness*) is already supported directly by SNT. This tutorial will assume you need to perform the filtering with adjusted parameters.

#### A Single Image

To process a single image with the Frangi Vesselness filter, pause SNT, and select {% include bc path='Process | Filters | Frangi Vesselness'%}. By way of example, let's say you need to enhance strucutres at two scales: twice the x voxel separation and five times that value. We apply a Gaussian convolution at each scale. Assuming your image has isotropic resolution with pixel width = pixel height = voxel depth = 1, the parameters would be: ![](/media/plugins/snt/frangi-parameters.png)
{% capture tip%}
To get the spatial calibration for your image, go to {% include bc path='Image|Properties...'%} ({% include key keys='Ctrl|Shift|P' %}) in the main Fiji dialog.
{% endcapture %}
{% include notice icon="tip" content=tip %} Save the result using {% include bc path='File | Save As|Tiff...'%} ("test-filtered.tif", for example). Then, in SNT's dialog look for the "Tracing on Secondary Image" widget in the *Main* tab. Click the file folder button to specify the secondary image. Next, toggle the "Trace on Secondary Image" checkbox (you can do so using {% include key key='I' %}. Now the pathfinding will occur on the secondary image. To view a MIP of the secondary image "over" the original image during tracing, toggle the "Render in overlay at X% opacity" checkbox.

<div align="center">

-   <img src="/media/plugins/snt/filtered-image-load.png" title="fig:Step 1" width="300" alt="Step 1" />
-   <img src="/media/plugins/snt/filtered-image-toggle.png" title="fig:Step 2" width="300" alt="Step 2" />

</div>

To display the image in a separate window, from the SNT dialog use {% include bc path='Show Cached Image'%} from the *gear* menu or {% include bc path='View | Show Cached *Secondary Image*'%}. <img src="/media/plugins/snt/display-filtered-image.png" title="fig:Secondary Image MIP" width="400" alt="Secondary Image MIP" />

#### Multiple Images

The easiest way to preprocess multiple images is to record a macro for processing a single image, then wrap it in a loop to iterate over all files in a directory. For example, using IJ1 macro language:

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
            run("Frangi Vesselness"); // arguments can be specified here
            selectWindow(expected_window_name);
            saveAs("Tiff", output_filename);
        }
    }

The same process can be accomplished more completely in a script using [ImageJ Ops](/libs/imagej-ops). For example, in Jython:

    # @ImageJ ij
    # @String(value="<HTML>This script applies the Frangi Vesselness filter to all TIFF images in a directory.<br>Only 2D or 3D grayscale images are supported. Processing log is shown in Console.", visibility="MESSAGE") msg
    # @File(label="Directory containing your images", style="directory") input_dir
    # @String(label="Consider only filenames containing",description="Clear field for no filtering",value="") name_filter
    # @boolean(label="Include subdirectories") recursive
    # @float(label="Size of structures to be filtered (spatially calibrated units)",description="The filter kernel will be determined from the average voxel size") scale
    # @LogService log
    # @StatusService status
    # @UIService uiservice

    **
    file: Filter_Multiple_Images.py
    author: Tiago Ferreira, Cameron Arshadi
    info: Bulk filtering of image files using Frangi Vesselness
    **

    from net.imagej.axis import Axes

    import os


    def get_image_files(directory, filtering_string, extension):
        **Returns a list containing the paths of files in the specified
           directory. The list will only include files with the supplied
           extension whose filename contains the specified string.**
        files = []
        for (dirpath, dirnames, filenames) in os.walk(directory):
            for f in filenames:
                if os.path.basename(f).startswith('.'):
                    continue
                if filtering_string in f and f.lower().endswith(extension):
                    files.append(os.path.join(dirpath, f))
            if not recursive:
                break  # do not process subdirectories

        return files


    def run():
        # First check that scale parameter is > 0, exiting if not
        if scale <= 0:
            log.error('Please select a value > 0 for the scale parameter. Exiting...')
            return

        # Get all files with specified name filter and extension in the input directory
        d = str(input_dir)
        extension = ".tif"
        files = get_image_files(d, name_filter, extension)
        if not files or len(files) == 0:
            uiservice.showDialog("No files matched the specified criteria", "Error")
            return

        processed = 0
        skipped = 0
        for f in files:

            basename = os.path.basename(f)
            msg = 'Processing file %s: %s...' % (processed + skipped + 1, basename)
            status.showStatus(msg)
            log.info(msg)

            # Load the input image
            input_image = ij.io().open(f)

            # Verify that the image is 2D/3D and grayscale, skipping it if not
            num_dimensions = input_image.numDimensions()
            if num_dimensions > 3 or int(input_image.getChannels()) > 1:
                log.error('Could not process %s...Only 2D/3D grayscale images are supported' % basename)
                skipped += 1
                continue

            # Convert input image to float, since we are dealing with derivatives
            float_input = ij.op().run("convert.float32", input_image)

            # Obtain spatial calibration of the image
            x_spacing = float_input.averageScale(0)
            y_spacing = float_input.averageScale(1)
            spacing = [x_spacing, y_spacing]

            if num_dimensions == 3 and float_input.axis(2).type() == Axes.Z:
                z_spacing = float_input.averageScale(2)
                spacing.append(z_spacing)

            # Create placeholder image for the output then run the Frangi Vesselness op
            output = ij.op().run("create.img", float_input)
            pixel_scale = scale / (sum(spacing) / len(spacing))  # average voxel size: convert scale to pixel units
            ij.op().run("frangiVesselness", output, float_input, spacing, pixel_scale)

            # Save the result using the same basename as the image, adding "[Frangi].tif"
            # For example, the output for "OP_1.tif" would be named "OP_1[Frangi].tif"
            l = len(f)
            el = len(extension)
            output_filepath = f[0:l - el] + "[Frangi].tif"
            ij.io().save(output, output_filepath)

            processed += 1

        log.info('Done. %s file(s) processed. %s file(s) skipped...' % (processed, skipped))


    run()

# Accurate Point Placement

This section describes methods to increase the accuracy of node placement.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td>
        <p>Accurate node placement requires <em>XY</em>, <em>ZY</em> and <em>XZ</em> views to be visible. You can do so at <a href="/plugins/snt/manual#startup-prompt">startup</a>, by making sure that <em>Default: XY, ZY and XZ views</em> is selected, or by clicking in <em>Display ZY/XZ Views</em> in the <a href="/plugins/snt/manual#options-tab">Options tab</a> if you have already started SNT.</p>
      </td>
      <td>
        <figure>
          <img src="/media/plugins/snt/snt-three-pane-view-enabled-startup-prompt.png" title="SNT-Three-Pane-View-Enabled-Startup-Prompt.png" alt="SNT-Three-Pane-View-Enabled-Startup-Prompt.png">
          <figcaption aria-hidden="true">
            SNT-Three-Pane-View-Enabled-Startup-Prompt.png
          </figcaption>
        </figure>
      </td>
    </tr>
    <tr>
      <td>
        <p>Find the approximate location of your start point by moving your mouse in the XY window, holding down {% include key key='Shift' %} to synchronize the view in the other panes. At this point, you should enable cursor <a href="/plugins/snt/manual#cursor-auto-snapping">auto-snapping</a> in the <a href="/plugins/snt/manual#main-tab">Main tab</a> using suitable parameters for your image.</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-1.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>When you press {% include key key='+' %} to zoom in, all the panes will zoom in on the point that the crosshair is over, so each time you press {% include key key='+' %}, make sure you move your mouse pointer so that it's still over the structure of interest. You may want to adjust in the <a href="/plugins/snt/manual#views">Views</a> widget (<a href="/plugins/snt/manual#options-tab">Options tab</a>) whether all views should zoom synchronously.<br>
        At this point, you should adjust a suitable <a href="/plugins/snt/manual#cursor-auto-snapping">snapping neighborhood</a> both in 2D (XY) and 3D (Z). Note that when Z-snapping is enabled, all views become synchronized,</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-2.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Locate the center of the structure to be clicked on. If <a href="/plugins/snt/manual#cursor-auto-snapping">cursor auto-snapping</a> is enabled, simply mouse over the structure, otherwise, try moving the mouse and scroll wheel in each of the panes (holding down {% include key key='Shift' %} so synchronize the views in all three panes). Note that you can toggle the cursor auto-snapping feature at will, by pressing the <a href="/plugins/snt/key-shortcuts">shortcut</a> {% include key key='S' %}. Also, note that you can "click" on the <a href="/plugins/snt/key-shortcuts#tracing">brightest voxel</a> of a voxel column, by pressing {% include key key='M' %}.</p>
        <p>When you're happy with the point under the crosshairs, left-click to start the path:</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-3.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>Zoom out again with the {% include key key='-' %} key, and similarly zoom in on the next point you want to be on your path to place it precisely:</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-4.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>The path along the neuron may not follow the center line perfectly:</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-5.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>... but you can later improve that with the {% include bc path='Refine/Fit|Fit Path...'%} option in the <a href="/plugins/snt/manual#path-manager">Path Manager</a>, which tries to align the path to the midline of the structure to sub-voxel accuracy:</p>
      </td>
      <td>
        <p><img src="/media/plugins/snt/snt-accurate-point-placement-walkthrough-updated-6.png" width="350"></p>
      </td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}
