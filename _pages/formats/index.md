---
title: Formats
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
nav-links: true
nav-links: Formats
---


Thanks to ImageJ's [extensibility](/develop/architecture#extensibility) via [plugins](/plugins), it supports a lot of image formats!

## File formats

### Life sciences

The [OME Bio-Formats](/formats/bio-formats) plugins provide support for over
130 file formats in microscopy, medical imaging, and related life science
formats. Bio-Formats is included with the [Fiji](/software/fiji) distribution
of ImageJ. See also the Bio-Formats
[list of supported formats](https://www.openmicroscopy.org/site/support/bio-formats/supported-formats.html).

### DICOM

ImageJ has some built-in support for the DICOM format, and there are also
plugins for working with DICOM files. See the [DICOM](/formats/dicom) page for
full details.

### HDF

The HDF5 [update site](/update-sites) enables support for reading and writing
{% include wikipedia title="Hierarchical Data Format" %} image data. Note that
HDF5 is a very broad specification; the HDF5 plugin will not support all manner
of HDF files, but only those written according to its constraints.

### Video

Out of the box, ImageJ has limited support for some video formats such as AVI
and [QuickTime](/formats/quicktime), and there are also plugins which extend
ImageJ's support for videos. See the [Video](/formats/video) page for details.

## Opening and importing

{% include warning/stub %}

## Saving and exporting

{% include img src="save-as" align="right" width=150 %}

### File formats

The {% include bc path="File|Save" %} (hotkey: S) menu command will save the
image as a TIFF file. Other formats are available (see menu image on the right)
and can be accessed by {% include bc path="File|Save As..." %}. When the "*Save
As*" dialog is opened, ImageJ will enter the image window's name, plus the
appropriate file suffix, as the "File Name".

*Animated GIF...* Choosing this option from the "*Save As*" menu saves a stack
as an animated GIF. It is only compatible on RGB or 8 bit images. A more
suitable option would be saving as *GIF*, where the only limitation is that any
RGB color stacks must be converted to 8 bit color.

Uncompressed AVI files are exported via
{% include bc path="File|Save As...|AVI..." %}. The frame rate and compression
option of the exported AVI movie is selected in the resulting window. Frame
rate can be between 0.1 and 100 frames per second (fps). The compression may be
in JPEG, PNG, or uncompressed. Though uncompressed files are large, they should
be playable on any PC/Mac without decoder issues.

Flash MX will import uncompressed AVI files. The frame-rate will then be
determined by Flash, not the AVI movie file.

Other options for saving and exporting image files are shown in the ImageJ
*Save As* menu. Their procedures are all straightforward.

### Image sequences

*Image Sequence...* This option saves each slice in a stack as a separate TIF
file. You will be presented with the option to either name the images
numerically or with the slice labels.

### Non-image formats

*Selection...* After drawing an ROI onto an image, the selection's coordinates
can be saved using this option. Once the ROI is deselected, it can be restored
at any time in the same location by opening the saved ROI.

*XY Coordinates...* This option is similar to
{% include bc path="File|Save As|Selection..." %}, but this choice saves the
coordinates of the selection in a text file with two columns for X and Y
coordinates.

*Results...* This uses the information in an active results window and exports
it into a text file.

### Exporting with Bio-Formats

Files may also be exported to many file types using
{% include bc path='Plugins|Bio-Formats|Bio-Formats Exporter'%}.
As of this writing, the supported file types are:

- Animated PNG
- AVI
- Encapsulated PostScript (EPS, EPSI)
- Image Cytometry Standard (IDS, ICS)
- Java source code
- JPEG
- JPEG-2000
- OME-TIFF
- OME-XML
- QuickTime
- TIFF

See the Export column of the [Bio-Formats list of supported
formats](http://openmicroscopy.org/site/support/bio-formats5/supported-formats.html)
for an up-to-date list of formats which can be exported.

## See also

- The ImageJ Documentation Wiki page
  [FAQ: Which file formats are supported by ImageJ](http://imagejdocu.list.lu/doku.php?id=faq:general:which_file_formats_are_supported_by_imagej)
  (though it is outdated).
