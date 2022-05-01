---
mediawiki: User:Pattersg
title: George Patterson
name: George Patterson
github: pattersg
---

**Photoswitching FRET experiment analysis**

These macros and plugins are designed to analyze experiments in which photoswitchable fluorescent proteins have been switched off. The kinetics of their decays in the presence and absence of an acceptor can be used to determine a FRET efficiency. These are meant to be updated through Fiji's updater using the URL to this page in the update site list. However, links to .ijm files or java archive files are indicated below. You will need to remove the timestamps and checksums from the names before using. Simply removing everything after .ijm or .jar in the file name before placing in the macros or plugins folder, respectively, should suffice.

**psFRET analysis macros**

The macros are designed to be used with images collected through an image splitter and may be of limited use. However, someone with a working knowledge of the ImageJ macro language can adapt them in a straightforward manner to accommodate most images.

The Dual-View image analysis macro can be downloaded or copied from here [1](https://sites.imagej.net/Pattersg/macros/psFRET_dual_view_image_analysis.ijm-20180801100053).

The curve-fitting macro can be downloaded or copied from here [2](https://sites.imagej.net/Pattersg/macros/psFRET_curve_fitting_analysis.ijm-20181217151301)

**psFRET_TProfiler**

This plugin was designed to accomplish the same goal of the macros above except it should hopefully be more versatile. A downloadable jar is available here [3](https://sites.imagej.net/Pattersg/plugins/psFRET_TProfiler-0.1.0-SNAPSHOT.jar-20181217151301).

The source code is available on GitHub.

https://github.com/pattersg/psFRET_TProfiler

**Photoswitching_Pixel_Fitter**

This plugin is designed to extract values at every pixel and fit the fluorescence decays to a single exponential with offset equation. Multi-exponential fitting is not implemented. A downloadable jar file is available here [4](https://sites.imagej.net/Pattersg/plugins/Photoswitching_Pixel_Fitter-0.1.0-SNAPSHOT.jar-20181217151301).

The source code is available on GitHub.

https://github.com/pattersg/Photoswitching_pixel_fitter

**Photoswitching Anisotropy FRET experiment analysis**

These macros are designed to analyze experiments in which photoswitchable fluorescent proteins have been switched off while monitoring anisotropy. These are meant to be updated through Fiji's updater using the URL to this page in the update site list. However, links to .ijm files or java archive files are indicated below. You will need to remove the timestamps and checksums from the names before using. Simply removing everything after .ijm in the file name before placing in the macros folder should suffice.

**psAFRET analysis macros**

The Dual-View image psAFRET analysis macro can be downloaded or copied from here [5](https://sites.imagej.net/Pattersg/macros/PS_AFRET_dual_view_image_analysis.ijm-20200103105654).

The curve-fitting and anisotropy calculation macro can be downloaded or copied from here [6](https://sites.imagej.net/Pattersg/macros/PS_AFRET_r_calculation.ijm-20200103105654)
