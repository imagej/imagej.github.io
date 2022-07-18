---
title: ImgLib2
section: Explore:Libraries:ImgLib2
artifact: net.imglib2:imglib2
doi: 10.1093/bioinformatics/bts543
project-blurb: the ImgLib2 multidimensional image processing library
---

ImgLib2 is a general-purpose, multidimensional image processing library.

It provides an interface-driven design that supports numeric and non-numeric data types (8-bit unsigned integer, 32-bit floating point, etc.) in an extensible way. It implements several data sources and sample organizations, including one single primitive array, one array per plane, N-dimensional array "cells" cached to and from disk on demand, and planes read on demand from disk.

## Resources

-   [ImgLib2 paper](http://bioinformatics.oxfordjournals.org/content/28/22/3009.full)
-   [ImgLib2 Documentation](/libs/imglib2/documentation)
-   [ImgLib2 Examples](/libs/imglib2/examples)
-   {% include javadoc project='ImgLib2' %} javadoc
-   [How To Migrate Code From ImgLib To ImgLib2](/libs/imglib2/migrate-from-imglib1)
-   ["Introduction to ImgLib2"](/libs/imglib2/workshop-introductory) workshop
-   ["Advanced Programming with ImgLib2"](/libs/imglib2/workshop-advanced) workshop
-   ["I2K 2020 Introductory ImgLib2"](https://github.com/saalfeldlab/i2k2020-imglib2-intro) workshop
-   ["I2K 2020 Advanced ImgLib2"](https://github.com/saalfeldlab/i2k2020-imglib2-advanced) workshop

## Source code

You can find the source {% include github org='imglib' repo='imglib2' %}.

There is also a continuous integration system that builds ImgLib2 [every time the code changes](https://travis-ci.org/imglib/imglib2).

## ImgLib2 vs. ImgLib1

[ImgLib1](/libs/imglib1) is the previous incarnation of the library. We encourage developers to use ImgLib2 instead, and [migrate existing ImgLib1 programs to ImgLib2](/libs/imglib2/migrate-from-imglib1) whenever possible.

For an explanation of how ImgLib2 has changed from ImgLib1, see the [Changes from ImgLib1 to ImgLib2](/libs/imglib2/changes-from-imglib1) page.

See the [How To Migrate Code From ImgLib To ImgLib2](/libs/imglib2/migrate-from-imglib1) page for details on how to update your ImgLib1-based code to use ImgLib2.

## API Version History

A history of API changes is available at: [https://abi-laboratory.pro/java/tracker/timeline/imglib2/](https://abi-laboratory.pro/java/tracker/timeline/imglib2/)

## Other links

-   [ImgLib2 development discussion](/libs/imglib2/discussion)
-   [ImgLib2 performance benchmarks](/libs/imglib2/benchmarks)
-   [ImageJ2](/software/imagej2) uses ImgLib2 as its core data model

## Publication

Pietzsch, T., Preibisch, S., Tomančák, P., & Saalfeld, S. (2012). [ImgLib2—generic image processing in Java](http://bioinformatics.oxfordjournals.org/content/28/22/3009.full). Bioinformatics, 28(22), 3009-3011.

 
