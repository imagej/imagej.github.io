---
title: Draw 3D ROI
categories: [3D,Segmentation]
description: How to use the Draw 3D ROI plugin
name: Draw 3D ROI plugin
source-label: Github
source-url: https://github.com/andmccall/Draw3DROI
team-developers: Andrew McCall
---

{% include notice icon="info" content='This plugin is unrelated to the 3D Draw ROI command from [3D ImageJ Suite](/plugins/3d-imagej-suite/index), and is not directly associated with 3D ImageJ suite. 
Despite the similar names 3D Draw ROI and Draw 3D ROI sevre different purposes. 3D Draw ROI takes a mask and creates a 3D outline of the mask shapes, creating the look of a more traditional 2D ROI selection. 
Draw 3D ROI is used to create a 3D mask from several 2D drawn ROIs.' %}

## Draw 3D ROI

This plugin allows users to create a 3D binary segmented mask by hand-drawing 2D ROIs from multiple image perspectives. The 3D binary mask is generated from the intersection of the user provided ROIs. 

## Installing the Plugin:

Availalbe on the list of [ImageJ updates sites](/update-sites/following). Requires Fiji. Will not work with standalone ImageJ1.x or ImageJ2 as it uses elements of both. 

## How to use Draw 3D ROI:

With any z-stack image open in Fiji, including 4D and 5D images, run the plugin found under Plugins > Draw 3D ROI, or search for Draw 3D ROI using the search bar. This plugin requires a z-stack image, if you want to make it work with a 2D time-lapse image you need to change the time-axis to a z-axis under Image > Properties. Upon starting Draw 3D ROI, the interactive plugin window will open along with a working image window. Changing the Display perspectives or projection method will change the display in the working image. Any of the projection methods can be used when working with the plugin, and changes to the perspectives or projection method will **not** clear the current ROI. If you accidentally close the working image, changing the perspective or projection method will bring it back. 

### Setting ROIs

To create a 3D mask, you just need to set an ROI using the "Set perspective's ROI" button for one or more perspectives, though at least two are recommended. **Any of the ImageJ selection tools can be used** to generate the ROIs, with the exception of the straight line tool with a line width of 1 and the multi-point tool. After setting the perspective ROI, the ROI selection will be cleared from the image, but can be retrieved again by clicking the "Get perspective's ROI" button. The "Reset perspective's ROI" button can be used to reset the ROI to the default ROI, which is the full image from that perspective (equivalent to the Select All command). This allows the user to modify existing perspective's ROI's if the preview looks incorrect (discussed below). This is generally best done by using easily-modifiable ROI tools (like the polygon tool) and clicking the Get then Reset buttons before adjusting the ROI. 

{% include img align="right" name="Draw 3D ROI plugin" src="draw3droi-mainwindow" %}

### Previewing your mask

The preview checkbox can be used to turn on and off a preview of the 3D mask. When turned on, this adds an additional channel to the working image, allowing users to evaluate exactly where the output mask will be generated relative to their data. The working image, including the preview channel, can be adjusted using Image > Adjust > Brightness/Contrast... or Image > Color > Channels Tool... to change the display to your preference. At this moment, any changes to the display perspective, projection method or preview checkbox will reset any of these changes to the image display, though I hope to change this in the future. 

The preview channel data will be projected using the selected projection method in the same way as any other data. The downside of this is that the preview will not necessarily be visible for every projection method, in particular median and occasionally variance can not show anything at all in the preview channel depending on the currently set perspective ROIs. The upside is that the preview can give a better indication of the overall 3D shape depending on the preview channel intensity and the projection method. 

For large images, generating the preview channel can take a very long time. For these images, it is recommended to either use the preview option sparringly, such as after all three perspective' ROIs have been set, or downsample the image (using Image > Adjust > Size or Image > Transform > Bin) prior to running Draw 3D ROI, then scaling the exported 3D mask back to full size after export. The data for the preview channel is only generated when the preview checkbox is initially checked, or if a perspective's ROI is changed, using Set or Reset, while the preview is turned on. 

### Exporting the mask

Once you have set your perspective ROIs, and likely verified the mask using the preview function, you can simply click the "Create 3D mask" button to generate a new segemented binary mask image. This output mask will have exactly 3 dimensions, even for 5D input images. Creating the output mask does not close Draw 3D ROI, so if you are unhappy with the mask, you can modify any perspective's ROI and re-export. 

Draw 3D ROI has no additional functionality after generating this mask. Once it's created you can use your favorite 3D processing and analysis tools, such as [MorphoLibJ](/plugins/morpholibj) or [3D ImageJ Suite](/plugins/3d-imagej-suite), to utilize the mask. 

## Additional Tips

### Using other plugins and commands
When clicking the "Set" and "Get" buttons, Draw 3D ROI will work with the currently active window, not specifically the working image. This means that you can use any tools available to you in Fiji to generate the 2D ROI to be passed into Draw 3D ROI. You can even create a 2D mask from a projection (e.g. using Image > Adjust > Threshold), then go to Edit > Selection > Create Selection to turn that mask into a selection and "Set" that as the ROI. The most important thing when doing this is that the "Display perspective" option is set correctly based on the image you are working with, and that the processed image has not been transformed in any way, as Draw 3D ROI does not check for this. 

### Modifying a freehand selection
If you created a freehand selection and are not happy with it, you can use Edit > Selection > Fit Spline to change it into a polygon selection, which you can then modify and "Set".

### Using ROI Manager
ROI manager can be used to create multiple objects in your exported mask. You can do this by adding as many selections to the manager as usual, then select all of those selections in the list, and click More >> OR (Combine). This will create one selection from all of those, and then click "Set". This can be a challenge if you are using ROI manager for multiple perspectives, as you'll need to keep track of which persepctive each ROI in the list is for. Additionally, the "Get" button will not be as useful, as it does not return these ROIs to the ROI manager and these multi-element ROIs are not as easy to manipulate, though some functions in the Edit > Selection menu do work.
