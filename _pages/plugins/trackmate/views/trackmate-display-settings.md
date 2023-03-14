---
title: TrackMate display settings
description: How to configure the display of TrackMate
categories: [Tracking, Segmentation]
---

Starting with version 7, we entirely redesigned the display settings in [TrackMate](/plugins/trackmate/index).
You can now tune how track are displayed in with many more parameters. 
Jan Eglinger initially made a config option that allowed changing the lookup table (LUT) for coloring in TrackMate. We built upon this to extend it by adapting a pattern used for [Mastodon](/plugins/mastodon/index) settings

## The display settings panel

In the config view panel of the UI, there is now a button that toggles the visibility of the display settings panel. 

{% include img src='/media/plugins/trackmate/trackmate-display-settings-1.png' width='250'  %}

This new panel lets you configure all of the display settings now available, of which only a subset is available on the config view panel.

{% include img src='/media/plugins/trackmate/trackmate-display-settings-2.png' width='250'  %}
{% include img src='/media/plugins/trackmate/trackmate-display-settings-3.png' width='250'  %}

Any change you make in this panel will be reflected immediately on the views currently opne.
The meaning of this parameters is summarized below:

{% include img src='/media/plugins/trackmate/trackmate-display-settings-4.png'  %}


## Configuring the default display settings

You can change what display settings are used by default in new Tracking sessions.
There is an extra plugin in Fiji in {% include bc path="Edit | Options | Configure TrackMate display settings..." %} that shows the same configuration panel.
At the bottom of this panel there are 3 buttons:

{% include img src='/media/plugins/trackmate/trackmate-display-settings-5.png' width='250'  %}

- `Reset` resets the display options to the built-in defaults.
- `Revert` reloads the display options from what was saved before.
- `Save to user default` saves the current display config to a file. These settings will be used from now in with all the new TrackMate sessions.

The display settings are saved as a JSon file, in the `.trackmate` folder in your home directory:

```sh
➜  ~ ls ~/.trackmate
userdefaultsettings.json
➜  ~ cat ~/.trackmate/userdefaultsettings.json 
{
  "name": "User-default",
  "spotUniformColor": "204, 51, 204, 255",
  "spotColorByType": "DEFAULT",
etc.
➜  ~ 
```

## Settings are saved with the data

When you save a TrackMate session to XML, the save file will include the display settings you configured. 
When you will reload the data, the display settings will also be loaded and used.

The display settings are saved in a section of the XML file called `<DisplaySettings>`. 
But in this tag, the display settings are saved as a JSon string 😅.
For instance you will be able to find the following at the end of v7 TrackMate XML file:

```xml
  <DisplaySettings>{
  "name": "Default",
  "spotUniformColor": "204, 51, 204, 255",
  "spotColorByType": "TRACKS",
  "spotColorByFeature": "TRACK_INDEX",
  "spotDisplayRadius": 1.0,
  "spotDisplayedAsRoi": true,
  "spotMin": 25.702575607472813,
  "spotMax": 108.47393301546651,
  "spotShowName": true,
  "trackMin": 25.702575607472813,
  "trackMax": 108.47393301546651,
  "trackColorByType": "TRACKS",
  "trackColorByFeature": "TRACK_INDEX",
  "trackUniformColor": "204, 204, 51, 255",
  "undefinedValueColor": "0, 0, 0, 255",
  "missingValueColor": "89, 89, 89, 255",
  "highlightColor": "51, 230, 51, 255",
  "trackDisplayMode": "FULL",
  "colormap": "Jet",
  "limitZDrawingDepth": false,
  "drawingZDepth": 10.0,
  "fadeTracks": true,
  "fadeTrackRange": 30,
  "useAntialiasing": true,
  "spotVisible": true,
  "trackVisible": true,
  "font": {
    "name": "Calibri",
    "style": 1,
    "size": 10,
    "pointSize": 10.0,
    "fontSerializedDataVersion": 1
  },
  "lineThickness": 1.0,
  "selectionLineThickness": 4.0,
  "trackschemeBackgroundColor1": "149, 170, 159, 255",
  "trackschemeBackgroundColor2": "192, 192, 192, 255",
  "trackschemeForegroundColor": "255, 255, 255, 255",
  "trackschemeDecorationColor": "4, 79, 79, 255",
  "trackschemeFillBox": false
}</DisplaySettings>
```
