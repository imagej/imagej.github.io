---
title: RootSystemTracker
categories: [Analysis]
description: Time-lapse tracking of root system architecture
pom-url: https://raw.githubusercontent.com/Rocsg/RootSystemTracker/main/pom.xml
---

<i>Current version : Handsome Honeysuckle (last release : July 13<sup>th</sup>, 2022).</i>

The plugin **RootSystemTracker** is an automatic analysis pipeline based on registration and topological tracking, capable of accurately describing the topology and geometry of observed root systems in 2D+t.

## Plugin features

-   2D segmentation of time series with root apparition time
-   Reconstruction of Root System Architecture
-   Movie Builder (interpolated growth of the root system, see below)
-   High-throughput (automatic batch processing)


## Demo

The following video shows the movie produced by RootSystemTracker on a specimen

{% include video platform='youtube' id='SWEqnnOhIOU'%}


## Installation

In order to install RootSystemTracker on your computer, please follow these simple steps:

1\. (if needed) Download and install Fiji from https://fiji.sc/ ; start Fiji, and let it automatically update. Then restart Fiji.

2\. Open Fiji, run the **Update manager** {% include bc path="Help | Update" %}. Click on "OK" to close the first popup windows, then click on the button **Manage update sites...**.

3\. In this list, activate **ImageJ-ITK** and **IJPB-plugins** by checking the corresponding checkboxes.

and add the **Fijiyama** repository (by clicking on the button **Add update site**, and filling the fields : name = "/plugins/fijiyama", site = https://sites.imagej.net/Fijiyama), then check the associated checkbox.

4\. Restart Fiji: a new **RootSystemTracker** entry should be available in the menu {% include bc path="Plugins | Analyze" %}. If not, go back to the Update Manager, and check that the repositories **ImageJ-ITK**, **IJPB** and **Fijiyama** are correctly selected.

5\. If you are a Windows user: there is specific issues between an external package ImageJ-ITK and the current JDK shipped with ImageJ. Whether or not you understand this point, please follow the documented procedure to escape this. You have to use ImageJ with a different JAVA version. It is well explained there: https://imagej.net/learn/faq#on-windows . You can find for example an OpenJDK 8 at OpenLogic, then install it, and when asked, check the box to select that it have to build a JAVA_HOME variable (replace a red cross symbole by a hard-disk symbol when asked, you’ll see it). After that you remove the java or jre dir in your Fiji.app, as said, and it’s ok!
The following video shows a tutorial for Fijiyama and RootSystemTracker installation:

{% include video platform='youtube' id='scm6UPlfgzU'%}

## Preparing your dataset

**Input data:** 2D + t image sequence acquired with an imaging automaton presenting a growing root system in a petri dish. Data should be organized in an input directory, one subdirectory per dish, with name patterning such as img_XX.tif, in order that ImageJ detect the image sequence autonomously.

**Output data:** 2D segmentation with root apparition time, root skeleton, root system architecture as a RSML file, and an interpolated movie of the growing root system (see below)


## Running the plugin

Open Fiji, then click on {% include bc path="Plugins | Analyze | Root System Tracker" %}
When prompted, identify the input then output path. The plugin then prompt you to edit the parameter file if needed, then run autonomously.

## Versions of RootSystemTracker

It is a living project, with frequent updates. Thanks to the Fiji updater, your version is updated each time the Fiji update starts.

Major updates include new features released, or major refactoring, while minor updates (change in the release time) should not modify deeply the behaviour of the plugin, to keep results reproducible. These information can be seen in the launching interface.

## Citing this work

-  Fernandez, R., Crabos, A., Maillard, M. et al. High-throughput and automatic structural and developmental root phenotyping on Arabidopsis seedlings. Plant Methods 18, 127 (2022). https://doi.org/10.1186/s13007-022-00960-5

## Contact

Issues, feature request ? Please contact romainfernandez06ATgmail.com
