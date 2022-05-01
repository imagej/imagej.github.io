---
title: ImageJ2
section: Explore:Software
doi: 10.1186/s12859-017-1934-z
artifact: net.imagej:imagej
icon: /media/icons/imagej2.png
project-blurb: the ImageJ2 platform
---

{% include aside content="
## Mission

- **Design** the next generation of ImageJ, driven by the needs of the community.
- **Collaborate** across organizations, fostering open development through sharing and reuse.
- **Broaden** ImageJ's usefulness and relevance across many disciplines of the scientific community.
- **Maintain** backwards compatibility with existing ImageJ functionality.
- **Unify** online resources to a central location for the ImageJ community.

See also [these presentation slides about ImageJ2](/presentations/2015-09-03-imagej2-and-fiji/#/4)." %}

ImageJ2 is a rewrite of [ImageJ](/software/imagej) for multidimensional image data, with a focus on scientific imaging. Its central goal is to broaden the paradigm of ImageJ beyond the limitations of the [original ImageJ application](/software/imagej), to support the next generation of multidimensional scientific imaging.

To ensure backwards compatibility, ImageJ2 has been designed to fully integrate into the existing ImageJ user interface. This allows users to keep using ImageJ in familiar ways, while providing the ability to migrate toward more powerful new features as needed.

The [Fiji](/software/fiji) project has been built on top of ImageJ2 for quite some time, so you may already be familiar with some of ImageJ2's features—some of which, such as the [Updater](/plugins/updater) and [Launcher](/learn/launcher), were originally developed as part of Fiji. 

## Features of ImageJ2

ImageJ2 provides many new features and capabilities:

-   The [ImageJ Updater](/plugins/updater) makes it simple to stay up to date, and to add new plugins by enabling additional [Update Sites](/update-sites).
-   New and enhanced file format support via the [SCIFIO](/libs/scifio) library ([see below](#improved-image-io-with-the-scifio-library)).
-   More powerful [Script Editor](/scripting/script-editor) with support for several scripting languages.
-   New commands:
    -   {% include bc path='Plugins | Debug | Dump Stack' %} for debugging when things {% include wikipedia title='Hang (computing)' text='hang' %}.
    -   {% include bc path='Plugins | Debug | System Information' %} for reporting on versions of installed plugins and libraries.
-   Use ImageJ2's N-dimensional [ImgLib2](/libs/imglib2)-based data structures (still in beta).
-   Write parameterized commands and scripts:
    -   Typed inputs and outputs with no dependence on AWT user interface.
    -   Mix and match ImageJ and ImageJ2 data structures.
    -   Plugins appear in the menu automatically without plugins.config files.
    -   Reusable in many contexts: [KNIME](/software/knime), [CellProfiler](/software/cellprofiler), [OMERO](/software/omero), [headless](/learn/headless)...

### Integrated search bar

<img src="/media/search-bar.png" width="600"/>

The search bar finds commands, and can search the ImageJ wiki as well as the [Image.sc Forum](http://forum.image.sc/) if you check those respective checkboxes.

For power users and developers, the search bar supports execution of "code snippets"—single lines of code for performing tasks—by starting the query with `!`. Any code that works in the [Script Interpreter](/scripting/interpreter) should be usable as a code snippet.

Developers can extend the capabilities of the search bar by writing [Searcher](https://github.com/scijava/scijava-search/blob/scijava-search-0.3.1/src/main/java/org/scijava/search/Searcher.java#L36-L46) plugins.

### Improved image I/O with the SCIFIO library

ImageJ2 uses the [SCIFIO](/libs/scifio) library (SCientific Image Format Input and Output) by default for most image input tasks. You can change this behavior at any time by running {% include bc path='Edit | Options | ImageJ2' %} and modifying the *Use SCIFIO when opening files* option.

For further details, see the [SCIFIO](/libs/scifio) page.

### ImageJ2 is more than just an application

ImageJ2 is also a collection of reusable software libraries built on [SciJava](/libs/scijava), using a powerful plugin framework to facilitate rapid development and painless user customization.

The following software component libraries form the core of ImageJ2:

-   [ImageJ Common](/libs/imagej-common) - The core image data model, using ImgLib2.
-   [ImageJ Ops](/libs/imagej-ops) - An extensible framework for reusable image processing algorithms.
-   [ImageJ Updater](/plugins/updater) - A mechanism to update individual plugins and libraries within ImageJ2.
-   [ImageJ Legacy](/libs/imagej-legacy) - Provides complete backwards compatibility with the original ImageJ.
-   [SciJava Common](/libs/scijava#scijava-common) - The core frameworks for plugins, modules and the application itself.

See the [Architecture](/develop/architecture) page for further details.

## Rationale

In recent years a segment of the ImageJ developer community has repeatedly inquired as to ImageJ's future. The program has been successful enough that it would greatly benefit from current open-source software best practices: a publicly accessible source code repository, a suite of unit tests with a continuous build integration system, a central repository of extensions, clear guidelines on how external developers can contribute to both those extensions and to the core program when warranted, and a development roadmap addressing feature requests and tasks from the community.

Listening to the ImageJ community, it is clear that:

1.  There is substantial demand from developers for a next-generation version of ImageJ with a cleaner, more modular API, so that ImageJ can be leveraged not just as a standalone analysis program, but as a **robust, extensible library** in a variety of contexts.
2.  The ImageJ user community has invested a lot of time and energy to develop complex workflows within ImageJ, and they oppose any change that would break them. Thus, any effort to improve the software must **maintain compatibility with existing code**.
3.  Further, any next-generation version of ImageJ must maintain community unity, and **not fork the project**. All components of this project will be developed as upgrades to core ImageJ.
4.  The ImageJ community as a whole would substantially benefit from a **central effort to organize** and serve program code (both the core application and its plugins), keep track of bugs and feature requests, and better leverage external developer contributions.

For more details, see the [presentation from the 2010 ImageJ Conference](http://developer.imagej.net/2010/10/29/imagejdev-presentation-imagejconf-2010).

## Funding

ImageJ2 is funded from a variety of sources. See the [Funding](/contribute/funding) page for details.

## Publications

* {% include citation %}

* {% include citation id='learn/flavors' %}

## Presentations

-   2017-Feb-16 "What's New in ImageJ2?" \[ [slides](/presentations/2017-02-16-imagej2-neubias/) \]
-   2015-Sep-03 "The ImageJ2 platform, and the Fiji distribution of ImageJ" \[ [video](https://vimeo.com/140929687), [slides](/presentations/2015-09-03-imagej2-and-fiji/) \]
-   2012-Oct-24 "ImageJ2: Current Status and Future Directions" \[ [slides](http://conference.imagej.net/2012/curtis-rueden/2012-10-24-imagej-conference.odp) \]
-   2010-Oct-27 "ImageJDev: Next Generation ImageJ" \[ [slides](http://conference.imagej.net/2010/curtis-rueden/2010-10-27-ImageJDev.pdf) \]

## See also

-   [ImageJ1-ImageJ2 cheat sheet](/develop/ij1-ij2-cheat-sheet)
