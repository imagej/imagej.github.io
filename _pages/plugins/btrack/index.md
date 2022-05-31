---
mediawiki: Tissue Branch Tracker
title: Tissue Branch Tracker
logo: /media/logos/btrack.png
categories: [Tracking,Tissue,Skeletonization]
---



<img src="/media/icons/btrack.png" width="250"/> 

BTrack is a tool, 
## Installation

1.  Click {% include bc path="Help | Update..." %}.
2.  Click the *Manage update sites* button.
3.  Select the *BTrack* update site in the list.
4.  Click *Close* and then click *Apply changes*.
5.  Restart Fiji.
6.  Launch the plugin with {% include bc path="Plugins | Tracking | BTrack" %}.

## Usage

### Tissue Detection

A typical dataset consists of a 2d time-lapse of the dynamically growing tissue branches. The file format can be any format readable by Fiji/Bioformats (.tif, .nd2, ... ). To run the tracker select {% include bc path='Plugins|BTrack|Tissue Tracking'%}

A panel to input the Raw and Segmentation with optional field of loading a csv file containing the end point locations will open.

<img src="/media/plugins/btrack/welcome.png" width="200"/>


#### Microscope Parameters
The Raw image metadata contains the information about the camera pixel size and the time calibration. If this information is not present in the metadata the users can modify the text field with the correct values. We use these values to output the final velocity calculation in these units.

#### Main Panel
After completing the selection of choosing the images and optional csv file press the button supplied in the "Done Selection" panel area. At this stage the boundary points of the tissue are computed from the segmentation image and if the csv file was also inputted the skeleton end points at their respective time frames are added to the display of the Raw image and a second panel containing computational and interactivity option will open.

<img src="/media/plugins/btrack/main.png" width="200"/>

#### Interactivity Options


**Deselect and select end points**


**Dynamic slider display**
After the welcome screen the user can only see the view of the input timelapse at the value indicated by the slider embedded into the panel. Moving the slider will interactively update the view along with the overlay of the chosen view.


#### Tracking Options

**Interactive track selection**

#### Save Options


## Citation

Please note that BTrack is available through Fiji, and is based on a publication. If you use it successfully for your research please be so kind to cite our work:

## References

[1] 
