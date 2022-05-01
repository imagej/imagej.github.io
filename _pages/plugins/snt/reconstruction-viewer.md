---
mediawiki: SNT:_Reconstruction_Viewer
title: SNT › Reconstruction Viewer
nav-links: true
nav-title: Reconstruction Viewer
---

SNT's Reconstruction Viewer is a powerful OpenGL 3D visualization tool for both surface meshes and reconstructions

-   It can be used as a standalone program or from withing SNT
-   Features:
    -   Advanced rendering supporting axes, transparency, color interpolation and path smoothing
    -   Interactive scenes (controlled rotations, panning, zoom, scaling, animation, "dark"/"light" mode)
    -   Tools for management and customization of scene elements
    -   Ability to render both local and remote files on the same scene
    -   Loading of surface meshes of several template brains (Drosophila and Allen CCF (Allen Mouse Brain Atlas))

![](/media/plugins/snt/reconstruction-viewer-animated-gif.gif)

# Starting the Viewer

The Reconstruction Viewer may be used as either a standalone program or from within SNT. To open Reconstruction Viewer as a standalone program, go to {% include bc path='Plugins|NeuroAnatomy|Reconstruction Viewer'%}. To open the program from within SNT, use the "Open Reconstruction Viewer" option in the 3D tab of the SNT dialog. If there are any tracings currently loaded in SNT, they will be displayed in Reconstruction Viewer after opening. Note that, for performance reasons, some Path Manager changes may need to be synchronized manually from RV controls.

# Scene Interaction

The display canvas supports multiple modes of interaction, including controlled rotations, panning, zoom, scaling, animation, and alternation between "dark" and "light" modes. The full list of keyboard shortcuts is found by navigating to {% include bc path='Scene Controls|Scene Shortcuts...'%} from RV Controls, or by pressing {% include key key='H' %} (notification) or {% include key key='F1' %} (separate window) in the Viewer scene. <img src="/media/plugins/snt/reconstruction-viewer-shortcuts.png" title="fig:" width="400" /> {% include clear%}


# RV Controls

## Scene Controls

<img src="/media/plugins/snt/reconstruction-viewer-scene-controls.png" title="fig:" width="400" /> This menu provides control over the rendered scene.

-   {% include bc path='Fit to Visible Objects'%} {% include key key='F' %} Computes a bounding box containing all objects of the scene and adjusts the zoom level to ensure all objects are within the camera view.
-   {% include bc path='Stretch-to-Fill'%} Stretches the projection on the whole viewport.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-not-stretched.png" title="fig:Stretch-to-Fill - disabled" width="200" alt="Stretch-to-Fill - disabled" />
-   <img src="/media/plugins/snt/reconstruction-viewer-stretched.png" title="fig:Stretch-to-Fill - enabled" width="200" alt="Stretch-to-Fill - enabled" />

</div>

-   {% include bc path='Impose Isotropic Scale|  '%} Squares the aspect ratio of the selected dimensions, leaving the others unchanged.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-aspect-ratio-none.png" title="fig:Impose Isotropic Scale - None" width="200" alt="Impose Isotropic Scale - None" />
-   <img src="/media/plugins/snt/reconstruction-viewer-aspect-ratio-zy.png" title="fig:Impose Isotropic Scale - ZY" width="200" alt="Impose Isotropic Scale - ZY" />

</div>

-   {% include bc path='Full Screen'%} {% include key keys='Shift|F' %} Enters full screen mode. To exit full screen press {% include key key='ESC' %}
-   {% include bc path='Reset Scene'%} {% include key key='R' %}
-   {% include bc path='Reload Scene'%} {% include key keys='CTRL|R' %} Resets the zoom level to the default, fitting and centering all scene objects into the camera view. The current rotation setting remains unchanged. Note if some drawables in the 3D scene are not being rendered properly when this option is selected, it will prompt to rebuild the scene completely.
-   {% include bc path='Rebuild Scene...'%} {% include key keys='CTRL|SHIFT|R' %} Clears all objects from the scene then rebuilds them from scratch.
-   {% include bc path='Wipe Scene...'%} Removes all objects from the scene. Note this action cannot be undone.
-   {% include bc path='Sync Path Manager Changes'%} If the 3D scene contains any trees that are currently stored in the Path Manager, re-render these trees to reflect any change in the path structure given by the Path Manager.

## Manage and Customize Neuronal Arbors

This menu relates to the import, customization and management of rendered reconstructions.

### Add

<figure><img src="/media/plugins/snt/reconstruction-manage-arbors-menu.png" width="400" /></figure>

-   {% include bc path='Import File...'%} Imports and renders a single reconstruction file (".swc" or ".traces"). A color may be chosen on import or applied later using the "Customize & Adjust" sub-menu. Note that loaded files will not be listed in the Path Manager.
-   {% include bc path='Import Directory...'%} Imports and renders all reconstruction files in a directory. A single color may be applied to all reconstructions or they may be colored uniquely. Note that loaded files will not be listed in the Path Manager.
-   {% include bc path='Import & Compare Groups...'%} Calls the {% include bc path='Utilities|Compare Reconstructions...'%} command found in the main SNT dialog, allowing import, rendering and comparison of multiple groups of reconstructions.
-   {% include bc path='Load from Database| '%} Allows import and rendering of reconstruction files fetched from the FlyCircuit, MouseLight and NeuroMorpho remote databases.

### Customize & Adjust

-   {% include bc path='All Parameters...'%} Allows customization of color, transparency and thickness parameters by neurite compartment in a single dialog.
-   {% include bc path='Color...'%} Assigns the chosen homogeneous color to all selected reconstructions.
-   {% include bc path='Color Coding|Individual Cells...'%} Applies morphometric color mapping to selected reconstructions. The chosen LUT is used to assign a metric-based color gradient to each reconstruction.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-color-mapping-individual.png" title="fig:Branch Order and Ice LUT" width="200" alt="Branch Order and Ice LUT" />

</div>

-   {% include bc path='Color Coding|Group of Cells...'%} Applies morphometric color coding to a selected group of reconstruction. Note that this option uses the chosen LUT to assign a homogeneous color to each reconstruction in the group based on the chosen metric.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-color-mapping-group.png" title="fig:No. Branch Points and Ice LUT" width="200" alt="No. Branch Points and Ice LUT" />

</div>

-   {% include bc path='Color Coding|Color Each Cell Uniquely'%} Applies a unique homogeneous color to each selected reconstruction. Note this option will override any previously applied color mapping to the selected reconstructions.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-color-mapping-unique.png" title="fig:Unique Color Coding" width="200" alt="Unique Color Coding" />

</div>

-   {% include bc path='Thickness...'%} Specifies a constant thickness to be applied to the selected reconstructions. Note this value will only affect how Paths are displayed in the Reconstruction Viewer.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-thickness-1.png" title="fig:Thickness = 1.0" width="200" alt="Thickness = 1.0" />
-   <img src="/media/plugins/snt/reconstruction-viewer-thickness-5.png" title="fig:Thickness = 5.0" width="200" alt="Thickness = 5.0" />

</div>

-   {% include bc path='Translate...'%} Specifies a translation to be applied to the selected reconstructions. To avoid overwriting data from a tracing session, this command is only available in the standalone viewer.

### Remove

-   {% include bc path='Remove Selected...'%} Deletes the selected reconstructions from the scene.
-   {% include bc path='Remove All...'%} Deletes all reconstructions from the scene.

## Manage and Customize 3D Meshes

<img src="/media/plugins/snt/reconstruction-viewer-mesh-controls.png" title="fig:" width="250" /> <img src="/media/plugins/snt/reconstruction-viewer-customize-mesh-controls.png" title="fig:{% include bc path='Customize|All Parameters...'%}" width="400" alt="{% include bc path='Customize|All Parameters...'%}" />

### Add

-   {% include bc path='Import OBJ File(s)...'%} Allows import and rendering of Wavefront OBJ files, commonly used to represent surface meshes of anatomical structures.

### Customize

-   {% include bc path='All Parameters...'%} Allows adjustment of the color and transparency of the selected mesh(es) and/or their computed bounding boxes in a single menu.
-   {% include bc path='Color...'%} Allows choice of mesh color from a generic CMYK profile.
-   {% include bc path='Transparency...'%} Sets mesh transparency as a percentage value.

### Remove

-   {% include bc path='Remove Selected...'%} Deletes the selected mesh(es) from the scene.
-   {% include bc path='Remove All...'%} Deletes all imported mesh(es) from the scene.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-obj-transparency-5.png" title="fig:Transparency = 5%" width="300" alt="Transparency = 5%" />
-   <img src="/media/plugins/snt/reconstruction-viewer-obj-transparency-95.png" title="fig:Transparency = 95%" width="300" alt="Transparency = 95%" />

</div>

{% include clear%}


## Reference Brains

This menu allows import of several Drosophila, Zebrafish and Mouse reference brains and anatomical compartments. <img src="/media/plugins/snt/reconstruction-reference-brains-menu.png" title="fig:" width="300" />

### Mouse

-   {% include bc path='Allen CCF Navigator (Adult)'%} Import and navigation system for the Allen Adult Mouse Common Coordinate Framework v3. Selecting this option imports the Whole Brain reference mesh, and presents a GUI allowing search, metadata retrieval, and import/rendering of ontologies contained in the Allen Common Coordinate Framework v3.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-allen-ccf-ontology.png" title="fig:Allen CCF Navigator" width="200" alt="Allen CCF Navigator" />
-   <img src="/media/plugins/snt/reconstruction-viewer-allen-ccf-thalamus-info.png" title="fig:Allen CCF Ontology Info" width="200" alt="Allen CCF Ontology Info" />

</div>

### Zebrafish

-   {% include bc path='Max Planck ZBA'%} Max Planck Zebrafish Brain Atlas

### Drosophila

-   {% include bc path='Adult Brain: FlyCircuit'%} FlyCircuit Drosophila reference brain
-   {% include bc path='Adult Brain: JFRC 2018'%} Janelia Farm Research Campus 2018 Drosophila reference brain
-   {% include bc path='Adult Brain: JRFC2 (VFB)'%} Janelia Farm Research Campus Virtual Fly Brain
-   {% include bc path='Adult Brain: JFRC3'%} Janelia Farm Research Campus Drosophila reference brain (Version 3)
-   {% include bc path='Adult VNS'%} Adult Drosophila ventral nervous system reference
-   {% include bc path='Larva L1'%} Drosophila 1st instar larval stage
-   {% include bc path='Larva L3'%} Drosophila 3rd instar larval stage

<div align="center">

-   <img src="/media/plugins/snt/reconstruction-flycircuit-reference.png" title="fig:FlyCircuit Drosophila (Adult)" width="300" alt="FlyCircuit Drosophila (Adult)" />
-   <img src="/media/plugins/snt/reconstruction-viewer-whole-mouse-thalamus.png" title="fig:Allen Adult Mouse Whole Brain + Thalamus" width="300" alt="Allen Adult Mouse Whole Brain + Thalamus" />
-   <img src="/media/plugins/snt/reconstruction-viewer-zebrafish-reference.png" title="fig:Max Planck ZBA" width="300" alt="Max Planck ZBA" />

</div>

{% include clear%}


## Analyze and Measure

<img src="/media/plugins/snt/reconstruction-viewer-measurement-menu.png" title="fig:" width="300" /> This menu houses several functions to measure and analyze loaded reconstructions.

### Tabular Results

-   {% include bc path='Measure...'%} Calls the {% include bc path='Analysis|Measure...'%} command in the main SNT dialog, allowing selection of specific measurements, with the ability to distinguish neurite compartments. If measuring multiple tracings, the table is sortable by column.
-   {% include bc path='Quick Measurements'%} Calls the {% include bc path='Analysis|Quick Measurements'%} command in the main SNT dialog, producing a table of summary statistics for the loaded reconstructions.
-   {% include bc path='Save Table...'%} Saves all measurements computed during a session to a .csv file.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-measurements-aa0100.png" title="fig:AA0100 Measurements" width="900" alt="AA0100 Measurements" />

</div>

### Distribution Analysis

-   {% include bc path='Branch Properties...'%} Measures all branches of the currently selected reconstructions (without considering cell identity) and plots a histogram of the chosen metric, enabling quantification of branch properties across a population.
-   {% include bc path='Cell Properties...'%} Measures each cell in the currently selected reconstructions individually and plots a histogram of the chosen metric, enabling comparison between individual cells.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-aa0100-distribution-analysis.png" title="fig:AA0100: Branch Order" width="200" alt="AA0100: Branch Order" />
-   <img src="/media/plugins/snt/reconstruction-viewer-op-distribution-analysis.png" title="fig:9 OP fibers: # Branch Points" width="200" alt="9 OP fibers: # Branch Points" />

</div>

### Single-Cell Analysis

{% include img src="reconstruction-viewer-brain-area-analysis" width="300" caption="Brain Area Analysis: Cable Length" %}

-   {% include bc path='Brain Area Analysis...'%} Measures the amount of cable length, number of terminal nodes, or both that occur in distinct anatomical regions of the brain, with the option to restrict the analysis up to a maximum depth in the ontology hierarchy. Note that only one reconstruction may be selected at a time with this option.
-   {% include bc path='Create Dendrogram...'%} Runs the {% include bc path='Utilities|Create Dendrogram...'%} command found in the main SNT dialog. See [Dendrogram Viewer](/plugins/snt/analysis#dendrogram-viewer). Note only one reconstruction may be selected at a time with this option.
-   {% include bc path='Sholl Analysis...'%} Runs the [Sholl Analysis](/plugins/sholl-analysis) plugin found in {% include bc path='Analyze|Sholl|Sholl Analysis (From Tracings)'%}. Note only one reconstruction may be analysed at a time.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-aa0100-sholl-table.png" title="fig:AA0100 Sholl Table" width="200" alt="AA0100 Sholl Table" />
-   <img src="/media/plugins/snt/reconstruction-viewer-aa0100-sholl-plot.png" title="fig:AA0100 Sholl Plot" width="221" alt="AA0100 Sholl Plot" />

</div>

-   {% include bc path='Strahler Analysis'%} Conducts Strahler Analysis on the selected reconstruction. Note only one reconstruction may be analysed at a time.

<div align="left">

-   <img src="/media/plugins/snt/reconstruction-viewer-aa0100-strahler-table.png" title="fig:AA0100 Strahler Table" width="227" alt="AA0100 Strahler Table" />
-   <img src="/media/plugins/snt/reconstruction-viewer-aa0100-strahler-plot.png" title="fig:AA0100 Strahler Plot" width="200" alt="AA0100 Strahler Plot" />

</div>

{% include clear%}


## Utilities

<figure><img src="/media/plugins/snt/reconstruction-viewer-tools-menu.png" title="reconstruction-viewer-tools-menu.png" width="400" alt="reconstruction-viewer-tools-menu.png" /><figcaption aria-hidden="true">reconstruction-viewer-tools-menu.png</figcaption></figure>

### Actions & Utilities

-   {% include bc path='Take Snapshot'%} {% include key key='S' %} Saves a PNG image of the current scene to disk. The default directory may be changed in the Reconstruction Viewer *Preferences*.
-   {% include bc path='Record Rotation'%} Animates a rotation of the current scene and saves each frame to disk. The save directory, rotation degree, duration and frames per second may be adjusted in the Reconstruction Viewer *Preferences*.
-   {% include bc path='Color Legends| '%} Contains options relating to the adding and management of LUT-based color legends.
-   {% include bc path='Light Controls...'%} Adjustments of light and shadows. Note these are currently experimental features, some of which are un-doable.

### Scripting

-   {% include bc path='Script This Viewer'%} Opens an instance of the Script Editor with pre-loaded extensible boilerplate code for advanced scripting of Reconstruction Viewer. For an example of the scripting capabilities of Reconstruction Viewer, see [Scripting Reconstruction Viewer](/plugins/snt/scripting#scripting-reconstruction-viewer). A related script template can also be found in the Script Editor at {% include bc path='Templates|Neuroanatomy|Analysis|Reconstruction Viewer Demo (Python)'%}.
-   {% include bc path='Script This Viewer In...'%} Prompts for selection of scripting language before running the previous command.
-   {% include bc path='Log Scene Details'%} {% include key key='L' %} Logs detailed information about the current scene (e.g., currently visible objects, API calls, etc.) to the Console. This facilitates programmatic control over the Viewer's scene.
-   {% include bc path='Debug Mode'%} Logs detailed information about plugin usage, including warnings and errors to the Console.

{% include clear%}


## Settings

<figure><img src="/media/plugins/snt/reconstruction-viewer-settings-menu.png" title="reconstruction-viewer-settings-menu.png" width="400" alt="reconstruction-viewer-settings-menu.png" /><figcaption aria-hidden="true">reconstruction-viewer-settings-menu.png</figcaption></figure>

### Keyboard & Mouse Sensitivity

A sub-menu with options for sensitivity of mouse and keyboard scene interaction. Note that a default shared sensitivity parameter can be specified for panning, zooming and rotating (using hotkeys) in the {% include bc path='Global Preferences...'%} dialog.

-   {% include bc path='Pan Accuracy| '%} Sets the responsiveness of panning. A lower step size is more responsive.
-   {% include bc path='Rotation Steps (Arrow Keys)| '%} Sets the number of degrees of a single rotation step. Note this preference only applies to rotations made with the Left/Right Arrow keys.
-   {% include bc path='Zoom Steps (+/-) Keys| '%} Sets the percentage of a single zoom step.

### Misc. Preferences

-   {% include bc path='Enable Hardware Acceleration'%} Use hardware accelerated 3D graphics.
-   {% include bc path='Global Preferences...'%} Configurable preferences for snapshot recordings, keyboard and mouse controls, and the preferred scripting language for the Viewer. Preferences persist across plugin sessions.
