---
mediawiki: Labkit
title: Labkit

artifact: net.imglib2:imglib2-labkit
categories: [Uncategorized]
---

<img src="/media/plugins/labkit-illustration.jpg" width="700"/>

Labkit is a user-friendly Fiji plugin for the segmentation of microscopy image data. 
It offers easy to use manual and automated image segmentation routines that can be rapidly applied to single- and multi-channel images as well as timelapse movies in 2D or 3D. 
Labkit is specifically designed to work efficiently on big image data.
Users of consumer laptops can conveniently work with multiple terabytes large image data. 
This efficiency is achieved by using Imglib2 and Big Data Viewer as the foundation of our software. Additionally, manual tools for ground-truth annotation are available. Furthermore, memory efficient and fast random forest based pixel classification based on the Waikato Environment for Knowledge Analysis (WEKA) is implemented, optionally exploiting the power of graphics processing units (GPUs) to gain additional performance. 
Labkit is easy to install on virtually all laptops and workstations.
Additionally, Labkit is prepared to be used on high performance computing clusters (HPC) for distributed processing of big image data. 

## Installation

There are two options for the installation of Labkit. Option A: The basic installation (without GPU acceleration) that works on all computers. Option B: The installation with GPU acceleration. (better performance, but requires an NVIDIA GPU).

### Option A: Basic Installation
1. Install Fiji
2. Install the [Labkit update site](https://sites.imagej.net/Labkit/). (For details on how to install an update site click [here](/update-sites/following).)

### Option B: Installation With GPU Support
(Requires a NVIDIA GPU, and propery installed graphics card drivers.)
1. Install Fijij
2. Install the “clij” and “clij2” update sites in Fiji. (see https://clij.github.io/clij2-docs/installationInFiji for details)
4. Install the “Labkit-Preview” update site, URL: https://sites.imagej.net/Labkit-Preview/
   (This update site is not in the list of official update sites. It needs to be added first.) 

## Tutorials

### Quick Start Tutorial

Follow these steps to segment an image:

1.  Open an image in ImageJ.
2.  Start Labkit by selecting {% include bc path="Plugins | Segmentation | Labkit" %} from the menu.
3.  Labkit should start and display the image. If it shows a black window instead of the image: Click {% include key key='S' %} and adjust the contrast.
4.  Select "foreground" (In the side bar of Labkit). Select the pencil tool (top bar of Labkit) and draw on the image.
5.  Select "background" and the pencil tool, and mark some other region of the image as background.
6.  In the side bar of Labkit, under the heading "Segmentation" you will find an entry "Classifier \#1". And next to it there is a play button (black triangle). Click it, to train the Classifier. After a moment you will see the automatic segmentation of your image.
7.  From Labkit's main menu select {% include bc path="Segmentation | Show Segmentation Result in ImageJ" %}, to export your segmentation into ImageJ.

### Tutorial: Labkit With GPU Accelleration

Make sure you installed Labkit with GPU support. Labkit can be used the same way as discribed above, with one additional step to enable the GPU acceleration.
Open the "Classifier Settings" and select "Use GPU acceleration".

### Tutorial: Manual Segmentation

1.  Start Fiji, open your image, start Labkit (`Plugins > Labkit > Open Current Image With Labkit`)
2.  Select `+ Add label`
3.  Use the `Draw` button (pencil icon) to mark the contour around any one object instance
4.  Use the `Flood Fill` button (bucket icon) to fill inside this contour
5.  When all objects have been labeled in the manner above, select `Labeling > Save Labeling`

<img src="https://user-images.githubusercontent.com/34229641/106534470-6b4df100-64f4-11eb-8c76-600a33de669a.gif"  width="800" />

### Tutorial: Segmenting a list of images with the macro recordable command

Automatic image segmentation can be very useful to segment a large number of images.
The images need to be similar to get good results. Make sure that brighness and contrast is normalized, and maybe do some background removal first.
Select a representive image.
Open this image with Labkit and segment the image as discribed in the quick start tutorial.
But in the last step save the trained classifier {% include bc path="Segmentation | Save Classifier ..." %} into a file.
Now the following ImageJ macro can be used to apply the classifier over many images.

```java
// ImageJ macro for segmenting a list of images
folder = "C:/path/to/folder/"
for (i = 0; i < 10; i++) {
   open(folder + "image_" + i + ".tif");
   run("Segment Image With Labkit", "segmenter_file=" + folder + "my_pretrained_classifier.classifier use_gpu=false");
   saveAs("Tiff", folder + "segmentation_" + i + ".tif");
   close();
   close();
}
```

### Tutorial: Segmenting a large image on a Cluster

On your computer
1.  Download the dataset of interest, unzip
2.  Use BigStitcher FIJI plugin to resave the dataset as BDV HDF5 + XML format:
    - Install BigStitcher update site in Fiji
    - Run Plugins > BigStitcher > Batch Processing > Define dataset …
      (Use Bioformats importer an make sure to select correct pixel size)
3.  Train a classifier with Labkit therefor:
    Plugins > Lakit > Open Image File With Labkit
4.  Continue as discribed in the quik start tutorial.
5.  Save the trained classifier {% include bc path="Segmentation | Save Classifier ..." %} into a file.

On the HPC cluster: (This is also covered on https://github.com/maarzt/labkit-command-line)

6.  Copy the dataset HDF5 + XML to the cluster
7.  Copy the trained classifier to the cluster
8.  Download the labkit command line tool https://github.com/maarzt/labkit-command-line/releases/download/v0.1.1/labkit-snakemake-exmaple-0.1.1.zip
9.  Extract this zip file
10.  In the “Snakemake” file change:
```sh
IMAGE = “/path/to/your/dataset.xml”
CLASSIFIER = “/path/to/your/pixel.classifier”
USE_GPU=”true”
```
11. Run:
```sh
$ snakemake --cluster=”sbatch --partition=gpu” --jobs=10 --local-cores=1 --restart-times=10
```

### Tutorial: Import & Export Segmentations

-   Things you can save, open, import or export:
    -   Labeling - As `*.tif` or `*.labeling`
    -   Bitmap - (One layer of the labeling) As `*.tif`
    -   Classifier - As `*.classifier`, only Labkit is able to work with them.
    -   Segmentation result - As `*.tif`, or show to ImageJ
    -   Segmentation's probability Map - As `*.tif`, or show in ImageJ
-   The word "labeling" is used to refer to the colorfully displayed areas overlayed on top of the image.
-   Labkit's file format for labelings is `*.labeling`. It works great for very large files with very few labels. (This file format is likely to be improved and changed in the future.)
-   The labeling can be saved and opened as `*.tif` as well. (This is a good option for not-too-big images. And can be used by any other tool.)

## FAQ

**Is it possible to manually segment a 3D image slice by slice?**

Yes, this can be achieved by a workaround: Simple convert your image to 2D+time before opening it with Labkit. In Fiji use "Image > Hyperstacks > Re-order Hyperstack ..." to convert your image from 3D to 2D+time. 

**After starting Labkit the window that should show my image is black?**

This often happens if Labkit can't find proper brightness & contrast settings. Please click the button that says "auto contrast".

**How I manually select the colors and brightness settings that are used to show the image?**

Click {% include key key='S' %} on your keyboard. This should show the BigDataViewer brightness & color dialog. Use it to manually adjust those settings.

**Can Labkit distinguish more than two classes "foreground" and "background"**

Yes, simple click the "Add label" button this will add a new class. You are free to name labels / classes as you would like, simple double click on the label.

**How can I change the color of the labels?**

Just click on the colored rectangle left of the labels name. This will show a color selection dialog.


## Keyboard Shortcuts

### Basic Navagation

Labkit is based on BigDataViewer. Navigation the image works as in BigDataViewer, and many shortcuts work too. Click [here](/plugins/bdv) for a description of the shortcuts.

-   {% include key keys='Ctrl|Shift|mouse-wheel' %} to zoom in and out
-   {% include key keys='right-drag' %} to move the image
-   {% include key keys='left-drag' %} to rotate a 3d image
-   {% include key key='mouse-wheel' %} to scroll through the z-slices of a 3d image


### Drawing Tool
-   {% include key keys='D|left-click' %} to draw with the pencil tool.
-   {% include key keys='E|left-click' %} to erase with the pencil tool.
-   {% include key keys='F|left click' %} to use the flood fill tool.
-   {% include key keys='R|left-click' %} to remove a connected component.
-   {% include key key='N' %} - switch to next label
