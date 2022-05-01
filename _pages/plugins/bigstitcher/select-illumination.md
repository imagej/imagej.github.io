---
mediawiki: BigStitcher_Select_illumination
title: BigStitcher › Select Illumination
nav-links: true
nav-title: Select Illumination
---

When views have more than one illumination, you can select the best one by selecting the views you wish to process and clicing {% include bc path='Preprocessing|Select Best Illuminations'%} in the **right-click menu**.

![](/media/plugins/bigstitcher/bigstitcher-illu-1.png)

-   Ticking **Process only selection** will limit the illumination selection to the views currently selected in the main window. Select which views should be processed and if you want to review the selections before applying.

<!-- -->

-   In the **Selection method** you can choose by which method the best illumination is determined. Currently, we support the following selection methods:

{% include thumbnail src='/media/plugins/bigstitcher/bigstitcher-illumselect-benchmark.png' title='**Figure 1:** Performance of the illumination selection methods on the images of a 2 angle, dual-illumination, 2x3 grid dataset. All methods correctly identify the right/left side illumination for the right and left images of the grid.'%}

-   -   **Pick brightest** will pick the illumination direction with the highest mean intensity (for multiresolution datasets, it will be calculated on the lowest resolution images).
    -   **Pick highest mean gradient magnitude** will calculate the mean gradient magnitude in the images via central differences and pick the illumination with the highest value (for multiresolution datasets, it will be calculated on the lowest resolution images).
    -   **Relative Fourier Ring Correlation** will calculate a local relative Fourier Ring Correlation (FRC) and pick the illumination direction with the highest integrated FRC (this is calculated in full-resolution images). You need to specify some parameters for the FRC calculation, please refer to the section on [FRC Quality Control]((/plugins/bigstitcher/frc) for a detailed explanation.

In general, our experience is that all three methods provide similar results, with gradient magnitude and FRC providing more differentiation power in close cases (at the cost of longer compute times), see e.g. **Figure 1**.

-   If the **Show selection results before applying** option was selected a new window showing the assigned illumination for all selected views will appear. The selected illumination can be manually changed for each view by changing the Illumination attribute in the list.

![](/media/plugins/bigstitcher/bigstitcher-illu-2.png)

After selecting the best illumination, only the chosen illumination will be used for the stitching and will appear in the BigDataViewer.

<img src="/media/plugins/bigstitcher/bigstitcher-illu-3.png" width="800"/>

Go back to the [main page](/plugins/bigstitcher#documentation)
