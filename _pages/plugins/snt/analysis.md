---
title: SNT › Analysis
nav-links: true
nav-title: Analysis
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
---

# Sholl Analysis

There are two [Sholl Analysis](/plugins/sholl-analysis) commands available in SNT's *Analysis* menu. The {% include bc path='Analysis|Shuoll Analysis...'%} option provides a set of pre-defined focal points the user can choose from. Note for the morphology-based focal points (e.g., *Soma*, *Root node(s): Primary apical dendrite(s)*) , the relevant morphology tag(s) must be assigned to the set of paths considered by the analysis. To select a focal point manually, see the following section.

{% capture text%}
Sholl Analysis has a dedicated [documentation page](/plugins/sholl-analysis) detailing [parameters](/plugins/sholl-analysis#parameters), [plots](/plugins/sholl-analysis#sholl-plots), and [metrics](/plugins/sholl-analysis#metrics).
{% endcapture %}
{% include notice icon="info" content=text %}

## Sholl Analysis (by Focal Point)

<img align="right" src="/media/plugins/snt/snt-sholl-coarse-intructions.png" title="Initiating Sholl Analysis: coarse method" width="250" alt="Initiating Sholl Analysis: coarse method" />
It is also possible to initiate [Sholl Analysis](/plugins/sholl-analysis) on a tracing in the canvas by manually selecting a focal point. You can do it coarsely by right-clicking near a node and choosing *Sholl Analysis at Nearest Node* from the contextual menu (Shortcut: {% include key keys='Alt|Shift|A' %}.

Alternatively, for precise positioning of the center of analysis:

1. Mouse over the path of interest. Press {% include key key='G' %} to activate it.
2. Press {% include key keys='Alt|Shift' %} to select a node along the path.
3. Press {% include key keys='Alt|Shift|A' %} to start analysis.

<div align="center">
  <img src="/media/plugins/snt/snt-sholl-precise-step-1.png" title="1) Select path" width="250" alt="1) Select path" />
  <img src="/media/plugins/snt/snt-sholl-precise-step-2.png" title="2) Snap cursor to node" width="250" alt="2) Snap cursor to node" />
  <img src="/media/plugins/snt/snt-sholl-precise-step-3.png" title="3) Sholl dialog" width="200" alt="3) Sholl dialog" />
</div>

 The Sholl dialog created by this approach differs slightly from the dialog created by running the {% include bc path='Analyze|Sholl|Sholl Analysis (From Tracings)...'%} plugin in the main Fiji menu. First, the center of analysis is automatically taken from the nearest (or exact) node where the user clicks. In addition to morphology and custom tag filters, the *Path filtering* drop-down menu provides an additional option to restrict the analysis to the subset of paths selected in the Path Manager. Another advantage is that the display canvas allows the radius step size to be previewed visually. To do this, toggle on the *Preview* checkbox under the *Sampling* section and experiment with different step sizes.

<div align="center">
  <img src="/media/plugins/snt/snt-sholl-preview-step-size-1.png" title="fig:Step Size = 0" width="200" alt="Step Size = 0" />
  <img src="/media/plugins/snt/snt-sholl-preview-step-size-2.png" title="fig:Step Size = 5" width="200" alt="Step Size = 5" />
</div>

In addition to the Sholl Profile plot and table, the output of the analysis can be visualized as a color mapping of the reconstruction . To color code the tracing, choose *Color coded paths* from the *Annotations* drop-down menu and select a Lut from the *Annotations Lut* drop-down menu before pressing *Run Analysis*. To output the Sholl Image, choose *3D viewer labels image* from the *Annotations* drop-down menu and select the desired LUT.

<div align="center">
  <img src="/media/plugins/snt/snt-sholl-profile-plot-new.png" title="fig:Sholl Profile Plot" width="310" alt="Sholl Profile Plot" />
  <img src="/media/plugins/snt/snt-sholl-profile-table-new.png" title="fig:Sholl Profile Table" width="232" alt="Sholl Profile Table" />
  <img src="/media/plugins/snt/snt-sholl-color-map.png" title="Traces Color Coded by Sholl Intersections - Ice Lut" width="202" alt="Color Coded Tracing - Ice Lut" />
</div>

# Strahler Analysis

To conduct [Strahler Analysis](/plugins/strahler-analysis) on the current contents of the Path Manager, choose the {% include bc path='Utilities|Strahler Analysis'%} command in the main SNT dialog. This command will output the results of the analysis as a table and plot. These figures contain morphometric statistics on the group of paths associated with each Horton-Strahler Number. Note that this feature analyzes traced reconstructions. To run Strahler analysis on images, use the {% include bc path='Analyze|Skeleton|Strahler Analysis...'%} plugin in the main Fiji dialog.

{% capture text%}
*Strahler Analysis (from Images)* has a dedicated [documentation page](/plugins/strahler-analysis) with useful information.
{% endcapture %}
{% include notice icon="info" content=text %}

<div align="center">
  <img src="/media/plugins/snt/snt-strahler-analysis-table.png" title="fig:Strahler Analysis table" width="300" alt="Strahler Analysis table" />
  <img src="/media/plugins/snt/snt-strahler-analysis-plot.png" title="fig:Strahler Analysis plot" width="300" alt="Strahler Analysis plot" />
</div>

# Path Order Analysis

Found at {% include bc path='Analysis|Path Order Analysis'%} in the main SNT dialog, this option analyzes the Paths in the Path Manager based on *Path Order* as opposed to Strahler classification in which branches are classified (more details on alternative branch classification schemes can be found e.g., [here](https://www.mbfbioscience.com/help/nx11/Content/Branch%20order/Branch_Order.htm)). Produces a table of results and a plot similar to the *Strahler Analysis* option, with morphometric statistics on the group of paths associated with each Branch Order.

<div align="center">
  <img src="/media/plugins/snt/snt-path-order-analysis-table.png" title="Path Order Analysis table" width="300" alt="Path Order Analysis table" />
  <img src="/media/plugins/snt/snt-path-order-analysis-plot.png" title="Path Order Analysis plot" width="300" alt="Path Order Analysis plot" />
</div>

# Measurements

SNT provides several ways to measure reconstructions. A comprehensive selection of measurements can be found by going to {% include bc path='Analysis|Measure...'%}. in the main SNT dialog.

To quickly measure all existing paths with a common set of statistics, choose {% include bc path='Analysis|Quick Measurements'%}. In both cases the results of the measurements are displayed in a common table.

To get measurements only on a select group of Paths, first select or filter for the Paths you want to measure in the Path Manager, then choose either command from the {% include bc path='Analyze'%} menu in the Path Manager.

Batch measurements of reconstructions can be accomplished via scripting. See *Measure\_Multiple\_Files.py* in the SNT [Script Templates](/plugins/snt/scripting#script-templates) for a basic example.

<div align="center">
  <img src="/media/snt-measure-results-table.png" title="Measurements Table" width="90%" />
</div>

# Dendrogram Viewer

<img align="right" src="/media/plugins/snt/snt-dendrogram-shortcuts.png" title="Dendrogram Viewer shortcuts" width="140" alt="Dendrogram Viewer shortcuts" /> 

Found at {% include bc path='Utilities|Create Dendrogram'%}, this option generates a {% include wikipedia title="Dendrogram" %} from one connected component (i.e., a single rooted tree structure) in the Path Manager, providing a high-level overview of neurite branching topology. Note that if multiple rooted trees exist in the Path Manager, you will be prompted to choose one of them.

The viewer provides controls for orientation, zoom level, panning, vertex editing and traversal as well as options to display vertex labels and edge weights (which by default are the euclidean distances between adjacent vertices). To see the available key shortcuts, right click on the viewer and choose *Available Shortcuts...*. The plot may be exported in several file formats, including HTML, PNG and SVG.

Fine-grained programmatic control over SNT's Graph objects is achieved using the [JGraphT API](https://jgrapht.org/javadoc/) in a script. Also relevant is the [sc.fiji.snt.analysis.graph](http://fiji.github.io/SNT/sc/fiji/snt/analysis/graph/package-frame.html) package which provides high-level tools for Graph creation and conversion. See *Graph\_Analysis.py* in the SNT [Script Templates](/plugins/snt/scripting#script-templates) for a basic example.

<div align="center">
  <img src="/media/plugins/snt/snt-dendrogram-viewer.png" title="Dendrogram Viewer" width="500" alt="Dendrogram Viewer" />
</div>

# Comparing Reconstructions

The {% include bc path='Utilities|Compare Reconstructions...'%} command will bring up a prompt which gives the user the option to compare two single reconstruction files against multiple metrics, or multiple groups of reconstruction files against a single metric.

<div align="center">
  <img src="/media/plugins/snt/snt-compare-reconstructions-single-or-group-choice.png" width="250" />
  <img src="/media/plugins/snt/snt-compare-reconstructions-single-file-chooser.png" width="300" />
  <img src="/media/plugins/snt/snt-compare-reconstructions-single-3dviewer-result.png" width="400" />
</div>

If you select, *Compare two files* and press *OK*, a file chooser dialog will appear allowing the user to select two SWC files and their respective colors for display in Reconstruction Viewer.

Use the *Browse* button to select the two files and press 'OK' to run the analysis. The results will include a table containing results of the *Quick Measurements* function for both reconstructions, as well as an instance of the 3D Reconstruction Viewer displaying both reconstructions.

<div align="center">
  <img src="/media/plugins/snt/snt-compare-reconstructions-single-measurements-table.png" title="fig:" width="90%" />
</div>

To instead compare multiple groups of reconstruction files against a single metric, choose *Compare groups of cells (two or more)* in the initial prompt.

<img align="right" src="/media/plugins/snt/snt-compare-reconstructions-group-file-chooser.png" width="200" />

The file selection prompt for this option allows selection of up to four directories containing SWC files. The metric to compare against is chosen from the *Metric* drop-down menu. Optionally, the user may restrict the analysis to specific neurite compartments. After making your selections, press *OK* to run the analysis. The result include multi-panel figure(s) rendering up to ten reconstructions from each group, a window with the metric statistics on each group, a box-plot and a histogram. These figures can all be exported as PNG or SVG.

<div align="center">
  <img src="/media/plugins/snt/snt-compare-reconstruction-group-render1.png" title="Montage of exemplars from Group 1" width="350" />
  <img src="/media/plugins/snt/snt-compare-reconstruction-group-render2.png" title="Montage of exemplars from Group 2" width="350" />
</div>

<div align="center">
  <img src="/media/plugins/snt/snt-compare-reconstruction-group-statistics-window.png" title="Snt-Compare-Reconstruction-Group-Statistics-Window.png" width="300" title="Statistics" />
  <img src="/media/plugins/snt/snt-compare-reconstruction-group-box-plot.png" title="Box-plot" width="200" />
  <img src="/media/plugins/snt/snt-compare-reconstruction-group-histogram.png" title="Histogram" width="300" />
</div>

# Custom Analyses

It is possible to script your own analysis routines. See [SNT Scripting](/plugins/snt/scripting) for the link to SNT's API as well as script templates demonstrating a range of analysis possibilities.
