---
mediawiki: Lasso_and_Blow_Tool
title: Lasso and Blow Tool
project: /software/fiji
categories: [Segmentation]
artifact: sc.fiji:Lasso_and_Blow_Tool
---

\[this is under construction\]

This selection tool is run from {% include bc path='Plugins | Segmentation | Lasso'%}. Running the plugin adds a new button to the toolbar.

There are 2 modes of operation: **lasso** and **blow** which can be selected by double clicking on the lasso button.

The configuration dialog has a mode selection box (lasso or blow) and a numeric field **ratio space/color** which controls how easily new points are added to the selection. Small values make selection rounder and insensitive to differences in image values, while large values (e.g. 100) restrict the growth of the selection into areas that are dissimilar.

The **lasso** mode, is experimental and not fully functional yet.

The **blow** mode grows a region by adding contiguous points having the same "cost" from the clicked center to the current location under the cursor. To use this, click inside the region to be segmented and drag the mouse within the region. The selection area will "grow" as the mouse cursor is moved away from the clicked point.

## See also

-   [ImageJ 1.x version](https://imagej.nih.gov/ij/plugins/lasso-tool/index.html) of this tool

 
