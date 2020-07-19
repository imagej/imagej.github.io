{{ComponentStats:sc.fiji:VIB_}}The VIB Protocol is designed for aligning 3D image stacks. The images we used are confocal images of adult fly brains, but basically the VIB protocol can be used for any 3D images.

== Workflow ==

* Load the input images. If they consist of several channels, the channels are splitted.
* Label the reference channel
* Resize images and labels
* Calculate the centers of gravity and use them to calculate a rough alignment
* Register each labelled region indivudually, again rigidly.
* Interpolate the displacement field between labelled regions. 

The output of the VIB Protocol is written to a user-specified folder. A description of how to use this plugin can found below, while a more detailed description about how the VIB Protocol works can be found in this [http://132.187.25.13/home/imagej/fens.pdf presentation], which was shown at the FENS 2008 in Geneve. There exists also a [http://132.187.25.13/home/imagej/fens.avi movie] which demonstrates nicely the alignment of two brains. 

== Documentation ==

The VIB Protocol starts with the following dialog:

[[Image:VIB_Protocol_1.png|center]]

A configuration file stores all the settings for running the VIB Protocol on a particular data set. It is saved in the output directory. If one wants to run the algorithm a second time, it is possible to load (and modify) the previous configuration. If you run this for the first time, just leave the text field blanc and click OK.

After that, a second dialog appears, which asks the user for all the necessary input:

[[Image:VIB_Protocol_2.png|center]]

The different fields have the following meaning:

;Files
:Use the buttons "Add to files" and "Delete from files" to add here the input images.

;Working directory
:All the output of the VIB Protocol goes into this folder.

;Template
:Choose one of the images in the "Files" list as a template (reference) brain (by selecting it in the list and clicking "Use as template"). Alternatively, you can choose an external reference by typing the path to the file you want to use.

;No of channels
:The number of channels contained in the input files.

;No of reference channel
:The number of the reference channel. The reference channel will be used for labelling.

;Resampling factor
:In order to speed up execution time, it is a good idea to scale the images down. Selecting here '2' for example means that a 1024x1024x256 images will be downsampled to 256x256x64.

Clicking OK will finally start the VIB Protocol. At this point, the above mentioned configuration file is created and saved, which is shown by:

[[Image:VIB_Protocol_3.png|center]]

Normally, the Segmentation Editor opens during the software execution and asks the user to label the brains. This step is omitted if there exists already a folder called 'labels' in the output directory and if this folder contains for each image the corresponding labels image. After that, no more user interaction is required, and the software finishes after some time. All the results can be found in the output directory. The structure of this directory is as follows:

[[Image:VIB_Protocol_4.png|center]]


[[Category:Plugins]][[Category:Segmentation]]
