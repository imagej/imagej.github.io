---
mediawiki: Cell_Counter
title: Cell Counter
project: /software/fiji
categories: [Particle Analysis]
artifact: sc.fiji:Cell_Counter
---

This plugin will open a new cell counter GUI. On the left are the counter types and counters, on the right the action buttons.

{% include notice icon="info" content='Please consider using the built-in [Multi-Point Tool](https://imagej.nih.gov/ij/docs/guide/146-19.html#sec:Multi-point-Tool) in ImageJ, as this tool now replicates most of the functionality of Cell Counter.' %}

## Bugs

May not work correctly after using **Load Markers** to load more than 8 counter types from an XML file. Opens off-screen on 1024 pixel wide and smaller monitors.

## Functions

-   **Initialize:** Initializes the current image or stack for counting, this will create a duplicate image/stack titled "counter window" - when keep original is checked, the source image remains open
-   **Add:** adds a counter type.
-   **Remove:** removes the last counter type.
-   **Delete mode:** toggles between insert and delete mode. When checked, the marker of the currently selected type closest to the mouse cursor will be deleted when you click.
-   **Delete:** delete the last placed marker.
-   **Reset:** reset all counters to 0.
-   **Results:** Shows the counter results in the ImageJ results table. In case of a stack the counts per slice and the totals are displayed.
-   **Save Markers:** Exports the marker data to an XML file - Only available when running java 1.4 or higher
-   **Load Markers:** Loads stored marker data from an XML file - - Only available when running java 1.4 or higher
-   **Export Image:** Makes a copy of the counter image with the markers written on it (only the current slice is copied in case of a stack)
-   **Measure...:** Measures the pixel value at each marker and displays a result window showing: Type - Slice - X coordinate - Y coordinate - Pixel Value

## Usage

Open the Cell Counter plugin and the image/stack you want to count (if the Cell Counter plugin is already open you don't need to open a new instance). Click initialize, now you are ready to count features. Note that at any time you can add types or remove them. Select the type you want to count, and count by clicking on the feature in the image. A colored number corresponding to the type you are counting will be displayed on the image every time you click, and the corresponding counter is updated.

Add the following macros to *ImageJ/macros/StartupMacros.txt*, restart ImageJ, and you will be able to change the counter type by pressing "1", "2", "3", etc.

```
macro "Type 1 [1]" {call("CellCounter.setType", "1");}
macro "Type 2 [2]" {call("CellCounter.setType", "2");}
macro "Type 3 [3]" {call("CellCounter.setType", "3");}
macro "Type 4 [4]" {call("CellCounter.setType", "4");}
macro "Type 5 [5]" {call("CellCounter.setType", "5");}
macro "Type 6 [6]" {call("CellCounter.setType", "6");}
macro "Type 7 [7]" {call("CellCounter.setType", "7");}
macro "Type 8 [8]" {call("CellCounter.setType", "8");}
```

## History

-   <u>2001/10/17</u>: first version
-   <u>2002/02/01</u>: bug fixes
-   <u>2004/06/26</u>: upgraded to work with ImageJ 1.32
-   <u>2005/12/27</u>: version 2
-   <u>2006/02/02</u>: No longer requires Java 5.0
-   <u>2006/02/14</u>: Added "Save Markers" and "Load Markers" buttons
-   <u>2006/03/06</u>: Added "Export Image" and "Measure" buttons
-   <u>2006/03/12</u>: Add "Show Numbers" checkbox
-   <u>2008/02/29</u>: Updated to work with [Grid](https://imagej.nih.gov/ij/plugins/grid.html) plugin
-   <u>2008/08/27</u>: Added "Show All" checkbox; works with hyperstacks and composite color images
-   <u>2008/09/02</u>: Added setType() method to support macros
-   <u>2008/09/22</u>: Out of focus markers displayed as outlines
-   <u>2009/07/01</u>: Fixed "Load Markers" bug
-   <u>2010/12/07</u>: Uses less memory

 
