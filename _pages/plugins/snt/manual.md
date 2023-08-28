---
title: SNT › Manual
nav-links: true
nav-title: Manual
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
---

{% capture version%}
**These instructions were last revised for version 4.3.0**.<br>
Please help us to keep this manual up-to-date by [editing](https://github.com/imagej/imagej.github.io/edit/main/_pages/plugins/snt/manual.md) this page directly to fill in any documentation gap. Do [reach out](https://forum.image.sc/tag/snt) if you need assistance!
{% endcapture %}
{% include notice content=version %}

# SNT Commands

SNT registers commands in Fiji's menu structure in the {% include bc path='Plugins|Neuroanatomy|' %} sub-menu, namely:

**Neuroanatomy Shortcuts Window** A toolbar panel listing _all_ SNT commands, actions, and scripts including entry points to Sholl and Strahler analyses. It can be open via {% include bc path='Plugins|Neuroanatomy|' %}, or more easily, by pressing *SNT* in the ImageJ toolbar:
<div align="center">
    <img align="center" width="40%" src="/media/plugins/snt/snt-shortcuts-window.png" title="The Neuroanatomy Shortcuts panel can be toggled using the SNT icon in the ImageJ toolbar" />
</div>

**[SNT](#startup-prompt)...** The main interface, from which tracing and path editing operations are done

**[Rec. Viewer](/plugins/snt/reconstruction-viewer)** A fast, streamlined 3D viewer for analysis and quantification of existing neuroanatomical data

**[Reconstruction Plotter](#reconstruction-plotter)** A utility for rendering 2D illustrations of reconstructions (including vector formats) without having to load other interfaces


# Startup Prompt

<img align="right" width="300" src="/media/plugins/snt/snt-startup-prompt.png" title="Shortcuts Window (v4.0)" />
SNT is initialized by running {% include bc path='Plugins|NeuroAnatomy|SNT...' %}. All the options in the startup prompt can be set once SNT is opened, but the startup prompt provides the convenience of setting the most important parameters at once.

- **Image**/**Image file** The image to be traced/analyzed. The drop-down menu will list all images currently open in ImageJ. Alternatively, an image path may be specified by clicking *Browse* and choosing an image file. If no image is chosen, SNT will create an empty display canvas from the computed bounding box of the reconstruction file (if provided).

- **Reconstruction file** The path of the reconstruction file to be imported. SNT will automatically try to fill this field by looking at all the reconstruction files (.traces, .(e)swc, .ndf, or .json) in the image directory and retrieving the filename closer to _Image file_.

- **User interface** Specifies which views to display for 3D images. The default setting provides the XY, ZY, and XZ views and allows for more [accurate node placement](/plugins/snt/step-by-step-instructions#accurate-point-placement) but requires more RAM.

- **Tracing Channel** Specifies the image channel to trace on (this option is ignored with single-channel images).


# Main Dialog

{% include img align="center" src="/media/plugins/snt/snt-main-gui.png" caption="Overview of main dialog (left). Note that clicking on the  headings separating the different widgets will point your browser to the relevant section of this manual!" %}

## Menu Commands

### File ›

Lists commands for I/O operations. Most are self-explanatory. Noteworthy:

#### Choose Tracing Image...
Specifies the image to trace on without having to restart SNT. To trace on an image currently open in ImageJ, use *From Open Image...*. A prompt with currently open images will appear, allowing selection of one. To browse for an image file, use *From File...*. You should toggle the *validate spatial calibration* checkbox to ensure the image to be imported is compatible with the existing one.

#### Autotrace Segmented Image...
If you have a binary mask of the image you want to trace saved to disk (i.e., a pre-processed version of the image in which background pixels have been zeroed), you can use this command to attempt automatic reconstruction. This is similar to {% include bc path='Utilities | Extract Paths from Segmented Image... ' %} but uses file paths as input. See [Full-automated tracing walkthrough](/plugins/snt/step-by-step-instructions#full-automated-tracing) for details.

#### Load Tracings ›
Imports of neuronal reconstructions from multiple sources, including:

- **{% include bc path='Local Files' %}** [TRACES](/plugins/snt/faq#in-which-format-should-i-save-my-tracings-traces-or-swc), [SWC](/plugins/snt/faq#what-is-a-swc-file) (single files or bulk import of a directory of files), NDF ([NeuronJ](/plugins/neuronj) data format), or JSON.

- **{% include bc path='Remote Databases' %}** Import of neuronal reconstructions from [FlyCircuit](http://www.flycircuit.tw/), [InsectBrain](https://insectbraindb.org/app/), [MouseLight](https://ml-neuronbrowser.janelia.org/), and [NeuroMorpho](http://neuromorpho.org/).

{% capture dnd %}
All SNT dialogs (including the _Neuroanatomy Shortcut Window_ support drag-and-drop: E.g., you can import SWC files just by dragging and dropping them either into the main SNT dialog or the Path Manager.
{% endcapture %}
{% include notice icon="info" content=dnd %}

#### Load Labels (AmiraMesh)...
{% include img src="/media/plugins/snt/load-demo-dialog.png" align="right" width="300px" %}
This option assumes you are tracing on the same spatial coordinates of an annotated neuropil for which compartments have been segmented (*labeled*) and stored in an [Amira](https://amira.zib.de/) labels file. Once loaded, SNT will report the name of the compartments in the ImageJ status bar when hovering over the image.

#### Load Demo Dataset...
Loads a demo dataset (a tracing image, a reconstruction, or both). Use this to familiarize yourself with the software, and to create [Minimal reproducible example](https://en.wikipedia.org/wiki/Minimal_reproducible_example) when reporting problems. The bottom part of the dialog describes each dataset including source, citation, and DOI (when available). Note that while some of the data is bundled with SNT, the majority of the datasets requires an internet connection.

#### Save Tracings ›
Options to save/export all of traced paths in the SWC and TRACES formats. Note that it is also possible to export subsets of paths using the [Path Manager](#path-manager).
This menu also includes controls to create _SNAPSHOT BACKUPS_. To use this feature:

1. Trace one more paths
2. Save them to a local file using {% include key key='ctlcmd|S' %} ({% include bc path='File|Save Tracings|Save' %})
3. Keep tracing paths. When pertinent, press {% include key key='ctlcmd|Shift|S' %} ({% include bc path='Save Tracings|Save Snapshot Backup' %}) to save current progress to a timestamped backup file
{% include img src="/media/plugins/snt/snt-recover-from-snapshot.png" align="right" width="300px" %}
4. Reinstate progress from backed up data using {% include bc path='File|Restore Snapshot Backup' %}, which allows you to go 'back in time':


#### Save Tables &amp; Analysis Plots...
Allows saving of any measurements and plots generated by analysis commands. Tables are saved in the {% include wikipedia title="Comma-separated values" %} file format.

#### Reveal Directory
Convenience shortcuts to reveal common directories (scripts, backups, folder of image being traced, etc.) in the native file explorer.

#### Reset SNT and Restart...
Resets all preferences and restarts SNT using default options.


### Analysis ›

#### Convex Hull
See [Analysis › Convex hull Analysis](/plugins/snt/analysis#convex-hull-analysis).

#### Path Order Analysis
See [Analysis › Path Order Analysis](/plugins/snt/analysis#path-order-analysis).

#### Path Properties: Export CSV...
Allows export of information regarding individual Paths (morphometrics, neurite compartments, linkage relationships to other Paths, start and end coordinates, etc.).

#### Brain Area Analysis
Summarizes projection patterns across brain areas. See [Analysis › Graph-based Analysis](/plugins/snt/analysis#graph-based-analysis) for details.

#### Sholl Analysis.../Sholl Analysis (by Focal Point)...
See [Analysis › Sholl Analysis](/plugins/snt/analysis#sholl-analysis).

#### Strahler Analysis...
See [Analysis › Strahler Analysis](/plugins/snt/analysis#strahler-analysis).

#### Measure...
Provides a comprehensive selection of measurements to apply to one connected component (i.e., rooted tree structure) from the Path Manager. See [Analysis › measurements](/plugins/snt/analysis#measurements) for details.

#### Quick Measurements
Shortcut for running {% include bc path='Measure...' %} with common metrics.


### Utilities ›

#### Command Palette
{% include img src="/media/plugins/snt/command-palette.png" align="right" width="450px" %}
The Command Palette is the fastest way to access actions and discover their respective shortcuts:
1. Press {% include key keys='ctlcmd|Shift|P' %} in either SNT or [Reconstruction Viewer](/plugins/snt/reconstruction-viewer)
2. Start typing to filter actions, scripts and available commands
3. Press {% include key keys='up' %} or {% include key keys='down' %} to select a command (or use the  {% include key keys='mouse wheel' %})
4. Press {% include key keys='Enter' %} to run it. If the record button is toggled, executed commands are recorded by the [Script Recorder](/plugins/snt/scripting#script-recorder).

<span id="plotter"></span>
#### Reconstruction Plotter
_Reconstruction Plotter_ is a whole-purpose 2D viewer for neuronal reconstructions by plotting 2D projections of traced paths. A control panel  allows for adjustment of the spatial orientation of the tracing. By default, the plot is monochrome. If paths are assigned color tags, or the structure has been color-coded  use {% include bc path='Actions|Render final (colorized) plot' %} from the control panel to render a (static) plot with color-mapped paths, with the final orientation matching that of the dynamic plot. Features include:

- Dark/light theme (controls in plotter's contextual menu)
- Export as SVG
- Color legends when color mappings are present
- Can be combined in multi-panel viewers (mainly via scripting)

<div align="center">
  <img src="/media/plugins/snt/snt-reconstruction-plotter-example.png" title="SNT-Reconstruction-Plotter-Example.png" width="250" alt="SNT-Reconstruction-Plotter-Example.png" />
  <img src="/media/plugins/snt/snt-reconstruction-plotter-controls.png" title="SNT-Reconstruction-Plotter-Controls.png" width="250" alt="SNT-Reconstruction-Plotter-Controls.png" />
  <img src="/media/plugins/snt/snt-reconstruction-plotter-colored.png" title="SNT-Reconstruction-Plotter-Colored.png" width="250" alt="SNT-Reconstruction-Plotter-Colored.png" />
</div>

#### Compare Reconstructions/Cell Groups...
Allows morphometric comparisons of two single reconstruction files or multiple groups of reconstruction files (including statistical reports and two-sample t-test/one-way ANOVA analysis). Color-coded montages of analyzed groups can also be generated. See [Comparing Reconstructions](/plugins/snt/analysis#comparing-reconstructions) for details.

#### Create Dendrogram
Generates a Dendrogram plot of a connected component (i.e, one rooted tree structure in the Path Manager). See [Analysis › Graph-based Analysis](/plugins/snt/analysis#graph-based-analysis) for details.

#### Create Annotation Graph...
See [Analysis › Graph-based Analysis](/plugins/snt/analysis#graph-based-analysis) for details.

#### Extract Paths from Segmented Image...
Similar to {% include bc path='File|Autotrace Segmented Image...| ' %} but using image(s) already open  as input. See [Full-automated tracing walkthrough](/plugins/snt/step-by-step-instructions#full-automated-tracing) for details.

#### Batch Scripts
A collection of batch processing scripts related to image processing, reconstruction analysis and data curation. See [SNT Scripts: Batch](/plugins/snt/scripting#batch) for details.

### Scripts›
See [SNT: Scripting](/plugins/snt/scripting).


### View›
Contains commands for organizing tracing views on screen, plus commands for displaying cached data used for computation of paths, including:

- **{% include bc path='Arrange Tracing Views' %}** Resets the view pane on-screen positions to their default.

- **{% include bc path='Hide Tracing Canvas| ' %}** Allows toggling of the visibility of the three orthogonal view tracing panes as well as the Legacy 3D View window.

- **{% include bc path='Display Secondary Image' %}** Displays the cached filtered image being used as secondary tracing layer.

- **{% include bc path='Toggle Fiji Console' %}** Toggles the visibility of Fiji's Console. The console displays errors and exceptions as well as informational messages when _Debug mode_ is activated.


## Main Tab

This *home* tab aggregated widgets for tracing and frequent operations.

### Data Source
<img align="right" src="/media/plugins/snt/snt-data-source-widget.png" width="300" />
If tracing on a multidimensional image (i.e., one with multiple data channels and/or a time axis), a particular channel/frame can be loaded into the views by selecting each and pressing the "Reload" button.

### Cursor Auto-snapping

**Enable Snapping checkbox** If active (the default) the cursor snaps to the brightest voxel in its vicinity (Toggling shortcut: {% include key key='S' %}). To accomplish this, SNT takes the cuboid of the specified dimensions (in pixels) centered on the current cursor position and searches quickly for local maxima in that neighborhood, moving the cursor to that position. The Z-plane in which the maximum was found is automatically selected if the "Z" parameter is greater than 0. Noteworthy:

<img align="right" width="300" src="/media/plugins/snt/cursor-snap.png" title="Cursor auto-snapping in 2D or 3D" />

 - This feature assumes the signal is brighter than the background as typically found in fluorescent images.

 - If multiple maxima exist (e.g., when the signal is saturated), it snaps to their centroid.

 - To streamline the computation: XYZ dimensions are constrained to even numbers and limited range.

 - Snapping occurs in 2D (i.e., in the active plane) if Z=0.

 - The XZ, ZY views are synchronized when 3D snapping is active (i.e., Z&gt;0).

 - This functionality was inspired by <a href="/plugins/neuronj">NeuronJ</a>, that described it like this in its manual:

   > To facilitate accurate positioning of starting points, so that they are really on a neurite rather than close to one, the program carries out a local snapping operation. This means that when moving the mouse within the image, the program quickly searches in a small window around the current mouse position for the pixel that is most likely to be on a neurite.

### Auto-tracing

<img align="right" width="450" src="/media/plugins/snt/snt-auto-tracing.png" title="Auto-tracing options" />
- **Enable A\* search algorithm** By default, SNT uses the {% include wikipedia title="A* search algorithm" text="A* search algorithm" %} to automatically trace paths between two manually selected points. To manually place nodes along a path, toggle this feature off. Note that it is also possible to enable other built-in algorithms or algorithms provided by external SNT add-ons. Current options include:

  - **A\* search**: Canonical and proven implementation of the historic algorithm, ported from [Simple Neurite Tracer](/plugins/snt/faq#what-is-the-difference-between-snt-and-simple-neurite-tracer)

  - **NBA\* search (New Bidirectional A\*)**: [Newer implementation](https://repub.eur.nl/pub/16100/ei2009-10.pdf) of A* expected to be faster than original but not as thoroughly tested

  - **Fast marching**: Provided by [Tubular Geodesics](/plugins/snt/tubular-geodesics), an external SNT add-on 

    Independently of the algorithm used, the gear menu in this pane provides options to tweak the performance, accuracy and footprint of the computations involved in the search. These include:

     - **Data structure** Defines how data is stored internally: Either _Map_ (slightly slower, but lower footprint), or _Array_ (slightly faster, but higher footprint)

     - **Cost Function** Auto-tracing algorithms aim to find a path to the destination node under the smallest _cost_ of deviating from the signal along a neurite. A successful search between two points is thus the _cheapest_ path with the least deviations. This is implemented through a _cost function_ in which voxels along a neurite are assigned lower costs, while voxels outside the neurite are assigned higher costs or penalties. SNT implements several _cost functions_, namely:

         - **Reciprocal of Intensity** The default, robust under a wide range of conditions

         - **Difference of Intensity** Fast on images with right-shifted histograms (mean >> 0)

         - **Difference of Intensity Squared** (Usually) Faster flavor of _Difference of Intensity_

         - **Probability of Intensity** Fast, specially on noisy images. To be used with 'Real-time statistics' (see below)

     - **Image Statistics** Successful cost functions rely on _a priori_ understanding of the image (simpler cost functions may only require access to the image minimum (dimmest intensity) and maximum (brightest intensity), but many others may need access to the image's mean, standard deviation, etc.). Options include:

          - **Compute Real-Time** The default. Image statistics are computed during _each_ auto-tracing operation, along a bounding-box defined by the start and end points of the search

          - **Specify Manually** Advanced option for users with if a quantitative understanding of the image. Searches may consider pixels outside neurites when maximum in over-estimated, and may take significantly longer when it is under-estimated, since each pixel will carry a greater-than-reasonable cost

          - **Compute Once** Statistics are computed once for the whole image (may take a while for large images) and stored in memory. If enough RAM is available this _may_ speed up searches. Although in real-word usage any speed-gains relatively to _Compute Real-Time_ seem negligible on modern hardware

### Tracing on Secondary Image (Layer)
<span id="tracing-on-secondary-image"></span>
<img align="right" width="450" src="/media/plugins/snt/snt-secondary-layer-menu.png" title="Secondary layer controls" />
This is one of SNT's most advanced and useful features. The [default auto-tracing](#Auto-tracing) provides a convenient and easy way to detect structures by their likelihood of *belonging* to a tube-like structure (such as a neurite). However, it is just _one_ approach for "tube-like" classification. What if your data requires different filtering?, or you want to experiment with other approaches?, or the perfect pre-processing algorithm for your images is not yet available in SNT? *Tracing on Secondary Layer* is the answer to these questions: It allows you to feed SNT with pre-processed data on which the A\* star search will operate. Because this option can be toggled at will, it becomes a secondary _layer_ for auto-tracing: E.g., you may decide to auto-trace certain neurites on the original image, while tracing other neurites on the secondary layer.

For the most part the secondary layer remains hidden because feedback on auto-tracing searches is always provided in the original image. When RAM is not limited, one can ping-pong between _secondary_ and _original_ image simply, by pressing {% include key key='L' %}, the shortcut for the _Trace/Fill on Secondary **L**ayer_ checkbox. Here are some specific usages for this feature:

- **Frangi *Vesselness* filtering** For certain datasets [Frangi](/plugins/frangi) filtering  is quite effective at enhancing tubular structures. However, it is more computation intensive, and thus, less suitable to be adopted by "compute-as-needed" approaches. Thus, Frangi-filtering can be computed once for the whole image, and the result loaded as secondary layer

- **Image Processing at multiple scales** Consider a structure formed simultaneously by very thick and very thin processes (e.g. axons and dendrites). To trace structures of variable diameters more effectively, one could pre-filter a copy of the current image at multiple scales, and load the result as _secondary layer_

- **Probability maps (p-maps)** Probability maps of classified images (generated using e.g., [machine learning](/plugins/tws/)) may not be 100% accurate. We find that, in many cases it is more effective to use p-maps as secondary layers, rather than attempting fully automated p-map reconstructions that typically require time-consuming _post-hoc_ corrections


#### Creating Secondary layers
<img align="right" width="450" src="/media/plugins/snt/snt-secondary-layer-wizard-prompt.png" title="Secondary layer wizard" />

Secondary layers are created/load using the second *gear* drop-down menu in the auto-tracing panel. The most common way to create a new layer is by calling the _Secondary Layer Creation Wizard_:

The wizard needs two types of information from the user: The type of filtering operation and the size(s) (scale(s)) of the structures being traced, which control the spatial scale of the filter (known as σ).

- **Filter** The filtering operation, including  *Frangi*, *Tubeness*, *Gaussian blur* and *Median*. Note rh.

  - **Tubeness** This corresponds to the _Hessian-based analysis_ of older SNT versions. This filter enhances tube-like structures in the image, using an improved [Tubeness](/plugins/tubeness) approach, modified to support multiple scale(s)

  - **Frangi vesselness** A proven and consistent strategy for filtering tube-like structures. Described in [Frangi](/plugins/frangi)

  - **Median** Filter for noise removal able to preserve neurite edges. Note that _Median_ accepts only one σ value, i.e., a single scale.

  - **Gaussian blur** Filter for noise removal, capable of gentle smoothing with some ability to preserve neurite edges, specially under small σ values.


- **Scale(s)** Also known as _sigmas_ (σ). These should reflect average radii of the structures being traced. If smaller values are specified, the filter becomes more sensitive to noise. Larger values on the other hand, make the filtering operation less sensitive to local shape characteristics. There are two ways to select this values:

    - **Select visually...**: The wizard will prompt you to click on a representative region of the image which has a meaningful structure. Once you click there, a preview palette is generated showing increasing values of σ (from top-left to bottom-right) applied to that region of the image. Select the suitable scales

    - **Estimate programmatically...**: This allows automated estimation of radii across the image, which can inform the choice of scale(s). The only parameter required is *Dimmest intensity (approx.)*: Pixel values below this value are treated as background when computing thicknesses. Use -1 to adopt the default cutoff value (half of the image max). After pressing *OK*, a color-mapped image (based off local radius) and a histogram showing the distribution of radii across the image are shown. The histogram can be used to validate values chosen _visually_ in the preview palette.

      NB: Analysis is performed via the *Local Thickness (complete process)* plugin ({% include bc path='Analyze|Local Thickness|Local Thickness (complete process)' %} in Fiji's menu bar). 

NB: The wizard also allows you to use a backup copy of the image being traced as secondary layer. This is only useful if you intend to modify the original image during a tracing session, but want to have convenient access to the initial image at a later time.


<div align="center">
 <img  width="900" src="/media/plugins/snt/snt-secondary-layer-wizard.png" title="Secondary layer wizard previewers" />
<br>
<b>Secondary Layer Wizard</b>.<br>
<b>Left</b>:  Visual selection of filtering kernel(s) using the <i>Sigma palette</i>. The palette features its own offline manual accessible by pressing <i>H</i> or <i>F1</i>. <b>Right</b>: Programmatic estimation of radii across the whole image using <i>local thickness</i>.
</div>
#### Loading Secondary layers

The second *gear* drop-down menu in the auto-tracing panel also allows for importing secondary images processed elsewhere: Either from a file or an image already open in Fiji.  See the [Generating Filtered Images](/plugins/snt/step-by-step-instructions#generating-filtered-images) walk-through for more details.

The same menu also provides options to import a [Weka](/plugins/tws) model. In the latter, the model is applied to the image being traced, and the resulting 'p-map' is loaded as secondary layer.


### Filters for Visibility of Paths

<img align="right" src="/media/plugins/snt/path-visibility-filters.png"  width="300" />
By default, all the nodes of a path are projected onto the current Z-slice. This is useful to see how much has been completed and gives a sense of the overall structure of the reconstruction. However, SNT provides three additional visibility options for paths: 

1. **Only selected paths (hide deselected)** Only show paths that have been manually selected in the Path Manager or with the {% include key key='G' %} key ({% include key keys='Shift|G' %} to select multiple paths).

2. **Only nodes within {x} nearby Z-slices** Only highlight nodes within {x} number of Z-slices on either side of the current slice. The projected skeletons of all paths remain visible.

3. **Only paths from active channel/frame** If tracing on a multichannel image or an image with a time axis, only show paths from the active channel or frame.

Any combination of these options may be toggled simultaneously. Note that these options do not apply to [Rec. Viewer](/plugins/snt/reconstruction-viewer) and [sciview](/plugins/sciview).


### Default Path Colors

<img align="right" src="/media/plugins/snt/cmyk-color-model.png" title="CMYK color selection UI" width="300" />
By default, finished paths are colored by their selection status (only selected paths can be edited, or extended). The default colors are <font color="#00FF00">Green</font> (selected paths) and <font color="#FF00FF">Magenta</font> (deselected). Default colors can be customized by pressing the respective button in the widget . For customizing unconfirmed and temporary paths, see the *Colors* option in the [UI Interaction](#ui-interaction) widget.

**Enforce default colors (ignore color tags)** If active, SNT will force all paths to conform to the default "Selected" and "Deselected" color buttons.
Any custom color tags will be ignored until the option is toggled off. Note that this options does not apply to [Rec. Viewer](/plugins/snt/reconstruction-viewer) and [sciview](/plugins/sciview).

{% capture tip %}
The [Path Manager](#path-manager) offers several ways to colorize Paths:
1. Using {% include bc path='Tag | Color' %} swatches (custom colors can be temporarily assigned to empty swatches, by right-clicking on them)
2. Using {% include bc path='Analyze|Color Coding...' %}, providing morphometric-based [color mapping](#analyze).

<center>
  {% include img src="path-manager-color-tag" width=272 %}
  {% include img src="color-tag-result" width=158 %}
  {% include img src="color-tag-result-image" width=221 %}
</center>
{% endcapture %}
{% include notice icon="info" content=tip %}


## Options Tab

This tab aggregated widgets for advanced settings.

### Views

<img align="right" width="300" src="/media/plugins/snt/snt-options-tab.png" title="Options tab" />
- **Overlay MIP(s) at X% opacity** Overlays the {% include wikipedia title="Maximum intensity projection" %} of the image "over" the image canvas at the specified opacity. The overlaid projection is only used as a visualization aid and is ignored by the auto-tracing algorithms. It is rendered using the LUT of the channel currently being traced. To reload the overlay (e.g., in case the image being traced changes during a tracing session) toggle the checkbox twice.

<div align="center">
  <img src="/media/plugins/snt/op1-without-mip.png" title="OP1 demo dataset without MIP overlay" width="250" alt="Image without MIP overlay" />
  <img src="/media/plugins/snt/op1-with-mip.png" title="OP1 demo dataset with MIP overlay at 30%" width="250" alt="Image with MIP overlay at 30%" />
</div>

- **Draw diameters in XY view** Displays the stored diameter (if any) in the XY view for all existing nodes. Each diameter is drawn as a line segment with length = diameter, which is bisected by the orthogonal tangent vector to the path at that node.

<div align="center">
    <img src="/media/plugins/snt/draw-diameters-disabled.png" title="Draw diameters - disabled" width="200" alt="Draw diameters - disabled" />
    <img src="/media/plugins/snt/draw-diameters-enabled.png" title="Draw diameters - enabled" width="200" alt="Draw diameters - enabled" />
</div>

- **Apply zoom changes to all views** If a zoom change is applied to any one of the XY, ZY or XZ views, apply the same change to the two other views if they are open. Since in ImageJ zooming may resize the image window, you can use {% include bc path='Views|Arrange Views' %} to reset their positions

- **Resize Canvas** If using a display canvas to view reconstructions, reset its dimensions to the default. Currently, this command is only available for display canvases, to resize an image go to IJ's command {% include bc path='Image | Adjust | Canvas Size...' %}

- **Display ZY/XZ views** If currently using the XY only view, display the ZY and XZ views as well.


### Temporary Paths

- **Confirm temporary segments** If active, prompts for either confirmation or denial of whether to keep an unconfirmed path segment. If inactive, automatically confirms the path segment created on each subsequent node placement after starting a path. Applies to both auto-traced and manually traced path segments. The following two settings are only toggle-able when this setting is active.

  - **Pressing 'Y' twice finishes path** Finish a temporary path on two successive {% include key key='Y' %} key presses.
  - **Pressing 'N' twice cancels path** Discard a temporary or unconfirmed path, including the start node, on two successive {% include key key='N' %} key presses.


### UI Interaction

- **Colors** Specifies how components should be rendered, including:

  - **Canvas annotations** The label shown on the top-left corner of the views indicating the state of the UI ("Tracing Paused", "Choosing Sigma", etc.)
  - **Fills** The pixels that have been reached by the Fill search
  - **Unconfirmed** and **Temporary** paths.

- **Path nodes rendering scale** Adjusts the radius of the drawn circles representing path nodes. A path node is rendered as a circle centered at the XYZ coordinate of the point annotation. The default scale is inferred from the current zoom level.

- **Activate canvas on mouse hovering** If active, moving the mouse cursor over any of the views automatically brings the view window into focus, allowing it to receive input.


### Misc

- **Skip confirmation dialogs** If active, disables the "*Are you sure?*" prompt preceding major actions. Note that this option does not apply to irreversible actions such as deleting paths.

- **Debug mode** If active, logs detailed information about actions in the console.

- **Preferences...** Allows setting other options, namely:

  - Whether the position of dialogs should be remembered across restarts
  - Whether {% include wikipedia title="Gzip" %} compression (lossless) should be used to reduce the storage footprint of ".traces" files.
  - The max number of parallel threads to be used by SNT, as specified in ImageJ's {% include bc path='Edit|Options|Memory & Threads...' %}
  - *Reset All Preferences...* Resets all options to their default values. A restart of SNT may be required for changes to take effect.

## 3D Tab

<img align="right" width="300" src="/media/plugins/snt/snt-3d-tab.png" title="3D tab" />
This tab aggregates widgets related to 3D interaction.

### Reconstruction Viewer

The [Reconstruction Viewer](/plugins/snt/reconstruction-viewer) is an advanced, fully scriptable OpenGL viewer enabling 3D visualization and interaction with reconstructions, OBJ meshes (including multiple model organism neuropil annotations and reference brains), computed surfaces (convex hulls) and other shape annotations. For performance reasons, some Path Manager changes may need to be synchronized manually from the RV controls. To open Reconstruction Viewer with the current contents of the Path Manager, press *Open Reconstruction Viewer*. To instead open the viewer press _Reconstruction Viewer_ on the [Shortcuts](#startup) dialog.

### sciview

This option assumes you have [sciview](/plugins/sciview) properly installed. sciview is a modern replacement for the Legacy 3D Viewer, providing sophisticated 3D visualization and virtual reality capabilities for arbitrarily large image volumes and meshes. Integration with [Cx3D](https://github.com/morphonets/cx3d) enables simulation of neurodevelopmental processes, including neuronal growth and formation of cortical circuits. See [SNT: Modeling](/plugins/snt/modeling) for details.

### Legacy 3D Viewer

The Legacy 3D Viewer is a functional tracing canvas, but it depends on outdated services that are now deprecated. It may not function reliably on recent operating systems. For usage instructions, see [Tracing using the Legacy 3D Viewer](/plugins/snt/step-by-step_instructions#tracing-in-the-legacy-3d-viewer).


# Contextual Menu

{% include img align="left" width="250" name="contextual menu" src="/media/plugins/snt/snt-contextual-menu.png" %}

Right-clicking on any of the tracing views will bring up a menu with various editing tools. The corresponding [keyboard shortcuts](/plugins/snt/key-shortcuts) are shown to the right of each option. The list includes:

**Select Nearest Path** {% include key key='G' %} Will select the path closest to the mouse cursor. Pressing {% include key keys='Shift|G' %} will keep adding the closest path to the existing path selection

**Select Paths by 2D ROI** A convenience utility to select path(s) quickly (but coarsely). One the command is run, it is possible to "draw" an area ROI around the paths of interest, so that path(s) intersecting ROI boundaries can be selected. The shape of the ROI (rectangle, oval, freehand, etc.) is determined by the area ROI tool currently selected in ImageJ's main toolbar

**Fork at Nearest Node** {% include key keys='Shift|Alt|Left Click' %} Creates a fork point at the node closest to the mouse cursor. Once a fork point is made, the branch may be extended as described in [Step-By-Step Instructions](/plugins/snt/step-by-step-instructions#branching-start-a-path-on-an-existing-path).

**Continue Extending Path** Allows continued tracing of previously finished paths. Note only one path may be extended at a time. To extend a path: first select it, choose this option, then place additional nodes as shown in [Step-By-Step Instructions](/plugins/snt/step-by-step-instructions#ii-pick-a-subsequent-point).

**Pause SNT** Waives all keyboard and mouse inputs to ImageJ, allowing you to interleave image processing routines with tracing operations. Note that if the image contents change while SNT is paused, the image should be reloaded so that SNT is aware of the changes. Tracing views are annotated with the *SNT Paused* [label](#ui-interaction) to indicate this state.

**Pause Tracing** Disables tracing functions until this option is deselected. Tracing views are annotated with the *Tracing Paused* [label](/plugins/snt/manual#ui-interaction) to indicate this state.

**Sholl Analysis at Nearest Node** {% include key keys='Shift|Alt|A' %} Described in [Analysis › Sholl Analysis (by Focal Point)](/plugins/snt/analysis#sholl-analysis-by-focal-point).


### Editing Paths

<img align="right" src="/media/plugins/snt/snt-path-edit-right-click-menu-active.png" title="Editing paths: contextual menu (v4.2)" width="300" />
Pressing *Edit Path* with a single path selected will activate *Edit Mode*, unlocking the menu options under *Edit Path*. When *Edit Mode* is active, moving the mouse cursor along the path will highlight the nearest node with a crosshair icon and synchronize the current Z-slice to the location of that node. Note that the ability to create new paths is temporarily disabled when in *Edit Mode*.

- **Bring Active Node to Current Z-plane** {% include key key='B' %} Moves the active node to the active Z-plane. Note that the translation is only done in Z. XY positions are unchanged.
- **Delete Active Node** {% include key key='D' %} or {% include key key='Backspace' %} Permanently removes the active node from the path.
- **Insert New Node At Cursor Position** {% include key key='I' %} Inserts a new node at the cursor position. The inserted node is placed between the active node and its parent.
- **Lock Active Node**  {% include key key='L' %} Ensures the active node won't change on cursor movement. Useful for e.g., ensuring that a merge operation is not affected by accidental cursor movement.
- **Move Active Node to Cursor Position** {% include key key='M' %} Moves the active node to the cursor location.
- **Set Active Node Radius...** {% include key key='R' %} Allows radius of active node to be modified. Options include: 1) Assign a specific value or a scaling factor; 2) half of the minimum voxel size; 3) The average radius of flanking nodes; or 4) the average path radius
- **Tag Active Node...** Assigns a color tag to active node. Note paths with color-coded nodes may be rendered differently from default paths in terms of opacity, rendering scale, etc.
- **Connect To (...)** {% include key key='C' %} Allows two existing paths to be connected, typically under a parent-child relationship. Described in this [walkthrough](/plugins/snt/step-by-step-instructions#mergingjoining-paths).
- **Split Tree at Active Node** {% include key key='X' %} Splits the current tree into two subtrees by disconnecting the active node from its parent structure
- **Reset Active Node** Clears the active node
- **Set Active Node as Tree Root** Reorganizes the existing tree so that the active node becomes its root


# Path Manager

<img align="right" width="300" src="/media/plugins/snt/snt-path-manager.png" title="Path Manager (v4.3)" />
![Path Manager](/media/plugins/snt/) The Path Manager dialog displays all existing paths in a hierarchical structure (tree), where one path is "primary" or "root" (path 0) and all other paths (paths 1...N) are children of the primary path. This pattern repeats for each cell being traced. The dialog also contains several menus with various editing, tagging, refinement/fitting, filling and analysis options. Paths can be searched by name and/or tags in the text filter, with more sophisticated search capabilities in the Advanced Filtering Menu.

{% include notice icon="info" content="Path Manager commands are applied to all paths if no paths are selected." %}


## Menu Commands

### Edit ›

#### Delete...
Removes selected Path(s) from the Path Manager. If no Paths are selected, all Paths are deleted.

#### Duplicate...
Duplicates the selected path. Only one Path may be duplicated at a time

#### Rename...
Renames the selected Path. Only one Path may be renamed at a time. Path names are expected to be unique.

#### Merge Primary Path(s) into Shared Root
Takes two or more primary paths and merges them into a common root node placed at the centroid defined by starting nodes of the primary paths to be merged. This is useful, e.g., when all the paths around a soma have been traced without passing through it. Note that this will alter parent-child relationships between Paths and, by consequence, individual nodes.

#### Combine...
Combines two or more _disconnected_ paths into one (undoable operation)

#### Concatenate...
Concatenates two or more paths into a single un-branched segment.

#### Disconnect...
Disconnects the selected Path from all of its connected Path(s) (Undoable operation).

#### Specify Radius...
Assigns a constant radius to all the nodes of selected Path(s). This setting only applies to unfitted Paths and overrides any existing values.

#### Specify No. Spine\Varicosity Markers...
Assigns the no. of markers (e.g., spines or varicosities) to be associated to selected path(s)

#### Ramer-Douglas-Peuker Downsampling...
Given an inputted maximum permitted distance between adjacent nodes, performs {% include wikipedia title="Ramer–Douglas–Peucker algorithm" %} downsampling on the selected Path(s).

#### Rebuild...
Resets all Path IDs and recompute connectivity for all paths. Useful to reset ill-relationships created from mis-editing paths.

### Tag ›
Assigns tags to Paths. Tags allow for paths to be searched, selected, and bookmarked. Note that only SWC-type tags are preserved across restarts when saving traces in the SWC format. All others require data to be saved in SNT's own .Traces format. Tags are organized in the following categories:

#### Type ›
Type of neurite compartment (*Axon*, *(Basal) Dendrite*, *Soma*, etc.), as used by the SWC file format. It is also possible to pair each type with a color tag through the {% include bc path='Tag|Options...' %} dialog. These tags are considered to be essential annotations and all paths are assigned the *Undefined*-type tag when created. For this reason they are not eliminated by the *Remove All Tags* command.

#### Color ›
A preset swatch color, or a custom one chosen from the color chooser (right-click on a blank swatch). Note it is also possible to assign unique (distinctive) colors to a group of paths. Metric-based color mapping can also be applied using the {% include bc path='Analyze|Color Coding...' %} command.

#### Image Metadata ›
Information on hyperstack position details (e.g., channel, frame or slice labels on which a path was traced).

#### Morphometry ›
Morphometric properties, such as *Path length*, *Path mean radius* or *[Path order](/plugins/snt/analysis#path-order-analysis)*.

#### Custom...
Ad-hoc comments.

<span id="refinefit"></span>
### Refine/Fit ›

{% capture text%}
Fitted radii are only exported to [SWC files](/plugins/snt/faq#in-which-format-should-i-save-my-tracings-traces-or-swc) when _Replace existing nodes_ is chosen in {% include bc path='Refine|Parameters...' %}.
{% endcapture %}
{% include notice icon="info" content=text %}

SNT can use the fluorescent signal around traced Paths to optimize curvatures and estimate the thickness of traced structures to sub-voxel accuracy. The optimization algorithm uses pixel intensities to fit circular cross-sections around each node. Once computed, fitted cross-sections can be used to: 1) Infer the radius of nodes, and/or 2) refine node positioning, by snapping their coordinates to the cross-section centroid.

Assuming you chose to fit both centroids and radii, a fitted path might look like the rightmost image below. Notice how the nodes follow the center line of the structure more closely, and how each node now has a non-zero radius approximating that of the traced axon.

<div align="center">
    <img src="/media/plugins/snt/fit-parameter-prompt.png" title="Fitting parameters" height="330" alt="Fitting parameters" />
    <img src="/media/plugins/snt/before-fitting.png" title="Before fitting" height="330" alt="Before fitting" />
    <img src="/media/plugins/snt/after-fitting.png" title="Fitted path" height="330" alt="Fitted path" />
</div>

The {% include bc path='Refine/Fit|' %} menu contains several commands:

#### Fit Path(s).../Un-fit Path(s)/Apply Existing Fit
This is a dynamic menu item that  will change depending on which Path(s) are currently selected. You can use it to 1) Fit selected Path(s), 2) Un-fit Path(s) that have already been fitted, or 3) Toggle cached fits that have not overridden the original path.

#### Explore/Preview Fit

{% include img align="right" name="Explore Fit Animation" src="/media/plugins/snt/explore-fit-preview.png" caption="Explore/Preview Fit command: The 'fly-through' animation can be used to peruse successful (left) and failed (right) fits at each node location. Not that there is nothing inherently _wrong_ about an invalid fit (in this example the failed fit is quite reasonable). The _invalid_ classification only means that the fit violates at least one constraint put in place (see [Fitting Parameters](#parameters)) to avoid rogue displacements of original coordinates." %}

Carves out a region of the image along and around each Path node, generating an animated cross-view (normal plane rendering) allowing to "fly-through" the result of the fitting operation. The animation is synchronized with the tracing image so that the active node in the animation becomes highlighted in the main image. The animation is annotated with the following details:

- **Fitting score** A  "Quality Score" (QS) of fit, with higher values reflecting better fits (akin to a circularity score). It is normalized so that the worst fit in the path is set to zero, the best to 1.
- **Angles** The angle between a node and parent tangent vectors. It is displayed in orange (dashed lines).
- **Modal radius of possible fits** The mode of the radii of all the possible fits attempted by the algorithm at the given location. If the fitting fails, this mode can be used as a 'best guess' radius for that location (as per  {% include bc path='Refine|Parameters...' %}). It is displayed in orange (dashed circumference) and is centered on the original node coordinates.
- **Fallback strategy** The strategy for radius value fallback as specified in  {% include bc path='Refine|Parameters...' %}.
- **Fitted coordinates and radius** Displayed in green when fit is valid, in red when invalid (filled circumference and dot). With invalid fits, the displacement between fitted and original coordinates is highlighted by a connecting line.

#### Discard Fit(s)...
Deletes the existing fit(s) for the selected Path(s), or all fits if no Paths are selected.

#### Parameters...
This command sets fitting options and should be run before computing a fit. Options include:

- **Type of Refinement** Either 1) *Assign radii of fitted cross-sections to nodes*, 2) *Snap node coordinates to cross-section centroids*, or 1) & 2) *Assign fitted radii and snap node coordinates*

- **Max. Radius** Defines (in physical units) the largest radius allowed in the fit. It constrains the optimization to minimize fitting artifacts caused by neighboring structures. This is the most critical parameter influencing the fit. Default is a distance matching ~10 pixels on each side of the path. If you are unsure about suitable values for your images:

  1. Estimate expected thicknesses using manual measurements or using the [Secondary Layer Wizard](#creating-secondary-layers)
  2. As a rule of thumb, consider using 1.5--2× the largest radius in the traced structure
  3. When in doubt, start with a smaller radius and repeat fitting under small increments using  {% include bc path='Explore/Preview Fit' %} to peruse the result

- **Radius fallback** This setting defines what should happen when radii are being fitted but fitting fails at certain node location(s). It allows such nodes to be assigned a 'best guess' (see explanation of *mode* in {% include bc path='Explore/Preview Fit' %}), the smallest radius possible (i.e., minimum voxel separation), or _NaN_. Note that the latter my cause statistical measurements to fail. See [Correct Radii](#correct-radii) for details on how to handle *fallback values*.

- **Min. angle** This is an advanced, micro-optimization setting defining (in degrees) the smallest angle between the fitted node and parent tangent vectors. It minimizes abrupt jaggering between neighboring nodes. For most structures, this value is expected to be between 60 and 90 degrees. Acuter angles are more permissive but may induce more drastic displacements between nodes.

- **Target image** If a [secondary tracing layer](#tracing-on-secondary-image-layer) is being used, this setting defines with image data should be used for fitting.

- **Replace nodes** Defines whether fitted coordinates/radii should replace (override) those of input path(s). Note that SWC export requires fitted values to override original coordinates/radii.

- **Multithreading** The number of parallel threads to be used by SNT while fitting. By default, it is the number of threads specified in [Preferences](#misc)

#### Correct Radii...
<img align="right" width="500" src="/media/plugins/snt/correct-radii.png" title="Correct Radii..." />
If the fitting fails at a certain location (e.g., because the shape of the cross-section is too irregular, or because the fitted centroid is too far off) the program will skip that node moving on to the next. Skipped nodes will retain their original coordinates but their radius may become unset (see _Radius fallback_ in [parameters](#parameters)). This command collects such nodes from selected paths, and assigns them new radii using linear interpolation based on remaining nodes with valid radii. It can apply the interpolation immediately, or simply preview it. Note that by default _NaN_ and negative numbers are always correct. The criteria specified in the prompt are used as extra conditions.

### Fill ›
This menu contains options to start the filling process for selected paths. For detailed instructions see [Filling: Step-By-Step Instructions](/plugins/snt/step-by-step-instructions#filling).

### Analyze ›
This menu contains several options which provide quick ways to analyze and visualize numerical properties of paths and associated branches. Note that these operations are only applied to the subset of currently selected Path(s). To apply these operations to the entire Tree, deselect all Paths first.

#### Color Coding ›
Commands to assign color codes to paths, or cells/branches based on a chosen metric. These commands prompt for the following settings:

- *Color by* Drop-down menu containing the metrics which inform the color mapping.
 
- *LUT* Drop-down menu containing the LUTs (Look Up Tables) that define the color palettes. The LUTs are those that come packaged with ImageJ. The selected LUT is displayed in the color bar directly underneath.
 
- *Rec. Viewer Color Map* If active, opens an instance of the Reconstruction Viewer with the selected paths color coded with the selected LUT.
 
- *Rec. Plotter Color Map* If active, open an instance of the Reconstruction Plotter with the selected paths color coded with the selected LUT.
 
- *Remove Existing Color Coding* Removes existing color coding from the selected paths.

<div align="center">
    <img src="/media/plugins/snt/snt-path-manager-color-mapper.png" title="Color Mapper prompt (v3.0)" width="300" />
    <img src="/media/plugins/snt/snt-color-mapped-op1.png" title="OP1 demo reconstruction color-coded by 'branch order' displayed in Reconstruction Viewer" width="300" />
</div>

#### Frequency Analysis ›
<img align="right" width="400" src="/media/plugins/snt/snt-combined-histograms.png" title="Branch-based Distributions..." />
Commands for retrieving histograms of selected path/branch metric(s). These commands prompt for the following settings:

- *Measurement* Drop-down menu with the available metrics.

- *Polar* Whether the histogram should be plotted using polar coordinates. Typically, this assumes that the data being profiled ranges between 0 and 360 degrees (e.g., bifurcation angles)

#### Measurements ›
Commands for retrieving a table of summary statistics for selected paths/cells. See [Analysis › Measurements](/plugins/snt/analysis#measurements) for details.

#### Convert to ROIs...
<img align="right" width="400" src="/media/plugins/snt/snt-convert-to-rois.png" title="Convert to ROIs prompt prompt" />
Allows conversion of Path(s) to ImageJ [ROIs](https://imagej.net/ij/docs/guide/146-10.html#sec:Selections-Intro) (Regions of Interest). Opens the [ROI Manager](https://imagej.net/ij/docs/guide/146-30.html#fig:The-ROI-Manager), if closed. Options include:

- *Convert* Drop-down menu specifying the structure(s) to convert (branches, branch-points, or end-points)
  
- *View* Drop-down menu specifying which view to overlay the ROIs (applies to 3D images only)
  
- *Impose SWC colors*. If selected, ROIs are colored as per their SWC-type tag
  
- *Adopt path diameter as line thickness* (Applies only to paths with known radius)

#### Multimetric Plot...
Plots a Path metric against several others.

### Plot Profile...
Uses voxel intensities values under path nodes to generate *Intensity vs. Distance* plots for selected Path(s). Refer to the prompt's mouse over tooltips for details.
<div align="center">
    <img src="/media/plugins/snt/snt-path-profile.png" width="500" title="Path profile (v4.1)" />
</div>

#### Skeletonize...
Outputs a binary image that is a topographic skeleton, ie, it generates an empty (zero-filled) image of the same dimensions of the one being traced, then paints a pixel at each node coordinates following the topographic rules of bitmap skeletons in which fork points, tips and slab voxels are determined by voxel connectivity. This command has a couple of configurable settings:

- *Roi filtering*: If an area ROI exists over the image (you may need to pause SNT to create such an ROI), then only paths inside it will be converted
- *Run "Analyze Skeleton" after conversion* Runs the [AnalyzeSkeleton](/plugins/analyze-skeleton) plugin on the skeletonized output image

<img align="right" width="400" src="/media/plugins/snt/snt-straightened-path.png" title="Highlighted path in cyan 'straightened' using Path Manager Analyze>Straighten... command" />

#### Straighten...
Creates a 'linear image' from the pixels associated with a single paths, similarly to [ImageJ's Straighten](/plugins/straighten) command. Useful to e.g., display intensity gradients or featured landmarks along a neurite.

#### Train Weka Classifier...
Uses selected Path(s) to train a random forest classifier (a machine learning algorithm for semantic segmentation) aimed at classifying neurite-associated pixels. Classification is performed by [Trainable Weka Segmentation](/plugins/tws). The resulting classification can be exported into other software, or loaded as secondary tracing layer. Refer to the prompt's built-in documentation for more details.

#### Spine/Varicosity Utilities ›
This menu contains commands tools for analyzing at manually placed markers along paths such as dendritic spines or axonal varicosities. The starting point for such analyses are multipoint ROIs placed along paths. These are detailed in [Step-by-step instructions](/plugins/snt/step-by-step-instructions#spinevaricosity-analysis).

#### Time-lapse Utilities ›
This menu contains commands tools for analyzing time-lapse videos, and assume that the same structure has been traced across multiple frames. Refer to [Step-by-step instructions](/plugins/snt/step-by-step-instructions#time-lapse-analysis) for more details.

#### Save Subset as SWC...
Exports the selected subset of Path(s) as an [SWC](/plugins/snt/faq#what-is-a-swc-file) file. Note the paths to be exported must include a primary path (i.e., one at the top level in the Path Manager hierarchy).


## Filter Toolbar

<img align="right" src="/media/plugins/snt/snt-path-manager-text-filter.png" title="Filtering toolbar (v3.0)" />
The filter toolbar allows paths to be searched and filtered quickly using tags (colors, annotations, SWC-type, etc.) or morphometric properties. The text field is used for text-based searches (recent searches can be recovered through its drop-down menu). The {% include key key='down' %} and {% include key key='up' %} arrow keys find the next/previous occurrence of the entered phrase, while the ![](/media/plugins/snt/snt-text-filter-balloon-button.png) button highlights all occurrences of the entered phrase. Settings for advance text-based filtering can be accessed through the ![](/media/plugins/snt/snt-text-filter-menu-button.png) button, including wildcard support, case-sensitive matching, and replace-by-pattern. In addition, the ![](/media/plugins/snt/snt-text-filter-advanced-button.png) button restricts filtering to the selected subset of Path(s). Other means of filtering Paths include:
<img align="right" src="/media/plugins/snt/snt-path-manager-text-filter-color-filters.png" title="Filtering by color tags (v3.0)" />

- **Color Filters** ![](/media/plugins/snt/snt-text-filter-color-button.png) Allows filtering of Paths by color tags. Custom colors may be selected by right-clicking an empty swatch, which will bring up the CMYK palette. The chosen color is temporarily saved in that swatch.

- **Morphology Filters** ![](/media/plugins/snt/snt-text-filter-morphology-button.png) Allows filtering of Paths by selected morphological properties (including cell identity). Note that these filters do not require Paths to be labeled using {% include bc path='Tag|Morphology| ' %}.
 
  - *Path Order...* Filters for Paths of [Path order](/plugins/snt/analysis#path-order-analysis) in the inputted range. Example queries: `1-2`: selects all primary and secondary paths; `max-max`: selects all terminal paths.
 
  - *Length...* Filters for Paths of length within the inputted range. Example queries: `10-20`: selects all Paths with lengths between 10 and 20μm; `max-max`: selects the longest path(s).

  - *Mean Radius...* Filters for Paths of mean radius within the inputted range.

  - *No. of Nodes...* Filters for Paths with node count within the inputted range.

  - *SWC Type...* Filters for Paths with the selected SWC type tags. Note that the Paths of interest must have been [tagged](/plugins/snt/manual#tag) using the{% include bc path='Tag|Type|' %} menu.


# Fill Manager

Provides controls for all filling operations. It is described in more detail in the [Filling: Step-By-Step Instructions](/plugins/snt/step-by-step-instructions#filling).
