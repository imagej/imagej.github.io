---
mediawiki: SPIM_Bead_Registration_(deprecated)
name: "Selective Plane Illumination Microscopy Registration"
title: SPIM Bead Registration (deprecated)
categories: [Registration]
release-date: "September 2011"
initial-release-date: "February 2010"
website: "http://fly.mpi-cbg.de/~preibisch"
team-founder: ['@StephanPreibisch', '@axtimwalde', '@dscho', '@tomancak']
team-maintainer: '@StephanPreibisch'
---

{% include info-box filename='SPIM\_Registration.jar'  category='SPIM Registration' %}

## Important Note

<span style="color:#A52A2A"> ***Please Note: This version of the software is outdated. It will be part of Fiji for the time being, but I highly recommend using the new [Multiview Reconstruction Plugin](/plugins/multiview-reconstruction). It is much more powerful, flexible and completely integrated with the [BigDataViewer](/plugins/bdv).*** </span>

## Citation

Please note that the SPIM registration plugin available through Fiji, is based on a publication. If you use it successfully for your research please be so kind to cite our work:

-   S. Preibisch, S. Saalfeld, J. Schindelin and P. Tomancak (2010) "Software for bead-based registration of selective plane illumination microscopy data", *Nature Methods*, **7**(6):418-419. [Webpage](http://www.nature.com/nmeth/journal/v7/n6/full/nmeth0610-418.html) [PDF](/media/nmeth0610-418.pdf) [Supplement](/media/nmeth0610-418-s1.pdf)

For technical details about the bead-based registration method and SPIM imaging see [SPIM Registration Method](/plugins/spim-registration/method).

## Overview of the ***deprecated*** SPIM bead-based registration plugin

The SPIM Registration plugin reconstructs an image from several input images, called views. For this reconstruction process some parameters defining the input and output data are required. The user has to define the naming convention of the input images, an approximate bead-brightness as well as the strategies for creating the fused output image.

### Creating a cropped output image

As the output images are typically very big (bounding box around all registered views) it is strongly recommended to define a cropping area where the imaged sample is positioned in the output image. As this is not possible in the first run, there is an option to first create a down-sampled version of the output image from which one can extract the cropping area. By running the plugin again and loading the previous registration parameters the cropped full-resolution output image can be created efficiently.

### Downloading example dataset

There is a 7-angle SPIM dataset of *Drosophila* available [here](http://fly.mpi-cbg.de/preibisch/nm/HisYFP-SPIM.zip). The cropping parameters pre-set in the plugin fit this dataset, only the appropriate folder has to be defined.

### System requirements

Multi-view SPIM datasets are typically rather large, therefore it is recommended to use the registration plugin on a computer with a lot of RAM. The minimal requirement for the example dataset is **at least 4Gb** of memory however we recommend an **8Gb** system. You may need to increase the Fiji memory limit by going to {% include bc path="Edit|Options|Memory & Threads" %}.

### Using the Plugins

There are three plugins which take those input parameters in different formats:

-   **[SPIM Registration](/plugins/spim-registration#spim-registration)**: Allows the registration of SPIM data with a subset of necessary options presented in the graphical user interface
-   **[Multi-Channel SPIM Registration](#multi-channel-spim-registration)**: Extends the [SPIM Registration](/plugins/spim-registration) to multiple channels and allows to override the z-stretching saved in the input files.
-   **[Advanced SPIM Registration](#advanced-spim-registration)**: Registration of SPIM data using all possible options via loading a configuration file

### Processing a Time Lapse Acquisition

Processing a time lapse acquisition requires two steps. In the first step the registration for each individual timepoint has to be computed and will be automatically stored. Therefore, in the first pass, input the timepoints that should be processed in **Time Points to process** (e.g. 1-100), check **Register only (no fusion)** and uncheck **Timelapse processing**. After the registration is performed one timepoint has to be selected as reference timepoint, typically one with a low registration error. This timepoint should be fused to determine the **[correct cropping area ](#creating-a-cropped-output-image)** which will afterwards be applied to all other timepoints.

After all individual timepoints are registered and the cropping area is defined the plugin has to be called again. This time check **Timelapse Registration**, insert the **Reference Timepoint**, uncheck **Register only (no fusion)** and insert the coordinates of the cropping area of the reference timepoint. The created output images can be viewed for example with {% include bc path="Plugins|Image5D|Virtual Image 5D Opener" %} [1](https://imagej.net/ij/plugins/image5d.html).

## ***deprecated*** SPIM bead-based registration

{% include thumbnail src='/media/spim-registration.png' title='Shows the SPIM Registration Dialog.'%}

-   **SPIM Data Directory**: Fill in the directory name that contains all the image files. You can either drag&drop the directory, browse for it or type the name directly.

<!-- -->

-   **Time Points to process**: Define the timepoint(s) that should be processed. You can give single numbers (e.g. 18), enumerate (e.g. 1, 18, 19, 100), define ranges (e.g. 1-18) or combine all of them in any combination wanted (e.g. 1,2,10,20-50).

<!-- -->

-   **Pattern of SPIM files**: Define the naming convention of the input files by explaining how the angle and the timepoint is encoded into the filename. For example the file names are named in following way  
    *spim\_tl1\_angle0.lsm*, *spim\_tl1\_angle45.lsm* ... *spim\_tl1\_angle270.lsm*  
    *spim\_tl2\_angle0.lsm*, ... *spim\_tl2\_angle270.lsm*  
    *spim\_tl100\_angle0.lsm*, ... *spim\_tl100\_angle270.lsm*.  
    That means the pattern of the file names corresponds to **spim\_tl{t}\_angle{a}.lsm**, where **{t}** is replaced with the current timepoint and **{a}** with the current angle. If the numbers contain leading zeros (e.g. 000, 045, 090, 135 instead of 0, 45, 90, 135), this can be encoded by simply adding more letters to the placeholder, in this case **{aaa}**.

<!-- -->

-   **Angles to process**: Define the angles (at least 2) that should be processed (for each timepoint if applicable). You can enumerate angles (e.g. 0, 90, 180, 270), define ranges in steps (e.g. 0-270:45 which means use angle 0 to 270 in steps of 45, i.e. 0, 45, 90, 135, 180, 225, 270) or combine all of them in any combination wanted (e.g. 0, 45, 180-270:45).

<!-- -->

-   **Timelapse processing**: Checked if a timelapse processing should be performed. In this case the **pre-registered** timepoints are re-registered to one reference timepoint which results in an aligned time series.

<!-- -->

-   **Reference Timepoint**: Define the reference timepoint for timelapse processing if timelapse processing above is checked.

<!-- -->

-   **Load segmented beads**: If the registration of the time point is carried out more than once (to recompute the registration) the initial segmentation of the beads can be loaded to speed up processing. Note: if **Load registration** is checked, **Load segmented beads** is implicitly checked as well.

<!-- -->

-   **Bead Brightness**: Define the brightness of the used beads relative to the sample.

<!-- -->

-   **Load Registration**: If the registration of the time point is carried out more than once (either to define the correct cropping area or to perform timelapse processing) the initial segmentation of the beads and the final affine matrices of the views can be loaded to speed up processing. Note: if **Load registration** is checked, **Load segmented beads** is implicitly checked as well and **Display registration** will be ignored.

<!-- -->

-   **Register only (no fusion)**: Checked if no fusion of the data should be performed.

<!-- -->

-   **Display registration**: This will display an interactive window visualizing the global optimization process.
    {% include notice icon="note" content="This slows down the optimization." %}

<!-- -->

-   **Fusion Method**: There are three options available.  
    *Fuse all images at once* loads all the input images and computes the output image. This is the fastest method but it also needs significant amounts of RAM.  
    *Fuse images sequentially* loads one input image after the other and computes the contribution sequentially. This is significantly slower but typically uses less RAM. However, this methods needs to allocate the output image twice during the fusion process as it needs to store image content and weights separatetly.  
    *Create independent registered images* is a special output option where each view is transformed into a compatible bounding box and written as a separate file for further processing.

<!-- -->

-   **Fusion use Blending**: Checked if blending at the edges of the overlapping views should be applied; this removes brightness differences at the hyperplanes where the overlapping images intersect.
    {% include notice icon="note" content="If neither Blending nor Content based Weightening is selected, only averaging is performed for fusion." %}

<!-- -->

-   **Fusion use Content based Weightening**: Checked if the content-based weightening should be used; this weights each pixel of each view by its local information content and thereby increases the contrast of the output image.
    {% include notice icon="note" content="The content based weightening is rather fast but consumes a lot of RAM. If neither Blending nor Content based Weightening is selected, only averaging is performed for fusion." %}

<!-- -->

-   **Output Image Scaling**: The factor defines the downsampling of the output image, e.g. 2 means that the output image will be half as big in each dimension and therefore need 8x less RAM than the full resolution output image. This is especially useful if the bounding box around the imaged sample (defined below) is not known yet as has to be determined.

<!-- -->

-   **Crop Offset Output Image X/Y/Z**: Defines the cropping offset in the x/y/z-dimension of the output image relative to the uncropped image. A value of 0 means no cropping.
    {% include notice icon="note" content="all the values are relative to the downsampling factor in **Output Image Scaling**." %}
-   **Crop Size Output Image X/Y/Z**: Defines the cropped size in the x/y/z-dimension of the output image relative to the uncropped image. A value of 0 means no cropping.
    {% include notice icon="note" content="all the values are relative to the downsampling factor in **Output Image Scaling**." %}

## Plugin Wishlist

When you find some features that you would like to be added to the plugin, please write them down here

-   Change Z-Stretching in Plugin
-   Automatic Timelapse processing
-   Preview (e.g. Max Projections of first angle) if register only checked and more than one timepoint

## Multi-Channel SPIM Registration

The multi-channel SPIM Registration extends the normal registration by the ability to register multiple channels and to override the resolution (xy, z) stored in the files. Therefore two new options are available

-   **Channels to process**: Define the channel(s) to process. You can give single numbers (e.g. 0), enumerate (e.g. 1, 2), define ranges (e.g. 1-3) or combine all of them in any combination wanted (e.g. 1,3-4).

<!-- -->

-   **Override file dimensions**: Check this box to override the axial and lateral resolution stored in the input files.

<!-- -->

-   **xy resolution (um/px)**: Define the xy-resolution in um per pixel, note that only the ratio between xy and z-resolution is used.

<!-- -->

-   **z resolution (um/px)**: Define the z-resolution in um per pixel, note that only the ratio between xy and z-resolution is used.

## Advanced SPIM Registration

{% include thumbnail src='/media/plugins/advanced-spim-registration.png' title='Shows the Advanced SPIM Registration Dialog.'%}  
For advanced SPIM registration all available parameters can be tuned using two configuration files (configuration.txt and VariablesAssignment.txt, see below). Contact the author for further details [2](http://fly.mpi-cbg.de/preibisch/contact.html).

### configuration.txt

    ### Configuration file for SPIM Registration
    ### ----------------------------------------
    ###
    ### The first line is the filename for the linkage from the entries in this file to the
    ### variable names in java. It is very important and you only need to change this
    ### if you change the source code.
    ###
    ### The rest of the file is divided into sections where you can change different
    ### types of parameters. Really important is the Input files section. Change it
    ### according to your experiment data.

    <VariablesAssignment.txt>

    ###
    ### Section: General Parameters
    ###

    Time Point Pattern = "18"
    Acquisition Angle Pattern = "0-270:45"
    # The input files can be in any format that Fiji can read.
    # They need to be 3D stacks with correct calibration, though.
    Input File Pattern = "spim_TL{t}_Angle{a}.lsm"
    Input Directory = "F:\Stephan\dros\"
    Output Directory = "F:\Stephan\dros\output"
    Registration File Directory = "F:\Stephan\dros\registration\"
    Debug Level = "DEBUG_MAIN"
    Show ImageJ Window = true

    ###
    ### Section: Time Lapse 
    ###

    Time Lapse Registration = false
    Reference Time Point = 1

    ###
    ### Section: Data Structures, Access and Paging
    ###

    Factory for Images during Segmentation = ArrayContainerFactory()
    Factory for Recursive Gauss = ArrayContainerFactory()
    Factory for Images during Fusion = ArrayContainerFactory()
    #Factory for Output Images = ArrayContainerFactory()
    Factory for Entropy = ArrayContainerFactory()
    Factory for Scale Space = ArrayContainerFactory()

    #Factory for Images during Segmentation = CubeContainerFactory(16)
    #Factory for Recursive Gauss = CubeContainerFactory(16)
    #Factory for Images during Fusion = CubeContainerFactory(16)
    Factory for Output Images = CubeContainerFactory( 256 )
    #Factory for Entropy = CubeContainerFactory(16)
    #Factory for Scale Space = CubeContainerFactory(35)

    Paging Temporary Directory = null

    Out of Bounds Strategy for Fusion = OutsideStrategyValueFactory(0)
    Out of Bounds Strategy for Gauss = OutsideStrategyMirrorFactory()
    Interpolator for Output Image = LinearInterpolatorFactory()

    ###
    ### Section: Main Switches
    ###

    Write Output Image = true
    Show Output Image = true
    Segmentation Use Scale Space = true
    Fusion Use Entropy = false
    Fusion Use Gauss = false
    Fusion Use Blending = false

    Fuse all Images at once = false
    Fuse Images sequentially = false
    Number of Paralell Views = 4
    Create multiple registered Output Images = true    

    Register Only = false
    Display Registration = false
    Read Segmentation = true
    Write Segmentation = true
    Read Registration = false
    Write Registration = true

    ###
    ### Section: Image Parameters
    ###

    Override Z-Stretching of Image = true

    # 20x, 2um z spacing ( 2.0 / 0.73 )
    Image Z-Stretching = 2.739726027397260273972602739726

    Image Background = 0

    ###
    ### Section: Threshold Bead Segmentation
    ###

    Bead Segmentation Threshold = 0.9
    Bead Segmentation Fixed Threshold = 0.02
    Bead Segmentation Use Fixed Threshold = true 
    Bead Segmentation Circularity Factor = 0.5
    Bead Segmentation Minimum Black Border around Bead = 1
    Bead Segmentation Minimum Bead Size = 10
    Bead Segmentation Maximum Bead Size = 13375
    Bead Segmentation Use Center of Mass = false

    ###
    ### Section: Scale Space Bead Segmentation
    ###

    Bead Scale Space Minimum Peak Value = 0.01
    Bead Scale Space Minimum Initial Peak Value = 0.005
    Bead Scale Space Identity Radius = 3.0
    Bead Scale Space Maxima Tolerance = 0.01
    Bead Scale Space Image Sigma = 0.5
    Bead Scale Space Initial Sigma = 1.4
    Bead Scale Space Steps per Octave = 4
    Bead Scale Space Steps = 3
    Bead Scale Space Number of Threads = 0

    ###
    ### Section: Point Descriptor and Global Optimization
    ###

    Point Descriptor Difference Threshold = 50
    Point Descriptor Ratio of Distance = 10
    Point Descriptor Number of Neighbors = 3
    Point Descriptor Use Associated Beads = false   
    Point Descriptor Use RANSAC = true

    RANSAC Maximum Epsilon = 5
    RANSAC Minimum Inlier Ratio = 0.1  
    RANSAC Number of Iterations = 1000

    # p__ = ( 1 - r^n ) ^ k
    # k = log(p__) / log ( 1 - r^n )

    # p__ ... probability that ransac fails
    # r   ... min inlier ratio
    # n   ... minimal number of points needed to create model
    # k   ... number of iterations 

    ###
    ### Section: Output Image
    ###

    Output Image Scale = 1

    Output Image Crop Offset X = 0
    Output Image Crop Offset Y = 0
    Output Image Crop Offset Z = 0
    Output Image Crop Size X = 0
    Output Image Crop Size Y = 0
    Output Image Crop Size Z = 0


    Output Image Number of Threads = 0

    ###
    ### Section: Volume Injection
    ###

    Volume Injection Sigma = 0.25
    Volume Injection Cut Off Radius = 2

    ###
    ### Section: Entropy
    ###

    Entropy Histogram Bins = 256
    Entropy Window Size X = 25
    Entropy Window Size Y = 25

    ###
    ### Section: Blending
    ###

    Blending Alpha = 1.5

    ###
    ### Section: Gauss Fusion
    ###

    Gauss Fusion Sigma 1 = 20
    Gauss Fusion Sigma 2 = 40

### VariablesAssignment.txt

    Input File Pattern = String inputFilePattern
    Time Point Pattern = String timepointPattern 
    Acquisition Angle Pattern = String anglePattern
    Input Directory = String inputdirectory 
    Output Directory = String outputdirectory
    Registration File Directory = String registrationFiledirectory
    Debug Level = String debugLevel
    Show ImageJ Window = boolean showImageJWindow

    Time Lapse Registration = boolean timeLapseRegistration
    Reference Time Point = int referenceTimePoint

    Factory for Images during Segmentation = ContainerFactory imageFactory
    Factory for Recursive Gauss = ContainerFactory recursiveGaussFactory
    Factory for Images during Fusion = ContainerFactory imageFactoryFusion
    Factory for Output Images = ContainerFactory outputImageFactory
    Factory for Entropy = ContainerFactory entropyFactory
    Factory for Scale Space = ContainerFactory scaleSpaceFactory

    Paging Temporary Directory = String tempDir

    Out of Bounds Strategy for Fusion = OutsideStrategyFactory strategyFactoryOutput    
    Out of Bounds Strategy for Gauss = OutsideStrategyFactory strategyFactoryGauss
    Interpolator for Output Image = InterpolatorFactory interpolatorFactorOutput

    Write Output Image = boolean writeOutputImage
    Show Output Image = boolean showOutputImage
    Segmentation Use Scale Space = boolean useScaleSpace
    Fusion Use Entropy = boolean useEntropy
    Fusion Use Gauss = boolean useGauss
    Fusion Use Blending = boolean useLinearBlening

    Fuse all Images at once = boolean paralellFusion    
    Fuse Images sequentially = boolean sequentialFusion
    Number of Paralell Views = int numParalellViews  
    Create multiple registered Output Images = boolean multipleImageFusion    

    Register Only = boolean registerOnly
    Display Registration = boolean displayRegistration
    Read Segmentation = boolean readSegmentation
    Write Segmentation =  boolean writeSegmentation
    Read Registration = boolean readRegistration
    Write Registration = boolean writeRegistration   

    Override Z-Stretching of Image = boolean overrideImageZStretching
    Image Z-Stretching = double zStretching
    Image Background = int background
        
    Bead Segmentation Threshold = float threshold
    Bead Segmentation Fixed Threshold = float fixedThreshold
    Bead Segmentation Use Fixed Threshold = boolean useFixedThreshold 
    Bead Segmentation Circularity Factor = double circularityFactor
    Bead Segmentation Minimum Black Border around Bead = int minBlackBorder
    Bead Segmentation Minimum Bead Size = int minSize
    Bead Segmentation Maximum Bead Size = int maxSize
    Bead Segmentation Use Center of Mass = boolean useCenterOfMass

    Bead Scale Space Minimum Peak Value = float minPeakValue
    Bead Scale Space Minimum Initial Peak Value = float minInitialPeakValue
    Bead Scale Space Identity Radius = float identityRadius
    Bead Scale Space Maxima Tolerance = float maximaTolerance
    Bead Scale Space Image Sigma = float imageSigma
    Bead Scale Space Initial Sigma = float initialSigma
    Bead Scale Space Steps per Octave = int stepsPerOctave
    Bead Scale Space Steps = int steps
    Bead Scale Space Number of Threads = int scaleSpaceNumberOfThreads

    Point Descriptor Difference Threshold = double differenceThreshold
    Point Descriptor Ratio of Distance = double ratioOfDistance
    Point Descriptor Number of Neighbors = int neighbors
    Point Descriptor Use Associated Beads = boolean useAssociatedBeads    
    Point Descriptor Use RANSAC = boolean useRANSAC

    RANSAC Maximum Epsilon = float max_epsilon
    RANSAC Minimum Inlier Ratio = float min_inlier_ratio   
    RANSAC Number of Iterations = int numIterations

    Output Image Scale = int scale
    Output Image Crop Offset X = int cropOffsetX
    Output Image Crop Offset Y = int cropOffsetY
    Output Image Crop Offset Z = int cropOffsetZ
    Output Image Crop Size X = int cropSizeX
    Output Image Crop Size Y = int cropSizeY
    Output Image Crop Size Z = int cropSizeZ
    Output Image Number of Threads = int numberOfThreads

    Volume Injection Sigma = float sigma
    Volume Injection Cut Off Radius = int cutOffRadiusGauss

    Entropy Histogram Bins = int histogramBins
    Entropy Window Size X = int windowSizeX
    Entropy Window Size Y = int windowSizeY

    Blending Alpha = float alpha

    Gauss Fusion Sigma 1 = float fusionSigma1
    Gauss Fusion Sigma 2 = float fusionSigma2

 
