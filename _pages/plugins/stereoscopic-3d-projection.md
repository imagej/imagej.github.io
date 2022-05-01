---
mediawiki: Stereoscopic_3D_Projection
title: Stereoscopic 3D Projection
categories: [Uncategorized]
---

This plugin allows the user to create 3-D anaglyph and Google Cardboard compatible projections from image stacks.

The source is attached to the jar, and is public on [Github](https://github.com/Joe-Napoli/Stereoscopic_3D_Projection).

Java 8 is required to run this plugin.

## Use

To create a new projection:

1.  Open an image stack.
2.  Launch the plugin.
3.  Review slice spacing, total degrees of rotation, degree steps, and start and end rotation.
4.  Select the projection medium -- either anaglyph or Google Cardboard.
    1.  If an anaglyph projection is attempted on a colored image stack, a prompt to convert the image stack to grayscale will appear. Color is incompatible with the lookup tables used in the anaglyph projection, and so the stack must be converted to grayscale to continue.
5.  Select "Ok!"

## About

The Stereoscopic 3D Projection plugin was created by Joe Napoli for [Visikol, Inc](https://visikol.com) as an aid for visualizing image stacks.
