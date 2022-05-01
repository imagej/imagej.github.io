---
mediawiki: EpiGraph
title: EpiGraph
artifact: EpiGraph
categories: [Uncategorized]
---

{% include notice icon="info" content="Please note that, this plugin is focused on biology research. This web page doesn't provide a complete explanation of usability. Deep detailed information can be found in the manuscript: [**EpiGraph: an open-source platform to quantify epithelial organization**](https://www.biorxiv.org/content/10.1101/217521v2), and in the official lab website: https://www.scutoids.es/" %}

{\| \|style="vertical-align:top" \| \|<span>  
</span>}


## **Introduction**

The [EpiGraph](/plugins/epigraph) is a Fiji plugin that combines computational geometry and graph theory to measure the degree of arrangement in any made by computational or natural tessellation. Here, a tessellation is treated as a network in which the edges are defined by the regions contacts. A network can be split up into different subgraphs named graphlets. The comparison of the quantity of each type of graphlets with the reference tessellations provide the Graphlet degree Distribution Distances (GDDs) as a marker of arrangement. This plugin has into account three different reference patterns: a "hexagonal lattice", a "random Voronoi Diagram" (generated Voronoi from seeds located randomly) and a "Voronoi Diagram 5" (which represents the common polygon distribution in nature). They have been used to compute a set of references that quantify organization: Epi-Hexagons, Epi-Random and Epi-Voronoi5, respectively.

It contains a set of visualization tools, together with graphical user interfaces for easy extraction and analysis of information. The collected data of arrangement can be exported to excel tables for being processed with other tools as well.

On top, to encourage the sharing of resources, [EpiGraph](/plugins/epigraph) is published under an open-source (GPLv3) license, which can be downloaded from https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/blob/master/LICENSE.

## **Pipeline**

EpiGraph consists of a pipeline of 5 very simple steps. First, the skeleton of a mosaic image is uploaded and the individual cells are identified. Second, there is a step where the user selects the distance threshold to identify two cells as neighbours. Here it is possible to select different thresholds and to check the number of neighbours of every cell in each case. Third, a ROI is selected. There are several possibilities such as a default ROI from the image or the selection of individual cells. Fourth, the graphlet information for the selected cells is calculated, obtaining the Epi-Hexagons, Epi-Random and Epi-Voronoi5. These values are incorporated to a table and serve as input data for a statistical analysis that indicates if a new image is inside or outside of the CVTn path, and what is the Voronoi diagram that presents the most similar organization to the sample. The fifth step includes the classification and labelling of different images in order to represent them in a new window. This final phase allows exporting the representation of the data in a three-dimensional graph. The next videos explain in detail each operation and the three GUI windows are shown as well:

### Installation and initial settings

[*1. Install EpiGraph*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/installEpiGraph%20.mp4)

[*2. Uninstall EpiGraph*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/Uninstalling%20EpiGraph.mp4)

[*3. Set the maximum RAM memory*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/Select%20your%20maximum%20RAM%20memory.mp4)

### Calculation of GDDs

[*4. Calculate graphlets - default*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/calculateGraphlets_default.mp4)

[*5. Calculate graphlets - select invalid region*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/invalidRegion.mp4)

[*6. Calculate graphlets - squared shape*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/graphletsSquareShape.mp4)

[*7. Calculate graphlets - 4 kind of motifs*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/mo29_mo17_mo10_mo7.mp4)

[*8. Calculate graphlets - 4-connectivity*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/connectivity4.mp4)

[*9. Calculate graphlets - ROI selection*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/roiSelection.mp4)

[*10. Calculate graphlets - large image*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/largeImage.mp4)

### Exporting and importing GDDs data

[*11. Export supplementary graphlets results*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/exportingGraphlets.mp4)

[*12. Export and import GDDs - main window*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/importExportExcel.mp4)

### Visualizing results

[*13. Visualizing window*](https://github.com/ComplexOrganizationOfLivingMatter/Epigraph/raw/master/tutorials/visualizingWindow.mp4)

## **Limitations**

EpiGraph only accepts single images right now. A stack of images should be adapted to single frames before uploading it to EpiGraph. Also, computers with little RAM memory (less than 16gb) will work but with a series of restrictions. For ensuring the usability, it is not recommended computing images with a high number of cells (more than 1000) due to a possible lack of memory. In the same way, we suggest skeletonizing the edges of the images and using a small radius (lower than 3) to calculate the cell's neighbourhood. Likewise, we warn if the input image is large (either 3000px of height or 3000px of width) in the case you have limited resources. Choosing an elevated radius value could slow down the work queue, increasing the use of RAM memory. On the other hand, computers with greater RAM memory will work with more complex and larger images and a wide range of radius.

If any of these requirements are not satisfied, the program alerts the user allowing him/her to change the image provided. Importantly, the images and the ROIs require a minimum number of cells in order to get coherent graphlets.

Regarding the 3D visualization tool, it allows the user to see the position of the samples from different angles. However, the resolution of the exported file is only 72 pixels per inch (dpi). This could be too low for publications and therefore EpiGraph provides an excel table with all the information needed to represent it with other programs. In addition, you can download any of the CVTn references (29-motifs, 17-motifs, ...) from the 'Visualizing window'.
