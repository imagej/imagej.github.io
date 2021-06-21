---
title: ImageJ Common
section: Explore:Libraries
artifact: net.imagej:imagej-common
icon: /media/icons/imagej2.png
---

The ImageJ Common library contains [ImageJ2](/software/imagej2)'s core image data model, based on the [ImgLib2](/libs/imglib2) library for multidimensional image data processing, as well as the corresponding core image display logic for user interfaces, based on the [SciJava Common](/libs/scijava#scijava-common) application framework.

{% include testimonial person='hadim' description='Python developer'
  quote='I have to admit that IJ2 API and Java 8 make the process very smooth. Much better than few years ago :-0'
  source='https://gitter.im/imagej/imagej?at=571e431b7469496137b9059f' %}

Using [ImgLib2](/libs/imglib2) offers several benefits:

-   Support for many different data types (different combinations of bit depths, signedness, and integer/real representations).
-   Support for large datasets (many planes/cubes/etc., large planes/cubes/etc.).
-   Abstraction of the underlying image storage mechanism (file on disk, data in memory, remote URL, remote database, etc.).

ImageJ Common is still in beta, with significant changes still planned for its central class hierarchies.

At the time of this writing, the central image data structures are:

-   {% include javadoc package='net/imglib2/meta' class='ImgPlus' %}
-   {% include javadoc package='net/imagej' class='Dataset' %} and {% include javadoc package='net/imagej' class='DefaultDataset' %}
