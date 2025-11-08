---
title: Image Viewer
description: utility plugins and macros to control images contast and LUTs
categories: [Annotation, Interactive, Macro, Microscopy, Montage, Utilities, Visualization]
---
This Update Site provides utility plugins and macros to help with handling and visualization of microscopy images

Features include:
- Two plugins to control image contrast and LUTs (Look Up Tables)
- A pluginTool called Multi Tool to enhance mouse interactions with image windows
- Utility macros :
	- basic multichannel montages (Split View)
	- auto-generated scale bar
	- A way to open images from thumbnail montages
	- Auto-contrast macros
	- Save all opened images

# Installation
- in Fiji, add the __Image Viewer__ [Update Site](https://imagej.net/update-sites/following)
- For ImageJ, download this [github repository](https://github.com/kwolbachia/Image_Viewer/tree/main)       
In your imageJ app folder : place the **Image Viewer** folder on the ``plugins`` folder and the **Image_Viewer_Toolset.ijm** file on the ``macros /toolsets/`` folder

All commands and plugins are located in the ``Plugins > Image Viewer`` menu       
But the easiest way is to install the toolbar menu from Image_Viewer_Toolset under the red `>>` menu in the ImageJ window            
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Toolset.png?raw=true)     
If you have a question, feedback or a bug to report, you can post it on the [Image.sc](https://forum.image.sc/t/looking-for-testers-channels-contrast-and-luts-manager-plugins/) Forum

___

### Channels and Contrast
This plugin combines imageJ's "Brightness and Contrast" and "Channels Tool" functionalities to manage visualization of the active image       
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Channels-and-Contrast.png?raw=true)     
You can:
- Change multi-channel display mode: composite, color, or grayscale
- Adjust all channels display range (contrast)
- Toggle visible channels in composite mode (checkboxes)
- Use two types of auto-contrast:
  - **Auto:** Uses imageJ "Enhance Contrast" command with a default of 0.1% saturated pixels (adjustable via "More" button). For stacks, contrast is based on displayed slice only
  - **Min/Max:** Sets display range to the channel stack's min/max values
- Interface with the **LUTs Manager** to apply LUT palettes or individual favorite LUTs
You can change order of LUTs in a palette directly with the mouse from the palette menu     
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-CC-palettes.png?raw=true)     
- Access more options and built-in utilities for multi-channel images via the "More" button     
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-CC-More.png?raw=true)     

### LUTs Manager
#### Multichannel Palettes
- Create and edit LUT sets
- Add LUTs by drag-and-drop from **LUTs Finder**
- Change LUT order with the mouse
- Right-click on palette to move or remove LUTs
- Empty palette channels default to "Grays"     
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-LUTs-Manager.png?raw=true){:width="400px"}         
#### LUTs Finder
The plugin scans all LUTs in your ImageJ `luts` folder
You can use the search bar and color buttons to filter the list
The Favorite LUTs are stored and accessible from the Channels and Contrast plugin
**Apply a LUT:**  
- Double-click a LUT or press **Enter** to apply to your image
**LUT preview bands:**  
- Check for uniformity in color transitions for good contrast visibility
**LUT properties:**  
Each LUT comes with an **estimated** description of its properties:
- **Basic:** Identifies classic 'pure' LUTs (Red, Green, Blue, Cyan, etc.)
- **Linear, Non-uniform:** Whether the perceptual brightness progression is linear
- **Diverging:** Transitions from one color through a neutral midpoint to another color
- **Isoluminant:** Changes in color but keeps the luminance consistent across the LUT
- **Cyclic:** If the first and last colors are the same
- **Luminance values:** Estimation of perceptual luminosity of the LUT min and max colors

### Multi Tool
This Tool is a neutral tool 
but it can perform many actions based on the mouse button, modifier keys (shift, ctrl, alt) and context:
- **Without modifier keys:** Left-click moves image window; Or move / resize any ROI     
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Default-Main-Tool.mp4" %}  
- **Middle mouse:** Switch multichannel display (composite/color)
- **Ctrl:** Mimic rectangle tool     
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Ctrl-Rectangle.mp4" %}       
- **Shift + Alt:** Local auto-contrast via box ROI around click     
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Local-Auto-Contrast.mp4" %}       
- **Alt:** Navigate Z (slice/frame) anywhere in image     
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Alt-Slice.mp4" %}       
- **Shift:** Adjust active channel contrast     
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Shift-Contrast.mp4" %}      
### Preview Opener
This command creates a montage of opened images and saves it in their directory.  
**How to use:**
1. Open the images you want (virtual stacks supported)
2. Adjust display settings
3. run the command `Create Preview Opener`
{% include video src="https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Preview-Opener-.mp4" %}       
With the **Multi Tool**, middle-click on a montage will open the image under the cursor—making it fast to find images within a folder
**Notes:**
- Montage title must include “Preview Opener” (you can add text before/after)
- Keep the Preview Opener file in the images folder
### Other Commands
A small collection of utility macros:
- **Split View:** Quickly create clean multichannel montages       
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-SplitView.png?raw=true){:width="400px"}    

- **Auto Scale Bar:** Estimate and add scale bar. You can adjust the size and hide the text in options. This macro is adapted from [Aleš Kladnik](https://forum.image.sc/t/automatic-scale-bar-in-fiji-imagej/60774)     
- **Auto-Contrast** recordable macro commands similar to the Channels and Contrast buttons
