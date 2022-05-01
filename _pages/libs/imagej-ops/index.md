---
mediawiki: ImageJ_Ops
title: ImageJ Ops
section: Explore:Libraries
artifact: net.imagej:imagej-ops
icon: /media/icons/imagej2.png
project: /software/imagej2
ref: Rueden, C., Dietz, C., Horn, M., Schindelin, J., Northan, B., Berthold, M. &amp; Eliceiri, K. (2021). ImageJ Ops [Software]. https://imagej.net/Ops.
---

ImageJ Ops is a framework for reusable image processing operations. Ops extends Java's mantra of "write once, run anywhere" to image processing algorithms.

The central goal is to enable programmers to code an image processing algorithm in the Ops framework, which is then usable as-is from any [SciJava](/libs/scijava)-compatible software project, such as [ImageJ2](/software/imagej2), [CellProfiler](/software/cellprofiler), [KNIME](/software/knime), [OMERO](/software/omero) and [Alida](/software/alida).  

## Design goals

Ops has three major design goals:

1.  **Easy to use and extend.** There must be a wealth of easy-to-use image processing operations ("ops"), as well as an easy framework for extending those ops in new directions.
2.  **Powerful and general.** An op should be able to consist of any number of typed input and output parameters, operating on arbitrary data structures, including images of N dimensions stored in a myriad of different ways: as files on disk, programmatically generated in memory, or in remote databases. Using the powerful [ImgLib2](/libs/imglib2) library achieves this ambitious goal.
3.  **Very fast.** Even though ImgLib2 is vastly more general than ImageJ's data model, that generality should not come at the expense of performance. Otherwise, users must pay a time tax to do the same things they could already do in ImageJ. The ImageJ Ops framework needs to provide a means to override *any* general-but-slow op with a faster-but-more-specific alternative, fully transparently to the user.

## Getting started

Start by reading these Jupyter notebooks:

-   [Using ImageJ Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1-Using-ImageJ/2-ImageJ-Ops.ipynb) - to call ops from your scripts.
-   [Extending ImageJ: Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/2-Extending-ImageJ/2-Ops.ipynb) - to write your own ops.

Ops are a special type of ImageJ plugin, so a basic understanding of the [SciJava plugin framework](/develop/plugins) is strongly recommended.

In addition to cloning the [imagej-ops](https://github.com/imagej/imagej-ops) itself, the following components have useful Ops examples:

-   {% include github org='imagej' repo='imagej-tutorials' label='ImageJ-tutorials' %} - examples of ImageJ plugins using Ops
-   {% include github org='imagej' repo='imagej-scripting' label='ImageJ-scripting' %} - provides [templates in the Script Editor](/scripting/templates)

## Tutorials and workshops

-   [Step-by-step guide: Adding new ops](/develop/writing-ops)
-   [ImageJ Tutorial: Introduction to ImageJ Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1-Using-ImageJ/2-ImageJ-Ops.ipynb)
-   [Extending ImageJ: Ops](https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/2-Extending-ImageJ/2-Ops.ipynb)
-   "Scripting in ImageJ - An introduction to ImageJ Ops" (February 2017 NEUBIAS2020) – [slides](/presentations/2017-02-12-imagej-ops-neubias/#/)
-   "ImageJ2 scripts: Parameters + ImageJ Ops" (ImageJ conference 2015) – [slides](/presentations/2015-09-04-imagej2-scripting/), [video 1](https://vimeo.com/140098817), [video 2](https://vimeo.com/140098835)
-   "The ImageJ Ops Framework: Image processing made easy" (January 2015) – [slides](/presentations/2015-01-12-imagej-ops/)
-   "Intro to ImageJ Ops - Usage and Development" (November 2015) – [slides](http://workshops.imagej.net/IntroToOps.pdf)

## FAQ

### Why not implement algorithms as "plain old Java" methods?

The Ops matching framework provides **extensibility.** Ops are plugins, so any developer can override the behavior of a particular op as needed—e.g., for improved performance of a special case. See "Design goals" above.

### Can a C/C++ or MATLAB function be converted to an op?

Yes, but there is no automagic wrapping of native/external functionality in Ops. The [ops-experiments](https://github.com/imagej/ops-experiments) project is an ongoing effort to work out a maven based build system for ops that use native code. The efforts so far have focused on wrapping, cuda, mkl and tensorflow implementations of deconvolution algorithms using [javacpp](https://github.com/bytedeco/javacpp).

### Is there a list of Ops somewhere with brief descriptions of their functionalities?

For an interactive tool to see all available Ops, see the [Op Finder](/plugins/op-finder) documentation.

For the core Ops available, you can go to the {% include javadoc package='?net/imagej/ops' class='package-summary' label='ImageJ Ops' %} javadocs. Any class under the package `net.imagej.ops` is related to Ops.

You can also use the [Script Editor](/scripting/script-editor) in ImageJ and actively search using Ops itself. For example in groovy language:

{% highlight groovy %}
// @OpService ops
print ops.help()

{% endhighlight %}
in groovy will give a list of every Op signature. The `help` op can also provide information about ops or namespaces; e.g., `ops.help("add")` will return info about available `add` ops.

### Are there any Ops for image processing?

Yes, there are. Take a look at the existing ops using the [ Ops Browser](#is-there-a-list-of-ops-somewhere-with-brief-descriptions-of-their-functionalities) or the `net.imagej.ops.*` packages in the [ImageJ javadocs](http://javadoc.imagej.net/ImageJ/).

### What are the Ops that need to be developed in the future?

Ops is under development at the moment, as indicated by the 0.x.x version number. For ideas and discussions of future developments visit the [ImageJ Ops GitHub page](https://github.com/imagej/imagej-ops/) and take a look at the issues and pull requests.

### Why is matching important?

This is a necessary part of any plugin-based infrastructure (see {% include wikipedia title="Inversion of control" %}). The core library (ImageJ Ops) has many built-in operations, but:

1.  cannot possibly cover all possible implementations and
2.  would be impractical if a user had to explicitly call the precise signature for their arguments.

Ops matching is an additional layer that allows plugin selection to be tailored to the arguments of the function being called.

A contrived example: Suppose the default ops implementation of `add(array, array)` iterates over the arrays and combines their values.

Then guava comes up with a way to combine arrays that is 100x faster; we do not want a guava dependency in the base ops library, but we can have an "imagej-ops-guava" component that provides a `GuavaAddArrayOp`.

Then an independent developer comes up with a new way to add the arrays that's 50,000x faster. They turn it into a closed-source, proprietary Op and sell it.

Regardless of this proliferation of implementations, a user just has to write `ops.math().add(array1, array2)` and it will work. If they have the guava implementation on their classpath it will be faster, and if they purchase the proprietary implementation it will be faster still. But their code does not have to be adjusted.

## See also

-   [2014-04-04 - Announcing ImageJ Ops](/news/2014-04-04-announcing-imagej-ops) news post
