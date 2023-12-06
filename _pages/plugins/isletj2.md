---
mediawiki: IsletJ2
title: IsletJ2
categories: [Uncategorized]
---

## General

IsletJ2 is a tool implemented as an ImageJ plugin that segments and reports properties of the Langerhans islets. The plugin was available already in 2018 under name [IsletJ](/plugins/isletj). However, many changes have been implemented since then. The original version can be found [here](/plugins/isletj).

Perhaps the most noticable change is the new graphical user interface (GUI). We made the GUI simpler and hopefully, more comfortable to use.

Despite being invisible to users, massive changes have been done in the plugin core. The whole plugin has been rewritten from the ground up, resulting in more modular and extensible code and lesser demands on computing resources. The plugin, however, still employs the same approach as before.

## Installation

The plugin was tested to work with ImageJ 1.52 (Fiji distribution) and Java 8. Follow these steps (a general procedure to install an ImageJ plugin) to install the plugin:

1.  Start ImageJ and start updater using `Help` – `Update...`.
2.  Click `Manage update sites` and add a new site using `Add update site`, then enter a name (e.g., `IsletJ2`) and URL [`https://sites.imagej.net/IsletJ2/`](https://sites.imagej.net/IsletJ2/). Close the dialog.
3.  Click `Apply changes` to fetch and install the plugin.
4.  Restart ImageJ.

## Training

The training procedure consists of three consecutive phases:

1.  sample loading,
2.  ground truth verification,
3.  and model training.

In the first phase, a user select a directory that contains input images together with their corresponding ground truth images. IsletJ2 expects the names of the input files to have a specific format consisting of a prefix, a single underscore, and a number. The plugin uses the prefix to group the images and the ground truths, respectively, which means that all the images must have a common prefix, and the same holds for the ground truths as well. The underscore serves purely as a delimiter between the preceding prefix and the following number. Finally, the number connects an image with its ground truth. For example, the names can be set as follows.

```shell
gt_01.png
gt_02.png
image_01.png
image_02.png
```

After the images are loaded and displayed to a user, the user should verify that the plugin recognized the images and ground truths correctly. If the retrieved segmentations are correct, it is possible to advance to the last phase.

The last phase deals with model training. It is required to set a path where a model will be saved. Then, after pressing the `Train` button, the plugin will extract features from the images and start training the model.

{% include notice icon="note" content="When the training starts, the values of the form inputs are saved and will be used to pre-fill the form in the next training.

The training will probably take several minutes (depending on the number and size of the input images, or your computer performance). It also uses a lot of CPU and operational memory." %}

### Training protocol

Once the training finishes, a protocol is composed and saved to the same directory as the trained model. The protocol is a CSV file with two columns per row. Each row represents a single training example: the first and the second column contain paths to the example image and ground truth, respectively. The protocol name has a particular form, namely `isletj_MODEL_YYYY-MM-DD_hh-mm-ss.csv`, where `MODEL` is the model name, and `YYYY-MM-DD_hh-mm-ss` specifies the date and time when the protocol was created, e.g., `isletj_model-file.gz_2019-12-19_14-23-31.csv`.

## Analysis

The analysis assumes that there is a trained model somewhere in the file system.

Contrary to the training, the analysis form is straightforward. It consists of five inputs that specify:

1.  a path to a directory containing images to analyze (or choose to analyze the currently active image),
2.  the size of a pixel in micrometers,
3.  the minimal diameter of islets to consider,
4.  a path to the trained model,
5.  a path to a directory to save the analysis output.

The selected input directory must exist and must contain at least one image. Currently, the plugin supports PNG format.

The output directory must exist; and if it is not empty, the plugin will ask for a confirmation. The directory will contain a segmentation for each input image and a protocol.

{% include notice icon="note" content="the input values will be saved and pre-filled for further analyses." %}

### Analysis protocol

Similarly to the training protocol, the analysis protocol is a CSV file. There is a row for each input image and consists of 4+15 columns:

1.  path to the input image,
2.  the number of recognized islets,
3.  elliptical volume (in IEQ),
4.  spherical volume (in IEQ),
5.  the last 15 columns are for 15 different bins with diameter frequencies (based on the histogram of Ricordi).

## Demo

The following steps show basic interaction with the plugin.

1.  Download a demo [dataset](/media/plugins/isletj-demo.zip) and extract the archive. Directory `isletj-demo` will be created containing one image and its ground truth segmentation.
2.  Start ImageJ and open the dialog for training (`Plugins` – `IsletJ` – `Train`).
3.  Select the extracted directory, set the prefixes of examples and GTs to `img_` and `gt_`, respectively, and click `Load` to load the dataset. Images (only a single one in this case) from the dataset will be displayed, and respective segmentations will be applied to the images resulting in green bordered regions.
4.  Ensure that the segmentations were loaded correctly and click `Ok`.
5.  Select a file path where the trained model should be saved and start training by clicking on `Train`. The name of the model can be arbitrary, but we suggest to use suffix `.gz` since then compression will be used, resulting in a smaller size of the model.
6.  Wait until the training finishes. It should take only a few seconds in case of the demo.
7.  Close the dialog for training and open the one for analysis (`Plugins` – `IsletJ` – `Analyze`).
8.  Select the extracted directory as before (we will analyze the training image for the demo purposes), set an appropriate pixel size (e.g., 2.355 μm) and minimal size of islets (e.g., 0 μm), and select the previously trained model.
9.  Select an output directory and click `Analyze`.

## Pretrained models

Pretrained segmentation models can be downloaded [here](http://ptak.felk.cvut.cz/Medical/microscopy/IKEM/IsletJ/public/). Note that future versions of IsletJ2 need not support older segmentation models. However, we will try to maintain a compatible model for each version.

## Tips

### Keyboard shortcuts

Should you use the plugin very frequently, it would be perhaps useful to access its features via some keyboard shortcuts.

A new keyboard shortcut can be defined using `Plugins` – `Shortcuts` – `Add Shortcut...` in the top menu. In the displayed window, pick a shortcut of your choice (e.g., `F12`) and select `Analyze` or `Train` as the command.

See [ImageJ docs](https://imagej.net/ij/docs/guide/146-31.html#toc-Subsection-31.2.2) for more information on how to manage keyboard shortcuts in ImageJ.

### Determining the pixel size

Take a photo of a stage micrometer and open the photo in Fiji. Use a straight line to measure the distance from 0 to 4. Then open `Analyze` – `Set Scale...` and fill the `Known distance` input. Fiji will compute the number of pixels per micrometer. Invert the number to get the number of micrometers per pixel.

![How to measure the pixel size. Taken from the [documentation](https://github.com/jschier/IsletJ/blob/-/pdf/IsletJ_Guide_2.pdf) of the original plugin version.](/media/micrometer.png)

## Acknowledgements

The current implementation is heavily inspired by the previous implementation done by *Jan Schier*.

The method used in the plugin was developed and described in the following work:

-   Habart, D. *et al.* (2016) 'Automated Analysis of Microscopic Images of Isolated Pancreatic Islets', *Cell Transplantation*, 25(12), pp. 2145–2156. doi: 10.3727/096368916X692005.
