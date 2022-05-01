---
mediawiki: Interactive_Fitting
title: Interactive Fitting
categories: [Plotting]
---

{% include info-box software='ImageJ 1.x' name='Interactive\_Fitting' author='Fred Damen' filename='Interactive\_Fitting.jar' source=' [Interactive\_Fitting.zip](/media/plugins/interactive-fitting.zip)' released='1 April 2020' status='stable' category='Plotting' website='' %}

The Interactive\_Fitting plugin provides the ability to fit plotted data to an equation and plot the results on the same plot, and to be able to update the plot without refitting if you suspect there is a better set of parameters or a better equation. I had noticed that an ability to fit a plotted dataset using CurveFitter was added to the PlotWindow(Data&gt;&gt;Add fit...). I needed more functionality, so...

N.B., I wish to express gratitude to the immense work that I was able to add a little part to.

## Features

<img src="/media/plugins/interactive-fitting.jpg" width="800"/>  
**PlotWindow** identifies the PlotWindow that contains the plot of interest.  
**DataSource** identifies the plotted dataset of interest.  
**Fit** identifies the desired fitting. The *<user defined>* option allows an arbitrary equation, using the macro language, to be specified. The rest of the options are CurveFitter predefined fitting options. A user specified equation which is essentially the same as a CurveFitter option may not fit exactly the same.  
**Equation** specifies the equation that is fitted and plotted in black. If *Shift-Enter* is pressed in this field, another equation line is added so that it can be plotted, red, green, blue, respectively. No fitting is performed on these addition equations. N.B., if the results of the **Copy to Clipboard** were pasted into the primary equation window, and upon *Enter* being pressed, the fields will be filled in as per the clipboard information.  
**letter** specifies the parameter value as per the primary equation. The values will be used for initial values. For the *<user defined>* option all the parameters are required. For CurveFitter fitting options, if the first value is blank they will be ignored as initial parameters. The values can be changed and if *Enter* is pressed the plot(s) will be updated with the updated parameters.  
**Offset** is used by CurveFitter for user defined equations. Not required.  
**Multiplier** is used by CurveFitter for user defined equations. Not required.  
**Automatically reset the parameters for doFit as they are currently set.** This is useful when the DataSource keeps changing and the fits should all start the same.  
**Auto doFit when the identified DataSource(the plot object) changes.**  
**doFit** causes the fit to be performed and the results plotted.  
**update** causes the equation(s) to be replotted with the current set of parameters.  
**Copy to Clipboard** allow the information from the current settings to be captured for later use. May be pasted into the primary equation field to recover the current equations/parameters settings.  
The *status field* presents any pertinent details about the fitting / updating.

## Coding Goodies

Fancy control of the GUI so that only relevant information is used.

Evaluating equations using the macro processor.

Interrogating plots and reacting as they change.

## Install

Unzip [Interactive\_Fitting.zip](/media/plugins/interactive-fitting.zip) into ImageJ 1.x plugins {% include bc path="File|Show Folder|Plugins" %} or plugins/jars directories. Source code in jar file.  
{% include bc path="Plugins|Interactive|Interactive\_Plotting..." %}

## Licence

GPL distribution licence.

## ChangeLog

1 April 2020 Initial version.

## Known Bugs

Let me know.

 
