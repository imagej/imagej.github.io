---
mediawiki: BigStitcher_BDV
title: BigStitcher › BigDataViewer
nav-links: true
nav-title: BDV
---

## Displaying selected views in BigDataViewer

If your dataset is in a format suitable for quick visualization by [BigDataViewer](/plugins/bdv) (e.g. multiresolution HDF5 or virtually loading), a BigDataViewer window in which selected Views can be visualized will open along with the BigStitcher main window. For other datasets, you can open BigDataViewer manually via the **right-click menu** by clicking {% include bc path='Displaying|Display in BigDataViewer(on/off)'%}. If a BigDataViewer window is currently open, clicking this will close it.

For help on using BigDataViewer, you can either click {% include bc path='Help|Show Help'%} in the BigDataViewer window or consult the BigDataViewer [documentation](/plugins/bdv#usage) on this Wiki.

{% include thumbnail src='/media/plugins/bigstitcher/bigstitcher-bdv-colormode.png' title='Toggle per-view and per-channel coloring by pressing **c** in the main window.'%}

In the BigDataViewer window accompanying the BigStitcher, you can switch between color schemes by pressing {% include key key='c' %} in the BigSitcher main window. A single press will switch between per-view and per-channel coloring. Pressing {% include key key='c' %} repeatedly will cycle through different colors.

## Displaying selected views as ImageJ images

In addition to toggling the BigDataViewer, you can also display selected views one-by-one as standard ImageJ images using the **Displaying** functions in the **right-click menu**.

-   Using {% include bc path='Displaying|Display Raw Image(s)'%}, you can open the selected views as 16-bit or 32-bit images in ImageJ.

<!-- -->

-   Using {% include bc path='Displaying|Max-Projection'%}, you can generate maximum-intensity projections of the selected view stacks and display them as ImageJ images.

Go back to the [main page](/plugins/bigstitcher#Documentation)
