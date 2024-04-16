---
title: Scripting TrackMate
description: Example Jython scripts for TrackMate.
categories: [Tracking, Segmentation]
project: /software/fiji
---

## TrackMate scripting principle

[TrackMate](/plugins/trackmate) can also be used without the GUI, using a scripting language that allows making calls to Java. The most simple way to get started is to use the [Script Editor](/scripting/script-editor), which takes care of the difficult & boring part for you (such as path). The examples proposed on this page all use Jython, but can be adapted to anything.

Since we are calling the internals of TrackMate, we must get to know a bit of its guts. I have tried to come up with a rational design; though not always successfully. There are three main classes to interact with in a script:

-   Model ([`fiji.plugin.trackmate.Model`](https://fiji.sc/javadoc/fiji/plugin/trackmate/Model.html)) is the class in charge of <u>storing the data</u>. It cannot do anything to create it. It can help you follow manual modifications you would made in the manual editing mode, interrogate it, ... but it is conceptually just a data recipient.

<!-- -->

-   Settings ([`fiji.plugin.trackmate.Settings`](https://fiji.sc/javadoc/fiji/plugin/trackmate/Settings.html)) is the class storing the fields that will configure TrackMate and pilot how the data is created. This is where you specify what is the source image, what are the detector and tracking algorithms to use, what are the filters to use, etc...

IMPORTANT! You will see in the example below that all detectors and trackers are configured in the `Settings` object using a `Map` (e.g. in Java) or a `dict` (e.g. in Python). You need to know the keys of the dictionary for each detector and tracker, and the type of values they accept. 

All the keys of the known detectors and trackers are documented [in this page](/plugins/trackmate/scripting/trackmate-detectors-trackers-keys).

<!-- -->

-   TrackMate ([`fiji.plugin.trackmate.TrackMate`](https://fiji.sc/javadoc/fiji/plugin/trackmate/TrackMate.html) is the guy that does the actual work. In scripts, we use it to actually <u>perform the analysis tasks</u>, such as generating spots from images, linking them into track, etc... It reads configuration information in the Settings object mentioned above and put the resulting data in the model.

So getting a working script is all about configuring a proper `Settings` object and calling `exec*` methods on a `TrackMate` object. Then we read the results in the `Model` object.


## A full example

Here is an example of full tracking process, using the easy image found in the [first tutorial](/plugins/trackmate/tutorials/getting-started). The following (Jython) script works as following:

-   It fetches the image from the web
-   It configures settings for segmentation and tracking
-   The model is instantiated, with the settings and imp objects
-   The [TrackMate](/plugins/trackmate) class is instantiated with the model object
-   Then the [TrackMate](/plugins/trackmate) object performs all the steps needed.
-   The final results is displayed as an overlay.

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/ExampleScript_ExecTracking.py' %}        


## Loading and reading from a saved TrackMate XML file

Scripting is a good way to interrogate and play non-interactively with tracking results. The example below shows how to load a XML TrackMate file and rebuild a full working model from it.

That way you could for instance redo a full tracking process by only changing one parameter with respect to the saved one. You might also want to check results without relying on the GUI. Etc...

For the example below to work for you, you will have to edit line 25 and put the actual path to your TrackMate file.

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/ExampleScript_ReadTrackMateFile.py' %}


## Display spot, edge and track numerical features after tracking

This example shows how to extract numerical features from tracking results.

TrackMate computes and stores three kind of numerical features:

-   Spot features, such as a spot location (X, Y, Z), its mean intensity, radius etc...
-   Edge or link features: An edge is a link between two spots. Its feature typically stores the velocity and displacement, which are defined only for two consecutive spots in the same track.
-   Track features: numerical features that apply to a whole track, such as the number of spots it contains.

By default, TrackMate only computes a very limited number of features. The GUI forces TrackMate to compute them all, but if you do scripting, you will have to explicitly configures TrackMate to compute the features you desire. This is done by adding feature analyzers to the settings object.

There are some gotchas: some feature analyzers require other numerical features to be already calculated. If something does not work, it is a good idea to directly check the preamble in the source code of the analyzers ([TrackMate feature logic](https://github.com/fiji/plugins/trackmate/blob/master/src/main/java/fiji/plugin/trackmate/features/)).

Finally, depending on their type, numerical features are not stored at the same place:

-   Spot features are simply conveyed by the spot object, and you can access them through `spot.getFeature('FEATURE_NAME')`
-   Edge and track features are stored in a sub-component of the model object called the FeatureModel ({% include github repo='fiji' branch='master' path='src-plugins/plugins/trackmate_/src/main/java/fiji/plugin/trackmate/FeatureModel.java' label='FeatureModel.java' %}).

Check the script below to see a working example.

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/ExampleScript_GetTrackingData.py' %}


## Exporting to TrackMate file, to CSV files, to simple track files

This script demonstrates several ways by which TrackMate data can be exported to files. Mainly: 1/ to a TrackMate XML file, 2/ & 3/ to CSV files, 4/ to a simplified XML file, for linear tracks.

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/ExampleScript_ExportToFiles.py' %}


        
## Manually creating a model

TrackMate aims at combining automatic and manual tracking facilities. This is also the case when scripting: a part of the API offers to a edit a model extensively. A few code patterns must be followed.

First, every edit must happen between a call to `model.beginUpdate()` and `model.endUpdate()`:

    model.beginUpdate()
    # ... do whatever you want to the model here.
    model.endUpdate()

The reason for this is that TrackMate caches each modification made to its model. This is required because we can deal with a rather complex content. For instance: imagine you have a single track that splits in two branches at some point. If you decide to remove the spot at the fork, a complex series of events will happen:

-   First, three edges will be removed: the ones that were connected to the spot you just removed.
-   Then the spot will actually be removed from the model.
-   But then you need to recompute the tracks, because now, you have 3 tracks instead of 1.
-   But also: all the numerical features of the tracks are now invalid, and you need to recompute them.
-   And what happens to the track name? What track, amongst the 3 new ones, will receive the old name?

Well, TrackMate does that for you automatically, but for the chain of events to happen timely, you must make your edits within this `model.beginUpdate() / model.endUpdate()` code block.

This script just shows you how to use this construct to build and populate a model from scratch. Appending content to a model is done by, sequentially:

-   Creating spot objects. You have to provide their x, y, z location, as well as a radius and a quality value for each. At this stage, you don't provide at what frame (or time) they belong.
-   This is done by adding the spot to the model, using `model.addSpotTo(Spot, frame)`, frame being a positive integer number.
-   Then you create a link, or an edge as it is called in TrackMate, between two spots. You have to provide the link cost: `model.addEdge(Spot1, Spot2, cost)`.

Spot quality and link cost are typically useful to quantify automatic spot detection and linking. We typically use negative values for these two numbers when doing manual edits.

The script below does this: ![](/media/plugins/trackmate/trackmate-animatedname.gif)

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/ExampleScript_CreateTrackingData.py' %}

## Making TrackMate macro recordable with a 64-line script

Contributed by {% include person id='imagejan' %} during a NEUBIAS course. Quoting from Jan:

> "The macro language is too limited to work with such awesome things as TrackMate, but that you can do everything with a more powerful scripting language. So when using a 64-line script to call it, it actually is macro recordable."

{% include code org='fiji' repo='TrackMate' branch='master' path='scripts/Run_TrackMate_Headless.groovy' %}

## Add 3D maximas in the ROI Manager using TrackMate

Using the 3D spots finder of TrackMate, it is possible to add the maximas to the ROI Manager with a simple Jython code:

```python
# @ImagePlus imp

# Imports
from fiji.plugin.trackmate.detection import LogDetector
from net.imglib2.img.display.imagej import ImageJFunctions

from ij.plugin.frame import RoiManager
from ij.gui import PointRoi

# Set the parameters for LogDetector
img = ImageJFunctions.wrap(imp)
interval = img
cal = imp.getCalibration()
# Get the calibration from the metadata if exists
calibration = [cal.pixelWidth, cal.pixelHeight, cal.pixelDepth]

# Values to enter based on the TrackMate GUI
radius = 5  # the radius is half the diameter
threshold = 1050
doSubpixel = True
doMedian = True


# Setup spot detector (see http://javadoc.imagej.net/Fiji/fiji/plugin/trackmate/detection/LogDetector.html)
#
# public LogDetector(RandomAccessible<T> img,
#            Interval interval,
#            double[] calibration,
#            double radius,
#            double threshold,
#            boolean doSubPixelLocalization,
#            boolean doMedianFilter)

detector = LogDetector(img, interval, calibration, radius, threshold, doSubpixel, doMedian)

# Start processing and display the results
if detector.process():
    # Get the list of peaks found
    peaks = detector.getResult()
    print str(len(peaks)), "peaks were found."

    # Add points to ROI manager
    rm = RoiManager.getInstance()
    if not rm:
        rm = RoiManager()

    # Loop through all the peak that were found
    for peak in peaks:
        # Print the current coordinates
        print peak.getDoublePosition(0), peak.getDoublePosition(1), peak.getDoublePosition(2)
        # Add the current peak to the Roi manager
        roi = PointRoi(peak.getDoublePosition(0) / cal.pixelWidth, peak.getDoublePosition(1) / cal.pixelHeight)
        # Set the Z position of the peak otherwise the peaks are all set on the same slice
        roi.setPosition(int(round(peak.getDoublePosition(2) / cal.pixelDepth))+1)
        rm.addRoi(roi)
    # Show all ROIs on the image
    rm.runCommand(imp, "Show All")

else:
    print "The detector could not process the data."
```

## Save track and spot statistics to CSV

To directly save to CSV (instead of displaying the tables in the GUI), you can use the TrackTableView API:

```python
#@ TrackMate tm
#@ File (style="save") csvFileSpots
#@ File (style="save") csvFileTracks
#@ File (style="save") csvFileAllSpots

from fiji.plugin.trackmate.visualization.table import TrackTableView
from fiji.plugin.trackmate.visualization.table import AllSpotsTableView
from fiji.plugin.trackmate import SelectionModel
from fiji.plugin.trackmate.gui.displaysettings import DisplaySettings

# Create default SelectionModel and DisplaySettings
sm = SelectionModel(tm.getModel())
ds = DisplaySettings()

# Save spot and track statistics
trackTableView = TrackTableView(tm.getModel(), sm, ds)
trackTableView.getSpotTable().exportToCsv(csvFileSpots)
trackTableView.getTrackTable().exportToCsv(csvFileTracks)

# Save all spots table
spotsTableView = AllSpotsTableView(tm.getModel(), sm, ds)
spotsTableView.exportToCsv(csvFileAllSpots.getAbsolutePath())
```

(Note that this script uses a SciJava `#@` parameter to get the current `TrackMate` instance. If you created an instance in your own script already, you can use this one directly.)
