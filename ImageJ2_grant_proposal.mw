The following is the original text of the [[ImageJ2|ImageJDev]] grant proposal circa mid-2009.
{{Warning
| message = Please note that [[ImageJ2]]'s project directions evolved substantially as it developed, so the text below is dated, but in many ways, this document continues to represent the project's conceptual core.
}}

== Summary ==

'''Purpose: Refine ImageJ’s core design to accommodate a broader range of needs in the scientific community.'''

Imaging is one of the most powerful tools available to the modern biologist and recent advances in quantitative microscopy and image analysis have greatly accelerated our understanding of many complex and dynamic processes. The NIH’s open-source [[ImageJ]] software has been enormously useful in many of these projects since its release in 1997. Any successful software project, after a period of sustained growth and the addition of functionality outside the original intended scope, will benefit from a subsequent period of scrutiny and refactoring, and ImageJ is no exception. Such review helps the program to remain accessible to newcomers, powerful enough for experts, and relevant to an evolving community. Furthermore, the pressing unmet needs of the existing ImageJ community, as well as of researchers who are hindered from building on ImageJ due to its limitations, lead us to propose the following work to improve ImageJ’s functionality and interoperability:

=== Aim I – Improve the ImageJ core architecture ===

Improvements in core architecture are required for the development and stability of the ImageJ project, its interoperability with other software, and its ability to support new features and applications:

# '''Separate the data model from the user interface''' – The current ImageJ is tightly coupled to its GUI, hindering its use in many applications. We will decouple the ImageJ data model from its display. This will enable alternate views of data, features like dynamic charts and real-time linked displays, and most importantly, the ability to use ImageJ in headless mode on a computing cluster or as a library of independent functions.
# '''Introduce an extensions framework for algorithms''' – To enable more widespread interoperability between independently developed algorithms and to enable the recording and writing of modular macros in multiple scripting languages, we will introduce a framework with clear declaration of inputs and outputs—including data types beyond images such as segmentation results, numerical statistics, and other metadata—modeled after successful analysis workflow software.
# '''Broaden the image data model''' – We will extend ImageJ to handle important image types, including large numbers of image planes, dimensionality beyond 5D, high-resolution image planes, and images stored in databases. The data model will also leverage image metadata, which is required as imaging experiments become more complex.

=== Aim II – Expand functionality by interfacing ImageJ with existing open-source programs ===

To ensure that development proceeds in a practical direction that maximizes interoperability, and to improve ImageJ’s functionality, we will interface the improved ImageJ framework with two existing open source biology applications, [http://www.loci.wisc.edu/visbio/ VisBio] and [http://www.cellprofiler.org/ CellProfiler]. We will rework VisBio as a suite of ImageJ extensions, taking advantage of the improved data model to provide robust 3D visualization and analysis of massive multidimensional image. We will link CellProfiler with ImageJ to allow users to execute analysis workflows between the two, such that algorithms can be shared.

=== Aim III – Grow community-driven development while maintaining compatibility ===

ImageJ has a strong, established user base, with thousands of plugins and macros for performing a wide variety of tasks; the proposed changes to ImageJ will be done in a manner that preserves the functionality of existing code. To foster participation, understanding and enthusiasm from a growing community, we propose the adoption of several “best practices” in line with other modern, successful open source projects, which when taken together will build on ImageJ's solid foundation of community-driven development. This will include establishing a public source code repository with a standard location for extensions, deploying unit tests and a continuous integration system, increasing usage of modern language features, and developing an integrated online help system.

=== Conclusion ===

Together, these improvements will enhance the functionality and interoperability of ImageJ, solidifying and expanding the efforts of the community of researchers who rely on it for important research across all areas of biomedicine.

== Approach ==

=== Aim I – Improve the ImageJ core architecture ===

Over the years, ImageJ has grown organically as requested features have been added, with many contributions from outside developers. The result has been a program with a wide range of functionality capable of solving a diverse collection of image processing and analysis problems, particularly in the life sciences. However, this pattern of growth, though carefully controlled by ImageJ's main developer {{Person|Rasband}}, is no substitute for a holistically engineered package built from the ground up with a modular design. Any successful software project, after a period of sustained growth and the addition of functionality outside the scope of the program's original intent, will benefit from a subsequent period of scrutiny and refactoring, and ImageJ is no exception. Such review helps the program to remain accessible to newcomers, powerful enough for experts, and relevant to an evolving community.

Based on the pressing unmet needs of the existing ImageJ community and the needs of several open source projects that have been hindered from building on ImageJ due to its limitations, we have divided this aim into three sub-aims that will maximally benefit and expand the ImageJ community:

=== Aim IA – Separate the data model from the user interface ===

Many developers want to use ImageJ as a library, in headless mode for batch processing without a GUI, or integrated with an external user interface (Swing, SWT, Java3D, etc.). The current ImageJ is tightly coupled to Java’s Abstract Windowing Toolkit (AWT), hindering its use in these contexts.

To overcome this problem, we will employ a popular and successful design pattern known as Model-View-Controller (MVC) to decouple the ImageJ data model from its display. This paradigm creates a two-tiered program with a “glue layer” for connecting the two. The lower layer is the data or “Model,” which in the case of ImageJ is the images themselves. The current implementation of ImageJ implicitly associates exactly one window onscreen with each open image; conversely, with an MVC design, the image data would stand alone without any graphical user interface (GUI) necessarily being needed at all. Such a design is useful, e.g., for external applications to make use of ImageJ as a library, reading in images, processing them, and outputting results, all without any needed interaction from the user. The upper layer is the GUI or “View,” which is connected to the Model via the glue layer, or “Controller.” Such a design allows for any number of linked windows to display the same underlying data, perhaps with different viewing parameters such as color table or image zoom.

We will also use Java's event-driven approach to provide a means for other software to “listen in” when ImageJ's Model changes, enabling features like dynamic charts and real-time linked displays. With this design, changes to the underlying Model will automatically propagate to all active linked Views, and user interaction with a View (such as cropping an image) will be capable of altering the Model.

Refactoring ImageJ to use an MVC design is a significant effort, but fortunately, preliminary work has already been done in this direction: Grant Harris has written a whitepaper ([[File:ImageJX_Mar09.pdf]]) describing his efforts thus far to deploy an interface-driven architecture for extensible, modular GUI support. With further development, we will transform ImageJ into a flexible library usable by a wide variety of scientific image software.

=== Aim IB – Introduce an extensions framework for algorithms ===

ImageJ has a Plugins infrastructure for extending ImageJ's functionality with user-created analysis algorithms and tasks. Though convenient and widely used, this mechanism only provides support for single-image-in, single-image-out processing, with more complex analysis results such as graphs being handled on an ad hoc basis. Such an approach, while flexible, limits interoperability between analysis algorithms. A more general extensions framework would enable more widespread interoperability between independently developed algorithms. Along these lines, we will define a means for extensions to clearly declare their inputs and outputs—including data types beyond images such as segmentation results, numerical statistics, and other metadata—modeled after CellProfiler's system for analysis workflows. With this more “strongly typed” framework, it will become possible to define exactly which output data from which analysis modules should be fed into which input parameters of other analysis modules, to define more complex analysis processes capable of working with various sorts of data including not only image planes but also segmentation results, per-image and per-experiment statistics and other numerical data.

Another useful feature of ImageJ is built-in support for small scripts (called “macros” in ImageJ terms) that execute a series of commands and plugins to create a mini-workflow for analysis. With macros it is possible to chain together analysis routines, batch process many images at once, or a combination of both. However, the ImageJ macro language, though similar in some ways to scripting languages like Javascript, has a unique syntax that is generally less powerful than independently developed scripting languages such as Jython, Beanshell and Clojure. Rather than continually trying to “catch up” to these languages in terms of expressiveness and functionality, we will leverage an MVC design similar to Aim IA to enable support for multiple scripting languages in an extensible, modular way. With this approach, users can write ImageJ scripts in their language of choice, and even generate such scripts from ImageJ user interface actions using ImageJ’s macro recorder feature.

=== Aim IC – Broaden the image data model ===

Like many image analysis programs, ImageJ adeptly handles common, non-scientific, two-dimensional image formats (such as JPEG, PNG and TIFF). Unlike many other image programs, though, ImageJ has increasingly made an effort to support multidimensional scientific images beyond 2D, including stacks of images representing three spatial dimensions (3D), time as an additional dimension, and multichannel images where colors provide additional dimensions. Images of 5 dimensions or more have become increasingly common in various disciplines of science; for example, fluorescence spectral lifetime imaging[19, 21] yields dimensions beyond 5D, which ImageJ does not currently support.

We will extend ImageJ's capabilities to handle image data of arbitrary dimensionality, with any number of channels per pixel, using a tensor representation of dimensional axis lengths. An important aspect of handling stacks of images that represent different dimensions is that proper handling and support for an image's accompanying metadata becomes critical. ImageJ has a minimal metadata model, with support for specifying the physical width, height and image plane slice distance, and little else. The great challenge with metadata is that each discipline has different information vital to its particular kinds of analysis, so there is no one “right way” to represent it all. However, as each discipline develops data models to describe its metadata (such as the Open Microscopy Environment has done for light microscopy acquisition metadata[15]), ImageJ should provide the flexibility to attach metadata expressed using these data models to images, such that analysis modules cognizant of a particular flavor of metadata can utilize and manipulate it if present. In this fashion, analysis workflows can share information whenever feasible without trying to force data into an overly constrictive representation.

Another concern is handling the growing size of the image data, given that it often exceeds the available computer memory. ImageJ provides a “virtual stack” feature that pulls image planes from disk one at a time on demand, to avoid storing large quantities of data on disk at once, but this feature is only the edge of what is possible with such techniques. With intelligent caching, much better performance can be achieved without requiring unreasonable amounts of memory. Further, since ImageJ is capable of operating the same with data in memory and data on disk, why not also data over the network, such as in a remote database, or on a website? We will use an interface-driven architecture to abstract the source of image data, with images on disk, from a URL, stored in a database, etc., all be equally accessible and functional given sufficient bandwidth.

Modern datasets have grown not just in number of image planes, but also the spatial size of each individual plane. Some disciplines such as digital pathology now produce huge image planes of entire glass slides in excess of 400 megapixels (20,000 by 20,000 pixels), which very few image software applications are capable of handling directly. Often, one such image plane already exceeds the available computer memory, meaning a more clever approach is necessary to effectively work with the data. We propose the addition of a multi-resolution tiling mechanism to ImageJ, similar to map web sites such as MapQuest and Google Maps, enabling analysis of one block of tiles at a time, retrieving image tiles from the data source as needed, similar to the caching approach for planes outlined above.

ImageJ is also missing some image types common in scientific image processing. Specifically, we will add support for signed 8-bit integer, unsigned 32-bit integer, and double precision floating point images.

=== Aim II – Expand functionality by interfacing ImageJ with existing open-source programs ===

Both to advance the feature set of ImageJ, and to demonstrate that the underlying software engineering improvements in Aim I enable interoperability and new functionality, we propose to interface two existing toolkits with ImageJ.

First, we will rework VisBio as a suite of ImageJ extensions, taking advantage of the improved data model to provide robust 3D visualization and analysis of massive multidimensional biological image data. Second, we will link CellProfiler with ImageJ to allow users to execute analysis workflows between the two, such that CellProfiler modules can take advantage of ImageJ extensions and vice versa. These two applications will demonstrate two very different but equally valid ways of harnessing the ImageJ codebase within scientific image software, and both will serve as models for other software seeking to accomplish similar goals.

=== Aim IIA – Continued development of VisBio within the ImageJ framework ===

While ImageJ is extremely useful for many tasks, its current incarnation has a few limitations with respect to life sciences image processing. Specifically, it lacks robust mechanisms for the following:

# Handle life sciences data of any size, dimensionality and file format.
# Visualize data in 3D using techniques such as arbitrary slicing, volume rendering and orthonormal stack projections.
# Enable analysis workflows by linking together sequences of operations.

To meet these requirements, we created [http://www.loci.wisc.edu/software/visbio VisBio], a biological visualization tool designed for easy visualization and analysis of multidimensional data[10]. Our main focus has been on a general infrastructure for working with massive N-dimensional light microscopy data. Most biological software packages available are limited to at most 5D (space, time and channel), or are specific to a particular modality such as spectral-lifetime. We wanted VisBio to transcend such limitations, while also providing targeted analysis features for specific modalities.

To accomplish the three goals above, VisBio needed a flexible multidimensional data engine, with a separation between the data itself and the graphical user interface. The [http://www.ssec.wisc.edu%7Ebillh/visad.html VisAD] library for scientific visualization and analysis provided the basis for such an engine with robust 3D visualization capabilities and a strict separation between data and display. Thus, item #2 above was fairly straightforward, and most of our effort went into the other two requirements: support for massive multidimensional image data regardless of file format, with a generalized analysis workflow system.

Unsurprisingly, in the course of developing the software, we found ourselves implementing readers for many file formats. We soon realized such file format support would be of great use to the community as a standalone library, and so we split it into its own package, Bio-Formats, and created a suite of [http://www.loci.wisc.edu/software/bio-formats Bio-Formats] plugins for ImageJ.

Meanwhile, a growing movement in the ImageJ community began to express interest in overcoming many of the same limitations that led to our work on VisBio. In recent years there have been several substantial improvements to ImageJ as a framework, but they do not go far enough to address the community’s needs:

* ImageJ now supports data of up to five dimensions—in 3-space, across time, and with multiple channels—but has no abstraction for higher dimensionality. For example, lifetime, spectral and polarization components are becoming increasingly common in light microscopy.
* ImageJ now has the concept of a “virtual stack,” with data pulled on demand from disk or another source, allowing processing of datasets larger than available memory—but it does not intelligently cache portions of the data to improve performance.
* Several limited 3D viewer plugins now exist, but there is still no core infrastructure decoupling image data from display. Many applications require the use of multiple linked views, with user actions in one view interactively updating other views.

VisBio was our initial attempt at addressing these problems, but ultimately we have solved several of them at the Bio-Formats level instead, because doing so was convenient. For example, because many data formats contain multidimensional data beyond 5D, Bio-Formats includes a representation for Ndimensional image data that was originally part of the VisBio data engine. Bio-Formats also provides a generalized caching mechanism, designed to intelligently manage subsets of image planes within memory. However even though we have begun to address some of these needs in VisBio and some of them in Bio-Formats, a tighter coupling between these code bases and ImageJ is needed.

Going forward, we anticipate a tighter coupling between ImageJ and Bio-Formats, to incorporate these features and others into the ImageJ framework (aim 1c). In addition to those features already mentioned, the Bio-Formats metadata model will be useful for ImageJ to flesh out its metadata support.  Creating a tighter coupling with VisBio/Bio-Formats would also provide ImageJ with the following new capabilities (items #2 and #3 above):

3D visualization. Once the modular display architecture is in place (aim 1a), we will adapt our VisBio visualization approaches into the ImageJ framework. We will provide a suite of VisBio 3D display modules for visualizing stacks of images, providing the same flexible display options currently available in VisBio, but integrated with the ImageJ framework. Some examples include: semi-transparent volume rendering; interactive arbitrary slicing; image stack views in either of perspective or orthonormal modes; interactive color table manipulation; overlay of multiple datasets in a single window; and VisBio-driven graphical overlays including shapes and text. With this integration, it will be possible to directly perform ImageJ operations on data being visualized in a VisBio window, or visualize the results of an ImageJ plugin in a VisBio-enabled context.

Analysis workflow system. The introduction of a more strongly typed extensions framework (technical aim 1b), including modular support for scripting languages within the ImageJ framework, will enable a powerful analysis workflow infrastructure. ImageJ scripts will be a way to record and repeat the steps performed on a given dataset. The only major remaining challenge in this regard will be interoperability with other analysis workflow systems. Where possible, we will adapt or integrate with other projects that provide related features, including the [http://www.openmicroscopy.org/info/omero OMERO platform], [http://jexperiment.wikidot.com/ Je’Xperiment] and [http://www.bioimage.ucsb.edu/ Bisque]. Although this effort may not retain the “VisBio” moniker, such integration has historically been a long-term VisBio design goal.

To the extent feasible, we will derive a common language for these tools to use in describing their analyses, which will facilitate repeatability in execution across multiple datasets. This common language will be an extension of the OME-XML schema for microscopy acquisition metadata, and will describe the steps taken during the workflow in a human- and machine-readable way. In areas where the various tools diverge in paradigm, we will ensure it is possible to embed analysis results from one system within another, so that no information about the workflow is lost. For example, in the OMERO platform, it is possible to attach binary files—such as an ImageJ script, spreadsheet or PDF file—to an experiment, and store the resultant data as a derivative image. In this way, analyses performed across multiple systems can retain their provenance.

=== Aim IIB – Linking Cell Profiler with ImageJ ===

CellProfiler is an example of a widely used biological image analysis program that was developed independently of ImageJ due to limitations in ImageJ’s infrastructure (see Carpenter letter of support).  The technical goals outlined in Aim 1 are instrumental to enable full interoperability of ImageJ with image analysis programs like CellProfiler. Both the CellProfiler and ImageJ communities would benefit from a well-built interface between the two software packages. Demand for this is strong and would enable sharing of algorithms and methodologies that have thus far been independently, and sometimes redundantly, developed.

For the purposes of developing an improved ImageJ architecture, CellProfiler is an excellent test case for interfacing because its typical usage on a computing cluster requires separation of the data model from the user interface (Aim 1a), its robust data model for analysis workflows will greatly inform the design of ImageJ's extensions mechanism (Aim 1b), and its typical use cases require an expanded data model, e.g., handling multi-dimensional images (Aim 1c). In the sections below, we briefly describe relevant aspects of CellProfiler’s architecture and use cases and how the enhancements to ImageJ will be beneficial.

==== Overview of CellProfiler ====

[http://www.cellprofiler.org CellProfiler] is a versatile, open-source tool to quantify a variety of phenotypes in biological images, particularly in high-throughput experiments[11-14]. Since its release three years ago, CellProfiler has become well-established and widely used, having been downloaded more than 8,000 times by users in over 60 countries and cited in nearly 100 papers. Using CellProfiler’s point-and-click interface, researchers build a customized chain of image analysis modules to identify and measure biological objects in images. The software evolved in an intensely collaborative and interdisciplinary research environment with dozens of diverse applications. CellProfiler has been successfully applied to measure cells, colonies, and whole organisms in a wide range of assays (e.g., cell counting, measuring staining intensities, and scoring complex phenotypes with machine learning) and experimental scales (a few images, or hundreds of thousands).

==== Overview of the CellProfiler data model ====

Designed primarily for automated analysis of experiments with large numbers of images, CellProfiler sequentially executes a pipeline of modules (each module customized with particular settings) on an image set. This processing generates derived images, segmentation results (objects) and measurements. The data model consists of two parts: a pipeline of modules and a workspace of images, segmentation results and measurements. Typically, images are processed using a computing cluster and data is uploaded to a database, although smaller-scale experiments can be processed locally and data analyzed in a spreadsheet.

A pipeline is a sequence of modules, each of which carries out an image or data operation. Each module has a collection of settings which constitute its internal state. Settings represent configuration values for a module; each setting can be serialized to a text value, the settings for a module can be serialized to a sequence of text values and a pipeline can be serialized to a sequence of sequences of text values.

'''Pipelines.''' A pipeline is a module container. It has mechanisms for loading and storing the modules it contains and for running itself on an image set. Images can be grouped into image sets by being present within the same image file (e.g., three wavelengths/channels present within a color image file), by being present in certain locations (e.g., subfolders), or by metadata tags present in the image file name or a separate data file.

'''Modules.''' Each module represents some image or data operation. A module’s state is completely represented by its settings. The code of a module has methods for finding the module’s settings, executing the image or data operation (e.g., image processing), supporting old versions of the software for backwards compatibility, and enumerating the measurements that the module generates.  CellProfiler’s modules generate three classes of measurements: experiment-wide measurements (''Experiment measurements''), measurements synthesized per image set (''Image measurements'') and measurements synthesized per object (''Object measurements'').

'''Settings.''' A setting holds a configuration value on behalf of a module. These settings are numeric values, value ranges (for instance minima and maxima for an algorithm) and text values (for instance, the directory for some file access step). There are two special classes of settings: providers and subscribers. These are text values that supply names, but they also have semantic significance.  Providers supply names for module outputs which are stored in the workspace. Subscribers supply names for module inputs which are taken from the workspace. Providers supply intermediate results for subsequent modules. Subscribers choose their values from among those made available by prior modules’ providers. At runtime, a module stores image and segmentation data in the workspace using values supplied by provider settings. A module retrieves image and segmentation data using values supplied by subscriber settings. Settings subscribers use the pipeline to find possible setting providers earlier in the pipeline.

In the context of CellProfiler’s UI, settings are the model in the model-view-controller (MVC) interface.  The view creates graphic elements for module configuration based on the class of the setting and the controller manipulates the setting based on the class of the setting and events generated by the view.  Settings are agnostic with regard to UI, which makes it possible to render them within frameworks other than CellProfiler. A subset of settings are ''visible settings''. Whereas settings represent the module’s state and can be used to serialize and deserialize the module’s state, visible settings are only those that should be displayed to the user. These can be context-dependent; in some cases a setting is only relevant (and thus only visible) if another setting has a particular value.

'''Workspaces.''' The CellProfiler workspace is a blackboard that holds the initial images of an image set and the intermediate images, objects and measurements produced by modules. Modules read inputs (typically images or objects) from the workspace and write results onto it (typically processed images, objects, and measurements).

==== Benefits of Aim 1's ImageJ design enhancements to interfacing with CellProfiler ====

'''Separation of data model from user interface (Aim 1a).''' CellProfiler has a data model that can be decoupled from display and can operate under the control of different UI frameworks. Once ImageJ has been updated to use an MVC design pattern, it will be feasible to display complex analysis results from CellProfiler in native ImageJ windows. This decoupling will also facilitate using ImageJ on a computing cluster, without a GUI—one of the primary hindrances of the use of ImageJ for the high-throughput user community served by CellProfiler.

'''Introducing an extensions framework for algorithms (Aim 1b).''' As described above, CellProfiler has a robust design for image analysis workflows, which could greatly inform similar functionality within ImageJ. With a similar framework in ImageJ, users will be able to mix and match image processing functions to create a workflow. The value of this cannot be underestimated: the testing of various algorithms against each other is critical to successful image analysis and the lack of a modular workflow accessible by non-programmers has been a key limitation in the current ImageJ. Introducing this framework has other advantages: (1) enabling CellProfiler and ImageJ to be interfaced quite uniformly, allowing various kinds of data (images, segmentation results and measurements) to be passed back and forth freely between the two programs (a goal of Aim 2), and (2) enhancing the types of operations feasible in ImageJ, by having its functions readily receive multiple complex inputs (multiple images, masks, text or numerical data) as is currently the case with CellProfiler’s modules and is particularly necessary for the high-throughput user community served by CellProfiler.

'''Broadening the image data model (Aim 1c).''' CellProfiler would benefit from several of the proposed image data model improvements. The ability to abstract the source of data would allow CellProfiler to process data from any new data source supported by ImageJ, such as from a URL or image database.  It would also expand the file formats readable by CellProfiler, via adoption of the Bio-Formats OME metadata model would enable CellProfiler to locate important metadata regardless of file format. Most CellProfiler users require a data model that effectively represents multi-dimensional images, such as those containing multiple colors, timepoints, and three-dimensional z-series. As well, CellProfiler has been optimized to work with images on the order of one megapixel (1000 x 1000) or less; a tiling mechanism within ImageJ would let CellProfiler operate efficiently on much larger images.

==== CellProfiler integration with ImageJ ====

The enhancements to ImageJ described in Aim 1 will enable us, therefore, to readily create a CellProfiler/ImageJ interoperability layer for bidirectional communication between the two packages.  There is strong demand for this interoperability in both user communities, as each package has powerful algorithms not available in the other. The interoperability layer will maintain a CellProfiler pipeline structure to configure settings, as well as a workspace on behalf of CellProfiler modules, including loading of the initial images for an image set into the workspace. It will also translate CellProfiler segmentation results including associated metadata into first-class ImageJ objects in order to make them available to other ImageJ extension modules according to the extension framework's typing mechanism. To facilitate this integration, we will use CellProfiler's provider/subscriber functionality to determine the image and segmentation results produced by a module, making the information available via the ImageJ extensions API. With this work completed, CellProfiler could appear as a single monolithic extension, with configuration involving module selection and configuration. Alternatively, modules written by users within the CellProfiler framework can be used as individual ImageJ extensions, and vice versa.

Examples of important aspects of this interfacing include masking and overlays. Masking is a useful, pragmatic technique when dealing with images containing unwanted objects such as dust, well edges, and a mixture of cell types, only some of which are of interest. We will ensure that both images and their associated masks can be freely communicated as input and output parameters between the CellProfiler and ImageJ modules. Segmentation and measurement overlays must also be properly interfaced between ImageJ and CellProfiler modules. Each object’s location in each image is information produced by CellProfiler segmentation modules. This information can be used in ImageJ to label or outline objects within images, to select objects within images, and to display calculated values on top of objects.

=== Aim III – Grow community-driven development while maintaining compatibility ===

ImageJ has a strong, established user base, with thousands of plugins and macros designed to perform a wide variety of tasks; the proposed changes to ImageJ will be done in a manner that preserves the functionality of existing code. To foster participation, understanding and enthusiasm from a growing community, we propose the adoption of several “best practices” in line with other modern, successful open-source projects, which when taken together will build on ImageJ's solid foundation of communitydriven development.

'''Public source code repository.''' We will be to establish an official repository for the ImageJ source code, from which all developers (internal and community wide) will work. Such a repository serves many purposes: preventing developers from overwriting each other's work, easing regular code backups, and simplifying contribution of code from the community, among other advantages.

'''Unit tests and continuous integration.''' In Aim 1, we have proposed major changes to the ImageJ codebase. It is crucial that we make these changes gradually, testing after each one to ensure that existing functionality continues to work. The most realistic way to do so is to establish a comprehensive suite of unit tests, which are small automated tests that verify each atomic piece of functionality with the system. While the creation of such a suite is a significant effort, it is a long term investment that ensures the program continues to work as advertised for many years to come. Furthermore, by linking the test suite with a continuous build integration system, the tests can be automatically run whenever code is committed to the official repository, notifying the developers whenever a test fails.

'''Modern language features.''' Version 5 of the Java language has become nearly ubiquitous, but like many legacy Java applications, ImageJ must remain compatible with the small minority of systems (e.g., Mac OS X 10.3) running older versions of Java. However, with tools like [http://retroweaver.sourceforge.net/ Retroweaver], it is possible to move forward while continuing to preserve support for these older systems. Thus, we can begin to migrate the codebase toward use of Java 5, which will increase code readability and type safety, while reducing certain kinds of program errors.

'''Central location for extensions.''' Similar to a central code repository for the core ImageJ software, the community needs a central place to go to find plugins, macros and other third party extensions. The ImageJ web site has a large list of plugins, but it is manually maintained by one person rather than a community effort. An alternate location, the ImageJ Documentation Wiki, was brought online in recent years, allowing anyone to submit a plugin and submit online documentation and links using the wiki community model (similar to how Wikipedia is run). We propose adopting this wiki approach on the main ImageJ web site, to ease the maintenance burden on the plugins list, while allowing the community to keep the site up to date with the latest work.

To facilitate widespread adoption of this resource, we will implement an “extension manager” feature within ImageJ, allowing the user to search, browse and download available extensions in various categories, similar to the package manager feature of many Linux distributions. This ability will eliminate the need for users to manually download JAR files and place them in the ImageJ plugins folder, and will also provide the ability to automatically check for updates to installed extensions.

'''Integrated help system.''' Lastly, another built-in system we will add to ImageJ is an online help feature for documenting program features and extensions. Each extension will be able to provide rich text explaining its use, and all will be searchable from within the main ImageJ interface. As we develop the extensions framework itself (Aim 1b), we will look for ways to provide a more granular help mechanism, such that individual input and output parameters can be documented as well.

== Timeline and Milestones ==

''Year 1, Quarter 1:''
<br />(Aim 3) Establish ImageJ source code repository.
<br />(Aim 3) Introduce unit tests to minimize regression bugs and ensure compatibility going forward.

''Year 1, Quarter 2:''
<br />(Aim 1a) Begin decoupling data model from user interface using Grant Harris's work as a starting point.
<br />(Aim 3) Continue developing unit tests, maximizing coverage of existing ImageJ features.

''Year 1, Quarter 3:''
<br />(Aim 1a) Continue work on Model-View-Controller (MVC) refactoring, using a new namespace to avoid conflicts with legacy code.
<br />(Aim 1c) Refactor data model to allow for any data source, not just files and URLs.
<br />(Aim 1c) Integrate support for tiled images into the data model.
<br />(Aim 3) Migrate code to use Java 5 language features where appropriate.

''Year 1, Quarter 4:''
<br />(Aim 1a) Enrich the event model, to enable features like dynamic charts and real-time linked displays.
<br />(Aim 1b) Develop generalized infrastructure for extensions, with support for common types of input and output data.
<br />(Aim 1c) Generalize 5D image model to N dimensions using a tensor representation.
<br />(Aim 1c) Implement support for additional commonly used pixel depths (signed 8-bit integer, double precision floating point, etc.).
<br />(Aim 3) Reduce legacy code by delegating to the new namespace where possible.

''Year 2, Quarter 1:''
<br />(Aim 1a) Implement additional display modules for Swing and Java3D.
<br />(Aim 1b) Migrate existing core analysis plugins to new extensions infrastructure.
<br />(Aim 1c) Extend support for &quot;virtual stacks&quot; to allow caching a subset of image data according to a user-guided caching strategy.
<br />(Aim 2) Begin updating VisBio visualization and analysis package to take advantage of the improved ImageJ extensions infrastructure.

''Year 2, Quarter 2:''
<br />(Aim 1b) Modularize scripting support to enable recording commands in any supported scripting language.
<br />(Aim 2) Continue work on new VisBio suite of ImageJ extensions: support for multi-view spectral lifetime data mining.
<br />(Aim 3) Implement an easy-to-use, standardized extension documentation mechanism.

''Year 2, Quarter 3:''
<br />(Aim 1c) Extend ImageJ's metadata model to store commonly used metadata fields in a format-independent way.
<br />(Aim 2) Integrate improved ImageJ framework with CellProfiler cell image analysis software.
<br />(Aim 3) Establish a unified extensions repository.

''Year 2, Quarter 4:''
<br />(Aim 2) Investigate use of new extensions mechanism within OMERO and FARSIGHT analysis workflow frameworks.
<br />(Aim 3) Create a graphical extension manager for downloading, installing, configuring and removing extensions.

== Measurable Outcomes ==

At the end of the of the two year development period we expect the following outcomes and deliverables:

# A reengineered ImageJ that has the functionality the developer needs and yet is transparent to the long time ImageJ user.
# An ImageJ development site that uses professional practices for code development and engineering.
# A CellProfiler and VisBio application that is fully interfaced with ImageJ and in regular use.

== Additional Deliverables ==

Examples of new applications facilitated by this grant’s technical aims:

# Spectral lifetime analysis using ImageJ (aims 1a &amp; 1c): The MVC architecture will enable real-time linked views depicting multiple data representations, to facilitate data mining. For example, when combined with multidimensional tensor representation and a 3D display module such as Java3D, we could probe spectral lifetime data.
# Tiled image browser, similar to brainmaps.org or Google maps (aim 1c): The tiling engine for high resolution image planes, combined with data source abstraction, will make this straightforward.
# Real-time remote browsing of images, such as an OMERO database (aim 1c): Data source abstraction is critical for this type of feature.
# Easy, flexible analysis workflow engine (aim 1b): Extensions with compatible inputs and outputs can be linked together.

== References ==

# Collins, T.J., ''ImageJ for microscopy''. Biotechniques, 2007. '''43'''(1 Suppl): p. 25-30.
# Pool, M., et al., ''NeuriteTracer: a novel ImageJ plugin for automated quantification of neurite outgrowth''. J Neurosci Methods, 2008. '''168'''(1): p. 134-9.
# Dello, S.A., et al., ''Liver volumetry plug and play: do it yourself with ImageJ''. World J Surg, 2007. '''31'''(11): p. 2215-21.
# Picht, E., et al., ''SparkMaster: automated calcium spark analysis with ImageJ''. Am J Physiol Cell Physiol, 2007. '''293'''(3): p. C1073-81.
# Irving, B.A., et al., ''NIH ImageJ and Slice-O-Matic computed tomography imaging software to quantify soft tissue''. Obesity (Silver Spring), 2007. '''15'''(2): p. 370-6.
# Cathelin, R., F. Lopez, and C. Klopp, ''AGScan: a pluggable microarray image quantification software based on the ImageJ library''. Bioinformatics, 2007. '''23'''(2): p. 247-8.
# Feige, J.N., et al., ''PixFRET, an ImageJ plug-in for FRET calculation that can accommodate variations in spectral bleed-throughs''. Microsc Res Tech, 2005. '''68'''(1): p. 51-8.
# Barboriak, D.P., et al., ''Creation of DICOM-aware applications using ImageJ''. J Digit Imaging, 2005. '''18'''(2): p. 91-9.
# Girish, V. and A. Vijayalakshmi, ''Affordable image analysis using NIH Image/ImageJ''. Indian J Cancer, 2004. '''41'''(1): p. 47.
# Rueden, C., K.W. Eliceiri, and J.G. White, ''VisBio: a computational tool for visualization of multidimensional biological image data''. Traffic, 2004. '''5'''(6): p. 411-7.
# Jones, T.R., et al., ''CellProfiler Analyst: data exploration and analysis software for complex image-based screens''. BMC Bioinformatics, 2008. '''9''': p. 482.
# Vokes, M.S. and A.E. Carpenter, ''Using CellProfiler for automatic identification and measurement of biological objects in images''. Curr Protoc Mol Biol, 2008. '''Chapter 14''': p. Unit 14 17.
# Lamprecht, M.R., D.M. Sabatini, and A.E. Carpenter, ''CellProfiler: free, versatile software for automated biological image analysis''. Biotechniques, 2007. '''42'''(1): p. 71-5.
# Carpenter, A.E., et al., ''CellProfiler: image analysis software for identifying and quantifying cell phenotypes''. Genome Biol, 2006. '''7'''(10): p. R100.
# Swedlow, J.R., I.G. Goldberg, and K.W. Eliceiri, ''Bioimage Informatics for Experimental Biology (*)''. Annu Rev Biophys, 2009. 38: p. 327-346.
# Eliceiri, K.W. and C. Rueden, ''Tools for visualizing multidimensional images from living specimens''. Photochem Photobiol, 2005. '''81'''(5): p. 1116-22.
# Eliceiri, K.W., et al., ''Analysis of multidimensional biological image data''. Biotechniques, 2002. '''33'''(6): p. 1268-73.
# Rueden, C.T. and K.W. Eliceiri, ''Visualization approaches for multidimensional biological image data''. Biotechniques, 2007. '''43'''(1 Suppl): p. 31, 33-6.
# Provenzano, P.P., et al., ''Nonlinear optical imaging and spectral-lifetime computational analysis of endogenous and exogenous fluorophores in breast cancer''. J Biomed Opt, 2008. '''13'''(3): p. 031220.
# Abramoff, M., P. Magalhaes, and S. Ram, ''Image processing with ImageJ''. Biophotonics International, 2004. '''LAURIN Publishing'''.
# Yan, L., et al., ''Applications of combined spectral lifetime microscopy for biology''. Biotechniques, 2006. '''41'''(3): p. 249, 251, 253 passim.

== See also ==

* [[File:ImageJX_Mar09.pdf]], the ImageJX whitepaper from 2008
