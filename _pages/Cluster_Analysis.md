{{Notice | This Wiki-Page is still under construction.}}

= Introduction =

Fiji-Plugin to segment and quantify confocal images.

== Install Plugin in Fiji==
The Cluster Analysis Plugin is integrated in the built-in Updater Site of Imagej and regular updates are available through it.

Go directly on your local Fiji-application and click on Update > Manage update sites > Add my site and type in the ImageJ Wiki account dcolam. After that all scripts and dependencies should be installed in the right place and you only need to restart Fiji.

== Prerequisites == 
Only thing one should follow, is the right organisation of the folder where you keep the images to be analyzed. In particular the titles should all have the same structure, meaning all useful information should be separated by a common delimiter (e.g. an underscore) that you need to specify and all images should have the same number of information (XX_YY_ZZ.tif for example, another title should accordingly look something like this AA_BB_CC.tif). The script throw an error, if the titles don't have the same length.
The script will initiate a database extracting informations from the title that you can specify and describe later on.

https://raw.githubusercontent.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Dialog5.png

If you want to exclude a particular information, don't type anything into the field

==  Running the Plugin == 
After successfull installation, you will find in Plugins > Cluster Analysis three sections, namely the script starter, the Manual and Helper which redirects you to this github-repository and a ini.cfg-file loader which will allow you to feed in older ini.cfg-files from other experiments. Load an ini.file from a previous experiment before starting the script and then run the Cluster Analysis script with the new parameters.

The general script workflow consists of several steps:
* Configuration of Parameters for the whole experiment
* Testing your parameters on a randomly drawn image from your dataset (repeat if necessary)
* Either reconfigure the parameters or start the experiment
* In experimental mode, all images will be analyzed in the background

== Parameter Configuration == 
After clicking on Cluster Analysis, a dialog should appear, where you need to specify the input folder path to your images. In addition, you can run the script in headless-mode, meaning that the current ini.cfg with all parameters from a previous run will be read directly and run directly in experimental mode. You also have the possibility to click the "Set Measurements"-option to choose which type of measurements such as Area, Mean Grey Value, Integrated Intensity or Perimeter to describe the particles in your images. Additionally, set a name for the current run. At the end, all parameters stored in that run will be stored in a configuration-file with the experiment name. If you re-run an analysis with the same name, your configuration-file will be overwritten. 

In the next dialog, you will be prompted to define several details for every channel of your images. If your images don't have 4 channels, just ignore the ones you don't need. You can also name every channel individually and specify whether you want to perform a Particle Analysis. Also make sure to click on the Test parameter button to test whether all parameters are set up correctly. When the Z-Stack option is omitted, the analysis will be run on all slices of your images. Specify also the delimiter used in your titles, so that information can be extracted from the image titles and be used in your database.

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Dialog1.png?raw=True)

You can perform a background subtraction using a sliding paraboloid with a specific rolling ball radius. Furthermore, you can filter a channel using Gaussian Blurring by a defined sigma (radius). It is also possible to adjust Brightness and Contrast either automatically or manually, even though neither are recommended nor useful. Both blurring radius and rolling ball are dependent on the resolution of your images. Finding the right parameters depend strongly on what information you want to extract from one channel. If you need to detect small particles, a strong blur and background subtraction can make the particles weaker and detection almost impossible. In general, the bigger the blurring radius, the bigger the blur. Conversly, the smaller the rolling ball, the higher the background that gets subtracted.

After setting up the first dialog, you will need to specify the parameters to perform the quantifications such as size or circularity range, as well as an automated thresholding method for every channel you want to perform a Particle Analysis on. You can choose and test more than one method by writing them out on the text field below the scroll down button, separated by just a single space. Click on the Watershed option to perform a watershed algorithm (https://en.wikipedia.org/wiki/Watershed_(image_processing)) for separating close objects based on their shape.

You can also perform a Colocalisation Analysis with other channels, for example, if you want to count the number of objects inside or outside the nuclei. Just tick the corresponding channel you want to perform the colocalisation with. The colocalisation algorithm works by using the identified objects during the particle analysis as a mask for another channel and perform a second particle analysis on the chosen channels only within the primary mask. You can also enlarge the mask created from the primary channel by a certain amount in microns (if your images are calibrated, otherwise pixels).

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Dialog2.png?raw=True)

After defining parameters for all corresponding channels, you can either choose to manually segment regions of interest in your pictures (you will need to sit in front of the screen during the whole run) or define an automated segmentation algorithm which is based on an additional Particle Analysis combining several channels together. By applying a high Gaussian Blur one can filter for dense structures in your images such as nuclei dense brain regions (e.g. pyramidal cell layer in the hippocampus) or using a morphological staining such as a dendritic marker (such as MAP2). The automated segmentation algorithm will always also include the quantification of the whole image, even if the algorithm fails to detect an appropriate mask. Play around with the parameters to find the suitable combination for your purpose. If you only want to select the whole image, just set every numerical option to 0.

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Dialog4.png?raw=True)

One can also include a step-wise segment analysis from your primary segmentation outcome with a defined step range in microns. This can be particularly useful when you want to analyse segments of synaptic rich layers such as the Stratum Radiatum of the hippocampus.

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Denditic_Segm_Analysis.png?raw=True)

The script will choose a random image after setting all parameters and show you all steps of the analysis to check whether the parameters meet all criterias. When you are satisfied with the outcome, press on Start Experiment or try another image or define all parameters again.The old parameters will be saved in the ini.cfg-file and remembered for when you want to re-run the script.

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Result1.png?raw=True)

Example of successful segmentation of the pyramidal cell layer (as red line) of the CA1 in the hippocampus and the quantificitation of a certain mRNA within the segmentation (thresholded particles in red, found particles segmented in green).

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Coloc_Example.png?raw=True)

Example of a GFP-filled neuron stained for a post- and presynaptic marker. GFP was used as a mask to find post- and presynaptic components individually. Colocalisation between post- presynapse was achieved by superimposing one channel to the other and counting inside the superimposed channel (all bounded within the GFP-mask). By rotating the superimposed channel by 90°, one can estimate the random colocalisation between the two channels (Done automatically when performing colocalisation analysis)

In experiment modus, the script will run all preprocessing and measurements steps in the background. This will make the analysis much faster. After the analysis is done, you will find in your original folder a new folder called Particle Analysis that includes a folder containing the saved region of interest (.roi files) to check on your segmentation outcome, as well as .tif file versions of your images after preprocessing. In the Output Table folder, you will find a SQlite database called Output.db with all the tables and measurements stored and an ini.cfg file, that contains the defined parameters of your experiment.

You will find four different tables in the database:
* Particle_Analysis_Table containing information about every measurement performed
* PA_Measurement_Tables containing information such as area and mean intensity about every single particle identified
* Colocalisation_Analysis_Table containing information about every measurement performed between two channels
* Coloc_Measurement_Tables containing information such as area and mean intensity about every single particle identified

These tables are also available as .csv-tables in the Output Table folder.

![Alt Text](https://github.com/dcolam/Cluster-Analysis-Plugin/blob/master/ExampleImage/Database.png?raw=True "SQLite Browser")

It is recommended to open your Output.db file with a a DB-Browser such as DB-Browser for Sqlite (http://sqlitebrowser.org/) for a quick look, but to import your datasets using Matlab, R, Python or another popular programming language to properly analyze your data. The usual routine consists of creating a connection to the database and defining a query containing conditional-statements to correctly retrieve the corresponding measurements.

=  ShinyApp to Analyze and Plot Results from the SQLite-Database (In Progress) =

Using the ShinyApp-library within the R-framework, we are currently working on a solution to allow people to analyze and plot the results given by the Cluster Analysis Plugin in form of the database without any need of scripting at all. The work is still in progress and should be soon available. 

= Headless-mode =

Thanks to the headless-mode functionality of ImageJ2 and the Cluster Analysis Plugin, the program is able to run in a desktop-free environment such as an external server (preinstalled with FIJI). Load a previously tested ini.cfg-file with the right parameters using following command in a bash-shell terminal (in a Linux-server):

<code>
pathToFiji/Fiji.app/ImageJ-linux64 --ij2 --headless --run pathToPluginFolder/Cluster_Analysis/Load_Custom_ini_File.py 'inifile="pathToIniFile/ini.cfg"'
</code>

Then start running the Cluster Analysis in a similar manner by using following command:

<code>
pathToFiji/Fiji.app/ImageJ-linux64 --ij2 --headless --run pathToPluginFolder/Cluster_Analysis/Cluster_Analysis_BETA_v2.py 'expath="pathToInputFolder/",headless="True",measure="False"'
</code>

Make sure all paths are correct and pointing to the right scripts and folders. The Output-folder with the spreadsheets and database can be found as usual in "pathToInputFolder/Particle_Analysis/Output_Table"

For more information, don't hesitate to contact me. Reporting bugs and issues in the issue-section of this repository is highly appreciated.
