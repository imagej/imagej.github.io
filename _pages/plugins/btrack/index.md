---
title: Tissue Branch Tracker
logo: /media/logos/btrack.png
categories: [Tracking,Tissue,Skeletonization]
---

<img src="/media/icons/btrack.png" width="250"/> 

BTrack is a Fiji plugin for tracking growing branches of tissue in 2 and 3D using generic skeletonization implementation of imglib2.

## Installation

1.  Click {% include bc path="Help | Update..." %}.
2.  Click the *Manage update sites* button.
3.  Select the *BTrack* update site in the list.
4.  Click *Close* and then click *Apply changes*.
5.  Restart Fiji.
6.  Launch the plugin with {% include bc path="Plugins | Tracking | BTrack" %}.

## Usage

### Tissue Detection

A typical dataset consists of a 2d/3d time-lapse of the dynamically growing tissue branches. The file format can be any format readable by Fiji/Bioformats (.tif, .nd2, ... ). To run the tracker select {% include bc path='Plugins|BTrack|Tissue Tracking'%}

A panel to input the Raw and Segmentation with optional field of loading a csv file containing the end point locations will open.

<img src="/media/plugins/btrack/welcome.png" width="200"/>


#### Microscope Parameters
The Raw image metadata contains the information about the camera pixel size and the time calibration. If this information is not present in the metadata the users can modify the text field with the correct values. We use these values to output the final velocity calculation in these units.

#### Main Panel
After completing the selection of choosing the images and optional csv file press the button supplied in the "Done Selection" panel area. At this stage the boundary points of the tissue are computed from the segmentation image and if the csv file was also inputted the skeleton end points at their respective time frames are added to the display of the Raw image and a second panel containing computational and interactivity option will open.

<img src="/media/plugins/btrack/main.png" width="400"/>

#### Interactivity Options




**Dynamic slider display**
After the welcome screen the user can only see the view of the input timelapse at the value indicated by the slider embedded into the panel. Moving the slider will interactively update the view along with the overlay of the chosen view.


**Deselect and select end points**
After the user clicks on skeletonize buddies the program will use the binary /integer labelled image to obtain skelton end points and show the progress of the computation using the progree bar which is updated along with the time text field next to the time slider. During the calculation all the unnecesary options in the plugin will be frozen. At this stage the user can only set the directory path to save the results in post computation. The calculation is skipped for the timepoints if a csv file is provided at teh start and skeeltonization operation is only performed for the time points that are not present in the csv file. As a use case assume that a claculation was interuppted and the csv file that the program creates when doing the skeletonization operation was incomplete. In this scenario the users can restart the computation using the csv file from the previous session and only compute for the missing timepoints than for the whole timelapse, hence saving valuable analysis time.

After th computation is doen the found skelton end points are displayed in pink, the users can add new points by clicking "a" on the keyboard and a new point will be created at the clicked location, clicking shift + a deselct sht closest point to the click and the color changes from pink to red. In the csv file that we save only the pink colored dots end up in the file.

#### Tracking Options

**Interactive track selection**

After the skeletonization operation is complete the users can use the Kalman Filter selection panel to perform the tracking of the tissue end points. These parameters include the search radius and the number of timepoints a gap is acceptable in a track and be continued as a part of being in the same track than have a new track ID assinged to it. The table shows the found tracks and is also fully interactive. Selecting a track from the table pops up a timelapse image with just the track and in the main image the clicked pink dot is surrounded with a big yellow circle indicating that this dot had been visualized in track. Alternatively doing a shift+left click on the image near a pink dot also opens the timelapse image displaying the track of that branch end. The table is highlighted with color green if the mouse position in the image corresponds to the closest track in the table.

#### Save Options

The users can either save one track at a time or can choose to save all the tracks at once. The saved information includes files containing velocities for each track, a pink dot image that contains the dot locations for all the tracks. This dot image is used in the later analysis to co localize the cell location with the growing tissue branch location.

## Citation

Please note that BTrack is available through Fiji, and is based on a publication. If you use it successfully for your research please be so kind to cite our work:

## Authors

Lead programmer, Mantainer: [Varun Kapoor](/people/kapoorlab)
Contributor, Debugger: [Claudia Carabana](/people/claudiacarabana)

## References

[^1]: J. Munkres, "Algorithms for the Assignment and Transportation Problems", Journal of the Society for Industrial and Applied Mathematics, 5(1):32–38, 1957 March
