---
title: SynActJ
icon: /media/icons/synActJ_logo.png
categories: [plugin]
---

{% capture maintainer%} {% include person id='schmiedc' %} {% endcapture %}

{% capture author%} {% include person id=schmiedc' %} {% endcapture %}

{% capture source%} {% include github org='schmiedc' repo='SynActJ' %} {% endcapture %} {% include info-box software='Fiji' name='SynActJ' maintainer=maintainer author=author source=source status='active' released='2021' category='Plugins' %}

# Synaptic Activity in ImageJ (SynActJ)

SynActJ is an image and data analysis workflow that allows to analyze synaptic activity. 
It is based on a Fiji plugin and a R Shiny App that implement the automated image analysis of active synapses in time-lapse movies.
We tested the workflow with movies of pHluorin or calcium sensors.

<img src="https://schmiedc.github.io/SynActJ/images/main/teaser.png" alt="Intro" class="inline"/>

## Documentation & source code

Have a look at the github pages site for more information:<br>
[https://schmiedc.github.io/SynActJ/](https://schmiedc.github.io/SynActJ/)
<br/>
<br/>
The code is published free and open source under the [MIT license](https://github.com/schmiedc/SynActJ/blob/master/LICENSE).<br/>
Please find the source code of the Fiji plugin here:<br/>
[https://github.com/schmiedc/SynActJ](https://github.com/schmiedc/SynActJ)
<br/>
<br/>
The source code of the R analysis can be found here:<br/>
[https://github.com/schmiedc/SynActJ_Shiny](https://github.com/schmiedc/SynActJ_Shiny)

## Core features
- Java Swing based graphical user interface
- Interactive adjustment over entire dataset
- Batch processing executed from main interface
- Saving and loading of processing settings
- Shiny App for data processing

## Accepted Datasets
Expected are 2D single channel .tif files containing multiple frames. At a specific frame the cultured neurons were stimulated and active boutons show an increase in intensity. The image calibration can be changed in the workflow. A settings file can be provided but can also be created later.

A small example file is provided here: [Link to example data](https://github.com/schmiedc/SynActJ/blob/master/testInput/testMovie.tif)

The default segmentation parameters should work for this example file.

## Installation

### Image analysis - Fiji plugin

Tutorial for Shiny app: [Link to tutorial](https://schmiedc.github.io/SynActJ/pages/Fiji_Plugin.html)

For the image analysis you need to download and install Fiji: [Link to Fiji](https://fiji.sc/).<br>
The plugin is available via an update site. Add the Cellular-Imaging site:

1. Select **Help › Update…** from the menu bar. This will install potential updates and open a new window.
2. Click on **Manage update sites**. Which opens the Manage update sites dialog.
3. Search for the **Cellular Imaging** update site in the list.
4. Add the update site by setting the tick box.
5. Press **Close** and then **Apply** changes.
6. The SynActJ should appear with the Status: **Install it**.
7. Press **Apply** changes wait for download to finish and restart Fiji.

### Data analysis - Shiny app

Repository for Shiny app: [Link to Repo](https://github.com/schmiedc/SynActJ_Shiny)<br>
Tutorial for Shiny app: [Link to tutorial](https://schmiedc.github.io/SynActJ/pages/SynActJ_Shiny.html)

For the data analysis you need to download R and RStudio: R Version 4.1.0<br>
[Link to R](https://cran.r-project.org/bin/windows/base/)<br>
Select version 4.1.0

RStudio 1.4.1717<br>
[Link to RStudio](https://www.rstudio.com/products/rstudio/download/)

1. Download the contents of the repository: SynActJ Shiny<br>
  Click on the green button: **Code**.<br>
  Press **Download ZIP** to download the scripts.
2. Unzip the script to a location of your choice.
3. Open the app.R file in RStudio.
4. Start the application: press **Run App** - top right corner of RStudio.
5. RStudio may ask to install or load extra packages - Download will take some time.
6. Once these packages are installed and loaded the RShiny GUI should pop up.
7. Optional: Press **Open in Browser** for a better rendering of the GUI.
