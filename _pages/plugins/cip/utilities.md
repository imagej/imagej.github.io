---
title: CIP Utilities
---

This page provides user documentation for the utility functions of the [CIP](/plugins/cip) package

{% include cip/nav %}

# measure

## Description

This function performs measures in image and region and return them as a table.

## Signature

```
outputTable = cip.measure( inputImage*, measures*, unit, prefix )
```
perform the specified measures on the entire input image.

```
outputTable = cip.measure( regions*, measures*, source, unit, prefix )
```
perform the specified measures for each of the provided region. if provided the source image is used for intensity measure.

## Input

* `inputImage*` : the image to measure
* `regions*` : a region or list of regions to be measured.
* `measures*` : a string or a list of strings taken from {`min`, `max`, `mean`, `stddev`, `median`, `position`, `boundary`, `size`} and representing the measure to be performed
* `source` : a image that will be used to perform the intensity based measure if the input is of type region. if not provided the measure will be done on the input object intensity
* `unit` : is a boolean value indicating to use or not the image pixel size. Default is true.
* `prefix` : is a string that will be set at the beginning of each column header in the output. It can be used for instance to differentiate measures performed on the same object withdifferent source image. Default is an empty string.

## Output

* `outputTable` : the measures table. Each column represent one of the requested measure while the first column provides a reference to the measures object. Each row contains the measures performed for a particular object.

## Example

```
regions = cip.region(labelMap)
table = cip.measure(regions, 'size' , 'nuclei' )
cip.show( table )
```

In the first line labelMap is the left image in the illustration below. In the second line, 'size' is the measure performed, 'nuclei' is used to customize region names (see object column in the illustration below). <img src="/media/plugins/cip/cip-measure.png" title="fig:CIP_measure.PNG" width="400" alt="CIP_measure.PNG" />

## Implementation
The measure function instanciate a toolbox adapted for the object to measure. the toolbox can receive new measures tools to extend the existing measure set.

# show

## Description

show display CIP data within IJ1 component: hyperstack viewer, results table and log window. this ensures easy communication and reuse of the data by the rest of imageJ ecosystem.

## Signature

```
handle = cip.show( inputImage* , color )
```
will display an hyperstack viewer with the name of the image and the requested color luts.

* `inputImage*` : the image to display.
* `color` : a string or a list of string representing a Look Up Table available inImageJ menu. For basic colors using the first letter of the lut is enough ('r' in place of 'red' or 'rgb' in place of \['red','green','blue'\]).

## Signature

```
cip.show( region*, handle, color, width, scalar, reset )
```
will add region contours to the overlay of the image pointed by handle and with the specified properties: color, width, scalars.

* `region*` : a region or list of regions. this works with bot 2d and 3d regions.
* `handle` : a string with the name of the window where region(s) will bedisplayed. if no string is provided, region will be shown on the image currentlyin focus in ImageJ.
* `color` : a string representing a colors or a lut available in imageJ menu.default is 'lila'. Colors have priority on lut of the same name.
* `width` : a scalar representing contour width in point. default is 1.
* `scalars` : a list of scalars representing a region attribute and being used tochoose region color in the lut. default is \[1,2,..., n\] where n is the numberof region provided as input.
* `reset` : a boolean indication whether or not to reset the overlay. The defaultis false.

## Signature

```
handle = cip.show( inputTable*, handle, reset)
```
will display an IJ1 results table with same headers and rows as the input table.

* `inputTable*` : a table to display.
* `handle` : a string with the name of the results table where the data will beappended.
* `reset` : a boolean indication whether or not to reset the results table. Thedefault is false.

## Signature

```
handle = cip.show( message* )
```
will display the message in IJ1 log window.

* `message*` : a string to display in the IJ1 log window.

## Signature

```
cip.show( TrackMateModel*, image, mode, track style, track depth )
```
will display tracks detected with trackmate or cip.track in trackscheme or overlaid in an hyperstack viewer.

* `TrackMateModel*` : a TrackMate model object returned by cip.track or createdwith the trackmate api.
* `image` : an image on which the track can be displayed, if not provided an emptyimage the same size as the one used for the tracking will be used.
* `mode` : a string in {<u>'image'</u>,'trackscheme','all'}. default is 'image'.When image is chosen tract are displayed in image overlay. With 'trackscheme' thetrackscheme ui is used to display the tracks.
* `track style` : a string in {<u>'all'</u>,'local','backward','forward''selection'}. 'all' is the default. depending of the value the track are shownentirely ('all'), a few step before('backward') or after ('forward') currenttime, both before and after ('local').
* `track depth` : a scalar defining the number of step draw in 'local', 'backward'and 'forward' track style. Default is 10.

## Output

* `handle` : a string with the name of the created results table or image window.

## Example
This example demonstrate how to label a gray level image and overlay the contour of the detected region on orignal image.

```
labelMap = cip.label(img, 'threshold', 500)
regions = cip.region(labelMap)
h = cip.show(img) # display img
cip.show(h, regions, 'glasbey' ) # overlay the region contour to img
```

<img src="/media/plugins/cip/cip-show-region.png" title="fig:CIP_show_region.PNG" width="650" alt="CIP_show_region.PNG" />

An example script displaying tracks can found [here](https://github.com/benoalo/CIP/blob/master/scripts/tracking_cip.py)

## Implementation
The show function relies on IJ1 component as a starting point as this is the way data are displayed when downloading a fresh version of Fiji. this also ensure that this data can easily be seen and processed the usual way by any imageJ plugins.

# region

## Description

This function is a converter is that IJ1 or IJ2 object and convert them to CIP regions.

## Signature

```
region = cip.region( image, name )
```
will convert an image to a region or a list of region.

## Input
 
* `image` : an image that will be interpreted as a mask if it has boolean type oras a label image otherwise.
* `name` : a string that will be used to name the region. if there are multipleregion the name will be appended with a scalar to differentiate the regions.

## Output

* `region` : a region if the input is boolean a list of region otherwise.

# toIJ1

## Description

Is a converter that converts image to ImagePlus and CIP regions to rois.

## Signature

```
IJ1_image = cip.gauss( image*)
```
converts an image (of any type) to an ImagePlus.

```
IJ1_roi = cip.gauss( region*)
```
converts a region (of any type) to Rois.

## Input

* `image*` : the image to convert to IJ1 ImagePlus.
* `region*` : a region or a list of region to convert to a list of list of Rois(where each list of Rois represents the 2d contours of a 3D object)

## Output

* `IJ1_image` : and ImagePlus version of the input image
* `IJ1_rois` : a list of list of Rois. each of the input region will berepresented by a list of Rois where each Roi is the contour of a 2d sectionthrough the region.

# toIJ2

## Description

Converts an image (of any type handled by CIP) to an IJ2 Dataset and a region (of any type handled by CIP) to an Imglib2 IterableRegion.

## Signature

```
IJ2_image = cip.toIJ2( image* )
```
converts an image to an IJ2 Dataset.

```
IJ2_region = cip.toIJ2( region* )
```
converts an image to an ImgLib2 IterableRegion.

## Input

* `image*` : an image to convert
* `region*` : a region or a list of region to convert

## Output

* `IJ2_image` : an image of type Dataset
* `IJ2_region` : a list of Iterable region

# spacing

## Description

Retrieves the pixel size of the input image

## Signature

`pixelSize = cip.spacing( inputImage* )`

## Input

* `inputImage*` : the image process

## Output

* `pixelSize` : a list of scalars representing the input image pixel size along each image dimension

# unit

## Description

Retrieves the units of the input image

## Signature

```
units = cip.unit( inputImage* )
```

## Input

* `inputImage*` : the image to process

## Output

* `units` : a list of string representing the input image unit along each image dimension

# axes

## Description

Retrieves the axes names of the input image

## Signature

```
axesName = cip.axes( inputImage* )
```

## Input

* `inputImage*` : the image process

## Output

* `axesName` : a list of string representing the input image axes names along each image dimension

# list

## Description

utility functions creating a Java list of object from a list of object.

The function was created for a technical reason. In Jython passing a list to CIP function (i.e. a java function) can be wrongly interpreted causing problem down the line. To avoid that `list(...)` converts a list of object to a java list of object.

## Signature

```
a list of scalar = cip.list( scalar1 , scalar2, ... )
a list of scalar = cip.list( [scalar1 , scalar2, ...] )
```
converts a list of scalar to a java list of scalars

```
a list of scalar = cip.list( string1 , string2, ... )
a list of scalar = cip.list( [string1 , string2, ...] )
```
converts a list of string to a java list of string

# help

TODO
