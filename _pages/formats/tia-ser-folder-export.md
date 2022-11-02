---
title: TIA .ser folder export
nav-links: true
---

## **Overview**

This tool converts TIA EM image .ser files in a folder to TIFF images.

Newly updated \[TEM\_ser\_dm3\_batch\_convert\] tool now also support Gatan .dm3 batch convert, including a mixture of .ser and .dm3 files in the same folder.

Scale info of TEM images is also exported as HFW (Horizontal Full Width) in the file name.

## **Dependency**

[TIA reader](https://imagej.nih.gov/ij/plugins/tia-reader.html).

Please follow the instruction in the webpage above to install the plugin before using this script.

While Steffen has done a great job in decoding the .ser files in imageJ, the batch processing function does not seems working very well for folder exporting .ser into .tif files. Because the .ser files are always in the same folder with associated .emi files where stores the acquisition metadata. When using the original TIA reader with ImageJ batch convert, it generates error msg every time when a .emi is read. The current script will filter other file formats in the folder.

## **Known Issue**

Scale info export does not work correctly for diffraction patterns.
