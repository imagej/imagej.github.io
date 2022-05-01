---
mediawiki: SpotCounter
title: SpotCounter
categories: [Particle Analysis]
---


{% capture source%}
{% include github org='nicost' repo='spotCounter' %}
{% endcapture %}
{% include info-box software='ImageJ' name='SpotCounter' author='Nico Stuurman (nico.stuurman at ucsf.edu)' maintainer='[Nico Stuurman](Nico_Stuurman)' filename='' source=source released='2015/07/30' latest-version='2018/01/18 (Version 0.14)' status='' category='Particle Analysis' %}

Simple ImageJ/Fiji plugin to count spots in image stacks. The plugin detects local maxima by scanning the image with a box of user-defined size. Local maxima are accepted when the maximum is higher than a user-defined number over the average of the 4 corners of the box. The plugin outputs the number of spots per frame, the average intensity of all identified spots in a frame, and an estimate of the background intensity. Data can optionally be automatically copied to the System Clipboard. When selecting "Append new results", the default ImageJ Results table will be used for each subsequent run of the plugin, and the filename of the analyzed data will be listed with the results. This really is a simple plugin meant to facilitate the work-flow of certain experiments in the lab.

To install this plugin check the "ValelabUtils" update site in the Fiji updater.

![](/media/plugins/spotcounter.jpg) ![](/media/plugins/spotcounterv013.png) ![](/media/plugins/spotcounterresults.gif)

<b>History:</b>  
2018-01-18 - Version 0.14: Updated build system. Now is compiled to Java 8 bytecode.  
2017-08-10 - Version 0.13: Added "append" option. Also adds the name of the data to the table.  

 
