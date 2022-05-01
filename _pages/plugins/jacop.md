---
title: JaCoP
categories: [Analysis,Colocalization]
doi: 10.1111/j.1365-2818.2006.01706.x
name: JaCoP
license-url: /licensing/lgpl
license-label: LGPLv3
team-developers:
- Fabrice P. Cordelières | mailto:Fabrice.Cordelieres@gmail.com
- Susanne Bolte | mailto:Susanne.Bolte@upmc.fr
---

# JACoP

{% include notice icon="info" content='This page describes **J**ust **A**nother **Co**localization **P**lugin, not the [Java Constraint Programming solver](http://jacop.org).' %}

**This plug-in is a compilation of co-localization tools.**

## Authors

Fabrice P. Cordelières, Bordeaux Imaging Center (France). Fabrice.Cordelieres at gmail dot com
Susanne Bolte, IFR 83, Paris (France). Susanne.Bolte at upmc.fr

## Features

JACoP allows:

***Calculating a set of commonly used co-localization indicators:***

-   Pearson's coefficient
-   Overlap coefficient
-   k1 & k2 coefficients
-   Manders' coefficient

***Generating commonly used visualizations:***

-   Cytofluorogram

***Having access to more recently published methods:***

-   Costes' automatic threshold
-   Li's ICA
-   Costes' randomization
-   Objects based methods (2 methods: distances between centres and centre-particle coincidence)

All methods are implemented to work on 3D datasets.

## Description

JACoP has been totaly re-written, based on user feedback. The interface has been re-designed to offer full access to all the options, based on a unique Swing frame.

![JACoP v2.0: The new interface](/media/plugins/jacop-interface.jpg)

It includes a "Zoom/Reset button" which allows the user to set the two selected images side-by-side, automatically adapting the zoom. For each method selected, the user's attention is drawn on options to set, by highlighting the appropriate tab by turning its caption to red.

## References/Citation

When using the current plugin for publication, please refer to our review (see below), to this webpage and of course to ImageJ. A copy of your paper being sent to both of our e-mail adresses would also be greatly appreciated!

{% include citation %}

JACoP v2.0 was released for the second ImageJ User and Developer Conference in November 2009. The conference proceedings related the plugin is available [1](https://conference.imagej.net/2008/jacop_ijconf2008.pdf%7Chere).

## Installation

Simply download [JACoP\_.jar](https://imagejdocu.list.lu/_media/plugin/analysis/jacop_2.0/just_another_colocalization_plugin/jacop_.jar) to the Plugins folder of ImageJ, restart ImageJ and use the "JACoP" command in the Plugins menu.

## Download

Plugin available here: [JACoP\_.jar](https://imagejdocu.list.lu/_media/plugin/analysis/jacop_2.0/just_another_colocalization_plugin/jacop_.jar)

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

Copyright (C) 2006 Susanne Bolte & Fabrice P. Cordelières

## Changelog

2.0 (07/11/2008):

-   New interface: one window presenting all options
-   JACoP is now fully macro recordable
-   Added the objects based method
-   Added the "Zoom/Reset button" allowing to set the two selected images side-by-side, automatically adapting the zoom.

2.1 (01/04/2010):

-   Fixed a bug leading to an error in the Manders' coefficients calculation when applying a threshold to images.

2.1.1 (20/08/2010):

-   Fixed a bug about distance based co-localization when calling the function from a macro.
