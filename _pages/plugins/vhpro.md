---
mediawiki: User:Idavidhf
title: VHPro
categories: [Uncategorized]
---

VHPro is an image-based plugin for relative measurements using custom ROIs.

| Author        | {% include person id="idavidhf" %}                            |
| Date          | 2016/09/08                                                    |
| Requirements  | ImageJ 1.17y or later                                         |
| Limitations   | Requires unwarped/undistorted and a thresholded 8-bit stack.  |
| Source        | `VHPro_.java`                                                 |
| Installation  | copy `VHPro_.class` to the plugins folder and restart ImageJ. |

This plugin uses ImageJ's particle analyzer to track n-objects, in vertical
order, through a stack. Imposition of the real time betwen stack frame is
allowable, also the output results in calibrated or uncalibrated unities.
It can be customized to given graphical outputs from the results.

## See also

* [MultiTracker](https://imagej.net/ij/plugins/multitracker.html)
* [Manual Tracking](/plugins/manual-tracking)
* [SpotTracker](/plugins/spottracker)
* [MTrack2](/plugins/mtrack2)
* [MTrackJ](/plugins/mtrackj)
