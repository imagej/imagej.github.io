---
title: Intensity Profile Tools
description: Macro toolset for horizontal/vertical intensity profiles
categories: [Feature Extraction]

name:  Intensity Profile Tools
source-url: https://github.com/LauLauThom/IntensityProfileToolset-ImageJ
release-date: 2021

license-url: /licensing/mit
license-label: mit

team-founders: "@LauLauThom"
---

# Installation 
Activate the *Intensity Profile Tools* update site in Fiji.

# Usage
After installation, you get a new entry *Intensity Profile Tools* in the `>>` menu of the ImageJ toolbar.  
Clicking this menu will load 2 macro tools in the toolbar.  

- X/Y intensity profile panel tools
When clicked, this tool will create 2 intensity profile windows : one for the vertical and one for the horizontal profile of the active image.  

- X/Y Line Profile Tool
This is an interactive tool : when selected, hovering the mouse over an image will overlay a cross-over pattern with the vertical and horizontal line profile for the current X/Y mouse position.  
Double-clicking the icon allows setting the scale factor, to adjust the amplitude of the line plot.  

Original version of the code was contributed by Nicolás De Francesco and Jerome Mutterer.  
See related [forum post](https://forum.image.sc/t/display-vertical-and-horizontal-intensity-profiles/59837).
