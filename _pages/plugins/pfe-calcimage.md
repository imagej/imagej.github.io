---
title: Import Maps from PFE-CalcImage and perform measurements
description: A series of macros to import maps from Probe Software CalcImage and plot and extract line profile data and area measurements
section: Extend
categories: [Import, Microscopy, Electron Microprobe]
---

##Purpose
To import quantified maps from Probe Software [Hyperlink](https://www.probesoftware.com/) CalcImage into ImageJ and assist with measurements

##Description
1. Allow import of Probe Software CalcImage .TXT files into channel stacks
2. Plot line profiles for channel stacks
3. Plot data table for lines in channel stacks
4. Measure areas for channel stacks

##Installation
Download zip folder containing macros from [Hyperlink](https://github.com/Benjamin-Buse/PFE-ImageJ/blob/main/PFE_CalcImage.zip). Unzip the folder and copy it to the plugin folder within ImageJ installation. If ImageJ is open, restart. Then should be visible within plugin menu.

##Usage
Prior to import into ImageJ, in CalcImage export quantified grd files to ascii txt
Once images have been imported into ImageJ:
Before running line profile draw a line on the channel stack, using the line tool, if you double click on the line tool a wide line can be selected
Before running measure area draw an area on the channel stack, using the rectangle, circle or freehand tool
