---
mediawiki: CElegansBeadsAnalysis_plugin
title: CElegansBeadsAnalysis plugin
categories: [Uncategorized]
---

This page provides a description and pointers towards the use of the CElegansBeadsAnalysis plugin. It is made available in conjunction with the publication of the paper:

Mykola Mylenko, Sebastian Boland, Sider Penkov, Julio L. Sampaio, Benoit Lombardot, Daniela Vorkel, Jean-Marc-Verbavatz, Teymuras V. Kurzchalia, NAD+ is a food component that promotes exit from dauer diapause in Caenorhabditis elegans, PLoS One, 2016

## Installation

The plugin can be downloaded from: ![](/media/plugins/celegans-beads-analysis-1.0.0.jar.zip). Its usage is described in the next section and its source code can be accessed on [MPI-CBG git repository](https://git.mpi-cbg.de/bioimage-informatics/cElegansBeadsAnalysis)

To install the plugin, download it and copy the unzipped file in your Fiji installation plugin folder. Next time you restart Fiji a new entry will appear in the Plugins menu with the name CElegansBeadsAnalysis.

## Usage

The plugin was written to quantify the ingestion of fluorescent beads by C. elegans worms in various experimental conditions. More specifically, the plugin was designed to analyze 2D images where one of the channel shows the fluorescent beads while the other one is a transmited light image of the worms.

Once the plugin is installed, you can analyze an image as follows:

-   Open Fiji and the image to analyze

<!-- -->

-   Start the plugin by clicking its menu entry

<!-- -->

-   A window will pop up requesting the following parameters
    -   **Transmission channel**: the channel with the transmitted light image of the worms ( note that channel start at 1 )
    -   **Beads channel**: The channel showing the beads fluorescent signal
    -   **Minimal mask area**: The minimum area of the regions in the worm mask
    -   **Use a manual threshold**: if checked, a manual threshold will be used to define the beads region otherwise a threshold of 3 times the mean intensity of the beads image will be used.
    -   **Manual beads Threshold**: the threshold used to detect the bead regions in case a manual threshold is requested.

<!-- -->

-   Once the parameters are set, click ok and the plugin will proceed with the analysis of the image. As a result one will obtain:
    -   An image of the worm mask
    -   An image with the beads selection on top of the beads image.
    -   2 lines are appended to the results table. The first one indicates the area (in pixel) and mean intensity of the worm mask. The second line indicates the area of the beads selection in pixel and the mean intensity of that selection in the beads image.

In further steps, the worms masks can be corrected manually if necessary. In that case, the area of the mask can be remeasured by pressing the M key. The worm mask area as well as the total beads signal is used further in the paper to analyze the relative quantity of beads ingested by worms in different experimental conditions.

Remark: Note that the plugin change the Fiji "black background" settings (in the menu {% include bc path="Process|Binary|Options..." %}) to uncheck.
