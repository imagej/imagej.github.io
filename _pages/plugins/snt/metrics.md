---
title: SNT › Metrics
nav-links: true
nav-title: Metrics
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
extensions: ["mathjax"]
tags: snt,reconstruction,tracing,arbor,neuron,morphometry,dendrite,axon,neuroanatomy
---

## Metrics
{% capture text%}
**This list is focused on default measurements available through SNT's GUI and does not include specialized metrics available via its scripting API. Thus, it only captures [a subset](#notes) of the full repertoire of SNT metrics.**
<br><br>
**For each metric SNT retrieves the descriptive statistics _Mix_, _Max_, _Mean_, _Standard Deviation_ (SD), _Sum_ and _N_**, which may lead to inevitable [redundancy](#notes) between measurements. E.g., when measuring  [Branch length](#branch-length) for a particular cell, it is possible to retrieve the length of the smallest branch (_Min_), the longest (_Max_), the average and standard deviation of all branch lengths (_Mean_ and _SD_), their total length (_Sum_), and number (_N_).
<br><br>
Metrics ported from published literature include their associated publication in the definition.
{% endcapture %}
{% include notice icon="info" content=text %}


<span id="b"></span>
##### Branch contraction
A measure of _straightness_. The ratio between the Euclidean distance of a branch (i.e., Euclidean distance between the first and last node of the branch) and its path length. Range of values: ]0--1] (unitless). L-measure metric[^2]
<br>See also: [Path contraction](#path-contraction)

##### Branch extension angle XY
The absolute [extension angle](#extension-angle) of a branch in the XY plane

##### Branch extension angle XZ
The absolute [extension angle](#extension-angle) of a branch in the XZ plane

##### Branch extension angle ZY
The absolute [extension angle](#extension-angle) of a branch in the ZY plane

##### Branch fractal dimension
Also known has [Hausdorff dimension](https://en.wikipedia.org/wiki/Hausdorff_dimension). Defined as the slope obtained from the log-log plot of _Path distance vs Euclidean distance_, as [implemented by L-measure](http://cng.gmu.edu:8080/Lm/help/index.htm) following the definition of [Marks & Burke (2007)](https://doi.org/10.1002/cne.21418). It is only computed for branches defined by at least five nodes. L-measure metric[^2] described in:
{% include citation doi='10.1002/cne.21418' %}

##### Branch length
The _path length_ of a branch (i.e., the sum of all its internode distances)
<br>See also: [Path length](#path-length)

##### Branch mean radius
The average of the radii of the nodes defining a branch

##### Branch surface area
_Estimated_ surface area[^1] of a branch computed from treating each internode segment as a conical frustum and summing the surface area of all frusta

##### Branch volume
_Estimated_ volume[^1] of a branch computed from treating each internode segment as a conical frustum and summing the volume of all frusta

<span id="c"></span>
##### Cable length
The total path length of a structure, i.e., the sum of all internode distances of its paths

##### Complexity Indices
Complexity Indices are ratios of anatomical properties that summarize branching patterns. Typically, this type of descriptors have been created to summarize (early) neural development in vitro

###### Complexity index: ACI
Also known as "Axonal Complexity Index". An index based on path orders, defined as $$\frac{\sum_{n=1}^{N} {Path\,order - 1}}{N}$$, with $$N$$ being the total number of paths in the reconstruction. Described in:

{% include citation doi='10.1523/JNEUROSCI.4434-06.2007' %}

###### Complexity index: DCI
Also known as "Dendritic Complexity Index". An index based on the number of primary neurites, total arbor length, and the number and Strahler-order of terminal branches. Described in:

{% include citation doi='10.1523/JNEUROSCI.19-22-09928.1999' %}

##### Convex hull
Defined as the polygon (2D) or the polyhedron (3D) enclosing a reconstruction

###### Convex hull: Boundary size
The perimeter of the 2D polygon or the surface area of the 3D polyhedron of the [convex hull](#convex-hull)

###### Convex hull: Boxivity
The extent to which the [convex hull](#convex-hull) approaches a rectangle (if 2D) or a cuboid (if 3D). Range of values: 0--1 (unitless)

###### Convex hull: Centroid-root distance
The distance between the root of a neuronal arbor and the centroid of its [convex hull](#convex-hull)

###### Convex hull: Compactness
The ratio between $$area^3/volume^2$$ of the 3D [convex hull](#convex-hull), normalized so that a sphere has a compactness value of 1. Defined in [Bribiesca E, 2008](https://doi.org/10.1016/j.patcog.2007.06.029). Not applicable to 2D convex hulls. Range of values: 0--1 (unitless)

###### Convex hull: Eccentricity
Defined as $$\sqrt{1 - \left(\frac{b}{a}\right)^2}$$, where $$a$$ and $$b$$ are the semi-major and semi-minor axes of the 2D [convex hull](#convex-hull). Not applicable to 3D Convex hulls. An eccentricity of 0 corresponds to a perfect circle. An eccentricity close to 1 indicates a highly elongated ellipse. Unitless

###### Convex hull: Elongation
The [caliper (Feret) diameter](https://en.wikipedia.org/wiki/Feret_diameter) of the [convex hull](#convex-hull)

###### Convex hull: Roundness
The extent to which the [convex hull](#convex-hull) approaches a circle (i.e., circularity in 2D) or a sphere (i.e., sphericity in 3D). Range of values: 0--1 (unitless)

###### Convex hull: Size
Either the area of the 2D polygon, or the volume of the 3D polyhedron defining the [convex hull](#convex-hull)

<span id="d"></span>
##### Depth
The depth of the bounding box embedding the structure being measured

<span id="e"></span>
##### Extension angle
The _overall_ outgrowth direction of a branch or path with at least two nodes. It is obtained from the slope of a linear regression performed across allcoordinates on either the XY, XZ, or ZY plane. Extension angles can be _absolute_ or _relative_ (_rel._):

- _Absolute angles_ are measured with respect to a fixed reference and range from [0°-360°[ under a _West-clockwise_ convention (W: 0°; N: 90°; E: 180°; S: 270°)

- _Relative (rel.) angles_ are measured as the acute intersection angle between the extension angle of a branch/path and the extension angle of its parent, and range between [0°-180°[. When no parent exists the relative extension angle is _NaN_

<span id="h"></span>
##### Height
The height of the bounding box embedding the structure being measured

##### Horton-Strahler bifurcation ratio
The average bifurcation ratio of [Strahler bifurcation ratios](https://en.wikipedia.org/wiki/Strahler_number#Bifurcation_ratio)

##### Horton-Strahler root number
The highest Horton-Strahler number of a tree, i.e., the Horton-Strahler number of its root node 

<span id="i"></span>
##### Inner branches
Defined as the branches of highest Strahler order. Typically, these correspond to the most 'internal' branches of an arbor, in direct sequence from the root. Note that _Primary branches_ are _inner branches_ starting at the tree's root
<br>See also: [Primary branches](#primary-branches), [Terminal branches](#terminal-branches)

###### Inner branches: Extension angle XY
The absolute [extension angle](#extension-angle) of [inner branches](#inner-branches) in the XY plane

###### Inner branches: Extension angle XZ
The absolute [extension angle](#extension-angle) of [inner branches](#inner-branches) in the XZ plane

###### Inner branches: Extension angle ZY
The absolute [extension angle](#extension-angle) of [inner branches](#inner-branches) in the ZY plane

###### Inner branches: Length
The length of [inner branches](#inner-branches)

##### Internode angle
The angle (in degrees, 0-360 range) between a node and its immediate neighbors. I.e., if node B is preceeded by node A and followed by node C, the internode angle at position B is defined as the angle between vecors AB and BC: $$\angle (\overrightarrow{AB}, \overrightarrow{BC})$$

##### Internode distance
The distance between nodes defining a branch or a Path. Can be retrieved as _squared internode distance_ when faster computations are required

<span id="l"></span>
##### Longest shortest path
The longest graph geodesic. Considering a [graph-theory tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)), the _longest shortest path_ corresponds to its [graph diameter](https://mathworld.wolfram.com/GraphDiameter.html) (also known as maximum geodesic, or longest graph geodesic). Can only be computed for structures that are valid mathematical trees.

###### Longest shortest path: Extension angle XY
Absolute [Extension angle](#extension-angle) of [longest shortest path](#longest-shortest-path) in the XY plane

###### Longest shortest path: Extension angle XZ
Absolute [Extension angle](#extension-angle) of [longest shortest path](#longest-shortest-path) in the XZ plane

###### Longest shortest path: Extension angle ZY
Absolute [Extension angle](#extension-angle) of [longest shortest path](#longest-shortest-path) in the ZY plane

###### Longest shortest path: Length
Length of [longest shortest path](#longest-shortest-path)

<span id="m"></span>
##### Maximum geodesic
Same as [Length of longest shortest path](#longest-shortest-path-length)

<span id="n"></span>
##### No. of branch nodes (branch fragmentation)
The total number of nodes (and thus _compartments_) in a branch

##### No. of branch points
The total number (count) of branch points (also known as fork points)

##### No. of branches
The total number (count) of branches

##### No. of fitted paths
The total number (count) of [fitted](/plugins/snt/manual#refinefit) paths

##### No. of inner branches
The number of branches of highest Strahler order. Typically, these correspond to the most 'internal' branches of an arbor, in direct sequence from the root

##### No. of path nodes (path fragmentation)
 The total number of nodes (and thus _compartments_) in a path

##### No. of paths
The total number (count) of paths defining a structure

##### No. of primary branches
The total number (count) of primary (or root-associated) branches. Primary branches have origin in a tree's root, extending to the closest branch point or end-point, i.e., they are _inner branches_ starting at the root. Note that a primary branch can also be terminal.

##### No. of spines/varicosities
Sum of all spine/varicosity markers in a structure

##### No. of spines/varicosities per path
Number of spines/varicosities associated with a path

##### No. of terminal branches
The total number (count) of branches ending at terminal endpoints (tips)

##### No. of tips
The total number (count) of terminal endpoints in a structure

##### No. of total nodes
The total number (count) of nodes in a structure

##### Node intensity values
The pixel intensity at each node location

##### Node radius
The radius at each node, typically obtained from [fitting procedures](/plugins/snt/manual#refinefit)

<span id="p"></span>
##### Partition asymmetry
L-measure metric[^2]. Computed at each bifurcation point of the structure being measured. Note that branch points with more than 2 children are ignored. Given $$n1, n2$$ the number of tips on each side of a bifurcation point, Partition asymmetry is defined as: $$\frac{abs(n1-n2)}{(n1+n2-2)}$$. 

##### Path channel
The color channel associated with a path (multidimensional images)

##### Path contraction
A measure of straightness of a path. See [Branch contraction](#branch-contraction) for definition

##### Path extension angle XY
Absolute [Extension angle](#extension-angle) of a path in the XY plane

##### Path extension angle XY (Rel.)
Relative [Extension angle](#extension-angle) of a path in the XY plane

##### Path extension angle XZ
Absolute [Extension angle](#extension-angle) of a path in the XZ plane

##### Path extension angle XZ (Rel.)
Relative [Extension angle](#extension-angle) of a path in the XZ plane

##### Path extension angle ZY
Absolute [Extension angle](#extension-angle) of a path in the ZY plane

##### Path extension angle ZY (Rel.)
Relative [Extension angle](#extension-angle) of a path in the ZY plane

##### Path frame
The time-point associated with a path (multidimensional images)

##### Path length
The sum of all internode distances in a path
<br>See also: [Branch length](#branch-length)

##### Path mean radius
The average of the radii of the nodes defining a traced path

##### Path order
See [Path Order Analysis](/plugins/snt/analysis#path-order-analysis)

##### Path spine/varicosity density
The number (count) of spine/varicosity markers associated with a path, divided by its path length

##### Path surface area
_Estimated_ surface area[^1] of a path computed from treating each internode segment as a conical frustum and summing the surface area of all frusta

##### Path volume
_Estimated_ volume[^1] of a path computed from treating each internode segment as a conical frustum and summing the volume of all frusta

##### Persistence diagram
See [persistence homology](/plugins/snt/analysis#persistence-homology)

##### Persistence landscapes
See [persistence homology](/plugins/snt/analysis#persistence-homology)

##### Primary branches
Primary branches that have origin in a tree's root, extending to the closest branch point or end-point, i.e., [inner branches](#inner-branches) starting at the root. Also known as root-associated branches. Note that a primary branch can also be terminal
<br>See also: [Inner branches](#inner-branches), [Terminal branches](#terminal-branches)

###### Primary branches: Extension angle XY
Absolute [Extension angle](#extension-angle) of [primary branches](#primary-branches) in the XY plane

###### Primary branches: Extension angle XZ
Absolute [Extension angle](#extension-angle) of [primary branches](#primary-branches) in the XZ plane

###### Primary branches: Extension angle ZY
Absolute [Extension angle](#extension-angle) of [primary branches](#primary-branches) in the ZY plane

###### Primary branches: Length
The length of [primary branches](#primary-branches)
<br>See also: [Inner branches length](#inner-branches-length), [Terminal branches length](#terminal-branches-length)

<span id="r"></span>
##### Remote bif. angles
The angle between each bifurcation point and its children in the simplified graph, which comprise either branch points or terminal nodes. Note that branch points with more than 2 children are ignored. L-measure metric[^2]

<span id="balancing-factor"></span><span id="bf"></span>
##### Root angles: Balancing factor
Dimensionless property related to [Centripetal bias](#root-angles-centripetal-bias) but with range $$[0, 1]$$. It is sufficient to produce realistic neuronal morphologies with generalized minimum spanning tree modeling. Described in:

{% include citation doi='10.1371/journal.pcbi.1000877' %}

##### Root angles: Centripetal bias
[Root angle analysis](/plugins/snt/analysis#root-angle-analysis) metric (dimensionless, range: $$[0,\infty[$$). It is defined as the concentration ($$\kappa$$) of the von Mises fit of the root angle distribution: $$\kappa=0$$ indicate no bias (root angles are distributed uniformly) while $$\kappa\to\infty$$ indicate that all neurites point directly toward the root of the tree

##### Root angles: Mean direction
[Root angle analysis](/plugins/snt/analysis#root-angle-analysis) metric. The mean direction of the fitted von Mises distribution (in degrees).

<span id="s"></span>
##### Sholl: Decay
The [Sholl regression coefficient](/plugins/snt/sholl#sholl-decay)

##### Sholl: Degree of Polynomial fit
The polynomial degree used to fit the Sholl profile. See [Sholl › Fitting functions](/plugins/snt/sholl#eq1)

##### Sholl: Kurtosis
See [Kurtosis](/plugins/snt/sholl#kurtosis) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: Max
See [Max inters.](/plugins/snt/sholl#max-inters) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: Max (fitted)
See [Critical value](/plugins/snt/sholl#critical-value) in [Sholl › Metrics based on fitted data](/plugins/snt/sholl#metrics-based-on-fitted-data)

##### Sholl: Max (fitted) radius
See [Critical radius](/plugins/snt/sholl#critical-radius) in [Sholl › Metrics based on fitted data](/plugins/snt/sholl#metrics-based-on-fitted-data)

##### Sholl: Mean
See [Mean inters.](/plugins/snt/sholl#mean-inters) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: No. maxima
The number of times _Max inters._ occurs in a Sholl profile. See [Max inters.](/plugins/snt/sholl#max-inters) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: No. secondary maxima
The number of times a secondary peak occurs in a Sholl profile. See [Max inters.](/plugins/snt/sholl#max-inters) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: Ramification index
See [Schoenen Ramification index](/plugins/snt/sholl#schoenen-sampled) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: Skewness
See [Skewness](/plugins/snt/sholl#skewness) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Sholl: Sum
See [Sum inters.](/plugins/snt/sholl#sum) in [Sholl › Metrics based on sampled data](/plugins/snt/sholl#metrics-based-on-sampled-data)

##### Surface area
Treating each internode segment as a conical frustum, the sum of the surface areas[^1] of all frusta

<span id="t"></span>
##### Terminal branches
Branches ending at terminal endpoints (tips)
<br>See also: [Inner branches](#inner-branches), [Primary branches](#primary-branches)

###### Terminal branches: Extension angle XY
Absolute [Extension angle](#extension-angle) of [terminal branches](#terminal-branches) in the XY plane

###### Terminal branches: Extension angle XZ
Absolute [Extension angle](#extension-angle) of [terminal branches](#terminal-branches) in the XZ plane

###### Terminal branches: Extension angle ZY
Absolute [Extension angle](#extension-angle) of [terminal branches](#terminal-branches) in the ZY plane

###### Terminal branches: Length
The sum of branch lengths of branches ending at terminal endpoints (tips)
<br>See also: [Inner branches length](#inner-branches-length), [Primary branches length](#primary-branches-length)

##### TMD
Topological Morphology Descriptor. See [persistence homology analysis](/plugins/snt/analysis#persistence-homology)

<span id="v"></span>
##### Volume
Treating each internode segment as a conical frustum, the sum of the volume[^1] of all frusta

<span id="w"></span>
##### Width
The width of the bounding box embedding the structure being measured

<span id="x"></span>
##### X,Y,Z coordinates
Cartesian coordinates in the three-dimensional space

### Notes

- This list does not include all of the specialized metrics provided by dedicated modules, such as [Strahler](/plugins/snt/analysis#strahler-analysis), [Sholl](/plugins/snt/sholl#metrics), [Persistence diagrams/landscapes](/plugins/snt/analysis#persistence-homology), or [Graph-based](/plugins/snt/analysis#graph-based-analysis) analysis

- Some combinations of metrics/statistics may not be meaningful: e.g., when measuring a single cell, pairing [cable length](#cable-length) to _SD_ will not be useful, since only one cable length value can be computed. In such cases, the Measurements table appends '[Single metric]' to such data

- Each of the 95+ metrics is represented by five statistical properties: minimum, maximum, mean, standard deviation and sum, resulting in a total of at least $$95\times 5$$ features. Note that there is an intrinsic redundancy between these features: E.g., for a given cell, retrieving [Branch length](#branch-length)'s _N_ is effectively the same as retrieving [No. of branches](#no-of-branches)

-  *NaN* values for a reported metric typically reflect undefined operations (e.g., division by zero), or the fact that the reconstruction being parsed is not a valid mathematical tree

- Currently, volume-related metrics do not take into account [path fillings](/plugins/snt/walkthroughs#filling)

[^1]: Volume and surface area calculations assume radii have been assigned to  path nodes, typically through [fitting routines](/plugins/snt/manual#refinefit).<br>
[^2]: [L-measure](http://cng.gmu.edu:8080/Lm/help/index.htm) metrics are described in: {% include citation doi='10.1038/nprot.2008.51' %}<br>


<span id="statistics"></span>
## Group Statistics
SNT assembles comparison reports and simple statistical reports (two-sample t-test/one-way ANOVA) for up to six groups of cells. This is described in [Comparing Reconstructions](/plugins/snt/analysis#comparing-reconstructions). Descriptive statistics of measurements can be obtained by running _Summarize Existing Results_ in the [Measurements dialog](/plugins/snt/analysis#measurements) or by running [ Frequency/Distribution Analysis](https://imagej.net/plugins/snt/analysis#statistics) commands.


## Glossary

###### Mesh
A polygon mesh defines the shape of a three-dimensional polyhedral object. In neuronal anatomy, meshes define neuropil annotations, typically compartments of a reference brain atlas (e.g., the hippocampal formation in mammals, or mushroom bodies in insects)

###### Multi-dimensional image
An image with more than 3 dimensions (3D). Examples include fluorescent images associated with multiple fluorophores (multichannel) and images with a time-dimension (time-lapse videos). A 3D multichannel timelapse has 5 dimensions

###### Neurite
Same as neuronal process. Either an axon or a dendrite

###### Path
Can be defined as a sequence of branches, starting from soma or a branch point until a termination. In manual and assisted (semi-automated) tracing, neuronal arbors are traced using paths, not branches. [Fitting algorithms](/plugins/snt/manual#refinefit) that take into account voxel intensities can be used to refine the center-line coordinates of a path, typically to obtain more accurate curvatures. Fitting procedures can also be used to estimate the volume of the neurite(s) associated with a path

###### (Neuronal) morphometry
Quantification of neuronal morphology

###### Neuropil
Any area in the nervous system. The cellular tissue around neuronal processes

###### Out-of-core
Software with out-of-core capabilities is able to process data that is too large to fit into a computer’s main memory. SNT supports out-of-core tracing via scripting.

###### Reconstruction
See [Tracing](#tracing)

###### ROI
Region of Interest. Define specific parts of an image to be processed in image processing routines

###### Skeleton
A thinned version of a digitize shape (such as a neuronal reconstruction) or of a binary image

###### Tracing
A digital reconstruction of a neuron or neurite. The term predates computational neuroscience and reflects the manual ‘tracing’ on paper performed with [camera lucida](https://en.wikipedia.org/wiki/Camera_lucida) devices by early neuroanatomists

###### Volume rendering
A visualization technique for displaying image volumes (3D images) directly as 3D objects


{% capture text%}
This glossary was assembled from the supplementary note of SNT's publication: {% include citation id='plugins/snt' %}
{% endcapture %}
{% include notice icon="info" content=text %}
