---
title: SciJava
section: Explore:Libraries
icon: /media/icons/scijava.svg
logo: /media/logos/scijava.png
artifact: org.scijava:scijava-common
ref: Rueden, C., Schindelin, J., Hiner, M. &amp; Eliceiri, K. (2021). SciJava Common [Software]. https://scijava.org/.
---

SciJava is a collaboration of projects providing software for scientific
computing—an effort to cooperate and reuse code when feasible.

It is also a collection of foundational software libraries, upon which
[ImageJ](/software/imagej) and [Fiji](/software/fiji) are built.

# The SciJava component collection

The following component layers are part of the **[SciJava component collection](/develop/architecture)**:

-   **SciJava** - foundational layer unspecific to image processing, including the [SciJava Common](#scijava-common) shared library with powerful plugin framework and application container, and plugins built on it.
-   [ImgLib2](/libs/imglib2) - core libraries for N-dimensional image processing.
-   [SCIFIO](/libs/scifio) - core libraries for N-dimensional image I/O.
-   [ImageJ2](/software/imagej2) - core libraries and application for N-dimensional image processing.
-   [Fiji](/software/fiji) - "batteries-included" distribution of ImageJ, bundling a lot of plugins which facilitate scientific image analysis.
-   [BigDataViewer](/plugins/bdv) - re-slicing browser and Fiji plugin for terabyte-sized multi-view image sequences
-   [TrakEM2](/plugins/trakem2) - Fiji plugin suite for morphological data mining, three-dimensional modeling and image stitching, registration, editing and annotation.
-   [Bio-Formats](/formats/bio-formats) - libraries and ImageJ plugins for life sciences image format I/O.

All components in this collection are managed by SciJava's [Bill of Materials](/develop/architecture#bill-of-materials) to make it easier for downstream components to use them without version conflicts.

# The SciJava pledge

The following projects are part of the **SciJava pledge** to work together, reuse code and synergize wherever possible:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: middle">
        <p>{% include icon name='ImageJ2' %}</p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="/software/cellprofiler"><img src="/media/logos/cellprofiler.png" height="64px"></a></p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="/software/knime"><img src="/media/logos/knime.jpg" height="54px"></a></p>
      </td>
      <td></td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="/software/omero"><img src="/media/logos/omero.png" height="32px"></a></p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="https://github.com/scenerygraphics/scenery"><img src="/media/logos/scenery.png" height="72px"></a></p>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>{% include icon name='Fiji' %}</p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="/software/icy"><img src="/media/logos/icy.png" height="48px"></a></p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p>{% include icon name='Micro-Manager' size='48px' %}</p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p>{% include icon name='VCell' size='48px' %}</p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p><a href="/formats/bio-formats"><img src="/media/logos/bio-formats.png" height="28px"></a></p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p>{% include icon name='Alida' size='48px' %}</p>
      </td>
      <td style="text-align: center; vertical-align: middle">
        <p>{% include icon name='MiToBo' size='48px' %}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

See the [Architecture](/develop/architecture) and [Governance](/contribute/governance) pages, as well as the [SciJava web site](https://scijava.org/), for further details.

# SciJava Common

SciJava Common is a common library for [SciJava](/libs/scijava) software. It provides a plugin framework, with an extensible mechanism for service discovery, backed by its own annotation processor, so that plugins can be loaded dynamically. It is used by both [ImageJ](/software/imagej) and [SCIFIO](/libs/scifio).

## Plugin framework

First and foremost, SciJava Common is a plugin framework—a base for developing highly modular and extensible Java applications.

### Plugin discovery

All plugins available on Java's classpath are automatically discovered and made available. This is accomplished by scanning classpath resources for the file path `META-INF/json/org.scijava.plugin.Plugin`. Such files are generated at compile time by a Java annotation processor that writes them in response to `@Plugin` annotations on Java classes, an idea inspired by the [SezPoz](https://github.com/jglick/sezpoz/) project.

## Application container

All program state, such as available plugins, is accessible from a root object known as the *application context*.

### Services


{% capture  content %}
Whereas [ImageJ1](/software/imagej1) is a {% include wikipedia title='Singleton pattern' text='singleton'%}, with static methods to access much of its functionality, [ImageJ2](/software/imagej2) encapsulates its program state in the application context, allowing multiple simultaneous such contexts in the same JVM.
{% endcapture %}
{% include notice icon="imagej1" content=content %}ImageJ encapsulates its various parts as separate "services" that provide related state functionality and track related program state. An instance of the {% include javadoc package='net/imagej' class='ImageJ' %} class is nothing more than a collection of these services; this instance is referred to as the "application gateway." Services are defined as interfaces, with concrete implementations as plugins. This design provides [seams](http://c2.com/cgi/wiki?SoftwareSeam) in the right places so that behavior at every level can be customized and overridden.

#### SciJava services

Here are a few of SciJava Common's major core services:

-   **{% include javadoc project='SciJava' package='org/scijava/app' class='AppService' %}** - Tracks software applications (SCIFIO, ImageJ, etc.) present in the context.
-   **{% include javadoc project='SciJava' package='org/scijava/display' class='DisplayService' %}** - Tracks available displays, as well as the active display, and provides the means to create new displays to visualize data.
-   **{% include javadoc project='SciJava' package='org/scijava/event' class='EventService' %}** - Publishes events to the {% include wikipedia title='Publish%E2%80%93subscribe pattern' text='event bus'%}, and allows interested parties to subscribe to them. The service provides the central means of communication between various parts of the codebase.
-   **{% include javadoc project='SciJava' package='org/scijava/io' class='IOService' %}** - General tools for opening and saving data within the context.
-   **{% include javadoc project='SciJava' package='org/scijava/menu' class='MenuService' %}** - Builds the application menu structure.
-   **{% include javadoc project='SciJava' package='org/scijava/module' class='ModuleService' %}** - Tracks available modules, and provides the infrastructure for executing them.
-   **{% include javadoc project='SciJava' package='org/scijava/object' class='ObjectService' %}** - Tracks available objects of various types, including {% include javadoc package='net/imagej' class='Dataset' %}s and {% include javadoc package='org/scijava/display' class='Display' %}s.
-   **{% include javadoc project='SciJava' package='org/scijava/options' class='OptionsService' %}** - Tools for managing program settings.
-   **{% include javadoc project='SciJava' package='org/scijava/platform' class='PlatformService' %}** - Provides hooks for extending the application's behavior depending on the deployment platform (operating system, version of Java, etc.).
-   **{% include javadoc project='SciJava' package='org/scijava/plugin' class='PluginService' %}** - Tracks available plugins, and provides the infrastructure for executing them (using the {% include javadoc package='org/scijava/module' class='ModuleService' %}).
-   **{% include javadoc project='SciJava' package='org/scijava/script' class='ScriptService' %}** - Provides utilities for running scripts and macros.
-   **{% include javadoc project='SciJava' package='org/scijava/app' class='StatusService' %}** - Publishes status updates for ongoing operations.
-   **{% include javadoc project='SciJava' package='org/scijava/thread' class='ThreadService' %}** - Manages multithreading.
-   **{% include javadoc project='SciJava' package='org/scijava/tool' class='ToolService' %}** - Tracks available tools—logic binding user input to behavior—as well as the active tool (selected on the toolbar).
-   **{% include javadoc project='SciJava' package='org/scijava/ui' class='UIService' %}** - Discovers and launches a user interface for interacting with ImageJ.

#### ImageJ services

Some of the services which ImageJ adds:

-   **{% include javadoc package='net/imagej' class='DatasetService' %}** - Tools for creating and managing image data.
-   **{% include javadoc package='net/imagej/display' class='ImageDisplayService' %}** - Similar to {% include javadoc package='org/scijava/display' class='DisplayService' %}, but specifically for {% include javadoc package='net/imagej/display' class='ImageDisplay' %}s.
-   **{% include javadoc package='net/imagej/display' class='OverlayService' %}** - Tools for creating and managing image overlays and regions of interest (ROIs).

#### SCIFIO services

SCIFIO provides several additional services—in particular:

-   **{% include javadoc project='SCIFIO' package='io/scif/services' class='FormatService' %}** - Service for managing available image formats.

## Menuing system

The SciJava menuing system is divided into several layers, to make it easier to override its behavior or customize its appearance in a user interface.

### Modules

Each module known to the system (via the {% include javadoc package='org/scijava/module' class='ModuleService' %} can have a `menuPath` that says where it should live (by default) in the menu. It also has a `menuRoot` that says in *which* menu it should live, with the default being the `APPLICATION_MENU_ROOT`, indicating the main application menu structure.

### MenuService

The {% include javadoc package='org/scijava/menu' class='MenuService' %} takes care of constructing {% include javadoc package='org/scijava/menu' class='ShadowMenu' %} tree structures for all available modules in the system, using their `menuPath` and `menuRoot` values. These tree structures are UI-agnostic. There is one `ShadowMenu` per `menuRoot`, which can be requested at will from the `MenuService`.

### User interfaces

The {% include javadoc package='org/scijava/ui' class='UIService' %} then takes care of constructing an actual UI-specific menu bar (or whatever UI components and/or widgets it wants) from the available `ShadowMenu`s. There is a type hierarchy beneath the {% include javadoc package='org/scijava/menu' class='MenuCreator' %} interface intended for this purpose; for example, the {% include javadoc package='org/scijava/ui/swing/menu' class='SwingJMenuBarCreator' %} implements `MenuCreator` to create and maintain a Swing {% include javadoc project='Java' package='javax/swing' class='JMenuBar' %} that reflects the state of a particular `ShadowMenu`.

### How changes propagate

When modules are added, removed or changed (via {% include javadoc package='org/scijava/module/event' class='ModulesAddedEvent' %}, {% include javadoc package='org/scijava/module/event' class='ModulesRemovedEvent' %}, {% include javadoc package='org/scijava/module/event' class='ModulesUpdatedEvent' %}), the `MenuService` listens and updates the associated `ShadowMenu`(s) accordingly. It notifies interested parties that it has done so by firing a corresponding event: {% include javadoc package='org/scijava/menu/event' class='MenusAddedEvent' %}, {% include javadoc package='org/scijava/menu/event' class='MenusRemovedEvent' %}, or {% include javadoc package='org/scijava/menu/event' class='MenusUpdatedEvent' %}.

## API Version History

A history of API changes is available at: https://abi-laboratory.pro/java/tracker/timeline/scijava-common/

## Further reading

-   [SciJava web site](https://scijava.org/)
-   [SciJava Common presentation](https://scijava.org/scijava-common/scijava-common.html)
-   {% include github org='imagej' repo='tutorials' label='ImageJ tutorials' %}
-   {% include github org='scijava' repo='scijava-common' label='SciJava Common source code' %}
