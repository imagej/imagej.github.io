---
title: Editing object shape in TrackMate
description: Tutorial on how to use TrackMate segmentation editor to modify object shape.
categories: [Segmentation,Tracking]
artifact: sc.fiji:TrackMate
section: Tips and Tricks:Closing the editor window
---

Since version 8, [TrackMate](/plugins/trackmate/index) ships a new feature that allows editing object shape in 2D. 
The spot editor is based on [Labkit](/plugins/labkit) components, and is made to simplify and accelerate the creation of tracking ground truth. 
In this page we explain how to use it to modify segmentation results directly in TrackMate.

## The editor

The spot editor can be launched from the _Display options_ panel of TrackMate:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-04.png" align="center"  width="300" %}

This button is visible only for 2D images.
When clicking on this button, the user interface of TrackMate is frozen and a new window appear:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-06.png" align="center" %}

The editor is made of several UI components:
- The main editor panel, where the image is painted along with the spot masks (center).
- The side panel (left) that contains from top to bottom: 
  - the 'Close and sen' button, that finishes editing and returns to TrackMate;
  - the image visibility tool (with the eye button), that let you hide / unhide the image, perform auto contrast, and open the display settings panel (will appear on the right);
  - the spot label list, listing all spots currently in the editor, and a global visibility button (the eye).
- The toolbar (top).

The toolbar shows the six editing tool we use to annotate an image:

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-six-tools-annotation-bis.png" align="center"  %}

## Navigating in the editor

The editor window is actually a [BDV component](/plugins/bdv/index). 
If you know your way around BDV you will get your bearings quickly.
Otherwise, here is how to navigate in the image panel.

### Panning, rotating and zooming

- Pan the image with the {% include key key="right click" %} button.
- Rotate the image with the {% include key key="left click" %}.
- Zoom in and out towards the center of the panel with the {% include key key="Mouse Wheel" %}.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-07.gif" align="center" width="300" %}

### Resetting the view

- {% include key key="Shift|Z" %} aligns the view with the XY plane.
- {% include key key="Shift|R" %} resets the view.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-08.gif" align="center" width="300"  %}

### Navigating to spots

On the left side bar, you can see the list of labels currently in the editor.
Each label initially corresponds to a spot in TrackMate. 
The label will have the same name and color that of the current view in TrackMate.
Shift-clicking on a label in the list will center the image view on the corresponding spot mask

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-09.gif" align="center" width="300" %}

### Changing the display settings

The _Image_ section in the left side bar allows you to change the display settings of the image.
The _auto contrast_ button will set the display range to the min and max pixel values in the image.
The _settings_ button will open a dialog to change the display settings of the image, such as the color table, the brightness and contrast and the visibility of channels and spots.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-10.gif" align="center" width="300" %}

## Editing spots

Editing spots is made by painting labels in the editor. 
When you modify a label, the modifications will be reimported into TrackMate when you close the editor. 
In TrackMate, 2D spots are polygons, but we found out that painting inside the input image then converting to spots was fast and convenient, particularly with a tablet. 

### For editing, TrackMate spots are written into labels

The editor will display the spots as a 'labeling', a colored image where the pixels inside each spot is painted with a specific label.
All the labels corresponding to the spots in the image are listed on the left side bar. 
The are created with the same color and name that of the spot they correspond to.

So it is possible that two different spots will lead to two different labels in the editor, but with the same color, which will make them indisinguishable. 
If this is the case we recommend changing the spot coloring before launching the editor. 
For instance, selecting the _Random color_ mode.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-RandomColoring.png" align="center" width="300"  %}

Modifying a spot is adding a removing pixels from its shape.
There is a gotcha however: When you finish editing the actual label of a spot does not matter anymore. 
For instance, if you paint a new spot with an existing label, so that the new spot is disconnected from the initial spot or even on another time-point, the new spot will be created as a separated one in TrackMate. 
The fact that the initial spot and the new one have the same label plays no role if they are not touching.

### The six editing tools

When you select one of the tool by cliking on its icon or with F1 - F6, the right part of the toolbar changes to show the tool controls.

### The pan / move tool -  {% include key key="F1" %}

See above.
When this tool is selected, the mouse is used to navigate in the image. 

### Painting labels -  {% include key key="F2" %}

When the paint tool is selected, left clicking in the image will paint the label currently selected in the image, as if you had a brush.
You can select a label in the side bar, or create a new label to create a new spot.
The select label tool described below is used to select a label at a given pixel.

You can change the diameter of the brush with the slider that appears right of the toolbar. 
The default key shortcuts to do so are {% include key key="Q" %} /  {% include key key="E" %} and  {% include key key="Shift|Q" %} /  {% include key key="Shift|E" %}

The rightmost list allows changing the paint mode.
There are three of them: _Replace, Add, Preserve_. 
The selected modes and brush size are remembered between use of the editor. 

#### Paint replace

This is the default mode. 
If you paint over an existing label, it is discarded.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-Paint-Replace.gif" align="center" width="300" %}

#### Paint add

In TrackMate the spots can be overlapping, and as a consequence, in the editor you can have several labels on one pixel. 
This is the way to edit overlapping spots.
The _Add_ mode paint labels, and if there is an existing label, it will add the selected one, and not remove the existing one:

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-Paint-AddMode.gif" align="center" width="300" %}

This will lead to overlapping spots, as demonstrated in the animation above.

#### Paint preserve

This mode is the converse of the 'Replace' mode. 
The selected label will be applied only on the pixels that have no label already.
It will only paint on the background.
This is useful if you have close objects that you know are not overlapping.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-Paint-PreserveMode.gif" align="center" width="300" %}


### Deleting pixels -   {% include key key="F3" %}

The delete tool also has several modes, that are made to harness possibly overlapping labels.

#### Delete all labels

This mode simply remove all labels at once. 
You get the background where you paint.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-Delete-AllLabels.gif" align="center" width="300" %}

#### Delete selected label

With this mode, the brush will only remove the label currently selected, and no touch the others:

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-Delete-SelectedLabel.gif" align="center" width="300" %}


### Flood fill  -   {% include key key="F4" %}

This tool allows for painting over a 'segment' of the labeling.
That is: any connected portion of the labels that have the same labels underneath. 
It is most useful to replace a label or add one.
There is also two modes for this tool.

#### Flood fill replace

Similar to the _Paint add_ tool, this leads to replace all the label of a segment with the selected label.
On the animation below, the red part of the labeling is overwritten with the blue label, leading to a larger spot:

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-FloodFill-Replace.gif" align="center" width="300" %}

#### Flood fill add

This _adds_ a label to a segment that might already have one.
On the animation below, the red label is added to the blue segment. 
This segment has now two labels, the blue and the red, and it appers in magenta in the editor. 
After returning to TrackMate, this leads to two spots overlapping:

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-FloodFill-Add.gif" align="center" width="300" %}

### Flood erase  -   {% include key key="F5" %}

This tool removes one or all labels of a segment.

#### Flood erase remove all

All the labels are removed from the segment.
The modified pixels are now part of the background.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-FloodErase-RemoveAll.gif" align="center" width="300" %}

#### Flood erase selected label

Only the currently selected label is removed. 
For instance, on the animation below, the top segment has two labels, red and blue, and appears in magenta.
The flood erase tool is used to remove the blue label from it, which leaves the red label.

{% include img src="/media/plugins/trackmate/spot-editor/TrackMate-Editor-FloodErase-SelectedLabel.gif" align="center" width="300" %}


### Select label  -   {% include key key="F6" %}

Click on any pixel to select its associated label.
If the pixel contains multiple labels, click repeatedly to cycle through them.


### Keyboard shortcuts changing the brush mode and size

Several keyboard shortcuts are available to speed up the editing process.
First you can press {% include key key="F1" %}, {% include key key="F2" %}, {% include key key="F3" %}, {% include key key="F4" %}, {% include key key="F5" %} and {% include key key="F6" %} to switch between the _Navigate_, _Add_, _Fill_, _Delete_, _Remove_ and _Select_ modes, respectively.
You can also use {% include key key="Q" %} and , {% include key key="E" %} to decrease and increase the brush size, respectively.
Pressing {% include key key="Shift|Q" %} and {% include key key="Shift|E" %} will change the brush size by a larger amount.

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-16.gif" align="center" width="300" %}


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

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-17.png" align="center"  width="300" %}

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
See the _Paint add_ mode above for instance.
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

{% include img src="/media/plugins/trackmate/spot-editor/trackmate-spot-editor-tuto-21.png" align="center" width="400" %}

### Closing the editor window

Has the same effect as clicking the _Close and send to TrackMate_ button.



### Other segmentation editor tools

We developed a segmentation editor tool in TrackMate, because we wanted it to be able to generate tracking ground-truth conveniently.
There are however many segmentation editors, not necessarily made for tracking, available in the domain of biological imaging. 
We list some of them here:

Commercial 
- Imaris 'Surface' objects can be edited manually, as 2D and 3D meshes.
- Arivis can be used for manual correction or creation of segmentation masks
- ...

Open-source
- I have a (somewhat) biased likeness for [Icy](https://icy.bioimageanalysis.org/). Its mask editor is super convenient, can work in 2D / 3D and over time, and has undo / redo. Check [the ROI cheat sheet](https://icy.bioimageanalysis.org/wp-content/uploads/2020/10/2021-04-23_icy-shortcuts_ROIcheatsheet.pdf)
- The UI of [QuPath](https://qupath.github.io/) is super convenient, and it also has undo / redo. The [brush tool](https://qupath.readthedocs.io/en/stable/docs/starting/annotating.html#brush-tool) is particularly useful.
- [Napari](https://napari.org/stable/) has a [label layer](https://napari.org/0.6.2/howtos/layers/labels.html) that can be used to edit manually a segmentation mask, as above.
- In ImageJ, Thierry Pécot created the [Annotater](https://github.com/tpecot/Annotater) plugin to facilitate the creation of Deep Learning models.
- ...

___
Jean-Yves Tinevez, August - December 2025
