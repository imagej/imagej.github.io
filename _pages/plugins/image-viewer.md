---
title: Image Viewer
description: utility plugins and macros to control images contast and LUTs
categories: [Annotation, Interactive, Macro, Microscopy, Montage, Utilities, Visualization]
---

This Update Site provides utility plugins and macros to help with handling and visualizing microscopy images before any analysis.     
Features include:

- Plugins to control image contrast and LUTs  
- A neutral Multi Tool for moving image windows and accessory functions  
- Easy opening of images from thumbnail montages  
- Utility macros for multichannel montages and auto-generated scale bars  

Access commands and plugins via the **Plugins > Image Viewer** menu, or the toolbar menu (installable from Image_Viewer_Toolset under the red `>>` menu in the ImageJ window).

---

## Channels and Contrast

This plugin combines "Brightness and Contrast" and "Channels Tool" functionalities to manage visualization of the active image.

You can:
- Adjust channel display range (contrast)
- Change multi-channel display mode: composite, color, or grayscale
- Set active channels
- Use two auto-contrast modes:
  - **Auto:** Uses "Enhance Contrast" with a default of 0.1% saturated pixels (adjustable via "More" button). For stacks, contrast is based on displayed slice only.
  - **Min/Max:** Sets display range to the channel stack's min/max values.
- Interface with **LUTs Manager** to set palettes or favorite LUTs.
- Access more options and utilities for multi-channel images via the "More" button.

shortcuts to "Brightness and Contrast" and "Channels Tool" is available for missing functionality.

---

## LUTs Manager

### Multichannel Palettes
- Create and edit LUT combinations
- Add LUTs by drag-and-drop from **LUTs Finder**
- Change LUT order with the mouse
- Right-click palette to move or remove LUTs
- Empty palette channels default to "Grays"

### LUTs Finder
Scans all LUTs in your ImageJ `luts` folder
You can use the search bar and color buttons to filter the list.  
The Favorite LUTs are stored for future sessions and accessible from the Channels and Contrast plugin.

**Apply a LUT:**  
- Double-click a LUT or press **Enter** to apply to your image

**LUT preview bands:**  
- Check for uniformity in color transitions for good contrast visibility.

**LUT properties:**  
Each LUT comes with an **estimated** description of its properties:

- **Basic:** Identifies classic 'pure' LUTs (Red, Green, Blue, Cyan, etc.).
- **Linear, Non-uniform:** Whether the perceptual brightness progression is linear.
- **Diverging:** Transitions from one color through a neutral midpoint to another color.
- **Isoluminant:** Changes in color but keeps the luminance consistent across the LUT.
- **Cyclic:** If the first and last colors are the same.

---

## Multi Tool

This Tool is a neutral tool but it can performs many actions in ImageJ based on the mouse click, modifier keys (shift, ctrl, alt) and context.
Without any modifier keys: 
- Left click on an image window will just move the window. But you keep the functionality to move and resize any ROI. 

- **No modifier keys:** Left-click moves image window; Or move / resize any ROI.
- **Middle mouse:** Switch multichannel display (composite/color)
- **Ctrl:** Mimic rectangle tool
- **Shift + Alt:** Local auto-contrast via box ROI around click
- **Alt:** Navigate Z (slice/frame) anywhere in image
- **Shift:** Adjust active channel contrast

---

## Preview Opener
This command creates a montage of opened images and saves it in their directory.  
With the **Multi Tool**, middle-click on a montage will open the image under the cursor—making it fast to find images within a folder.

**How to use:**
1. Open the images you want (virtual stacks supported)
2. Adjust display settings.
3. run the command `Create Preview Opener`

**Notes:**
- Montage title must include “Preview Opener” (can add text before/after)
- Keep the Preview Opener file in the images folder

---

## Other Commands

- **Split View:** Quickly create clean multichannel montages
- **Auto Scale Bar:** Estimate and add scale bar. You can adjust the size and hide the text in options.
- **Auto-Contrast** recordable macro commands similar to the Channels and Contrast buttons.

---
## Installation
- in Fiji, add the Image Viewer [Update Site](https://imagej.net/update-sites/following)
- For ImageJ, download this [repository](https://github.com/kwolbachia/Image_Viewer/tree/main) as .zip
