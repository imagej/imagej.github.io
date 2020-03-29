{{FormatsMenu}}{{Infobox
| software               = ImageJ
| name                   = OlympusViewer Plugin
| author                 = OLYMPUS CORPORATION (olympus-imagejplugin at ot.olympus.co.jp)
| maintainer             = 
| filename               = 
| source                 = The source code of plugin is in Olympus_Viewer.jar. The source code of native library is not provided.
| released               = Dec. 9, 2015: First version Ver.1.1.1
| latest version         = Mar. 17, 2020: Ver.2.3.1
| status                 = 
| category               = [[:Category:Import-Export]]
| website                = 
}}This plugin can load Olympus vsi/oir/omp2info file formats and show some meta data.

{{TOC}}
== Installation ==
Please see also [http://www.olympus-lifescience.com/OlympusImageJPlugin/HowToInstallOlympusViewerPlugin installation manual].

Windows
# Download OlympusViewer-win.zip [http://www.olympus-lifescience.com/OlympusImageJPlugin/OlympusViewer_Win here]
# Extract the zip file.
# Execute OlympusViewer-win.exe. This file is in self-extracting format.
# If you agree to our end user license agreement, extract it to your specified folder.
# Unzip the OlympusViewer-package.zip
# Install vs2017 runtime if the runtime is not installed in your PC. The runtime is in OlympusViewer-package/WinRuntime. If you use 32bit OS, install VC_redist.x86.exe. If you use 64bit OS, install VC_redist.x64.exe
# Copy "OlympusViewer" folder in "OlympusViewer-package" folder to the plugins folder of your ImageJ directory. If ImageJ plugin folder already has OlympusViewer folder, delete the folder before copying.
Mac
# Download OlympusViewer-mac.dmg [http://www.olympus-lifescience.com/OlympusImageJPlugin/OlympusViewer_Mac here]
# Double click the dmg file.
# If you agree to our end user license agreement, extract it.
# Copy "OlympusViewer-Ver2.3.1" folder to the plugins folder of your ImageJ directory. If ImageJ plugin folder already has OlympusViewer folder, delete the folder before copying.
== How to use ==
File Open
# Select a menu item ( Plugins -> OlympusViewer -> Viewer )
# Select a file.
Show Meta Data
# Select a menu item ( Plugins -&gt; OlympusViewer -&gt; ShowInfo )
Drag & Drop (ver2.1.1-)
# Select a menu item ( Plugins -&gt; OlympusViewer -&gt; DragDrop )
# Drop a image file.
Virtual stack mode for large images (ver2.2.1-)
# Select a menu item ( Plugins -&gt; OlympusViewer -&gt; DragDrop -&gt; Use Virtual Stack for large images )
# Drop a image file.
Use Macro function (ver2.3.1-)
# Enable Macro Record function.
# Select menu item ( Plugins -> OlympusViewer -> Viewer )
# Select image file.
# You can see that Macro command was registered.
== Macro sample code ==
=== Use GUI commands ===
* Sample for opening an image:
<source lang="plain">
run("Viewer", "open=D:/image/test/test.oir");
</source>
* Sample for opening an image which has multiple groups or levels:
<source lang="plain">
run("Viewer", "open=D:/image/test/test.vsi group1_level1");
</source>
* Sample for opening images in a directory:
<source lang="plain">
input = "D:/image/test/";

list = getFileList(input);
for (i = 0; i < list.length; i++){
	path = input + list[i];
	run("Viewer", "open=[path]");
}
</source>
* Sample for batch processing:
<source lang="plain">
setBatchMode(true);

input = "D:/image/test/";

list = getFileList(input);
for (i = 0; i < list.length; i++){
	path = input + list[i];
	run("Viewer", "open=[path]");
	// process image e.g. "run("Smooth", "stack");"
	saveAs("Tiff", "D:/image/test/out_" + i + ".tif");
}
</source>

=== Use programming interface ===
You can use programming interface by using ''OVMacro'' command.
* Sample for opening an image:
<source lang="plain">
run("OVMacro");
Ext.openFile("D:/image/test/test.oir");
</source>
* Sample for opening an image which has multiple groups or levels:
<source lang="plain">
run("OVMacro");
Ext.openFile("D:/image/test/test.vsi", 1, 2); // Open Group 2, Level 3
</source>
* Sample for opening images in a directory:
<source lang="plain">
run("OVMacro");
Ext.openFolder("D:/image/test"); // You can specify group and level like as openFile
</source>
* Sample for getting number of groups and levels:
<source lang="plain">
run("OVMacro");
path = "D:/image/test/test.vsi";
Ext.getGroupCount(path, groupNum); // Get total count of groups
Ext.getLevelCount(path, groupNum-1, levelNum); // Get total count of levels
Ext.openFile(path, groupNum-1, levelNum-1); // Open last level of the last group
</source>

== See Also ==
This plugin uses jai-imageio.
[[Category:Plugins]]
[[Category:Import-Export]]
