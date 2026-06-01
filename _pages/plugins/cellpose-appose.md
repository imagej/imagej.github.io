---
title: Cellpose-Appose 
description: PLugin to use Cellpose from Fiji relying on Appose.
source-url: https://github.com/Image-Analysis-Hub/cellpose-appose
artifact: fiji.plugin:Cellpose_Appose
categories: [Segmentation]
forum-tag: fiji, cellpose
---

This plugin install and run [cellpose](https://www.cellpose.org/) on an image (2D/3D/multi-colors/time) in Fiji. 
Two version of cellpose are available:
- Cellpose (v3, [doi:10.1038/s41592-025-02595-5](https://www.nature.com/articles/s41592-025-02595-5))  
- Cellpose-SAM (v4, [doi:10.1101/2025.04.28.651001](https://www.biorxiv.org/content/10.1101/2025.04.28.651001v1))

This plugin is based on [Appose](https://github.com/apposed/appose), that automatically install python environment and allows python script execution with shared objects with Fiji.

{% include img name="cellpose-overview" src="/media/cellpose-appose/overview.png" %}

## Installation

You can install the plugin for the unliste update site `Appose-Playground`:
- In Fiji, go to `Help>Update...`
- Select `Manage Update Sites` in the window that opens.
- Click `Add unliste update site`, name it `Appose-Playground` and write its address `https://sites.imagej.net/Appose-Playground`.
- Select the Appose-Cellpose `.jar` file to install only this plugin, or keep all proposed plugins. 
- Press `Apply changes` and restart Fiji when it's done.

{% include notice icon="warning" content=" You should have a recent version of Fiji, based on Java 21 or more. Download a new version if you're current installation is too old." %}

## Usage

The plugin handles images or movies that are 2D or 3D, that contains or not multiple channels. It can also have a temporal dimension. First open an image and then run the plugin. If you have several images opened when you launch the plugin, it will run on the active one.

From Fiji:

- Open the image that you want to process.
- Launch one of the cellpose version available in the plugin:  
    - `Plugins>Segmentation>Cellpose-Appose>Cellpose...`
      This option allows to run CellPose v3. 
      The full official Cellpose 3 documentation is available [here](https://cellpose.readthedocs.io/en/v3.1.1.1/). 
    - `Plugins>Segmentation>Cellpose-Appose>Cellpose-SAM...`
        This option allows to run CellPose v4 with SAM.
        The full official Cellpose 4 documentation is available [here](https://cellpose.readthedocs.io/en/latest/).   
- Configure your Cellpose run through the Graphic Interface. _see [here](#parameters) for documentation_  
- Press "Ok" and Enjoy!   

{% include notice icon="info"
  content="The first time you run each option of this plugin, a python environment with the requested Cellpose version will be automatically installed in your home `.local\shared\appose` directory, which will take some time. The next time you use the same option, the environment will be directly activated from the plugin when needed so it will be much faster." %}

{% include notice icon="info"
  content="Cellpose-SAM relies on a much bigger neural network than Cellpose3. Thus computation with this version takes longer and it is advised to have a GPU available." %}

___

## Parameters

After you selected a version of Cellpose, a graphical interface will pop-up to let you choose the parameters to run cellpose. See the Cellpose [documentation](https://cellpose.readthedocs.io/en/latest/) for full description of the parameters.

### Cellpose parameters

- `Cellpose model` (**Cellpose v3 only**): Select a pretrained model from Cellpose website. These models have been trained on dataset with specific biological objects, as for example nuclei for `nuclei` model. Select the model that corresponds the best to your data.
  
- `Path to custom model`: if you have fine-tuned or trained your own cellpose model, write here the full path to the directory containing the model files.
  
- `Diameter`: The prediction is sensitive to the size of the objects to detect, so you need to indicate the average diameter of the objects (cell or nuclei), in pixels. This parameter strongly affects the segmentation results for Cellpose v3, while Cellpose-SAM can handle a much bigger range of object sizes. Cellpose will resize your image(s) to have an average object size compatible to the one of the training data (30 pixels for most models), and resize back the results to your initial image size.
  &#9881; _Default value is 30 pixel_.

- `Channel selection`: Choose the color channel on the image to do the segmentation on (that contain the staining of your objects). The number of the channel to select are the same one as in the Fiji interface, starting at one for the first channel.
  - For **Cellpose 3**: you can select one or two channels, one for the main object to segment (`Cytoplasmic channel`) and an optional one for the nuclei staining (`Nuclei chanel`). When you have both stainings, selecting also the nuclei channel can help the segmentation of the contour of the cell by giving more information.
  - For **Cellpose-SAM**: Cellpose-SAM can use information from up to 3 channels to segment the objects. So select the number of channels that are relevant to segment your objects of interest.
 
- `Minimum Object Size`: At the end of the segmentation process, objects that are smaller in size (total area in pixel) from this parameter will be removed. This allows to get rid off small errors segmentation of only a few pixel.<br/>
   &#9881; _Default value is 15 pixels^2_.

- `Normalize Channel Intensity`: whether to use Cellpose's normalization or not. The normalization allows to put the images in the same range of pixel values than the one used for training to get better results. This is recommended, except if you perform your own normalization before.<br/>
  &#9881;  _Default to True (checked)_.

- `Resample Segmentation`: This allows to have more accurate boundaries when your object size is bigger than the model's size (usual 30 pixels, see `diameter` parameter), but will be slower to compute. Indeed, when this option is selected the "dynamics", i.e. the post-processing specific from cellpose to reconstruct the cells from the network's output, will be run at your original image size (at full resolution then). If it's not checked, these "dynamics" will be run on the resized image, which will be smaller if your `diameter` parameter is bigger than 30 pixels.<br/>
  &#9881; _Default value to True (checked)._

- `return ROIs` (**not for 3D images**): the default output (segmentation) that you get is a label image: each object is assigned a unique identity (label), displayed in different color. If you check this option, you will also have a Region Of Interest for each object, added to the ROIManager.
  &#9881; _Unselected by default_

### Advanced options parameters

- `Cell probability threshold`: Cellpose runs a neural network to predict the probability of a pixel to be part of an object and the direction from this pixel to the center of this object (the flows). This threshold allows to tune which pixels to keep in the final segmentation: increasing the threshold will reduce the size of detected objects, keeping only most probable pixels, while decreasing it allows to find larger and more objects.
  &#9881; _This parameter range from -6 to 6 and is 0 by default._

- `Flows threshold` (**not for 3D images**): Cellpose runs a neural network to predict the probability of a pixel to be part of an object and the direction from this pixel to the center of this object (the flows). The error between the segmentation mask and the calculated flow is calculated, and pixels with an error smaller than the threshold will be kept. Increasing this threshold will thus increase the size/number of objects kept and also allows less regular shape.
 &#9881; _This parameter range from 0 to 1 and is 0.4 by default._

- `Tile overlap`: Cellpose is dividing the input images into tiles of (256*256) and computing the neural networks in each tile, then putting back the results together. A small overlap between neighboring tiles allows to reconstruct well the cells that are on the boundaries.
 &#9881; _This parameter range from 0 (no overlap) to 1 (full overlap, doesn't make sense). Default value is 0.1 (10% overlap)._

- `Compute flows`: Cellpose runs a neural network to predict the probability of a pixel to be part of an object and the direction from this pixel to the center of this object (the flows). By default, you only get the resulting image of cell segmented with a label assigned to each cell. Checking this option allows to also get the flows images as a results. This could be usefull to change the postprocessing step for example.
 &#9881; _Not selected by default_.

- `Iterations`: The number of iterations computed by Cellpose when calculating the cell shapes from the flows (`niter` parameter in Cellpose). If the value is set to `None` (0 in the interface), Cellpose will automatically calculate it based on the cell diameter. Increase it for detecting elongated objects.
&#9881; _0 by default (None, automatic calculation)._

### 3D Options

**These options can be modified only if the image is a 3D stack (contains more than 1 slice)**. 

{% include notice icon="info"
  content="If your image should be 3D but is not detected as such (the 3D parameters cannot be modified), check that the metadata are correct: go to `Image>Properties...` and check that the number of slices is more than 1. If you have several frames and only 1 slice and the image should be 3D instead of temporal, exchange the values of number of slices and of frames and click `Ok`." %}

- `Mode 3D`: To segment cells in 3D, Cellpose proposes 2 ways to do it. First option `2D+stitch` is computing the segmentation in each 2D slice, and then reconstructing the 3D cells by linking the probable same cell accross slices. Second option `3D` is not really running in 2D: Cellpose will run on the image on `x,y` direction, `x,z` and then `y,z`. The 3D results will then be reconstructed by combining the flows calculated with each direction.
  
- `Stitch threshold` (**2D+stitch mode**): If you selected the `2D+stitch` option, Cellpose will predict the cells in each 2D slice and then will reconstruct the 3D cells by linking together cells that overlap enough between consecutive slices. This threshold controls how much cells in consecutive slices should overlap (intersection over union score). If you put 0, the cells will not be linked from one slice to another. If 1, cells would be linked as the same cell only if they are exactly the same from one slice to the next one. Decreasing this threshold allows to linked more cells together.
 &#9881; _This parameter range from 0 (no overlap) to 1 (full overlap: the cells are exactly the same). Default value is 0.0 (no 3D reconstruction)._
  
- `Flow 3d smooth` (**3D mode**): If you selected the `3D mode` option, this parameter allows to smooth the flows calculated by cellpose in 3D. The smoothing will be done with a gaussian filter with a stddev of the given parameter. This allows to have more regular 3D shapes.
 &#9881; _Default value to 0.0 (no smoothing)._
  
