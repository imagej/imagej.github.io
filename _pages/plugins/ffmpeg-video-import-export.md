---
title: Import/Export movie using FFmpeg
name: FFmpegVideoImportExport
categories: [Import-Export]
source-url: https://github.com/anotherche/imagej_ffmpeg_video
release-date: March 11 2025
release-version: 0.6.0
dev-status: Active
support-status: Active
team-founders: "@anotherche"
team-maintainers: "@anotherche"
---

## Overview

The plugin allows you to import and export video files using the JavaCV interface to FFmpeg. 
It supports all formats and compression methods known to ffmpeg (i.e. virtually all known video types).

During import you can select the necessary frame range and perform the simplest operations on images like flip and convert to grayscale.
The resulting sequence of images is displayed as a virtual image stack (optionally decimated) or converted to a 5D hyperstack with customizable field order and number of z-slices and time-frames.

Export allows you to save the image stack or hyperstack to video in the required format and compression.

The plugin depends on another plugin - [JavaCV Installer](https://imagej.net/plugins/javacv-installer), which must be installed in ImageJ (see Installation details below). 

## Usage

***Import***

1. Select menu "Import Movie Using FFmpeg..." from the Import menu
2. Specify the video file
3. Configure import options in the user interface

***Export***

1. Make required image stack active
2. Select the Save As menu item - "Export Movie Using FFmpeg..."
3. Customize export options in the user interface
4. Specify the video file to save

## Installation in Fiji

Running the plugin requires installation of the [JavaCV installer](https://imagej.net/plugins/javacv-installer), which installs the interface for FFmpeg.
Although you can install the JavaCV installer and then add FFmpeg manually as described in the JavaCV installer description, 
this is not necessary as the plugin will check for the availability of the required components and offer to download and install them automatically.

Therefore, the following simple procedure is recommended:
<ol>
  <li>Install the video plugin </li>
  <li>Run the import or export command, and the plugin will install everything by itself (several restarts of ImageJ will be required) </li>
</ol>

To install the video plugin:
<ol>
  <li>add VideoImportExport update site https://sites.imagej.net/VideoImportExport/ using the update sites manager </li>
  <li>install the plugin normally using the updater </li>
</ol>


## Additional information and support

The plugin is discussed at [imagej forum](https://forum.image.sc/t/plugins-for-reading-and-writing-compressed-video/8777)
