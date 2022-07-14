---
title: Using TrackMate from MATLAB
project: /software/matlab
description: Using TrackMate from MATLAB.
categories: [Segmentation,Tracking]
doi: 10.1101/2021.09.03.458852
---

This page shows how to use and control TrackMate directly from *within [MATLAB](/scripting/matlab)*. 
This is great and made possible thanks to the great [ImageJ-MATLAB](/scripting/matlab) extension, made starting in 2016 by Mark Hiner.
It makes the Fiji classes visible from [MATLAB](/scripting/matlab). 
Check this page first if you have not already. 

Apart from that, the collections of examples that follow just look like several scripts. 
Which is actually the case: We use the [MATLAB](/scripting/matlab) interpreter as a scripting interface for TrackMate, as we did in the [Scripting TrackMate](/plugins/trackmate/scripting) page. 
We separated this page to highlight [MATLAB](/scripting/matlab) specificities and to exploit its capabilities better.


## A simple tracking example

Here we open an image though Fiji (not through [MATLAB](/scripting/matlab)) and track its content. 
The results are displayed in a Fiji window as well.
[MATLAB](/scripting/matlab) is used here only to control TrackMate and does not really plays a role in the process. 
This example is actually the same that in the first [Scripting TrackMate](/plugins/trackmate/scripting) example.

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/MATLABExampleScript_1.m' %}


## Why is this greater than it seems?

Because your just ran a [MATLAB](/scripting/matlab) script that uses and benefits from multithreading without relying on any toolbox! 
Here is how to tune the number of threads used by TrackMate:

```matlab
% ... Do initialization before.
trackmate = TrackMate(model, settings);
trackmate.setNumThreads(3); % As many threads as you want.
```
