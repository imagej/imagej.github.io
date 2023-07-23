---
title: SNT › Analysis
nav-links: true
nav-title: Analysis
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
---

# Brain Area Analysis
See [Graph-based Analysis](#graph-based-analysis).

# Convex Hull Analysis
_Convex hull_ commands (in SNT  main dialog, [Rec. viewer](/plugins/snt/reconstruction-viewer) and [Rec. plotter](/plugins/snt/manual#plotter)) compute the 2D or 3D convex hull of a reconstruction (i.e., the smallest convex polygon/polyhedron that contains the nodes of its paths). Convex hull measurements are defined in [Metrics](/plugins/snt/metrics#convex-hull-boundary-size).

# Measurements

SNT provides a couple ways to measure reconstructions. To measure complete cells use {% include bc path='Analysis|Measure...'%} in the main SNT dialog (or {% include bc path='Analyze & Measure'%} in Reconstruction Viewer). A simplified _Quick Measurements_ variant of this command also exists, in which common metrics are immediately retrieved using default settings. To get measurements only on a select group of Paths, first select or filter for the Paths you want to measure in the Path Manager, then use the commands in the Path Manager's {% include bc path='Analyze|Measurements'%} menu.

{% include img align="center" name="Measurements dialog" src="/media/plugins/snt/snt-measurements-prompt.png" caption="The measurements dialog features an offline guide accessible through the <i>Gear</i> menu." %}

The reason for distinguish between branch-based (ie., cell-based) and path-based measurements is flexibility:  Path-based measurements can be performed on any structures, even those with loops, while branch-based measurements require the structure to be a [graph-theoretic tree](#graph-based-analysis). The bulk of SNT measurements is described in [Metrics](/plugins/snt/metrics).  Measurements available in the GUI are typically single-value metrics. Many others measurements are available via [scripting](/plugins/snt/scripting).

Batch measurements of reconstructions can be accomplished via scripting. See, e.g., the [bundled template script](/plugins/snt/scripting#bundled-templates) *Measure\_Multiple\_Files.py*, and related batch scripts for examples.

**Note on Fitted Paths:**<br>
Some branch-based metrics may not be available when mixing fitted and un-fitted paths because paths are fitted independently from one another and may not be aware of the original connectivity. When this happens, metrics may be reported as NaN and related errors reported to the Console (when running in Debug mode).
If this becomes an issue, consider fitting paths in situ using the Replace existing nodes option instead. Also, remember that you can also use the Path Manager's Edit>Rebuild... command to re-compute relationships between paths

# Statistics
SNT assembles comparison reports and simple statistical reports (two-sample t-test/one-way ANOVA) for up to six groups of cells. This is described in [Comparing Reconstructions](#comparing-reconstructions). In addition, descriptive statistics are commonly reported in histograms from *Frequency/Distribution Analysis* commands.

{% include img align="center" src="/media/plugins/snt/snt-combined-histograms.png" caption="Example of histograms obtained from the Path Manager's _Branch-based Distributions..._ command."%}

<span id="dendrogram-viewer"></span>
# Graph-based Analysis
Analyses based on [graph-theory](https://en.wikipedia.org/wiki/Tree_(graph_theory)) are better performed via the [scripting](/plugins/snt/scripting). However, SNT features a quite-capable _Graph Viewer_ that has many built-in options for handling graph objects. 

The viewer provides controls for orientation, zoom level, panning, vertex editing and traversal as well as options to customize the display vertices (shape and labels) and edges (shape and weight labels). Basic support for themes (including _dark_, _light_ and _formal_) are also supported. The_Graph Viewer_ canvas may be exported in several file formats, including HTML, PNG and SVG.

Typically, the most common types of graphs handled by _Graph Viewer_ are:

 - **Dendrograms**: {% include wikipedia title="Dendrogram" %}s can be obtained from single rooted tree structure, and provide a high-level overview of neurite branching topology. In the GUI, dendrograms can be created from {% include bc path='Utilities|Create Dendrogram'%} in the main SNT dialog or {% include bc path='Analyze &amp; Measure|Create Dendrogram'%} in [Reconstruction Viewer](/plugins/snt/reconstruction-viewer).

 - **Annotation Graphs** These rely on brain annotations (i.e., neuropil labels) and are typically used to summarize projectomes or relationships between brain areas, including ferris-wheel diagrams. Note that annotation graphs can be generated for a single cell or groups of cells.

{% include gallery align="fill" content=
"
/media/plugins/snt/graph-viewer-dendrogram-simple.png | Dendrogram of a neuronal tree (_Toy neuron_ demo dataset) under the _vertical hierarchical_ layout. Edges depict branch length (µm). Vertices depict the root node (1), branch-, and end- points.
/media/plugins/snt/graph-viewer-dendrogram-color-coded.png | Dendrogram of a neuronal tree (_Toy neuron_ demo dataset) color-coded by edge weight, i.e., branch length (µm), under the default layout (_vertical tree_).
/media/plugins/snt/graph-viewer-ferris-wheel.png | Ferris-wheel diagram for a group of MouseLight PT-neurons (medulla-projecting) located in the secondary motor cortex (MOs, center vertex). Outer vertices depict target areas innervated by the cells' axons (automatically grouped by ontology). Edges encode axonal cable length (µm).
"
%}

Two other type of _Brain Area Analysis_ visualizations relying on graph-based analysis (but not _Graph Viewer_) include boxplots and Sankey (flow) diagrams reporting innervation across brain areas/neuropil regions:

{% include gallery align="fill" content=
"
/media/plugins/snt/sankey-flow-plot-with-tooltip.png | Flow-plot (Sankey diagram) for two groups of MouseLight PT-neurons: Medulla-projecting (MY Proj.) and Thalamus-projecting (TH Proj.) _Flows_ depict axonal cable length (µm) at target areas () colored using the default ontology color-scheme adopted by the Allen Mouse Brain Common Coordinate Framework, CCFv3).
/media/plugins/snt/brain-analysis-group-boxplot.png | The same flow-plot data in boxplot format (see *Flow and Ferris-Wheel Diagrams Demo* script)
/media/plugins/snt/brain-analysis-combined-boxplot.png | *Analysis › Brain Area Analysis...* histogram in which frequencies of a particular morphometric trait are retrieved across brain areas (neuropil labels). In this example, *No. of tips* was retrieved for the four cells in the *MouseLight dendrites* demo dataset (*File › Load Demo Dataset...*)
"
%}

Ultimately, fine-grained programmatic control over SNT's Graph objects is achieved via scripting. Relevant resources:
- [JGraphT](https://jgrapht.org/): The underlying library handling graph theory data structures and algorithms ([JAVA API](https://jgrapht.org/javadoc/) and [Python API](https://pypi.org/project/jgrapht/).
- [SNT graph package](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/graph/package-summary.html): High-level tools for graph creation within SNT
- *SNT Demo Scripts*: See e.g., *Graph\_Analysis.py* and *Flow\_and\_Ferris\-Wheel\_Diagrams\_Demo.groovy*, two [SNT demo scripts](/plugins/snt/scripting#snt-scripts).. 
- *Python notebooks*: For [pyimagej](/scripting/pyimagej) examples, have a look at the *Hemisphere Analysis* [notebook](/plugins/snt/scripting#python-notebooks).

# Sholl Analysis

{% capture sholl%}
There are several entry points to Sholl Analysis in SNT. You can find those in the _Neuroanatomy Shortcuts_ panel ({% include bc path='Plugins|Neuroanatomy|'%} or "SNT" icon in Fiji's toolbar):

1. Sholl Analysis (Image): Direct parsing of images, bypassing tracing
2. Sholl Analysis (Tracings): Parsing of reconstructions
3. Sholl Analysis Scripts: These handle batch processing of files, specialized analysis, and misc. utilities 

Sholl Analysis has a dedicated [documentation page](/plugins/sholl-analysis) detailing [parameters](/plugins/sholl-analysis#parameters), [plots](/plugins/sholl-analysis#sholl-plots), and [metrics](/plugins/sholl-analysis#metrics).
{% endcapture %}
{% include notice icon="info" content=sholl %}


In the main SNT dialog, Sholl commands are available in the {% include bc path='Analysis| '%} menu and image contextual menu and include:

-  **{% include bc path='Sholl Analysis...'%}** Analyzes cells based on a set of pre-defined, morphology-based focal points (e.g., *Soma*, *Root node(s): Primary apical dendrite(s)*). Note that this assumes the relevant morphology tag(s) have been assigned to the set of paths being analyzed. Since the center of analysis is only determined after the prompt has been dismissed, preview of sampling shells may not be available.

- **{% include bc path='Sholl Analysis (by Focal Point)...'%}** Analyzes cells on an _exact_, user-defined focal point. It is described on the following section.

- **{% include bc path='Sholl Analysis at Nearest Node'%}** Coarser alternative to {% include bc path='Sholl Analysis (by Focal Point)...'%}, run from the image contextual menu by right-clicking _near_ a node (Shortcut: {% include key keys='Alt|Shift|A' %}.

## Sholl Analysis (by Focal Point)

For precise positioning of the center of analysis:

1. Mouse over the path of interest. Press {% include key key='G' %} to activate it
   <img align="right" width="400px" src="/media/plugins/snt/sholl-analysis-by-focal-point.png" title=" " />
2. Then, select the node to be used as focal point. This can be done in one of two ways:
   1. Select a node along the path as you would for forking operation: i.e., by pressing {% include key keys='Alt|Shift' %} while moving the cursor along the path (Note the "Fork Point" label appearing near the cursor on non-display canvases). With {% include key keys='Alt|Shift' %} still pressed, press  {% include key keys='A' %} to start the analysis
   2. Make the path editable (right-click on the image and choose _Edit Path_ from the contextual menu). Move the cursor along the path until the desired node is highlighted. Press  {% include key keys='Alt|Shift|A' %} to start the analysis

NB: The default {% include key keys='Alt|Shift' %} modifier can be simplified in the _Options_ tab of the main dialog.

The Sholl dialog created by this approach is a variant of the dialog created by running the {% include bc path='Sholl|Sholl Analysis (From Tracings)...'%} from the _Neuroanatomy Shortcuts_ panel, with a couple of changes:
1. Since the center of analysis is defined precisely on an image, radius step size can be previewed 
2. The *Path filtering* drop-down menu provides additional options to restrict the analysis to the subset of paths selected in the Path Manager
3. The type of annotations is more specialized and includes:
  - **Color coded nodes** Intersection counts will be color mapped into path nodes under the _annotation LUT_.
  - **3D viewer labels image** This generates a synthetic image holding the number of intersections at each distance from the center under _annotation LUT_. This image can then be fed to the "Apply Color Labels" action of the legacy 3D viewer, to "overlay" the mapping on the legacy 3D viewer scene.

Note that plots and tables can be directly saved to disk by selecting _Save_ and specifying a valid directory in the dialog. The remaining options in the dialog are described in the [Sholl documentation page](/plugins/sholl-analysis).

{% include img align="center" src="/media/plugins/snt/sholl-analysis-outputs.png" caption="Overview of Sholl analysis outputs: Linear and log-log profile (Sholl decay calculation), *detailed* and *summary* tables. Note that 'traditional' plots are obtained by disabling curve-fitting altogether."%}

# Strahler Analysis
{% capture strahler%}
Similarly to _Sholl Analysis_, there are several entry points to Strahler Analysis in SNT. You can find those in the _Neuroanatomy Shortcuts_ panel ({% include bc path='Plugins|Neuroanatomy|'%} or "SNT" icon in Fiji's toolbar):

1. Strahler Analysis (Image)... Direct parsing of images, bypassing tracing
2. Strahler Analysis (Tracings)... Parsing of reconstructions
3. Strahler Analysis Scripts: These handle batch processing of files

_Strahler Analysis (Image)_ has a dedicated [documentation page](/plugins/strahler-analysis) with details on the classification.
{% endcapture %}
{% include notice icon="info" content=strahler %}

To conduct [Strahler Analysis](/plugins/strahler-analysis) on the current contents of the Path Manager, choose the {% include bc path='Analysis|Strahler Analysis...'%} in the main SNT dialog. This command will output the results of the analysis as a table and plot(s). These figures contain morphometric statistics of branches at each Horton-Strahler number. Refer to the _Strahler Analysis (Image)_ [documentation](/plugins/strahler-analysis) for details on the classification.
{% include img align="center" src="/media/plugins/snt/strahler-analysis-from-reconstructions.png" caption="Strahler Analysis detailed output."%}

# Path Order Analysis

Found at {% include bc path='Analysis|Path Order Analysis'%} in the main SNT dialog, this option is a variant of Strahler with the following differences:
- Classification is based on _Path Order_: Paths are the scope of classification (not branches)
- Ranking of orders is reversed relatively to Strahler analysis (reversed Strahler orders), with primary paths having _order 1_ and terminal paths having the highest order
- Classification accepts _any_ structure: Since classification is path-based, there are no topological constrains in the analysis. While Strahler requires structures to be valid mathematical trees, Path order analysis can be performed on any structures, even those with loops

# Persistence Analysis
Currently, persistence analysis is only available via [scripting](/plugins/snt/scripting).  See e.g.,  the *Persistence Landscape* [notebook](/plugins/snt/scripting#python-notebooks).

# Comparing Reconstructions
<img align="right" width="300px" src="/media/plugins/snt/snt-compare-groups-prompt.png" title=" " />
SNT can compare up to six groups of cells. The entry point for this type of comparison is twofold:
- **{% include bc path='Utilities|Compare Reconstructions/Cell Groups...'%}** in the main SNT dialog. This includes a convenience option to compare single reconstruction files.
- **{% include bc path='Neuronal arbors|Load &amp; Compare Groups...'%}** in Reconstruction Viewer, allowing groups to be tagged, and imported into a common scene while being compared.

The dialog  prompt for this feature allows selection of up to six directories containing reconstruction files (SWC, TRACES, JSON, NDF). The metric to compare against is chosen from the *Metric* drop-down menu. Optionally, it is possible to  restrict the analysis to specific neurite compartments. After making your selections, press *OK* to run the analysis. The result typically includes:
- A simple statistical report, including descriptive statistics and a two-sample t-test (when comparing two groups) or one-way ANOVA (when comparing three or more groups)
- Comparison plots for the chosen metric: Grouped histogram and boxplot
- _Montages_ of groups. These are multi-panel vignettes of up to 10 group exemplars. These can all be exported as PNG or SVG.

{% include img align="center" src="/media/plugins/snt/snt-compare-reconstructions-overview.png" caption="Comparing _No. of branches_ between two cell groups: Overview of outputs."%}

{% include notice icon="info" content="SNT performs statistical tests without verifying if samples fulfill basic test-criteria (e.g., normality, variance homogeneity, sample size, etc.)" %}

# Custom Analyses

It is possible to script your own analysis routines. See [SNT Scripting](/plugins/snt/scripting) for the link to SNT's API as well as script templates demonstrating a range of analysis possibilities.


