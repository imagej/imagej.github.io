---
title: 4d Tools
description: 4d Tools is a set of macros/plugin for (1) import of legacy 4d datasets as movies (.MOV, .MP4, .AVI); (2) simplified import of Imaris .IMS and Micro-manager 1.4/2.0 datasets into Fiji; and (3) experimental playback of maximum-intensity projections on the fly as a crude attempt to recaptiulate legacy Perkin-Elmer UltraView software.
categories: [Import-Export,Stacks]
release-date: September 1, 2025
release-version: 0.7.0
dev-status: Active
support-status: Active
team-founders: "@jdhardin"
team-maintainers: "@jdhardin"
---

## Overview

4d Tools is a set of macros/plugin for (1) import of legacy 4d datasets as movies (.MOV, .MP4, .AVI); (2) simplified import of Imaris .IMS and Micro-manager 1.4/2.0 datasets into Fiji; and (3) experimental playback of maximum-intensity projections on the fly as a crude attempt to recaptiulate legacy Perkin-Elmer UltraView software.

**Rationale**
1. Import of legacy datasets is useful for many long-established *C. elegans* laboratories, for example, which have large numbers of legacy 4d DIC datasets as movies in xytc format. For this vintage approach, see, for example:
   {% include citation doi="10.1126/science.273.5275.603" %}

2. Micro-Manager has an integrated playback mechanisms built on top of ImageJ, and a free multi-platform Imaris player is avaialble, but in some cases direct import into Fiji is useful, and these macros simplify this process for routine work.

3. Oddly, there doesn't seem to be a stratighforward way to display a "range" of Z slices as a maximium intensity projection in ImageJ/Fiji. Old Perkin-Elmer Ultraview software had this functionality.

## Installation in Fiji

Add the 4d-Tools update site using the Fiji update sites manager. After updating, five new menu itms will be aqdded to Fiji:

***4d Import options***

A "4d" submenu will be added to the "Import" menu in Fiji. Four items will be avaialble in this submenu:
1. **Classic 4d AVI to Hyperstack:** Imports a 4d AVI video as a  Virtual Hyperstack. It looks for a plain text file with the same root name as video. If none is found the macro will ask for the number of focal planes.
2. **Classic 4d Movie to Hyperstack:** Imports a 4d Quicktime .MOV or an MPEG4 .MP4 video as a 4d Virtual Hyperstack using FFMpeg. It looks for a plain text file with the same root name as the video. If none is found the macro will ask for the number of focal planes. FFmpeg is very versatile in terms of video formats; particularly valuable for classic QWuicktime movies, both MPEG  will accept 
3. **Classic 4d Movie to Hyperstack Bio-Formats:** Imports a 4d Quicktime .MOV or an MPEG4 .MP4 video as a 4d Virtual Hyperstack using the Bio-Formats Importer built into Fiji. It looks for a plain text file with the same root name as the video. If none is found the macro will ask for the number of focal planes. NOTE #1: due to an issue with Bio-Formats virtual hyperstacks, the data is loaded into RAM. A warning dialog asks if this is OK. NOTE #2: For historical reasons, Bio-Formats focused on the Motion JPEG B codec (compression.decompression) format. Attempting to import MPEG A formatted video will throw an error.
4. **Classic 4d Viewer to Hyperstack:** Imports classic 4d Viewer data (a folder of .MOV or .mov files) as a 4d Virtual Hyperstack using the Bio-Formats Importer built into Fiji. Rather than using the 4d Viewer info file, it simply counts the number of movie files, which are assumed to be the indivual focal planes. NOTE: this script only displays the movie data; displaying annotation/overlay information is not supported.
5. **PE AVIs to Hyperstack:** Imports a series of AVIs exported from the old Perkin-Elmer UltraView LCI software into Fiji. The PE software doidn't pad the numbers in filenames with leading zeroes. Unless this is done prior to impoort misordering of images will occur. There ar emay platform-specific file renaming applications that will do this. For PE AVIs one easy way to pad filenames in Fiji is the [Pad Image Names macro tool](https://dev.mri.cnrs.fr/projects/imagej-macros/wiki/Pad_Image_Names).
6. **PE TIFFs to Hyperstack:** Imports a TIFF data series geenrated using the old Perkin-Elmer UltraView LCI software into Fiji. This is actually just a wrapper for the [Bio-Formats Importer](https://imagej.net/formats/bio-formats) plugin with a couple of paramaters set via script.
7. **Imaris to Hyperstack:** Imports the highest-resolution dataset in an Imaris .IMS file (a variant of the HDF5 format) as a Virtual Hyperstack using the Bio-Formats Importer built into Fiji.
8. **MM Images to Hyperstack:** Imports a Micro-Manager 1.4 or 2.0 dataset as a Virtual Hyperstack, using the metadata in the dataset.

***Hyperstack Projector***

A new "Hyperstack Projector" item will be added to the {% include bc path="Image|Hyperstacks" %} submenu. Running this plugin will attempt to recaptiulate the functionality of the old Perkin-Elmer Ultraview software, which performed a maximum-intensity projection on a specified range of images on the fly. The plugin assumes a 4d Hyperstack is open, and temporarily replaces the stack window with a custom window that allows specificaiton of the number of focal planes to be projected. CLosing the window restores the original stack window.

**NOTE:** This plugin is **extremely** experimental. The code in the installed .JAR file can likely be massively improved.

## Usage

### Classic 4d AVI to Hyperstack

1. Select menu {% include bc path="Import|4d|Classic 4d AVI to Hyperstack" %}.
2. Specify the video file.
3. If no text file with focal plane information is found, specify the number of focal planes.
4. The dataset will be loaded as a Virtual Hyperstack.
5. A window with the focal plane and time point information should be visible.

### Classic 4d Movie to Hyperstack/Classic 4d Movie to Hyperstack Bio-Formats

1. Select menu {% include bc path="Import|4d|Classic 4d Movie to Hyperstack" %} or {% include bc path="Import|4d|Classic 4d Movie to Hyperstack Bio-Formats" %}.
2. Specify the video file.
3. If no text file with focal plane information is found, specify the number of focal planes.
4. The dataset will be loaded as a Virtual Hyperstack.
5. A window with the focal plane and time point information should be visible.

### Classic 4d Viewer to Hyperstack

1. Select menu {% include bc path="Import|4d|Classic 4d Viewer to Hyperstack" %}.
2. Specify the directory containing the focal plane movies.
3. The dataset will be loaded as a Virtual Hyperstack.
4. A window with the focal plane and time point information should be visible.
NOTE: this script only loads the movie data; annotation/overlay information is not supported.

### PE AVIs to Hyperstack

1. Running the script will warn the user that the filenames must be numerically padded (...001.avi - ...010.avi, etc. vs. ..1.avi - ...010.avi). The PE software did not pad filenames. For PE AVIs one easy way to pad filenames in Fiji is the [Pad Image Names macro tool](https://dev.mri.cnrs.fr/projects/imagej-macros/wiki/Pad_Image_Names).
2. Specify the first AVI.
3. The script will examine filenames to guess if each AVI is a single focal plane over time or if it is a Z stack of a single time point and populate a dialog allowing the user to confirm the data structure.
4. The dataset will be loaded as a Virtual Hyperstack.

### PE TIFFs to Hyperstack

1. Specify the first TIFF in the dataset.
2. The dataset will be loaded as a Virtual Hyperstack.

### MM Images to Hyperstack

1. Select menu {% include bc path="Import|4d|MM Images to Hyperstack" %}.
2. Specify the data directory.
3. The dataset will be loaded as a Virtual Hyperstack.

### Imaris to Hyperstack

1. Select menu {% include bc path="Import|4d|Imaris to Hyperstack" %}.
2. Specify the data file.
3. The dataset will be loaded as a Virtual Hyperstack.

### Movie to Hyperstack macro tool
{% include img name="4d tools" src="/media/4d_macro_tool.png" %}
1. The Movie to Hypersrtack macro tool will be avialable as an option in the ImageJ toolbar (click the >> button to see a list of aviualble toolbars).
2. Selecting "Movie to Hyperstack" will load the toolbar. Clicking the leftmost button provides easy selectino of the scripts in the {% include bc path="Import|4d" %} submenu.
3. Mousing over the other buttons provides a description of the other buttons, which allow standard navigation through Hyperstacks fro the toolbar. 

### Hyperstack Projector

1. With a 4d Hyperstack in the frontmost window, select menu {% include bc path="Import|Hyperstacks|Hyperstack Projector" %}.
2. The Hyperstack window will be replaced with a custom window.
3. Enter the number of focal planes to be projected centered on the current focal plane in the "d" text field.
4. A running projection will be displayed centered on the current z plane and time point.
5. Navigate up and down in space using the "z" slider and forward and backward in time using the ">" slider. Clicking the "v" button will play the movie, which will loop if the "loop" checkbox is selected.

## Additional information and support

Sample data can be downloaded from the [Hardin Lab microscopy page](https://worms.zoology.wisc.edu/research/microscopy/).
