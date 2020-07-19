After making this choice of segmentation in the advanced mode the following panel appears

[[Image:TrackAdvancedWater.png|300px]]

Here the user can again make a choice of increasing or decreasing the edge enhancement factor. 

All the watershed and MSER parameters appear in the second panel. The threshold value to create the binary image to perform watershedding has been explained in the section about it in [[watershedding and Hough transform parameters]].

Apart from having the options of displaying Bitimage and Watershedimage the user can also ask the program to auto determine the threshold value in which case Otsu method of determination of an appropriate threshold value would be used, else the user can deselect this option and make their own selection of the threshold value. 

The MSER parameters that appear here as explained in [[MSER parameters]]

After making suitable parameter selection the user can then go over the tracking options where they can see some advanced parameter selections for the optimizer and assignment layer of the program. This panel is shown here

[[Image:ModelChoice.png|800px]]

Read more about [[sub-pixel localization parameter selection]].

*Start tracking

If the user does not wish to change the default settings for sub-pixel localization, they can skip this step and directly click on start tracking button to start the tracking from user defined first and last frame.


*Save parameters

After successful tracking, the user has the option to save the program parameters, so that the movie can be run (again) in batch mode. This choice can also be made without doing the tracking after just making the parameter selection. Clicking on this button triggers the close of the program and saves the program parameters in IJ.log file of FIJI, this close of program is done to ensure that the log file is properly updated by FIJI.
