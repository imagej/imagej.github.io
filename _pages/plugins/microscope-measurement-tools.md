---
mediawiki: Microscope_Measurement_Tools
title: Microscope Measurement Tools
categories: [Registration]
---


{% capture demisjohn %}
{% include person id='demisjohn' %}
{% endcapture %}

{% capture source%}
{% include github org='demisjohn' repo='Microscope-Measurement-Tools' %}
{% endcapture %}
{% include info-box software='Fiji' name='Microscope Measurement Tools' author=demisjohn maintainer=demisjohn filename=' [Download from GitHub/Releases](https://github.com/demisjohn/Microscope-Measurement-Tools/releases)' source=source released='Sept. 24<sup>th</sup>, 2015' latest-version='2.3' status='beta' website=' [Microscope Measurement Tools at GitHub](https://github.com/demisjohn/Microscope-Measurement-Tools)' %} Recall saved calibrations for your microscope's measurement scale and create measurement annotations.

## Description

This set of plugins provides a quick way to save distance/length calibrations for various microscopes/objectives in a simple text file.

You can then choose any of your prior measurement calibrations to be applied to an open image (or all open images), as so:

![](/media/microscope-meas-tools-choose-calibration-01.png)

The "Draw Measurement" plugin then allows you to draw a line with the calibrated measurement length, as so:

![](/media/microscope-meas-tools-draw-meas-line.png)

Three files are included:

-   *Choose\_Microscope\_Calibration.py*
    -   Opens the "Choose Calibration" window, for setting the measurement scale to a preconfigured value.
-   *Draw\_Measurement\_-\_Line.py*
    -   Converts a Line ROI into a drawn annotation with the measurement length indicated.
-   *Microscope\_Calibrations\_user\_settings.py*
    -   Settings file that contains your pre-configured scale calibrations, along with some settings for drawing annotations (background/text color etc.)

## Installation & Usage Manual

Please see the complete installation & usage instructions here:

  
[**Microscope Meas. - Calibration instructions.pdf**](https://github.com/demisjohn/Microscope-Measurement-Tools/blob/master/Microscope%20Meas.%20-%20Calibration%20instructions.pdf)

Basic instructions are as follows.

1\. Extract the .zip file linked at [GitHub/Releases](https://github.com/demisjohn/Microscope-Measurement-Tools/releases), and place the resulting *Analysis* folder inside

  
*Fiji.app / Plugins / Scripts*

<!-- -->

  
(If an *Analysis* folder already exists, do Not overwrite it - you must have another Analysis plugin installed! Instead, merge the two folders.)

### Setting up your calibrations

2\. Open an image with a feature of some known length, taken with some microscope/objective that you desire to save a calibration for.

3\. Draw a line along the feature of known length.

4\. Select the {% include bc path='Analyze | Set Scale'%} menu item.

5\. Type in the known length in "*Known Distance*" and record the "**Scale**" value for this calibration.

  
Perform more calibrations (on other images) if desired, recording the Scale values for each.

6\. Edit the File

  
*Fiji.app / plugins / Scripts / Analyze / Microscope Measurement Tools /*

<!-- -->

  
  
*Microscope\_Calibrations\_user\_settings.py*

7\. Type in the Calibration's Names & Scale values, making sure to match up the list of names with their corresponding calibrations.

  
This settings file is an actual python script, so you can edit the lists there using normal Python syntax. eg. functions like `myList.append( [ ] )` or `myList = ['cm'] * 5` etc. will work.

Unfortunately, changes to the settings file may not be automatically picked up by Fiji. The workaround is to do the following:

8\. Quit Fiji.

9\. Delete the "*py.class*" file in the plugin's folder:

  
*Fiji.app / plugins / Scripts / Analyze / Microscope Measurement Tools /*

<!-- -->

  
  
*Microscope\_Calibrations\_user\_settings$py.class*

10\. Open Fiji. It should have picked up the new settings now.

You should only have to do this calibration once, when you do your initial calibration/setup.

### Applying a pre-configured scale to your image

11\. Run {% include bc path='Analyze | Microscope Measurement Tools | Choose Microscope Calibration'%} - the pop-up window shows the new names and calibration values you set in your user-settings file.

### Annotating your image with a length measurement

To draw a measurement annotation,

1\. Draw a "Straight Line" along the feature you want to measure (the length is displayed in the Fiji status bar)

2\. Select {% include bc path='Analyze | Microscope Measurement Tools | Draw Annotation - Line'%}.

  
The annotation will be drawn directly onto the image.

It is recommended that you work on a copy of your file. Unfortunately there is currently no Undo feature. I may try to figure out ho to use the "Overlay" feature to make something like that possible.

### Adding a custom function to the Calibrations list

A sub-folder is included that shows how to implement a custom function in Python, that will be executed to get the scale parameter, and shows up in the Calibrations list.

The example adds a Calibration for a JEOL SEM, which automatically sets the scale based on an accompanying \*.txt file. The functionality could be extended to other scale-calibrations which are difficult to hard-code as a single resolution (other continuously-varying magnifications, like SEM tools etc.).

## Author(s)

This simple python (jython) plugin was created by {% include person id='demisjohn' %}, 2015.

I used the following plugins as inspiration: [Correct\_3D\_drift](/plugins/correct-3d-drift) and [Microscope Scale](https://imagej.nih.gov/ij/plugins/microscope-scale.html) (which sadly is no longer easily customizable).

Please see the GitHub page for issues needing coding work, and ideas for improvement. You are always welcome to contribute code to the GitHub project, it is remarkably simple due to Fiji's excellent Python API!

 
