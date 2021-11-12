---
title: Labkit Documentation
---

# Labkit Documentation

## Interface

Labkit's interface is divided in multiple panels:

- Image: in this panel, users can toggle on/off the image in the viewer, as well as autocontrasting the current slice
- Labeling: the labeling panel lists all label layers, each of them can be shown/hidden, exported, have their colors changed...
- Segmentation: this panel allows training classifiers for automated segmentation based on the labels
- Tools: the tool bar is shown above the viewer and give users access to drawing tools in order to intereact with the labeling layers
- Viewer: the image is shown within the [BigDataViewer](/plugins/bdv) and serve as reference for labeling

## Navigating the image

Labkit uses the BigDataViewer to view the image. Navigation works as in BigDataViewer, including most shortcuts ([see here](/plugins/bdv)). Here are some useful examples:

-   {% include key keys='Ctrl|Shift|mouse-wheel' %} to zoom in and out
-   {% include key keys='right-drag' %} to move the image
-   {% include key keys='left-drag' %} to rotate a 3d image
-   {% include key key='mouse-wheel' %} to scroll through the z-slices of a 3d image

## Drawing tools

The tool bar above the viewer allows interacting with the labeling layers. It contains the following tools:

- **Move**: rotate the image
- **Draw**: draw on the currently selected labeling layer, the thickness of the pencil tool can be set using the corresponding slider
- **Flood fill**: fill an entire connected area in the currently selected labeling layer
- **Erase**: erase labeled pixels from the currently selected labeling layer
- **Remove blob**: remove an entire connected component from the currently selected labeling layer
- **Select label**: select the corresponding labeling layer
- **Allow overlapping labels**: if checked, pixels can be labeled in multiple labeling layers
- **Brush size**: Only available with the **Draw** and **Erase**, setting the size of the pencil tool

The various tools can be quickly accessed using shortcuts:

-   {% include key keys='D|left-click' %} to draw with the pencil tool.
-   {% include key keys='E|left-click' %} to erase with the pencil tool.
-   {% include key keys='F|left click' %} to use the flood fill tool.
-   {% include key keys='R|left-click' %} to remove a connected component.
-   {% include key key='N' %} - switch to next label

## Labeling

All labeling layers can be hidden/shown either globally (eye icon in the top right corner, or individually (eye icon corresponding to each layer). They can also be entirely removed by clicking on "Remove all" (bottom right). 

In order to add new layers, simply click "Add label" (bottom right). For each layer, users can change both name and color. To change the name, double click on the current one for the dialog to open. The color can be change by clicking once on the color flag. The target button moves the view to the slice with the highest number of labeled pixel in the layer. Finally, the downward arrow (equivalent to a right click) gives access to additional options, including saving the labeling as a `*.tif` file or exporting the layer to ImageJ.

More options are available in the `Labeling` menu (top of the Labkit window):

- Open Labeling: open a `.labeling` file in place of the current labels
- Save Labeling: save the current labeling layers as a `.labeling` file
- Show Labeling in ImageJ: export all labeling layers to ImageJ
- Import Labeling: add the layers contained in a `.labeling` file to the current layer list
- Import Bitmap: add layers saved as a '.tif' file to the current layer list
- Export selected Label as Bitmap: export the selected layers as `.tiff` file

## Segmentation

In the `Segmentation` panel, you can add pixel classifier, modify there settings, run to learn a segmentation and export their results.

### Pixel classification settings

<!--- Describe what filters are --->

By clicking on the wheel, you can open the pixel classification settings for a particular classifier. A window opens, which allows you to set custom filters to tune your classifier and the segmentation results.

A filter is a operation that can be applied to your image in order to extract features. In turn, these features will be used to learn the segmentation. Segmentation can be performed by clicking on the run button. The results is overlaid with the image. 

Refer to the [guidelines]() for advice on choosing filters for your segmentation task.

#### Basic filters

Basic filters are in most cases the only filters you need. Except for the `original image`, the filters are run for each sigma in the sigmas list.

- Original image
- Gaussian blur (for each sigma): for each sigma in the list, the image is Gaussian blurred with a Gaussian of corresponding standard devaition.
- Difference of Gaussians (for each sigma): 
- Gaussian gradient magnitude (for each sigma):
- Laplacian of Gaussian  (for each sigma):
- Hessian eigenvalues (for each sigma):
- Structure tensor eigenvalues (for each sigma):
- Min filters (for each sigma):
- Max filters (for each sigma):
- Mean (for each sigma):
- Variance filters (for each sigma):

#### Customizable filters

Customizable filters are filters whose parameters can be chosen by the user.

- Difference of Gaussians
- Gaussian blur
- Hessian eigenvalues 
- Gaussian gradient magnitude
- Laplacian of Gaussian
- Min filters
- Max filters
- Mean
- Structure tensor eigenvalues
- Variance filters

#### Deprecated filters

Deprecated filters are here to ensure backward compatibility with classifier trained with older versions of Labkit. We advise using only basic and customizable filters.

### Import & Export

The segmentation menu and the small arrow next to a classifier allow users to import/export various objects:

- Import/export classifier using `Open Classifier...` or `Save Classifier...`
- Save the segmentation result as `.tif` or `.h5`
- Show the segmentation in ImageJ
- Create a label layer from a segmented class

