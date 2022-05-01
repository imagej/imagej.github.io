---
mediawiki: Distance_Analysis
title: Distance Analysis
categories: [Analysis,Colocalization]
---

## Distance Analysis (DiAna)

This plugin allows :

-   Calculating co-localization between objects in 3D
-   Measuring 3D distances between nearest object, co-localized or not
-   Getting some 3D measurements about each objects

The plugin can be used with labelled images, but it also integrates tools for the segmentation of the objects.

## Author

Jean-François Gilles, Institute of Biology Paris Seine (France). jean-francois.gilles (at) upmc.fr

Thomas Boudier ![](/media/emailboudier.png), [Academia Sinica](https://www.sinica.edu.tw/en), Taipei, Taiwan.

## Features

**Denoise filter**

-   Mean, Median, Gaussian blur filters

**Segmentation of the objects**

-   Global thresholding

<!-- -->

-   [3D Segmentation](https://imagejdocu.list.lu/plugin/segmentation/3d_spots_segmentation/start) (iterative thresholding, spots segmentation, ...)

**Object based co-localization and distance analysis**

-   Colocalization from objects in image A, B, and/or A+B
-   Distance center – center ;
-   Distance center – edge ;
-   Distance edge – center ;
-   Surface in contact
-   Generates results representations such as:
    -   Objects' map ;
    -   Colocalization object's map ;

**Counting and measurements on objects**

Counts the number of 3D objects in two stacks.

Quantifies for each found object the following parameters:

-   Volume
-   Mean of the gray values
-   Surface area
-   Standard deviation of the gray values
-   Minimum & Maximum gray values
-   Centroid
-   Centre of mass
-   Feret's Diameter

## Description

*Note that when the mouse arrow passes on the items of the plugin, an explanation of each parameter is given.*

Open at least two images. This plugin does not support RGB and 32-bits images.

### Images to analyse

Select the image A and the image B. The image A is the reference image.

**Binary images:**

Apply threshold with value 1

Filter objects by size and remove objects from image edges is possible

**Gray level images:**

Apply filter to suppress noise (optional)

Segment the image with either threshold or spot segmentation method

\- Threshold method :

choose a threshold value

Filter objects by size and remove objects from image edges is possible

\- Spot segmentation method : a tutorial for this method is found [here](https://imagejdocu.list.lu/plugin/segmentation/3d_spots_segmentation/start)

\- Iterative segmentation method : a tutorial for this method is found [here](https://imagejdocu.list.lu/plugin/segmentation/3d_spots_segmentation/start)

\- Filter objects by size is possible

### Interactions filters

When unchecking « All objects touching » , the plugin will analyse the non co-localizing objects in addition to co-localizing objects.

### Measures & Analysis

**Colocalisation**

Choose the parameters that will be measured for co-localizing objects

**Distance**

Choose the parameters that will be measured for non co-localizing objects

**Shuffle**

Select to do a shuffle of the objects on all the image or inside a mask

**Other measures**

Choose the parameters that will be measured for each objects

**Resolution infos** Image calibration has to be given for the measurements to be calibrated. If images opened are already calibrated, the plugin reads the calibration (otherwise it will ask you to inter the values).

### The plugin retrieves :

-   Objects from image A and B are listed in a ROI Manager.
-   Number of objects and number of co-localizing objects are given in the log window.
-   ColocResults gives measurements on co-localizing objects.
-   DistanceResults gives measurements on non co-localizing objects.
-   Curve of the shuffle (cumulative distances)
-   OtherMeasuresResults-A/B gives measurements on each objects from images A and B.

### Batch :

if the recorder has a problem, here are some examples of macro line:

-   run("DiAna\_Segment", "img=imageName.tif filter=median rad=1.0 thr=739-3-2000-true-false");
-   run("DiAna\_Segment", "img=C0.tif peaks=2.0-2.0-50.0 spots=30-10-1.5-3-2000-true");
-   run("DiAna\_Segment", "img=C0.tif iter=3-2000-20-30-true");
-   run("DiAna\_Analyse", "img1=imageA.tif img2=imageB.tif lab1=segA.tif lab2=segB.tif coloc distc=50.0 adja kclosest=1 dista=50.0 measure");

## Installation

Download and copy the following jar in your plugins folder [Diana\_1.49.jar](https://drive.google.com/file/d/1W1qOUGuOgSOs5KeNY0BZ6353tp-TJnky)

You have also to manually download and copy into your plugins directory the [3D ImageJ Suite](https://mcib3d.frama.io/3d-suite-imagej/).

*Note that this version works only with the 3D ImageJ library [mcib3d-core4.0.1.jar] and upper!*

## Citation

Gilles J-F, Dos Santos M, Boudier T, Bolte S, Heck N. DiAna, an ImageJ tool for object-based 3D co-localization and distance analysis. Methods 2016 Nov 24. [1](http://www.sciencedirect.com/science/article/pii/S1046202316304649)

The spot segmentation method is based on : Heck N, Dos Santos M, Amairi B, Salery M, Besnard A, Herzog E, Boudier T, Vanhoutte P, Caboche J. A new automated 3D detection of synaptic contacts reveals the formation of cortico-striatal synapses upon cocaine treatment in vivo. Brain Struct Funct. 2014 Jul 8. DOI 10.1007/s00429-014-0837-2. [2](http://link.springer.com/article/10.1007%2Fs00429-014-0837-2)

## License

GPL distribution (see [3](http://www.cecill.info/index.en.html%7Clicence)). Sources for plugins are available freely.

## Change log

-   14/12/2016 v1.0.1: bug fixed for retrieving the calibration, add "about" button
-   16/12/2016 v1.1: add save 3D-ROIs button
-   05/09/2017 v1.2: many improvements within the code. update possibility when initializing images in Analyse. macro enable for the labelling part
-   25/01/2018 v1.3: 8bits bug fixed, add macro features
-   05/07/2018 v1.4: bugs fixed
-   19/12/2018 v1.41: bugs fixed
-   21/12/2018 v1.42: show again info in the log
-   17/01/2019 v1.43: correct user interface and a bug with 2D images, thanks to Chin-Chun
-   14/05/2019 v1.44: bugs fixed and compatibility with the last version of 3D Suite.
-   29/10/2019 v1.45: bugs fixed and maven update. Thanks to N. Chiaruttini
-   24/01/2020 v1.46: bug fixed, add coloc image in the batch
-   24/02/2020 v1.47: bug fixed with the shuffle in macro line
-   28/04/2020 v1.48: add integrated density measure
-   02/02/2022 v1.49: bugs fixed, add some small options

   
