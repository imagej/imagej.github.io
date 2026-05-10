---
title: SNT › Spine/Varicosity Analysis
nav-links: true
nav-title: Spines/Varicosities
name: Spine/Varicosity Analysis
categories: [Maxima,Analysis,Neuroanatomy]
artifact: org.morphonets:SNT
icon: /media/icons/snt.png
forum-tag: snt
update-site: Neuroanatomy
doi: 10.1038/s41592-021-01105-7
tags: snt,tracing,neuroanatomy,maxima
---


{% capture version%}
**This page was last revised for [version 5.0.10](https://github.com/morphonets/SNT/releases)**.
{% endcapture %}
{% include notice content=version %}

# Spine/Varicosity Analysis

{% capture spot-spine%}
Currently, SNT supports detection, annotation, and density analysis of bright puncta around paths. Complete shape analysis of dendritic spines can be performed using [Spot Spine](/plugins/spot-spine).
{% endcapture %}
{% include notice icon="info" content=spot-spine %}


## Automated Detection
SNT can automatically detect intensity maxima (spines, varicosities, synaptic puncta) in the vicinity of traced paths using the **Peripath Detector**. At each path node, a perpendicular cross-section is sampled from the image, masked to an annular region around the neurite, and analyzed for local maxima via prominence filtering. Detections from adjacent cross-sections are deduplicated automatically. The detection algorithm is the same used by ImageJ's {% include bc path='Process|Find Maxima...' %}

{% capture maxima-demo%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing _Hippocampal neuron (Neuronal receptors)_ or _Hippocampal neuron (Synaptic labeling)_ datasets:

1. Choose a neurite of interest. Adjust cursor size to the neurite thickness using {% include key keys='Ctrl|Mouse Wheel' %}
2. Trace a small path (finish it by {% include key keys='Double Click' %})
3. Run {% include bc path='Analyze|Spines/Varicosities|Detect Maxima Around Paths...' %}

{% endcapture %}
{% include notice icon="tip" content=maxima-demo %}

To run {% include bc path='Analyze|Spines/Varicosities|Detect Maxima Around Paths...' %}, select first the path(s) of interest (or none to include all). The command's dialog provides the following parameters:

- **Detection channel** The image channel to analyze (1-based; only for multi-channel images)

- **Inner radius** The inner boundary of the search annulus. In _Multiplier_ mode, this is a fraction of each node's fitted radius (e.g., 0.5 starts searching at half the local dendrite thickness, catching maxima near the membrane edge). In _Absolute_ mode, a fixed radius in calibrated units. Default multiplier: 1.0

- **Outer radius** The outer boundary of the search annulus. In _Multiplier_ mode, a multiple of each node's radius (e.g., 2.0 searches up to 2× the local thickness). In _Absolute_ mode, a fixed radius in calibrated units. Default multiplier: 2.0

{% capture maxima-membrane%}
To detect puncta specifically at the neurite membrane, use _Multiplier mode_ with a narrow band around 1.0 (e.g., inner = 0.95, outer = 1.05). This creates a thin annulus centered on the membrane edge, assuming paths have been traced with accurate radii.
{% endcapture %}
{% include notice icon="tip" content=maxima-membrane %}

- **Prominence** Noise tolerance for maxima detection, in image intensity units. A maximum is only accepted if it protrudes above its surrounding saddle by at least this value. Higher values yield fewer, more prominent detections. The channel's intensity histogram ({% include bc path='Analyze|Histogram' %}) can help guide this choice: set prominence well above the noise floor (the spread of background intensities) but below the typical peak-to-saddle difference of real features. Default: 5% of the channel's dynamic range

- **Merging distance** Minimum separation between detections in physical units. Nearby detections are merged, keeping the brightest. Set to 0 for automatic (defaults to the outer radius)

- **Output** Results can be exported as _ROIs_ (added to the ROI Manager, grouped per path with path name and color) or as _Bookmarked locations_ (added to the [Bookmark Manager](/plugins/snt/manual#bookmarks-tab))

Detected counts are automatically assigned to each path's spine/varicosity tally. Paths with [fitted radii](./manual#refinefit-) will produce better results, as the annulus adapts to local neurite thickness.


### Advanced: Torus Mask Segmentation

The annular search region used by the Peripath Detector can also be exported as a binary mask via scripting. This generates a 3D torus-shaped volume around each path, defined by the same inner and outer radius parameters used for detection. The mask can then be used to extract or quantify signal in the vicinity of traced neurites independently of detection (e.g., to measure mean fluorescence intensity around dendrites, or to isolate peri-neuronal signal for downstream analysis).

Note that the mask is a voxel-level approximation of the continuous search annulus; small gaps may appear due to discretization. A morphological closing operation can be applied to fill these if a contiguous volume is needed.

See {% include bc path='Scripts|Demos|Peripath Detection Demo' %} ({% include bc path='Templates|Neuroanatomy|Analysis|Peripath Detection Demo' %} in the Script Editor) for a working example that runs detection and generates the torus mask on one of the demo datasets.


## Along-Path Detection (Radius Swellings)

SNT can also detect swellings (boutons, varicosities, blebs) **along** traced paths using the _Along-Path Detector_, which analyzes longitudinal radius profiles. The algorithm works as follows:
- At each node, the node radius is compared to the average radius of its neighbors within a sliding window
- A node is flagged as a swelled candidate when its radius exceeds the neighbor average by a configurable factor
- Optionally, a intensity (brighness) threshold can filter candidates further
- Adjacent candidates are merged via non-maximum suppression

Unlike the Peripath Detector (which searches for bright *off-skeleton* [outside path centerline] maxima in perpendicular cross-sections), the Along-Path Detector identifies *on-skeleton* [along path centerline] swellings, i.e., regions where the neurite itself is wider than its surroundings. This is particularly suited for axonal varicosities and en-passant boutons.

To run {% include bc path='Analyze|Spines/Varicosities|Detect Swellings Along Paths...' %} Select the path(s) of interest. Note that **Paths must have radii**: Paths without radii are skipped. 

The command's dialog provides the following parameters:

- **Swelling factor** A node is flagged when its radius exceeds the average of its neighbors by at least this factor. Default: 1.5 (i.e., 1.5× the local average). Lower values increase sensitivity; higher values restrict detection to more prominent swellings

- **No. of neighbors** Total number of neighboring nodes used to compute the local average radius, split evenly on each side of the test node. Default: 10. Larger values smooth out local noise but may miss closely spaced features

- **Min. intensity** Minimum on-skeleton (centerline) intensity for a detection to be accepted. Three modes: **0** disables intensity filtering (radius-only detection); **-1** auto-computes a threshold as the midpoint of the image's dynamic range; any **positive value** sets an explicit threshold in image intensity units

- **Intensity channel** The image channel for intensity sampling (1-based; only shown for multi-channel images and when intensity filtering is enabled)

- **Merging distance** Minimum separation between detections in physical units. Nearby detections are merged, keeping the one with the highest score. Set to 0 for automatic (defaults to 2× mean radius across all paths)

- **Exclude junctions/tips** When enabled, nodes near branch points and path tips are excluded from detection. These regions may have naturally enlarged radii that produce false positives. The exclusion zone extends by the half-window size on each side of every junction and at each path endpoint. Default: enabled

- **Output** Results can be exported as _ROIs_ (added to the ROI Manager, grouped per path) or as _Bookmarked locations_ (added to the [Bookmark Manager](/plugins/snt/manual#bookmarks-tab))

Detected counts are automatically assigned to each path's spine/varicosity tally, just as with the Peripath Detector.


## Manual Annotation

This approach uses manually placed multi-Point ROIs along paths as markers for neurite features. Currently only counts and densities are supported. A typical workflow proceeds as follows:

{% capture spines-demo%}
You can follow these instructions using {% include bc path='File|Load Demo Dataset...' %} and choosing the _L-systems fractal (Toy neuron)_ dataset.
{% endcapture %}
{% include notice icon="tip" content=spines-demo %}

1. Run {% include bc path='Analyze|Spines/Varicosities|Spine/Varicosity Analysis Help...' %} in the Path Manager to have offline instructions available in a dedicated dialog
2. Pause SNT from the [contextual menu](/plugins/snt/manual#contextual-menu), and select the multipoint tool from ImageJ's toolbar
3. Click over the features to be counted. Point placement may not need to be accurate, but with 3D images points should be placed on the same plane (Z-plane) as the feature being counted. Skip this step if you are running a programmatic routine that automatically annotates locations
4. Once you have placed all the points, select the Path(s) associated with the features (or select none, if all Paths are to be considered) and run Path Manager's {% include bc path='Analyze|Spines/Varicosities|Compute Densities from Annotations...' %}. The dialog allows you to specify:
   
    - **Source of Multi-point ROI(s)** The location of the markers. Particularly useful if the ROIs are being generated programmatically and stored in the ROI Manager. It also allows [bookmarked locations](/plugins/snt/manual#bookmarks-tab) to be parsed as markers
   
    - **Max. association distance** The maximum allowed distance between a point and its path in physical units. This option is ignored if set to -1 (the default). This works as follows: for every point ROI, the closest path node is identified. The ROI is only considered to be associated with a path if its distance to the closest path node is less than or equal to _Max. association distance_.
   
    - **Add extracted counts to ROI Manager** Generates new ROIs from the assigned counts and adds them to the ROI Manager. This allows you to validate the extraction and ensure the assignments are correct, as each ROI gets tagged by its associated Path.

NB:

- Point ROIs can also be generated programmatically or in a semi-automated way, e.g.:
  - Create a freehand area ROI around the path(s) of interest
  - Run ImageJ's {% include bc path='Process|Find Maxima...' %}. Detection will be restricted to the freehand selection

- SNT only keeps a tally of the features being counted and location of ROIs are not saved in .traces files, so you may want to save the multipoint ROIs for future reference

- ImageJ has several ways to expedite handling of multipoint ROIs:
  - {% include key key='left click' %} on a point and drag to move it
  - {% include key key='alt|left click' %} on a point to delete it
  - To delete multiple points, create an area selection while holding down {% include key key='alt' %}
  - Use {% include bc path='Edit|Selection|Select None' %} to delete a multi-point selection
  - Use {% include bc path='Edit|Selection|Restore Selection' %} to restore a deleted multipoint selection
  - {% include key key='double click' %} on the Multi-point tool in the ImageJ toolbar for further options
