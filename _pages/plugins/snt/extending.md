---
title: Extending SNT
nav-links: true
nav-title: Extending
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
tags: snt,tracing,segmentation,neuroanatomy
---

## Using SNT in other projects
Currently, the easiest way to improve the code base is by following the guidance of the [source-code repository](https://github.com/morphonets/SNT#developing). You will likely need an [IDE](/develop/ides) and some _basic_ familiarity with [maven](/develop/maven).

To use SNT as a software library in your own project, simply add SNT as a maven dependency in your  project's pom, e.g.:
```xml
<!-- https://mvnrepository.com/artifact/org.morphonets/SNT -->
<dependency>
    <groupId>org.morphonets</groupId>
    <artifactId>SNT</artifactId>
    <version>4.2.0</version> <!-- only required if pom-scijava is not being used as parent pom -->
</dependency>
```
See e.g., [this forum thread](https://forum.image.sc/t/minimal-autotrace-code-for-snt-java/51654/15) for a concrete example of SNT being used as a software library.

## Tubular Geodesics

The Tubular Geodesics plugins were developed several years ago for [Simple Neurite Tracer](/plugins/snt/faq#what-is-the-difference-between-snt-and-simple-neurite-tracer) but remain functional in modern [SNT](/plugins/snt). They can be installed manually as an SNT add-on. Once installed, they allow you to trace on a filtered-version of your image in which neuronal processes (or other tubular structures) are significantly enhanced using [ITK](/software/itk) segmentation. More details on the following pages:
- [Tubular Geodesics homepage](https://www.epfl.ch/labs/cvlab/software/biomedical/delin-fiji/)
- [Tracing on Filtered Images](/plugins/snt/manual#main-dialog#tracing-on-secondary-image)
- [Secondary Image Screencast](/plugins/snt/screencasts#secondary-images)
- [Generating Filtered Images](/plugins/snt/step-by-step-instructions#generating-filtered-images)

Tubular geodesics reference:
{% include citation doi='10.1109/cvpr.2012.6247722' %}


## TRACES File Format

The .traces files that are saved by [SNT](/plugins/snt) are gzipped compressed XML. SNT will also load/save uncompressed XML files, but by default, they are saved in the compressed form.

The XML DTD is included in the DOCTYPE of each file. The root element is always &lt;tracings&gt;, and this can contain the following elements:

-   [&lt;imagesize&gt;](#.3Cimagesize.3E)
-   [&lt;samplespacing&gt;](#.3Csamplespacing.3E)
-   [&lt;path&gt;](#.3Cpath.3E)
-   [&lt;fill&gt;](#.3Cfill.3E)
-   [&lt;node&gt;](#.3Cnode.3E)

### &lt;imagesize&gt;

There must be exactly one of these elements present, with attributes that describe the size of the image in terms of number of voxels across, up and down, e.g.:

```html
<imagesize width="520" height="434" depth="117"/>
```

### &lt;samplespacing&gt;

There must be exactly one of these elements present, with attributes that describe the spacing of the samples in the image (voxels) in world-coordinates, e.g.:
```html
<samplespacing x="0.28838738962693633" y="0.28838738962693633" z="1.2" units="micrometers"/>
```

### &lt;path&gt;

The `<path>` element can have the following attributes:

- `id`: a non-negative integer ID unique among the `<path>`s in this file
- `startson`: if this is present, it gives the ID of the path which the beginning of this path branches off from. If `startson` is specified, then either the deprecated attribute `startsindex` or the recommended attributes `startsx`, `startsy` `startsz` must be specified as well.
- **\[deprecated\]** `startsindex`: This attribute used to indicate the 0-based index of the point in the other Path where the branch occurred. Please use `startsx`, `startsy` and `startsz` instead.
- `startsx`, `startsy` and `startsz`: These attributes indicate where on the path specified by `startson` the branch occurs. If one of these is attributes is specified, all must be specified.
- `endson`: if this is present, it gives the ID of the path which the branch ends on. If `endson` is specified, then either the deprecated attribute `endsindex` or the recommended attributes `endsx`, `endsy` `endsz` must be specified as well.
- **\[deprecated\]** `endsindex`: This attribute used to indicate the 0-based index of the point in the other Path where this path joins it. Please use `endsx`, `endsy` and `endsz` instead.
- `endsx`, `endsy` and `endsz`: These attributes indicate where on the path specified by `endson` this path ends. If one of these is attributes is specified, all must be specified.
- `name`: A string giving the name of this path
- `reallength`: The length of this path found by summing the Euclidean distance between each consecutive pair of points, in the units specified in &lt;samplespacing&gt;
- `fitted`: If present, this attribute gives the ID of another path which is a version of this path after the centre-line has been adjusted and radii at each point found. If this attribute is present, the `fittedversionof` attribute may not be.
- `fittedversionof`: If present, this attribute gives the ID of another path which was the source version for this one. Typically, the path specified does not have radii defined for each point, although this is not always the case. If this attribute is present, the `fitted` attribute may not be.
- `usefitted`: This attribute must be present if either the `fitted` or `fittedversionof` attributes are. This attribute is either `"true"` or `"false"`. It should only be "true" for paths that have a fitted version, when it implies that the user wants the fitted path to be display in favour of this (the unfitted) one. If "false" and this path has a fitted version, it means that this path should not be displayed. It should always be "false" for paths that are fitted versions of other paths.

  NB: This is confusing and regrettable; in later versions this will be replaced by attributes with simpler semantics.

- `swctype`: The integer flag defining the type of the path as defined in the [latest SWC specification](https://swc-specification.readthedocs.io/en/latest/). If not present, the default value is 0.

The &lt;path&gt; element may contain zero or more &lt;point&gt; elements. These are described below:

### &lt;point&gt;

This represents a point in a path. A point element may have the following attributes:

-   `xd`, `yd`, `zd`: These three attributes give the position of the point in world coordinates. e.g. you can use these coordinates directly to calculate the length of paths.
-   **\[deprecated\]** `x`, `y`, `z`: These attributes represent the position of the point in image coordinates (i.e. indices of voxels in each axis). They are still generated for backwards compatibility, but it's better to use `xd`, `yd` and `zd`.
-   `r`: If present, this attribute gives the radius of the neuron at that point.
-   `tx`, `ty`, `tz`: If present, these attributes give the tangent vector along the neuron at (`xd`, `yd`, `zd`)

### &lt;fill&gt;

The `<fill>` element represents a fill around a path. It contains all the points found in the search starting from points on the path, but those that actually make up the fill are just those below the threshold specified in the attributes. (This is so that the search can be restarted if the fill is reloaded.) The `<fill>` element can have the following attributes:

-   `id`: The ID of the fill, a non-negative integer unique among all the other fill IDs in this file.
-   `frompaths`: A comma ( optional space) separated IDs of the paths from which this fill started. e.g. if this attribute is `frompaths="2, 0"` then there are nodes with distance 0 at each of the points on `<path id="2" ...` and `<path id="0" ...` in this fill.
-   `metric`: The cost function used during the fill. `metric` is a bad name for this attribute, but it was kept for backwards compatibility.
-   `threshold`: The search threshold. All the points with a "distance" less than this path are considered to be part of the fill.

### &lt;node&gt;

-   `id`: Each node in the search has a non-negative integer ID which is unique within the enclosing fill.
-   `x`, `y`, `z`: the position of the node in the image stack in image co-ordinates, i.e. 0-based indices in voxels.
-   `previousid`: If present, this ID gives you previous node on the shortest route from the original paths to this point. It is not present for the points on the original paths, which also have a `distance` attribute equal to 0.
-   `distance`: This is the minimum "distance" so far found for any route moving from any point on the original paths to this node. (The complete route can be reconstructed by following `previousid`s.)
-   `status`: this attribute can either have the value `open` or `closed`, which have their conventional meanings in A\* search.
