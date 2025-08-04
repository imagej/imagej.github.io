---
title: FRAP Tools
description: FRAP Tools is a set of scripts for (1) Generating and saving FRAP data from an image stack and (2) display of saved data using either built-in ImageJ plot functions or the JFreeChart library.
categories: [Analysis]
release-date: August 1 2025
release-version: 1.0
dev-status: Active
support-status: Active
team-founders: "@jdhardin"
team-maintainers: "@jdhardin"
---

## Overview
FRAP Tools is a set of scripts for (1) generating and saving FRAP data from an image stack and (2) display of saved data using either built-in ImageJ plot functions or the JFreeChart library.

**Rationale**: 1. There are many options for FRAP analysis, but most are not integrated into Fiji/ImageJ.
2. There are relatively few options for semi-automated pooling of individual FRAP experiments and curve-fitting of pooled data.
3. Plot functions in ImageJ are powerful, but the resulting plots are bitmaps. Adding JFreeChart plot options allows saving as .SVG files.

***FRAP Analysis***:
FRAP Analysis is a .py script inspired by hackathon code avaialble 
[here:](https://imagej.net/tutorials/analyze-frap-movies).
This script automates locating the bleach timepoint and trimming fluorescence recovery after photobleaching (FRAP) experimental data, and then allows analysis of the recovery kinetics.

FRAP Analysis uses the double normalization method outlined in:
Phair RD, Gorski SA, Misteli T. (2004). Measurement of dynamic protein binding
to chromatin in vivo, using photobleaching microscopy. Methods Enzymol. 375:393-414.
doi: 10.1016/s0076-6879(03)75025-3. PMID: 14870680.
This normalization method relies on a non-FRAPed region containing signal, a second region containing non-bleached actual signal, and a third containing background signal. It assumes an image stack is open containing a FRAP experiment and three ROIs saved in the ROI Manager. Options are provided for automatically saving the data for a given dataset in a folder, saving a snapshot image with ROIs, and there are various options provided for how curve fitting is done. The resulting data can be plotted using the provided plotting scripts. 

***FRAP Plotting Scripts***:
Scripts are provided for plotting (a) single FRAP experiments (which may or may not contain a curve fit) using built-in ImageJ plot functions or JFreeChart; (b) similar generalized scripts for plotting data in .CSV files that may be useful for other purposes; and (c) scripts for combining multiple FRAP experiments so that they can be plotted on the same plot, mean +/- SEM/SD recovery data can be calculated/plotted, and a recovery curve fit of the pooled data can be generated and plotted. 

Resulting output from the "FRAP Analysis" and "Combine_FRAP_data..." scripts can be easily imported into other programs.

## Installation in Fiji
Add the FRAP-Tools update site using the Fiji update sites manager. After updating, seven new menu itms will be added to Fiji bin the submenu "FRAP" in the "Analyze" menu:

## Usage
***FRAP Analysis***

1. With the desired ImageStack open, create a ROI containing the FRAP region. Add it to the ROI Manager by typing "t", which will open the ROI Manager.
Alternatively, use the menu command "Analyze->Tools->"ROI Manager..." to open it and click the "Add" button. Repeat for a region containing signal but which was not photobleached, and for a region containing no signal (a background region). The ROI Manager should now contain three and only three ROIs saved in the specified order.
2. Invoke the "Analyze->FRAP->"FRAP Analysis" script.
3. A dialog box with options will appear, allowing you to set options:
a. Curve fitting method: Single or double exponential recovery can be selected.
b. Force curve fit through origin for single exponential: in theory, the curve should pass through x = 0 (first time point after bleach) and the minimum signal (y). This may or may not give the best overall fit to the recovery curve.
c. Stretch intensities to full range (0-1): normalizes the range to 0 (immediately post-bleach) to 1 (average signal pre-bleach).
d. Time interval: different platforms with different metadata (or no such data) are not parsed; instead, the time interval is manually entered here. 
e. Create image with ROls: creates a snapshot image with the three ROIs for future reference. Note: ROIs can also be re-loaded from a saved ROI .ZIP file later if this was saved.
f. Autosave settings: the results can be saved to a folder and the windows closed after each run to reduce clutter and tedium.
4. Click "OK" to run the analysis. If "Autosave" options were selected, plot and analysis windows will be closed and the data saved to a folder with the name  (Image name) + "-FRAP". If this folder already exists, you will be asked if you want to overwrite it.

***Import FRAP data and plot Jython*** and ***Import FRAP data and plot JFree***

1. Invoke the "Analyze->FRAP->"Import FRAP data and plot Jython" (or "...JFree") script. The script will open a recovery curve dataset or a recovery curve with a second set of XY columns that contains the fitted curve.
2. Multiple FRAP data files can be selected in the File opener dialog; the script will open all files and plot them individually.
3. Select the legend position (JFree version only): The default position of the legend in JFreeChart is outside the chart; a custom routine can place it inside the chart.
4. Click "OK" to run the script.

***Read CSV and plot Jython*** and ***Read CSV and plot JFree***

1. Invoke the "Analyze->FRAP->"Read CSV file and plot Jython" (or "...JFree") script. The script will open a file containing one or more columns of XY data and plot the data.
2. Multiple FRAP data files can be selected in the File opener dialog; the script will open all files and plot them individually.
3. Select the data structure: the data can have a single X column with multiple Y columns or separate pairs of XY data.
4. Select the legend position (JFree version only): The default position of the legend in JFreeChart is outside the chart; a custom routine can place it inside the chart.
5. Click "OK" to run the script.

***Combine FRAP data Jython*** and ***Combine FRAP data JFree***

1. Invoke the "Analyze->FRAP->"Combine FRAP data Jython" (or "...JFree") script. The script will open two or more single XY recovery curve datasets, plot them on the same graph, calculate and plot mean +/- SEM (or SD) FRAP recovery data, and calculate and plot a fitted curve to the mean recovery data. The script assumes that the datasets (a) have the same X axis (i.e., the same time interval of sampling; and (b) have the same Y range (typically normalized to a 0-to-1 range), and that the datasets all begin with the first post-bleach time point (i.e., there are no pre-bleach time points).
2. A dialog box with options will appear, allowing you to set options:
a. Combine plots: Plots all datasets on a single graph.
b. Plot Y mean values: Calculates mean Y value at each time point and displays on a separate plot.
c. Show error bars: Calculates standard error of the mean (SEM) or standard deviation (SD) for Y values at each time point and displays on the mean plot.
d. Curve fit means: performs a curve fit on the mean recovery values.
e. Curve fit method: Single or double exponential recovery can be selected.
f. Force curve fit through origin for single exponential: in theory, the curve should pass through x = 0 (first time point after bleach) and the minimum signal (y). This may or may not give the best overall fit to the recovery curve.
NOTE: for the Jfree version there is an additional option for legend placement. The default position of the legend in JFreeChart is outside the chart; a custom routine can place it inside the chart.
3. Click "OK" to run the script.

NOTE: The results, curve fit data, and plot(s) must be saved manually.

## Additional information and support
Sample data and additional information can be downloaded from the [Hardin Lab microscopy page](https://worms.zoology.wisc.edu/research/microscopy/)