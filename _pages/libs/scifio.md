---
mediawiki: SCIFIO
title: SCIFIO
section: Explore:Libraries
categories: [Software,Citable]
artifact: io.scif:scifio
doi: 10.1186/s12859-016-1383-0
---

[SCIFIO](https://scif.io/) is a flexible framework for **SC**ientific **I**mage **F**ormat **I**nput and **O**utput. In other words, it is a library for reading and writing N-dimensional image data—e.g., to and from files on disk. SCIFIO is built on the [SciJava Common](/libs/scijava#scijava-common) library.

[ImageJ2](/software/imagej2) uses SCIFIO by default for most image input tasks. You can change this behavior at any time by running {% include bc path='Edit | Options | ImageJ2'%} and modifying the *Use SCIFIO when opening files* option.

## Benefits of using SCIFIO

SCIFIO is focused on robust and extensible support for reading and writing image file formats. Using it with ImageJ provides many advantages:

-   There is no need to call a special SCIFIO plugin; it works with commands like {% include bc path='File | Open'%} automatically.
-   There are additional import options available via the {% include bc path='File | Import | Image...'%} command.
-   There is a [Bio-Formats](/formats/bio-formats) plugin for SCIFIO, included with the [Fiji](/software/fiji) distribution of ImageJ, that adds automatic support for over a hundred life sciences file formats.
-   Additional SCIFIO file format plugins can be dropped into ImageJ and will also work automatically.
-   Unlike the ImageJ 1.x TIFF implementation, SCIFIO's support for TIFF adheres to the specification, allowing to successfully read many more sorts of TIFFs.
-   Similarly, SCIFIO supports more sorts of JPEG files since it uses its own JPEG decoder.
-   SCIFIO also ships with support for several QuickTime codecs, allowing ImageJ to read QuickTime MOV files even in 64-bit mode without QuickTime for Java.
-   SCIFIO supports many additional open file formats out of the box:
    -   animated GIF
    -   animated PNG
    -   encapsulated postscript (EPS)
    -   JPEG-2000
    -   Micro-Manager datasets
    -   Multi-image Network Graphics (MNG)
    -   Nearly Raw Raster Data (NRRD)
    -   Imspector OBF
    -   OME-TIFF (multidimensional rich metadata TIFF)
    -   OME-XML
    -   PCX
    -   PICT (even in 64-bit mode and/or without QuickTime for Java installed)
-   If SCIFIO cannot handle the image file, it falls back to ImageJ 1.x.
-   You can save to SCIFIO-supported file formats using the {% include bc path='File | Export | Image...'%} command. Supported formats for export include:
    -   APNG
    -   AVI
    -   EPS
    -   ICS
    -   JPEG
    -   JPEG2000
    -   QuickTime
    -   TIFF

## Current limitations of SCIFIO

-   SCIFIO is still in beta, so there is likely to be a higher incidence of bugs. Issues can be reported on the [SCIFIO issue tracker](https://github.com/scifio/scifio/issues).
-   Although we strive for full backwards compatibility, some files may appear slightly different when opened.
-   Opening files with SCIFIO is not fully macro recordable yet.

## Publications

{% include citation %}
