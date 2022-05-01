---
title: OlympusImageJPlugin
section: Learn:ImageJ Basics:File Formats
categories: [Import-Export]
---

{% include info-box software='ImageJ' name='OlympusViewer Plugin' author='OLYMPUS CORPORATION (olympus-imagejplugin at ot.olympus.co.jp)' source='The source code of plugin is in Olympus_Viewer.jar. The source code of native library is not provided.' released='Dec. 9, 2015: First version Ver.1.1.1' latest-version='Mar. 17, 2020: Ver.2.3.1' %}

This plugin can load Olympus vsi/oir/omp2info file formats and show some meta data.

## Installation

Please see also [installation manual](http://www.olympus-lifescience.com/OlympusImageJPlugin/HowToInstallOlympusViewerPlugin).

Windows

1.  Download OlympusViewer-win.zip [here](http://www.olympus-lifescience.com/OlympusImageJPlugin/OlympusViewer_Win)
2.  Extract the zip file.
3.  Execute OlympusViewer-win.exe. This file is in self-extracting format.
4.  If you agree to our end user license agreement, extract it to your specified folder.
5.  Unzip the OlympusViewer-package.zip
6.  Install vs2017 runtime if the runtime is not installed in your PC. The runtime is in OlympusViewer-package/WinRuntime. If you use 32bit OS, install VC\_redist.x86.exe. If you use 64bit OS, install VC\_redist.x64.exe
7.  Copy "OlympusViewer" folder in "OlympusViewer-package" folder to the plugins folder of your ImageJ directory. If ImageJ plugin folder already has OlympusViewer folder, delete the folder before copying.

Mac

1.  Download OlympusViewer-mac.dmg [here](http://www.olympus-lifescience.com/OlympusImageJPlugin/OlympusViewer_Mac)
2.  Double click the dmg file.
3.  If you agree to our end user license agreement, extract it.
4.  Copy "OlympusViewer-Ver2.3.1" folder to the plugins folder of your ImageJ directory. If ImageJ plugin folder already has OlympusViewer folder, delete the folder before copying.

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
