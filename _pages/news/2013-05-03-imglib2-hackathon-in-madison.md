---
title: 2013-05-03 - ImgLib2 Hackathon in Madison
---

From Saturday, April 27, 2013 through Friday, May 3, 2013, LOCI in Madison hosted Tobias Pietzsch and Stephan Preibisch, two [ImgLib2](/libs/imglib2) main developers, for a hackathon. Here is a brief summary of overall accomplishments and topics of discussion:

-   Initial version of SCIFIOCellImg
-   Much discussion and ideas and proofs of concept for better OPS
-   Start on [better imglib2 type hierarchies for metadata](https://github.com/imglib/imglib/commit/e4e26aa05e0f42ff1a90e8c6d67235431471de44), particularly units
-   Decided on histogram unification and [merged to master](https://github.com/imglib/imglib2/commit/79bbc2008eeec6f221c16b6f84782daca2b3f496)
-   Deprecated [ImgLib1](/libs/imglib1) more fully, purging it from the [imglib repository](https://github.com/imglib/imglib2)
    -   See the [deprecation announcement thread](http://thread.gmane.org/gmane.comp.java.imagej.devel/1477) for details
-   Explored dual (read/write) type hierarchy; decided it is too complex

And here is a rough summary of what we worked on:

## Stephan Preibisch

-   Together with Johannes we removed imglib1 from the imglib git repository, it now lives in [legacy-imglib1](https://github.com/fiji/legacy-imglib1). It could not go into SPIM\_Registration directly due to circular dependencies with the 3d-viewer.
-   I implemented wrappers from imglib1 &lt;-&gt; imglib2 that allow efficient, non-copying wrapping of array and cell images between both libraries. To achieve that imglib1 now depends on imglib2. This allows a gradual modification of source code which should ultimately result in the removal of imglib1. Additionally, new implementations in imglib1-based projects can now be implemented in imglib2.
-   We have been working on a new Type hierarchy that reflects the opposed read and write capabilities for integer/floating point based Types. The repository [lives on GitHub](https://github.com/StephanPreibisch/funwithtypes). Until now it does not work though as it seems very hard to express it using Java generics. I hope that is not true ...

## Curtis Rueden

I developed a new component to manage extra metadata about N-dimensional images. In particular, it provides a class hierarchy for attaching per-dimension metadata as extensions of the Axis interface. The AnnotatedSpace interface provides a EuclideanSpace extension that manages the Axis list.

Work was done on a branch called `img-metadata`, culminating in [d3f8e64](https://github.com/imglib/imglib/commit/d3f8e640fec2b91bba761930b46d13170486b9f5). The branch then sat for several months before being [merged to master](https://github.com/imglib/imglib/commit/e4e26aa05e0f42ff1a90e8c6d67235431471de44) on August 12, 2013.

## Johannes Schindelin

There were a couple of things I worked on (apart from the inevitable Fiji side tracks, in this case mostly the SezPoz class loader issue preventing the uploading part of the uploader to work):

-   Tobias showed me his SPIM viewer which is slated to be in Fiji very soon.
-   Tobias and I had a quick look whether we could easily support wrapping IJ1 VirtualStacks in Imgs and decided: no, there is no easy way. At least not as a small path to ImageJFunctions.
-   We had a lot of discussions revolving about Ops and Expressions and performance. My current thinking is that we need to separate Ops from Expressions: to make developing, understanding and maintaining Ops as easy as possible, we have to separate the concerns better.  
    And it is simply easier for everybody if the Ops do one thing, and one thing only, but that one well: evaluate an operation, working on Type variables. Expressions, however, need to know about temporary variables, input and output variables and about being clever not to copy data around too much. But that's the Expressions' job, not the Ops'.
-   Performance is another issue, completely. Over the course of several experiments, I became convinced that we were wrong to rely on the JIT so much: it is okay for simple things, but for ever so slightly complicated things, we need a precompiler that knows what we really want to do. For example, just the mere fact should have taught us something that stand-alone FloatType instances \*must\* refer to their \*single\* float value as a 1-element float array \*just so\* that the JIT does not do an utterly bad job when we access single values as well as pixel values in an array.
-   As a consequence of the findings regarding performance, I came up with a simple proof-of-concept that things could be made fast by using Javassist, a library for bytecode manipulation. We use this library extensively in ImageJ2 and Fiji already for just-in-time patching of, say, ImageJ 1.x. It was a natural choice to turn to Javassist for trying to optimize ImgLib, too. Mind you, the example I made was very simple: it constructed a class working on ArrayImgs of FloatType directly, without even inspecting any code to know what to do, but instead hard-coding the "+" op. But it showed the way to how we could do things in the future: inspect what the, say, Expression is supposed to do and rewrite it in optimized bytecode. The speed improvement was—as I expected—impressive.
-   A lot of discussion went into the question: "where should that optimization take place?". The major problem is—as so often—that you cannot completely rely on good design to get good performance. You have to have a place where the good design can be overridden by something potentially performant. So something has to give. But what? The way out, as far as I am concerned, is to leverage the scijava-common infrastructure and add an OpService. This will be a lot of work, of course, but it was invaluable to have the discussions and hands-on experiments together with the other guys. When you have such a concentration of programming talent in one room, good things happen!

## Barry DeZonia

The discussions I participated in included:

-   a proposal for a new roi interface where rois are Positionable, Localizable, and IterableInterval<BoolType>. The hope is to have rois you can move through space, bind to an existing interval, and then iterate the interval data directly.
-   a proposed set of new histogram classes that can unify the various existing implementations
-   a new approach to data operations in OPS (via new Expressions design and a new OpsService including Javassist accelerated operations)
-   improved support for axes and calibration in Imglib2
-   data type hierarchy experiments

The new roi discussion led to an attempt to see if the new interface design had any gotcha limitations. To that end I spent much of my time exercising the new interface by implementing it for some of the most general PointSet implementations. The test interface was laid out [here as NewPointSet](https://github.com/imglib/imglib/blob/be367d9aad54448efa7e2955b791ac5026e86c34/ops/src/main/java/net/imglib2/ops/sandbox/NewPointSet.java).. I have now created four implementations of this interface that can be found [here](https://github.com/imglib/imglib/tree/be367d9aad/ops/src/main/java/net/imglib2/ops/sandbox). So far I have not run into any show stopper gotchas. The new implementations are sometimes slower than the old implementations but that may be addressable with additional attention.

I also presented work I had done on a set of histogram classes in Imglib2 that could be used to unify the various histogram implementations currently found there. Suggestions were fielded, some changes were made, and the code has been [merged to master](https://github.com/imglib/imglib/commit/79bbc2008eeec6f221c16b6f84782daca2b3f496).

In regards to data type hierarchy experiments I tried to determine the ramifications of supporting BigInteger and BigDecimal data types in Imglib2 for ImageJ2. As part of this work I mocked up a version of the Haskell numeric type hierarchy so that it could inform any future development of data types. It can be found on the types-experiment branch [here](https://github.com/imglib/imglib/blob/faaeaae7f5fe9c66520ebdba6f50efd9cb6d18f9/ops/src/main/java/net/imglib2/ops/sandbox/types/Types.java) and [here](https://github.com/imglib/imglib/blob/faaeaae7f5fe9c66520ebdba6f50efd9cb6d18f9/ops/src/main/java/net/imglib2/ops/sandbox/types/Types2.java).

Now that the hackathon is complete there are additional related tasks to follow up on. They include:

-   Incorporating Mark Hiner's hackathon work (supporting very large image data) into IJ2.
-   Assisting Curtis Rueden with incorporating the imglib2-metadata code into IJ2
-   Implementing the rest of the existing PointSet classes as NewPointSets.
-   Improving the performance improve of the implementations of the NewPointSet interface
-   Leveraging the new histogram classes throughout Imglib2
-   Updating IJ2 (and perhaps OPS' functions) to use new Expressions approach in OPS if it stands up to scrutiny

## Mark Hiner

Over the hackathon and this past week I've been working on extending Tobias's CellImg structures with a SCIFIO backing. The goal here is to get ImageJ2 using SCIFIO for its image IO operations, with the Cell's facilitating caching for huge datasets as needed. This will replace the need for specifying a virtual stack, as the SCIFIO cells will automatically determine optimal tile sizes and load the tiles when requested.

This has required work on all three projects:

-   ImgLib2
    -   made the Cell classes more extensible (adding a Cell interface, refactoring some typing to be more general instead of on concrete implementations)
-   SCIFIO
    -   Converted [ImgSaver](https://github.com/hinerm/bioformats/blob/scifio-cell-image/components/scifio-devel/src/ome/scifio/io/img/ImgSaver.java) and [ImgOpener](https://github.com/hinerm/bioformats/blob/scifio-cell-image/components/scifio-devel/src/ome/scifio/io/img/ImgOpener.java) to use the SCIFIO API.
    -   Extended the imglib2 cell components with [SCIFIO cell classes](https://github.com/hinerm/bioformats/tree/scifio-cell-image/components/scifio-devel/src/ome/scifio/io/img/cell). Currently, these components create 2D cells using the optimal tile height/width, as determined by the current SCIFIO reader. The cells are cached per-dataset using soft references to determine when cells are disposed.
-   ImageJ2
    -   Updated [DefaultIOService](https://github.com/imagej/imagej/blob/scifio-cells/core/io/src/main/java/imagej/io/DefaultIOService.java) and [SaveImg](https://github.com/imagej/imagej/blob/scifio-cells/plugins/commands/src/main/java/imagej/core/commands/io/SaveAsImage.java) to use the updated SCIFIO ImgOpener and ImgSaver. This also means that IJ2 can read/write all the formats currently supported in SCIFIO.

### Future plans

-   ImgSaver uses the SCIFIO API but is still set up to handle planar imgs. It needs to be updated to use SCIFIO cell imgs.
-   The SCIFIO cell cache is currently read-only because when cells are disposed they aren't written to disk, they're just GC'd. So the cache will be updated to allow writing disposed cells to disk.
-   ImgOpener only opens SCIFIO cell imgs right now. We'll add back the ability to open planar imgs if the dataset size is within appropriate bounds.
-   Also, currently many operations in IJ2 (including just opening a dataset.. but also running plugins like Brightness/contrast) require dataset-wide operations (specifically calculating min/max values and autoscaling). This means that while SCIFIO cells can be used to open huge datasets, it's not practical because the autoscaling takes forever. So we need to decide how to limit the range of these operations (e.g. to the current plane, or to the set of known planes).

### Limitations

These changes don't immediately allow for opening large single planes in IJ2—just large numbers of planes—as each whole plane is always loaded in IJ2. However, I think cells will lay the foundation for supporting large single planes in future IJ2 betas.

## Tobias Pietzsch

See the [thread on imagej-devel](/pipermail/imagej-devel/2013-May/001488.html).
