{{Infobox
| software               = Fiji
| name                   = Manual drift correction
| author                 = [[User:Benoit|Benoit Lombardot]]
| maintainer             = [[User:Benoit|Benoit Lombardot]]
| released               = 22 March 2016
| filename               = [[File:Manual Drift Correction-1.0.0.jar.zip]]
| source                 = [https://github.com/mpicbg-scicomp/Manual_drift_correction github]
| category               = [[:Category:Plugins|Plugins]], [[:Category:Registration|Registration]]
}}

[[Category:Plugins]]
[[Category:Registration]]

==Goal of the plugin==
Manual Drift Correction plugin allows to correct drift in an image sequence by using a few landmarks (Rois) gathered in the Roi Manager. The main interest of the plugin is that it avoid tedious annotation of the image by interpolating between key landmarks. Thus rather than providing input for each image of the sequence, the user only need to provide landmark when significant changes occure.

==Usage==

===Installation===

To get started with the plugin first  download it ([[File:Manual Drift Correction-1.0.0.jar.zip]]), unzip it and install it (Fiji menu Plugins>Install...). Alternatively you can manually copy the unzipped file in <Fiji folder>/plugins.Once the file is installed, restart Fiji. A new entry will be available in the menu Plugins>Registration>Manual drift correction meaning that the plugin was properly installed.

===Tutorial===

To perform Manual drift correction:

# Open Fiji and load the sequence to correct
# Browsing through the image of the sequence, select some landmarks that will be visible throughout the time sequence.
# Starting from the first timesteps annotate these landmark position with a ROI (point, line or polyline) and add them to the Roi Manager (this can be done by pressing the "t" on your keyboard).
# Going further in time, repeat the previous step annotating the same landmark in the same order. Reapeat the operation till you covered the whole sequence.
# If your image is an hyperstack check that the time dimension is properly set in image properties (menu Image>Properties)
# Set the time slider to the reference image (all other image of the stack will be registered to this one)
# Click the menu Plugins>Registration>Manual drift correction. The registered stack will open in the Fiji UI.

=== Limitations ===

The plugin can process stack and hyperstack. In the later case the registration is done along the time dimension. It means that z slices or channel at the same time step in the sequence will be transformed in the same way.

Landmarks can be inputed with  Point, Line or Polyline Rois. If you use multiple landmarks at each time step they should be provided in the same order for each time step.

The plugin also expects Landmarks to be provided to the Roi Manager in chronological order.

Currently the plugin corrects drift only with 2D translation (but that could be updated in the future to 3D and other kind of global transformation)

==Processing description==

The plugin is relying on the [http://javadoc.imagej.net/MPI-CBG/ mpicbg library] that is part of Fiji distribution. This library is used for creating transformation from the landmarks and performing the actual transformation of the image.

The processing is successively:
* Grabbing the last selected image in Fiji UI, the current time of the sequence (i.e. visible in the viewer is used to define the reference image)
* Collecting landmarks from the ROI manager,
* Doing a linear interpolation of their 2D positions to create landmark where not provided. At the begining (end) of the sequence if no landmark is provdided and no interpolation can be done the postion of the first (last) provided landmark is used.
* Then for each slice in the sequence:
** A global transformation is created from current image landmarks and the reference image landmarks.
** The image is then transformed to the reference image
* Finally the registered sequence is displayed in Fiji UI.

==Development plan==

This implementation could be improved. Here are a few feature that could be added:
* Decouple UI and and actual registration pipeline. the current version is written in script style mixing UI and processing.
* Allow to choose the interpolation between landmark.
* Allow to choose the transformation model (as provided by MPI-CBG library).
* Output transformations for analysis purpose.
* Allow to choose the dimension along which to register (Z, time or channel).
