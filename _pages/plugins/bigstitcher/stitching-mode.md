---
mediawiki: BigStitcher_Stitching_Mode
title: BigStitcher › Stitching Mode
nav-links: true
nav-title: Stitching Mode
---

After opening a XML file the main windows will appear in the **Stitching Mode**. In this mode all necessary steps for image stitching are performed

### The main window

<img src="/media/plugins/bigstitcher/bigstitcher-overview-1.png" width="1000"/>

-   At the top of the window **(1)**, you can switch between Stitching and MultiView mode.

<!-- -->

-   Also at the top of the window **(2)** the name of the currently open .XML will appear. **Info** shows extended information of all Views in the current XML file. The **Save** button saves all current changes done to the XML.

<!-- -->

-   In the center of the window a list **(3)** shows all available views for the selected Timepoint and Angle.

<!-- -->

-   The views can be grouped by different attributes **(5)**. In this case views are grouped by Channels and Illuminations.

<!-- -->

-   In Stitching mode, only one Timepoint and Angle is displayed. Different Timepoints or Angles are accessed by the drop-down menu at the bottom **(4)**.

### The BigDataViewer window

If the dataset is in a format suitable for quick visualization by [BigDataViewer](/plugins/bdv) (e.g. multiresolution HDF5 or virtually loading), a BigDataViewer window in which selected Views can be visualized will open along with the BigStitcher main window. For other datasets, you can open BigDataViewer manually via the menu.

<img src="/media/plugins/bigstitcher/bigstitcher-overview-2.png" width="1000"/>

### The right-click menu

Select the views you wish to process in the main window and right-click to open a menu with further options.

<img src="/media/plugins/bigstitcher/bigstitcher-overview-3.png" width="500"/>

-   **Displaying (1)** shows functions for displaying the data in BigDataViewer or in ImageJ ([details](/plugins/bigstitcher/bdv)).
-   **Preprocessing (2)** shows functions for manually moving views ([details](/plugins/bigstitcher/manual-translation)), selecting the best illuminations ([details](/plugins/bigstitcher/select-illumination)) and performing flat-field correction ([details](/plugins/bigstitcher/flatfield-correction)).
-   **Stitching Wizard (3)** shows functions that guide you through the stitching process.
-   **Step-by-step Stitching (4)** shows functions to execute the individual steps of the stitching process, [Pairwise shift calculation](/plugins/bigstitcher/pairwise-shift), [Link Preview and Verification](/plugins/bigstitcher/preview-pairwise-shift) and [Global Optimization](/plugins/bigstitcher/global-optimization).

There are also several advanced expert functions for the individual steps in the stitching pipeline ([details](/plugins/bigstitcher/advanced-stitching)).

-   **Registration Refinement (5)** shows functions for refining the alignment via ICP ([details](/plugins/bigstitcher/icp-refinement))
-   **Fusion (6)** shows functions for the fusion of views (or parts thereof) into single output images ([details](/plugins/bigstitcher/fuse)).
-   **Calibration/Transformations (7)** shows functions for removing transformations from the dataset.
-   **Modifications (8)** shows functions for resaving the dataset, e.g. as multiresolution HDF5 ([details](/plugins/bigstitcher/autoloader#options-for-re-saving-as-hdf5)).
-   **Help (9)** contains a link to this documentation.

Go back to the [main page](/plugins/bigstitcher#documentation)
