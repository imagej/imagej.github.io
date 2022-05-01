---
mediawiki: Watershed_followed_by_MSER
title: Watershed followed by MSER
---

After making this choice of segmentation in the advanced mode the following panel appears

<img src="/media/plugins/mtrack/trackadvancedwater.png" width="300"/>

Here the user can again make a choice of increasing or decreasing the edge enhancement factor.

All the watershed and MSER parameters appear in the second panel. The threshold value to create the binary image to perform watershedding has been explained in the section about it in [watershedding and Hough transform parameters](/plugins/mtrack/watershed-hough-parameters).

Apart from having the options of displaying Bitimage and Watershedimage the user can also ask the program to auto determine the threshold value in which case Otsu method of determination of an appropriate threshold value would be used, else the user can deselect this option and make their own selection of the threshold value.

The MSER parameters that appear here as explained in [MSER parameters](/plugins/mser-parameters)

After making suitable parameter selection the user can then go over the tracking options where they can see some advanced parameter selections for the optimizer and assignment layer of the program. This panel is shown here

<img src="/media/plugins/mtrack/modelchoice.png" width="800"/>

Read more about [sub-pixel localization parameter selection](/plugins/mtrack/sub-pixel-localization-parameter-selection).

-   Start tracking

If the user does not wish to change the default settings for sub-pixel localization, they can skip this step and directly click on start tracking button to start the tracking from user defined first and last frame.

-   Save parameters

After successful tracking, the user has the option to save the program parameters, so that the movie can be run (again) in batch mode. This choice can also be made without doing the tracking after just making the parameter selection. Clicking on this button triggers the close of the program and saves the program parameters in IJ.log file of Fiji, this close of program is done to ensure that the log file is properly updated by Fiji.
