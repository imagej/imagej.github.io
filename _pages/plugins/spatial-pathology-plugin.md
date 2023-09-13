---
mediawiki: Spatial_Pathology_Plugin
name: "Spatial Pathology Plugin"
title: Spatial Pathology Plugin
categories: [Uncategorized]
dev-status: "Maintaining"
team-founder: "@ariondey"
team-maintainer: "@ariondey"
source-label: on GitHub
source-url: https://github.com/ariondey/Spatial-Pathology-Plugin
---
# Spatial Pathology Plugin

## Usage
This is a gastrointestinal-focused spatial pathology plugin to advance research in spatial analysis of GI epithelial tissues to quantify immunostaining markers in a tissue landscape through a spatial lens.

### Installing
In order to use this plugin, you need Fiji which is the latest version of ImageJ, you must use this version in order to get the remote update. This plugin is hosted on a remote webserver so you can download it using this tutorial: https://imagej.net/update-sites/following and by using the URL http://sites.imagej.net/SpatialPathology/
You only need to do this on the first install, if it was installed correctly you will see "SpatialpathologyIJMJava" in your plugins folder and if any changes are made to the plugin, all you will need to do is update your imagej. 
![UpdaterScreenshot](../assets/updater-screen-shot.png?raw=true)
### Workflow 
When you launch the plugin you will be immediately asked what you want the bin interval to be. Once an image is run, the normalized distances to user selected points will range from 0 (directly on the base line) or 1.0 (directly on the top line). 
Example (assuming you choose a bin interval of 0.1): 
```md
| 0   | 0.1  | 0.2  | (This will be your interval)
| 0   | 0.5  | 1.5  | (This will be the cells / gland)

```
 Therefore, if you want the table at the end to count instances  Once you do that, you will then be prompted and asked if you want to draw the line through uploading a .csv file of the line's coordinates. 
The structure of the csv you could upload must be as follows: 
```md
| X     | Y    |
| 0     | 0    |
| 1     | 1    |
| ...   | ...  |

Table: This table illustrates what the table you upload must look like. The file also must be saved as a .csv (notably, ImageJ interprets the UTF-8 character marker in plaintext and it will not work, so make sure it is a regular .CSV and not a .csv UTF-8.

```
If you opt to not upload a .csv of the lines, you can draw them using the segmented line tool (the one selected by default) or through the freehand line tool. The first prompt will ask for the base of the gland and the second line will be the top. 
After this, you will be asked to place points through a .csv. The format for this is exactly the same as the format for adding a line, and if you opt not to use these, you will be able to draw them manually. You will also be prompted twice to store things: once for the edited image, and once for your excel sheets.

### Batch Processing
You will be prompted if you want to repeat with another image. Every image will output both excel files detailed in data output, but keep in mind that while the xls file that has the image name will be specific to the image it ran under, the histogram will account for ALL IMAGES RUN IN THAT SESSION. MEANING: if you realize you ran the wrong type of image or you annotated it poorly, you can get the histogram results from the previous image and essentially have a clean restart point.

![BatchProcessing](/media/plugins/batch-processing.png?raw=true)
### Data Output
For saving images you will be prompted to select a folder, I would highly reccomend that you save everything in the same folder as the image, as all outputs are coded to start with the same information as the image. In my practice this has been the most sensible way to format everything. The image saving format is as a .tiff, but all inputs accepted by ImageJ are accepted in this plugin. There will also be two excel sheets as the output. One of them is all the information in the image (centroid coordinates, distances from the base to the centroid, distances from the top to the centroid and then the normalized distance). The other one the averaged out one that uses the normalized distances and the bin intervals that the user specified earlier.
![nonHistogramExcel](/media/plugins/non-histogram-excel.png?raw=true)
![HistogramExcel](/media/plugins//histogram-excel.png?raw=true)



### Common Useful Commands:
ctrl + a: Undoes your current selection, excellent way to let you redo anything that pops up

### Questions(?)
If you have any questions or issues, please contact me with concerns or create an issue within github itself. Although this is a plugin affiliated with the Weis Lab at Wake Forest University I am the sole developer so bothering them with any issues you have with this will be fruitless but I would be happy to help with anything.
