---
mediawiki: Sync_Windows
title: Sync Windows
categories: [User Interface]
artifact: sc.fiji:Sync_Win
---

The Sync Windows plugin synchronizes mouse motion and input between multiple windows. Thus, an ROI drawn in one window is replicated in all other synchronized windows in the synchronized window set. A synchronization cursor (the red box above) indicates the location of the mouse in all synchronized windows.

## Installation

**ImageJ**: Copy the Sync\_Win.jar file from /ij/plugins/download/jars/Sync_Win.jar into the ImageJ/Plugins folder and either restart ImageJ or run the {% include bc path='Help | Update Menus'%} command. After this two new commands should appear in {% include bc path='Analyze | Tools'%}: **Sync Windows** and **Sync Measure 3D**.

**Fiji**: this plugin is part of the Fiji distribution, there is no need to download it.

## Use

The command {% include bc path='Analyze | Tools | Sync Windows'%} opens a dialog that allows to choose what features should be synchronized:

-   Sync Cursor
-   Sync Channels
-   Image Coordinates
-   Sync z-Slices
-   Sync t-Frames
-   Image Scaling

Clicking on **Synchronize All** starts synchronizing all windows, clicking on **Unsynchronize All** stops synchronization.

<img src="/media/plugins/sync-win.png" width="750"/>

 
