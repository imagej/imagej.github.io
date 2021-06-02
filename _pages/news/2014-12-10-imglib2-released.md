---
mediawiki: 2014-12-10_-_ImgLib2_released
title: 2014-12-10 - ImgLib2 released
---

We are happy to announce the first stable release version of the [ImgLib2](/libs/imglib2) core library!

This release was a central goal of the recent [hackathon](/events/hackathons) at [LOCI](/orgs/loci) in Madison, during the week of October 13 - 17.

The ImgLib2 core library is now [available on Maven Central](http://search.maven.org/#search%7Cga%7C1%7Cg%3A%22net.imglib2%22), and the [source code](/develop/source) for all ImgLib2 projects is [accessible on GitHub](https://github.com/imglib).

Like the [SciJava](/libs/scijava) and [ImageJ2](/software/imagej2) projects, ImgLib2 releases now follow the [semantic versioning](/develop/versioning) scheme. Also, the project and [git](/develop/git) repository structure has changed. The main imglib repository has been [split into multiple repositories](/develop/architecture#git-repositories), named consistently with the artifact names and java package prefixes. Projects are now coupled using non-SNAPSHOT versions, in order to achieve [reproducible builds](/develop/architecture#reproducible-builds).

For further technical details on project structure, see the [Architecture](/develop/architecture) page.

Before coming out of beta, we have made several last-minute changes to the code:

-   All `@Deprecated` methods and classes have been removed.
-   All metadata handling (formerly `imglib2-meta` subproject) is being moved into {% include github org='imagej' repo='imagej-common' label='imagej-common' %}. From ImgLib2 core, the classes `AnnotatedSpace`, `AbstractAnnotatedSpace`, and `Axis` were moved to {% include github org='imagej' repo='imagej-common' label='imagej-common' %}.
-   The current ROI representation was not considered stable enough to be included in a release. The `net.imglib2.roi` and `net.imglib2.labeling` packages were moved to the new {% include github org='imglib' repo='imglib2-roi' label='imglib2-roi' %} subproject which will remain in beta for now.
-   The `net.imglib2.multithreading` package was moved to {% include github org='imglib' repo='imglib2-algorithm' label='imglib2-algorithm' %} and deprecated.
-   We merged work by Albert Cardona and Stephan Preibisch on "fractional" types. ImgLib2 `NativeType`s map pixels into primitive arrays, where often the mapping is one-to-one. For example, an `UnsignedByteType` pixel maps into one byte of a primitive `byte[]` array. With fractional types this mapping maybe non-integral, for example `Unsigned12BitType` maps pixels into a `long[]` array, where each pixel occupies 12/64 longs.
-   Superfluous generic parameters were removed from `Projector<A,B>` interface which is now only `Projector`. Projector implementations were fixed accordingly.
-   Several classes were renamed or moved to more suitable places:
    -   `Extended[Real]RandomAccessibleInterval` moved to the `net.imglib2.view` package.
    -   `RandomAccessibleOnRealRandomAccessible` moved to the `net.imglib2.view` package.
    -   `Binning` moved to the `net.imglib2.util` package.
    -   The contents of package `net.imglib2.collection` (`KDTree` etc.) moved to the `net.imglib2` package.
    -   `net.imglib2.concatenate.Util` was renamed to `net.imglib2.concatenate.ConcatenateUtils`.
    -   `Bounded` moved to the `net.imglib2.outofbounds` package.
    -   The class `NearestNeighborInterpolator` from package `net.imglib2.interpolation.neighborsearch` was renamed to `NearestNeighborSearchInterpolator` (to avoid confusion with the `net.imglib2.interpolation.randomaccess.NearestNeighborInterpolator` class).
    -   The `Pair` interface moved to the `net.imglib2.util` package.
-   The `net.imglib2.util.Util` class was cleaned up:
    -   Methods `getTypeFromRandomAccess()` and `getTypeFromRealRandomAccess()` were removed. We considered them too dangerous because the `RandomAccess` may be pointing to invalid position.
    -   Unused methods `setCoordinateRecursive()` and `getRecursiveCoordinates()` were removed.
    -   Some variants of `computeLength()` and `computeDistance()` were removed. Use methods `distance()` and `length()` from `net.imglib2.util.LinAlgHelpers` instead.
    -   Methods `computeMedian()`, `computeAverage()`, etc. were renamed to `median()`, `average()`, etc.
-   These unused classes were removed:
    -   `IterableIntervalSubsetT`
    -   `Triple`
    -   `RealPositionableFloorPositionable`
    -   `RealPositionableRoundPositionable`
    -   `ImgTranslationAdapter`
-   Packages `net.imglib2.img.constant` and `net.imglib2.sampler.special` were removed (`ConstantImg`, `ConstantRandomAccessible`, etc). Similar functionality can now be achieved through the `net.imglib2.util.ConstantUtils` class and `Views`.

All ImgLib2 subprojects have been adapted to these changes and released (in some cases as new beta versions).

One thing still pending is to upload these new ImgLib2 releases to the ImageJ and [Fiji](/software/fiji) [update sites](/update-sites), making them available to users of ImageJ and Fiji. This change has been rather involved, since there is a lot of downstream code affected by the API changes. But we expect to make the new ImgLib2 available to users before the end of the calendar year. Stay tuned for further announcements!

 
