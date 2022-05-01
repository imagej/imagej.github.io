---
mediawiki: SlideJ
title: SlideJ
categories: [Uncategorized]
---

**SlideJ**

SlideJ is an ImageJ plugin for processing digital slides (also known as virtual slides, WSI, etc). SlideJ is an ImageJ plugin for processing digital slides (also known as virtual slides, WSI, etc). SlideJ has been tested on slides in the following formats: Aperio .SVS, Leica .SCN, Hamamatsu .NDPI, Mirax, Generic tiled TIFF and regular TIFF. It works by splitting the slide in square tiles and iterating a user-configurable macro on each of them.

SlideJ can be called directly from the ImageJ user interface, but as many other plugins, also from another macro. At launch, a modal dialog is shown to configure the main execution parameters.

SlideJ is available at https://github.com/MITEL-UNIUD/SlideJ

*Motivation*

SlideJ was created to provide a common framework for rapid prototyping of image processing and analysis of digital slides using ImageJ. It is based on Bio-Formats, which already provides digital slide access, but SlideJ adds a layer of abstraction useful for many algorithms (though not all).

SlideJ has been developed with the partial support of the EU Marie Curie project [AIDPATH](http://aidpath.eu), grant no. 612471.

*Installation*

To install SlideJ, just put it in the Plugins folder of ImageJ. The only requirements are the Bio-Formats package and fiji-lib.jar (put them in the jar folder of ImageJ, or directly use Fiji.

*Instructions*

The interface of the plugin is a dialog that resembles the one implemented in ImageJ for batch macro execution. The user is allowed to process multiple images present in a folder and store the eventual results in a different folder by setting up paths in the "Input..." and "Output..." fields, respectively. A macro selection button allows the user to choose the file containing the macro to be executed on the tiles.

[center](File_SlideJdialog.png)

Another parameter is aimed at setting the tile size according to user needs (typically depending on maximum memory available - the more the better, up to 16384 or so). In addition to that, another parameter defines the overlap between tiles, identical for X and Y directions (useful for some algorithms).

The last parameter defines whether the tiles are deleted or not after each processing step. If not, they will be available after SlideJ run. Tiles are stored in TIFF format with a file name that reflects their position on the overall digital slide according to the following template:

OriginalFileName.ext\_\_series\_Xorigin\_Yorigin.tif

*Tests*

To test SlideJ, create a folder (e.g., "in") and put digital slides into it; create another folder to storing tiles (e.g., "out"). Choose a macro you want to run on your slides. From the ImageJ Plugins menu, call the plugin, set parameters, and wait.

*License*

SlideJ is licensed under LGPL 3.0.

**Authors**

SlideJ is developed by Giulia Lucrezia Baroni, [Vincenzo Della Mea](http://users.dimi.uniud.it/~vincenzo.dellamea/) and David Pilutti at the [Medical Informatics, Telemedicine and eHealth Lab](http://mitel.dimi.uniud.it/), dept. of Mathematics, Computer Science and Physics, University of Udine, Italy.

If you use it, please cite Slidej as: *Della Mea V, Baroni GL, Pilutti D, Di Loreto C (2017) SlideJ: An ImageJ plugin for automated processing of whole slide images. PLoS ONE 12(7): e0180540.*
