---
title: Diadem Challenge Data
---

This page describes how to visualize the various data sets provided as part of the [Diadem Challenge](http://www.diademchallenge.org/) in Fiji, and in particular viewing the traced neurons with [Simple Neurite Tracer](/plugins/snt). The most important point about this is that the SWC files distributed as part of the challenge all use co-ordinates that are image-coordinates rather than world co-ordinates. (This isn't how I interpret [the paper that describes the SWC format](http://dx.doi.org/10.1016/S0165-0270(98)00091-0), but in practice different software uses different conventions, so one has to deal with both.) This means that you should always select the "ignore image calibration" option when importing the SWC file into Simple Neurite Tracer. The other key point is that the image data are distributed with each slice in a separate TIFF file and don't specify the slice separation in those files. So, after importing the sequence you will need to correct the calibration according to information on the Diadem challenge website or they will look odd when rendered in 3D. I describe these steps in more detail below.

If you have any comments or suggestions relating to this page, please email <em>mark-diadem</em> at <em>longair</em> dot <em>net</em>.

## Olfactory Project Neurons

This data set [is described here](http://www.diademchallenge.org/olfactory_projection_fibers_readme.html). I will go through loading the example "OP\_1". Each image stack in this data set is distributed as a directory of TIFF files, one per slice. To load such a stack, go to {% include bc path='File | Import | Image Sequence'%} and select the file "1.tif". You should be shown a dialog like this:

![](/media/diadem-challenge-data-1.png)

These default options should be fine - as you can see from the dialog it will have worked out that there are 60 image slices in that directory to be imported. If you click OK you should get a normal image stack:

![](/media/diadem-challenge-data-2.png)

Unfortunately these TIFF files do not have the separation of these slices encoded correctly, so you should correct this manually. If you go to {% include bc path='Image | Properties'%} you will see that the pixel width, pixel height and voxel depth are all set to the same value (0.3296485). The [page with information about the data set](http://www.diademchallenge.org/olfactory_projection_fibers_readme.html) tells us that the z-separation should be three times the x and y separation, so correct the voxel depth to 3 times 0.3296485, like this:

![](/media/diadem-challenge-data-4.png)

... and then press "OK". To save yourself from having to re-enter this calibration information, and to be able to open the stack from the "Recent Files" menu, etc. I think it's helpful to now save this stack as a single TIFF. So, I would go to {% include bc path='File | Save As | Tiff ...'%} and save this as OP\_1.tif in the directory above the one with individual slices.

Now start the tracing plugin by going to {% include bc path='Plugins | Segmentation | Simple Neurite Tracer'%}. If you keep the default options, you should see a display like this:

<img src="/media/diadem-challenge-data-6.png" width="750"/>

To load the SWC file with the supplied traces, click on "Load Traces / SWC File" and navigate to OP\_1.swc. When you have selected this file, you will see the following options dialog:

![](/media/diadem-challenge-data-7.png)

The important setting here is that you should have the "Ignore calibration" option selected. You should not apply an offset or scale for this data set. When you click OK you should see that the traces are overlayed in the stack window and in the 3D viewer:

<img src="/media/diadem-challenge-data-8.png" width="750"/>

You may wish at this point to adjust the viewing options in the tracer's dialog to examine the tracings in detail:

<img src="/media/diadem-challenge-data-9.png" width="750"/>

## Diadem Neocortical Layer 1 Axons

[The Neocortical Layer 1 Axons](http://www.diademchallenge.org/neocortical_layer_1_axons_readme.html) data set is based on a set of image stacks that need to be stitched together. The key point here is that you must use the offsets supplied by the Diadem challenge rather than allowing Fiji to stitch the automatically - the stitching will be subtly different.

Firstly, however, it will help to load each image sequence and save out the stack to a single TIFF image stack file. For each of the 6 directories, do the following: go to {% include bc path='File | Import | Image sequence'%} and select the first file in the directory (01.tif). After opening with the default options, save this out into the parent directory with the following names:

```
directory 01 -> Tile_01_02.tif
directory 02 -> Tile_02_02.tif
directory 03 -> Tile_03_02.tif  
directory 04 -> Tile_03_01.tif  
directory 05 -> Tile_02_01.tif  
directory 06 -> Tile_01_01.tif
```

Now create a text file in the same directory called TileConfiguration.txt with the following contents, but changing the directory path to whereever these files are on your computer:

```
# Define the number of dimensions we are working on
dim = 3

# Define the image coordinates
/home/mark/diadem-examples/Neocortical/Tile_01_01.tif; ; (0.0, 0.0, 0.0)
/home/mark/diadem-examples/Neocortical/Tile_02_01.tif; ; (468.0, -14.0, -1.0)
/home/mark/diadem-examples/Neocortical/Tile_03_01.tif; ; (924.0, 3.0, -19.0)
/home/mark/diadem-examples/Neocortical/Tile_01_02.tif; ; (73.0, 507.0, -5.0)
/home/mark/diadem-examples/Neocortical/Tile_02_02.tif; ; (526.0, 484.0, 11.0)
/home/mark/diadem-examples/Neocortical/Tile_03_02.tif; ; (952.0, 462.0, -21.0)
```

These offset values are taken from [the official page describing the data set](http://www.diademchallenge.org/neocortical_layer_1_axons_readme.html).

Now you can stitch together the images using these offsets by going to {% include bc path='Plugins | Stitching | Stitch Collection of Images'%}, browsing to the TileConfiguration.txt file you've just created and making sure you uncheck the box "compute overlap". It should look something like this:

![](/media/diadem-neocortical-layer-6-axons-1.png)

After clicking OK, this should stitch together all those stacks into one huge stack. (If there are problems, you should see details of them in the log window.)

<img src="/media/diadem-neocortical-layer-6-axons-2.png" width="750"/>

Next, you should correct the Z-calibration of the stitched stack. The data set page tells us that the z separation is 3.03 pixels, so open up {% include bc path='Image | Properties'%} and set the Voxel Depth to 3.03 times the Pixel Width:

![](/media/diadem-neocortical-layer-6-axons-3.png)

Now you should save the stitched stack, and work from that from now on. (Since the stitched stack isn't very large (156MB) one wonders why this wasn't distributed already stitched.) Save the stack with {% include bc path='File | Save As | Tiff...'%}.

To load the SWC files, start up the tracer with {% include bc path='Plugins | Segmentation | Simple Neurite Tracer'%}. You should see something like this after it has started, with the stack rendered in the 3D Viewer:

<img src="/media/diadem-neocortical-layer-6-axons-4.png" width="750"/>

You might have noticed that the offsets used in stitching above had some negative Y and Z values. This means that when you load in the SWC files, you will need to apply an offset to compensate for this. (0,0,0) in the stitched image will be at (0,-14,-21) in the space of the tracings, so when you click on "Import traces / SWC file" and have chosen (for example) NC\_14.swc, you should expand the "Apply offset to SWC file co-ordinates" option and fill in these values:

![](/media/diadem-neocortical-layer-6-axons-7.png)

Then the traces should load in the correct position with those offsets:

<img src="/media/diadem-neocortical-layer-6-axons-6.png" width="750"/>

## Cerebellar Climbing Fibers

We will go through loading in the CF\_1 image stack from the [Cerebellar Climbing Fibers](http://www.diademchallenge.org/cerebellar_climbing_fibers_readme.html) data set. The raw data for this image is stored in RGB and about 3.4GB in size, so for convenience you may wish to load this as a virtual stack (i.e. one where the slices are loaded from disk as required), convert it to 8-bit and resave the file first. In any case, I would recommend using a machine with 2GB of RAM (at the very least) to deal with these files.

To load the files as a virtual stack, go to {% include bc path='File | Import | Image Sequence ...'%} and select the first file in the sequence, "01.tif". You will be presented with the import dialog, in which you should make sure that "Use virtual stack" is selected.

![](/media/diadem-cerebellar-1.png)

(Note that the number of slices in the directory (34) was automatically set.) You should now be able to browse through the stack:

<img src="/media/diadem-cerebellar-2.png" width="750"/>

After loading this you need to convert this to 8-bit. You can do this in any number of ways, and if you're actively working on a tracing task with this data you will probably want to do this in such a way that picks out the brown coloured neuronal processes. However, a simple way just for viewing purposes is to use the {% include bc path='Image | Color | RGB to Luminance'%} option. (Another option is to use {% include bc path='Image | Type | 8-bit'%}.) This will produce results like this:

<img src="/media/diadem-cerebellar-3.png" width="750"/>

You can close the original virtual stack now.

It is a good idea to invert this image, since the 3D Viewer will make the low values of the image more transparent, and Simple Neurite Tracer assumes that neurons are brighter than their background. So, go to {% include bc path='Edit | Invert'%} and select "Yes" in response to the question about whether to process all 34 images. The results should look like this:

<img src="/media/diadem-cerebellar-4.png" width="750"/>

Before saving this out as a single 862MB stack, it is a good idea to correct the calibration of the image. The [data set web page](http://www.diademchallenge.org/cerebellar_climbing_fibers_readme.html) tells us that the separation between slices is 8.08 pixels. So, if you bring up the {% include bc path='Image | Properties'%} dialog, then you can correct the voxel depth to be 8.08 times the pixel width:

![](/media/diadem-cerebellar-5.png)

Now save this as a single TIFF stack called CF\_1.tif by going to {% include bc path='File | Save As | Tiff ...'%}, saving it in the directory above the one with the slices, to avoid confusion.

You can now start the tracer with {% include bc path='Plugins | Segmentation | Simple Neurite Tracer'%}. This may take some time, since there is a lot of data to load in to the 3D viewer. The result should look like this:

<img src="/media/diadem-cerebellar-6.png" width="750"/>

You may wish to adjust the transparency in the 3D viewer by selecting the image volume (left click on the image in the 3D viewer) and then going to {% include bc path='Edit | Attributes | Change Transparency...'%}:

![](/media/diadem-cerebellar-7.png)

Now, to load the traces click on "Load Traces / SWC File" and select CF\_1.swc. You will be presented with an options box like this:

![](/media/diadem-cerebellar-7b.png)

Make sure that "Ignore calibration" is selected (as in that screenshot) and that there is no offset or scale set. Once loaded you should be able to see the traces as here:

<img src="/media/diadem-cerebellar-8.png" width="750"/>

## Hippocampal CA3 Interneuron

The [Hippocampal CA3 Interneuron](http://www.diademchallenge.org/hippocampal_ca3_Interneuron_readme.html) data set is difficult to deal with, since even after converting the stack to 8-bit values, it is still nearly 2GB in size.

As with the other stacks, you should load the image stack using {% include bc path='Import | Image Sequence'%} and selecting the "Use virtual stack" option:

![](/media/diadem-hippocampal-ca3-interneuron-2.png)

That should load in the image data:

<img src="/media/diadem-hippocampal-ca3-interneuron-3.png" width="750"/>

Now convert it to 8-bit with {% include bc path='Image | Type | 8-bit'%}. (The same comments as above regarding converting to 8-bit apply here as well.)

<img src="/media/diadem-hippocampal-ca3-interneuron-4.png" width="750"/>

... and invert the image with {% include bc path='Edit | Invert'%}, saying "Yes" to the question about whether to process all 110 slices:

<img src="/media/diadem-hippocampal-ca3-interneuron-5.png" width="750"/>

Now set the voxel depth to 1.52 times the voxel width, as specified on the [data set page](http://www.diademchallenge.org/hippocampal_ca3_Interneuron_readme.html):

![](/media/diadem-hippocampal-ca3-interneuron-6.png)

And then I would save this file as a TIFF stack (with {% include bc path='Save As | Tiff...'%}) so that you don't have to go through these steps again. That will need about 2GB of disk space, and will only work if your filesystem supports single files of that size.

If you now start {% include bc path='Plugins | Segmentation | Simple Neurite Tracer'%} with its default options you should (eventually!) see something like the following:

<img src="/media/diadem-hippocampal-ca3-interneuron-7.png" width="750"/>

Then you can load the SWC files via "Load Traces / SWC file" with these options:

![](/media/diadem-hippocampal-ca3-interneuron-8.png)

(I've unchecked "Replace existing paths" for this data set, since it's nice to load several SWC files into the tracer at once.) The results of loading three of the reconstructions, for example, might look like this:

<img src="/media/diadem-hippocampal-ca3-interneuron-9.png" width="750"/>

## Neuromuscular Projection Fibers

There are a number of caveats regarding these image data and reconstructions which are [listed on its web page](http://www.diademchallenge.org/neuromuscular_projection_fibers_readme.html).

These 152 image stacks are in total so large that stitching them together and dealing with the stitched stack is not likely to be helpful. Instead, I would suggest that you just stitch together those images that you need to cover a particular SWC file. Since there are so many input stacks, I've written a clojure script for Fiji to help process these, which you can [view and download via github](http://gist.github.com/508411). On running this script you will be asked to select a directory - you should select the directory that contains all of your unpacked image stack directories (probably called "000", "001", etc.) For each of these directories it will then:

-   Import the sequence of slices
-   Correct the calibration so that the voxel depth is 3.04 times the pixel width
-   Write out each stack as a single TIFF stack (e.g. as well as the directory "000" you will also have "000.tif"

Finally, the script will output a TileConfiguration.txt file in the same directory. Supposing one had vast amounts of RAM, this file could be used unaltered with {% include bc path='Plugins | Stitching | Stitch Collection of Images'%}, as above. However, the file is still useful even with modest amounts of RAM, since you can copy this file to a new name and edit out all but a few of the images that are listed there. For example, here are image stacks 000 to 007 stitched together:

<img src="/media/neuromuscular-0-7-stitched.png" width="750"/>

That script may be useful as a basis for a smarter selection of images to stitch for particular reconstructions.

You should then be able to adjust the SWC import options in order to import the reconstructions in the correct positions - you will need to understand the translations described for the reconstructions [on the web page](http://www.diademchallenge.org/neuromuscular_projection_fibers_readme.html) in order to get this right. (I haven't had time to do this accurately myself yet.)


