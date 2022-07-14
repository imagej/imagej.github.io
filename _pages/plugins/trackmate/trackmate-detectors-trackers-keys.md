---
title: Setting keys for TrackMate detectors and trackers
description: Setting keys for TrackMate detectors and trackers.
categories: [Tracking, Segmentation, Scripting]
---

# Setting keys for TrackMate detectors and trackers.

The detectors and trackers in TrackMate are configured via a set of key and values. In the GUI, TrackMate takes care of presenting to the user only the settings relevant to the chosen detector or tracker, but in scripts or other program, they must be known. This document lists all the parameters of all the current known detectors and trackers in TrackMate and shows how to configure them in your scripts and programs.

## Configuring a detector and a tracker.

First a word of how to specify what detector / tracker to use, and how to configure them programmatically. 

In TrackMate, all the parameters of a tracking are specified in a `Settings` object. This object contains everything, from the source image itself to the filters on tracks. It is made so that when properly set, you can get the final results of tracking and filtering with the following lines:

```python
# imp is the source ImagePlus.
settings = Settings( imp )

# configure settings now...
settings.xyz = abc # etc see below

# Create a TrackMate instance on these settings and run it.
trackmate = TrackMate( settings )
if not trackmate.checkInput():
  print( trackmate.getErrorMessage() )
else:
  if not trackmate.process():
    print( trackmate.getErrorMessage() )
print( 'Done.' )
```

We restrict ourselves here in showing how to configure the detector and tracker in the `Settings` object.

### The detector factory.

The detector to use is determined by setting the field `Settings.detectorFactory`. The value to enter must be a `SpotDetectorFactoryBase`. For instance like this (in Python):

```python
settings.detectorFactory = LogDetectorFactory()
```

As of today (February 2022), the following spot detectors are known:

#### Built-in detectors.

They are all found in the `fiji.plugin.trackmate.detection` package.

1. `LogDetectorFactory`
2. `DogDetectorFactory` 
3. `MaskDetectorFactory`
4. `ThresholdDetectorFactory`
5. `LabeImageDetectorFactory`
6. `ManualDetectorFactory`

#### Detectors in extensions.

7. `CellposeDetectorFactory`, in the `fiji.plugin.trackmate.cellpose` package, requires the `TrackMate-Cellpose` extension.
8. `IlastikDetectorFactory`, in the `fiji.plugin.trackmate.ilastik` package, requires the `TrackMate-Ilastik` extension.
8. `MorphoLibJDetectorFactory`, in the `fiji.plugin.trackmate.morpholibj` package, requires the `TrackMate-MorphoLibJ` extension.
9. `StarDistDetectorFactory`, in the `fiji.plugin.trackmate.stardist` package, requires the `TrackMate-StarDist` extension.
10. `StarDistCustomDetectorFactory`, as above.
11. `WekaDetectorFactory`, in the `fiji.plugin.trackmate.weka` package, requires the `TrackMate-Weka` extension.

### The tracker factory.

The tracker to use is determined by setting the field `Settings.trackerFactory`. The value to enter must be a `SpotTrackerFactory`. For instance like this (in Python):

```python
settings.trackerFactory = SimpleSparseLAPTrackerFactory()
```

As of today (February 2022), the following spot trackers are known:

1. `SimpleSparseLAPTrackerFactory` in the `fiji.plugin.trackmate.tracking.sparselap` package.
2. `SparseLAPTrackerFactory` in the same package.
3. `KalmanTrackerFactory` in the `fiji.plugin.trackmate.tracking.kalman` package.
4. `OverlapTrackerFactory` in the `fiji.plugin.trackmate.tracking.overlap` package.
5. `NearestNeighborTrackerFactory` in the `fiji.plugin.trackmate.tracking.kdtree` package.
6. `ManualTrackerFactory` in the `fiji.plugin.trackmate.tracking` package.

### The settings map or dict.

Once you picked a detector factory and a tracker factory, you must input their settings using a `Map<String Object>` in Java, or a `dict` in Python.  In what follows we suppose we are using a Python script to run TrackMate and will use the syntax of its language.

So, the settings for a detector or a tracker factory are given by a collection of key / value pairs, where the keys are all strings, and the values can be `int` ,`float`, `boolean` or more rarely other objects. They must be stored in a field called `detectorSettings` for the detector and in a field called `trackerSettings ` for the tracker. For instance, an example settings for the `LoGDetectorFactory` would be the following:

```python
settings.detectorFactory = LogDetectorFactory()
settings.detectorSettings = {
    'DO_SUBPIXEL_LOCALIZATION' : True,
    'RADIUS' : 2.5,
    'TARGET_CHANNEL' : 1,
    'THRESHOLD' : 0.,
    'DO_MEDIAN_FILTERING' : False,
}
```

We need to know for each detector and tracker exactly what are the keys they support and what is the type of values they expect. This is the goal of this document.

## Key / value definition for the detectors.

### LoG and DoG detector (`LogDetectorFactory` and `DogDetectorFactory`).

These two detectors use a different implementation but relies on the same key / valeus for their settings

| Key                        | Value Type       | Description                                                  |
| -------------------------- | ---------------- | ------------------------------------------------------------ |
| `TARGET_CHANNEL`           | positive `int`   | Channel index, 1-based (1 is the first channel).             |
| `RADIUS`                   | positive `float` | The radius of the object to detect, in physical units ( μm if the pixel size is in  μm). |
| `THRESHOLD`                | positive `float` | Threshold value on quality below which detected spots are discarded. |
| `DO_SUBPIXEL_LOCALIZATION` | `boolean`        | If `True` the spot position will be refined with sub-pixel accuracy (quadratic fitting scheme). |
| `DO_MEDIAN_FILTERING`      | `boolean`        | If `True` the input will be processed by a 2D 3x3 median before detection. |

### The mask detector (`MaskDetectorFactory`).

| Key                 | Value Type     | Description                                                  |
| ------------------- | -------------- | ------------------------------------------------------------ |
| `TARGET_CHANNEL`    | positive `int` | In what channel is the mask, 1-based (1 is the first channel). |
| `SIMPLIFY_CONTOURS` | `boolean`      | If `True` the 2D contours detected will be simplified. If `False`, they will follow exactly the pixel borders. |

### The threshold detector (`ThresholdDetectorFactory`).

| Key                   | Value Type     | Description                                                  |
| --------------------- | -------------- | ------------------------------------------------------------ |
| `TARGET_CHANNEL`      | positive `int` | In what channel is the mask, 1-based (1 is the first channel). |
| `SIMPLIFY_CONTOURS`   | `boolean`      | If `True` the 2D contours detected will be simplified. If `False`, they will follow exactly the pixel borders. |
| `INTENSITY_THRESHOLD` | `float`        | The threshold on pixel value to use for segmentation.        |

### The label image detector (`LabeImageDetectorFactory`).

Careful, there is a typo in the factory name, and a 'l' is missing.

| Key                 | Value Type     | Description                                                  |
| ------------------- | -------------- | ------------------------------------------------------------ |
| `TARGET_CHANNEL`    | positive `int` | In what channel are the labels, 1-based (1 is the first channel). |
| `SIMPLIFY_CONTOURS` | `boolean`      | If `True` the 2D contours detected will be simplified. If `False`, they will follow exactly the pixel borders. |

### The manual detector factory (`ManualDetectorFactory`).

Using this detector will result in the automatic detection step to be skipped.

| Key      | Value Type       | Description                                                  |
| -------- | ---------------- | ------------------------------------------------------------ |
| `RADIUS` | positive `float` | The default radius to use when creating objects, in physical units ( μm if the pixel size is in  μm). |

### The cellpose detector (`CellposeDetectorFactory`).

| Key                        | Value Type                                                   | Description                                                  |
| -------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `TARGET_CHANNEL`           | positive `int`                                               | What channel to use as the main channel for segmentation with cellpose.  ‘0’ means that cellpose will run on a grayscale combination of all channels. ‘1’ stands for the first channel, corresponding to the red channel in a RGB image. Similarly for ‘2’ and ‘3’, the second and third channel, corresponding to the green and blue channels in a RGB image. |
| `OPTIONAL_CHANNEL_2`       | positive `int`                                               | The `cyto` and `cyto2` pretrained models have been trained on images with a second channels in which the cell nuclei were labeled. It is used as a seed to make the detection of single cells more robust. It is optional and this parameter specifies in which channel are the nuclei (‘1’ to ‘3’). Use ‘0’ to skip using the second optional channel. For the `nuclei` model, this parameter is ignored. |
| `CELLPOSE_PYTHON_FILEPATH` | `string`                                                     | Absolute path to the cellpose executable, as it was installed outside of Fiji. See [the TrackMate-Cellpose documentation](/plugins/trackmate/trackmate-cellpose) for details. |
| `CELLPOSE_MODEL`           | One of the `fiji.plugin.trackmate.cellpose` `.CellposeSettings.PretrainedModel` enum value. Can be `CYTO`, `CYTO2`, `NUCLEI` or `CUSTOM`. | What pretrained model to use for segmentation. See below to enter a custom cellpose model. |
| `CELLPOSE_MODEL_FILEPATH`  | `string`                                                     | If for the `CELLPOSE_MODEL` parameter you pick `CUSTOM`, you can use this settings to enter the path to a custom cellpose model. It must be an absolute file path. |
| `CELL_DIAMETER`            | `float` greater or equal to 0.                               | Estimate of the cell diameter in the image, in physical units. Enter the value ‘0’ to have cellpose automatically determine the cell size estimate. |
| `USE_GPU`                  | `boolean`                                                    | If `False`, cellpose will only use the CPU, even on systems where a GPU is configured. |
| `SIMPLIFY_CONTOURS`        | `boolean`                                                    | If `True` the 2D contours detected will be simplified. If `False`, they will follow exactly the pixel borders. |


### The ilastik detector (`IlastikDetectorFactory`).

| Key                   | Value Type               | Description                                                  |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| `TARGET_CHANNEL`      | positive `int`           | What channel to run through to the ilastik model, 1-based (1 is the first channel). |
| `CLASSIFIER_FILEPATH` | `string`                 | The absolute path to the ilastik project file.               |
| `CLASS_INDEX`         | `int`, 0-based.          | The index of the class specified in the ilastik file to get the probability map for. |
| `PROBA_THRESHOLD`     | `float` between 0 and 1. | The threshold on the probability map output by ilastik.      |

### The MorphoLibJ detector  (`MorphoLibJDetectorFactory`)

| Key                 | Value Type                                                   | Description                                                  |
| ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `TARGET_CHANNEL`    | positive `int`                                               | In what channel are the membrane objects, 1-based (1 is the first channel). |
| `TOLERANCE`         | `float`                                                      | The tolerance value for the morphological segmentation of MorphoLibJ. |
| `CONNECTIVITY`      | Either the `int` `6` (for 'straight' connectivity) or `26` (for 'diagonal' connectivity). | The connectivity to use when using the watershed algorithm.  |
| `SIMPLIFY_CONTOURS` | `boolean`                                                    | If `True` the 2D contours detected will be simplified. If `False`, they will follow exactly the pixel borders. |

### The StarDist detector with built-in nuclei model (`StarDistDetectorFactory`).

| Key              | Value Type     | Description                                                  |
| ---------------- | -------------- | ------------------------------------------------------------ |
| `TARGET_CHANNEL` | positive `int` | In what channel are the nuclei, 1-based (1 is the first channel). |

### The StarDist detector with custom model  (`StarDistCustomDetectorFactory`).

| Key                 | Value Type               | Description                                                  |
| ------------------- | ------------------------ | ------------------------------------------------------------ |
| `TARGET_CHANNEL`    | positive `int`           | What to segment, 1-based (1 is the first channel).           |
| `MODEL_FILEPATH`    | `string`                 | The absolute path to the model file to use in the StarDist detector. |
| `SCORE_THRESHOLD`   | `float` between 0 and 1. | Threshold on object detection. Higher values lead to fewer segmented objects, but will likely avoid false positives. |
| `OVERLAP_THRESHOLD` | `float` between 0 and 1. | Threshold on object separation. Higher values allow segmented objects to overlap substantially. |

### The Weka detector (`WekaDetectorFactory`).

| Key                   | Value Type               | Description                                                  |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| `TARGET_CHANNEL`      | positive `int`           | What channel to run through to the Weka model, 1-based (1 is the first channel). |
| `CLASSIFIER_FILEPATH` | `string`                 | The absolute path to the Weka model file.                    |
| `CLASS_INDEX`         | `int`, 0-based.          | The index of the class specified in the Weka model to get the probability map for. |
| `PROBA_THRESHOLD`     | `float` between 0 and 1. | The threshold on the probability map output by Weka.         |

## Key / value definition for the trackers.

### The simple LAP tracker (`SimpleSparseLAPTrackerFactory`).

This stripped-down implementation of the LAP tracker from *Jaqaman et al, 2008* has many parameters that are described in the next paragraph. For the purpose of this simplified version, it is best to start from the default settings returned by:

```py
settings = fiji.plugin.trackmate.tracking.LAPUtils.getDefaultLAPSettingsMap()
```

and edit the 3 following important parameters:

| Key                        | Value Type       | Description                                                  |
| -------------------------- | ---------------- | ------------------------------------------------------------ |
| `LINKING_MAX_DISTANCE`     | positive `float` | The max distance between two consecutive spots, in physical units, allowed for creating links. |
| `MAX_FRAME_GAP`            | positive `int`   | Gap-closing time-distance. The max difference in time-points between two spots to allow for linking. For instance a value of `2` means that the tracker will be able to make a link between a spot in frame `t ` and a successor spots in frame `t+2`, effectively bridging over one missed detection in one frame. |
| `GAP_CLOSING_MAX_DISTANCE` | positive `float` | Gap-closing max spatial distance. The max distance between two spots, in physical units, allowed for creating links over missing detections. |

### The LAP tracker (`SparseLAPTrackerFactory`).

This tracker is fully configurable with many parameters and feature weights.  All parameters are described in the table below. However for practical usage it is best  to start from the default settings returned by:

```py
settings = fiji.plugin.trackmate.tracking.LAPUtils.getDefaultLAPSettingsMap()
```

and edit the parameters that needs to change. For details on their meaning, please refer to the [TrackMate documentation](https://imagej.net/plugins/trackmate/algorithms#lap-trackers) and  *Jaqaman et al, 2008*.

| Key                               | Value Type                          | Description                                                  |
| --------------------------------- | ----------------------------------- | ------------------------------------------------------------ |
| `LINKING_MAX_DISTANCE`            | positive `float`                    | The max distance between two consecutive spots, in physical units, allowed for creating links. |
| `LINKING_FEATURE_PENALTIES`       | a dictionary of `string` to `float` | Specify the feature penalties for frame-to-frame linking. See below the table for how to enter this dictionary. |
| `ALLOW_GAP_CLOSING`               | `boolean`                           | If `True` then the tracker will perform gap-closing, linking tracklets or segments separated by more than one frame. |
| `MAX_FRAME_GAP`                   | positive `int`                      | Gap-closing time-distance. The max difference in time-points between two spots to allow for linking. For instance a value of `2` means that the tracker will be able to make a link between a spot in frame `t ` and a successor spots in frame `t+2`, effectively bridging over one missed detection in one frame. |
| `GAP_CLOSING_MAX_DISTANCE`        | positive `float`                    | Gap-closing max spatial distance. The max distance between two spots, in physical units, allowed for creating links over missing detections. |
| `GAP_CLOSING_FEATURE_PENALTIES`   | a dictionary of `string` to `float` | Specify the feature penalties for gap closing. See below the table for how to enter this dictionary. |
| `ALLOW_TRACK_MERGING`             | `boolean`                           | If `True` then the tracker will perform tracklets or segments merging, that is: have two or more tracklet endings linking to one tracklet beginning. This leads to tracks possibly fusing together across time. |
| `MERGING_MAX_DISTANCE`            | positive `float`                    | Track merging max spatial distance. The max distance between one tracklet end one tracklet beginning, in physical units, allowed for creating links leading to track merges. |
| `MERGING_FEATURE_PENALTIES`       | a dictionary of `string` to `float` | Specify the feature penalties for track merging. See below the table for how to enter this dictionary. |
| `ALLOW_TRACK_SPLITTING`           | `boolean`                           | If `True` then the tracker will perform tracklets or segments splitting, that is: have one tracklet ending linking to two or more tracklet beginnings . This leads to tracks possibly separating into several sub-tracks across time, like in cell division. |
| `SPLITTING_MAX_DISTANCE`          | positive `float`                    | Track splitting max spatial distance. The max distance between one tracklet end one tracklet beginning, in physical units, allowed for creating links leading to track splits. |
| `SPLITTING_FEATURE_PENALTIES`     | a dictionary of `string` to `float` | Specify the feature penalties for track merging. See below the table for how to enter this dictionary. |
| `ALTERNATIVE_LINKING_COST_FACTOR` | positive `float`                    | Factor used to compute alternative costs in the LAP matrix.  |
| `CUTOFF_PERCENTILE`               | positive `float` from 0 to 1.       | Cutoff percentile                                            |
| `BLOCKING_VALUE`                  | positive `float`                    | Blocking value: cost for mon-physical, forbidden links. Default value is `Infinity`. |

#### The feature penalty map.

Feature penalties are a way to alter individual linking cost by using the numerical features computed for all spots. We repeat here how individual costs they are calculated for this tracker.

The user is asked for a maximal allowed linking distance (entered in physical units, via *e.g.* the `LINKING_MAX_DISTANCE` parameter), and for a series of spot features, alongside with penalty weights. These parameters are used to tune the cost matrices. For two spots that may link, the linking cost is calculated as follow:

1. The distance between the two spots D is calculated

2. If the spots are separated by more than the max allowed distance, the link is forbidden, and the cost is set to infinity. If not,

3. For each feature in the map, a penalty p is calculated as
   ```
   p = 3 × W × |f1−f2| / ( f1+f2 )
	 ```
   where `W` is the weight associated to the feature in the map. This expression is such that:

   - there is no penalty if the 2 feature values `f1` and `f2` are the same;
   - with a weight of 1, the penalty is 1 if one feature value is the double of the other;
   - the penalty is 2 if one feature is 5 times the other one.

4. All penalties are summed, to form `P = (1 + ∑ p )`

5. The cost is set to the square of the product: `C = ( D × P )²`

If the user feeds no penalty, the costs are simply the distances squared.

The penalties are specified via a dictionary that maps the feature key to the weight `W` for this feature. For instance to specify a feature penalty for the frame-to-frame linking step on the spot radius with a weight of 2 and on the mean intensity in channel 1 with a weight of 5, create the following dict:

```python
penalty = {
    'RADIUS' : 2.,
    'MEAN_INTENSITY_CH1' : 5.
}
```

and use it as the value of the `LINKING_FEATURE_PENALTIES` key. This will penalize linking spots that have very different radii and small difference in the mean intensity.

You must use the **keys** of the features, not their name. Here is the table of the feature keys and names for the spot features:

| Spot feature key                                    | Spot feature name                                   |
| --------------------------------------------------- | --------------------------------------------------- |
| `MEAN_INTENSITY_CH1`, `MEAN_INTENSITY_CH2`, ...     | Mean intensity ch1, Mean intensity ch2, ...         |
| `MEDIAN_INTENSITY_CH1`, `MEDIAN_INTENSITY_CH2`, ... | Median intensity ch1, Median intensity ch2, ...     |
| `MIN_INTENSITY_CH1`, `MIN_INTENSITY_CH2`, ...       | Min intensity ch1, Min intensity ch2, ...           |
| `MAX_INTENSITY_CH1`, `MAX_INTENSITY_CH2`, ...       | Max intensity ch1, Max intensity ch2, ...           |
| `TOTAL_INTENSITY_CH1`, `TOTAL_INTENSITY_CH2`, ...   | Sum intensity ch1, Sum intensity ch2, ...           |
| `STD_INTENSITY_CH1`, `STD_INTENSITY_CH2`, ...       | Std intensity ch1, Std intensity ch2, ...           |
| `CONTRAST_CH1`, `CONTRAST_CH2`, ...                 | Contrast ch1, Contrast ch2, ...                     |
| `SNR_CH1`, `SNR_CH2`, ...                           | Signal/Noise ratio ch1, Signal/Noise ratio ch2, ... |
| `ELLIPSE_X0`, `ELLIPSE_Y0`                          | Ellipse center x0, Ellipse center y0                |
| `ELLIPSE_MAJOR`, `ELLIPSE_MAJOR`                    | Ellipse long axis, Ellipse short axis               |
| `ELLIPSE_THETA`                                     | Ellipse angle                                       |
| `ELLIPSE_ASPECTRATIO`                               | Ellipse aspect ratio                                |
| `AREA `                                             | Area                                                |
| `PERIMETER `                                        | Perimeter                                           |
| `CIRCULARITY `                                      | Circularity                                         |
| `SOLIDITY `                                         | Solidity                                            |
| `POSITION_X`, `POSITION_Y`, `POSITION_Z`            | X, Y and Z position                                 |
| `QUALITY`                                           | The spot detection quality                          |
| `RADIUS`                                            | The spot radius                                     |

### The Kalman tracker (`KalmanTrackerFactory`).

| Key                    | Value Type       | Description                                                  |
| ---------------------- | ---------------- | ------------------------------------------------------------ |
| `LINKING_MAX_DISTANCE` | positive `float` | The initial search radius, in physical units, specifying how far two spots can be apart when initiating new tracks. |
| `KALMAN_SEARCH_RADIUS` | positive `float` | The max search radius specifying how far from a predicted position the tracker should look  for candidate spots. |
| `MAX_FRAME_GAP`        | positive `int`   | The max difference in time-points between two spots to allow for linking. For instance a value of `2` means that the tracker will be able to make a link between a spot in frame `t ` and a successor spots in frame `t+2`, effectively bridging over one missed detection in one frame. |

### The overlap tracker (`OverlapTrackerFactory`).

| Key               | Value Type                           | Description                                                  |
| ----------------- | ------------------------------------ | ------------------------------------------------------------ |
| `SCALE_FACTOR`    | positive `float`                     | Scale factor:  enlarging (&gt;1) or shrinking (&lt;1) the spot shapes before computing their intersection over union (IoU). |
| `MIN_IOU`         | positive `float`                     | Minimal IoU below which links are not created.               |
| `IOU_CALCULATION` | `string`, either `FAST` or `PRECISE` | What method to use for IoU calculation.                      |

### The nearest-neighbor tracker (`NearestNeighborTrackerFactory`).

| Key                    | Value Type       | Description                                                  |
| ---------------------- | ---------------- | ------------------------------------------------------------ |
| `LINKING_MAX_DISTANCE` | positive `float` | The max distance, in physical units, specifying how far two spots can be apart to be linked. |

### The manual tracker (`ManualTrackerFactory`)

Using this tracker will result in the automatic tracking step to be skipped. It has no parameter.
