---
title: TIFF
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export, Development]
---


The {% include wikipedia title='TIFF' text='TIFF file format' %} is one of the most widely used formats in biosciences. Many commercial instruments write images using some flavor of TIFF. It is used in [open source](/licensing/open-source) efforts as well; for example, the [Open Microscopy Environment](/software/omero) developed the [OME-TIFF format](http://www.openmicroscopy.org/site/support/ome-model/ome-tiff/) as an open exchange standard for microscopy data.

## ImageJ support

[ImageJ](/software/imagej) (and therefore [ImageJ2](/software/imagej2) with its default legacy user interface) has built-in support for TIFF files via the {% include bc path='File | Open...' %} command.

You can also import TIFFs as [virtual stacks](https://imagej.nih.gov/ij/docs/guide/146-8.html#sub:Virtual-Stacks) via the {% include bc path='File | Import | TIFF Virtual Stack...' %} command.

-   **Pro:** The ImageJ TIFF reader is very fast.
-   **Con:** The ImageJ TIFF support is incomplete. Some valid baseline TIFF files will not open properly. In particular, TIFF files with out-of-order planes cannot be opened.

## Bio-Formats

The [Bio-Formats](/formats/bio-formats) plugins offer a more complete TIFF importer, accessible via the {% include bc path='File | Import | Bio-Formats' %} command.

-   **Pro:** The Bio-Formats TIFF reader can handle many more varieties of TIFF.
-   **Con:** The Bio-Formats TIFF support is not as speedy as ImageJ's TIFF reader.

## SCIFIO

The [SCIFIO](/libs/scifio) library, the I/O library of [ImageJ2](/software/imagej2), imports TIFF files using code adapted from the [Bio-Formats](/formats/bio-formats) project. As such, it is similar to Bio-Formats in that it supports a wider variety of TIFFs, but is less performant than the ImageJ reader. SCIFIO is accessible via the {% include bc path='File | Import | Image...' %} command.

You can tell ImageJ2 to use SCIFIO by default via the {% include bc path='Edit | Options | ImageJ2...' %} menu's "Use SCIFIO when opening files (BETA!)" checkbox.
