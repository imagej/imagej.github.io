---
title: SNT › Analysis
nav-links: true
nav-title: Analysis
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
---

# Measurements
{% include img align="right" name="Measurements dialog" src="/media/plugins/snt/snt-measurements-prompt.png" caption="The measurements dialog features options for searching and selecting metrics, renderer measured cells, and summarize existing measurements. An offline guide is also accessible through the <i>Gear</i> menu." %}

SNT provides a couple ways to measure reconstructions. To measure complete cells use {% include bc path='Analysis|Measure...'%} in the main SNT dialog (or {% include bc path='Analyze & Measure| '%} in Reconstruction Viewer). To get measurements only on a select group of Paths, first select or filter for the Paths you want to measure in the Path Manager, then use the commands in Path Manager's {% include bc path='Analyze|Measurements'%} menu.

The reason for distinguishing between cell-based (i.e., branch-based) and path-based measurements is flexibility:  Path-based measurements can be performed on any structures, even those with loops, while cell-based measurements require the structure to be a [graph-theoretic tree](#graph-based-analysis). The bulk of SNT measurements is described in [Metrics](/plugins/snt/metrics).  Measurements available in the GUI are typically single-value metrics. Many others measurements are available via [scripting](/plugins/snt/scripting).

A convenience _Quick Measurements_ command also exists ( {% include bc path='Analysis| '%} menu in the main SNT dialog or {% include bc path='Analyze & Measure| '%} in Reconstruction Viewer), in which common metrics are immediately retrieved using default settings without prompts.

Batch measurements of reconstructions can be accomplished via scripting. See, e.g., the [bundled template script](/plugins/snt/scripting#bundled-templates) *Measure\_Multiple\_Files.py*, and related batch scripts for examples.

**Note on Fitted Paths:**<br>
Some cell-based metrics may not be available when mixing fitted and un-fitted paths because paths are fitted independently of one another and may not be aware of the original connectivity. When this happens, metrics may be reported as NaN and related errors reported to the Console (when running in Debug mode).
If this becomes an issue, consider fitting paths in situ using the Replace existing nodes option instead. Also, remember that you can also use the Path Manager's Edit>Rebuild... command to re-compute relationships between paths

# Statistics
SNT assembles comparison reports and simple statistical reports (two-sample t-test/one-way ANOVA) for up to six groups of cells. This is described in [Comparing Reconstructions](#comparing-reconstructions). In addition, descriptive statistics are commonly reported in histograms from *Frequency/Distribution Analysis* commands.

{% include img align="right" src="/media/plugins/snt/snt-combined-histograms.png" caption="Distributions or morphometric traits..."%}

Notes on SNT charts and plots:

- SNT charts are zoomable, scalable, and rendered using scientific plotting styles to be as publication-ready as possible. Right-click on a plot canvas to export it as vector graphics (PDF or SVG), access customization controls, a light/dark theme toggle, and options to aggregate charts in multi-panel figures

- With simple charts, it is possible double-click on plotted components to edit them and export data as CSV

- Histogram distributions can be fitted to a [normal distribution](https://en.wikipedia.org/wiki/Normal_distribution) (Gaussian) or a [Gaussian mixture model](https://en.wikipedia.org/wiki/Mixture_model) (see _Components & Curve Fitting_ in the histogram right-click menu). In both cases, curves are scaled so that the [area under the curve](https://en.wikipedia.org/wiki/Integral) of the fitted curve matches that of the histogram. [Quartile](https://en.wikipedia.org/wiki/Quartile) marks can also be overlaid. By default, the [Freedman-Diaconis](https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule) rule is used to compute the no. of histogram bins.

- Unless specified, all radial plots display angles in [0°-360°[ degrees

- While SNT is not a statistical analysis software, it does offer some basic convenience methods to parse third-party data. See e.g., [this example](./scripting#analysis-of-external-data) for fitting a Gaussian mixture model to CSV data

# Comparing Reconstructions

<img align="right" width="300px" src="/media/plugins/snt/snt-compare-groups-prompt.png" title=" " />
SNT can compare up to six groups of cells. The entry point for this type of comparison is twofold:
- **{% include bc path='Utilities|Compare Reconstructions/Cell Groups...'%}** in the main SNT dialog. This includes a convenience option to compare single reconstruction files.
- **{% include bc path='Neuronal arbors|Load & Compare Groups...'%}** in Reconstruction Viewer, allowing groups to be tagged, and imported into a common scene while being compared.

The dialog  prompt for this feature allows selection of up to six directories containing reconstruction files (SWC, TRACES, JSON, NDF). The metric to compare against is chosen from the *Metric* drop-down menu. Optionally, it is possible to  restrict the analysis to specific neurite compartments. After making your selections, press *OK* to run the analysis. The result typically includes:

- A simple statistical report, including descriptive statistics and a two-sample t-test (when comparing two groups) or one-way ANOVA (when comparing three or more groups)
- Comparison plots for the chosen metric: Grouped histogram and boxplot
- _Montages_ of groups. These are multi-panel vignettes of up to 10 group exemplars. These can all be exported as PDF, PNG, or SVG

{% include img align="center" src="/media/plugins/snt/snt-compare-reconstructions-overview.png" caption="Comparing _No. of branches_ between two cell groups: Overview of outputs."%}

{% include notice icon="info" content="SNT performs statistical tests without verifying if samples fulfill basic test-criteria (e.g., normality, variance homogeneity, sample size, etc.)" %}


# Convex Hull Analysis
_Convex hull_ commands (in SNT  main dialog, [Rec. viewer](/plugins/snt/reconstruction-viewer) and [Rec. plotter](/plugins/snt/manual#plotter)) compute the 2D or 3D convex hull of a reconstruction (i.e., the smallest convex polygon/polyhedron that contains the nodes of its paths). Convex hull measurements are defined in [Metrics](/plugins/snt/metrics#convex-hull-boundary-size).


# Sholl Analysis

{% capture sholl%}
There are several entry points to Sholl Analysis in SNT. You can find those in the _Neuroanatomy Shortcuts_ panel ({% include bc path='Plugins|Neuroanatomy|'%} or "SNT" icon in Fiji's toolbar):

1. Sholl Analysis (Image): Direct parsing of images, bypassing tracing
2. Sholl Analysis (Tracings): Parsing of reconstructions
3. Sholl Analysis Scripts: These handle batch processing of files, specialized analysis, and misc. utilities

Sholl Analysis has a dedicated [documentation page](./sholl) detailing [parameters](./sholl#parameters), [plots](./sholl#sholl-plots), and [metrics](./sholl#metrics).
{% endcapture %}
{% include notice icon="info" content=sholl %}

In the main SNT dialog, Sholl commands are available in the [Analysis](manual#analysis-) and [image contextual](manual#image-contextual-menu) menus and include:

- **{% include bc path='Sholl Analysis...'%}** Analyzes cells based on a set of pre-defined, morphology-based focal points (e.g., *Soma*, *Root node(s): Primary apical dendrite(s)*). Note that this assumes the relevant morphology tag(s) have been assigned to the set of paths being analyzed. Since the center of analysis is only determined after the prompt has been dismissed, preview of sampling shells may not be available.

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

Note that plots and tables can be directly saved to disk by selecting _Save_ and specifying a valid directory in the dialog. The remaining options in the dialog are described in the [Sholl documentation page](./sholl).

{% include img align="center" src="/media/plugins/snt/sholl-analysis-outputs.png" caption="Overview of Sholl analysis outputs: Linear and log-log profile (Sholl decay calculation), *detailed* and *summary* tables. Note that 'traditional' plots are obtained by disabling curve-fitting altogether."%}


# Strahler Analysis

{% capture strahler%}
Similarly to _Sholl Analysis_, there are several entry points to Strahler Analysis in SNT. You can find those in the _Neuroanatomy Shortcuts_ panel ({% include bc path='Plugins|Neuroanatomy|'%} or "SNT" icon in Fiji's toolbar):

1. [Strahler Analysis (Image)...](./strahler) Direct parsing of images, bypassing tracing
2. Strahler Analysis (Tracings)... Parsing of reconstructions (described in this section)
3. Strahler Analysis Scripts: These handle batch processing of files

{% endcapture %}
{% include notice icon="info" content=strahler %}

{% include img align="right" src="/media/plugins/snt/strahler-classification-example.png" caption="Strahler classification"%}
{% include wikipedia title='Strahler number' text='Strahler numbering'%} is a numerical procedure that summarizes the branching complexity of mathematical trees. The {% include wikipedia title='Strahler number' text='Strahler classification'%} occurs as follows:

- If a brach is terminal (has no children), its Strahler number is one
- If a branch has one child-branch with Strahler number *i*, and all other children-branches have Strahler numbers less than *i*, then the Strahler number of the branch is *i* again
- If a branch has two or more children-branches with Strahler number *i*, and no children-branches with greater number, then the Strahler number of the branch is *i+1*

The *Strahler number* of a neuronal arbor reflects the highest number in the classification, i.e., the number of its root branch. Original publications by {% include wikipedia title='Robert E. Horton' text='Robert E. Horton'%} and {% include wikipedia title='Arthur Newell Strahler' text='Arthur N. Strahler'%} include:

- Arthur N Strahler, Hypsometric (Area-Altitude) Analysis Of Erosional Topography (1952). GSA Bulletin; 63(11): 1117–42. [doi: 10.1130/0016-7606(1952)63[1117:HAAOET]2.0.CO;2](https://doi.org/10.1130/0016-7606(1952)63[1117:HAAOET]2.0.CO;2)
- Arthur N Strahler, Quantitative analysis of watershed geomorphology (1957). Eos, Transactions American Geophysical Union,  38(6), 913–20. [doi: 10.1029/TR038i006p00913](https://doi.org/10.1029/TR038i006p00913) ([PDF](http://www.uvm.edu/~pdodds/files/papers/others/1957/strahler1957a.pdf))

To conduct Strahler analysis on the current contents of the Path Manager, choose the {% include bc path='Analysis|Strahler Analysis...'%} in the main SNT dialog. This command will output the results of the analysis as a table and plot(s). These figures contain morphometric statistics (cf. [Strahler metrics](./metrics)) of branches at each Horton-Strahler number.
{% include img align="center" src="/media/plugins/snt/strahler-analysis-from-reconstructions.png" caption="Strahler Analysis detailed output."%}

To conduct analyses directly from (thresholded) images, have a look at [Strahler Analysis (From Images)](./strahler).

# Path-based Analysis
Path-based analyses accept _any_ traced structure (e.g., disconnected paths, paths associated with different cells, etc.), even those with loops. While most SNT measurements require traced structures to be valid mathematical trees, path-based measurements have no topological constraints. There are two commands in this category: [Path Order Analysis](#path-order-analysis), and [Path Properties: Export CSV...](#path-properties-export-csv).

### Path Order Analysis
This command ({% include bc path='Analysis|Path-based|Path Order Analysis'%} in the main SNT dialog) is a variant of [Strahler](#strahler-analysis) with the following differences:
- Classification is based on _Path Order_: Paths are the scope of classification (not branches)
- Ranking of orders is reversed relatively to Strahler analysis (reversed Strahler orders), with primary paths having _order 1_ and terminal paths having the highest order
- Any collection of paths can be analyzed without validating into a formal tree

### Path Properties: Export CSV...
This command ({% include bc path='Analysis|Path-based|Path Properties: Export CSV...'%}) exports path details morphometrics, neurite compartments, linkage relationships to other Paths, start and end coordinates, etc.) to a spreadsheet file.

# Atlas-based Analysis
Atlas-based analyses require reconstruction nodes to be tagged with neuropil IDs (atlas labels) (e.g., ). Broadly, there are two types of analyses: [Brain Area Frequencies](#brain-area-frequencies) and [Annotations Graphs](#annotations-graphs).


### Brain Area Frequencies
This command ({% include bc path='Analysis|Atlas-based| '%} menu in main dialog, or {% include bc path='Analyze & Measure| '%} in Reconstruction Viewer) summarizes projection patterns across brain areas by computing frequency histograms of how often a morphometric trait (no. of tips, cable length, etc.) occurs across brain regions (neuropil labels). Such histograms can be obtained for groups of cells, isolated cells, or parts thereof.

{% include gallery align="fill" content=
"
/media/plugins/snt/brain-analysis-combined-histograms.png | *Brain Area Frequencies...* in which *No. of tips* was tabulated across the motor cortex subregions associated with the four cells in the *File › Load Demo Dataset...  › MouseLight dendrites* demo dataset
/media/plugins/snt/snt-brain-analysis-ipsi-contra.png | *Brain Area Frequencies...* of a single cell in which *Cable length* of axonal projections was tabulated across ipsilateral and contralateral hemisphere regions.  See the *Hemisphere Analysis* [notebook](https://github.com/morphonets/SNT/tree/main/notebooks) for details
"
%}

### Annotations Graphs
Annotations Graphs rely on brain annotations (i.e., neuropil labels) and are typically used to obtain unbiased, semi-quantitative summaries of projectomes or relationships between brain areas. Annotation graphs can be generated for a single cell or groups of cells. There are three major types of annotation graphs reporting neurite occupancy across brain areas/neuropil regions: 1) Sankey (flow) diagrams, 2) Ferris wheel diagrams, and 3) Boxplots:

{% include gallery align="center" content=
"
/media/plugins/snt/sankey-flow-plot-with-tooltip.png | Flow-plot (Sankey diagram) for two groups of MouseLight PT-neurons: Medulla-projecting (MY Proj.) and Thalamus-projecting (TH Proj.) _Flows_ depict axonal cable length (µm) at target areas (colored using the default ontology color-scheme adopted by the Allen Mouse Brain Common Coordinate Framework, CCFv3).
/media/plugins/snt/brain-analysis-group-boxplot.png | The same flow-plot data in boxplot format (see *Flow and Ferris-Wheel Diagrams Demo* script)
/media/plugins/snt/graph-viewer-ferris-wheel.png | Ferris-wheel diagram for the group of MY-projecting neurons. These cells are located in the secondary motor cortex (MOs, center vertex). Outer vertices depict target areas innervated by the cells' axons (automatically grouped by ontology). Edges encode axonal cable length (µm).
"
%}

Prompts for generation of Annotation graphs, typically require a common set of inputs to be specified:

- **Metric**: The morphometric trait defining connectivity (cable length, no. of tips, etc.)
- **Cutoff value**: Brain areas associated with less than this quantity are excluded from the diagram. E.g., if metric is "No. of Tips" and this value is 10, only brain areas targeted by at least 11 tips are reported
- **Deepest ontology** The highest ontology level to be considered for neuropil labels. As a reference, the deepest level for mouse brain atlases is around 10. Setting this value to 0 forces SNT to consider all depths

Other types of specialized graphs are described in [Graph-based Analysis](#graph-based-analysis).


<span id="dendrogram-viewer"></span>
# Graph-based Analysis
Analyses based on [graph-theory](https://en.wikipedia.org/wiki/Tree_(graph_theory)) are better performed via the [scripting](/plugins/snt/scripting). However, SNT features a quite-capable _Graph Viewer_ that has many built-in options for handling graph objects.

The viewer provides controls for orientation, zoom level, panning, vertex editing and traversal as well as options to customize the display vertices (shape and labels) and edges (shape and weight labels). Basic support for themes (including _dark_, _light_ and _formal_) are also supported. The _Graph Viewer_ canvas may be exported in several file formats, including HTML, PNG, and SVG.

Typically, the most common types of graphs handled by _Graph Viewer_ are:

 - **Graphs based on morphology**: {% include wikipedia title="Dendrogram" %}s can be obtained from single rooted tree structure, and provide a high-level overview of neurite branching topology. In the GUI, dendrograms can be created from {% include bc path='Utilities|Create Dendrogram'%} in the main SNT dialog or {% include bc path='Analyze &amp; Measure|Create Dendrogram'%} in [Reconstruction Viewer](/plugins/snt/reconstruction-viewer). Typically, dendrograms are generated for single cells

 - **Graphs based on brain annotations** As mentioned [above](#annotations-graphs), these rely on brain annotations (i.e., neuropil labels). Annotation graphs can be generated for a single cell or groups of cells

{% include gallery align="center" content=
"
/media/plugins/snt/graph-viewer-dendrogram-simple.png | Dendrogram of a neuronal tree (_Toy neuron_ demo dataset) under the _vertical hierarchical_ layout. Edges depict branch length (µm). Vertices depict the root node (1), branch-, and end- points.
/media/plugins/snt/graph-viewer-dendrogram-color-coded.png | Dendrogram of a neuronal tree (_Toy neuron_ demo dataset) color-coded by edge weight, i.e., branch length (µm), under the default layout (_vertical tree_).
/media/plugins/snt/snt-graph-viewer-ml-dendrites.png | Relationships between brain areas associated with the _MouseLight dendrites_ demo dataset
"
%}

Ultimately, fine-grained programmatic control over SNT's Graph objects is achieved via scripting. Relevant resources:

- [JGraphT](https://jgrapht.org/): The underlying library handling graph theory data structures and algorithms with [JAVA](https://jgrapht.org/javadoc/) and [Python](https://pypi.org/project/jgrapht/) APIs
- [SNT graph package](https://javadoc.scijava.org/SNT/index.html?sc/fiji/snt/analysis/graph/package-summary.html): High-level tools for graph creation within SNT
- *SNT Demo Scripts*: See e.g., *Graph\_Analysis.py* and *Flow\_and\_Ferris\-Wheel\_Diagrams\_Demo.groovy*, two [SNT demo scripts](/plugins/snt/scripting#snt-scripts)
- *Python notebooks*: For [pyimagej](/scripting/pyimagej) examples, have a look at the *Hemisphere Analysis* [notebook](/plugins/snt/scripting#python-notebooks)


# Persistence Homology
<img align="right" width="300px" src="/media/plugins/snt/snt-persistence-landscape.png" title="Visualization of a persistence landscape for ML neuron #AA0039" />
<img align="right" width="350px" src="/media/plugins/snt/snt-persistence-analyzer.png" title="Persistence Homology prompt" />

Persistent homology computes topological features of neuronal reconstructions at different spatial resolutions, which in turn can be used to obtain topological signatures of their branching patterns. The Topological Morphology Descriptor (TMD) is the first published algorithm to use persistence Homology to describe neuronal arbors. It is described in:

Kanari, L., Dłotko, P., Scolamiero, M., Levi, R., Shillcock, J., Hess, K., & Markram, H. (2017). A Topological Representation of Branching Neuronal Morphologies. Neuroinformatics, 16(1), 3–13. [doi:10.1007/s12021-017-9341-1](https://doi.org/10.1007/s12021-017-9341-1).

SNT implements TMD and TMD variants by supporting several descriptor functions:
- Radial: The Euclidean (i.e., "straight line") distance between a node and the tree's root, as used in the original TMD description by Kanari et al.
- Centrifugal: The reversed [Strahler classification](#strahler-analysis) of a node
- Geodesic: The "path distance" between a node and the tree's root
- Path order: The [path order](#path-order-analysis) of a node
- Coordinates: The X, Y, or Z coordinate of a node

In addition, SNT also implements descriptors based on persistence landscapes, as described in Bubenik, P. (2012). Statistical topological data analysis using persistence landscapes. ArXiv. [doi:10.48550/ARXIV.1207.6437](https://doi.org/10.48550/ARXIV.1207.6437).

Currently, _basic_ persistence homology descriptors can be computed using UI commands {% include bc path='Analysis|Persistence Homology...'%} (main interface), or {% include bc path='Analyze & Measure|Persistence Homology...'%} in [Rec. viewer](/plugins/snt/reconstruction-viewer). Complete extraction of descriptors can be obtained with [scripting](/plugins/snt/scripting).  See e.g.,  the *Persistence Landscape* [notebook](https://github.com/morphonets/SNT/blob/main/notebooks/).

# Delineation Analysis

Delineations allow measuring proportions of reconstructions within other structures defined by ROIs or neuropil annotations (e.g., cortical layers, biomarkers, or counterstaining landmarks). Some of the questions that delineation analyses can answer include:

- Do branching patterns of neurons change along strata (cell layers)?
- Do branches near a lesion site differ from branches further away from it?
- Are there morphological differences across subregions of a neuron's receptive field?

Delineations are described in [Walkthroughs › Delineation Analysis](/plugins/snt/walkthroughs#delineation-analysis).

# Root Angle Analysis
Root angle analysis measures the angular distribution of how far neurites deviate from a direct path to the soma (or root of the neuronal arbor), a functional property that is captured by [Sholl profiles](#sholl-analysis). It quantifies properties such as [balancing factor](./metrics#root-angles-balancing-factor), [centripetal bias](./metrics#root-angles-centripetal-bias), and [mean direction](./metrics#root-angles-mean-direction). It is described in:

{% include citation doi='10.1016/j.celrep.2019.04.097' %}

A root angle is defined as the angle between a neurite segment (defined centripetally from the termination point to the soma) and the direct path to the soma or root (see [Bird and Cuntz 2019](https://pubmed.ncbi.nlm.nih.gov/31167149/)). The analysis proceeds as follows:

- Root angles are computed centripetally for every node in the arbor in centripetal sequence (from tips to root)

- The distribution of root angles is fitted to a [von Mises distribution](https://en.wikipedia.org/wiki/Von_Mises_distribution), a specialized probability distribution that models angles/directions. von Mises can be considered a 'wrapped normal', or a circular analogue of the normal distribution, as it addresses the issue of "wrapping" that occurs when dealing with angles revolving around a circle where 0° and 360° (2π) are the same.

- [Centripetal bias](./metrics#root-angles-centripetal-bias), [Balancing factor](./metrics#root-angles-balancing-factor), and [Mean direction](./metrics#root-angles-mean-direction) are then computed from the von Mises fit

The analysis can be performed from the [Analysis menu](/plugins/snt/manual#root-angle-analysis) in the main dialog, Reconstruction Viewer's [Analyze & Measure](/plugins/snt/reconstruction-viewer#analyze--measure) menu, or [template scripts](/plugins/snt/scripting#bundled-templates). The screenshot below depicts the output of the *Analysis › Root Angle Analysis* template script:

{% include img align="fit" src="/media/plugins/snt/snt-root-angle-analysis.png" %}

# Other Specialized Analyses
See [SNT Scripting](/plugins/snt/scripting), as well as script templates demonstrating a range of analysis possibilities.
