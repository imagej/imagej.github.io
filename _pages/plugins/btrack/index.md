---
title: Tissue Branch Tracker
icon: /media/icons/btrack.png
categories: [Tracking,Tissue,Skeleton]
---

<img src="/media/icons/btrack.png" width="250"/> 

BTrack is a TrackMate detector for tracking growing ends of tissue branches using skeletonization implementation of imglib2.

## Installation

1.  Click {% include bc path="Help | Update..." %}.
2.  Click the *Manage update sites* button.
3.  Select the *BTrack* update site in the list.
4.  Click *Close* and then click *Apply changes*.
5.  Restart Fiji.
6.  The detector would show up in the drop down menu list of TrackMate.

## Usage

### Tissue Detection

BTrack is a tool to analyse the growth of branched tissues. A 2D time-lapse/ 3D image can be analysed with this detector. The file format can be any format readable by Fiji/Bioformats (.tif, .nd2, ... ). To run the tracker, select {% include bc path='Plugins|Tracking|TrackMate'%}

For using this detector select Btrack from the detector menu list of TrackMate. The screen looks as shown here

{% include img src="/media/plugins/btrack/Btrackdetector_screen_1.png" %}


#### Detection Panel
Click next and if you are using a hyperstack with Raw and segmentation images in two channels, choose the segmentation image channel for the detector. Click Preview to see the detected end points. The panel for this looks as shown here

{% include img src="/media/plugins/btrack/Btrackdetector_screen_2.png" %}

In our [example, download from Zenodo](https://zenodo.org/record/6838981) we have the Segmentation image in channel 1 and the Raw image in channel 2 and the initial detections look as shown here

{% include img src="/media/plugins/btrack/initial_detections.png" %}

#### Tracking Options

After the initial preview click on the next button to run the detector on all the timepoints, after that you can use the simple LAP tracker of TrackMate [^1] to track the growing end points. The final result after tracking looks as shown here

{% include img src="/media/plugins/btrack/initial_tracks.png" %}



#### Save Options
All the usual tracking, track editing and saving options that are provided by TrackMate can be used to further analyze and compute the growth rates of individual tracks. For detailed options available for doing so please refer to the manual of [TrackMate](https://imagej.net/plugins/trackmate/)

## Authors
Lead programmer, Mantainer: {% include person id='kapoorlab' %}

## References

[^1]: J. Munkres, "Algorithms for the Assignment and Transportation Problems", Journal of the Society for Industrial and Applied Mathematics, 5(1):32–38, 1957 March
