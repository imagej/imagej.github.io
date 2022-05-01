---
mediawiki: Test_Java3D
title: Test Java3D
categories: [Uncategorized]
---

{% include info-box software='ImageJ' name='Test Java3D' author='Benjamin Schmid' maintainer='Benjamin Schmid' filename='http://132.187.25.13/home/imagej/Test\_Java3D.jar' source='http://132.187.25.13/home/imagej/Test\_Java3D.jar' released='-' latest-version='-' status='stable' category='Plugins' %}

## Purpose

Plugin to test whether Java3D is installed and working correctly.

## Documentation

Java3D is an extension to Java, providing a library for hardware-accelerated 3D rendering. It runs on any common platform, but there are different binaries for Windows, Linux and Mac OS. Furthermore, the underlying graphics interface can either be OpenGL (via Jogl, its Java binding) or DirectX.

These dependencies on the system lead sometimes to problems with Java3D. If a problem occurs, the first step is to find out whether it is due to an incorrectly installed Java3D or to the code in the 3D Viewer.

This plugin uses very basic Java3D features, and thereby provides a way to check if Java3D is working correctly. All it does is to show a rotating coloured cube, as shown in the figure below.

![](/media/plugins/test-java3d.png)

If you encounter problems, you might want to consult the [Java 3D Application Development page](http://wiki.java.net/bin/view/Javadesktop/Java3DApplicationDevelopment). In particular, you might want to restart Fiji with [specific Java 3D properties set](http://wiki.java.net/bin/view/Javadesktop/Java3DApplicationDevelopment#java-3d-system-properties).


