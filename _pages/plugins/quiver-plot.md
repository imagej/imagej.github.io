---
mediawiki: Quiver_Plot
title: Quiver Plot
categories: [Visualization]
---


{% capture author%}
{% include person id='llamero' %}
{% endcapture %}

{% capture maintainer%}
{% include person id='llamero' %}
{% endcapture %}

{% capture source%}
{% include github org='llamero' repo='Quiver_Plot' %}
{% endcapture %}
{% include info-box name='Quiver Plot' software='plugin' author=author maintainer=maintainer source=source released='January 11<sup>th</sup>, 2017' latest-version='March 17<sup>th</sup>, 2017 (v0.2.0)' status='stable, active' category='Visualization' %}

## Introduction

A quiver plot is a 2D array of vector arrows that can be used to visualize dynamic processes such as flow or wave propagation. Vectors have both magnitude and direction; therefore to generate a vector plot, there needs to be a corresponding 2D array of the direction of each vector, and a 2D array of the magnitude of each vector.

{% include thumbnail src='/media/plugins/intro-quiver-plot-image.jpg' title='**Intro to generating a quiver plot** From left to right: The original data showing a wave moving through time (blue = start time, red = end time). Vector analysis was performed on the wave to generate a corresponding array of vector angles and vector speeds for points in space. (NOTE: The actual pixel values in these images needs to be the angle in degrees, and the magnitude of the vector). The Quiver Plot plugin was then used to make a quiver plot based off of the angle and speed arrays.'%}

## Running the Quiver Plot Plugin

The Quiver Plot plugin needs two 32-bit images, one representing the vector angles (direction) and one representing the vector magnitude. When you run the plugin, you will see the following window:

![](/media/plugins/quiver-plot-plugin-gui.png)

There are two drop-down menus that list all of the currently open windows. Of these windows, select the images that correspond to the angle map and magnitude map (i.e. speed, intensity, etc.). NOTE: pixels with a value of NaN will generate erratic vectors. Make sure that there are no NaN values with your images before using the plugin.

The third option allows you to set the resolution of plot (i.e. the pixel dimensions of the final plot.).

The plugin will then search for the largest magnitude vector in the magnitude image, and scale all of the vectors relative to the largest vector. This means that the vector lengths are relative, and therefore the vector lengths between any two plots are not cross-comparable.

This plugin is also recordable within ImageJ, and can be implemented as part of a macro.

## Installing the Quiver Plot Plugin

The Quiver Plot plugin is part of the [UCB Vision Sciences](UCB_Vision_Sciences) library. To install it, you just need to [ add](/update-sites/following#add-update-sites) the UCB Vision Sciences update site:

1\) Select {% include bc path='Help | Update...'%} from the Fiji menu to start the updater.

2\) Click on *Manage update sites*. This brings up a dialog where you can activate additional update sites.

3\) Activate the [UCB Vision Sciences](UCB_Vision_Sciences) update site and close the dialog. Now you should see additional jar files for download.

4\) Click *Apply changes* and restart Fiji.

You should now find the plugin under the sub-menu {% include bc path='Plugins |UCB Vision Sciences | Quiver Plot'%}.

**Note**: Quiver Plot is only one of the plugins included in the [UCB Vision Sciences](UCB_Vision_Sciences) suite. By following these installation steps, you will be installing as well the rest of plugins in the suite.

## Acknowledgements

This plugin was developed as part of the University of California, Berkeley Vision Sciences core grant NIH P30EY003176.

## License

This program is **free software**; you can redistribute it and/or modify it under the terms of the **GNU General Public License** as published by the Free Software Foundation ([http://www.gnu.org/licenses/gpl.txt](http://www.gnu.org/licenses/gpl.txt)).

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
