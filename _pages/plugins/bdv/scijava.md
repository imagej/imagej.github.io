---
mediawiki: Bigdataviewer_Scijava
title: Bigdataviewer Scijava
---

As announced in the forum [here](https://forum.image.sc/t/getting-bigdataviewer-instance-in-an-imagej-command/21110/8) and [here](https://forum.image.sc/t/fiji-commands-for-bigdataviewer/25601), this repository aims at a better integration of BigDataViewer into Fiji by using the Scijava Framework.

## Installation

Enable the [update site](/update-sites/following) (https://biop.epfl.ch/Fiji-Update-Bdv/) to activate bigdataviewer\_scijava commands. All commands from this update site are present in the github repository [bigdataviewer\_scijava](https://github.com/BIOP/bigdataviewer_scijava). A [list of all commands](https://github.com/BIOP/bigdataviewer_scijava#list-of-all-commands-of-the-repository) can be found in the repository.

## Goals

-   **Modularity for bigdataviewer!** Being able to combine scripts or code for display and processing. This update site creates a way to access an existing BDV instance when scripting or writing java code.
-   **Provide a set of macro recordable commands for bigdataviewer**. Makes it possible to script basic actions on BigDataViewer with the IJ1 recorder.

## What you can do with this update site

By using Scijava framework to store BigDataViewer windows through its `BdvHandle` interface, it is possible to communicate bdv instances between scripts and commands (see [script parameter page](/scripting/parameters)). This also facilitates the use of Fiji GUI because the commands of this repository can be chained easily. Any script or Command which declares a `BdvHandle` parameter can retrieve or provide reference to existing BigDataViewer instances.

In practice, Bdv windows created via the commands from this update site are put by default in the `ObjectService`. To get a reference to these windows:

-   In groovy, add this at the beginning of your script

<!-- -->

    #@bdv.util.BdvHandle bdvh

-   In Java:

<!-- -->

    @Parameter
    BdvHandle bdvh;

## How to make your bigdataviewer workflow compatible with Scijava

Two options:

-   Use the command `BdvWindowCreate` from this repository and retrieve its reference through SciJava parameter annotation. This will make your Bdv Window accessible to other plugins / commands.
-   Create your own Bdv window, but declare the associated `BdvHandle` as an output of your Command:
    -   in Java: `@Parameter(type = ItemIO.OUTPUT); BdvHandle bdvh_out;`

The type of the parameter annotation can also be `ItemIO.BOTH` if your command is modifying an existing `BdvHandle`

## Secondary Goals

This repo provide an implementation of all the command from the repository bigdataviewer\_fiji to make it scijava compatible, so it should have the same commands.

-   Because complex bdv dataset (metadata, multiple views, channels...) are usually organized into `SpimData` objects, this update site / repository also provide tools to manipulate these objects, in a scijava compatible manner. Hence declaring in groovy `#@mpicbg.spim.data.generic.AbstractSpimData sd` or in java `@Parameter AbstractSpimData asd;` allows to manipulate and communicate such objects.
-   Easy visualization of the bdv sources present in a Bdv Window (-&gt; access to display options). Right clicking on selected source also enables to access basic display operations.
-   Easy edition with "standard actions" on bdv sources held within a Bdv Handle:
    -   transform
    -   registration
    -   export
    -   import

## Examples

### Video

#### 1 - Simple

https://www.youtube.com/watch?v=-q5qIdH9Idw (1 minute)

-   Open a sample image.
-   Change display settings.
-   Double clicking on the source in the bdv window translate the window to the origin of the source

#### 2 - IJ Script example

https://youtu.be/IjIW5bOn4P8 (3 minutes)

-   Create Bdv Window
-   Start IJ1 recorder
-   Open a voronoi image
-   Create an affine transform
-   Transform source with affine transform
-   Make a loop and execute it
-   Modify display settings

#### 3 - Procedural + Warping + Export (xml hdf5 and ImagePlus)

https://youtu.be/uOYWn7tUsf0 (7 minutes)

-   Open a procedural image ( mandelbrot )
-   Create new Bdv Window
-   Open voronoi in this new window
-   Warp one into another using BigWarp
-   Create a new bdv window
-   Transfer initial Voronoi Image into this window
-   Transfer transformed fractal into this window
-   Resample transformed Mandelbrot like Voronoi
-   Save initial voronoi and transformed resampled mandelbrot into a new dataset
-   Close everything
-   Reopen saved dataset
-   Apply correct display settings

Resampling is necessary because XML/Hdf5 do not allow to save procedural images.

### Scripts

#### Groovy

Run both scripts consecutively:

-   Display a recursive Fiji image:

<!-- -->

    import bdv.util.Procedural3DImageShort
    import net.imglib2.RealRandomAccessible
    import bdv.util.BdvFunctions
    import bdv.util.BdvOptions
    import bdv.util.BdvHandle
    import net.imglib2.type.numeric.integer.UnsignedShortType
    import net.imglib2.FinalInterval
    import net.imglib2.Interval
    import net.imglib2.type.numeric.ARGBType
    // Input : provided by Single Input Preprocessor in case no widow is present
    #@bdv.util.BdvHandle bdv_h 
    // Output : allow to updates list of sources
    #@output bdv.util.BdvHandle bdv_h 

    // Simple Fiji Image stored as an array
    fijiData =
                [[0,0,0,0,0,0,0,0,0],
                 [0,1,1,1,1,1,1,1,0],
                 [0,1,0,0,0,0,0,0,0],
                 [0,1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1,0],
                 [0,1,0,0,0,1,0,0,0],
                 [0,1,0,1,1,1,0,0,0],
                 [0,0,0,0,0,0,0,0,0]] as short[][];

    // Declare a procedural image
    def s = new Procedural3DImageShort({p -> getRecursiveFiji(p[1], p[0], p[2])}).getRRA();  

    // Interval (mainly useless here, but required by BdvFunctions
    Interval interval = new FinalInterval([ 0, 0, 0] as long[], [ 9, 9, 0 ] as long[]);

    // Display the source in the bdv_h window
    bss = BdvFunctions.show( s , interval, "Fiji", BdvOptions.options().addTo(bdv_h) );

    // Display options
    bss.setDisplayRange(0,1);
    bss.setColor(new ARGBType(ARGBType.rgba(101,164,227,255)));


    //------------- FUNCTION for recursive Fiji Image generation

    int getRecursiveFiji(double x, double y, double level) {
        def valueLevel = (int) (fijiData[((int)x%9)][((int)y%9)])
        if (level<=0) {
            return valueLevel
        } else {
            if (valueLevel==1) {
                if (level>2) {
                    level=2;
                }
                return getRecursiveFiji(x*9,y*9,level-1)
            } else {
                return 0
            }
        }
    }

-   Duplicate and rotate specified sources:

<!-- -->

    import ch.epfl.biop.bdv.scijava.command.BdvWindowCreate
    import ch.epfl.biop.bdv.scijava.command.edit.transform.BdvSourcesAffineTransform
    import bdv.util.BdvHandle

    // bdv handle containing the source to transform
    #@bdv.util.BdvHandle bdv_h_in
    // index of the source in bdv handle input 
    #@int index_src
    // output bdv window
    #@output bdv.util.BdvHandle bdv_h_out

    // Command Service
    #@CommandService cs

    bdv_h_out = (BdvHandle) cs.run(BdvWindowCreate.class, true,
                    "is2D",false,
                    "windowTitle","Bdv_out",
                    "px",0.0,
                    "py",0.0,
                    "pz",-1.0,
                    "s",12.0).get().getOutput("bdvh");

    affine_matrix = "[3d-affine: (0.45, -0.05, 0.0, 0.4, 0.05, 0.5, 0.0, -0.2, 0.0, 0.0, 1.0, -0.6)]";

    cs.run(BdvSourcesAffineTransform.class, true, 
                    "at", affine_matrix,
                    "transformInPlace", false,
                    "bdvh", bdv_h_in,
                    "bdvh_out", bdv_h_out,
                    "sourceIndexString", index_src,
                    "output_mode", "Add To Bdv").get()

    for (int i=0;i<2;i++) {
        cs.run(BdvSourcesAffineTransform.class, true,
                    "at", affine_matrix,
                    "transformInPlace", false,
                    "bdvh", bdv_h_out,
                    "bdvh_out", bdv_h_out,
                    "sourceIndexString", i,
                    "output_mode", "Add To Bdv").get()
    }

#### IJ1 Macro Language

Opens blobs and deforms it and append it in BigDataViewer:


    run("Create Empty BDV Frame", "is2d=false windowtitle=Bdv px=0.0 py=0.0 pz=-1.0 s=850.0");
    run("Blobs (25K)");
    run("Current IJ1 Image [ImgLib2]");
    run("Set Sources Color", "c=255,51,51 sourceindexstring=0"); 
    run("Transform Sources (Affine, string)", "sourceindexstring=0 bdvh_out=Bdv output_mode=[Add To Bdv] stringmatrix=[1,-0.1,0,250,\n 0,0.5,0.1,0,\n 0,0,1,0, \n 0,0,0,1] transforminplace=false");

## List of all commands

The list of commands of this repository is available in the git repository : https://github.com/BIOP/bigdataviewer_scijava
