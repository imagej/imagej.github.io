---
mediawiki: User:Rerger
title: Fuzzy Set Intensity Transformations
categories: [Uncategorized]
---

# Fuzzy Set Intensity Transformations User Guide

## Introduction

FUZZY SET, the application, has evolved from developing a method to transform images as a class project into creating a "plugin" for Fiji users. We include a brief overview of the development and application for the plugin that we will refer to as just "Fuzzy Set". For those users who might want to explore the theory behind the application, we refer to the text Digital Image Processing, by Rafael Gonzalez. Users must also refer to the Fiji website for using more advanced features of the Fiji application.

We began developing a GUI based java application separate from the Fiji platform, but soon discovered the idea of creating a "plugin" as we explored the powerful features of Fiji. We found that the ability to make changes was efficient and simple. Fiji is an open source application that encourages contributions by its users. Being a java friendly application provided an easy platform for developing and modifying the code.

Our application employs the principle of fuzzy sets to transform pixels with the hope of enhancing an image.  The Fuzzy Set plugin inputs the pixels from an image into an array.  The user provides, through the use of an input window, numbers that correspond to values (except z0) in the following equation.

<div style="text-align: center;" markdown=1>
![](/media/plugins/fuzzysetformula.gif)
</div>

All images utilize the gray levels of the image; therefore, limiting the range of output values from "0-255" ("0" corresponds to totally black, likewise "255" corresponds to totally white).

Once the user inputs the values, our application analyzes the output values for every pixel "z0".  Every pixel in the image is transformed pixel by pixel.  The program displays the new modified image in its own window.  Two windows appear that display a histogram for both the original image and the modified image.  The final modified image appears illustrating the transformation as delineated by the user.  The user will be able to transform images into many possible outcomes using the features of the Fuzzy Set plugin.  Hopefully with practice, the user can adapt the application to meet their respective needs or just have fun exploring the concept of using fuzzy sets in image processing.

We would like to take this time to thank our professor, Dr. Nikolay Sirakov.  Dr. Sirakov encouraged us to go beyond the scope of a regular graduate course in image processing.  We cannot express our gratitude for his constant prodding, encouragement and feedback that allowed us to contribute to the outside world of image processor users.

## Software Installation

To use our software to transform images, the user must install the software onto their own device. We assume that our users are experienced computer users and have some familiarity with using a browser software such as Google Chrome to link to the fiji website. We would also like to note that every computer will behave somewhat independently and the use of these instructions must be applied with some flexibility and adaptability. Begin by opening a browser window on your device. Connect to the fiji website via the URL address: http://fiji.sc/. Navigate to the appropriate download to meet your operating system requirements, and follow the directions from the website. Notes when downloading ImageJ:  

1. You will need to know whether you have a 32- or 64-bit operating system, according to the website, Fiji can run on:

-   Windows XP, Vista, 7, 8, 10, 11, etc.
-   Mac OS X 10.8 "Mountain Lion" or later
-   Linux on amd64 and x86 architectures

2. Once it is installed you will need to unzip the file and double click on the FiJi .exe file. It may take a few moments to open.

## Plugin Installation

Once the Fiji application has successfully installed, navigate to the help menu on the toolbar.  Select Update from the drop down menu.  A window will pop up entitled "ImageJ Updater".  Select "Manage update sites" from the button on the lower left side.  This will list several sites to various "plugins" as well as providing the user to keep java and imageJ updated.  Navigate to the site "Fuzzy Sets".  Select the box on the left side to obtain the "plugin" and also keep the site updated.  Choose "close".  Finally the Fiji application must be restarted to apply the changes and/or add the plugin into the user's Fiji application.

## Opening an Image

Launch the Fiji application until the following window appears.

<div style="text-align: center;">

![](/media/plugins/openinganimage.jpg)

</div>

Under File, select Open from the drop-down menu and navigate to a location of an image on your computer that you wish to transform.

## Launching the Plugin

Select the Plugin from the application window. See diagram below.

<div style="text-align: center;">

![](/media/plugins/launchingplugin.jpg)

![](/media/plugins/launchingplugin2.jpg)

</div>

A user may now set the appropriate user defined values.

<div style="text-align: center;">

![](/media/plugins/selectvalues.jpg)

</div>

The Following Windows will appear after selecting the values from the control panel.

## Histogram Window

Below is an example of a histogram window.

<div style="text-align: center;">

![](/media/plugins/histogramwindow.jpg)

</div>

## Modified Histogram Window

Below is an example of the modified Histogram

<div style="text-align: center;">

![](/media/plugins/modifiedhistogramwindow.jpg)

</div>

## Modified Image Window

Following is an example of the Modified Image Window (image supplied by author)

<div style="text-align: center;">

![](/media/plugins/modifiedwindow.jpg)

</div>

## Saving Results

The user of the application can save results using the save as feature under the file option.  The Fiji application provides the options to save the image with a wide choice of extensions.

## Demo

We did many experiments with the application, but to show case one such result, we have included a demo below. ![](/media/2.jpg) ![](/media/plugins/modae.jpg)

<div>

![](/media/plugins/hist2.jpg) Histogram of Image Before Transformation

</div>

![](/media/plugins/histmod.jpg) Histogram of Image After Transformation

## Acknowledgements

<div style="text-align: center;">

![](/media/dr.jpg)

</div>

We would like to thank our professor [Dr. Nikolay Sirakov](http://faculty.tamuc.edu/nsirakov/), [Texas A&M-Commerce](http://www.tamuc.edu/). Under his tutelage and guidance we were able to transform a class project into a shared application for the ImageJ community. Special thanks to [Pavan Kumar](mailto:pavan.kumar.pic@gmail.com), our coding partner, who developed the application for the plugin. In addition, we wish to thank Robert Erger and Beverly Baird, the math team, for assistance in developing the algorithm and providing the documentation.

Contact Person: [Email Robert Erger](mailto:rerger@leomail.tamuc.edu)
