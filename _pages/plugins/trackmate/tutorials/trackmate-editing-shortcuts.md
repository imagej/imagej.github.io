---
title: Shortcuts for editing and navigating the main view of TrackMate
description: Keyboard shortcuts for editing tracks in the TrackMate main view.
categories: [Segmentation,Tracking]
artifact: sc.fiji:TrackMate
doi: 10.1101/2021.09.03.458852
---


## The TrackMate tool config panel

When a [TrackMate](/plugins/trackmate) session is running, the Fiji toolbar displays a new tool specific to TrackMate.

{% include img src='/media/plugins/trackmate/trackmate-configtool-01.png' align='center'  %}


**This tool must be active for the shortcuts displayed below to work.**
By 'active', we simply means that it must be selected.

Double-clicking on the tool icon will bring the TrackMate tool config panel:

{% include img src='/media/plugins/trackmate/trackmate-configtool-02.png' align='center'  width='800' %}


## Related tutorials

The following tutorials exemplifies how to do manual curation or editing of tracks, where these shortcuts and tools are used:
-   [Manual editing of tracks using TrackMate](/plugins/trackmate/tutorials/manual-track-editing) shows how to manually curate and edit tracking results.
-   [Manual tracking with TrackMate](/plugins/trackmate/tutorials/manual-tracking) shows how to perform a fully manual annotation of tracks in a source image.


## Selection

| Key / Mouse                  | Action                                                       |
| ---------------------------- | ------------------------------------------------------------ |
| `click` inside a spot        | Select the spot.                                             |
| `shift` + `click`            | Add / Remove from selection.                                 |
| `click` and `drag`           | Draws a freehand ROI. All spots in the current frame inside the ROI are selected. |
| `shift` + `click` and `drag` | The spots across all frames inside the ROI are selected.     |


## Navigation

| Key / Mouse | Action                                                       |
| ----------- | ------------------------------------------------------------ |
| `↓` / `↑`   | When a spot is selected, navigate within a track, forward and backward in time. |
| `←` / `→`   | Within a track, move across siblings. That is: move to a spot that belongs to the same track within the same frame. For instance: across two daughter cells after a cell division. |
| `⇟` / `⇞`   | Navigate across tracks.                                      |
| `f` / `g`   | Change the time-point currently displayed. Move backward / forward in time, by an amount specified in the TrackMate tool config panel. |


## Editing.

All editing commands require the mouse to be placed _inside_ a spot. No need to click.

| Key / Mouse         | Action                                                       |
| ------------------- | ------------------------------------------------------------ |
| `a`                 | Add a new spot at the mouse location. <br />If the auto-linking mode is on, the new spot is automatically linked to the spot currently selected, and the new spot becomes selected. |
| `d`                 | Delete the spot at the mouse location.                       |
| `q` / `e`           | Change the radius of the spot at the mouse location. Make it smaller / bigger. |
| `shift` + `q` / `e` | Like above, but with greater amount of changes.              |
| `l`                 | Toggle a link between two spots in the selection. There must be exactly two spots selected, and they need to be not in the same frame. If a link already exists between the two selected spots, it is removed. |
| `shift` + `a`       | Start semi-automatic tracking for the spot in the selection. The parameters for semi-automatic tracking can be edited in the TrackMate tool config panel. |
| `shift` + `l`       | Toggle auto-linking mode on / off.                           |

