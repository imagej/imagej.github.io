---
title: Warpy Extension
artifact: ch.epfl.biop:bigdataviewer-biop-tools
nav-links: true
toc: true
---

This page documents a way to register whole slide images in Fiji and analyze their result in QuPath. This workflow allows to register slides with transformations which are **more complex than affine transform**, by using the ImgLib2 library, elastix, and BigWarp. Reasonably, if the sample is not too deformed or damaged, registration at the sub-cellular level can be achieved on the whole slide - provided you are not working on serial sections where the cells are not identical between successive sections.

If you are registering serial sections, you can modify the registration parameters in order to have a match at the tissue level instead of at a cellular/subcellular level.

# Videos tutorials

[Playlist](https://www.youtube.com/watch?v=cgRA9NZ-AOo&list=PL2PJpdamvnti8PqyMdcezGLeAtH6LSy69)

# Installation 

## Option 1 - Automated procedure with bash scripts

This is an experimental install procedure which is performing all the steps detailed in the Complete procedure below, but with bash scripts. It is the one explained in the video tutorial:

- If you use windows, install [Git 4 Windows](https://gitforwindows.org/) with the default parameters
- Go to [https://github.com/BIOP/biop-bash-scripts](https://github.com/BIOP/biop-bash-scripts)
- Download the repository as Zip: {% include bc path="Green 'Code' button|Download as Zip"%}
- Unzip it
- On windows:
  - Double click the script `install_warpy.sh`
  - Enter the path `C:/` (recommended)
- On mac:
  - Go to the directory of the zip file
  - Unzip it
  - Go to the directory of the unzipped file
  - Right-click `install_warpy.command` and select Open. By doing this right-click, you can force the execution of the scripts. Do not double-click the `.sh` files since it will open a text editor. Your admin password will be asked. Take care! No `*` character is displayed when you type it.
  - Enter the path (`/Applications/` recommended)

{% include notice icon="warning"
  content="On Mac, your previous QuPath install may be erased, so rename your previous QuPath if you want to keep it" %}

{% include notice icon="warning"
  content="On Mac, If you get an error message, please [grant the terminal application with full disk access](https://osxdaily.com/2018/10/09/fix-operation-not-permitted-terminal-error-macos/)" %}

## Installation - Option 2 - Manual procedure

### ImageJ / Fiji

#### PTBIOP update site

Enable the [PTBIOP](https://imagej.github.io/update-sites/following) update site, then restart Fiji.

#### Elastix  - To enable automated registrations capabilities
- Download the [release 5.0.1 of elastix for your OS](https://github.com/SuperElastix/elastix/releases/tag/5.0.1). This documentation has been tested for elastix 5.0.1.
- Unzip it somewhere convenient ( `C` drive on windows, in `Applications` for Mac )

##### Windows

For windows users, you also need to install [Visual C++ redistributable](https://docs.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist), you'll most probably need `vc_redist.x64.exe`

##### Mac

Fiji will be calling the elastix executables, which are recognized as ‘unknown developers’ by Mac OS. Thus you need to [make security exceptions for both elastix and transformix](https://support.apple.com/en-hk/guide/mac-help/mh40616/mac) to avoid clicking indefinitely on the OS warning messages.

##### Linux (not tested)

Nothing particular should be required for linux system. If it works, please contact the BIOP and let us know!

#### Indicate `elastix` and `transformix` executable location in Fiji

- Execute {% include bc path="Plugins|BIOP|Set and Check Wrappers"%} then indicate the proper location of the executable files 

{% include img name="set and check wrappers" src="/media/plugins/bdv/warpy/warpy-set-chek-wrappers.png" %}

- This message should show up in the ImageJ console : 

`[INFO] Transformix	->	set :-) Elastix	->	set :-)`. You may have an error message for Cellpose, which can be ignored.

Once elastix is installed, you can run [the following script](https://gist.githubusercontent.com/NicoKiaru/b91f9f3f0069b765a49b5d4629a8b1c7/raw/0744676341b16ee4f37ed203130f0e0b761c08c8/TestRegister.groovy) in Fiji to test elastix functionality. Save the file with a `.groovy` extension, open it Fiji, and run it.

### QuPath

* Install the [latest QuPath version (0.4+)](https://qupath.github.io/)
* Install the [QuPath Warpy extension by following its readme](https://github.com/BIOP/qupath-extension-warpy).

# Step by step registration procedure

To follow the WSI registration procedure, a demo dataset, consisting of  a fluorescent image which can be registered to a RGB H-DAB image, can be [downloaded from Zenodo](https://doi.org/10.5281/zenodo.5674521). Only the files with the `.ome.tiff` extensions are necessary.

## Create your QuPath project
[Create first a QuPath project](https://qupath.readthedocs.io/en/latest/docs/tutorials/projects.html) containing all the images that you want to register. 

{% include img name="Import images in QuPath with the Bio-Formats image server" src="/media/plugins/bdv/warpy/warpy-qupath-import-images.png" %}

{% include notice icon="warning"
  content="Only the Bio-Formats image builder is supported on the Fiji side. Make sure to select `Bio-Formats builder` when importing your slides." %}

If your image can't be loaded in QuPath using the `Bio-Formats builder`, you can convert your slides in `ome.tiff` format. Several options are available, for instance by using [Kheops](https://github.com/BIOP/ijp-kheops) (preferred for a better computation of low resolution levels), or [the glencoe ngff converter](https://www.glencoesoftware.com/products/ngff-converter/).


{% include notice icon="warning"
  content="All files need to be properly calibrated (microns, millimeters, etc, but not pixels!). Check on the image tab of QuPath that you have a proper physical unit specified, and not pixels!" %}

If the pixel size is wrong, you need to override it in QuPath and re-save the project before resuming the workflow.

{% include img name="Set image pixel size in QuPath" src="/media/plugins/bdv/warpy/warpy-qupath-set-pixel-size.png" %}

Save your project, and you are done for now on the QuPath side. 

{% include notice icon="info"
  content="You can let QuPath open while performing the registration on Fiji." %}

## Registration in Fiji

### Open your QuPath project
In Fiji, open your QuPath project using 
{% include bc path="Plugins|BigDataViewer-Playground|BDVDataset|Create BDV Dataset [QuPath]"%}. You can also directly type `QuPath` in Fiji's search bar to avoid struggling in Fiji's menu hierarchy.

- Select your QuPath project file (usually named `project.qpproj`).
- Let the default options but make sure to select **MILLIMETER** in the `physical units of the dataset` field

{% include img name="Open QuPath project in Fiji" src="/media/plugins/bdv/warpy/warpy-qupath-open-project.png" %}

{% include notice icon="info"
  content="the `physical units of the dataset` field actually indicates how you want to import your dataset. Bio-Formats takes care of converting the unit of the acquisition into millimeters. This can be achieved only if the image is correctly calibrated initially: bio-formats knows how to converts from microns to millimeters, or from angstrom to millimeters, but it can't know how to transform from pixels to millimeters." %}

{% include notice icon="info"
  content="this WSI registration workflow hides many registration parameters by making use of the proper calibration in physical units, and by assuming it targets a cellular resolution level (do not expect registration precision at 50 nm resolution, unless you manually correct it with BigWarp)." %}

After you have opened your project, a window called `BDV Sources` should pop-up. If you double click on the `Sources` node, you should be able to browse the hierarchy and see the "sources" contained in your QuPath project. Note that the fluorescent channels have been split into separated sources. In the demo file, you get a window like this:

{% include img name="Tree view of the QuPath project" src="/media/plugins/bdv/warpy/warpy-bdvpg-tree-view.png" %}

- `DAB.ome.tiff - DAB.tif-ch0` is the RGB DAB image
- `Fluo.ome.tiff - TileScan_001_Merging001-ch0` is the DAPI fluorescent channel
- `Fluo.ome.tiff - TileScan_001_Merging001-ch1` is the EdU fluorescent channel, which staining should be similar to DAB

For the demo dataset registration, the DAB image is used as the fixed image, and the DAPI channel as the moving image.

{% include notice icon="info"
  content="You can put nicer names to the images in QuPath before opening the project in Fiji." %}

Navigating within BigDataViewer requires a bit of experience. In 2D, the minimal commands to know are written below:

  - **hold and drag right-click**: Pan;  
  - **mouse wheel (or up / down key)**: zoom in and out;
  - **`shift` modifier key**: zoom in or out faster, 
  - **`ctrl` modifier key**: more precise zoom.
  - You'll soon notice that holding **`left-click`** rotates the view. To go back to the default rotation, click **`shift+Z`**

### Creating a Warpy Registration

You can start the registration wizard by clicking 
{% include bc path="Plugins|BigDataViewer-Playground|Sources|Register|QuPath - Create Warpy Registration"%}

First, select the DAB source as the fixed source, and the DAPI channel as the moving source that will be used for the registration as indicated in the image below:

{% include img name="Select fixed and moving images" src="/media/plugins/bdv/warpy/warpy-select-fixed-moving-images.png" %}

Another window shows up:

{% include img name="Warpy wizard options" src="/media/plugins/bdv/warpy/warpy-wizard-options.png" %}

The successive steps (0,1,2,3,4) of registration happens consecutively, all are optional. It is advised to keep the first two boxes checked to remove most of the intitial XYZ offsets which could be stored in the files. The initial offset is usually due to bioformats metadata storing the stage position during acquisition.

{% include notice icon="info"
  content="If you check `Show results of automated registrations`, ImageJ1 images will be created to show the different images which are effectively sent to elastix for automated registration. It's a good way to visualize intermediate registration steps and check what could have gone wrong. However, the processing will be slower because each registration is happening sequentially instead of being parallel." %}

In the rest of this documentation, we assume all registration steps have been checked. The demo dataset requires all these steps, but a small image may be sufficiently well registered with a single affine transform.

The extra parameters located below the chosen steps will be explained when need in the registration steps.

#### Step 1 - Manual rigid registration

Just after clicking `OK`, you will get a BigDataViewer window similar to this one:

{% include img name="Warpy initial display" src="/media/plugins/bdv/warpy/warpy-wizard-initial-display.png" %}

You have three cards on the right part of the window:

1 - `Sources` : this card can be used to the display settings of the sources (min / max  and color for fluorescent images)

After some adjustment, the fluorescence image can be made brighter (max = 50) and the DAB a little bit dimmer (max = 400):

{% include img name="Warpy display after brightness contrast adjustements" src="/media/plugins/bdv/warpy/warpy-wizard-bc-adjusted.png" %}

{% include notice icon="info"
  content="If you register two RGB images, it is important to increase the maximum display values for both images (for instance, from 256 to 512). Otherwise overlayed images will appear fully white." %}

2 - `WSI Registration Wizard` : this card displays the registration step we are in, some navigation hints, and some convenience actions : restoring the initial view, performing auto-scale on images, and showing / hiding the fixed or the moving image.

3 - The third card is specific to the current wizard step.  

In this step, you will need to modify the location of the fluorescent image in order to approximately put it at its proper location. If you zoom in, you will see an obvious shift which can be corrected with a manual rigid registration:

{% include img name="Manual registration, before shift correction" src="/media/plugins/bdv/warpy/warpy-wizard-shift-uncorrected.png" %}

To correct it:
- Click the button `Start manual rigid registration` in the third card.
- Pan the view until the two images are approximately aligned (some rotation and zoom adjustment can also be performed, but a translation is enough in the example):

{% include img name="Manual registration, after shift correction" src="/media/plugins/bdv/warpy/warpy-wizard-shift-corrected.png" %}

- Finally click `Confirm transformation` to go to the next step of the wizard.

{% include notice icon="info"
  content="If you make a mistake while moving the images in the registration, you can click `Cancel manual registration` to restore the initial state." %}

#### Step 2 - Automated affine registration - Define rectangular ROI

{% include img name="ROI definition for registration initial roi" src="/media/plugins/bdv/warpy/warpy-wizard-rectangular-roi-before.png" %}

In this step, you need to define the rectangular region that will be used to do a first coarse affine registration. By default a yellow rectangle surrounding the biggest image is set. However, in the demo case, this rectangle is too large : a large portion of the DAB image is not covered by the fluorescent image. To set a better rectangular ROI, you can directly draw a rectangle in the viewer by dragging the mouse while holding the left button:

{% include img name="ROI definition for registration corrected roi" src="/media/plugins/bdv/warpy/warpy-wizard-rectangular-roi-after.png" %}

If you are not satisfied with the rectangle, you can erase the last one by drawing a new rectangle until you are satisfied. Then go to the next step by clicking `Confirm rectangle`.

{% include notice icon="info"
  content="You can deactivate the rectangle selection mode and toggle the navigation mode by clicking `Enable navigation`. You can also restore the initial rectangle with `Restore initial rectangle` if needed." %}

For the coarse affine registration with elastix, both the fixed and moving images will be resampled over this rectangular selection. Moreover, the resampling will be performed with a pixel size equals to the value specified in the `Pixel size for coarse registration in microns` parameter. By default, this value is set to 10 microns.

{% include notice icon="warning"
  content="The coarse affine registration is not performed directly when clicking the `Confirm rectangle` button. Instead, patches locations for the automated spline registration are set first, before any automated registration is started. This means that, when selecting patches for the spline registration (next step), you should consider the fixed image rather than the moving image, since the moving image will be transformed before each patch is acquired." %}

#### Step 3 - Automated spline registration - Define landmarks

{% include img name="Spline registration, before definition of landmarks" src="/media/plugins/bdv/warpy/warpy-wizard-spline-before.png" %}

Using the mouse left button, position points that will be used to locally correct the warping of the moving slide. You can concentrate the landmark on the regions you are more interested in. Here's an example of landmarks positioning:

{% include img name="Spline registration, after definition of landmarks" src="/media/plugins/bdv/warpy/warpy-wizard-spline-after.png" %}

The number of necessary landmarks is not obvious to know in advance. You need to place them however where common structures are easily identifiable in both the moving and fixed image.

Tips:
- You can move each landmark by dragging its middle point after it has been positioned on the viewer ( the middle point increases in size when it can be dragged )
- You can clear all landmarks and restart positioning landmarks by clicking `Clear points`
- You can restore the navigation mode ( `Enable navigation` ) to zoom on the slide and position better the landmarks. Do not forget to restore the point selection mode ( `Enable point selection` ) if you want to drag patches or create new ones (even when adding the grid).
- It is possible to place patches automatically on a grid  over the rectangular regions defined in the previous step by clicking  `Add landmark grid`. You can set the spacing between the patches to allow for some overlap or on the contrary to let some space between them:

{% include img name="Spline registration, auto landmark placement - no overlap" src="/media/plugins/bdv/warpy/warpy-wizard-spline-ex0.png" %}

{% include img name="Spline registration, auto landmark placement - extended" src="/media/plugins/bdv/warpy/warpy-wizard-spline-ex1.png" %}

{% include img name="Spline registration, auto landmark placement - with overlap" src="/media/plugins/bdv/warpy/warpy-wizard-spline-ex2.png" %}

It is not advised (but possible) to add more than a few hundred landmarks.

{% include notice icon="info"
  content="Overlapping patches is not issue. In fact, after the patch registration, only the location of the patch central point is kept to interpolate the transformation over the whole slide." %}

{% include notice icon="info"
  content="You can change the size of the patches by changing the value `Patch size for precision patch registration` in the initial step of the wizard. Setting it to 200 microns leads to this automated grid placement (with a spacing of 300 microns between patches:" %}

{% include img name="Spline registration, smaller patches" src="/media/plugins/bdv/warpy/warpy-wizard-spline-small-patch.png" %}

It is advised to shift the landmarks where very little structure is present:

{% include img name="Spline registration, smaller patches, better positioned" src="/media/plugins/bdv/warpy/warpy-wizard-spline-small-patch-corrected.png" %}

By default, for each patch, the fixed and moving image is resampled with a pixel size of 1 micron. This value can be modified at the beginning of the wizard if necessary (`Pixel size for precise patch registration in micron`)

Click `confirm points` to start the registration. The ImageJ log window shows the progression of the registration:

It typically takes a minute to register the demo dataset.

{% include img name="Log of warpy registrations" src="/media/plugins/bdv/warpy/warpy-wizard-registration-log.png" %}

#### Step 4 - Manually correct landmarks location with BigWarp

If you have selected `4 - Manual spline registration (BigWarp)`, you will now be able to manually investigate and correct landmarks that have been automatically registered, and also **add new landmarks** to the slides, if you want to adjust more precisely a particular region. The interface used is directly the one of [BigWarp](https://imagej.github.io/plugins/bigwarp), so please check the documentation of BigWarp itself in order to edit landmarks. 

Here's a convenient way to perform this step:

- First, ignore the moving image window and increase the size of the BigWarp fixed image.

{% include img name="Warpy - BigWarp step" src="/media/plugins/bdv/warpy/warpy-wizard-bigwarp-initial.png" %}

- press `F1` for help window
- press `F` to toggle ON and OFF the registered moving image (F stands for fused)
- zoom (mouse wheel) and pan (drag right mouse button) to investigate the registration quality
- press `ctrl+D` to move to the next landmark

{% include notice icon="warning"
  content="The DAB image has its min max value reset to 0 and 65535. Re-set these values to correct ones by using the `Sources` card." %}

To correct a landmark position:
- press `space` to enter the landmark mode
- carefully select and drag a landmark to modify its position. Live visualization of the transformed image helps you positioning it correctly
- press `space` to exit landmark mode
- navigate and repeat for each landmark that needs correction

To add another landmark:
- in landmark mode, press `ctrl + left click` to pin a new landmark on both the moving and fixed image at the current mouse location. It can then be dragged.

You can delete landmarks in the landmark table if necessary:

{% include img name="Warpy - delete BigWarp landmarks" src="/media/plugins/bdv/warpy/warpy-wizard-bigwarp-delete-landmarks.png" %}

Press `Click to finish` to end the wizard and save the transformation to QuPath.

#### Step 5 - Successful registration message

If all went smoothly, you should get this message if the ImageJ log window:

```
Transformation file successfully written to QuPath project: Path\id_moving\transform_moving_fixed.json
```

This means that the result of the registration has been stored as a file into your QuPath project. It can then be used from within QuPath to transfer annotations and or detections from one slide to another one, as explained in the next section.

{% include notice icon="info"
  content="the transformation is stored as a json file in the data entry folder of the fixed moving image. It is named by convention `transform_{i}_{j}.json` where `i` and `j` are the entry ids of the fixed and the the moving image in the QuPath project." %}


# Editing a previous registration

Once the registration has been performed, you may have second thoughts regarding a region which has not been registered well enough. If that's the case, you can go back to Fiji, re-open your QuPath project, and run the command
`QuPath - Edit Warpy Registration`:

{% include img name="Warpy - edit registration window" src="/media/plugins/bdv/warpy/warpy-wizard-edit-registration.png" %}

You will need to select the moving and fixed image (a warning message is displayed if no previous registration is found or if you have switched moving and fixed).

Running this command will launch the BigWarp interface, in which you can modify, remove, or add new landmarks. Click the appropriate button in the BigWarp bigdataviewer window in order to save and override your previous registration (which is lost, unless you save the BigWarp landmark file).

# Analysis in QuPath

From within QuPath, annotations and or detections can be transferred within registered images, one way or another. Indeed, provided transformations are regular enough, they are invertible.

To transfer annotations or detections from one image to another:
- using the procedure of your choice (cell detection plugin, stardist, manual annotation, etc.), create annotations or detections on the image of your choice (for instance the moving image). 
- move to the other registered image (for instance the fixed image).
- you can then execute one of the scripts below {% include bc path="Automate|User scripts...|New Script..."%}

{% include code
     org="BIOP"
     repo="qupath-extension-warpy"
     branch="main"
     path="src/main/resources/scripts/Warpy_transfer_annotations_and_detections_to_current_entry.groovy"
     label="Transfer annotations" %}

{% include code
     org="BIOP"
     repo="qupath-extension-warpy"
     branch="main"
     path="src/main/resources/scripts/Warpy_transfer_TMA_to_current_entry.groovy"
     label="Transfer TMAs" %}

The above scripts consists of two parts:
- `Warpy.getCandidateSourceEntries` looks through all images of the QuPath project if there are transformations files will allow to transfer annotations and detections from one image to the current (target) one, and then performs the transfer.

- transfered annotations/detections does not contain the standard measurements provided by QuPath (fluorescent intensity / DAB value, etc.) In order to add the measurements on the target image, the function `Warpy.addIntensityMeasurements` can be called

# Saving the registered image

You have several options, but please be aware that computing the fully transformed image is not as safe as working with transfered ROIs. The image can be modified significantly.

{% include notice icon="warning"
  content="Computing a fully transformed image, created with ImageCombinerWarpy or with the Fiji Warpy exporter, is a transformation over the pixel contents of the original images! The pixel difference between the original and the transformed image depends on the transformation, the used interpolation as well as the downsampling used in the current viewer. This must be taken into account in all analysis steps performed on such transformed images." %}

## With Image Combiner Warpy

This requires using QuPath and the Image Combiner capabilities. For more informations, go to
[export combined image to OME-TIFF.](/plugins/bdv/warpy/warpy-image-combiner-additional-info#project-entry--image-file)

## With Warpy in Fiji

In Fiji, you can type ‘export warpy’ into Fiji’s search bar and you should get a window like this:

{% include img name="Warpy - export choose images" src="/media/plugins/bdv/warpy/warpy-fiji-export-window0.png" %}

After clicking ok, you’ll get a second window with writing options:

{% include img name="Warpy - export options" src="/media/plugins/bdv/warpy/warpy-fiji-export-window1.png" %}

And if everything’s right, you’ll get a progress bar during image writing (click on the bottom right square of Fiji’s main bar):

{% include img name="Warpy - export progress bar" src="/media/plugins/bdv/warpy/warpy-fiji-export-progress.png" %}





