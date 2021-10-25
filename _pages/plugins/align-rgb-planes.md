---
title: Align RGB planes
project: ImageJ
categories: [Color Processing]
name: Align RGB planes
website: https://blog.bham.ac.uk/intellimic/g-landini-software/
team-founders: Gabriel Landini | /people/landinig
team-leads: Gabriel Landini | /people/landinig
team-maintainers: Gabriel Landini | /people/landinig
dev-status: Stable
source-label: align_rgb.zip
source-url: https://github.com/landinig/IJ-Align_RGB_planes/raw/main/align_rgb.zip
release-date: 27 March 2007
---

## Documentation

From the plugin inline help:

<blockquote markdown=1>

<u>Align RGB planes</u> v1.7 by G.Landini

Changes the alignment of the RGB planes independently.

*Red* *Green* and *Blue* checkboxes switch ON and OFF the planes and undo the alignment since last plane change. Note that when switching planes, the portion of the previously edited plane left outside the image frame is lost. Rotation, Width and Height changes are interpolated (so there is some loss of sharpness) and do not retain the image portions outside the image frame. You can use the **Resize2Rotate** macro to avoid losing any image data.

The *Rotate*, *Width* and *Height* sliders set integer values, but fractional values can also be typed in the entry boxes. Just make sure you press {% include key key="RETURN" %} after the number is typed.

The {% include button label="Revert" %} button works only with single images, not stacks.

Note: When using stacks, 2 buttons {% include button label="< Prev" %} and {% include button label="Next >" %} are added to the panel. Do not use the slide bar in the stack window, but use those buttons instead.

</blockquote>

## Version history

-   v1.0 12/Jan/2004 released
-   v1.1 12/Feb/2004 avoids error if image does not exist
-   v1.2 27/May/2005 added rotation of the planes, reverting resets the plane checkboxes
-   v1.3 30/May/2005 added stretching of the planes, requires 1.34o
-   v1.4 9/Jun/2005 added log output based on Leon Espinosa modification
-   v1.5 12/Jun/2005 fixed stretching handling
-   v1.6 12/Jun/2005 fixed window closing
-   v1.7 28/Mar/2007 supports RGB stacks

 
