---
title: Dorsal Horn Mapping
descrpition: An intitive plugin to map cell location inside murine dorsal horn laminae.
source-url: https://sites.imagej.net/ReferenceFrameToolkit/  
github: https://github.com/LucasRoettger/Dorsal-Horn-Mapping
---

# Description
A plugin aimed at harmonizing the reporting of location information of murine neurons inside the dorsal horn laminae. This plugin can be used on any images of murine spinal cord slices which fullfill the following critieria:
1. The outline of the dorsal horn must be visible
   * Via a channel with a brightfield-image of your slice
   * Via a clearly visible outline of the dorsal horn's autofluorescent signal in at least one fluorescent channel
2. Cells inside at least one of the channels have to be clearly visible and be marked as ROIs inside the ROI-Manager

The plugin allwos to sort the cells into different groups (see below), it can also handle pre-sorted cells (use the ROI-Groups)

# How to install
Install the plugin directly via the FIJI update site. In FIJI’s main window choose 'Help>Update', then wait for the ImageJ Updater to open.  
Click “Manage Update Sites”, then “Add unlisted Site”. Scroll down to “Dorsal Horn Mapping” and tick the box on the left. Click “Apply and Close” then click “Apply Changes” in the ImageJ Updater.  
After you restart FIJI, you find the plugin under 'Plugins>Dorsal Horn Mapping'.

# How to use
1.	Once the Plugin is installed open the first image you want to analyze. Open a set of ROIs that mark cells in that image or mark the cells manually as ROIs. You must have at least one ROI in the ROI-manager.

  * To test the plugin, just use our test-image and ROI-set:
  * Load it via 'Plugins>Dorsal Horn Mapping>Example_Dataset' and proceed
2.	Start the Plugin (Plugins>Dorsal Horn Mapping>Mapping). The main window of the plugin will open.
3.	In the first line of the main window, select the spinal cord segment.

Note: You can always change the segment if you are not sure. Just select another segment from the drop-down menu or with the arrow buttons. Any adjustments you have already made will be applied to the new segment. If you want to start all over, use the “Reset” button at the bottom of the main window.

4.	Use the sliders to align the outline of the frame to the dorsal horn. If the image shows a left dorsal horn, use the “Flip image”-button to mirror the image along with the cell-ROIs.

5.	(Optional) If you have used several stains in one experiment, you might want to sort the cells into groups. You can do that either before executing the plugin using FIJIs prebuild ROI-groups or you can use the grouping feature of our plugin. At any point during the execution of the plugin you can click the “Group Cells”-button. 

  i.	A new window will open showing a crop of one cell at a time in each channel of the image. Below you see a bar with the ten possible groups you can sort the cell into (zero through nine) with the current group selected.
  ii.	Use your mouse on the bar or the number key on your keyboard (not the number pat) to assign a group of your choosing.
  iii.	Use the arrow buttons at the bottom of the window or the arrow keys on your keyboard to navigate through the cells.
  iv.	Click the “Finish”-button once you are done to close the window and return to the main window.
6.	(Optional) Select your export options. Tick or untick any options to fit your preferences.
  i.	“Export .xls-file”: The data will be saved as a two-page XLS-Spreadsheet. The first page contains the data corresponding to the cells (ROI ID, Coordinates (X, Y), cell group, “normal” coordinates (Rx, Ry), lamina and segment), the second page contains the transformations applied to the respective frame (Translation (X, Y), rotation, scaling (in X and Y direction)) for later reference and reproducibility.

  ii.	“Export .csv-file”: The data will be saved as two CSV-Files. The first contains the data corresponding to the cells (ROI ID, Coordinates (X, Y), cell group, “normal” coordinates (Rx, Ry), lamina and segment), the second contains the transformations applied to the respective frame (Translation (X, Y), rotation, scaling (in X and Y direction)) for later reference and reproducibility.

  iii.	“Save flattened RGB-image”: Saves a PNG-copy of the image you are currently working in with all active ROIs and the transformed frames superimposed on it for later reference or data presentation.

  iv.	“Save grouped ROIs”: If you used the “Group Cells”-feature (Step 5), this option will save a copy of the ROIs in the ROI-Manager with the groups you assigned.

Note: The plugin will save any data you selected in the folder you loaded the image from.

7.	Click the “Finish”-Button to start the analysis process. You will be shown a data-table with all cell coordinates and additional data as outlined above. Everything you selected will be saved automatically. You can now close the image and delete the contents of the ROI-Manager.
8.	(Optional) You can directly proceed to analyze another image. To do so:
  i.	Open the image in FIJI or select it if it is already open.
  ii.	Load the respective ROI-set for this image, or mark ROIs.
  iii.	Press the “Reset”-Button on the bottom of the main window to start the process from Step 3.

# Plotting your Data

## Plotting via the inbuild plotting function
Open the Plotter-feature ('Plugins> Dorsal Horn Mapping>Plotter').
  i.	Select a folder that contains at least one of the XLS-spreadsheets (CSV does not work) created by the Plugin.
  
  ii.	Select the plotting mode:
    (1)	“By Segment”: Plots one overlay per segment found in all input data (i.e. one overlay for L1, one overlay for L3 if the input data contains only data from L1 and L3).    
    (2)	“By Image”: Plot the data for each analyzed image separately – handy for troubleshooting and outlier-search.

## Plotting via a third party script
Scripts with similar fuctions for plotting the overlays in R or MATLAB can be found on our [GitHub](https://github.com/LucasRoettger/Dorsal-Horn-Mapping).

# Source
(in print)
