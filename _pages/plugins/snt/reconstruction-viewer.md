---
title: SNT › Reconstruction Viewer
nav-links: true
nav-title: Rec. Viewer
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
---

{% capture version%}
**This page was last revised for [version 5.0.0](https://github.com/morphonets/SNT/releases)**.<br>
Please help us to keep up-to-date documentation by [editing](https://github.com/imagej/imagej.github.io/edit/main/_pages/plugins/snt/reconstruction-viewer.md) this page directly to fill in any documentation gap. Do [reach out](https://forum.image.sc/tag/snt) if you need assistance!
{% endcapture %}
{% include notice content=version %}


# Overview
SNT's Reconstruction Viewer is a 3D visualization tool for both surface meshes and skeletonized reconstructions of neurons. It can be used as a standalone program or from within SNT. Some of its features include:

 - Interactive scenes (controlled rotations, panning, zoom, scaling, animation, dark/light theme)
 - Support for axes, transparency, color interpolation, path smoothing, and geometric annotations (surfaces, meshes, vectors, planes, etc.)
 - Tools for management and customization of scene elements
 - Loading of surface meshes of several template brains (Drosophila, zebrafish, and mouse (Allen CCF))
 - Render both local and remote files on the same scene
 - Render scenes via GPU (the default), via CPU, or offscreen (headless)
 - Generate scenes programmatically via scripting

<div align="center">
  <img src="/media/plugins/snt/snt-rec-viewer-demo2-dark.gif" title="Dark mode (MouseLight scene)" width="48%" alt="Dark mode (MouseLight scene)" />
  <img src="/media/plugins/snt/snt-rec-viewer-demo1-light.gif" title="Light mode (MouseLight scene)" width="48%" alt="Light mode (MouseLight scene)" />
</div>


# Starting the Viewer
Reconstruction Viewer may be used as either a standalone program or from within SNT:

 - To open a standalone instance, press the "SNT" icon in the ImageJ toolbar and choose "Reconstruction Viewer" from the {% include bc path='Neuroanatomy Shortcuts Window'%}. **This is the preferred way to visualize and quantify existing reconstructions**.

 - To open the program from within SNT, use the "Open Reconstruction Viewer" option in the 3D tab of the SNT dialog. Note that for performance reasons some Path Manager changes may need to be synchronized manually from RV controls.


# Scene Interaction
The display canvas supports multiple modes of interaction, including controlled rotations, panning, zoom, scaling, animation, and alternation between "dark" and "light" modes. Basic navigation controls include:

| Rotate | {% include key keys='Left Drag' %} &nbsp; or &nbsp; {% include key key='left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} |
| Pan | {% include key keys='Right Drag' %} &nbsp; or &nbsp; {% include key key='shift' %} + {% include key key='left' %} {% include key key='right' %} {% include key key='up' %} {% include key key='down' %} |
| Zoom | {% include key keys='Mouse Wheel' %} &nbsp; or &nbsp; {% include key key='+' %} {% include key key='-' %} |
| Animate | {% include key keys='Double Click' %} |
| Snap to top/side view | {% include key keys='CTRL|Left Click' %} |

The [full list of keyboard shortcuts](/plugins/snt/key-shortcuts#reconstruction-viewer) is found by pressing the {% include key key='H' %} (<i><u>H</u>elp notification</i>) or {% include key key='F1' %} (separate window), or by using the [Scene Controls](#scene-controls) menu.

{% capture coordinates%}
_Reconstruction viewer_ is a generic visualization tool, supporting multiple species/animal models. Scenes are  defined under Cartesian coordinates, not anatomical. As a consequence, the preset views obtained when control-clicking the scene correspond to XY, YZ, ZY planes, which may not reflect anatomical axes. E.g., the coronal view of the Allen [reference brain](#reference-brains) for the adult mouse is mapped to YZ, which may seem unexpected.
{% endcapture %}
{% include notice icon="info" content=coordinates %}


# RV Controls
The RV Controls dialog is the Reconstruction Viewer equivalent to the [Path Manager](/plugins/snt/manual#path-manager) in SNT's tracing interface. It allows you to control and customize the objects displayed in the scene. Note that only interactive instance of the viewer display this dialog. Those generated programmatically via scripting may omit it. The dialog is organized as follows:

## Scene Controls
This menu provides control over the rendered scene.
<img align="right" src="/media/plugins/snt/snt-recviewer-scene-controls.png" title="Scene Controls" width="300" />

### Toggle Dark Mode
Switches between dark and light theme. Shortcut: {% include key key='D' %}

### Fit to Visible Objects
Computes a bounding box containing all objects of the scene and adjusts the zoom level to ensure all objects are within the camera view. Shortcut: {% include key key='F' %}

### Fit to Selection
Zooms into the object(s) currently selected in the object list.

### Impose Isotropic Scale ›
Squares the aspect ratio of the selected dimensions, leaving the others unchanged. Default is _None_.

### Axes ›
Controls to label, toggle and change the orientation of the cartesian axes of the scene. The 'Flip axis' commands may be useful to mitigate mismatches between cartesian and anatomical orientations.

### Stretch-to-Fill
Stretches the projection on the whole viewport. NB: This may distort proportions in the scene.

### Viewer Size...
Allows fine-control over the viewer dimensions (useful for, e.g., resizing the viewer to known dimensions before recording an animation).

### Full Screen
Enters full screen mode ({% include key keys='Shift|F' %}). To exit full screen press {% include key key='ESC' %}

### Reset View
Resets the view point, view mode, and zoom level, fitting and centering all scene objects into the camera view. Shortcut: {% include key key='R' %}

### Reload Scene
Resets the view and checks if all the drawables in the scene are being rendered properly. If not, allows the scene to be rebuilt completely. Shortcut: {% include key keys='CTRL|R' %}

### Rebuild Scene
Clears all objects from the scene then rebuilds them from scratch. Shortcut: {% include key keys='CTRL|SHIFT|R' %}

### Wipe Scene
Removes all objects from the scene (this action is undoable).

### Scene Shortcuts...
Displays the viewer's hotkeys. Shortcut: {% include key keys='F1' %}

### Duplicate Scene
Stores the current scene into a new non-interactive instance of the viewer to allow side-by-side rendering of detailed scenes.

### Sync Path Manager Changes
This option is only available when the viewer was initialized from SNT. It ensures any pending changes performed in the Path Manager percolate into the 3D scene. Shortcut: {% include key keys='CTRL|SHIFT|S' %}


## Neuronal Arbors
This menu relates to the import, customization and management of reconstructions and is organized into three sections.
<img align="right" src="/media/plugins/snt/snt-recviewer-arbor-controls.png" title="Neuronal Arbors" width="300" />

### Add Neuronal Arbors

#### Load File...
Imports and renders a single reconstruction file (".swc", ".traces", ".ndf", or ".json").

#### Load Directory...
Imports and renders reconstruction files in a directory (filename pattern matching supported).

#### Load & Compare Groups
Allows import and rendering of groups of cells while performing morphometric comparisons between groups (including statistical reports and two-sample t-test/one-way ANOVA analysis). Color-coded montages of analyzed groups can also be generated. It is a modified alias for {% include bc path='Utilities|Compare Reconstructions...'%} in the [tracing UI](/plugins/snt/manual#compare-reconstructionscell-groups). See [Comparing Reconstructions](/plugins/snt/analysis#comparing-reconstructions) for details.

#### Load Demo(s)...
Loads [demo](/plugins/snt/manual#load-demo-dataset) subsets that can be open directly into the viewer.

#### Load From Database ›
Allows import and rendering of reconstruction files fetched from the [FlyCircuit](http://www.flycircuit.tw/), [InsectBrain](https://www.insectbraindb.org/), [MouseLight](https://ml-neuronbrowser.janelia.org/), and [NeuroMorpho](https://neuromorpho.org/) remote databases.

### Customize & Adjust Neuronal Arbors
This sections lists commands to modify the way reconstructions are displayed (colors, transparencies, etc.).

#### All Parameters...
Allows customization of color, transparency and thickness of neurites in a single dialog

#### Color...
Changes the (opaque) color of selected reconstructions.

#### Color Mapping ›
This menu includes commands that apply morphometric color mapping to selected reconstructions, so that a quantitative trait gets mapped to a color ramp (lookup table). Typically, such mapping will render reconstructions under a color gradient, with warmer hues depicting higher values of the mapped metric. It includes two options:

- {% include bc path='Color Mapping|Individual Cells...'%} Assigns color mappings to each cell independently in the ensemble of selected cells
- {% include bc path='Color Mapping|Groups of Cells...'%} Assigns color mappings using metrics retrieved for the ensemble of selected cells

Legends can be edited using [Color Mapping Legends ›](#color-mapping-legends-). This menu also includes commands to remove existing color mappings, and an option to assign unique (distinctive) colors to selected cell(s).

#### Thickness...
Specifies a constant thickness to be applied to the selected reconstructions. Confusingly, thickness is set using an arbitrary scale ranging from 1 (thinnest) to 8 (thickest).

#### Soma Radius...
Applies a constant radius (in physical units) to the soma(s) of selected reconstructions. Note that this requires nodes to be explicitly tagged as soma during import.

#### Translate...
Specifies a translation to be applied to selected reconstructions.

### Remove Neuronal Arbors
This section of the menu includes commands for deleting reconstructions from the scene. Note that you can also remove objects using the [contextual menu](#contextual-menu).

## 3D Meshes
This menu includes commands for loading, managing, and customizing 3D meshes commonly used to represent surface meshes of anatomical structures, neuropil labels, or brain compartments. Currently only Wavefront OBJ files are supported. It is also organized in three sections:
<img align="right" src="/media/plugins/snt/snt-recviewer-mesh-controls.png" title="3D Meshes" width="300" />

### Add Meshes
Includes commands for import and rendering of Wavefront OBJ files, or folders containing multiple files.

### Customize Meshes
Includes commands for adjustment of the color and transparency of the selected mesh(es) and/or their computed bounding boxes, including color, transparency (as percentage), visibility of bounding box, etc.

### Remove 3D Meshes
This section of the menu includes commands for deleting meshes from the scene. Note that you can also remove objects using the [contextual menu](#contextual-menu).


## Geometric Annotations
This menu includes commands for handling geometric annotations such as points, vectors, surface, and cross-section planes.

<img align="right" src="/media/plugins/snt/snt-recviewer-annot-controls.png" title="Geometric Annotations" width="350" />

### Add Annotations
Commands for adding cross-section planes, surfaces, as well as simpler primitives (spheres, vectors, and planes). Annotations can be split in two categories:

#### Cross-section planes
Cross-section planes can be cell-based or mesh-based:

- Cell-based: Cross-section planes can be rendered in either X,Y,Z axis along the centroid (mid-plane) of either dendrites, or axons, or at the center of cell soma
- Mesh-based: Cross-section planes can be rendered in either X,Y,Z axis along the centroid (mid-plane) of the mesh

#### Surfaces
Similarly to [convex hulls](#convex-hull), surfaces reflect enclosing polyhedrons. Surfaces can also be of two types:

- Cell-based: Cell-based surfaces can be assembled from the point cloud defined by branch-points or tips of a neuronal arbor
- Mesh-based: Mesh-based surfaces can be assembled from the point cloud of the mesh's vertices associated with either the left or the right hemisphere (bilaterians model organisms)

{% include img align="right" name="Geometric annotations" src="/media/plugins/snt/snt-recviewer-geometric-annot.png" caption="Geometric annotations: Surfaces and planes" %}



#### Misc ›
This menu includes controls for adding 3D primitives to the scene including, parallelograms, spheres, or vectors at specified coordinates.


### Customize Annotations
This section contains commands to modify the color, transparency, etc. of annotations, as well as more advanced options, including:

- Color Gradient: Display the annotation under a hue gradient along a specified axis. NB: Transparency levels of color gradients may not be adjustable
- Surface Rendering: Adjusts the ambient, diffuse, and specular lighting model of objects. This option is only available for simple 3D primitives such as spheres and vectors

### Remove Annotations
This section of the menu includes commands for deleting annotations from the scene. Note that you can also remove objects using the [contextual menu](#contextual-menu).


## Reference Brains
<img align="right" src="/media/plugins/snt/snt-recviewer-atlas-controls-navigator.png" title="Reference Brains and CCF Navigator" width="500" />
This menu allows import of neuropil meshes for Drosophila, zebrafish, and mouse. Several reference brains and anatomical compartments are available either locally (offline) or through direct download (internet connection required).

The menu is organized by animal model:

- **Mouse (Allen CCF Navigator)**: Import and navigation system for the Allen Adult Mouse Common Coordinate Framework (CCF). The Navigator automatically loads the CCF outline mesh, and presents a searchable hierarchy of CCF(v3) ontologies that can be downloaded into the scene.

  For further details:
  - [Allen Brain Reference Atlases](https://atlas.brain-map.org/)
  - [CCF: 2D Atlas Viewer](https://atlas.brain-map.org/atlas?atlas=602630314)
  - [CCF: 3D Atlas Viewer](https://connectivity.brain-map.org/3d-viewer)

- **Zebrafish**: Offline access to the [Max Planck Zebrafish Brain Atlas](https://mapzebrain.org/home) template

- **Drosophila**: Support for multiple neuropils:
  - Templates for adult brain (e.g., [FCWB](http://dx.doi.org/10.5281/zenodo.10568), [JRC 2018 unisex brain template](https://www.janelia.org/open-science/jrc-2018-brain-templates), [JFRC2](http://natverse.org/nat.flybrains/reference/JFRC2.html), [JFRC3](http://natverse.org/nat.flybrains/reference/JFRC2013.html)) and Ventral Nerve Cord ([JRC 2018 unisex VNC](https://www.janelia.org/open-science/jrc-2018-brain-templates))
  - Larval stages, including 1st (L1) and 3rd instar (L3)
  

  For further details:
  - [Virtual Fly Brain - Templates](https://www.virtualflybrain.org/docs/concepts/templates/)
  - [natverse - Drosophila Template Brains](http://natverse.org/nat.flybrains/reference/#drosophila-template-brains)
  - {% include citation doi='10.1371/journal.pone.0236495' %}

## Analyze & Measure
<img align="right" src="/media/plugins/snt/snt-recviewer-measure-controls.png" title="Analyze and Measure" width="400" />
This menu houses commands to measure and analyze loaded reconstructions. Most are described in [Analysis](./analysis).

### Tabular Results
Includes two commands:
- {% include bc path='Measure...' %} Provides a comprehensive selection of measurements to be extracted from selected cells. See [Analysis › Measurements](/plugins/snt/analysis#measurements) for details
- {% include bc path='Quick Measurements...' %} Convenience shortcut for running {% include bc path='Measure...' %} with common metrics

### Distribution Analysis
Includes two commands:
- {% include bc path='Branch Properties...' %} Measures all branches of the currently selected reconstructions (without considering cell identity) and plots frequencies of the chosen metric. Enabling quantification of branch properties across a population.
- {% include bc path='Cell Properties...' %} Plots frequencies of single-cell measurements.


### Specialized Analysis

#### Convex Hull...
Computes and displays the convex hull of a reconstruction (i.e., the smallest convex polygon/polyhedron that contains a neuronal arbor). Convex hull measurements are defined in [Metrics](/plugins/snt/metrics#convex-hull-boundary-size). Note that it is also possible to define polyhedron based on subsets of nodes (e.g., branch points) using [surface annotations](#surfaces).

#### Create Dendrogram
Generates a Dendrogram plot of single cells. See [Graph-based Analysis](/plugins/snt/analysis#graph-based-analysis).

#### Persistence Homology...
See [Analysis › Persistence Homology](/plugins/snt/analysis#graph-based-analysis).

#### Sholl Analysis...
Runs [Sholl Analysis](/plugins/snt/sholl#analysis-of-traced-cells) on single cells.

#### Strahler Analysis...
Conducts [Strahler Analysis](/plugins/snt/analysis#strahler-analysis) on single cells.

{% include gallery align="center" content=
"
/media/plugins/snt/snt-combined-histograms.png | [Distribution Analysis](#distribution-analysis)
/media/plugins/snt/snt-recviewer-convexhull-and-surface.png | [Convex Hull](#convex-hull)
/media/plugins/snt/graph-viewer-dendrogram-simple.png | [Create Dendrogram](#create-dendrogram)
/media/plugins/snt/sholl-analysis-outputs.png | [Sholl Analysis](#sholl-analysis)
/media/plugins/snt/strahler-analysis-from-reconstructions.png | [Strahler Analysis](#strahler-analysis)
/media/plugins/snt/sankey-flow-plot-with-tooltip.png | [Annotation Graph](#annotation-graph)
/media/plugins/snt/snt-brain-analysis-ipsi-contra.png | [Brain Area Frequencies](#brain-area-frequencies)
"
%}

### Atlas-based Analysis

#### Annotation Graph

<img align="right" src="/media/plugins/snt/snt-annotation-graph-prompt.png" title="Annotation Graph... prompt" width="400" />
Creates [annotation graphs](/plugins/snt/analysis#annotations-graphs) (e.g., Ferris wheel and Flow (Sankey) diagrams) from one or more cells. See [Analysis › Annotation Graphs](/plugins/snt/analysis#annotations-graphs) for details.


#### Brain Area Frequencies
Measures the amount of cable length, number of terminal nodes, or both that occur in distinct anatomical regions of the brain, with the option to restrict the analysis up to a maximum depth in the ontology hierarchy. See [Analysis › Brain Area Frequencies](/plugins/snt/analysis#brain-area-frequencies) for details.

### Data Export
Allows saving of any tabular measurements and plots generated by analysis commands. Tables are saved as {% include wikipedia title="Comma-separated values" %}, while plots are saved as images. Note that individual plots can be exported to PDF/SVG using the plot's contextual menu.

## Utilities &amp; Actions
<img align="right" src="/media/plugins/snt/snt-recviewer-util-controls.png" title="Utilities" width="450" />

### Utilities

#### Annotation Label...
Adds a text label with options to customize font size, style, color, rotation angle, and location.

#### Color Mapping Legends ›
Contains options to add, edit, or remove [Color Mapping](#color-mapping-) legends.

#### Create Figure...
Only available in standalone viewers. See [Manual › Create Figure...](/plugins/snt/manual#create-figure).

#### Light Controls...
Adjustments of light and shadows. Note these are currently experimental features.

#### Record Rotation
Animates a rotation of the current scene and saves each frame to disk. The save directory, rotation degree, duration and frames per second may be adjusted in [Preferences](#other).


### Screenshots
Commands for handling scene snapshots, including:

- {% include bc path='Take Snapshot & Display'%} Takes a snapshot of the current scene and displays it in ImageJ
- {% include bc path='Take Snapshot & Save to Disk'%} Saves a PNG image of the current scene to disk. The default directory may be changed in [Preferences](#other). Snapshot: {% include key key='S' %}
- {% include bc path='Show Snapshot Directory'%} Opens the snapshot export directory in the native file explorer


## Scripting
Commands to create scripts, including:
<img align="right" src="/media/plugins/snt/snt-recviewer-script-controls.png" title="Scripting" width="450" />

- {% include bc path='Record Script...'%} Starts the [Script Recorder](/plugins/snt/scripting#script-recorder). Shortcut: {% include key key='[' %}
- {% include bc path='Log Scene Details to Recorder'%} Logs detailed information about the current scene (e.g., currently visible objects, API calls, etc.) to the Console. This facilitates programmatic control over the Viewer's scene, since logged info can be used directly in scripts. Shortcut: {% include key key='L' %}


## Settings
Options and global settings. It is divided in 4 sections:
<img align="right" src="/media/plugins/snt/snt-recviewer-setting-controls.png" title="Settings" width="500" />

### Layout
Includes options to toggle the visibility of the _RV Controls_ dialog (typically hidden in full screen). Shortcut: {% include key keys='SHIFT|C' %}


### Keyboard & Mouse Sensitivity
This section contains options for sensitivity of mouse and keyboard scene interaction. Note that a default shared sensitivity parameter can be specified for panning, zooming and rotating (using hotkeys) in the {% include bc path='Global Preferences...'%} dialog, including

- {% include bc path='Pan Accuracy| '%} Sets the responsiveness of panning. A lower step size is more responsive
- {% include bc path='Zoom Steps (+/- Keys)| '%} Sets the percentage of a single zoom step via {% include key key='+' %} {% include key key='-' %} keys
- {% include bc path='Rotation Steps (Arrow Keys)| '%} Sets the number of degrees of a single rotation step via {% include key key='left' %} {% include key key='right' %} keys


### Advanced Settings
Includes advanced controls such as:

- {% include bc path='Debug Mode'%} Logs detailed information about commands usage, including warnings and errors to the Console
- {% include bc path='Enable Hardware Acceleration'%} Sets hardware accelerated 3D graphics

### Other
Sets persisting preferences for snapshot recordings, keyboard and mouse controls, and the preferred scripting language for the Viewer. Persistent preferences apply across viewers and sessions.


## Command Palette
Triggered by {% include key keys='ctlcmd|Shift|P' %}. See [User Manual › Command Palette](/plugins/snt/manual#command-palette).


## Contextual Menu
<img align="right" src="/media/plugins/snt/snt-recviewer-contextual-menu.png" title="Contextual Menu" width="300" />

Lists commands to select, show, or hide objects and their components (e.g., {% include bc path='Show Soma of Selected Trees' %}, or {% include bc path='Hide Bounding Box of Selected Meshes' %}), as well as other utilities. Noteworthy:

### Add Tag(s)
Adds one or more tags (space or comma-separated list) to selected items. Tags encoding a color (e.g., 'red', 'lightblue', or '#FFB300') are used to highlight entries. Note that it is also possible to double-click on an object to edit its tags. Shortcut: {% include key keys='ctlcmd|Shift|T' %}

### Apply Scene-based Tags
Tags selected entries with their respective rendering colors. Assumes selected objects are monochromatic.

### Label Categories
Tags listed entry with the icon corresponding to their type (reconstruction, annotation, or mesh).

### Sort List
Sorts the list alphabetically.

### Toggle Selection Toolbar
<img align="right" src="/media/plugins/snt/snt-recviewer-selection-toolbar.png" title="Selection Toolbar" width="300" />

Allows objects to be searched and filtered, functioning similarly to [Path Manager's Filter Toolbar](/plugins/snt/manual#filter-toolbar). Shortcut: {% include key keys='ctlcmd|F' %}


# Advanced Scenes
Advanced scenes are generated via scripting. The _Render_ collection of [template scripts](/plugins/snt/scripting#bundled-templates) demonstrates how to use the viewer in headless mode, and how to generate programmatic scenes.
