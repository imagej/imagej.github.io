---
mediawiki: SNT:_Key_Shortcuts
title: SNT › Key Shortcuts
nav-links: true
nav-title: Key Shortcuts
---

{% capture text%}
Most SNT features are triggered by keyboard shortcuts. Shortcuts are typically single keystrokes and do not require other modifier keys to be pressed. Most are highlighted in the user interface. E.g., to toggle the *Trace/Fill on Secondary <u>L</u>ayer* checkbox, one only needs to press its highlighted letter, i.e., {% include key key='L' %}.
{% endcapture %}
{% include notice icon="info" content=text %}

### Interactive Prompt

These shortcuts are always available:

-   {% include key key='Y' %} - Confirms the current temporary path. *Mnemonic: <u>Y</u>es*.

<!-- -->

-   {% include key key='N' %} - Discards the current temporary path. *Mnemonic: <u>N</u>o*.

<!-- -->

-   {% include key key='F' %} - Finishes a path. Note that you can finish a path by pressing {% include key key='Y' %} twice.

<!-- -->

-   {% include key key='C' %} - Cancels a path. Note that you can finish a path by pressing {% include key key='N' %} twice.

<!-- -->

-   {% include key key='Esc' %} - Aborts current operation / Exits current mode

### Tracing

These shortcuts are available when running SNT in *Tracing Mode*:

-   {% include key key='L' %} - Toggles Tracing/Filling on Secondary <u>L</u>ayer (filtered image).

<!-- -->

-   {% include key key='V' %} - Finds the brightest <u>V</u>oxel above and below the current x,y position and automatically clicks on it. If multiple maxima exist, their average positioning is used. Note that this feature assumes that neurites are brighter than the background.

<!-- -->

-   {% include key key='S' %} - Toggles cursor <u>S</u>napping: If enabled, the plugin will automatically move the cursor to the brightest voxel within the specified x,y,z snapping window<sup>1</sup>. This facilitates accurate [positioning of path points](/plugins/snt/step-by-step-instructions#accurate-point-placement) and it is described in more detail in this [issue](https://github.com/fiji/Simple_Neurite_Tracer/issues/1).

<!-- -->

-   {% include key keys='Alt|Shift' %}-click - Selects a point along the active path to be used as forking point (See [step-by-step instructions](/plugins/snt/step-by-step-instructions#branching-start-a-path-on-an-existing-path) for more details on joining and branching).

<!-- -->

-   {% include key keys='Shift|E' %} Activates *Edit Mode* (editing of selected Path).

<!-- -->

-   {% include key keys='Shift|P' %} <u>P</u>auses tracing operations.

### Navigation and Zoom

These shortcuts are always available:

-   {% include key key='Shift' %} - Synchronizes XY, ZY, and XZ views while moving the cursor when not using cursor snapping.

<!-- -->

-   {% include key key='+' %} - Zooms in (Simultaneously on all views) (IJ default).

<!-- -->

-   {% include key key='-' %} - Zooms out (Simultaneously on all views) (IJ default).

<!-- -->

-   {% include key key='4' %} - Displays tracing view(s) at original scale (IJ default).

<!-- -->

-   {% include key key='5' %} - Displays tracing view(s) at 100% (IJ default).

<!-- -->

-   {% include key key='Spacebar' %} - Activates the Pan (Hand) tool (IJ default).

<!-- -->

-   {% include key key='>' %} / {% include key key='<' %} - Previous/Next Z-slice, or Previous/Next channel, depending on the *Reverse CZT oder of "&gt;" and "&lt;"* choice set in IJ's {% include bc path='Edit|Options|Misc..'%} prompt (IJ default).

<!-- -->

-   {% include key key='enter' %} - Shuttles the window focus between the tracing image and the SNT window.

### Path Handling

These shortcuts are always available:

-   {% include key key='1' %} - Toggles the first visibility filter: Whether all traced paths should be displayed or just selected ones

<!-- -->

-   {% include key key='2' %} - Toggles the second visibility filter: Whether all nodes should be displayed across the Z-stack or just those in nearby Z-slices

<!-- -->

-   {% include key key='3' %} - Toggles the third visibility filter: Whether paths from all channels/frames should be displayed or just those in the active channel/frame

<!-- -->

-   {% include key key='G' %} - Selects the nearest path to the mouse cursor. Holding {% include key keys='Shift|G' %} adds the path nearest to the mouse cursor to the current list of selected paths. *Mnemonic: <u>G</u>roup paths around cursor.* Note that Paths can only be edited one at a time, and thus {% include key keys='Shift|G' %} is disabled in *Edit Mode*.

### Path Editing

These shortcuts become available in *Edit Mode*, activated through the contextual menu (displayed when right-clicking on a tracing canvas) or by pressing {% include key keys='Shift|E' %}:

-   {% include key key='B' %} - <u>B</u>rings active node to current Z-plane.
-   {% include key key='C' %} - Connects highlighted nodes (see *Connect to Help...* in contextual menu)
-   {% include key key='D' %} - <u>D</u>eletes the active node.
-   {% include key key='I' %} - <u>I</u>nserts a new node at cursor position.
-   {% include key key='L' %} - <u>L</u>ocks active node to prevent accidental editing.
-   {% include key key='M' %} - <u>M</u>oves active node to cursor position.
-   {% include key key='X' %} - Split Tree at active node: Re-roots the current reconstruction at the active node.

### Reconstruction Viewer

-   {% include key key='left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} - Rotate (with mouse: Left-click & drag)
-   {% include key keys='shift|left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} - Pan (with mouse: Right-click & drag)
-   {% include key key='+' %} {% include key key='-' %} - Zoom (with mouse: Scroll wheel)
-   {% include key key='A' %} - Toggle <u>A</u>xes
-   {% include key key='C' %} - Toggle <u>C</u>amera Mode
-   {% include key key='D' %} - Toggle <u>D</u>ark Mode
-   {% include key key='F' %} - <u>F</u>it View to Visible Objects
-   {% include key key='L' %} - <u>L</u>og Scene Details to Console
-   {% include key key='R' %} - <u>R</u>eset View
-   {% include key keys='Shift|R' %} - <u>R</u>eload View
-   {% include key key='S' %} - Save <u>S</u>creenshot

-   {% include key keys='Shift|F' %} - <u>F</u>ull Screen ({% include key key='Esc' %} to exit)
-   {% include key keys='Shift|C' %} - Toggle <u>C</u>ontrol Panel

-   {% include key key='H' %} - <u>H</u>elp (as Notification) ({% include key key='F1' %} shows Help on a dedicated window)

### SciView

-   {% include key key="Left Drag" %} - Move around
-   {% include key keys='Shift|Left Drag' %} - Rotate around selected node
-   {% include key key="Left Click" %} - Select node
-   {% include key key="Double Click" %} - Centers clicked node
-   {% include key keys='Shift|Mouse Wheel' %} - Zoom
-   {% include key key='W' %} {% include key key='A' %} {% include key key='S' %} {% include key key='D' %} - Move around (hold {% include key key='Shift' %} for slow movement)

See [sciview](/plugins/sciview)'s {% include bc path='Help| '%}menu for a full list of shortcuts.

### Legacy 3D Viewer

All shortcuts that are not specific to tracing canvases (XY, ZY and XZ views) *should* be recognized by the [Legacy 3D viewer](/plugins/snt/step-by-step-instructions#legacy-3d-viewer). In addition the following are also implemented:

-   {% include key key='H' %} - Selects the <u>H</u>and (rotation) tool.
-   {% include key key='W' %} - Selects the <u>W</u>and (selection) tool.
-   {% include key key='Esc' %} - Shuttles between the Hand and Wand tool after both have been selected at least once.

### Other

There are other key and mouse combinations used in e.g., [Sholl Analysis (by Focal Point)](/plugins/snt/analysis#sholl-analysis), and [Branching and Joining Paths](/plugins/snt/step-by-step-instructions#branching-start-a-path-on-an-existing-path), that are listed in the contextual menu, displayed when righ-clicking a tracing canvas.


{% capture tip%}
SNT was designed so that its shortcuts do not collide with those of ImageJ. SNT hotkeys do not require holding down {% include key key='Control' %} ({% include key key='Cmd' %} on MacOS). When such a modifier key is pressed, the hotkey will no longer be intercepted by SNT. E.g., During a tracing session pressing {% include key key='S' %} will toggle cursor snapping while Pressing {% include key keys='Control|S' %} ({% include key keys='Cmd|S' %}on MacOS) will allow you to save the traced image using IJ"s built-in command {% include bc path='File|Save'%}.
{% endcapture %}
{% include notice icon="tip" content=tip %}
