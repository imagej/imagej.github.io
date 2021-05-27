---
mediawiki: Analyzing_TrackMate_results_with_MATLAB
title: Analyzing TrackMate results with MATLAB
categories: [Tracking,Matlab,tutorials]
---

This page documents the various ways to exchange data between [TrackMate](/plugins/trackmate) and [MATLAB](/scripting/matlab).

## Introduction

[TrackMate](/plugins/trackmate) was originally designed solely as a tracking tool. Its goal was just to generate the tracks then another tool was supposed to analyze these tracks. Nonetheless, we built some crude analysis facilities in TrackMate for rapid inspection. But in no way they can compete with a proper dedicated, custom analysis tool.

I favor [MATLAB](/scripting/matlab) as a tool for data analysis. Therefore the interoperability facilities first deal with this software.

## Location and installation of import functions

These tools take the form of several, hopefully well documented [MATLAB](/scripting/matlab) functions that are shipped with in your Fiji installation. All of them are located in the `scripts` folder of your Fiji package

```
tinevez@primevere:~/Development/fiji> cd ~/Applications/Fiji/Fiji.app/scripts/
tinevez@primevere:~/Applications/Fiji/Fiji.app/scripts> ls
InstallJava3D.m              Matlab3DViewerIntroduction.m
IsJava3DInstalled.m          Miji.m
Matlab3DViewerDemo_1.m       Miji_Test.m
Matlab3DViewerDemo_2.m       bfopen.m
Matlab3DViewerDemo_3.m       importTrackMateTracks.m
tinevez@primevere:~/Applications/Fiji/Fiji.app/scripts>
```

If you did not do it already, there is a configuration step to take in [MATLAB](/scripting/matlab), so as to make [MATLAB](/scripting/matlab) aware of these files. You need to add the `scripts` folder to the [MATLAB](/scripting/matlab) path:

In [MATLAB](/scripting/matlab), select in the menu {% include bc path='File | Set Path...'%} and add the `scripts` folder there (on Mac, the file chooser doesn't let you choose directories within .app packages, so you have to use the [MATLAB](/scripting/matlab) command `addpath('/Applications/Fiji.app/scripts')` or whatever folder works for you).

## Importing track files

TrackMate has an action to export a simplified XML file containing only the tracks as spot positions. It is only suitable for linear tracks: tracks that are non-branching, non-merging. In that case, there is a [MATLAB](/scripting/matlab) function that can use this XML file to import the tracks and retrieve the relevant metadata:

```matlab
>> [tracks, md] = importTrackMateTracks('RealPhotobac20min_Tracks.xml');
>> tracks

tracks =

    [125x4 double]
    [ 99x4 double]
    [125x4 double]
    [126x4 double]
    ...

>> md

md =

       spaceUnits: 'pixel'
        timeUnits: 's'
    frameInterval: 5
             date: 'Thu, 8 Aug 2013 13:33:23'
           source: 'TrackMate v2.1.0'
```

Check the help section to learn about the output format (`doc importTrackMateTracks`). But basically, each track is represented by a `double` array in a cell array (one cell per particle). The `double` array itself is organized as `T X Y Z` with T by default being the frame integer number.

There exists one flag that can remove the Z dimension in 2D case. And another that can scale the time value so that it is in physical units rather than frame number. Again, check the function documentation for details.

## Application examples and links

There are some specialized tools in [MATLAB](/scripting/matlab) that can exploit TrackMate results. For instance, here is a [MATLAB](/scripting/matlab) class that performs [mean-square displacement analysis](http://www.mathworks.com/matlabcentral/fileexchange/40692-mean-square-displacement-analysis-of-particles-trajectories). It is hopefully well documented in this [[MATLAB](/scripting/matlab) tutorial](http://www.mathworks.com/matlabcentral/fileexchange/40692-mean-square-displacement-analysis-of-particles-trajectories/content/msdanalyzer/MSDTuto.html).

{% include person id='tinevez' %} ([talk](User_talk_JeanYvesTinevez)) 10:35, 8 August 2013 (CDT)
