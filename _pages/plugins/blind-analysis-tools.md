---
mediawiki: Blind_Analysis_Tools
title: Blind Analysis Tools
categories: [Uncategorized]
---

{% include info-box name='Blind Analysis Tools' software='Fiji' source=' [on GitHub](https://github.com/ahtsaJ/Blind-Analysis-Tools)' author='Astha Jaiswal, Holger Lorenz' maintainer='Astha Jaiswal, Holger Lorenz' status='Active' %}

## Introduction

These tools have been developed to facilitate blind i.e., unbiased analysis of (image) data.

## Installation

To install on Fiji, check the update site called "**Blind Analysis Tools**". To install on ImageJ 1.x, download the .jar file [here](https://github.com/ahtsaJ/Blind-Analysis-Tools/releases/tag/v1.0), save it in the Plugins folder and restart ImageJ. "Blind Analysis Tools" will appear under the Plugins menu.

## File Name Encrypter

This tool copies randomly selected (image) files to a new subfolder (output folder, name: "BlindRandomFiles" + timestamp) with encrypted names. A mapping file (name: "Mappings" + timestamp) is also saved, which maps encrypted names to original names. The tool first asks to choose a directory containing files and to select file extensions of interest. Only the files with the selected extensions are considered hereafter. The number of available files (*n*) is displayed at the top. The tool offers basic and advance modes.

1.  In **basic mode**, only one parameter i.e., the number of files to be copied/encrypted is required.


{% include img align="center" name="File Name Encrypter: Basic mode." src="filenameencrypterbasic" %}

1.  In **advance mode**, you can decide if files should be grouped. When grouping is set to "No", each file is treated as an independent entity. To group files, set the option to "Yes" and provide a substring.

{% include img align="center" name="File Name Encrypter: Advance mode." src="filenameencrypteradvance" %}

Grouping comes in handy when, for example, different channels are saved in separate files with related names and you would like to keep the relation even with encrypted names. The tool will look for the first occurrence of the substring in the names of the available files to determine groups. The groups can be of different sizes. File names not containing the substring will be treated as independent entities. In the output folder, all file names in a group will start with the same cryptic string and will have different suffixes. For example, when the following six files are available:

1404\_1\_w1TL-BF\_tub0.mat, 1404\_2\_w1TL-BF\_tub1.mat, 1404\_1\_w2SD-561.tif, 1404\_1\_w3SD-488.tif, 1404\_2\_w2SD-561.tif, 1404\_2\_w3SD-488.tif

* Grouping "No" will result in the number of entities/groups = 6

* Grouping "Yes" with Substring "\_w" will result in the number of entities/groups = 2. File names will be split as follows:



|File name | Part 1 | Part 2 |
| :---: | :---: | :---: |
|1404\_1\_w1TL-BF\_tub0 |1404\_1 |\_w1TL-BF\_tub0 \|
|1404\_2\_w1TL-BF\_tub1 |1404\_2 |\_w1TL-BF\_tub1 \|
|1404\_1\_w2SD-561 |1404\_1 |\_w2SD-561 |
|1404\_1\_w3SD-488 |1404\_1 |\_w3SD-488 |
|1404\_2\_w2SD-561 |1404\_2 |\_w2SD-561 |
|1404\_2\_w3SD-488 |1404\_2 |\_w3SD-488 |

Part 1 will determine the group and part 2 will determine the suffix of each file in the group. In the above example, all files in a group are shown in the same color.

In advance mode, you can freely choose how many files should be copied in the output folder. Note that repetition would be required to copy more than n files. You can control repetition with the following parameters under **Replicates**:

* Minimum: minimum guaranteed repetitions of each file

* Maximum: maximum possible repetitions of each file

* Total: total number of files to be copied in the output folder. Total must be between minimum\*(*n* or no. of groups) and maximum\*(*n* or no. of groups).

Following are some examples of different replicates parameter settings for *n*=6 and no grouping:

| Example | Parameter setting              | Result                                                                                                                                                                                    |
|----------------------------------------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1                                      | Minimum=0, Maximum=1, Total=6  | All six files will be copied once with encrypted names.                                                                                                                                   |
| 2                                      | Minimum=1, Maximum=1, Total=6  | All six files will be copied once with encrypted names.                                                                                                                                   |
| 3                                      | Minimum=1, Maximum=2, Total=10 | All six files will be copied once with encrypted names. In addition, four files will be randomly chosen and be copied with encrypted names. No file will be repeated more than two times. |
| 4                                      | Minimum=1, Maximum=5, Total=20 | All six files will be copied once with encrypted names. In addition, 14 files will be randomly chosen and be copied with encrypted names. No file will be repeated more than five times.  |
| 5                                      | Minimum=0, Maximum=5, Total=20 | 20 files will be randomly chosen and be copied with encrypted names. No file will be repeated more than five times.                                                                       |

## Analyse & Decide

This tool facilitates blind image analysis by randomly opening an image and displaying it with an encrypted name. Therefore, the user does not see the original image name. You can provide **macro commands** to apply to each image before it is presented. This feature could be useful, for example, if you would like to remove a channel (because it is unnecessary or confusing for the analysis) prior to image display.

{% include img align="center" name="Analyse & Decide" src="analyse-decidemain" %}

It is possible to make a **decision** about an opened image, for example, weak/medium/strong or small/large, etc. You can simply type your own decision choices at the beginning by pressing the "Set" button. Provide your decision choices as a comma-separated list and press OK. Note that once you press the "Open First Image" button, the "Set" button and the macro text box will be disabled.

{% include img align="center" name="Analyse & Decide: Setting choices" src="analyse-decidesetchoices" %}

Click on the "Open First/Next Image" button to open the next image for analysis. Once you have analyzed an adequate number of files (&lt;= *n*), press done to finish the analysis. During this analysis, macro commands are recorded in the background. A decisions file (name: "BlindAnalyse&Decide\_Log" + timestamp) and a log file (name: "BlindAnalyse&Decide\_Decisions" + timestamp) will be saved in the input folder containing a detailed report of your analysis including:

* Start and end time of the analysis

* Chosen directory

* Number of available files and number of analyzed files

* Absolute names of the available and analyzed files

* Initial macro

* Recorded macro

## Limitations

1.  Currently, bio-formats files containing only one series are handled. Files containing multiple series are not correctly handled.
2.  When dealing with big files, a time lag may be experienced while copying or opening files.

## License

These tools are free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License](http://www.gnu.org/licenses/gpl-3.0.txt) for more details.

## Contact

This plugin has been developed at the ZMBH Imaging Facility, University of Heidelberg. If you found any bug or have suggestions, please write to [Astha Jaiswal](mailto:ajcjam@gmail.com) or [Holger Lorenz](mailto:h.lorenz@zmbh.uni-heidelberg.de).
