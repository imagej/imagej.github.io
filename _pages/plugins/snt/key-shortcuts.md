---
title: SNT › Key Shortcuts
excerpt: >-
  These keyboard shortcuts are available
  to control SNT behavior in various modes.
nav-links: true
nav-title: Hotkeys
artifact: org.morphonets:SNT
icon: /media/icons/snt.svg
forum-tag: snt
update-site: Neuroanatomy
---

{% include snt-modes %}
{% capture version%}
**This page was last revised for [version 5.0.21](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice icon="snt" content=version %}

{% capture text%}
{% include img src="/media/plugins/snt/command-palette.png" align="right" width="450px" %}

Most SNT features are triggered by keyboard shortcuts. Shortcuts are typically single keystrokes and most do not require other modifier keys to be pressed. Most are highlighted in the user interface. E.g., to toggle the *Trace/Fill on Secondary <u>L</u>ayer* checkbox, one only needs to press its highlighted letter, i.e., {% include key key='L' %}.

_Typically_, when {% include key keys='ctlcmd' %} is pressed, hotkeys are not intercepted by SNT. E.g., During a tracing session pressing {% include key key='N' %} triggers <u>N</u>o* in the interactive prompt while {% include key keys='ctlcmd|N' %} will trigger IJ's built-in command {% include bc path='File|New|image...'%}.

The [Command Palette](manual#command-palette) ({% include key keys='ctlcmd|Shift|P' %}) is the fastest way to access actions and discover their respective shortcuts!
{% endcapture %}
{% include notice icon="info" content=text %}


{% capture legend %}
Unless marked, shortcuts work in all tracing canvases: the classic XY/ZY/XZ views and [SNT Stream](./snt-stream) (BDV/BVV). Marked shortcuts are limited to one of them:

{{ crop }} → Requires an image fully loaded into memory: A traditional image or a [materialized regions](./manual#materialized-regions) in Stream mode<br>
{{ stream }} → Stream Mode only

In Stream Mode, BDV/BVV's own shortcuts are retained unless noted otherwise.
{% endcapture %}
{% include notice icon="snt-stream" content=legend %}


### Interactive Prompt

| {% include key key='C' %}  | {{ crop }} <u>C</u>ancels a path. Note that you can finish a path by pressing {% include key key='N' %} {% include key key='N' %} twice |
| {% include key key='F' %}  | {{ crop }} <u>F</u>inishes a path. Note that you can finish a path by pressing {% include key key='Y' %} {% include key key='Y' %} twice or using {% include key keys='Double Click' %}|
| {% include key key='N' %}  | {{ crop }} Discards the current temporary path. *Mnemonic: <u>N</u>o*  |
| {% include key key='Y' %}  | {{ crop }} Confirms the current temporary path. *Mnemonic: <u>Y</u>es* |
| {% include key key='Enter' %} | {{ stream }} Finishes the temporary path (same as {% include key key='Double Click' %} while tracing; otherwise, a double click centers the view) |
| {% include key key='Esc' %}| Aborts current operation / Discards the temporary path / Exits current mode |
| {% include key key='Z' %}  | Undo last segment (temporary paths) |


### Navigation and Zoom

| {% include key key='Shift' %}    | {{ crop }} Synchronizes XY, ZY, and XZ views while moving the cursor when not using cursor snapping |
| {% include key key='+' %} / {% include key key='-' %}      | {{ crop }} Zooms in/out (Simultaneously on all views) (IJ default) |
| {% include key key='4' %}        | {{ crop }} Displays tracing view(s) at original scale (IJ default) |
| {% include key key='5' %}        | {{ crop }} Displays tracing view(s) at 100% (IJ default) |
| {% include key key='Spacebar' %} | {{ crop }} Activates the Pan (Hand) tool (IJ default) |
| {% include key key='>' %} / {% include key key='<' %} | {{ crop }} Previous/Next Z-slice, or Previous/Next channel, depending on the *Reverse CZT order of "&gt;" and "&lt;"* choice set in IJ's {% include bc path='Edit|Options|Misc...'%} prompt (IJ default) |
| {% include key key='Enter' %}    | {{ crop }} Shuttles the window focus between the tracing image and the SNT window |
| {% include key key='Ctrl|Tab' %} {% include key key='Ctrl|Shift|Tab' %} | {{ crop }} Activates the next/previous tab in the main SNT window |
| {% include key keys='Ctrl/Cmd|G' %} | {{ stream }} Prompts for a location to fly to |


### Path Selection and Visibility

| {% include key key='G' %} | <u>G</u>rabs the nearest path to the mouse cursor. Holding {% include key keys='Shift|G' %} adds the nearest path to the current selection. Note that Paths can only be edited one at a time, and thus {% include key keys='Shift|G' %} is disabled in *Edit Mode* |
| {% include key keys='Alt|G' %} | Deselects the last selected path (nothing remains selected if only one path was selected) |
| {% include key keys='Shift|Alt|G' %} | Deselects all paths (*Select None*) |
| {% include key key='H' %} | Temporarily <u>H</u>ides all paths/annotations while pressed |
| {% include key key='O' %} | {{ crop }} Temporarily shows path <u>O</u>rientations (start→end direction) while pressed |
| {% include key key='1' %} | {{ crop }} Toggles the first visibility filter: Whether all traced paths should be displayed or just selected ones |
| {% include key key='2' %} | {{ crop }} Toggles the second visibility filter: Whether all nodes should be displayed across the Z-stack or just those in nearby Z-slices |
| {% include key key='3' %} | {{ crop }} Toggles the third visibility filter: Whether paths from all channels/frames should be displayed or just those in the active channel/frame |

Path (de)selection shortcuts are disabled in *Edit Mode*, in which a single path is always selected.


### Tracing

These shortcuts are available when running SNT in *Tracing Mode*:

| {% include key key='L' %}                     | Toggles Tracing/Filling on Secondary <u>L</u>ayer (filtered image) |
| {% include key key='V' %}                     | {{ crop }} Finds the brightest <u>V</u>oxel above and below the current x,y position and automatically clicks on it. If multiple maxima exist, their average positioning is used. Note that this feature assumes that neurites are brighter than the background |
| {% include key key='S' %}                     | {{ crop }} Toggles cursor <u>S</u>napping: If enabled, the plugin will automatically move the cursor to the brightest voxel within the specified x,y,z snapping window. When set correctly, this facilitates accurate [positioning of path points](/plugins/snt/walkthroughs#accurate-point-placement) |
| {% include key key='P' %}                     | {{ stream }} <u>P</u>icks the structure under the cursor as a representative structure (e.g., for the _Pick Sigma(s)_ palette) |
| {% include key key='Spacebar' %}              | {{ stream }} A quick tap toggles tracing on/off; holding it disables tracing for as long as it is pressed |
| {% include key keys='Ctrl|Mouse Wheel' %}     | {{ crop }} Change diameter of path being traced |
| {% include key keys='Alt|Shift|Left Click' %} | Selects a point along the active path to be used as forking point (See [step-by-step instructions](/plugins/snt/walkthroughs#branching-start-a-path-on-an-existing-path) for more details on joining and branching). This shortcut can be [simplified](/plugins/snt/manual#temporary-paths) |
| {% include key keys='Shift|E' %}              | Activates *Edit Mode* (<u>E</u>diting of selected Path) |
| {% include key keys='Shift|P' %}              | {{ crop }} <u>P</u>auses tracing operations |
| {% include key keys='Ctrl|S' %} / {% include key keys='Command|S' %}           | {{ crop }} <u>S</u>ave tracings |
| {% include key key='Ctrl|Shift|S' %} / {% include key keys='Command|Shift|S' %} | {{ crop }} Backup tracings |
| {% include key key='Ctrl|Shift|O' %} / {% include key keys='Command|Shift|O' %} | {{ crop }} Save tracings & Open Next Image |
| {% include key key='Ctrl|Alt|O' %} / {% include key keys='Command|Alt|O' %} | {{ crop }} Save tracings & Open Previous Image |


### Bookmarks and Analysis

| {% include key keys='Shift|B' %} | {{ crop }} <u>B</u>ookmarks cursor location. Not used in Stream Mode because it collides with BDV/BVV native bookmark support |
| {% include key key='M' %}        | {{ stream }} <u>M</u>arks cursor location |
| {% include key keys='Shift|Alt|A' %} | Sholl analysis at nearest node |
| {% include key key='K' %}        | {{ stream }} Records a <u>K</u>ey frame ({% include key keys='Shift|K' %} clears the frames recorded so far) |
| {% include key keys='Shift|S' %} | {{ stream }} Saves a <u>S</u>creenshot (BVV only) |
| {% include key keys='Ctrl|Shift|P' %} / {% include key keys='Command|Shift|P' %} | Toggle Command <u>P</u>alette |


### Path Editing

These shortcuts become available in *Edit Mode*, activated through the contextual menu (displayed with {% include key keys='Right Click' %} on a tracing canvas), or by pressing {% include key keys='Shift|E' %}. When active, tracing is suspended and the node under the cursor is the active node:

| {% include key key='B' %} | {{ crop }} <u>B</u>rings active node to current Z-plane |
| {% include key key='C' %} | <u>C</u>onnects highlighted nodes (see *Connect to Help...* in contextual menu) |
| {% include key key='Shift|C' %} | {{ stream }} Quick <u>C</u>onnects nodes (see *Connect to Help...* in contextual menu) |
| {% include key key='D' %} | <u>D</u>eletes the active node |
| {% include key key='I' %} | <u>I</u>nserts a new node at cursor position |
| {% include key key='L' %} | <u>L</u>ocks active node to prevent accidental editing |
| {% include key key='M' %} | <u>M</u>oves active node to cursor position |
| {% include key key='P' %} | {{ crop }} Toggle <u>P</u>aint Mode for brush editing |
| {% include key key='R' %} | Changes the <u>R</u>adius of active node |
| {% include key key='T' %} | <u>T</u>ags the active node (assigns it a unique color) |
| {% include key key='X' %} | Splits tree at active node, re-rooting the selected structure at the active node |
| {% include key key='Z' %} | Undo last operation |
| {% include key key='Esc' %} | Exits *Edit Mode* |
| {% include key keys='Ctrl|Mouse Wheel' %}     | {{ crop }} Adjust node radius / brush size (Paint Mode) |
| {% include key keys='Alt|Drag' %}             | {{ crop }} Move node / blend radii (Paint Mode) |

Commands without an equivalent in Stream Mode (e.g., paint mode) are disabled in its contextual menu.

### Reconstruction Viewer

| {% include key key='left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} | Rotate (with mouse: {% include key keys='Left Drag' %}) |
| {% include key keys='shift|left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} | Pan (with mouse: {% include key keys='Right Drag' %}) |
| {% include key key='+' %} / {% include key key='-' %} | Zoom (with mouse: {% include key keys='Mouse Wheel' %}) |
| {% include key keys='Double Click' %} | Toggle animation (auto-detect rotation axis) |
| {% include key keys='Shift|Double Click' %} | Toggle animation (force Z-axis rotation) |
| {% include key keys='CTRL|Left Click' %} | Snap to top/side view |
| {% include key key='A' %}        | Toggle <u>A</u>xes |
| {% include key key='C' %}        | Toggle <u>C</u>amera Mode |
| {% include key key='D' %}        | Toggle <u>D</u>ark Mode |
| {% include key key='F' %}        | <u>F</u>it View to Visible Objects |
| {% include key key='H' %}        | <u>H</u>elp (as Notification) ({% include key key='F1' %} shows Help on a dedicated window) |
| {% include key key='L' %}        | <u>L</u>og Scene Details to Console |
| {% include key key='R' %}        | <u>R</u>eset View (1 press) or <u>R</u>eload Scene (double press) |
| {% include key key='S' %}        | Save <u>S</u>creenshot |
| {% include key keys='Shift|C' %} | Toggle <u>C</u>ontrol Panel |
| {% include key keys='Shift|F' %} | Toggle <u>F</u>ull Screen ({% include key key='Esc' %} can also be used to exit) |
| {% include key keys='Shift|S' %} | Toggle <u>S</u>tatus Bar |
| {% include key keys='Ctrl|Shift|P' %} / {% include key keys='Command|Shift|P' %}| Toggle Command <u>P</u>alette |

### sciview

| {% include key key="Left Drag" %}          | Move around |
| {% include key keys='Shift|Left Drag' %}   | Rotate around selected node |
| {% include key key="Left Click" %}         | Select node |
| {% include key key="Double Click" %}       | Centers clicked node |
| {% include key keys='Shift|Mouse Wheel' %} | Zoom |
| {% include key key='W' %} {% include key key='A' %} {% include key key='S' %} {% include key key='D' %} | Move around (hold {% include key key='Shift' %} for slow movement) |

See [sciview](/plugins/sciview)'s {% include bc path='Help| '%}menu for a full list of shortcuts.

### Legacy 3D Viewer

The most important shortcuts for the [Legacy 3D viewer](/plugins/snt/walkthroughs#tracing-in-the-legacy-3d-viewer) are:

| {% include key key='H' %} | Selects the <u>H</u>and (pan) tool |
| {% include key key='W' %} | Selects the <u>W</u>and (tracing) tool |
| {% include key keys='Middle Drag' %} | Rotation |
| {% include key keys='Shift|Middle Drag' %} | Pan (translation) |
| {% include key keys='Mouse Wheel' %} | Zoom |
| {% include key keys='Shift|Left Drag' %} | When Hand tool is active: Pan (translation) |
| {% include key keys='Left Drag' %} | When Hand tool is active: Rotation |

In addition, _most_ shortcuts that are not specific to tracing canvases (XY, ZY and XZ views) can be used in the 3D Viewer. When a key stroke is not recognized by the 3D Viewer, a message is displayed in the [status bar](/plugins/snt/manual#status-bar) of the main dialog.


### Other

There are other key and mouse combinations used in e.g., [Sholl Analysis (by Focal Point)](/plugins/snt/analysis#sholl-analysis), and [Branching and Joining Paths](/plugins/snt/walkthroughs#branching-start-a-path-on-an-existing-path), that are listed in the contextual menu, displayed when right-clicking a tracing canvas. In Stream Mode, right-click without dragging (since right-drag pans the view) to bring up the same menu. It also includes _Continue Extending Path_, which replaces the toolbar button used by earlier versions of Stream Mode.
