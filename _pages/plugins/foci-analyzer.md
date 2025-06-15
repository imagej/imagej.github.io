---
title: Foci Analyzer
categories: [Analysis]
icon: /media/icons/Foci-Analyzer-icon.png
source-url: "https://github.com/BioImaging-NKI/Foci-analyzer"
update-site: "foci-analyzer"
release-version: v1.8
team-founders: ['@BioImaging-NKI', '@bvandenbroek']
team-maintainers: ['@BioImaging-NKI', '@bvandenbroek']
---
{%- assign github            = page.github            -%}
{%- assign release-version   = page.release-version   -%} {%- comment -%} Most recent component release version                       {%- endcomment -%}
{%- assign release-date      = page.release-date      -%} {%- comment -%} Most recent component release date                          {%- endcomment -%}
{%- assign dev-status        = page.dev-status        -%} {%- comment -%} Unstable, Active, Stable, or Obsolete                       {%- endcomment -%}
{%- unless team-maintainers  -%} {%- assign team-maintainers  = page.team-maintainer  -%} {%- endunless -%}

Foci Analyzer is a comprehensive Fiji macro to detect, analyze and visualize nuclear/cellular foci in 2D/3D fluorescence microscopy images of cells and tissue.

Foci are efficiently and reliably detected in images from different imaging modalities (confocal, widefield), with a wide range of resolutions.
The output data include detailed tables with foci statistics and overlays of segmented cells with foci on the original image. Colocalization analysis is performed on images with two foci channels, and shown in insightful overlap maps.

![image](https://github.com/user-attachments/assets/749fc433-576b-49d2-8fe7-2b3b049ee4d9)

Author: Bram van den Broek, The Netherlands Cancer Institute, Amsterdam. For questions please use the [image.sc forum](https://forum.image.sc/) with tag @bramvdbroek.

## Workflow summary

1. Nuclei are segmented using the pre-trained deep learning network [StarDist](https://imagej.net/plugins/stardist) (2D / 2D projection). Alternatively, the deep learning network [Cellpose](https://github.com/MouseLand/cellpose) can be used to segment nuclei or whole cells (2D, 2.5D or 3D), thanks to the [Cellpose wrapper for Fiji](https://github.com/BIOP/ijl-utilities-wrappers) by BIOP. Alternatively, classic thresholding + watershedding can be used (though no parameters can be changed). 

2. Foci are detected in each nucleus in 2D or 3D. After Difference of Gaussians background subtraction, local maxima are detected and used as seeds for [MorpholibJ](https://imagej.net/plugins/morpholibj)'s [marker-controlled watershed](https://imagej.net/plugins/marker-controlled-watershed) (executed on the GPU using [CLIJ2/CLIJx](https://clij.github.io/)). Additionally, AreaMaxima local maxima detection can be used as detection method.
Thresholds are automatically calculated per image as 3 times the median of the standard deviations of the (outlier-removed) foci signal in the nuclei, and can be adapted using the threshold bias sliders.

3. Foci are quantified in a single channel A, or in two channels A and B.
For each nucleus a number of metrics are reported in a table: foci count, as well as mean/median values for foci intensity, area/volume, and whole nucleus intensity.
If two channels are selected, foci colocalization between channels is automatically calculated.
The table is saved as a `.tsv` file, which can be easily opened in other programs (e.g. Excel).

4. Segmented nuclei and foci are visualized as overlays on the original images for easy inspection. If desired, foci detection settings (threshold bias, min/max size) can be adapted before processing all input images. A colocalization map is also created when two channels are measured.

## Installation / Requirements
______
**IMPORTANT NOTE**: Currently StarDist does not function with Fiji-Latest, due to a [TensorFlow issue](https://github.com/fiji/fiji/issues/393). For the time being, please use Fiji-Stable: select the 'Stable' distribution next to the large green download button on [https://fiji.sc/](https://fiji.sc/)).
______

[Activate](https://imagej.net/update-sites/following) the following Fiji update sites (in the menu bar, via Help -> Update...):
- Foci-Analyzer
- 3D ImageJ Suite
- CLIJ
- CLIJ2
- CLIJx-assistent
- CLIJx-assistent-extensions
- CSBDeep
- IJPB-plugins
- StarDist
- (TensorFlow) Due to a recent Fiji update, StarDist [may require the TensorFlow Update Site](https://forum.image.sc/t/stardist-error-since-update/107729) to function properly.

Run Foci Analyzer from the Fiji menu: `Plugins -> Foci Analyzer -> Foci Analyzer`.
`Combine result files` can be used to pool output `.tsv` files into a single file/table.

In case you also want to use Cellpose segmentation you additionally need:
- A working Cellpose (2.0 or higher) environment in Python (conda or venv)
- Activated PTBIOP update site, with proper settings. See [here](https://github.com/BIOP/ijl-utilities-wrappers/blob/master/README.md#cellpose) for more details.


## Usage manual

The macro starts with a large dialog containing all options and parameters (click to enlarge):
The dialog has several (color-coded) sections that are discussed below. All settings in this dialog will be remembered after you click `OK`.

<img src="https://github.com/user-attachments/assets/438a42c7-90d9-454d-b4e6-a15809e94f75" width="600">

### File settings

- _Input files_ : Here you can specify which files to analyze. Simply add them to the list using the buttons, or directly drag&drop from a file explorer window. Input images should be multichannel images. (RGB images will be converted to composite multichannel image with channels 1:Red, 2:Green; 3:Blue.) Each file should contain at least a channel with nuclei staining, and a channel with foci (though technically they can be the same). The file format can e.g. be `.tiff`, or any proprietary microscopy file format that Fiji (i.e. Bio-Formats) can open, including multiple images packed into a single file as series.

- _Output folder_ : the folder where all the analyzed images and result output files will be written.

### Image settings

- _Load settings from previously analyzed image?_ : When checked, a separate dialog will popup where an output `.zip` file can be selected (overlay or colocalization map). All settings are loaded from the metadata in the saved image. The script parameter entries in this large dialog are ignored.

- _Nuclei channel_ : The image channel that contains the nuclei. For StarDist nuclei segmentation is performed using this channel, which always happens in 2D (in the case of 3D images on a maximum intensity projection). For Cellpose, there are two possibilities, depending on the value of _Cytoplasm/membrane channel_ below.

- _Cytoplasm/membrane channel_ : The image channel that contains cytoplasm or membrane. If set to `-1`, segmentation is performed on the nucleus channel alone. If _not_ `-1` and Cellpose is chosen as [segmentation method](https://imagej.net/plugins/foci-analyzer#nucleicell-segmentation-settings), segmentation is performed on this channel. In this case the nuclei channel is the 'additional helper channel'. If _not_ set to `-1` and StarDist is chosen, this channel not used in the segmentation, but instead just displayed in the overlay image. (default: -1) 

- _Foci channel A_ : the first foci channel (default: 2)

- _Foci channel B_ : the second foci channel (default: 3)

- _Also detect foci in Channel B and perform colocalization?_ : If checked, foci in both channels *A* and *B* will be analyzed, followed by a simple colocalization analysis. (default: checked)

- _2D/3D foci detection_ : This parameter determines how foci in 3D images should be analyzed. For 2D input images this setting is ignored. The options are:
  - *Detect foci in 3D (or 2D when N/A)* (default) performs foci analysis using 3D filters and 3D marker-controlled watershed functions. Connected foci in consecutive slices are counted once.
  - *Detect foci on the Maximum Intensity Projection* performs 2D foci analysis on the MIP projection.
  - *Detect foci on a Extended Depth of Focus Projection* performs 2D foci analysis on an EDF projection.
  - *Detect foci on the Standard Deviation Projection* performs 2D foci analysis on the STDEV projection.
  - *Detect foci on the Summed Intensity Projection* performs 2D foci analysis on the SUM projection.
  - *Use quasi-2D foci detection (detect foci separately in every Z-slice)* analyzes every z-slice in a 3D image as a separate 2D image. This setting is useful in cases where the z-spacing is very large and each focus is visible in only one z-slice. Hence, connected foci in consecutive slices will be counted multiple times.
  - *Process a single z-slice only (specify below which slice)* allows the user to analyze foci only in a particular z-slice.

  Often analysis on 2D projections provides satisfactory results that are easier visualized/inspected compared to true 3D analysis, and much faster processing, with minimal sacrifices (e.g. foci intensities).

- _[single z-slice foci detection only] Slice nr_ : the single z-slice used for the option above. For any other choice this parameter is ignored.

- _Remove image borders (pixels)_ : Possibility to remove edges from the image. This can in particular be useful when the image edges have very different intensities, causing incorrect automatic nuclei segmentation.  (default: 0)

- _Image XY binning before analysis_ : Optional pixel binning in case the resolution is very high and the foci consist of many pixels. A value of 2 means: 2x2 pixels will be binned into 1 pixel. This reduces noise in the image and speeds up analysis. (default: 1)

### Nuclei/cell segmentation settings

- _Nuclei/cell segmentation method_ :
  - *Stardist nuclei segmentation 2D (or on 2D projection)* (default) uses the pretrained convolutional neural network [StarDist](https://github.com/stardist/stardist#readme) to recognize cell nuclei in fluoresence microscopy images. In general this method works very well on a large variety of samples.
  - *Cellpose segmentation 2D (or on 2D projection)* uses the deep learning network [Cellpose](https://github.com/MouseLand/cellpose#--cellpose--) to recognize whole cells or nuclei. Use this option if you want to measure foci in entire cells, or if you prefer Cellpose nuclei segmentation over StarDist. Cellpose requires additional installations (see [Installation / Requirements](https://imagej.net/plugins/foci-analyzer#installation--requirements)).
  - *Cellpose segmentation 3D*: If this option is chosen a new dialog pops up with extra settings. These are the most important parameters for 3D segmentation. More parameters can be added in the 'Additional Cellpose parameters' field. The `Help` button takes you to the [Cellpose CLI](https://cellpose.readthedocs.io/en/latest/cli.html) with explanations of all parameters.
![image](https://github.com/user-attachments/assets/46199403-13c0-4082-9767-af73519effcf)

  - *Classic nuclei segmentation* allows the user to segment nuclei using manual/automatic thresholding is provided for legacy reasons. The method is almost always outperformed by the two other methods.
  - *Load ROIs from file*: ImageJ ROI `.zip` files can be loaded instead of performing segmentation. This option is used in the (near future) QuPath-Fiji workflow. ROI files should have the same name as the input images without extensions, followed by '_ROIs.zip'.
  - *Load label images* allows loading a labelmap, if the segmentation has been done by external programs, or to quickly re-run files with the same segmentation. Label image files should be present in another folder and have the exact same name as the input images.
- _Stardist nuclei rescaling factor [1-n], 0 for automatic, 1 for no rescaling_ : Stardist is trained on medium resolution images, and generally performs well on images with pixel sizes around 0.2-0.5 µm. For images with much smaller pixel size StarDist tends to 'oversegment' nuclei. Set to `0` for automatic rescaling the nuclei to an optimal pixel size of 0.25 µm, or put any other number for manual control of the rescaling. N.B. If the pixel unit is not µm, no rescaling is performed.
This option only affects the nuclei segmentation; it is different from the previously mentioned 'XY binning' parameter, which also changes the pixel size of the foci channels. (default: 0)

- _Probability/flow threshold [0.0-1.0] (StarDist/Cellpose)_ : Lower values will accept more nuclei/cells; higher values will be more stringent. For Cellpose this is actually the [_flow_threshold_](https://cellpose.readthedocs.io/en/latest/settings.html#flow-threshold) parameter. (Cellpose's [Cellprob parameter](https://cellpose.readthedocs.io/en/latest/settings.html#cellprob-threshold) has less influence and is always set to 0.) (default: 0.5)

- _Cellpose cell diameter (pixels), 0 for automatic_ : Estimated diameter of the cells, in pixels. Setting this parameter to 0 will trigger Cellpose to estimate it. Please check the Fiji console for the resulting estimate.

- _Cellpose model_ : The [model](https://cellpose.readthedocs.io/en/v3.1.1.1/models.html#models) (built-in or custom) used for segmentation. Tested up to Cellpose 3.1 (cpsam may just work though).

- _Remove nuclei with diameter smaller than (units)_ : Objects smaller than circles having an area corresponding to this diameter will be removed. 'Units' depends on the image, and will almost always be 'µm', or otherwise 'pixels' in case the pxiel calibration values are missing. (default: 4)

- _Remove nuclei with diameter larger than (units)_ : Likewise, but for large objects. (default: 50)

- _Exclude nuclei on image edges_ : When checked, nuclei that touch the image edge will not be analyzed. (default: checked).

- _Manual nuclei removal_ : allows the user to erase ill-segmented nuclei before analysis. (default: No thanks) Options:
  - *No thanks* means no manual nuclei editing
  - *Manually remove nuclei* : Remove nuclei by leftclicking them in the image with the mouse. Editings will be saved to a small text file in the output folder.
  - *Load previously saved removals (from output folder)* : If you have edited the segmented nuclei on this image before, it will load the previous nuclei removals from the file in the specified output folder. (Hence, if you change the output folder parameter this option will not work.)
 
### Foci detection settings

- _Preview foci detection (for parameters fine-tuning)?_ : Checking this will allow the user to adapt the foci detection settings on a preview analysis before quantifying. (default: checked)

- _Foci size channel A/B (after XY binning)_ : choices between *tiny*, *small*, *average*, *large*, *huge*, and *other*. This parameter controls several foci image filtering steps and steers the macro towards detecting smaller or larger foci. (default: average).

- _Foci detection method_ :
  - *Marker-controlled watershed* uses MorphoLibJ's [marker-controlled watershed](https://imagej.net/plugins/marker-controlled-watershed) with local maxima as seeds to segment foci
  - *AreaMaximum detection* tends to detect only the peaks of the foci. Can be tried when the other option doesn't provide satisfactory results. This options requires the SCF MPI CBG Fiji Update Site to be installed.

- _Foci intensity threshold bias channel A/B_ : The macro will automatically estimate the intensity threshold for foci detection (after difference-of-Gaussians background subtraction). This default threshold is set at 3 times the median standard deviation of the nuclear background signal in all nuclei in the image. The user can bias this threshold with the slider to lower values (accepting more low intensity foci) or higher values (gearing towards high intensity foci). The bias slider couples exponentially to the used threshold value: threshold = estimated_threshold * e<sup>bias</sup>. 
Since the minimum and maximum slider values are (-2.5, 2.5) the threshold can be set to anywhere between 0.2 and 36 times the standard deviation of the nuclear background signal. (default: 0)

- _Minimum foci size (pixels/voxels)_ : Foci occupying an area/volume smaller than this value (in pixel/voxels) will be deleted. Note that for the marker-controlled watershed detection method the minimum foci size is `5 pixels` for 2D images and `7 voxels` for 3D images. Hence, setting sizes smaller than this will not change the number of detected foci.

- _Maximum foci size (pixels/voxels)_ : The upper limit for the foci size, in pixels/voxels.

- _Max distance of foci outside nuclei/cells (units); -1 for full image_ : This controls how far (in units (=microns)) outside the cell/nucleus segmentation foci should be still be counted. (default: 0)

- _Minimum overlap of foci to colocalize_ : Foci in channel A and B will be counted as colocalizing *only if they overlap with at least this area/volume (in pixels/voxels).

### Visualization options

- _Nuclei/cell overlay choice_ : Select which numbers are added to the overlay: nucleus/cell ID, foci count, both or none.

- _Nuclei/cell label color_ : The color of the nucleus/cell ID text overlay.

- _Foci count label color_ : The color of the foci count text overlay.

- _Nuclei/cell label font size_ : The size of the nuclei/cell ID text overlay.

- _Nuclei/cell outline brightness_ : The brightness of the nuclei outlines overlay: bright or dim.

- _Nuclei/cell outline color_ : The color of the nuclei outlines overlay.

- _Debug mode (show intermediate images)_ : Used for development and bug fixing: checking this option will trigger displaying many intermediate results during the processing. It will also slow down the analysis.


## Foci detection optimization 
When the option _Preview foci detection (for parameters fine-tuning)?_ is checked, a preview image of the detected foci will be shown during processing. A dialog appears where foci detection parameters can be adjusted (see [foci detection settings](https://imagej.net/plugins/foci-analyzer#foci-detection-settings) for explanations):

![image](https://github.com/user-attachments/assets/7ddc5514-13c5-41cc-9ca1-80a2ce457328)

Under `Action` there are four options:
- *Recalculate with these settings*: re-run the foci detection with the current parameters. The segmentation remains the same. (default)
- *Done optimizing \ Process and optimize the next image*: Finishes the analysis for the current image and shows the dialog again for the next image.
- *Done optimizing \ Process all other images with these settings (calculate thresholds for each image)*: Performs the analysis on all subsequent images with the current settings. Foci threshold values are estimated and calculated for every image. The absolute threshold value depends on the image characteristics (see [foci detection settings](https://imagej.net/plugins/foci-analyzer#foci-detection-settings)) and can vary (slightly) from image to image. 
- *Done optimizing \ Process all other images with these settings (fix current threshold levels)*: Performs the analysis on all subsequent images with the current settings. The calculated absolute foci threshold value for _this_ image is used for all other images. This setting is useful when processing separate tiles of a larger image.

After changing the settings, clicking `OK` will detect the foci on the same nuclei with the updated parameters and redisplay them in the preview image. Channel display settings and zoom are remembered in between optimization steps.
The preview image shows an ImageJ hyperstack that, besides the z-slices of the 3D image (if applicable), contains two *frames* representing the foci channels A and B (if applicable), and four *channels*:
1. The nuclei staining channel (azure blue)
2. The original foci data (green)
3. The detected foci (magenta)
4. The centroids of the detected foci (white)

![image](https://github.com/user-attachments/assets/c7670dd1-89ea-4b23-92df-9b6d7dad4dbb)

The image below shows a montage layout of such a hyperstack, with vertically the '*frames*' (foci channels A and B - here 2 and 3), and horizontally the '*channels*' (as described above):
![image](https://user-images.githubusercontent.com/33119248/206936107-175705d8-61b0-45df-8872-e279052ae035.png)

By changing the displayed channels (*Shift-Z*), adjusting brightness&contrast (*Shift-C*) of the channels and zooming in ('+' and '-' keys), the user can inspect the foci detections for both foci channels, adjust the detection parameters if desired and rerun the foci detection step. In particular, unchecking channel 1 (nuclei), and then alternating the displaying of channel 3 (detected foci) is most helpful.

![image](https://user-images.githubusercontent.com/33119248/206996059-d86441ce-795c-4c43-a9e7-c3181f0bdd71.png)
![foci_03_crop_RGB_optimization_crop](https://user-images.githubusercontent.com/33119248/206938037-fd79a4eb-3b14-42d5-8ddc-8aa39794a727.gif)
![channels_tool](https://user-images.githubusercontent.com/33119248/206938473-f8f575fc-26b9-4071-abbe-77a33e86e156.gif)



## Time-lapse images

When a Time-lapse image is detected, individual frames are split and saved to disk. The script then analyzes these single frame images one by one and saves the results.
Currently, the time-lapse image is not being rebuilt. This can be done by running `Concatenate timelapse with overlays`, in the Foci-Analyzer Fiji submenu (`Plugins` -> `Foci-Analyzer`).

After [concatenating the result files](https://imagej.net/plugins/foci-analyzer#handling-results) for all frames it is possible to run `Plot foci timetraces` from the Foci-Analyzer submenu. This will read data from the `Results` table and generate a table containing the foci count per cell per time frame, as well as a plot. N.B. This feature is experimental and under development.

![image](https://github.com/user-attachments/assets/1132af51-5c21-4cc3-8b20-c48961cd0711)


## Output

### Files

The following output tables are displayed after analysis of each image/frame. These are saved in the designated output folder:

1. A `.zip` file ending with `overlay_ch...zip`, containing the abovementioned channels, with segmented cells/nuclei outlines, as well as nucleus ID and/or foci count as text overlay. This image also contains (almost) all analysis settings as metadata (`Image` -> `Show Info... in Fiji), which is useful for documentation/reproducibility purposes, as well as re-using the same settings on another image (by [loading them](https://imagej.net/plugins/foci-analyzer#output:~:text=Load%20settings%20from%20previously%20analyzed%20image%3F)).
![image](https://github.com/user-attachments/assets/388695ef-b32e-43d5-b43d-ae9b8f1a9be3)

2. When `Also detect foci in Channel B and perform colocalization` is checked: a  `.zip` file ending with `foci_coloc_map.zip`, containing the [colocalization maps](https://imagej.net/plugins/foci-analyzer#colocalization-maps). Here, analysis settings are also stored in the metadata (`Image` -> `Show Info... in Fiji).

3. A `.tsv` file ending with `Foci_results.tsv` with statistics _per cell/nucleus_, with the following columns: _cell area/volume, background intensity, mean intensity, sum intensity, foci count, mean foci intensity, median foci intensity, mean foci volume, median foci volume, total foci volume, total foci intensity_ for the foci channel(s), as well as _background intensity, mean intensity, sum intensity_ for the nucleus channel. When colocalization is performed, the table also contains: _overlapping foci count, overlapping foci volume, overlap count % ch_A, overlap volume ch_A, count % ch_B, overlap count % ch_B, overlap volume ch_B_.

4. A `.tsv` file ending with `All_Foci_statistics.tsv` containing relationship info and intensity info for every individual focus: _label, Cell ID, Mean, StdDev, Max, Min, Median, Skewness, Area/Volume, Circularity/Sphericity, Centroid.X, Centroid.Y, (Centroid.Z)_. (Centroids coordinates with respect to the image origin.)

### Log
The complete Log Window is saved as `Log.txt` in the output folder after the analysis has finished.

### Colocalization maps

The macro produces overlap maps for the foci in the two chosen channels that visualize the overlap of foci in the different channels. This map has 6 channels:

1. detected foci mask channel A (green)
2. detected foci mask channel B (red)
3. overlap % foci _count_ with channel A (azure; the brighter, the more foci overlap)
4. overlap % foci _area/volume_ with channel A  (Manders M1) (magenta)
5. overlap % foci _count_ with channel B (azure)
6. overlap % foci _area/volume_ with channel B (Manders M2) (magenta)

![image](https://github.com/user-attachments/assets/d4f43130-7d62-4568-beb4-6e2513064706)

## Handling results
For each image (or frame) a new result file is generated. When multiple images (or frames) are processed. Result `.tsv` files in a folder can be appended by running `Combine result files` in the Foci-Analyzer Fiji submenu. The resulting table is saved as `Results_all_files.tsv` in the same folder as the input `.tsv` files. (By the way, this script also runs on other text-based files, e.g. `.csv`, `.txt`.)
