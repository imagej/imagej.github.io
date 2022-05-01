---
title: 2016-03-31 - TrackMate v3.1.0 released
---

We just release the version 3.1.0 of [TrackMate](/plugins/trackmate), a Fiji plugin for single-particle tracking. We also mention here the changes of version 3.0.1, which did not get a news item.

## Improvements.

-   Add an action that export all visible spots statistics, regardless of whether they belong in a track or not.

![](/media/news/trackmate-exportallspotsstatistics.png)

-   New display mode: show only selection.

This track display mode only shows the content of the current selection, for spots and edges. It can be accessed in the GUI panel 'Configure views' with a special track display mode called 'Selection only'. Careful: the content of the selection model can still be edited in this mode. Of course, the track display mode is ignored by TrackScheme, which then can be used to modify the selection in this mode.

{% include video platform='youtube' id='H72C1pae5-A'%}

-   The semi-auto tracker now detects spots in the currently selected channel, in case of a multi-C image.

-   The thumbnail images in TrackScheme are taken from the currently selected channel as well.

-   There is now a step-wise time browsing ('à la MaMuT'): press 'F' and 'G' to move in time by jumping to frames, spaced by a number set in the Spot edit tool of TrackMate (double-click on the icon in the ImageJ toolbar).

![](/media/news/trackmate-stepwisetimebrowsing.png)

-   The manual editing of spot radius (press 'Q' and 'E') is fully reversible (if you press 3 times 'Q' then 3 times 'E', you get back the initial radius).

-   TrackMate is now more verbose when doing manual editing.

## Changes.

-   We really do not relaunch TrackScheme automatically when loading a TrackMate file.

-   The 3D Viewer is working again, at least (as of today) on Windows platforms. On Macs, the time slider does not work and trying to interact with it will crash Fiji.

-   Also, to keep the 3D Viewer tidy, it is not kept in sync with the manual edits made on the model. It just shows a snapshot of the model at the time when it was launched. It was not working properly before anyway, so we officially disable this feature.

[JeanYvesTinevez](/people/tinevez) 06:46, 31 March 2016 (CDT)


