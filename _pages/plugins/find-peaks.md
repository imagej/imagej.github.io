---
mediawiki: Find_Peaks
name: "Find Peaks"
title: Find Peaks
categories: [Scripting,Analysis]
tags: [local maxima,local minima,extrema,inflection point, signal processing, spectral analysis]
initial-release-date: "February 2014"
team-founder: "@tferr"
team-maintainer: "@tferr"
---

{% capture filename%}
{% include github org='tferr' repo='Scripts' branch='master' path='BAR/src/main/resources/scripts/BAR/Data_Analysis/Find_Peaks.bsh' %}
{% endcapture %}

{% capture source%}
{% include github org='tferr' repo='Scripts' branch='master' path='README.md\#data-analysis' %}
{% endcapture %}
{% include info-box filename=filename source=source category='Analysis, Scripting' %}

A [BAR](/plugins/bar) script (written in [BeanShell](/scripting/beanshell)) that retrieves local maxima and minima from an ImageJ plot. The easiest way to install *Find Peaks* is by [subscribing](/plugins/bar#installation) to the BAR [update site](/list-of-update-sites).

## Options

{%- capture FindPeaksSnapshot-title -%}
Analysis of synthetic data plotted from a .csv file. CSV files can be imported into ImageJ by drag and drop, or by using {% include bc path="File | Import | Results" %}. Once [options](#options) are specified, coordinates of retrieved peaks are logged to the table of a new plot window'
{%- endcapture -%}
{% include thumbnail src='/media/plugins/findpeakssnapshot.png' title=FindPeaksSnapshot-title %}

Peak amplitude  
The smallest depth (in Y-axis units) that a qualified valley must exceed. By default, it is set to one standard deviation of the data.

<!-- -->

Min. value of maxima  
The smallest value (in Y-axis units) a qualified maxima must exceed. This filter is disabled when set to *NaN* (Not a Number).

<!-- -->

Max. value of minima  
The highest value (in Y-axis units) a qualified minima must not exceed. This filter is disabled when set to *NaN* (Not a Number).

<!-- -->

Min. peak distance  
The smallest separation between peaks (in X-axis units). When this value is not zero (the default), smaller peaks within the specified vicinity will be ignored. This works in the following way: 1) Identified peaks that fulfill all of the above criteria are sorted in descending order (largest to smallest amplitude); 2) Beginning with the largest peak, the script ignores all remaining peaks that are not separated by more than the specified *Min. peak distance*. Applies to both maxima and minima.

<!-- -->

Exclude peaks on edges of plot  
If active, a peak is only accepted if it is separated by two qualified valleys. If disabled (the default), peaks at the limits of the data range (i.e., flanked only by one valley) are also considered.

<!-- -->

List values  
If active, the Plot's table will be displayed (as frontmost window), allowing values to be saved programmatically when calling *Find Peaks* from other macros or scripts. Examples:

<!-- -->

    // From an ImageJ macro
    run("Find Peaks", "min._peak_amplitude=35 min._peak_distance=0 min._value=NaN max._value=NaN list");
    saveAs("Results", "/Path/to/Output/Directory/Plot Values.csv");
    run("Close");

    // From a script
    IJ.run("Find Peaks", "min._peak_amplitude=35 min._peak_distance=0 min._value=NaN max._value=NaN list");
    IJ.saveAs("Results", "/Path/to/Output/Directory/Plot Values.csv");
    WindowManager.getActiveWindow().close()

## Notes

-   Both maxima and minima are listed in descending order, from the largest to smallest amplitude
-   Peaks with flat tops are retrieved at their centers
-   Peak coordinates are logged according to the following layout: \[*X0,Y0*\]: Original data; \[*X1,Y1*\]: Maxima; \[*X2,Y2*\]: Minima
-   *Min. peak distance* can be used for peak width filtering
-   Use *Scientific notation* and *Decimal places* in {% include bc path='Analyze|Set Measurements...'%} to improve the representation of values that are too big or too small to be displayed in the decimal form
-   Find Peaks was initially though as a [complementary tool](/plugins/sholl-analysis#complementary-tools) for [Sholl Analysis](/plugins/sholl-analysis) but it that can be applied to any dataset. For this reason, it is now part of [BAR](/plugins/bar)

## Related Resources

Analysis of 1D-signals was discussed in March 2014 on the [ImageJ mailing list](https://list.nih.gov/cgi-bin/wa.exe?A1=ind1403&L=IMAGEJ#32). That discussion highlighted the following alternatives to *Find Peaks*:

-   [PeakFinder Tool](http://simon.bio.uva.nl/objectj/examples/PeakFinder/peakfinder.html) by Norbert Vischer, a [macro](/scripting/macro) tool that retrieves intensity peaks along a straight line ROI.
-   [Multi-Peak fitting using R](https://wiki.cmci.info/documents/120206pyip_cooking/python_imagej_cookbook#rmulti-peak_fitting_using_r) by Kota Miura, a [Jython](/scripting/jython) script that calls the [R](http://www.r-project.org) package [Peaks](http://cran.r-project.org/web/packages/Peaks/index.html). Requires [Rserve](http://www.rforge.net/Rserve/doc.html) ([instructions](https://wiki.cmci.info/documents/101105ij_r_jython#using_r_from_imagej_via_rserve))
-   [Fast Filters plugin](http://imagejdocu.list.lu/doku.php?id=plugin:filter:fast_filters:start) by Michael Schmid, a collection of unidirectional filters that can be applied to to rows or columns in an image ([instructions](https://list.nih.gov/cgi-bin/wa.exe?A2=ind1403&L=IMAGEJ&F=&S=&P=136934)).

## Installation

The easiest way to install *Find Peaks* is by [subscribing to the BAR update site](/plugins/bar#installation).

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [Free Software Foundation](http://www.gnu.org/licenses/gpl.txt). This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

  
