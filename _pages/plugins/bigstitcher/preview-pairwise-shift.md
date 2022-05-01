---
mediawiki: BigStitcher_Preview_Pairwise_shift
title: BigStitcher › Preview Pairwise Shift
nav-links: true
nav-title: Preview Pairwise Shift
---

The second step of the stitching process after the pairwise shifts between views has been calculated is previewing the links and correlation coefficients. It is important to screen the results and remove erroneous links.

If you are running the **Stitching Wizard**, you will be taken to **Interactive Link Explorer** immediately after calculating pairwise shifts. Otherwise, you can find the link verification functions in the right-click menu under **Step-by-step Stitching**:

<img src="/media/plugins/bigstitcher/bigstitcher-stitch-4-0.png" width="600"/>

-   **Interactive Link Explorer ...** will open a window allowing you to preview the calculated pairwise shifts, filer them based on criteria such as cross correlation and remove individual bad links.

{% include notice icon="info" content='The Interactive Link Explorer will work on the views selected in the main window, the others will be grayed out while it is open' %}

-   **Filter Links by Parameters ...** offers the same functionality as the Interactive Link explorer in a simple dialog without any live preview.
-   **Remove Links** allows you to remove the calculated shifts, either for the currently selected views or for all views.

## Interactive Link Explorer

The Interactive Link Explorer allows you to to preview the pairwise links of a view. If you select a view in the main window, its pairwise links will be displayed in the Interactive Link Explorer window.

-   If the BigDataViewer is open, you can see a preview of the transformations for the selected view and its neighbours. At the same time in the **Interactive Link Explorer** window, the calculated cross correlation value and calculated shift will appear.
    -   Here, you can also filter links by correlation coefficient, shift dimensions or shift magnitude.
    -   Selecting a single view pair in the Link Explorer will highlight the two views in the BigDataViewer
    -   Right-clicking on a link in the link explorer brings up a menu that allows you to remove this specific link.

<!-- -->

-   In the link explorer window you can set a minimum and maximum value for the **cross correlation** of the shifts.
-   You can also set filters for **maximum** shift in any dimension or the total shift magnitude.

<!-- -->

-   Apply your filtering criteria to the actual views by clicking **Apply Filter**.

<!-- -->

-   Once you are satisfied with the results, you can click **Apply & Run Global Optimization** to continue with the [global optimization](/plugins/bigstitcher/global-optimization) immediately.

<img src="/media/plugins/bigstitcher/bigstitcher-stitch-4-1.png" width="1000"/>

Go back to the [main page](/plugins/bigstitcher#documentation)
