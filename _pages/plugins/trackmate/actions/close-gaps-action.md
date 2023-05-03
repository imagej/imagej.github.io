---
title: Close gaps in tracks by introducing new spots
categories: [Segmentation,Tracking,Benchmark]
description: Close gaps in TrackMate tracks by introducing new spots
artifact: sc.fiji:TrackMate
---

The _Close gaps in tracks by introducing new spots_ action is a  [TrackMate](/plugins/trackmate/index) action that fills gaps in tracks by adding new spots. 
A gap in a track corresponds to a missed detection that could be bridged by the tracker.
For instance, a track will contain a spot at frame _t_ and one linked to it at _t+2_, but the detection at _t+1_ is missing.
This action modifies the track by inserting a spot at frame _t+1_ in the track.
Several methods are available and can be configured to simply interpolate the spot position or search for them in the source image.

    
{% include img src='/media/plugins/trackmate/actions/close-track-gaps-01.png' align='left'  %}
{% include img src='/media/plugins/trackmate/actions/close-track-gaps-02.png' align='right'  %}
    


## Usage.

Once the tracking is done, move to the last panel of the main TrackMate window, called **Actions**, by clicking on the `Next` button.
The close track gap action can be found near the end of the list. 
After selecting, click the `Execute` button.
A new window should appear.

{% include img src='/media/plugins/trackmate/actions/close-track-gaps-03.png'  align='left' %}
{% include img src='/media/plugins/trackmate/actions/close-track-gaps-04.png' align='right'  %}

When possible, the default parameters are taken from the tracking settings you last used.

### Linear interpolation.

When this method is selected,  the new spots are created by interpolating their position and radius from the spots that precede and follow them.
The image data is not used.

### Search with LoG detector.

Here, TrackMate will try to detect spots by using the LoG detector.
It will search for brigth, roundish structures of a given diameter, within a region around the interpolated position of the spot. 
The size of the region can be specified using the `Search radius` settings.
Note that it is specified in units of the spot diameter. 
If the spot diameter is 1 μm and the `Search radius` is set to 2, the new spot will be searched within 2 μm from the interpolated center, in a cube (for 3D images) of size 4 μm.

If `Automatic diameter` is selected, the radius of the spot to find will be taken by interpolation from the neighbor spots.
Otherwise you can specify a diameter in physical units. 
The spot inserted will be the one with the largest quality found in the region.

### Search with Hessian detector.

This method works as the previous one, but uses the Hessian detector to search for spots. 
You can specify separately a radius for XY and Z.

### Detect in channel.

For the two methods that are based on a spot detector, you need to specify in what channel to perform the detection.
This setting is visible only if the input image has more than 1 channel.

### Close gaps for.

You can specify to perform gap closing for all the visible edges, or just for the edges in the current selection.
Note that the edges in the selection are considered. 
The spots in the selection do not matter.


##  Notes.

With the detector-based methods, the gaps will always be filled, regardless of whether there is an actual bright blob  near the spot location or not.
Some additions might be spurious is there is nothing to detect in the search region.

There is no undo.
Please save your tracks before running this action.

_____________________
*Authors:*
- Robert Haase
- Jean-Yves Tinevez

Jun 2016 - July 2022
