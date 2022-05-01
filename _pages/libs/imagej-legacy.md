---
title: ImageJ Legacy Bridge
section: Explore:Libraries
artifact: net.imagej:imagej-legacy
icon: /media/icons/imagej2.png
project: /software/imagej2
---

Backward compatibility is one of ImageJ2's most important goals. It must remain possible to use existing plugins and macros with new versions of ImageJ.

## ImageJ Legacy

The [ImageJ2](/software/imagej2) project is a complete redesign, with no dependency on the original [ImageJ](/software/imagej). However, to facilitate backwards compatibility, there is an **ImageJ Legacy** component (source {% include github org='imagej' repo='imagej-legacy' %}) which provides extensions for ImageJ2 and ImageJ to operate in harmony.

The ImageJ legacy layer provides the following extensions:

-   It makes ImageJ **usable [headless](/learn/headless)** from the command line.
-   It wraps the **ImageJ UI as a [SciJava](/libs/scijava) user interface**.
-   It **translates between ImageJ and ImageJ2 data structures** on demand.

ImageJ2 currently uses the ImageJ user interface by default, since many users need to retain access to ImageJ plugins.

### The ImageJ user interface

ImageJ2 legacy layer converts the ImageJ user interface (UI) into a SciJava-compatible UI by implementing the {% include javadoc project='SciJava' package='org/scijava/ui' class='UserInterface' %} interface via the {% include javadoc package='net/imagej/legacy/ui' class='LegacyUI' %} class.

However, things are complicated by the fact that the original ImageJ was not designed with such requirements in mind. The legacy layer uses a bytecode manipulation library called [Javassist](/develop/javassist) to rewrite portions of ImageJ at runtime, in order to facilitate integration and extension. See the {% include github org='imagej' repo='ij1-patcher' label='ij1-patcher' %} project for details.

### Translation of data structures

Each {% include javadoc package='net/imagej/display' class='ImageDisplay' %} has a linked {% include javadoc project='ImageJ1' package='ij' class='ImagePlus' %}, kept in sync by the {% include javadoc package='net/imagej/legacy' class='LegacyImageMap' %}. Whenever the need arises, the legacy layer syncs the linked data objects. In order to maintain reasonable performance, every opportunity is taken to avoid data translation by making data changes in place, and only on demand (lazily, with caching). The legacy layer reuses data by reference when feasible—in particular, when image planes are stored in primitive arrays—but in some cases the data must be copied (e.g., for ROIs).

Currently, automatic synchronization is disabled as it has negative performance implications. The planned solution to the performance problems is to {% include github org='imagej' repo='imagej-legacy' issue='86' label='implement a wrapping layer' %}, instead of relying on up-front pixel-wise translation.

In the mean time, full synchronization can be forced by setting a `imagej.legacy.sync` [system property](https://docs.oracle.com/javase/tutorial/essential/environment/sysprop.html). This can be done in a running ImageJ instance, for example by running the following as a [BeanShell script](/scripting/beanshell):

```java
System.setProperty("imagej.legacy.sync", "true");
```

## Updating ImageJ commands to the new paradigm

The eventual goal is to migrate all core ImageJ plugins to the ImageJ2 paradigm. Many ImageJ plugins have been already been updated in this fashion; see the {% include github org='imagej' repo='imagej-ops' label='imagej-ops' %} and {% include github org='imagej' repo='imagej-plugins-commands' label='imagej-plugins-commands' %} repositories in particular.

## See also

-   The [ImageJDev talk](https://conference.imagej.net/2010/curtis-rueden/2010-10-27-ImageJDev.pdf) from the ImageJ 2010 Conference, for a historical perspective on how this approach to compatibility evolved over time.
