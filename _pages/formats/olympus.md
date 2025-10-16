---
title: EvidentImageJPlugin
name: EvidentViewer Plugin
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
nav-links: true
initial-release-date: "Dec. 9, 2015: First version Ver.1.1.1"
release-date: "Jan. 30, 2023: Ver.2.4.1"
team-maintainer: 'EVIDENT CORPORATION (GLOB-SM-imagejplugin at evidentscientific.com)'
---

{% include info-box source='The source code of plugin is in Olympus_Viewer.jar. The source code of native library is not provided.' %}

This plugin can load EVIDENT vsi/oir/omp2info file formats and show some meta data.

## New release 
  Ver.2.4.1 Fix for incorrect colours displayed in some VSI files.

## Download
  Download the latest EvidentViewer ImageJ Plugin for [Windows](https://evidentscientific.com/en/downloads?product=ImageJ&type=Software) and [Mac](https://evidentscientific.com/en/downloads?product=ImageJ&type=Software).

## Installation
  Please see our installation instructions for [Windows](https://github.com/evident-imagejplugin/evident-viewer-guide/blob/main/EvidentViewer_Installation_Guide_win.md) and [Mac](https://github.com/evident-imagejplugin/evident-viewer-guide/blob/main/EvidentViewer_Installation_Guide_mac.md).

## How to use

File Open

1.  Select a menu item {% include bc path="Plugins | OlympusViewer | Viewer" %}
2.  Select a file.

Show Meta Data

1.  Select a menu item {% include bc path="Plugins | OlympusViewer | ShowInfo" %}

Drag & Drop (ver2.1.1-)

1.  Select a menu item {% include bc path="Plugins | OlympusViewer | DragDrop" %}
2.  Drop a image file.

Virtual stack mode for large images (ver2.2.1-)

1.  Select a menu item {% include bc path="Plugins | OlympusViewer | DragDrop | Use Virtual Stack" %} for large images
2.  Drop a image file.

Use Macro function (ver2.3.1-)

1.  Enable Macro Record function.
2.  Select menu item {% include bc path="Plugins | OlympusViewer | Viewer" %}
3.  Select image file.
4.  You can see that Macro command was registered.

## Macro sample code

### Use GUI commands

-   Sample for opening an image:

`run("Viewer", "open=D:/image/test/test.oir");`

- Sample for opening an image which has multiple groups or levels:

`run("Viewer", "open=D:/image/test/test.vsi group1_level1");`

- Sample for opening images in a directory:

```java
input = "D:/image/test/";

list = getFileList(input);
for (i = 0; i < list.length; i++){
	path = input + list[i];
	run("Viewer", "open=[path]");
}
```

-    Sample for batch processing:

```java
setBatchMode(true);

input = "D:/image/test/";

list = getFileList(input);
for (i = 0; i < list.length; i++){
	path = input + list[i];
	run("Viewer", "open=[path]");
	// process image e.g. "run("Smooth", "stack");"
	saveAs("Tiff", "D:/image/test/out_" + i + ".tif");
}
```

### Use programming interface

You can use programming interface by using *OVMacro* command.

-   Sample for opening an image:

```java
run("OVMacro");
Ext.openFile("D:/image/test/test.oir");
```

-   Sample for opening an image which has multiple groups or levels:


```java
run("OVMacro");
Ext.openFile("D:/image/test/test.vsi", 1, 2); // Open Group 2, Level 3
```

-   Sample for opening images in a directory:

```java
run("OVMacro");
Ext.openFolder("D:/image/test"); // You can specify group and level like as openFile
```

-   Sample for getting number of groups and levels:

```java
run("OVMacro");
path = "D:/image/test/test.vsi";
Ext.getGroupCount(path, groupNum); // Get total count of groups
Ext.getLevelCount(path, groupNum-1, levelNum); // Get total count of levels
Ext.openFile(path, groupNum-1, levelNum-1); // Open last level of the last group
```

## See Also

This plugin uses jai-imageio.
