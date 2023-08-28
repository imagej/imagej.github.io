---
title: SNT › Key Shortcuts
nav-links: true
nav-title: Shortcuts
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
---

{% capture text%}
Most SNT features are triggered by keyboard shortcuts. Shortcuts are typically single keystrokes and most do not require other modifier keys to be pressed. Most are highlighted in the user interface. E.g., to toggle the *Trace/Fill on Secondary <u>L</u>ayer* checkbox, one only needs to press its highlighted letter, i.e., {% include key key='L' %}.
<br><br>
_Typically_, when {% include key keys='ctlcmd' %} is pressed, hotkeys are not intercepted by SNT. E.g., During a tracing session pressing {% include key key='N' %} triggers <u>N</u>o* in the interactive prompt while {% include key keys='ctlcmd|N' %} will trigger IJ's built-in command {% include bc path='File|New|image...'%}.
{% endcapture %}
{% include notice icon="info" content=text %}

{% capture cmdpalette%}
{% include img src="/media/plugins/snt/command-palette.png" align="right" width="450px" %}
The Command Palette is the fastest way to access actions and discover their respective shortcuts:
1. Press {% include key keys='ctlcmd|Shift|P' %} in either SNT or Reconstruction Viewer
2. Start typing to filter actions, scripts and available commands
3. Press {% include key keys='up' %} or {% include key keys='down' %} to select a command (or use the  {% include key keys='mouse wheel' %})
4. Press {% include key keys='Enter' %} to run it
{% endcapture %}
{% include notice background-color="white" icon="tech" content=cmdpalette %}

### Interactive Prompt

| {% include key key='Y' %}  | Confirms the current temporary path. *Mnemonic: <u>Y</u>es* |
| {% include key key='N' %}  | Discards the current temporary path. *Mnemonic: <u>N</u>o*  |
| {% include key key='F' %}  | <u>F</u>inishes a path. Note that you can finish a path by pressing {% include key key='Y' %} {% include key key='Y' %} twice |
| {% include key key='C' %}  | <u>C</u>ancels a path. Note that you can finish a path by pressing {% include key key='N' %} {% include key key='N' %} twice |
| {% include key key='Esc' %}| Aborts current operation / Exits current mode |


### Navigation and Zoom

| {% include key key='Shift' %}    | Synchronizes XY, ZY, and XZ views while moving the cursor when not using cursor snapping |
| {% include key key='+' %} / {% include key key='-' %}      | Zooms in/out (Simultaneously on all views) (IJ default) |
| {% include key key='4' %}        | Displays tracing view(s) at original scale (IJ default) |
| {% include key key='5' %}        | Displays tracing view(s) at 100% (IJ default) |
| {% include key key='Spacebar' %} | Activates the Pan (Hand) tool (IJ default) |
| {% include key key='>' %} / {% include key key='<' %} | Previous/Next Z-slice, or Previous/Next channel, depending on the *Reverse CZT oder of "&gt;" and "&lt;"* choice set in IJ's {% include bc path='Edit|Options|Misc...'%} prompt (IJ default) |
| {% include key key='enter' %}    | Shuttles the window focus between the tracing image and the SNT window |


### Path Handling

| {% include key key='1' %} | Toggles the first visibility filter: Whether all traced paths should be displayed or just selected ones |
| {% include key key='2' %} | Toggles the second visibility filter: Whether all nodes should be displayed across the Z-stack or just those in nearby Z-slices |
| {% include key key='3' %} | Toggles the third visibility filter: Whether paths from all channels/frames should be displayed or just those in the active channel/frame |
| {% include key key='G' %} | Selects the nearest path to the mouse cursor. Holding {% include key keys='Shift|G' %} adds the path nearest to the mouse cursor to the current list of selected paths. *Mnemonic: <u>G</u>roup paths around cursor.* Note that Paths can only be edited one at a time, and thus {% include key keys='Shift|G' %} is disabled in *Edit Mode* |


### Tracing

These shortcuts are available when running SNT in *Tracing Mode*:

| {% include key keys='Ctrl|S' %} / {% include key keys='Command|S' %}           | <u>S</u>ave tracings |
| {% include key key='Ctrl|Shift|S' %} / {% include key keys='Command|Shift|S' %} | <u>S</u>ave <u>S</u>napshot Backup |
| {% include key key='L' %}                     | Toggles Tracing/Filling on Secondary <u>L</u>ayer (filtered image) |
| {% include key key='V' %}                     | Finds the brightest <u>V</u>oxel above and below the current x,y position and automatically clicks on it. If multiple maxima exist, their average positioning is used. Note that this feature assumes that neurites are brighter than the background |
| {% include key key='S' %}                     | Toggles cursor <u>S</u>napping: If enabled, the plugin will automatically move the cursor to the brightest voxel within the specified x,y,z snapping window<sup>1</sup>. When set correctly, this facilitates accurate [positioning of path points](/plugins/snt/step-by-step-instructions#accurate-point-placement) |
| {% include key keys='Alt|Shift|Left Click' %} | Selects a point along the active path to be used as forking point (See [step-by-step instructions](/plugins/snt/step-by-step-instructions#branching-start-a-path-on-an-existing-path) for more details on joining and branching) |
| {% include key keys='Shift|E' %}              | Activates *Edit Mode* (<u>E</u>diting of selected Path) |
| {% include key keys='Shift|P' %}              | <u>P</u>auses tracing operations |


### Path Editing

These shortcuts become available in *Edit Mode*, activated through the contextual menu (displayed with {% include key keys='Right Click' %} on a tracing canvas), or by pressing {% include key keys='Shift|E' %}:

| {% include key key='B' %} | <u>B</u>rings active node to current Z-plane |
| {% include key key='C' %} | <u>C</u>onnects highlighted nodes (see *Connect to Help...* in contextual menu) |
| {% include key key='D' %} | <u>D</u>eletes the active node |
| {% include key key='I' %} | <u>I</u>nserts a new node at cursor position |
| {% include key key='L' %} | <u>L</u>ocks active node to prevent accidental editing |
| {% include key key='M' %} | <u>M</u>oves active node to cursor position |
| {% include key key='R' %} | Changes the <u>R</u>adius of active node |
| {% include key key='X' %} | Splits tree at active node, re-rooting the selected structure at the active node |

### Reconstruction Viewer

| {% include key key='left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} | Rotate (with mouse: {% include key keys='Left Drag' %}) |
| {% include key keys='shift|left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} | Pan (with mouse: {% include key keys='Right Drag' %}) |
| {% include key key='+' %} / {% include key key='-' %} | Zoom (with mouse: {% include key keys='Mouse Wheel' %}) |
| {% include key key='A' %}        | Toggle <u>A</u>xes |
| {% include key key='C' %}        | Toggle <u>C</u>amera Mode |
| {% include key key='D' %}        | Toggle <u>D</u>ark Mode |
| {% include key key='F' %}        | <u>F</u>it View to Visible Objects |
| {% include key key='L' %}        | <u>L</u>og Scene Details to Console |
| {% include key key='R' %}        | <u>R</u>eset View (1 press) or <u>R</u>eload Scene (double press) |
| {% include key key='S' %}        | Save <u>S</u>creenshot |
| {% include key keys='Shift|C' %} | Toggle <u>C</u>ontrol Panel |
| {% include key keys='Shift|F' %} | Toggle <u>F</u>ull Screen ({% include key key='Esc' %} can also be used to exit) |
| {% include key keys='Shift|S' %} | Toggle <u>S</u>tatus Bar |
| {% include key key='H' %}        | <u>H</u>elp (as Notification) ({% include key key='F1' %} shows Help on a dedicated window) |

### sciview

| {% include key key="Left Drag" %}          | Move around |
| {% include key keys='Shift|Left Drag' %}   | Rotate around selected node |
| {% include key key="Left Click" %}         | Select node |
| {% include key key="Double Click" %}       | Centers clicked node |
| {% include key keys='Shift|Mouse Wheel' %} | Zoom |
| {% include key key='W' %} {% include key key='A' %} {% include key key='S' %} {% include key key='D' %} | Move around (hold {% include key key='Shift' %} for slow movement) |

See [sciview](/plugins/sciview)'s {% include bc path='Help| '%}menu for a full list of shortcuts.

### Legacy 3D Viewer

All shortcuts that are not specific to tracing canvases (XY, ZY and XZ views) *should* be recognized by the [Legacy 3D viewer](/plugins/snt/step-by-step-instructions#legacy-3d-viewer). In addition, the following are also implemented:

| {% include key key='H' %}   | Selects the <u>H</u>and (rotation) tool |
| {% include key key='W' %}   | Selects the <u>W</u>and (selection) tool |
| {% include key key='Esc' %} | Shuttles between the Hand and Wand tool after both have been selected at least once |

### Other

There are other key and mouse combinations used in e.g., [Sholl Analysis (by Focal Point)](/plugins/snt/analysis#sholl-analysis), and [Branching and Joining Paths](/plugins/snt/step-by-step-instructions#branching-start-a-path-on-an-existing-path), that are listed in the contextual menu, displayed when right-clicking a tracing canvas.
