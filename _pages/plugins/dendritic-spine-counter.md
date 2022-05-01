---
title: Dendritic Spine Counter
description: Streamlined data entry and computer vision assisted operations for counting dendritic spines in neuronal slices
categories: [Annotation,Segmentation,Feature Extraction]
icon: https://raw.githubusercontent.com/Mighty-Data-Inc/dendritic-spine-counter/main/src/main/java/images/icons/dsc--find-spines.png?token=AABJVJLPWILI3C6C4QEA7JDBQDGM4
---

*Dendritic Spine Counter* creates a modular wizard dialog to assist neuroscientists
with the task of counting dendritic spines in microscope images. It 
achieves this through the use of statistics-based 
computer vision algorithms to partially 
(and optionally) automate the detection of features, and the organization 
of user interfaces to provide a quick and convenient way for users to enter, 
consolidate, tabulate, and save their data.

It was debuted to the neuroscience community online via a virtual poster
presentation on Nov 11, 2021, at the [2021 annual meeting of the Society 
for Neuroscience](https://www.sfn.org/meetings/neuroscience-2021/). 
[**View the Neuroscience 2021 poster presentation**](http://todo-do-this)

## Downloading and Installing the Plugin
Users of ImageJ can acquire and install *Dendritic Spine Counter* in a number of ways.

### Using the ImageJ Update System
The most straightforward and "official" way to get *Dendritic Spine Counter* is to 
use ImageJ's existing update system. This approach will keep *Dendritic Spine Counter*
automatically up-to-date whenever you run ImageJ (assuming you are running the updater).

From within a running instance of ImageJ (sample screenshots show Fiji):
1. Click on "Help"
1. Click on "Update..."
1. Click on "Manage update sites"
1. Find the update site "Mighty Data, Inc.", and check the checkbox to the left of it. It *should* show up in your list automatically. If it's not present in your list of update sites, you may need to add it. You can do so by clicking "Add update site", and entering the following information:
    * Name: `Mighty Data, Inc.`
    * URL: `https://sites.imagej.net/mightydatainc/`
1.  Click on "Close", and follow the prompts. You should see ImageJ downloading several JAR files. Afterwards, *Dendritic Spine Counter* should appear in your list of plugins.

![Dendritic Spine Counter installation via ImageJ Update.](https://raw.githubusercontent.com/Mighty-Data-Inc/dendritic-spine-counter/main/documentation/images/installation-from-imagej-updater.jpg)

### From GitHub Releases
You can download the latest stable release from the GitHub repository. The process for doing so is pretty simple, but you'll have to actively rememeber to download new releases yourself if you care about staying up-to-date should *Dendritic Spine Counter* get new features or bug fixes.

1. Find the latest release on [the project's release page](https://raw.githubusercontent.com/Mighty-Data-Inc/dendritic-spine-counter/releases).
1. Download the JAR file.
1. Move the JAR file to the `plugins` subdirectory of the directory where ImageJ is installed on your computer.

![Copying the JAR file to your plugins folder.](https://raw.githubusercontent.com/Mighty-Data-Inc/dendritic-spine-counter/main/documentation/images/installation-copy-to-plugins.jpg)


### How you know it worked
After you perform any of the above download and installation sequences, you'll need to relaunch ImageJ. Upon relaunch, *Dendritic Spine Counter* can be found in the `Plugins` menu.

![Dendritic Spine Counter resides in the Plugins dropdown.](https://raw.githubusercontent.com/Mighty-Data-Inc/dendritic-spine-counter/main/documentation/images/01-03.2-Plugins-menu.jpg)


## User Manual
Please read the usage guide for a detailed walkthrough of how to use the software's features and capabilities.

[***Dendritic Spine Counter* Usage Guide**](https://github.com/Mighty-Data-Inc/dendritic-spine-counter/blob/main/documentation/Usage.md)

## Further Reading 

### Whitepaper 
If you wish to use *Dendritic Spine Counter* in research that you intend to formally submit
in a paper or presentation, you'll probably need to know how it works. Fortunately,
*Dendritic Spine Counter* was intentionally built with very straightforward methodologies
and operating principles. We've eschewed artificial neural networks and other machine learning techniques
in favor of heuristic and statistical approaches, so as to permit neuroscientists to use the
software with a confident understanding of what it's doing and how it's doing it. 

[***Dendritic Spine Counter* Whitepaper**](https://github.com/Mighty-Data-Inc/dendritic-spine-counter/blob/main/documentation/Paper.md)

### GitHub Project Page
This project is hosted on GitHub. 

[***Dendritic Spine Counter* GitHub project page**](https://github.com/Mighty-Data-Inc/dendritic-spine-counter)

### ImageJ Plugin
This project is primarily released through ImageJ as a plugin. We maintain a plugin page
on the ImageJ extension list. 

[***Dendritic Spine Counter* ImageJ plugin page**](https://imagej.net/plugins/dendritic-spine-counter)

### Society for Neuroscience 2021 Materials

*Dendritic Spine Counter* was presented as a virtual poster at the
2021 annual conference of the Society for Neuroscience.

[**Read the abstract**](https://www.abstractsonline.com/pp8/#!/10485/presentation/19804)

[**View the virtual poster presentation**](https://www.abstractsonline.com/pp8/#!/10485/presentation/19804)

