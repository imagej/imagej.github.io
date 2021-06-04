---
mediawiki: User:CrossSectionalAnalyzer
title: Cross Sectional Analyzer
name: Cross Sectional Analyzer
source-url: https://github.com/mattrothman/cross-sectional-analysis
source-label: on GitHub
release-date: 2020/05/14
team-developers: Thalia Barr-Malec, Nalin Richardson, Matthew Rothman
categories: [Uncategorized]
---

This plugin takes in an image of muscle fibers, outlines and numbers all of the
fibers, and outputs a table of each fiber's area as well as an RGB Color image
of the numbered fiber outlines on a black background.

<img src="/media/fibers.png" title="fig:Input Image" width="300" alt="Input Image" /> <img src="/media/plugins/fiberoutlines.png" title="fig:Output Image" width="300" alt="Output Image" />

## Installation

1. Download
   [Cross-sectional-analysis.zip](/media/plugins/cross-sectional-analysis.zip), unzip
   it and locate `Cross_Sectional_Analyzer.jar`.

2. Open the package contents of ImageJ, and navigate to `ImageJ/plugins/Filters`.

3. Put `Cross_Sectional_Analyzer.jar` inside the `ImageJ/plugins/Filters` folder, and restart imageJ.

4. Once ImageJ opens, open an image to analyze, and calibrate the image. To run
   the plugin, use
   {% include bc path="Plugins|Filters|Cross Sectional Analyzer" %}.
