---
title: DICOM
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
---


{% include wikipedia title='DICOM' text='Digital Imaging and Communications in Medicine (DICOM)'%} is a standard for handling, storing, printing, and transmitting information in medical imaging.

## How to read DICOM files into ImageJ?

-   ImageJ has built-in support for reading some kinds of DICOM files. Try {% include bc path='File | Open'%} and see how it goes.
-   The [Bio-Formats](/formats/bio-formats) plugin supports some kinds of DICOM files, too. Bio-Formats is available in the [Fiji](/software/fiji) distribution of ImageJ. Try {% include bc path='File | Import | Bio-Formats'%}.
-   The [Tudor Dicom Tools](http://santec.tudor.lu/project/dicom) plugin suite can read and write many kinds of DICOM, and provide some support for working with DICOM metadata structures.

## How to save DICOM files from ImageJ?

The [Tudor Dicom Tools](http://santec.tudor.lu/project/dicom) provide basic support for saving as DICOM.

## How to work with DICOM headers from a script?

An example of using the `DicomTools.getTag()` method from [JavaScript](/scripting/javascript):
```java
importClass(Packages.ij.IJ)
importClass(Packages.ij.util.DicomTools)
imp = IJ.openImage("http://wsr.imagej.net/images/ct.dcm.zip");
studyDescription = DicomTools.getTag(imp, "0008,1030");
imagePosition = DicomTools.getTag(imp, "0020,0032");
pixelSpacing = DicomTools.getTag(imp, "0028,0030");
print("Study Description: "+ studyDescription);
print("Image Position: "+imagePosition);
print("Pixel Spacing: "+ pixelSpacing);
```

## How to work with DICOM headers from a macro?

See these [macro](/scripting/macro) functions:

-   [getImageInfo()](https://imagej.nih.gov/ij/developer/macro/functions.html#getImageInfo)
-   [getInfo(DICOM\_TAG)](https://imagej.nih.gov/ij/developer/macro/functions.html#getInfo)
-   [getMetadata("Info")](https://imagej.nih.gov/ij/developer/macro/functions.html#getMetadata)

An example using `getInfo()`:

```java
open("http://wsr.imagej.net/images/ct.dcm.zip");
studyDescription = getInfo("0008,1030");
imagePosition = getInfo("0020,0032");
pixelSpacing = getInfo("0028,0030");
print("Study Description: "+ studyDescription);
print("Image Position: "+imagePosition);
print("Pixel Spacing: "+ pixelSpacing);
```
