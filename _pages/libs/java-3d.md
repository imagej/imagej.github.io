---
mediawiki: Java_3D
title: Java 3D
section: Explore:Libraries
---

{% include wikipedia title='Java 3D' text='Java 3D'%} is a technology used for 3D visualization in Java. It is used by ImageJ's [3D Viewer](/plugins/3d-viewer) plugin, and hence transitively by other plugins which rely on the 3D Viewer for their visualization, such as [TrakEM2](/plugins/trakem2) and [Simple Neurite Tracer](/plugins/simple-neurite-tracer).

## Status of Java 3D

The Java 3D project, originally developed at Sun (now Oracle), has been abandoned for several years in favor of [JavaFX 3D](https://docs.oracle.com/javase/8/javafx/graphics-tutorial/javafx-3d-graphics.htm). However, it has been adopted by the [JogAmp](https://jogamp.org/) community, and is now maintained there—though no longer under active development.

From the perspective of new features, Java 3D is essentially a dead technology. The future of 3D visualization in ImageJ is the [sciview](/plugins/sciview) plugin. But it will be a lot of work to make sciview comparable to—and eventually better than—3D Viewer, so the ImageJ and [Fiji](/software/fiji) teams are still exploring the best ways to proceed here.

## Versions of Java 3D

### Java 3D 1.5

The last version of Java 3D supported by Sun/Oracle was 1.5.2. It was packaged as an extension of Java, meaning it needed to be installed into your Java Runtime Environment, rather than shipped as a normal Java library.

It works with Java 6, but:

-   It has a restrictive license.
-   It does not work with Java 7 or 8 on macOS.
-   It does not work with Java 8 (or 7?) on some Windows systems.

The Java 6 version of ImageJ works with Java 3D 1.5.2, by launching the 3D Viewer and allowing it to automatically install Java 3D; see [this page](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) for further details.

### Java 3D 1.6

Java 3D 1.6 is the community version maintained by JogAmp. It was rewritten to work on top of {% include wikipedia title='Java OpenGL' text='JOGL'%}, and requires Java 7 or newer.

The Java 8 version of ImageJ includes Java 3D 1.6; see [this page](/news/2016-05-10-imagej-howto-java-8-java-6-java-3d) for further details.
