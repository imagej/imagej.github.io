---
title: Labkit - Automatic Segmentation - Quick Start Tutorial
---
# Labkit - Automatic Segmentation - Quick Start Tutorial

This quick start tutorial shows you how to segment an image within seconds using the [Labkit](index) plugin in Fiji.

1.  Open an image in ImageJ.
2.  Start Labkit by selecting {% include bc path="Plugins | Labkit | Open Current Image With Labkit" %} from the menu.
3.  Labkit should start and display the image. If it shows a black window instead of the image: Click {% include key key='S' %} and adjust the contrast.
4.  Select "foreground" (In the side bar of Labkit). Select the pencil tool (top bar of Labkit) and draw on the image.
5.  Select "background" and the pencil tool, and mark some other region of the image as background.
6.  In the side bar of Labkit, under the heading "Segmentation", there is a button named "Labkit Pixel Classifier". Click the button.
7.  you will find an entry "Labkit Pixel Classifier \#1". And next to it there is a play button (black triangle). Click it, to train the Classifier. After a moment you will see the automatic segmentation of your image.
8.  From Labkit's main menu select {% include bc path="Segmentation | Show Segmentation Result in ImageJ" %}, to export your segmentation into ImageJ.

(For more tutorials and installation instructions click [here](/plugins/labkit))

As video:
![labkit-quick-start](https://user-images.githubusercontent.com/24407711/133519201-67d6e29f-f024-4803-8eee-75831a996952.gif)
