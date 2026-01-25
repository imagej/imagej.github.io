---
title: Image Viewer
description: utility plugins and macros to control images contast and LUTs
categories: [Annotation, Interactive, Macro, Microscopy, Montage, Utilities, Visualization]
---
This Update Site provides utility plugins and macros to help with handling and visualization of microscopy images        
**If you have a question, feedback or a bug to report, you can post it on the [Image.sc](https://forum.image.sc/t/looking-for-testers-channels-contrast-and-luts-manager-plugins/) Forum**

Main Features include:
- Two plugins to control image contrast and LUTs (Look Up Tables)
- A pluginTool called Multi Tool to enhance mouse interactions with image windows
- Utility macros :
	- basic multichannel montages (Split View)
	- auto-generated scale bar
	- A way to open images from thumbnail montages
	- Auto-contrast macros
	- Save all opened images

# LUTs Manager
#### Multichannel Palettes:
- Create and edit LUT sets
- Add LUTs by drag-and-drop from **LUTs Finder**
- Change LUT order with the mouse
- Right-click on palette to move or remove LUTs
- Empty palette channels default to "Grays"
- All created palettes will be easilly accessible from the **Channels and Contrast** plugin! 
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-LUTs-Manager.png?raw=true){:width="700px"}        

#### LUTs Finder
All LUTs in your ImageJ `luts` folder are scanned      
You can use the search bar and color buttons to filter the list       
Favorite LUTs are stored and accessible from the **Channels and Contrast** plugin         
**Apply a LUT:** Double-click a LUT or press **Enter** to apply to your image         
**LUT preview bands:** Check for uniformity in color transitions for good contrast visibility         
**LUT properties:**           
Each LUT comes with an **estimated** description of its properties:         
- **Basic:** Identifies classic 'pure' LUTs (Red, Green, Blue, Cyan, etc.)
- **Linear, Non-uniform:** Whether the perceptual brightness progression is linear
- **Diverging:** Transitions from one color through a neutral midpoint to another color
- **Isoluminant:** Changes in color but keeps the luminance consistent across the LUT
- **Cyclic:** If the first and last colors are the same
- **Luminance values:** Estimation of perceptual luminosity of the LUT min and max colors

# Channels and Contrast
This plugin combines and enhance most imageJ's "Brightness and Contrast" and "Channels Tool" functionalities to manage visualization of the active image       
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Channels-and-Contrast.png?raw=true){:width="600px"}          
You can:
- Change multi-channel display mode: composite, color, or grayscale
- Adjust all channels display range (contrast)
- **Right click on a slider to set value manually**
- Toggle visible channels in composite mode with the checkboxes
- Use two types of auto-contrast:
  - **Auto:** Uses imageJ "Enhance Contrast" command with a default of 0.1% saturated pixels (adjustable from "More" button). For stacks, contrast is based on displayed slice only
  - **Min/Max:** Resets the display range betwin the min and max values of the full channel stack. (this is why it can be a bit slow with huge images)       
- Interface with the **LUTs Manager** to apply LUT palettes or individual favorite LUTs      
You can change order of LUTs in a palette directly with the mouse from the palette menu     
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-CC-palettes.png?raw=true){:width="300px"}     
- Access more options and built-in utilities for multi-channel images via the "More" button     
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-CC-More.png?raw=true){:width="200"}      

# Preview Opener
This command creates a thumbnail montage of opened images and saves it in their directory  
Then the Multi Tool can interact with this montage to open the selected image 
##### **How to use:**
1. Open the images you want (virtual stacks supported) from a single folder
2. Adjust display settings
3. run the command `Create Preview Opener`       
The generated montage will auto-save in the images folder         
NOW! With the **Multi Tool**, double click or middle-click on a thumbnail to open the corresponding image!
         
![Image-Viewer-Preview-Opener](https://github.com/user-attachments/assets/96bcd24a-208d-4628-ad91-884a8d34c5a0){:width="500"}
  
###### **Notes:**
- Keep the Preview Opener file in the images folder
- Montage title must include “Preview Opener” (you can add text before/after)

# Multi Tool
This Tool is a neutral tool with a simple click:
### **Windows**     
- **Move Window:**       
  Left Click and Drag (outside ROI):  Moves the image window position interactively.     
- **Reversible Full Screen:**       
  Double Left Click:  Maximizes the image window, double click again to go back to original size.
                
But it can do **many** actions based on the mouse button, modifier keys (shift, ctrl, alt) and context!
### **Composite Display Switch**     
- **Switch Composite Display:**       
  Middle Click on composite image:  Toggle display mode between Composite and Color.        
### **ROI**     
- **Create Rectangular ROI:**       
  Ctrl + Left Mouse Drag: creates a rectangular selection.      
- **Handle Polygon/Point ROI:**       
  Drag ROI handles using Left Mouse and modify selected selection / points.      
- **Remove ROI:**       
  Ctrl + Click outside the ROI removes the current ROI.     
### **Contrast**     
- **Local Box Auto-Contrast:**       
  Shift + Alt + Left Click (on non-RGB images): Creates a fixed-size box ROI and auto-adjusts contrast in its area.      
  ![Image-Viewer-Local-Auto-Contrast-1](https://github.com/user-attachments/assets/4af5fdae-0f32-4762-957f-18947bf2cda8){:width="600px"}           
- **Live Contrast Adjustment:**       
  Shift + Left Mouse Drag (non-RGB images):  Drag pointer in the image to interactively adjust contrast.        
  ![Image-Viewer-Shift-Contrast](https://github.com/user-attachments/assets/d5f47fc6-9f6d-49e2-a067-8a0075369935){:width="500px"}       
### **Stack Browsing**     
- **Live Scroll through Slices/Frames:**       
  Alt + Left Mouse Drag (on stack/multi-frame images):  Drag horizontally to scroll through slices or frames.     
### **Preview Opener interaction**      
- **Open Image from Preview Opener:**      
  Mouse Over thumbnails will update top left label showing the file name of the selected image.      
  Middle Click on a thumbnail to open the corresponding file.       
  If Caps Lock ON: Opens image as ‘virtual stack’.           

### Multi Tool Shortcuts Summary

| Mouse & Keys       | Action                                          |
|--------------------|------------------------------------------------|
| Left Drag (no ROI) | Move image window                              |
| Double Left Click  | Maximize/minimize image window                 |
| Middle Click       | Composite display toggle / Preview opener open  |
| Ctrl + Left Drag   | Create rectangle ROI                           |
| Ctrl + Click out of ROI  | Remove current ROI                             |
| Shift + Alt + Left Click | Box auto-contrast                  |
| Shift + Left Drag  | Live contrast adjustment             |
| Alt + Left Drag    | Stack/frame scroll                             |    
{:.left}

# Other Commands
A collection of utility macros:
### **Split View:** 
Quickly create clean multichannel montages for up to 5 channels :       
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-SplitView.png?raw=true){:width="500px"}    

### **Auto Scale Bar:** 
Estimate and add scale bar. You can adjust the size and hide the text in options. This macro is adapted from [Aleš Kladnik](https://forum.image.sc/t/automatic-scale-bar-in-fiji-imagej/60774)     

### **Auto-Contrast** 
Recordable macro commands reproducing the **Channels and Contrast** buttons       


# Installation
- in Fiji, add the __Image Viewer__ [Update Site](https://imagej.net/update-sites/following). That's it.
- For ImageJ, download this [github repository](https://github.com/kwolbachia/Image_Viewer/tree/main)       
Then in your imageJ app folder : place the **Image Viewer** folder on the ``plugins`` folder and the **Image_Viewer_Toolset.ijm** file on the ``macros /toolsets/`` folder

All commands and plugins are located in the ``Plugins > Image Viewer`` menu.       
However, The easiest way to access commands is from the toolbar menu you can find as ``Image_Viewer_Toolset`` under the red `>>` menu in the ImageJ window:            
![](https://github.com/imagej/imagej.github.io/blob/main/media/Image-Viewer/Image-Viewer-Toolset.png?raw=true){:width="300px"}    
This will intall a "View" menu in your Toolbar will all Image Viewer commands!     

Note :     
If you like these tools so much you need to get them installed at every starts, just copy this macro code and past it at the end of your 
- `Fiji/macros/StartupMacros.fiji.ijm` for Fiji       
- `ImageJ/macros/StartupMacros.txt` for ImageJ

  
```java
var viewer_Menu = newMenu("Image Viewer Menu Tool",
	newArray( 
		"Channels and Contrast",
		"LUTs Manager",
		"Multi Tool",
		"-",
		"Split View (multi-channel montage)",
		"Auto scale bar",
		"Create Preview Opener",
		"Image Viewer options",
		"-",
		"Auto contrast all images",
		"Auto contrast all channels",
		"Auto contrast active channel",
		"Reset min max all images",
		"Reset min max all channels",
		"Reset min max active channel",
		"Same contrast to all opened images",
		"-",
		"Save all opened images as",
		"Image Viewer online help"
	)
);

macro "Image Viewer Menu Tool - N20C000 T0c15v T8c10i  Tac10e Tfc10w" {
	command = getArgument(); 
	run(command); 
}
```
