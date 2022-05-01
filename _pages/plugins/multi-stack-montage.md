---
mediawiki: Multi_Stack_Montage
title: Multi Stack Montage
categories: [Stacks, Montage, Visualization]
---


{% capture source%}
{% include github org='PTBIOP' repo='ijp-multi-stack-montage' %}
{% endcapture %}
{% include info-box name='Multi Stack Montage' software='ImageJ' author='Olivier Burri, Romain Guiet' maintainer='Olivier Burri' filename='Multi\_Stack\_Montage.jar' released='August 2015' latest-version='August 2015' source=source status='stable' website=' [BIOP Staff Page](http://biop.epfl.ch/INFO_Facility.html#staff)' %}

## Purpose

This plugin brings a bit more functionality that was not available using the **Make Montage...** Plugin, namely making montages out of multiple stacks and hyperstacks.

## Installation

This plugin is available from the [PTBIOP Update Site](/list-of-update-sites) This places it in a "BIOP" Folder in the plugins directory of Fiji/ImageJ

## Use

Call up the plugin using {% include bc path="Plugins|BIOP|Multi Stack Montage..." %} and select the stacks that you wish to use.

{% include img src="hyperstacks-montage-menu" width="400" caption="Interface of the plugin" %}

{% include notice icon="warning" content='If you are going to make a montage, you need each stack to be as follows:

-   Same number of Channels, Slices and Timepoints
-   Same Data Type (8-bit, 16-bit, 32-bit or RGB)' %}

In the case that there would be many images open, the plugin does not pre-select any images.

{% include img src="hyperstacks-montage-example" width="400" caption="Example on RGB Stacks. Also works on multichannel, multislice, timepoints and any combination" %}

This plugin is useful when montaging multiple views or when montaging RGB datasets all in one go.

## Macro Recordable

Making use of the GenericDialog class, the plugin is macro-recordable.

```java
run("Multi Stack Montage...", "stack_1=Image1 stack_2=[Another Image] stack_3=Image3 rows=2 columns=2");
```

## Running from a Plugin

What you need to run this in a plugin is

```java
import ch.epfl.biop.StackMontage;
```

And then call the static method

```java
ImagePlus montaged_image = StackMontage.montageImages(ArrayList<ImagePlus> theimages, int nrows, int ncols);
```

You can have a look at this minimal plugin that runs StackMontage.

```java
import ij.*;
import ij.plugin.*;

// Required by StackMontage
import java.util.ArrayList;
import ch.epfl.biop.StackMontage;

/**
 * Short example on making hyperstack montages
 * @author Romain Guiet, Olivier Burri
 * @version 1.0
 */
public class My_Plugin implements PlugIn {

    public void run(String arg) {

        // Make some nice images
        ImagePlus imp = IJ.openImage("https://imagej.nih.gov/ij/images/confocal-series.zip");
        String imageName = imp.getTitle();

        // Recolor them
        ImagePlus imp1 = new Duplicator().run(imp, 1, 2, 1, 25, 1, 1);
        IJ.run(imp1, "Blue", "");
        imp1.setTitle(imageName+"c1Blue");
        
        ImagePlus imp2 = new Duplicator().run(imp1, 1, 2, 1, 25, 1, 1);
        imp2.setC(2);
        IJ.run(imp2, "Magenta", "");
        imp2.setTitle(imageName+"c1Blue_c2Magenta");
        
        ImagePlus imp3 = new Duplicator().run(imp2, 1, 2, 1, 25, 1, 1);
        imp3.setC(1);
        IJ.run(imp3, "Cyan", "");
        imp3.setTitle(imageName+"c1Cyan_c2Magenta");
        
        IJ.run(imp3, "RGB Color", "slices");
        IJ.run(imp2, "RGB Color", "slices");
        IJ.run(imp1, "RGB Color", "slices");
        IJ.run(imp, "RGB Color", "slices");



        // Montage Options
        int nrows = 2;
        int ncols = 2;
        
        // Prepare container for images
        ArrayList<ImagePlus> images = new ArrayList<ImagePlus>();
        
        // Add images to ArrayList for the montage
        images.add(imp);
        images.add(imp1);
        images.add(imp2);
        images.add(imp3);


        // Make the montage
        ImagePlus impr = StackMontage.montageImages(images, nrows, ncols);
        // Show the result
        impr.show();
    }

}
```

## Notes

The Dialog is limited to 10 elements so as not to make a window potentially larger than the monitor's vertical resolution. However, it is unlimited if calling it from the macro recorder.

You do not need to enter "\*None\*" as the last stack.
