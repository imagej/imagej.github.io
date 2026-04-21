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

## Implementation and Algorithms
A high-level description of SNT's algorithms is available on [GitHub](https://github.com/morphonets/SNT/blob/main/NOTES.md).

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
- [Generating Filtered Images](/plugins/snt/walkthroughs#generating-filtered-images)

Tubular geodesics reference:
{% include citation doi='10.1109/cvpr.2012.6247722' %}


## TRACES File Format

The `.traces` files saved by [SNT](/plugins/snt) are gzip-compressed XML. SNT will also load and save uncompressed XML files, but the compressed form is the default.

The XML DTD is included in the DOCTYPE of each file. The root element is always `<tracings>`, which can contain the following elements: [`imagesize`](#imagesize), [`samplespacing`](#samplespacing), [`path`](#path), and [`fill`](#fill).


### `imagesize`

There must be exactly one `<imagesize>` element, with attributes describing the image dimensions in voxels:

```xml
<imagesize width="520" height="434" depth="117"/>
```

| Attribute | Description |
|-----------|-------------|
| `width`   | Number of voxels along the X axis |
| `height`  | Number of voxels along the Y axis |
| `depth`   | Number of voxels along the Z axis |


### `samplespacing`

There must be exactly one `<samplespacing>` element, with attributes describing the voxel spacing in world coordinates:

```xml
<samplespacing x="0.28838738962693633" y="0.28838738962693633" z="1.2" units="micrometers"/>
```

| Attribute | Description |
|-----------|-------------|
| `x`       | Voxel spacing along X in world-coordinate units |
| `y`       | Voxel spacing along Y in world-coordinate units |
| `z`       | Voxel spacing along Z in world-coordinate units |
| `units`   | The unit of measurement (e.g., `"micrometers"`) |


### `path`

Each `<path>` element represents a traced path and can have the following attributes:

| Attribute | Description |
|-----------|-------------|
| `id` | A non-negative integer ID, unique among all paths in the file |
| `name` | A string giving the name of this path |
| `reallength` | The path length computed by summing Euclidean distances between consecutive points, in the units specified by `samplespacing` |
| `swctype` | Integer flag defining the path type per the [SWC specification](https://swc-specification.readthedocs.io/en/latest/). Defaults to 0 if absent |
| `startson` | ID of the path that the beginning of this path branches off from. When present, either the deprecated `startsindex` or the recommended `startsx`/`startsy`/`startsz` must also be specified |
| `startsx`, `startsy`, `startsz` | World coordinates of the branch point on the path given by `startson`. If any one is specified, all three must be |
| `endson` | ID of the path that this path ends on. When present, either the deprecated `endsindex` or the recommended `endsx`/`endsy`/`endsz` must also be specified |
| `endsx`, `endsy`, `endsz` | World coordinates of the point on the path given by `endson` where this path terminates. If any one is specified, all three must be |
| `fitted` | ID of another path that is a fitted version of this one (with adjusted center-line and radii). Mutually exclusive with `fittedversionof` |
| `fittedversionof` | ID of the unfitted source path that this path was derived from. Mutually exclusive with `fitted` |
| `usefitted` | Required when `fitted` or `fittedversionof` is present. Value is `"true"` or `"false"`. For an unfitted path with a fitted version, `"true"` means the fitted version should be displayed instead. For fitted paths, this should always be `"false"`. *NB: This attribute has confusing semantics and will be replaced in a future version.* |
| ~~`startsindex`~~ | **Deprecated.** 0-based index of the branch point in the path given by `startson` |
| ~~`endsindex`~~ | **Deprecated.** 0-based index of the join point in the path given by `endson` |

#### `point`

Each `<path>` may contain zero or more `<point>` elements representing the coordinates along the path:

| Attribute | Description |
|-----------|-------------|
| `xd`, `yd`, `zd` | Position of the point in world coordinates. These are the values used for length calculations |
| `r` | Radius of the neuron at this point (optional) |
| `tx`, `ty`, `tz` | Tangent vector along the neuron at this point (optional) |
| ~~`x`~~, ~~`y`~~, ~~`z`~~ | **Deprecated.** Position in image coordinates (0-based voxel indices) |


### `fill`

Each `<fill>` element represents a fill around a path. It contains all points found during the search starting from path nodes; the actual fill consists of those points whose distance is below the specified threshold. (The full set is stored so that the search can be resumed if the fill is reloaded.)

| Attribute | Description |
|-----------|-------------|
| `id` | A non-negative integer ID, unique among all fills in the file |
| `frompaths` | Comma-separated (optionally space-separated) IDs of the paths from which this fill started. For example, `frompaths="2, 0"` means nodes on paths 2 and 0 have distance 0 in this fill |
| `metric` | The cost function used during the fill. (The attribute name is a legacy misnomer, kept for backward compatibility.) |
| `threshold` | The distance threshold. Points with a distance below this value are considered part of the fill |

#### `node`

Each `<fill>` may contain `<node>` elements representing individual search nodes:

| Attribute | Description |
|-----------|-------------|
| `id` | A non-negative integer ID, unique within the enclosing fill |
| `x`, `y`, `z` | Position in image coordinates (0-based voxel indices) |
| `previousid` | ID of the previous node on the shortest route from the original paths to this point. Absent for points on the original paths (which have `distance` = 0) |
| `distance` | Minimum distance found for any route from the original paths to this node. The complete route can be reconstructed by following `previousid` links |
| `status` | Either `"open"` or `"closed"`, with their conventional meanings in A\* search |


## Curation File Format

Preset files (`.curation` file extension) used by [Curation Assistant](./curation#data-curation) use a simple key=value format. Each check parameter has a value key and an `.enabled` key. Example:

```properties
# Calibrated from NeuroMorpho.org pyramidal cells ids XX-XX (20 cells, P5/P95)
branchAngle.min=15.2
branchAngle.max=95.5
branchAngle.enabled=true
directionContinuity.minAlignment=12.3
directionContinuity.enabled=true
radiusContinuity.maxRatio=1.8
radiusContinuity.enabled=true
terminalBranchLength.minLength=3.5
terminalBranchLength.enabled=true
somaDistance.maxDist=200.0
somaDistance.enabled=true
tortuosityConsistency.maxDiff=0.2
tortuosityConsistency.enabled=true
constantRadii.enabled=true
pathOverlap.proximity=4.0
pathOverlap.enabled=true
radiusJumps.maxRatio=2.5
radiusJumps.enabled=true
radiusMonotonicity.minRun=8
radiusMonotonicity.enabled=true
```
