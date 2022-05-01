---
title: 2009-06-26 - TrakEM2 0.7i now with non-linear transforms and fast marching region growth
---

[TrakEM2](/plugins/trakem2) has been updated to version 0.7i

Please call "Help - Update Fiji" to get the new TrakEM2\_.jar and updated dependency jars into your plugins folder.

The update includes:

-   Manual non-linear registration mode, multi-tile.
-   Region growing via Erwin Frise's fast marching implemention in the [Level Sets library](/plugins/level-sets). Just select an AreaList and click anywhere on an image using the pencil tool. Adjust algorithm parameters via right-click "Display - Adjust fast-marching parameters...".
-   Preprocessor scripts in jython, javascript and beanshell.
-   Grid overlays in calibrated units.
-   Speedups for label importing from tif or amira into AreaList.

And many more. See [all TrakEM2 0.7i new features and fixes](http://t2.ini.uzh.ch/trakem2.html).

The new manual non-linear transform mode is mostly the work of [Stephan Saalfeld](http://fly.mpi-cbg.de/saalfeld).

Thank you to [Mitya Chklovskii](http://research.janelia.org/Chklovskii) for generously hosting a TrakEM2 development event.


