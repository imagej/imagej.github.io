---
title: 2009-05-15 - Updated TrakEM2 to version 0.7f
---

[TrakEM2](/plugins/trakem2) has been updated to version 0.7f

Please call "Help - Update Fiji" to get the new TrakEM2\_.jar into your plugins folder.

The update includes:

-   Fixes for AreaList mesh generation.
-   Fixes for blending overlapping images: images where width and height were different were failing to blend.
-   Fixes for creating new AreaList, new Pipe, etc: now correctly repainting the first area or point added.
-   Now {% include key keys='Ctrl|A' %} ({% include key keys='Command|A' %} in macosx) selects all but sensitive to object visibility and the presence of a ROI.
-   Now one must {% include key keys='Shift|Left Click' %} the first point to get the Profile to close, or {% include key keys='Shift|C' %} any time to toggle the closed state.

Thanks to [German Koestinger](http://www.ini.uzh.ch/people/german) and {% include person id='axtimwalde' %} for testing and bug reports.


