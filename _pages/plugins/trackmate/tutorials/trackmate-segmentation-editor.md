---
title: Editing object shape in TrackMate
description: Tutorial on how to use TrackMate segmentation editor to modify object shape.
categories: [Segmentation,Tracking]
artifact: sc.fiji:TrackMate
section: Tips and Tricks:Closing the editor window
---


{% include notice icon="warning" 
  content="This feature is not released yet! 
  It depends on the future version of TrackMate (the forthcoming v8), to be released Autumn 2025 (if everything goes well)." %}

Since version 8, TrackMate ships a new feature that allows editing object shape in 2D. 
The spot editor is based on [Labkit](/plugins/labkit) components, and is made to simplify and accelerate the creation of tracking ground truth. 
In this tutorial we will explain how to use it to modify segmentation results directly in TrackMate 

## Preparing the tutorial data

Download [this image](/media/plugins/trackmate/spot-editor/Celegans-2D.tif) and open it in Fiji.
It is a movie of the early development of a _C. elegans_ embryo, projected in 2D, for which the nuclei have been stained in fluorescence.
We will generate an incorrect segmentation of these nuclei in TrackMate, and fix it with the spot editor. 

In Fiji, with the image open, launch TrackMate ({% include bc path="Plugins|Tracking|TrackMate"%}).
Click the _Next_ button and select the _Thresholding detector_. 
In its configuration page, put a threshold of 1000 and click _Next_.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-02.png" align="center" width="300px"  %}

Click the _Next_ button until you are in the tracker selection page and select the _LAP tracker_.
In its configuration page, 
- put 5 µm as max linking distance, 
- uncheck the _Track segment gap closing_ button, 
- check the _Track segment splitting_ button and put a _max distance_ of 5 µm,
- uncheck everything else.

You should get the following:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-03.png" align="center" width="300px"  %}

## Launching the spot editor

The threshold we set is too stringent, and many nuclei are improperly segmented, and some polar bodies are missing. 
For instance, in frame 2 the top-left nucleus looks like this:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-05.png" align="center" width="300px"  %}

We will use the spot editor to correct some of the mistakes there.
The spot editor can be launched from the _Display options_ panel of TrackMate:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-04.png" align="center"  %}

Move to frame 2 and click the `Launch spot editor button`.
The user interface of TrackMate is frozen and a new window appear:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-06.png" align="center"  %}

The large bottom right panel displays the image overlaid with the spots.
Notice that the spots have been converted to masks, and that they have the same color that in the TrackMate UI.

The top bar is made of widgets that change the brush mode (navigate, add, remove, fill, ...) and the brush size.
We will describe them below.

The left side bar contains (from top to bottom) 
- the button to end editing,
- auto-contrast and display config panel for the spot editor,
- the list of labels currently in the editor, initially there is one label per spot,
- a button to create a new label, possibly for a new spot.

## Navigating in the editor

The editor window is actually a [BDV component](/plugins/bdv/index). 
If you know your way around BDV you will get your bearings quickly.
Otherwise here is how to navigate in the image panel.

### Panning, rotating and zooming

- Pan the image with the {% include key key="right click" %} button.
- Rotate the image with the {% include key key="left click" %}.
- Zoom in and out towards the center of the panel with the {% include key key="Mouse Wheel" %}.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-07.gif" align="center"  %}

### Resetting the view

- {% include key key="Shift|Z" %} aligns the view with the XY plane.
- {% include key key="Shift|R" %} resets the view.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-08.gif" align="center"  %}

### Navigating to spots

On the left side bar, you can see the list of labels currently in the editor.
Shift-clicking on a label in the list will center the image view on the corresponding spot mask

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-09.gif" align="center"  %}

### Changing the display settings

The _Image_ section in the left side bar allows you to change the display settings of the image.
The _auto contrast_ button will set the display range to the min and max pixel values in the image.
The _settings_ button will open a dialog to change the display settings of the image, such as the color table, the brightness and contrast and the visibility of channels and spots.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-10.gif" align="center"  %}

## Editing spots

Let's fix the top left nucleus in frame 2.
Center and zoom in on it, so that it fills the panel.
We see that there are two spurious detections on the side, of 1-pixel size, and that the largest spot is not large enough to cover the nucleus.
Let's first remove the spurious detections.

### Deleting pixels 

The fourth button on the top bar is the _Delete_ button.
Click it to make the delete brush mode active.
But if you click on the spurious detections, nothing happens.
This is because the **delete brush only works on the pixels of the label that is currently selected in the left side bar**.
You need to select the label you want to edit first.
To do so, you can either
- {% include key key="Shift|left click" %} on the spot mask in the image panel, 
- click on the _Select_ button on the top toolbar (the sixth button on the left) then click on the spot in the image,
- or select the label in the left side bar.

{% include notice icon="note"
  content="*Shift-click* in the image selects the spot at the cursor position." %}

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-11.gif" align="center"  %}

Shift-click on each of the spurious detections to select them, and then click on them with the _delete_ brush on to remove them.
Notice that the corresponding labels in the left side bar are not removed, which is normal.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-12.gif" align="center"  %}

### Painting spots

We now want to enlarge the largest spot to cover the nucleus.
First shift-click on it in the image panel to make the spot label active.
Then click on the _Add_ button in the top bar which is the second button from the left.
Edit the brush size to about 5 pixels, and paint over the nucleus.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-13.gif" align="center"  %}

### Removing entire spots

You can also remove entire spots from the editor using the _Remove_ mode, which is the third button from the left in the top bar.
Again, the corresponding label of the spot to remove must be selected in the left side bar.
Click on the _Remove_ button, select the label in the left side bar and click on the spot you want to remove.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-14.gif" align="center"  %}

### Filling holes

Another way of creating spots is to paint the border and fill the inside.
After drawing the contour of the nucleus, you can use the _Fill_ button, which is the third button from the left in the top bar.
Click it, and click inside the contour to fill it.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-15.gif" align="center"  %}

### Keyboard shortcuts changing the brush mode and size

Several keyboard shortcuts are available to speed up the editing process.
First you can press {% include key key="F1" %}, {% include key key="F2" %}, {% include key key="F3" %}, {% include key key="F4" %}, {% include key key="F5" %} and {% include key key="F6" %} to switch between the _Navigate_, _Add_, _Fill_, _Delete_, _Remove_ and _Select_ modes, respectively.
You can also use {% include key key="Q" %} and , {% include key key="E" %} to decrease and increase the brush size, respectively.
Pressing {% include key key="Shift|Q" %} and {% include key key="Shift|E" %} will change the brush size by a larger amount.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-16.gif" align="center"  %}


### Keyboard shortcuts for editing

You can also use the following keyboard shortcuts to directly edit in the image, without having to select a brush mode first.
Put the brush in the _Navigate_ mode ({% include key key="F1" %}), and start editing with the following keys:

| Key | Action |
| --- | --- |
| {% include key key="A" %}{% include key key="left click" %} or {% include key key="Space|left click" %} | add pixels |
| {% include key key="D" %}{% include key key="left click" %} or {% include key key="Space|right click" %}| delete pixels |
| {% include key key="R" %}{% include key key="left click" %} | remove entire spot |
| {% include key key="L" %}{% include key key="left click" %} | fill holes |
| {% include key key="Shift|left click" %} | select spot at mouse location |
| {% include key key="Q" %} and {% include key key="E" %} | decrease and increase the brush size |
| {% include key key="Shift|Q" %} and {% include key key="Shift|E" %} | decrease and increase the brush size faster |
| {% include key key="Space|mouse wheel" %} or {% include key key="A|mouse wheel" %} or {% include key key="D|mouse wheel" %} | change the brush size |


The default key bindings are chosen to match the edition of spots in the TrackMate UI.
For adding, deleting, removing and filling spots, the keys must be used as modifiers, and kept pressed while you paint.

## Passing the results to TrackMate

Once you are done editing, click the _Close and send to TrackMate_ button in the top left side bar.
This will close the editor and prompt you with the following dialog:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-17.png" align="center"  %}

If you click _No_, your changes will be discarded.
If you click _Yes_, the modified spots will be sent to TrackMate. 
If you selected the _Simplify contours_ checkbox, the contours of the spots will be smoothed and simplified before being sent to TrackMate.
This relies on the same routine that for the _Simplify contours_ option found in most of the segmentation detectors in TrackMate, and explained [here](/plugins/trackmate/tutorials/trackmate-segmentation-detectors#simplifying-contours).
Because the spot editing is done with a mask, it is recommended to use this option to avoid having jagged contours.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-18.png" align="center"  %}

## Tips and tricks

### Editing a subset of the image

If the image is very large and you want to only edit a region, you can first draw a ROI in the image before launching the editor.
Only the spots that are fully in the bounding box of the ROI will be sent to the editor.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-19.gif" align="center"  %}

### Editing all time frames

The spot editor normally only edits the spots in the frame that is currently displayed in Fiji.
However if you press the _Shift_ while pressing the _Launch spot editor_ button, all frames will be sent to the editor.
This respects whether you have a ROI in the image or not.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-20.gif" align="center"  %}

### Spots can be overlapping

In TrackMate, spots are represented as polygons, as as such they can overlap. 
This is also the case in the spot editor.
This is the reason why it is necessary to select the spot you want to edit before using the brush.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-22.gif" align="center"  %}

### Several spots can have the same label

In TrackMate, a single spot is of a single polygon.
It cannot have holes, nor cannot be made of several disconnected polygons.
For this reason, when you use one label in the editor to create multiple separated masks, they will appear as multiple spots in TrackMate.

### Spots are reinserted in the tracks

When you edit a spot, it will be possibly reinserted in the TrackMate model, within the track it belonged to. 
If the edits generate masks that are too different from the initial spots, they will be considered as new spots, and the tracks will have to be corrected in [TrackScheme](/plugins/trackmate/tutorials/manual-track-editing#launching-trackscheme).

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-23.gif" align="center"  %}



### Key bindings are customizable

You can customize the key bindings of the spot editor in a dedicated dialog, displayed when you press {% include key key="Ctrl|," %}.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-21.png" align="center"  %}

### Closing the editor window

Has the same effect as clicking the _Close and send to TrackMate_ button.



___
Jean-Yves Tinevez, August 2025
