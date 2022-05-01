---
mediawiki: DICOM_open
title: DICOM open
categories: [Import-Export]
---

{% include info-box software='ImageJ 1.x' name='DICOM\_open' author='Fred Damen' filename='DICOM\_open.jar' source=' [DICOM\_open.zip](/media/plugins/dicom-open.zip)' released='1 April 2019' status='stable' category='Import-Export' website='' %}

The DICOM\_open plugin provides additional functionality on top of the DICOM plugin. There were three main impetuses for developing this plugin, first was to be able to search the DICOM files for a series to open, second was to open the series and get at the actual voxel data, and, third was to properly arrange the images in a hyperstack.

DICOM datasets, that I generally come across, are stored in a hierarchical directory structure in which the directory names do not enlighten the content. The DICOM files are database entries, and the parameters within hold the clues to which datasets may be desired. This plugin's GUI provides an interactive interface to find the series of interest to open. For dealing with a single hodgepodge directory of DICOM files, see included DICOM\_explode plugin.

MRI DICOM dataset's voxel data tends to be stored as 16 bit unsigned integers, i.e., magnitude data, albeit, the tags within the DICOM files say they are signed. ImageJ does not support signed 16 bit image data. For some reason, they add 32768 to the dataset voxel values and store them in unsigned 16 bit integer ShortProcessor(s); confusing to say the least. This plugin provides the means to access the voxel data as someone who deals with MRI data would expect.

The DICOM datasets that I open in ImageJ, contain multiple volumes, where each volume was acquired under slightly different conditions, e.g., multi b-value diffusion. DICOM\_explode plugin can sort a DICOM dataset into a top down properly sorted hyperstack, suitable for processing see F\_Project plugin.

## Features

![](/media/plugins/dicom-open.jpg)

When run as a plugin the plugin will first present a directory browser to select the parent directory of where to start the DICOM dataset search, and then, present this GUI. At the top is the directory of the currently selected item.The second line presents a Pulldown to select an item under the currently selected item. Select an item to display information about the item below the Pulldown. The 'Load Series' button at the bottom is only available when the current item is a series.

If the DICOM series is a multi b-value diffusion dataset then use the Pulldown to select the appropriate type `Trace`, `R/L`, `A/P`, `S/I`; DTI is not supported. Supported vendors (0008,0070) are `GE MEDICAL SYSTEMS` and `SIEMENS`. Otherwise, if the DICOM series was acquired whilst varying a DICOM tag value, enter the DICOM tag and a variable name to be used in the slice's short label. Neither of these fields are required.

The `Float` format causes the voxel values to be the same as in the DICOM dataset, albeit, in 32-bit FloatProcessor format. The `Scaled` format causes the FloatProcessor values to be scaled according to the linear rescale (0028,1053) and intercept (0028,1052). The **16-bit fixed** format causes the FloatProcessor values to be directly converted to short(s) and placed in a ShortProcessor, (i.e., Java: (short)floatvalue; not: (ShortProcessor)FloatProcessorValue, n.b., the (ShortProcessor) conversion rescales). The **16-bit broken** format is as the DICOM plugin imported.

## Methods

```java
public static boolean isDICOM(File file)
```
Does the file have the proper magic number (`DICM`).

```java
public static TreeMap<String,String> parseDICOM(ImagePlus imp, int s)
```
Return the DICOM tag/value mappings in easy to use format. The slice `s` is as returned by `ImagePlus.getStackIndex`.

```java
public static ImagePlus openDICOMFloat(File dfs)
public static ImagePlus openDICOMFloat(File[] dfs)
public static ImagePlus openDICOMScaled(File dfs)
public static ImagePlus openDICOMScaled(File[] dfs)
public static ImagePlus openDICOMShort(File dfs)
public static ImagePlus openDICOMShort(File[] dfs)
public static ImagePlus openDICOM(File dfs, String format)
public static ImagePlus openDICOM(File[] dfs, String format)
```
These methods open a DICOM dataset. All but the last one are convenience methods that call the last one. The DICOM dataset is not yet sorted. With `File dfs`, `dfs` can be either the parent directory of the DICOM files or a single DICOM file. For `File[] dfs`, `dfs` should be an array of DICOM files.

```
public static ImagePlus openDICOMDiff(File dfs, String format, String reqdirstr)
```
Opens a multi b-value diffusion dataset, whilst ignoring the spacial directions that are not `reqdirstr`. `reqdirstr` is one of `Trace`,`R/L`,`A/P`,`S/I`.

```java
public static ImagePlus volumeDICOM(ImagePlus imp)
```
Sorts the DICOM `imp` assuming there is only one volume.

```java
public static ImagePlus arrayDICOM(ImagePlus imp, String tag, String var)
```
Sorts DICOM `imp` into a hyperstack assuming `imp` was collected by varying the DICOM `tag` property. The string `var` is used in conjunction with the DICOM `tag`'s value to set each slice's label.

```java
public static ImagePlus[] diffusionDICOM(ImagePlus imp) throws Exception
```
Sorts a multi b-value diffusion dataset into a array of 4 hyperstacks, one array element for each of `Trace`,`R/L`,`A/P`,`S/I`. Only the array elements that existed in imp are filled in.

```java
public static double[] getArray(ImagePlus imp, int s, String tag)
public static double getDouble(ImagePlus imp, int s, String tag)
public static int getInt(ImagePlus imp, int s, String tag)

// Convenience methods to access DICOM tag values for a slice s. The slice s is as returned by ImagePlus.getStackIndex.
public static String getTagValue(ImagePlus imp, int s, String tag)
public static String getTagLine(ImagePlus imp, int s, String tag) 
```

## Install

Unzip [DICOM\_open.zip](/media/plugins/dicom-open.zip) into ImageJ 1.x plugins {% include bc path="File|Show Folder|Plugins" %} or `plugins`/`jars` directories. Source code in jar file. `DICOM_explode` is included.

## Licence

GPL distribution licence.

## ChangeLog

1 April 2019 Initial version.

## Known Bugs

Let me know.
