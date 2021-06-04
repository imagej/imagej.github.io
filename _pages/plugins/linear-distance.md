---
mediawiki:
- Linear_Distance
- LinearDistance
title: LinearDistance
categories: []
---

{% capture source%}
{% include github org='kleinsimon' repo='PointAnalysis' %}
{% endcapture %}
{% include info-box software='ImageJ' name='Linear Distance' maintainer='Simon Klein' author='Simon Klein' source=source released='15/04/2016' latest-version='29/12/2016' status='Alpha' category='[Plugins](/plugin-index)' website='' %}

Plugin for ImageJ to measure linear distances in images in X and Y direction. At this time, two methods are implemented: First, the automatic scan of a binarized, two phased image. Second, the interactive placement of marks which will be measured afterwards (Linear Interception).

More information on github.

For automatic installation in Fiji, add update site SimonKlein.

## LinearDistance

Plugin for ImageJ to measure linear distances in binary images in X and Y direction. It scans an image linewise (with a given skip distance) in both directions and finds stripes of only black or white and calculates the mean length of these stripes.

## Application

Used for the calcuation of mean free paths in a two phase material.

## Dependecies

tested with ImageJ 1.50e and Fiji

## Installation

Copy the File **LinearDistance\_.jar** in the plugins/jars folder. When using Fiji, you can simply add the update site **LinearDistance**.

## Usage

Open one or more binary (black/white) images or binarize an image. Start the plugin by selecting {% include bc path="Plugins|Analyze|Measure linear distances" %} and select the results you want to obtain.

## Available Options

| Option                         | Description                                                            |
|--------------------------------|------------------------------------------------------------------------|
| Apply image calibration        | Applies the set scale of each image to the results (by multiplying it) |
| Step distance between measures | The number of pixels/units to skip between the analyzed lines          |
| Calibrate step distance        | Skip units instead of pixels                                           |
| Measure all opened images      | When not selected, only the active image will be analyzed              |
| Standard Deviations            | Print standard deviations for all measurements                         |
| Numbers                        | Print the number of counted stripes                                    |
| Both Phases                    | Calculates also the mean of both (all) Phases (Black and White)        |

## Source

Source available at [https://github.com/kleinsimon/LinearDistance/](https://github.com/kleinsimon/LinearDistance/)
