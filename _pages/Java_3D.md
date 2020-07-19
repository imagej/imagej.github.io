[[wikipedia:Java 3D|Java 3D]] is a technology used for 3D visualization in Java. In [[ImageJ]], it is used by the [[3D Viewer]] plugin, and hence transitively by other plugins which rely on the 3D Viewer for their visualization, such as the [[Simple Neurite Tracer]] and [[TrakEM2]].

== Status of Java 3D ==

The Java 3D project, originally developed at Sun (now Oracle), has been abandoned for several years in favor of [https://docs.oracle.com/javase/8/javafx/graphics-tutorial/javafx-3d-graphics.htm JavaFX 3D]. However, it has been adopted by the [https://jogamp.org/ JogAmp] community, and is now maintained there—though no longer under active development.

From the perspective of new features, Java 3D is essentially a dead technology. The future of 3D visualization in ImageJ is the [[SciView]] plugin. But it will be a lot of work to make SciView comparable to—and eventually better than—3D Viewer, so the ImageJ and [[Fiji]] teams are still exploring the best ways to proceed here.

== Versions of Java 3D ==

=== Java 3D 1.5 ===

The last version of Java 3D supported by Sun/Oracle was 1.5.2. It was packaged as an extension of Java, meaning it needed to be installed into your Java Runtime Environment, rather than shipped as a normal Java library.

It works with Java 6, but:

* It has a restrictive license.
* It does not work Java 7 or 8 on OS X.
* It does not work with Java 8 (or 7?) on some Windows systems.

The Java 6 version of ImageJ works with Java 3D 1.5.2, by launching the 3D Viewer and allowing it to automatically install Java 3D; see [[2016-05-10 - ImageJ HOWTO - Java 8, Java 6, Java 3D|this page]] for further details.

=== Java 3D 1.6 ===

Java 3D 1.6 is the community version maintained by JogAmp. It was rewritten to work on top of [[wikipedia:Java OpenGL|JOGL]], and requires Java 7 or newer.

The Java 8 version of ImageJ includes Java 3D 1.6; see [[2016-05-10 - ImageJ HOWTO - Java 8, Java 6, Java 3D|this page]] for further details.
