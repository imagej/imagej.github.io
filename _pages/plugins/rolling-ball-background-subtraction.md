---
mediawiki: Rolling_Ball_Background_Subtraction
name: "Rolling Ball Background Subtraction"
title: Rolling Ball Background Subtraction
categories: [Filtering]
initial-release-date: "22 November 2007"
website: "https://imagej.net/ij/plugins/rolling-ball.html"
dev-status: "first version"
team-founders: [Michael Castle, Janice Keller]
---

{% include info-box filename='Rolling\_Ball\_Background.class' source=' [Rolling\_Ball\_Background.java](https://imagej.net/ij/plugins/download/Rolling_Ball_Background.java)' %}

## Documentation

This plugin tries to correct for uneven illuminated background by using a "rolling ball" algorithm.

A local background value is determined for every pixel by averaging over a very large ball around the pixel. This value is hereafter subtracted from the original image, hopefully removing large spatial variations of the background intensities. The radius should be set to at least the size of the largest object that is not part of the background.

This plugin implements (differently) the same algorithm as the one built-in ImageJ in the {% include bc path='Process | Subtract background'%} menu, but adds a useful *Preview* capability. Also, to display the background subtracted in a separate (new) window, hold the ALT key when pressing "OK" (Preview must be off).

The rolling-ball algorithm was inspired by Stanley Sternberg's article, "Biomedical Image Processing", IEEE Computer, January 1983.

 
