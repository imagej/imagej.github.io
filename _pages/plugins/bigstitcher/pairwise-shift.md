---
mediawiki: BigStitcher_Pairwise_shift
title: BigStitcher › Pairwise Shift
nav-links: true
nav-title: Pairwise Shift
---

The first step in stitching a tiled dataset is determining the pairwise shifts between the views. In the **Stitching Mode** select the views for the pairwise shift calculation. Then right-click and select {% include bc path='Stitching Wizard|Stitch dataset...'%}. The **Stitching wizard** will guide you through the three steps of pairwise shift determination, link verification and global optimization.

-   If you just want to determine pairwise shifts and skip the other steps, you can use {% include bc path='Step-by-step Stitching|Calculate Pairwise Shifts...|Phase Correlation'%}

<!-- -->

-   Aside from the default **Phase correlation** algorithm for shift determination, we also offer alignment via the Lucas-Kanade method or interest point registration, as well as expert view grouping options. For those advanced methods, refer to [BigStitcher\_Advanced\_stitching](/plugins/bigstitcher/advanced-stitching)

<img src="/media/plugins/bigstitcher/bigstitcher-stitch-0.png" width="600"/>

### Pairwise shift calculation

After starting the stitching process, you need to specify how to handle multiple channels (if present) and which downsampling to use.

-   If your dataset has multiple channels, you will be asked which channel to use for the stitching. You can also average the channels for the stitching process.

<img src="/media/plugins/bigstitcher/bigstitcher-stitch-1.png" width="600"/>

-   Next, choose the the downsampling in x,y,z to be used for the calculation. Select a predefined downsampling factor or choose your own.

{% include notice icon="info" content='In our experience, some downsampling (2-4x) improves results over using raw image data, as it reduces noise in the images. It also dramatically speeds up computations, so we advise using moderate downsampling in this step' %}

<img src="/media/plugins/bigstitcher/bigstitcher-stitch-2.png" width="600"/>

-   If you ran the **Stitching wizard**, you will be asked to proceed to [Link Preview Mode](/plugins/bigstitcher/preview-pairwise-shift). Otherwise, you can proceed to this step via the right-click menu.

Go back to the [main page](/plugins/bigstitcher#documentation)

{% include notice icon="warning" content='When calculating pairwise shifts, we use only the **overlapping parts of two views**. This reduces the amount of data we have to look at and speeds up the computation, but might lead to incorrect results if the initial overlap (e.g. the positions loaded from metadata or manual grid specification) of the images is too small.' %}
