
== Select Type of Dataset ==
[[File:MVR_define1.png]]

There are three types of datasets:
* Image Stacks (LOCI Bioformats)
** to open non TIFF images
* Image Stacks (ImageJ Opener)
** use this to open TIFF and zipped TIFFS
* Zeiss Lightsheet Z.1 Dataset
** experimental way of opening Zeiss data

== Define Dataset 1/3 ==

This dialog specifies of what your dataset consists of:
* timepoints
* channels
* illumination directions
* angles

[[File:MVR_define2.png]]

== Define Dataset 2/3 ==
This dialog asks you several facts:
* image directory
* image file pattern
** there are 3 different variables. They are used to identify the images. All of them can have leading zeros, e.g. {aaa} for a angle of 045 degrees or {tttt} for 0014 as a time point
*** {t} - time points
*** {c} - channel
*** {a} - angles
* time points, channels and angles can be given as a comma seperated list or in a more elegant way, {start}-{end}:{interval}
* calibration can be either read from file or entered by hand
* data container, smaller image stacks can use '''ArrayImg''', bigger one should use '''CellImg''' 

[[File:MVR_define3.png]]

In case you selected the option, a list of found files will be presented
[[File:MVR_define4.png]]
== Define Dataset 3/3 ==
Finally the plugin shows you the calibration it read from the files or asks for it.
[[File:MVR_define5.png]]

== Log File Output ==
<pre>
Dimensions of viewsetup 0 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x81
Dimensions of viewsetup 1 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x91
Dimensions of viewsetup 2 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x102
Dimensions of viewsetup 3 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x91
Dimensions of viewsetup 4 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x101
Dimensions of viewsetup 5 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x91
Dimensions of viewsetup 6 unknown. Loading them ... 
Image stack size of first stack: 1388x1040x111
(Thu Aug 21 13:35:38 CEST 2014): Saved xml '/Users/janosch/no_backup/HisYFP/./dataset_orig.xml'.
</pre>
