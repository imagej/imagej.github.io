---
name: "EM tool"
title: IMBalENce
categories: [Microscopy, Import-Export]
release-date: "06/05/2020"
initial-release-date: "30/08/2018"
dev-status: "Stable, Active"
team-maintainer: 'Zhou XU | https://github.com/IMBalENce'
source-url: https://github.com/IMBalENce/EM-tool
update-site: EM tool
---

This is a suite of ImageJ plugins that are used for processing images acquired from electron microscopes. Currently the main focus is on SEM images, but I will keep working on streamline the image processing of both SEM and TEM data.

## Components and Functions

Click the links below to find more about each tool.

1.  \[ [SEM FEI metadata and scale](/plugins/sem-fei-metadata-scale) \] reads FEI SEM acquisition metadata from tiff tags and set image scale based on pixel size.
2.  \[ [SEM FEI databar cut](SEM_FEI_databar_cut) \] cuts databar from FEI SEM images, then save image and databar as individual files. (Page in preparation)
3.  \[ [SEM JOEL Scale](/plugins/sem-joel-scale) \] sets image scale based on pixel size store in the `.txt` file associated with SEM image.
4.  \[ [SEM ZEISS metadata scale](SEM_Zeiss_metadata_scale) \] reads ZEISS SEM acquisition metadata from tiff tags and set image scale based on pixel size.
5.  \[ [SEM Hitachi metadata scale](SEM_Hitachi_metadata_scale) \] Upcoming soon...
6.  \[ [Image feature measurement annotation](/plugins/image-annotation) \] measures and mark the size of features. It annotates the length of line tool in a calibrated image and export measurement results.
7.  \[ [Flat field correction](Flat_field_correction) \] Applies flat filed correction to a folder of images for large area mapping to mitigate chess pattern after stitching. (Page in preparation)
8.  \[ [ TEM .ser .dm3 folder export](/plugins/tia-ser-folder-export) \] This tool convert TIA EM image `.ser` files and Gatan `.dm3` files in a folder to TIFF format.

## Installation

### Installation via the ImageJ Updater

1. [Fiji](https://fiji.sc) (Fiji Is Just ImageJ) should be installed on your computer.

2. Click {% include bc path="Help | Update..." %} to open the [Updater](/plugins/updater). If it's the first time updating your Fiji, it might take some time to download the update files and may also require to restart Fiji a few times. Once done, click {% include bc path="Help | Update..." %} again to bring up the ImageJ updater window.

   {% include img src="emtool-01" width=350 %}

3. Click "Manage update sites".

   {% include img src="emtool-02" width=500 %}

4. Find and tick "EM tool", URL "https://sites.imagej.net/IMBalENce/".

5. If the update site does not show, you can manually add the site by clicking {% include button label="Add update site" %}. Type in Name "EM tool", URL "https://sites.imagej.net/IMBalENce/"

   {% include img src="emtool-03" width=500 %}

6. Click {% include button label="Close" %} on the "Manage update sites" window, then click {% include button label="Apply changes" %} on the ImageJ Updater window.

7. Once update is completed, restart Fiji. You should be able to see the plugins "EM tool" installed in the top toolbar.

### Manual Installation

If you only want to use one of the plugins you can follow these steps:

1. The source code of these macro scripts can be viewed [on GitHub](https://github.com/IMBalENce/EM-tool).

2. Download the script you want.

3. Save `.ijm` files in the desired location within your ImageJ application.

4. Go to {% include bc path="Plugins|Macros|Install..." %} to add the macros, or drag-and-drop the `.ijm` file onto ImageJ/Fiji.
