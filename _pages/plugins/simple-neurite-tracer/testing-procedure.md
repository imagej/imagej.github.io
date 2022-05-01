---
mediawiki: Testing_Procedure_for_Simple_Neurite_Tracer
title: Simple Neurite Tracer › Testing Procedure
nav-links: true
nav-title: Testing Procedure
---

{% include warning/deprecated new="[SNT](/plugins/snt)"
  old="[Simple Neurite Tracer](/plugins/simple-neurite-tracer)" %}

This is a set of instructions to follow to test as much of the code as possible in [Simple Neurite Tracer](/plugins/snt). It does not give complete coverage, but following this before each new release should stop the more obvious problems from getting through. The coverage results for this procedure with VIB at 6840872c6a492e31caa453a6776d1e9fac26f58d are [here](https://fiji.sc/~longair/coverage-VIB-6840872c6a492e31caa453a6776d1e9fac26f58d/_files/2b.html).

## Basic Tracing

-   Open example-for-tracing.tif
-   Run "Simple Neurite Tracer", selecting "Create new 3D Viewer" and "Use three pane view"
-   Rotate the 3D view
-   Use the slice selector to run through the slices in each pane
-   Hold down Shift while moving the red crosshair around in each pane in turn
-   Click to start a path
-   Cancel Path
-   Click to start a path
-   Select a further point along the path
-   Check with "Shift" that the cyan search progress appears in each pane
-   Check that blue path is create in each pane, and in the 3D viewer
-   Click "No" to answer the question "Keep new path segment"
-   Try again to select a further point along the path
-   Click "Abandon Search" half way through the search for the path.
-   Try again to select a further point along the path, but allow it to continue to completion
-   Click "Yes" to confirm the temporary path
-   Check that the red path appears in all panes and the 3D viewer
-   Pick a further point and confirm that next segment.
-   Click on "Complete Path"
-   Check that the magenta path appears in all of the viewers
-   Select the path in the Path Window
-   Hold down Control and click a point on the existing path where you want a branch point to start
-   Add a few more segments to the the new path, complete it normally
-   Start a new path at a random point in the stack, and end it on an existing path by holding down Control when you select the final point
-   Create a new path that both starts and ends on an exisiting path
-   Check that these paths appear sensibly in the Path window
-   Try selecting and deselecting the paths in the Path window, check that the right paths are highlighted in each pane and in the 3D viewer
-   Turn on the "Only Show Selected Paths" option and do the same, checking that only the selected paths appear
-   Turn off the "Only Show Selected Paths"
-   Select "2D: parts in nearby slices"
-   Look through all the slices to check that they're displayed properly
-   Try changing the "slices on either side" parameter and doing the same
-   Turn on "Hessian based analysis"
-   Add an extra path
-   Turn off "Hessian based analysis"
-   Click on "Pick Sigma Visually"
-   Click on an interesting point in the image
-   In the Sigma Palette, try adjusting the maximum, adjusting the slice and click on one of the boxes with a different sigma
-   Close the palette and wait for the Gaussian to finish calculating
-   Try adding a path
-   Turn off "Hessian based analysis"
-   Click "Pick Sigma Visually", click in the image, but close the window while the palette is generating to check that this cancels the generation properly
-   Click "Pick Sigma Manually" and try setting some values - check that the Gaussian is recalculated and you can trace a new path
-   Click on the green rectangle and then change the colour. Check that the colour changes in the panes and in the 3D Viewer
-   Click on the magenta rectangle and then change the colour. Check that the colour changes in the panes and in the 3D Viewer.
-   Use "Show / Hide Fill List" and "Show / Hide Path List" to display and hide the two windows
-   Select a single path in the Path Window, hold down Shift and click "Fit Volume"
-   "Fly Through" the normal path which is fitted
-   Select all paths in the Path Window and click "Fit Volume"
-   Check that they are all fitted in the 3D Viewer (note bug here: selection is not preserved afterwards)
-   Try selectively unfitting two of the paths
-   Refit one of them.
-   Select a (not top level path) and click "Make Primary"
-   Check that the path list is rearranged
-   Click on a path and rename it (not bug here: only the non-fitted path's name is changed)
-   Delete the path with start and end joins
-   Don't quit the tracer but move onto the next set of tests...
-   Select a single path and click "Fill Out" (note bug here: panes stop updating due to NPE)

```
Exception in thread "AWT-EventQueue-0" Exception in thread "AWT-EventQueue-0" java.lang.NullPointerException
   at tracing.SearchThread.anyNodeUnderThreshold(SearchThread.java:682)
   at tracing.SearchThread.drawProgressOnSlice(SearchThread.java:729)
   at tracing.FillerThread.drawProgressOnSlice(FillerThread.java:365)
   at tracing.TracerCanvas.drawOverlay(TracerCanvas.java:87)
```

-   (FIXME: add further filling test script here.)
-   Click "Cancel Fill"
-   Move on to the next section

## Saving and Loading

-   Click "Export as CSV"
-   Check that the CSV file has been created properly
-   Repeat, checking there's a warning about overwriting and overwriting
-   Repeat, checking there's a warning about overwriting and not overwriting
-   Click "Save Traces File", save to foo.nonstandard
-   Quit the tracer (there should be no "unsaved paths" warning...)
-   Close the 3D Viewer
-   Start "Simple Neurite Tracer" and select "Create new 3D Viewer" and "Three Pane View"
-   Click "Load Traces" and select foo.nonstandard
-   Look through the stack and check that all are reloaded, the renamed path is still renamed, etc.
-   Add a new path
-   Click "Quit Tracer", check that you're warned about unsaved paths - cancel, check that it doesn't quit
-   Click "Quit Tracer", check that you're warned about unsaved paths - go ahead and quit
-   Rename "foo.nonstandard" to "foo.traces"
-   Start "Simple Neurite Tracer" and select "Create new 3D Viewer" and "Three Pane View"
-   Click "Load Traces" and check that it offers to load the renamed traces file.
-   Click "No", and select it manually.
-   Quit the tracer and try again, this time loading the default when it offers.

## Test Different 3D Views

-   Load up the traces file, make sure that some paths are fitted, some not
-   Try each of the View Paths (3D) options, check they all work
-   Change back to surface reconstructions

## Reuse an existing 3D viewer

-   Select "Show only selected paths", pick two fitted paths
-   Change the fitted path colour to something different from the default (e.g. yellow)
-   Quit the tracer, don't save
-   Select the "image for tracing" in the 3D Viewer, remove it
-   With the original ImagePlus as the current image, start the 3D viewer, but select "Reuse 3D Viewer", and pick the existing 3D Viewer
-   Add a new path, check that the existing yellow reconstructions are still there
-   Quit the tracer and close the 3D Viewer

## Load Labels

-   Load up an image which has a corresponding labels file
-   Click "load labels", select the right labels file
-   Hover the mouse over different regions and check that the ImageJ status updates to tell you the region's name
-   Quit the tracer

## Show Correspondences To Traces

-   Load a file for which you have a traces file
-   Start the tracer
-   Draw a few paths
-   Click "Show Corresponding Traces" and select the existing traces file
-   Change 3D view to "lines" and check that the correspondences are shown correctly
-   Quit the tracer

## SWC Import

-   Load an image file for which you have a corresponding SWC file
