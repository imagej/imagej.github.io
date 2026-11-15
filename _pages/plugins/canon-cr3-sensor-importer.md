---
title: Canon CR3 Sensor Importer
---

Canon CR3 Sensor Importer opens supported Canon RAW and C-RAW files in Fiji. The image
contains one unsigned 16-bit value per sensor site, including the masked sensor
margins. A 14-bit sample retains its original numeric value. This is useful for
measurements that need the Bayer mosaic before cropping, black-level correction
or demosaicing.

## Installation

Use Fiji with Java 21 or later. Choose **Help › Update… › Manage update sites**.
Add an unlisted site named **Canon CR3 Sensor Importer** with this URL. Enable it, apply changes
and restart Fiji.

```text
https://carstenartur.github.io/Photographer/fiji/cr3/
```

## Importing a file

Choose **File › Import › CR3 Sensor Data...** and select a CR3 file.
**Image › Show Info...** displays the camera model and available sensor metadata,
including the Bayer pattern and bit depth. Adjusting brightness and contrast
changes how the mosaic is displayed while preserving the pixel values.

To import a file from an ImageJ macro:

```ijm
run("CR3 Sensor Data...", "path=[/data/capture.cr3]");
```
