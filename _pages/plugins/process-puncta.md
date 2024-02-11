---
mediawiki: Puncta Process
title: Puncta Process
categories: [Particle Analysis]
source-url: https://github.com/DanHUMassMed/puncta_process_plugin
team-founders: [Dan Higgins, Amy Walker]
---

The Puncta Process ImageJ PlugIn is a {% include wikipedia title='Particle Analysis' text='practical analysis' %} tool for counting puncta in 3D image data. 

 The plugin uses single-channel data to produce three specific values: 
- **Puncta Volume** An average number of voxels (volume picture elements) of the object times z,y, and z calibrations. 
- **Puncta Number** The average number of puncta counts within a given ROI (Region of Interest)
- **ROI Intensity** The measures the overall pixel intensity over the Region of Interest


The Puncta Process expects that the preprocessing step of selecting the ROIs has been completed and that the image data is separated into a directory structure based on fluorescence (488, 561)

 The Puncta Process leverages the [MorphoLibJ](https://imagej.github.io/plugins/morpholibj) and [3D Objects Counter](https://imagej.github.io/plugins/3d-objects-counter) PlugIns and allows users to select Filter options and threshold levels prior to process execution.  

The process provides detailed outputs of each process step, including:
- White Top Hat corrected images
- 3D Object Counter details (CSV)
- Z Projected images (maximum intensity)

And a summary output including:
- MS Excel Report
- Preliminary Visualizations BarCharts with Error bar
- Summary CSV data (for ease of import into downstream processes)


## Installation

-   In [Fiji](/software/fiji)), you just need to [ add](/update-sites/following#add-update-sites) the Puncta Process and IJPB-plugins sites to your list of update sites:
    1.  Select {% include bc path='Help | Update...' %} from the menu to start the [updater](/plugins/updater).
    2.  Click on *Manage update sites*. This brings up a dialog where you can activate additional update sites.
    3.  Activate the **Puncta Process** and **IJPB-plugins** sites and close the dialog.
    4.  Click *Apply changes* and restart ImageJ.


## Resources

The main source code directory is on GitHub under [here](https://github.com/DanHUMassMed/puncta_process_plugin).


## Screenshots

<img src="https://raw.githubusercontent.com/DanHUMassMed/puncta_process_plugin/main/docs/Puncta_Process_Dialog.png" width="500" >
<br>
<img src="https://raw.githubusercontent.com/DanHUMassMed/puncta_process_plugin/main/docs/BarCharts_Screenshot.png" width="500">
<br>
<img src="https://raw.githubusercontent.com/DanHUMassMed/puncta_process_plugin/main/docs/Excel-Screenshot.png" width="500">
